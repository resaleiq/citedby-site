"""RES-3973: the classes of finding CitedBy's own crawl of citedby.eu raised on 24 Oct, kept from coming back (founder, 22 Oct: fix them and try not to cause them again).
Every URL in the sitemaps is read through the real server, as the crawler reads it:
  - status 200 and indexable (no noindex, canonical = its own address): crawl check noindex_in_sitemap, and a 301 in the sitemap;
  - <title> 15-65 characters, description 50-160, neither cut with an ellipsis or at a cut word: title_length, description_length (RES-3261: a length fix once cut titles mid-phrase);
  - JSON-LD on the page: schema_missing;
  - three or more question headings carry FAQPage: schema_faq_missing;
  - no host of /sitemap-backlinks.xml is a name the server redirects (www.<host>), thin or noindex: noindex_in_sitemap.
All English addresses are read; the other four languages are read every STRIDE-th host (the title and description wording of every host in every language is also tested without a render).
Run: python3 -m pytest -q test_res3973_crawl_classes.py"""
import html, http.client, json, os, re, sqlite3, tempfile, threading
os.environ.update(OPTIN_SECRET="x" * 40, BASE_URL="http://t", DATA_DIR=tempfile.mkdtemp())
import pytest
import backlinks as b
import backlinks_i18n as i
import proxy
import server

STRIDE = 9
srv = server.ThreadingHTTPServer(("127.0.0.1", 0), server.H)
threading.Thread(target=srv.serve_forever, daemon=True).start()
SITE = "https://citedby.eu"
PUB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")


def get(path):
    c = http.client.HTTPConnection("127.0.0.1", srv.server_port, timeout=30)
    try:
        c.request("GET", path)
        r = c.getresponse()
        return r.status, r.read().decode("utf-8", "replace"), dict(r.getheaders())
    finally:
        c.close()


def locs(xml):
    return re.findall(r"<loc>([^<]+)</loc>", xml)


def tags(h):
    t = re.search(r"<title>(.*?)</title>", h, re.S)
    d = re.search(r'<meta name="description" content="(.*?)"', h, re.S)
    robots = " ".join(re.findall(r'<meta name="robots" content="([^"]*)"', h))
    canon = re.search(r'<link rel="canonical" href="([^"]*)"', h)
    return (html.unescape(t.group(1)) if t else "", html.unescape(d.group(1)) if d else "", robots, canon.group(1) if canon else "")


def ld_types(h):
    out = []
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        d = json.loads(m)
        for n in (d if isinstance(d, list) else d.get("@graph", [d])):
            if isinstance(n, dict):
                out.append(n.get("@type"))
    return out


def questions(h):
    return [x for x in re.findall(r"<h[23][^>]*>(.*?)</h[23]>", h, re.S) if re.sub(r"<[^>]+>", "", x).strip().endswith(("?", "?"))]


def whole_phrase(s):
    """No ellipsis, no dangling separator: a cut title or description ends where a phrase ends."""
    s = s.strip()
    return not s.endswith(("…", "...", " |", " -", " –", ",", ":")) and "…" not in s and "..." not in s


def problems(url, h, status, headers):
    """What the crawl would flag on one sitemap URL."""
    out = []
    if status != 200:
        return [f"status {status}"]
    title, desc, robots, canon = tags(h)
    if "noindex" in (robots + headers.get("X-Robots-Tag", "")).lower():
        out.append("noindex")
    if canon and canon.rstrip("/") != url.rstrip("/"):
        out.append(f"canonical {canon}")
    if not 15 <= len(title) <= 65 or not whole_phrase(title):
        out.append(f"title {len(title)}: {title}")
    if not 50 <= len(desc) <= 160 or not whole_phrase(desc):
        out.append(f"description {len(desc)}: {desc}")
    if not ld_types(h):
        out.append("no JSON-LD")
    if len(questions(h)) >= 3 and "FAQPage" not in ld_types(h):
        out.append(f"{len(questions(h))} question headings, no FAQPage")
    return out


def test_static_sitemap_urls_are_clean():
    urls = [u for u in locs(open(os.path.join(PUB, "sitemap.xml"), encoding="utf-8").read()) if u.startswith(SITE)]
    assert len(urls) > 100
    bad = {}
    for u in urls:
        if proxy.ROUTES["GET"].fullmatch(u[len(SITE):] or "/"):  # served by the app container: the app's own tests and the live crawl read these
            continue
        s, h, hd = get(u[len(SITE):] or "/")
        p = problems(u, h, s, hd)
        if p:
            bad[u] = p
    assert not bad, json.dumps(dict(list(bad.items())[:15]), indent=1, ensure_ascii=False)


def test_sitemap_does_not_list_the_latest_alias_of_a_dated_page():
    """/data/ai-access-index says canonical = the dated run page: listing both is a mixed signal (crawl: noindex_in_sitemap)."""
    assert f"{SITE}/data/ai-access-index" not in locs(open(os.path.join(PUB, "sitemap.xml"), encoding="utf-8").read())


