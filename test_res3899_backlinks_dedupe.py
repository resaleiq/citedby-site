"""RES-3899: /backlinks/<host> pages no longer read 60% the same. The method text lives once (/backlinks/method), referrers that most hosts have are folded into one line, and a page that says what a stronger host's says
(a short list, or the same list: a link network) is noindex and out of the sitemap. QA's near-duplicate check of the live pages flagged 370 of 1,000 crawled pages.
Run: python3 -m pytest -q test_res3899_backlinks_dedupe.py"""
import html, http.client, itertools, os, re, sqlite3, statistics, tempfile, threading
os.environ.update(OPTIN_SECRET="x" * 40, BASE_URL="http://t", DATA_DIR=tempfile.mkdtemp())
import pytest
import backlinks as b
import backlinks_i18n as i
import server

LOCALES = ("en", "fr", "de", "es", "nl")
srv = server.ThreadingHTTPServer(("127.0.0.1", 0), server.H)
threading.Thread(target=srv.serve_forever, daemon=True).start()


def get(path):
    c = http.client.HTTPConnection("127.0.0.1", srv.server_port, timeout=20)
    try:
        c.request("GET", path)
        r = c.getresponse()
        return r.status, r.read().decode("utf-8", "replace")
    finally:
        c.close()


def visible(h):
    body = h[h.index("<main"):h.index("</main>")]
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body)))


def shingles(t):
    w = re.findall(r"\w+", t.lower())
    return {" ".join(w[k:k + 5]) for k in range(len(w) - 4)}


def make_db(path, doms, bl, common=(), thin=()):
    c = sqlite3.connect(path)
    c.executescript("create table dom(domain text primary key, referring_domains int, tier int) without rowid; create table bl(domain text, rank int, referrer text, referrer_inlinks int); create table meta(k text primary key, v text);"
                    "create table common(referrer text primary key, hosts int) without rowid; create table thin(domain text primary key, why text) without rowid;")
    c.executemany("insert into dom values (?,?,2)", doms)
    c.executemany("insert into bl values (?,?,?,?)", [(d, r, ref, x) for d, rows in bl.items() for r, (ref, x) in enumerate(rows, 1)])
    c.executemany("insert into meta values (?,?)", [("graph", "g"), ("domains", "1000"), ("links", "2000"), ("read_on", "2026-10-23"), ("common_pct", "3"), ("common_hosts", "5011")])
    c.executemany("insert into common values (?,1000)", [(r,) for r in common])
    c.executemany("insert into thin values (?, 'twin')", [(d,) for d in thin])
    c.commit(); c.close()


@pytest.fixture()
def small(tmp_path, monkeypatch):
    p = str(tmp_path / "bl.sqlite")
    own = [("own%02d.de" % k, 900 - k) for k in range(40)]
    make_db(p, [("a.de", 500), ("b.de", 400), ("c.de", 300), ("d.de", 200)],
            {"a.de": [("google.com", 9000), ("wikipedia.org", 8000)] + own, "b.de": [("google.com", 9000)] + own[:3], "c.de": own, "d.de": [("google.com", 9000), ("blogspot.com", 7000)] + own[:12]},
            common=["google.com", "wikipedia.org", "blogspot.com"], thin=["c.de"])
    monkeypatch.setattr(b, "DB", p)
    monkeypatch.setattr(b, "FULL_DB", str(tmp_path / "none.sqlite"))
    b._COMMON.clear(); b._THIN.clear(); b._SITEMAP.clear()
    yield p
    b._COMMON.clear(); b._THIN.clear(); b._SITEMAP.clear()


def test_common_referrers_leave_the_table_and_are_named_in_one_line(small):
    n, rows, folded = b.split("a.de")
    assert n == 500 and folded == ["google.com", "wikipedia.org"]
    assert [r for _, r, _ in rows] == [x for x, _ in [("own%02d.de" % k, 0) for k in range(30)]] and [k for k, _, _ in rows] == list(range(1, 31))   # 30 of its own, ranks close up
    h = b.host_page("a.de")[1]
    t = visible(h)
    assert "google.com</td>" not in h and "wikipedia.org</td>" not in h
    assert "Left out of the table because they link to many domains in this data, for example: google.com, wikipedia.org." in t
    assert "Below are 30 of the strongest." in t and "Strength is how many" not in t


def test_a_host_with_no_common_referrer_gets_no_folded_line(small):
    assert "for example: google.com." in visible(b.host_page("b.de")[1])
    assert b.split("c.de")[2] == []   # c.de lists none of the three
    assert "Left out of the table" not in visible(b.host_page("c.de")[1])


