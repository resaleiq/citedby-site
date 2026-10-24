"""RES-3699 module 2: /backlinks and /backlinks/<host>, who links to a site, from Common Crawl's public domain web graph (job and method: RES-3703, seo-intel/backlinks/METHOD.md).
Served at request time from data/backlinks.sqlite (tools/build_backlinks_db.py: our sites, rivals and the top 5,000 EU-ccTLD domains).
RES-3749: the same pages in fr, de, es and nl under /fr/backlinks ... (words in backlinks_i18n.py). A host outside the file gets a "not in the set" page (noindex), never a zero.
Standard library only."""
import html, json, os, re, sqlite3
from urllib.parse import quote

import langroutes
from backlinks_i18n import HOME, LANGS, NAMES, T, UI, fmt, plural_key, prefix

E = html.escape
HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.environ.get("BACKLINKS_DB", os.path.join(HERE, "data", "backlinks.sqlite"))
HOST = re.compile(r"^(?=.{4,253}$)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,24}$")
ROUTE = re.compile(r"^(?:/(fr|de|es|nl))?/backlinks(?:/(.*))?$")  # group 1: language prefix, group 2: the host part (None = the lookup page)
LINK_DENY = re.compile(r"porn|xxx|sex|escort|casino|bet(?!a|ter|ween|s)|poker|viagra|cialis|pharma|loan|crypto|slot|lotto|gambl|adult|hentai|nude|dating|vape|cbd|payday")  # RES-3801 (open): a referrer with one of these words is listed as text, never linked or featured; the SEO lead decides whether it is hidden
HIDE_ADULT = frozenset(l.strip() for l in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "backlinks-hide-adult.txt"), encoding="utf-8")
                       if l.strip() and not l.startswith("#"))  # RES-3819 (decision RES-3801 B): adult-content referrers left out of every list; exact host match on the stored name, never a keyword rule
OWN_ZERO = {"citedby.eu", "hexaciv.com", "civiqpass.com", "revalx.eu"}  # METHOD.md sanity check: the graph saw none of them
GRAPH, GRAPH_COVER = "cc-main-2026-aug-sep-oct", "2026-08/2026-10"
OG = {**langroutes.OG_LOCALE, "en": "en_IE"}  # English keeps the og:locale it was published with


def _q(sql, args=()):
    c = sqlite3.connect("file:%s?mode=ro" % DB, uri=True)
    try:
        return c.execute(sql, args).fetchall()
    finally:
        c.close()


FULL_DB = os.environ.get("BACKLINKS_FULL_DB", "/backlinks/backlinks.sqlite")  # RES-3749 part C: Casa's table for every .eu / EU / UK country-domain site with 100+ referring domains, mounted read-only (RES-3706)
_FULL = {}  # file version -> {"n", "top"} or None: one check per version of the file, so a renamed-in file is picked up without a restart


def _qf(sql, args=()):
    """Rows from the full table, or None when the file is missing, half written or not ours: the pages then use the shipped set only."""
    try:
        c = sqlite3.connect("file:%s?mode=ro" % FULL_DB, uri=True, timeout=2)
    except sqlite3.Error:
        return None
    try:
        return c.execute(sql, args).fetchall()
    except sqlite3.Error:
        return None
    finally:
        c.close()


def full_info():
    """{"n": domains in the full table, "top": its 24 most-linked (domain, referring_domains)}, or None when there is no usable file."""
    try:
        st = os.stat(FULL_DB)
    except OSError:
        return None
    key = (FULL_DB, st.st_mtime_ns, st.st_size, st.st_ino)
    if key not in _FULL:
        n = _qf("select count(*) from dom")
        top = _qf("select domain, referring_domains from dom order by referring_domains desc, domain limit 80") if n and n[0][0] else None
        top = [r for r in top if not LINK_DENY.search(r[0])][:24] if top is not None else None
        ok = top is not None and _qf("select 1 from bl limit 1") is not None
        _FULL.clear()
        _FULL[key] = {"n": n[0][0], "top": top} if ok else None
    return _FULL[key]


def norm(raw):
    v = re.sub(r"^[a-z]+://", "", (raw or "").strip().lower()).split("/")[0].split("?")[0].split("#")[0].split(":")[0]
    v = re.sub(r"^www\.", "", v)
    return v if HOST.match(v) else ""


def meta():
    return dict(_q("select k, v from meta"))


