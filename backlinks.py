"""RES-3699 module 2: /backlinks and /backlinks/<host>, who links to a site, from Common Crawl's public domain web graph (job and method: RES-3703, seo-intel/backlinks/METHOD.md).
Served at request time from the full table when the host mounts it at /backlinks/backlinks.sqlite (RES-3706: every domain the job kept, 264,824; tier 3 = on demand, noindex),
else from the 5,011-host cut baked into the image (data/backlinks.sqlite, tools/build_backlinks_db.py: our sites, rivals and the top 5,000 EU-ccTLD domains). English only for now.
A host outside the file gets a "not in the set" page (noindex), never a zero. Standard library only."""
import html, json, os, re, sqlite3
from urllib.parse import quote

E = html.escape
HERE = os.path.dirname(os.path.abspath(__file__))
DB_BAKED = os.path.join(HERE, "data", "backlinks.sqlite")
DB_MOUNT = "/backlinks/backlinks.sqlite"  # read-only bind mount from /opt/citedby/backlinks (recreate.sh, deploy-citedby-site); built by seo-intel/backlinks/serve_db.py
DB = os.environ.get("BACKLINKS_DB") or None  # explicit override (tests, rollback); None = decided per request by _db()
COVER_CUT = "our own sites, SEO tools and the most-linked sites under .eu, .fr, .de, .es, .nl, .it, .pt and .be"
COVER_FULL = ("our own sites, SEO tools and every domain under a European country-code domain (.eu, .fr, .de, .es, .nl, .it, .pt, .be, .at, .pl, .se, .uk and 16 more) "
              "that has at least 100 referring domains")
HOST = re.compile(r"^(?=.{4,253}$)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,24}$")
OWN_ZERO = {"citedby.eu", "hexaciv.com", "civiqpass.com", "revalx.eu"}  # METHOD.md sanity check: the graph saw none of them
GRAPH, GRAPH_LABEL, GRAPH_COVER = "cc-main-2026-aug-sep-oct", "Aug-Oct 2026", "2026-08/2026-10"
METHOD = ("Source: Common Crawl's public domain web graph, built from three monthly crawls ({d} domains, {l} links). We count distinct linking domains, not pages, "
          "and do not use any third-party backlink index. Common Crawl samples the web, so counts are lower than a full index such as Ahrefs or Semrush; use them to compare sites "
          "and spot big referrers, not as an exact total. Updated each quarter, last graph: " + GRAPH + ". Nofollow and link position are not in this data.")


def _db():
    """The override, else the mounted full table when the file is there, else the baked cut. Looked up per request, so renaming the file in or out of
    /opt/citedby/backlinks switches the table with no restart (and `mv backlinks.sqlite backlinks.sqlite.off` is the instant rollback)."""
    return DB or (DB_MOUNT if os.path.exists(DB_MOUNT) else DB_BAKED)


def _q(sql, args=()):
    c = sqlite3.connect("file:%s?mode=ro" % _db(), uri=True)
    try:
        return c.execute(sql, args).fetchall()
    finally:
        c.close()


def norm(raw):
    v = re.sub(r"^[a-z]+://", "", (raw or "").strip().lower()).split("/")[0].split("?")[0].split("#")[0].split(":")[0]
    v = re.sub(r"^www\.", "", v)
    return v if HOST.match(v) else ""


def meta():
    return dict(_q("select k, v from meta"))


def hosts():
    return [r[0] for r in _q("select domain from dom where tier in (1,2) order by tier, referring_domains desc")]


def tier(host):
    """1 our sites and rivals, 2 the sitemap set, 3 the on-demand rest (served, noindex); 0 = not in the table."""
    r = _q("select tier from dom where domain=?", (host,))
    return r[0][0] if r else 0


def _cover():
    """What the loaded table covers, in words: the cut and the full table say different things."""
    return COVER_FULL if _q("select 1 from dom where tier=3 limit 1") else COVER_CUT


def lookup(host):
    """(referring_domains, [(rank, referrer, referrer_inlinks)]) or None when the host is not in the shipped set."""
    r = _q("select referring_domains from dom where domain=?", (host,))
    if not r:
        return (0, []) if host in OWN_ZERO else None
    return r[0][0], _q("select rank, referrer, referrer_inlinks from bl where domain=? order by rank", (host,))