def test_without_a_common_table_the_page_lists_everything_as_before(small):
    c = sqlite3.connect(small); c.execute("drop table common"); c.execute("drop table thin"); c.commit(); c.close()
    b._COMMON.clear(); b._THIN.clear()
    n, rows, folded = b.split("b.de")
    assert folded == [] and [r for _, r, _ in rows][:2] == ["google.com", "own00.de"]
    assert b.thin_hosts() == frozenset() and 'name="robots"' not in b.host_page("c.de")[1]


def test_a_thin_or_twin_host_is_noindex_without_schema_or_alternates_and_out_of_the_sitemap(small):
    h = b.host_page("c.de")[1]
    assert '<meta name="robots" content="noindex,follow">' in h and 'application/ld+json' not in h and 'rel="alternate" hreflang' not in h
    assert 'name="robots"' not in b.host_page("a.de")[1] and 'application/ld+json' in b.host_page("a.de")[1]
    s = b.sitemap()
    assert "/backlinks/a.de<" in s and "/backlinks/c.de<" not in s and s.count("<url>") == 5 * (2 + 3)


def test_the_method_text_lives_on_one_page_in_every_language(small):
    for lg in LOCALES:
        p = i.prefix(lg)
        st, page = get(f"{p}/backlinks/method")
        assert st == 200 and f'<html lang="{lg}">' in page and 'name="robots"' not in page
        assert f'<link rel="canonical" href="https://citedby.eu{p}/backlinks/method">' in page and 'hreflang="x-default" href="https://citedby.eu/backlinks/method"' in page
        method = html.escape(i.T[lg]["method"].format(d=i.fmt(1000, lg), l=i.fmt(2000, lg), graph=b.GRAPH))
        assert method in page and i.T[lg]["method_h1"] in html.unescape(page)
        assert html.escape(i.T[lg]["method_fold"].format(pct="3", n=i.fmt(5011, lg))) in page   # the folding rule is stated with its share and host count
        host = b.host_page("a.de", lg)[1]
        assert method not in host and f'<a href="{p}/backlinks/method">' in host and visible(host).count(i.T[lg]["method_h2"]) == 1   # one line, one link
        assert f'<a href="{p}/backlinks/method">' in b.index_page("", lg) and method not in b.index_page("", lg)
    assert get("/backlinks/method/")[0] == 200 and get("/backlinks/METHOD")[0] in (200, 301, 404)


def test_every_locale_has_the_new_strings():
    for k in ("method_link", "folded", "method_h1", "method_title", "method_desc", "method_fold"):
        assert len({i.T[lg][k] for lg in LOCALES}) == 5, k
    for lg in LOCALES:
        assert "{a}" in i.T[lg]["method_link"] and "{z}" in i.T[lg]["method_link"] and "{list}" in i.T[lg]["folded"] and "{pct}" in i.T[lg]["method_fold"] and "{n}" in i.T[lg]["method_fold"], lg
        d = i.T[lg]["method_desc"]
        assert d.rstrip()[-1] in ".?!" and len(d) <= 165 and i.T[lg]["method_title"].endswith("| CitedBy") and len(i.T[lg]["method_title"]) <= 100, lg


def test_the_shipped_pages_share_well_under_the_flag_level():
    """CitedBy's own check flags two pages that share 60% of their 5-word shingles (once the site's menu and footer are removed). Raw overlap here keeps the menu and footer in, so it is the stricter number.
    Before RES-3899 the shipped pages read 0.52-0.68 against their closest mate."""
    th = b.thin_hosts()
    assert len(th) > 400 and "semrush.com" not in th and "ahrefs.com" not in th and len(th) < 1200
    hs = [h for h in b.hosts() if h not in th]
    hs = hs[::max(1, len(hs) // 120)]
    sh = {h: shingles(visible(b.host_page(h)[1])) for h in hs}
    js = [len(sh[x] & sh[y]) / len(sh[x] | sh[y]) for x, y in itertools.combinations(hs, 2)]
    assert max(js) < 0.5 and statistics.median(js) < 0.3, (max(js), statistics.median(js))
    words = [len(re.findall(r"\w+", visible(b.host_page(h)[1]))) for h in hs[:40]]
    assert min(words) > 200, min(words)   # a page that stays indexable still has its own text


def test_every_indexable_shipped_host_has_enough_referrers_of_its_own():
    th = b.thin_hosts()
    for h in b.hosts()[::50]:
        n, rows, folded = b.split(h)
        tier1 = bool(sqlite3.connect("file:%s?mode=ro" % b.DB, uri=True).execute("select 1 from dom where domain=? and tier=1", (h,)).fetchone())
        if h not in th and not tier1:
            assert len(rows) >= 8, (h, len(rows))
        assert len(rows) <= b.SHOWN and len(folded) <= b.FOLD_MAX and not set(folded) & {r for _, r, _ in rows}, h