def hosts():
    return [r[0] for r in _q("select domain from dom where tier in (1,2) order by tier, referring_domains desc")]


_COMMON = []  # (file version, frozenset): the referrers folded into one line (RES-3899)


def commons():
    """Referrers that are among the strongest for at least COMMON_PCT % of the hosts in the set (google.com, wikipedia.org, blogspot.com ...): a page folds them into one line and lists its own. Empty when the file has no `common` table."""
    try:
        st = os.stat(DB)
    except OSError:
        return frozenset()
    key = (st.st_mtime_ns, st.st_size)
    if not _COMMON or _COMMON[0] != key:
        try:
            got = frozenset(r[0] for r in _q("select referrer from common"))
        except sqlite3.Error:
            got = frozenset()
        _COMMON[:] = [key, got]
    return _COMMON[1]


_THIN = []  # (file version, frozenset)


def thin_hosts():
    """Hosts of the shipped set whose page is noindex and out of the sitemap: too few referrers of their own once the common ones are folded, or the same list as a stronger host (a link network). Empty without a `thin` table."""
    try:
        st = os.stat(DB)
    except OSError:
        return frozenset()
    key = (st.st_mtime_ns, st.st_size)
    if not _THIN or _THIN[0] != key:
        try:
            got = frozenset(r[0] for r in _q("select domain from thin"))
        except sqlite3.Error:
            got = frozenset()
        _THIN[:] = [key, got]
    return _THIN[1]


SHOWN, FOLD_MAX = 30, 10  # rows in the table; names in the folded line


def split(host):
    """(referring_domains, rows, folded) or None. rows = [(rank, referrer, referrer_inlinks)]: up to 30 of the host's own strongest referrers once adult-content hosts (RES-3819) and the common referrers are taken out, ranks closed up;
    folded = up to 10 common referrers of this host, strongest first. A host in the shipped set (indexable pages) first, else the full table (on-demand pages), else None."""
    r = _q("select referring_domains from dom where domain=?", (host,))
    if r:
        n, got = r[0][0], _q("select referrer, referrer_inlinks from bl where domain=? order by rank", (host,))
    elif host in OWN_ZERO:
        return 0, [], []
    elif not full_info():
        return None
    else:
        r = _qf("select referring_domains from dom where domain=?", (host,))
        if not r:
            return None
        n, got = r[0][0], _qf("select referrer, referrer_inlinks from bl where domain=? order by referrer_inlinks desc, referrer", (host,)) or []
    com = commons()
    got = [(ref, inl) for ref, inl in got if ref not in HIDE_ADULT]
    own = [(ref, inl) for ref, inl in got if ref not in com]
    return n, [(i, ref, inl) for i, (ref, inl) in enumerate(own[:SHOWN], 1)], [ref for ref, _ in got if ref in com][:FOLD_MAX]


def lookup(host):
    """(referring_domains, [(rank, referrer, referrer_inlinks)]) for a host in the shipped set (indexable pages), else in the full table (on-demand pages), else None."""
    got = split(host)
    return None if got is None else got[:2]


def curated(host):
    """True for the shipped set (own sites, SEO tools, the top .eu/.fr/.de/.es/.nl/.it/.pt/.be domains): those pages are indexable. Everything else comes from the full table and is noindex."""
    return host in OWN_ZERO or bool(_q("select 1 from dom where domain=?", (host,)))


def _alts(tail):
    """hreflang alternates for one page: every language, and English as x-default."""
    base = "https://citedby.eu"
    return "".join(f'<link rel="alternate" hreflang="{l}" href="{base}{prefix(l)}{tail}">' for l in LANGS) + f'<link rel="alternate" hreflang="x-default" href="{base}{tail}">'


_TOP_EN = ('<a class="sr" href="#main">Skip to content</a>\n'
           '<header class="topbar"><div class="in"><a class="mark" href="/"><i></i>CitedBy</a><nav aria-label="Main"><a class="opt" href="/#checks">What we check</a><a href="/plans">Pricing</a>'
           '<a href="/blog">Guides</a><a class="opt" href="/data">Data</a></nav><a class="signin" href="/signin?next=%2Fapp.html">Sign in</a><a class="btn sm go" href="/app.html#/new">Audit a site</a></div></header>')