def test_backlinks_sitemap_hosts_are_their_own_address_and_indexable():
    xml = b.sitemap()
    seen = locs(xml)
    assert len(seen) > 20000
    thin = b.thin_hosts()
    for u in seen:
        host = u.rsplit("/", 1)[-1]
        if host in ("backlinks", "method"):
            continue
        assert b.norm(host) == host, f"{u}: the server sends this name to {b.norm(host)} with a 301"
        assert b.stored(host) not in thin, u
    assert not [h for h in b.hosts() if h.startswith("www.")]
    assert f"{SITE}/backlinks/www.cci.fr" not in seen and f"{SITE}/backlinks/cci.fr" in seen
    assert len(b.hosts()) == 5011


def test_www_host_of_the_data_has_its_page_at_the_address_without_www():
    """The data stores www.cci.fr; /backlinks/www.cci.fr redirects to /backlinks/cci.fr, which must then be the real page and not an empty "not in the data" one."""
    s, _, hd = get("/backlinks/www.cci.fr")
    assert s == 301 and hd["Location"] == "/backlinks/cci.fr"
    s, h, _ = get("/backlinks/cci.fr")
    assert s == 200 and "3,840 domains link to cci.fr" in html.unescape(h)


def test_backlinks_every_english_address_in_the_sitemap_is_clean():
    bad = {}
    for u in locs(b.sitemap()):
        if "/backlinks" not in u or any(u.startswith(f"{SITE}/{lg}/") for lg in ("fr", "de", "es", "nl")):
            continue
        s, h, hd = get(u[len(SITE):])
        p = problems(u, h, s, hd)
        if p:
            bad[u] = p
    assert not bad, f"{len(bad)} flagged: " + json.dumps(dict(list(bad.items())[:10]), indent=1, ensure_ascii=False)


def test_backlinks_other_languages_sample_is_clean():
    allu = [u for u in locs(b.sitemap()) if any(u.startswith(f"{SITE}/{lg}/backlinks") for lg in ("fr", "de", "es", "nl"))]
    bad = {}
    for u in allu[::STRIDE] + [u for u in allu if u.endswith(("/backlinks", "/backlinks/method"))]:
        s, h, hd = get(u[len(SITE):])
        p = problems(u, h, s, hd)
        if p:
            bad[u] = p
    assert not bad, f"{len(bad)} flagged: " + json.dumps(dict(list(bad.items())[:10]), indent=1, ensure_ascii=False)


def test_title_and_description_wording_fits_for_every_host_and_language():
    """No render: the title and description chosen for every host of the shipped set in every language fit the crawl's limits whole (never an ellipsis)."""
    rows = b._q("select domain, referring_domains from dom where tier in (1,2)")
    assert len(rows) > 5000
    n_one = []
    for lg in i.LANGS:
        t = i.T[lg]
        for host, n in rows:
            for title in (b.fit_title(t, host, "host_title", "host_title2"), b.fit_title(t, host, "nis_title", "host_title2")):
                assert 15 <= len(title) <= 65 and whole_phrase(title), (lg, host, title)
            for key, kw in (("desc_n", dict(n=b.fmt(10 ** 6 - 1, lg))), ("desc_n_one", {})):
                d = b.fit_desc(t, key, host=host, label=t["graph_label"], **kw)
                assert 50 <= len(d) <= 160 and d.rstrip().endswith(".") and whole_phrase(d), (lg, host, d)
        for k in ("index_title", "method_title"):
            assert 15 <= len(t[k]) <= 65 and whole_phrase(t[k]), (lg, k, t[k])


def test_fit_title_never_cuts():
    t = i.T["en"]
    assert b.fit_title(t, "a.eu", "host_title", "host_title2") == "Who links to a.eu? Referring domains | CitedBy"
    long = "x" * 40 + ".example.com"
    got = b.fit_title(t, long, "host_title", "host_title2")
    assert got == f"{long} backlinks | CitedBy" or got == f"{long} | CitedBy"
    assert len(got) <= 65 and "…" not in got
    mid = "k" * 24 + ".eu"
    assert b.fit_title(t, mid, "host_title", "host_title2") == f"Who links to {mid}? | CitedBy"


def test_blog_questions_with_three_headings_have_faq_markup():
    """The crawl flagged /blog/ai-crawler-check-in-ci: four question headings and no FAQPage. Every built article with three or more has the markup."""
    bad = []
    for root, _, files in os.walk(os.path.join(PUB, "blog")):
        for f in files:
            if not f.endswith(".html"):
                continue
            h = open(os.path.join(root, f), encoding="utf-8").read()
            if len(questions(h)) >= 3 and "FAQPage" not in ld_types(h):
                bad.append(os.path.join(root, f)[len(PUB):])
    assert not bad, bad