def _shell(title, desc, canonical, body, noindex=False, ld=None):
    ld_tag = '<script type="application/ld+json">%s</script>' % json.dumps(ld).replace("</", "<\\/") if ld else ""
    robots = '<meta name="robots" content="noindex,follow">' if noindex else ""
    return f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">{robots}
<link rel="canonical" href="https://citedby.eu{canonical}">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="https://citedby.eu{canonical}"><meta property="og:type" content="website"><meta property="og:locale" content="en_IE">
<meta name="theme-color" content="#0F1B2D">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/saas.css"><link rel="stylesheet" href="/doc.css?v=bbef868a"><link rel="stylesheet" href="/data.css?v=08430f8c">
{ld_tag}
</head><body class="cb dc dp">
<a class="sr" href="#main">Skip to content</a>
<header class="topbar"><div class="in"><a class="mark" href="/"><i></i>CitedBy</a><nav aria-label="Main"><a class="opt" href="/#checks">What we check</a><a href="/plans">Pricing</a><a href="/blog">Guides</a><a class="opt" href="/data">Data</a></nav><a class="signin" href="/signin?next=%2Fapp.html">Sign in</a><a class="btn sm go" href="/app.html#/new">Audit a site</a></div></header>
<main id="main" class="wide">
{body}
</main>
''' + _footer()


_FOOT = []


def _footer():
    if not _FOOT:
        t = open(os.path.join(HERE, "public", "data", "launch-crawl-2026-10.html"), encoding="utf-8").read()
        _FOOT.append(t[t.index("<footer>"):])
    return _FOOT[0]


def _form(value=""):
    return (f'<form class="bl-form" action="/backlinks" method="get" role="search"><label for="bl-host">Domain</label> '
            f'<input id="bl-host" name="host" type="text" inputmode="url" autocomplete="off" placeholder="example.com" value="{E(value)}" required maxlength="253"> '
            f'<button class="btn p" type="submit">Who links to it?</button></form>')


def _cta(host=None):
    u = ("/?url=%s&" % quote(host) if host else "/?") + "utm_source=citedby_backlinks&utm_medium=free_tool&utm_campaign=backlinks"
    name = host or "your site"
    return (f'<section class="cta"><h2>Can search engines and AI assistants read {E(name)}?</h2><p class="lede">Links get a site noticed. Access and clean markup get it cited. '
            f'We crawl your site up to your plan\'s page limit and give you the exact fix for each issue. Free check first; full audits from €9, 14-day money-back guarantee.</p>'
            f'<div class="actions"><a class="btn p" href="{E(u)}">Check {E(name)} free</a></div></section>')


def index_page(msg=""):
    m = meta()
    top = _q("select domain, referring_domains from dom where tier=2 order by referring_domains desc limit 24")
    li = "".join(f'<li><a href="/backlinks/{E(d)}">{E(d)}</a> <span class="src">({n:,})</span></li>' for d, n in top)
    note = f'<p class="ans">{E(msg)}</p>' if msg else ""
    body = f'''<p class="crumb"><a href="/">CitedBy</a> / Backlinks</p>
<h1>Who links to a website? Free referring-domain lookup</h1>
{note}<p class="ans">Type a domain to see the 20 strongest domains that link to it in Common Crawl's latest open web graph, with the method shown. No sign-up.</p>
{_form()}
<section><h2>Most-linked EU sites in the data</h2><ul>{li}</ul>
<p class="src">Count in brackets: referring domains. The lookup covers {_q("select count(*) from dom")[0][0]:,} domains: {_cover()}.</p></section>
<section><h2>Method and limits</h2><p>{E(METHOD.format(d=f"{int(m['domains']):,}", l=f"{int(m['links']):,}"))}</p></section>
{_cta()}'''
    return _shell("Who links to a website? Free referring-domain lookup | CitedBy", "Free lookup of the strongest domains linking to a site, from Common Crawl's open web graph. Method and limits shown.", "/backlinks", body)


def host_page(host):
    """(status, html). 200 for a host in the set; 200 noindex for a valid host outside it."""
    got = lookup(host)
    m = meta()
    if got is None:
        body = f'''<p class="crumb"><a href="/">CitedBy</a> / <a href="/backlinks">Backlinks</a> / {E(host)}</p>