def _topbar(lg):
    if lg == "en":
        return _TOP_EN
    t = UI[lg]  # the same masthead tools/docshell.localize gives the other reading pages
    return (f'<a class="sr" href="#main">{t["skip"]}</a>\n<header class="topbar"><div class="in"><a class="mark" href="{t["home"]}"><i></i>CitedBy</a>'
            f'<nav aria-label="{t["main"]}"><a class="opt" href="{t["home"]}#checks">{t["check"]}</a><a href="{t["plans_h"]}">{t["plans"]}</a><a href="{t["blog_h"]}">{t["blog"]}</a>'
            f'<a class="opt" href="/data">{t["data"]}</a></nav><a class="signin" href="/signin?next=%2Fapp.html">{t["signin"]}</a><a class="btn sm go" href="/app.html#/new">{t["cta"]}</a></div></header>')


def _shell(lg, title, desc, canonical, body, noindex=False, ld=None, alts=""):
    ld_tag = '<script type="application/ld+json">%s</script>' % json.dumps(ld, ensure_ascii=False).replace("</", "<\\/") if ld else ""
    robots = '<meta name="robots" content="noindex,follow">' if noindex else ""
    return f'''<!doctype html>
<html lang="{lg}"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">{robots}
<link rel="canonical" href="https://citedby.eu{canonical}">{alts}
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="https://citedby.eu{canonical}"><meta property="og:type" content="website"><meta property="og:locale" content="{OG[lg]}">
<meta name="theme-color" content="#0F1B2D">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/saas.css"><link rel="stylesheet" href="/doc.css?v=bbef868a"><link rel="stylesheet" href="/data.css?v=08430f8c">
<style>.dc .cta a.btn:not(.p){{background:#fff;color:var(--navy);border:2px solid var(--navy)}}.bl-form{{display:flex;flex-wrap:wrap;align-items:center;gap:8px 12px}}.bl-form .fld{{flex:1 1 220px;max-width:420px}}@media(max-width:480px){{.langs{{min-height:3em}}}}</style>
{ld_tag}
</head><body class="cb dc dp">
{_topbar(lg)}
<main id="main" class="wide">
{body}
</main>
''' + _footer(lg)


_FOOT = []


def _footer(lg="en"):
    if lg != "en":
        t = UI[lg]
        return (f'<footer><div class="w"><span>© 2026 CitedBy · <a href="mailto:hello@citedby.eu">hello@citedby.eu</a></span><a href="{t["plans_h"]}">{t["plans"]}</a><a href="{t["blog_h"]}">{t["blog"]}</a>'
                f'<a href="/data">{t["data"]}</a><a href="/methodology">{t["method"]}</a><a href="/{lg}/about">{t["about"]}</a><a href="/{lg}/terms">{t["terms"]}</a><a href="/{lg}/privacy">{t["privacy"]}</a>'
                f'<a href="/{lg}/refund">{t["refund"]}</a><a href="/contact">{t["contact"]}</a><a href="/legal">{t["legal"]}</a></div></footer>\n</body></html>\n')
    if not _FOOT:
        t = open(os.path.join(HERE, "public", "data", "launch-crawl-2026-10.html"), encoding="utf-8").read()
        _FOOT.append(t[t.index("<footer>"):])
    return _FOOT[0]


def _switch(lg, tail):
    """The same page in each language, as plain links (hreflang tells search engines; this tells people)."""
    links = " · ".join(f'<a href="{prefix(l)}{tail}" hreflang="{l}" lang="{l}"' + (' aria-current="true"' if l == lg else "") + f">{NAMES[l]}</a>" for l in LANGS)
    return f'<p class="src langs">{E(T[lg]["lang_label"])} {links}</p>'


def _crumb(lg, *rest):
    t, p = T[lg], prefix(lg)
    return f'<p class="crumb"><a href="{HOME[lg]}">{E(t["crumb_home"])}</a> / ' + " / ".join(rest or (E(t["crumb_bl"]),)) + "</p>"


def _form(lg, value="", primary=False):
    """The lookup form. Its button is the filled one only on the lookup page; on a host page the free-check link below is the one primary."""
    t = T[lg]
    return (f'<form class="bl-form" action="{prefix(lg)}/backlinks" method="get" role="search"><label for="bl-host">{E(t["form_label"])}</label> '
            f'<input class="fld" id="bl-host" name="host" type="text" inputmode="url" autocomplete="off" placeholder="{E(t["form_ph"])}" value="{E(value)}" required maxlength="253"> '
            f'<button class="btn{" p" if primary else ""}" type="submit">{E(t["form_btn"])}</button></form>')


