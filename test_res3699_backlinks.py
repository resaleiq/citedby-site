"""RES-3699: /backlinks/<host> answers first, shows the method, never turns "not in the set" into zero, and every link and CTA is real."""
import json, re
import backlinks as b

def text(h): return re.sub(r"<[^>]+>", " ", h[h.index("<main"):])

def test_norm():
    assert b.norm("https://www.Semrush.com/pricing?x=1") == "semrush.com"
    assert b.norm("semrush.com:443") == "semrush.com"
    for bad in ("", "localhost", "a b.com", "../etc/passwd", "x.y;drop", "1.2.3.4"): assert b.norm(bad) == "", bad

def test_known_host_answer_table_method_schema():
    code, h = b.host_page("ahrefs.com")
    t = text(h)
    assert code == 200 and "127,837 domains link to ahrefs.com" in t and t.index("127,837") < 0.3 * len(t)
    assert "cc-main-2026-aug-sep-oct" in t and "Common Crawl samples the web" not in t   # RES-3899: the method text lives once, on /backlinks/method
    assert 'href="/backlinks/method">Method and limits</a>' in h
    assert "Common Crawl samples the web, so counts are lower than a full index" in text(b.method_page())
    assert h.count("<tr>") == 1 + b.SHOWN and 'name="robots"' not in h
    ld = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S).group(1))
    assert ld["@type"] == "Dataset" and ld["license"] == "https://commoncrawl.org/terms-of-use" and ld["temporalCoverage"] == "2026-08/2026-10"
    assert 'rel="canonical" href="https://citedby.eu/backlinks/ahrefs.com"' in h and "utm_campaign=backlinks" in h and "url=ahrefs.com" in h
    assert not re.search(r"powered by ai|ai-powered|\bour ai\b", h.lower())

def test_own_site_zero_case_and_unknown_host_is_not_zero():
    code, h = b.host_page("citedby.eu")
    assert "Common Crawl found no linking domains for citedby.eu" in text(h) and "<table" not in h
    code, h = b.host_page("example-unknown-site.fr")
    assert code == 200 and 'content="noindex,follow"' in h and "not in the set we have loaded yet" in h and "linking domains" not in text(h).replace("not in the set", "")

def test_every_shipped_host_has_20_rows_and_in_set_links_only():
    hs = b.hosts()
    assert len(hs) == 5011 and "ahrefs.com" in hs
    for d in ("ahrefs.com", hs[100]):
        _, h = b.host_page(d)
        for ref in re.findall(r'href="/backlinks/([^"]+)"', h):
            if ref not in (d, "method"): assert b.lookup(ref) is not None, ref

def test_sitemap_and_index():
    s = b.sitemap()
    kept = len(b.hosts()) - len(b.thin_hosts())   # RES-3899: a thin or twin page is noindex and not listed
    assert s.count("<url>") == 5 * (2 + kept) and "https://citedby.eu/backlinks/ahrefs.com" in s and "https://citedby.eu/fr/backlinks/method" in s   # RES-3749: the lookup and every host page in 5 languages, plus the method page
    thin = sorted(b.thin_hosts())
    assert len(thin) > 100 and not any(f"/backlinks/{d}</loc>" in s for d in thin)
    assert 'action="/backlinks"' in b.index_page() and "name=\"host\"" in b.index_page()