<h1>Who links to {E(host)}?</h1>
<p class="ans">{E(host)} is not in the set we have loaded yet. The lookup covers {_cover()}. It does not mean the site has no links. The set grows with each quarterly graph.</p>
{_form(host)}{_cta(host)}'''
        return 200, _shell(f"Who links to {host}? Not in the data yet | CitedBy", f"{host} is not in CitedBy's backlink data set yet.", f"/backlinks/{host}", body, noindex=True)
    n, rows = got
    d, l = f"{int(m['domains']):,}", f"{int(m['links']):,}"
    if n == 0:
        ans = f"Common Crawl found no linking domains for {host}. New or small sites are often missing; it does not mean you have none."
        table = ""
    else:
        ans = f"{n:,} domains link to {host} in the latest Common Crawl web graph ({GRAPH_LABEL}). Below are the {len(rows)} strongest. Strength is how many domains link to that referrer."
        known = {x[0] for x in _q("select domain from dom where tier <= 2 and domain in (%s)" % ",".join("?" * len(rows)), [r[1] for r in rows])}  # links stay inside the indexable set
        link = lambda ref: f'<a href="/backlinks/{E(ref)}">{E(ref)}</a>' if ref in known else E(ref)
        tr = "".join(f'<tr><td data-label="#">{r}</td><td data-label="Referring domain">{link(ref)}</td><td class="n" data-label="Strength">{inl:,}</td></tr>' for r, ref, inl in rows)
        table = f'<section><h2>Strongest referring domains</h2><div class="tw"><table><thead><tr><th>#</th><th>Referring domain</th><th class="n">Domains linking to it</th></tr></thead><tbody>{tr}</tbody></table></div></section>'
    desc = (f"{n:,} domains link to {host} in Common Crawl's open web graph ({GRAPH_LABEL}). The 20 strongest, with the method." if n else f"Common Crawl found no linking domains for {host}. What that means and how the data is built.")
    ld = {"@context": "https://schema.org", "@type": "Dataset", "name": f"Referring domains of {host} (Common Crawl web graph {GRAPH})", "description": desc,
          "url": f"https://citedby.eu/backlinks/{host}", "inLanguage": "en", "isAccessibleForFree": True, "license": "https://commoncrawl.org/terms-of-use",
          "creator": {"@type": "Organization", "name": "Common Crawl", "url": "https://commoncrawl.org"}, "temporalCoverage": GRAPH_COVER,
          "publisher": {"@type": "Organization", "name": "CitedBy", "url": "https://citedby.eu"}, "dateModified": m["read_on"],
          "isBasedOn": {"@type": "Dataset", "name": f"Common Crawl domain web graph {GRAPH}", "url": "https://commoncrawl.org/web-graphs"}}
    body = f'''<p class="crumb"><a href="/">CitedBy</a> / <a href="/backlinks">Backlinks</a> / {E(host)}</p>
<h1>Who links to {E(host)}?</h1>
<p class="ans">{E(ans)}</p>
<p class="src">Common Crawl graph {GRAPH} · read {E(m["read_on"])} · {n:,} referring domains</p>
{table}
<section><h2>Look up another domain</h2>{_form()}</section>
<section><h2>Method and limits</h2><p>{E(METHOD.format(d=d, l=l))}</p></section>
{_cta(host)}'''
    return 200, _shell(f"Who links to {host}? Referring domains from open data | CitedBy", desc, f"/backlinks/{host}", body, noindex=tier(host) >= 3, ld=ld)  # tier 3: on demand, not offered to search engines (METHOD.md)


def sitemap():
    ds = hosts()
    m = meta()
    u = "".join(f"<url><loc>https://citedby.eu/backlinks/{d}</loc><lastmod>{m['read_on']}</lastmod></url>" for d in ds)
    return ('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
            f'<url><loc>https://citedby.eu/backlinks</loc><lastmod>{m["read_on"]}</lastmod></url>{u}</urlset>')