def _cta(lg, host=None, primary=True):
    """The free-check call to action. The filled button on a host page; on the lookup page the lookup button is the primary and this one is the outline style."""
    t = T[lg]
    u = HOME[lg] + ("?url=%s&" % quote(host) if host else "?") + "utm_source=citedby_backlinks&utm_medium=free_tool&utm_campaign=backlinks"
    name = host or t["cta_name"]
    return (f'<section class="cta"><h2>{E(t["cta_h2"].format(name=name))}</h2><p class="lede">{E(t["cta_lede"])}</p>'
            f'<div class="actions"><a class="btn{" p" if primary else ""}" href="{E(u)}">{E(t["cta_btn"].format(name=name))}</a></div></section>')


def _method(lg, m):
    return E(T[lg]["method"].format(d=fmt(int(m["domains"]), lg), l=fmt(int(m["links"]), lg), graph=GRAPH))


def _method_link(lg):
    """RES-3899: the method text lives once, on /backlinks/method; every other page says so in one line."""
    link = '<a href="%s/backlinks/method">' % prefix(lg)
    return f'<p class="src">{E(T[lg]["method_link"]).format(a=link, z="</a>")}</p>'


def method_page(lg="en"):
    t, m, p = T[lg], meta(), prefix(lg)
    pct = m.get("common_pct")
    fold = f'<p>{E(t["method_fold"].format(pct=pct, n=fmt(int(m["common_hosts"]), lg)))}</p>' if pct and m.get("common_hosts") else ""
    body = f'''{_crumb(lg, f'<a href="{p}/backlinks">{E(t["crumb_bl"])}</a>', E(t["method_h2"]))}
{_switch(lg, "/backlinks/method")}
<h1>{E(t["method_h1"])}</h1>
<p class="ans">{_method(lg, m)}</p>
{fold}
<section><h2>{E(t["another_h2"])}</h2>{_form(lg, primary=True)}</section>
{_cta(lg, primary=False)}'''
    return _shell(lg, t["method_title"], t["method_desc"], f"{p}/backlinks/method", body, alts=_alts("/backlinks/method"))


def index_page(msg="", lg="en"):
    t, m, p = T[lg], meta(), prefix(lg)
    full = full_info()
    top = full["top"] if full else _q("select domain, referring_domains from dom where tier=2 order by referring_domains desc limit 24")
    note_text = t["top_note_full"].format(n=fmt(full["n"], lg)) if full else t["top_note"].format(n=fmt(len(hosts()), lg))
    li = "".join(f'<li><a href="{p}/backlinks/{E(d)}">{E(d)}</a> <span class="src">({fmt(n, lg)})</span></li>' for d, n in top)
    note = f'<p class="ans">{E(msg)}</p>' if msg else ""
    body = f'''{_crumb(lg)}
{_switch(lg, "/backlinks")}
<h1>{E(t["index_h1"])}</h1>
{note}<p class="ans">{E(t["index_ans"])}</p>
{_form(lg, primary=True)}
<section><h2>{E(t["top_h2"])}</h2><ul>{li}</ul>
<p class="src">{E(note_text)}</p></section>
{_method_link(lg)}
{_cta(lg, primary=False)}'''
    return _shell(lg, t["index_title"], t["index_desc"], f"{p}/backlinks", body, alts=_alts("/backlinks"))


def host_page(host, lg="en"):
    """(status, html). 200 for a host in the set; 200 noindex for a valid host outside it."""
    got = split(host)
    t, m, p = T[lg], meta(), prefix(lg)
    tail = f"/backlinks/{host}"
    crumb = _crumb(lg, f'<a href="{p}/backlinks">{E(t["crumb_bl"])}</a>', E(host))
    if got is None:
        full = full_info()
        nis = t["nis_ans_full"].format(host=host, n=fmt(full["n"], lg)) if full else t["nis_ans"].format(host=host)
        body = f'''{crumb}
{_switch(lg, tail)}
<h1>{E(t["host_h1"].format(host=host))}</h1>
<p class="ans">{E(nis)}</p>
{_form(lg, host)}{_cta(lg, host)}'''
        return 200, _shell(lg, t["nis_title"].format(host=host), t["nis_desc"].format(host=host), p + tail, body, noindex=True)
    n, rows, folded = got
    one = plural_key(n) == "one"
    if n == 0:
        ans, table, desc = t["ans_0"].format(host=host), "", t["desc_0"].format(host=host)
    else:
        ans = t["ans_n_one" if one else "ans_n"].format(n=fmt(n, lg), host=host, label=t["graph_label"], k=len(rows))
        desc = t["desc_n_one" if one else "desc_n"].format(n=fmt(n, lg), host=host, label=t["graph_label"])
        refs, marks = [r[1] for r in rows], ",".join("?" * len(rows))
        known = {x[0] for x in _q("select domain from dom where domain in (%s)" % marks, refs)}
        if full_info():  # a referrer that has a page in either file is a link
            known |= {x[0] for x in (_qf("select domain from dom where domain in (%s)" % marks, refs) or [])}
        known = {k for k in known if not LINK_DENY.search(k)}  # gambling and adult names stay text (RES-3801)
        link = lambda ref: f'<a href="{p}/backlinks/{E(ref)}">{E(ref)}</a>' if ref in known else E(ref)
        tr = "".join(f'<tr><td data-label="{E(t["dl_rank"])}">{r}</td><td data-label="{E(t["dl_ref"])}">{link(ref)}</td><td class="n" data-label="{E(t["dl_str"])}">{fmt(inl, lg)}</td></tr>' for r, ref, inl in rows)
        table = (f'<section><h2>{E(t["table_h2"])}</h2><div class="tw"><table><thead><tr><th>{E(t["th_rank"])}</th><th>{E(t["th_ref"])}</th><th class="n">{E(t["th_str"])}</th></tr></thead>'
                 f'<tbody>{tr}</tbody></table></div>'
                 + (f'<p class="src">{E(t["folded"].format(list=", ".join(folded)))}</p>' if folded else "") + "</section>")
    on_demand = not curated(host) or host in thin_hosts()  # from the full table, or a page that says what a stronger host's says (RES-3899): useful to a visitor, not a page we ask search engines to index
    ld = None if on_demand else {"@context": "https://schema.org", "@type": "Dataset", "name": t["ld_name"].format(host=host, graph=GRAPH), "description": desc,
          "url": f"https://citedby.eu{p}{tail}", "inLanguage": lg, "isAccessibleForFree": True, "license": "https://commoncrawl.org/terms-of-use",
          "creator": {"@type": "Organization", "name": "Common Crawl", "url": "https://commoncrawl.org"}, "temporalCoverage": GRAPH_COVER,
          "publisher": {"@type": "Organization", "name": "CitedBy", "url": "https://citedby.eu"}, "dateModified": m["read_on"],
          "isBasedOn": {"@type": "Dataset", "name": f"Common Crawl domain web graph {GRAPH}", "url": "https://commoncrawl.org/web-graphs"}}
    body = f'''{crumb}
{_switch(lg, tail)}
<h1>{E(t["host_h1"].format(host=host))}</h1>
<p class="ans">{E(ans)}</p>
<p class="src">{E(t["src_line"].format(graph=GRAPH, date=m["read_on"], n=fmt(n, lg)))}</p>
{table}
<section><h2>{E(t["another_h2"])}</h2>{_form(lg)}</section>
{_method_link(lg)}
{_cta(lg, host)}'''
    return 200, _shell(lg, t["host_title"].format(host=host), desc, p + tail, body, noindex=on_demand, ld=ld, alts="" if on_demand else _alts(tail))


_SITEMAP = []  # (mtime of the data file, xml)


def sitemap():
    """Every language: the lookup page and one page per host in the set (5 x 5,012 URLs, under the 50,000 limit)."""
    mt = os.path.getmtime(DB)
    if _SITEMAP and _SITEMAP[0] == mt:
        return _SITEMAP[1]
    thin = thin_hosts()
    ds, m = [h for h in hosts() if h not in thin], meta()
    u = "".join(f"<url><loc>https://citedby.eu{prefix(l)}/backlinks</loc><lastmod>{m['read_on']}</lastmod></url>"
                f"<url><loc>https://citedby.eu{prefix(l)}/backlinks/method</loc><lastmod>{m['read_on']}</lastmod></url>"
                + "".join(f"<url><loc>https://citedby.eu{prefix(l)}/backlinks/{d}</loc><lastmod>{m['read_on']}</lastmod></url>" for d in ds) for l in LANGS)
    xml = '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + u + "</urlset>"
    _SITEMAP[:] = [mt, xml]
    return xml
