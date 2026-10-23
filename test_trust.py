"""RES-3683: fact pages (/data, the free tools) carry source, checked-on date, method and change-log links, and sameAs plus dateModified in JSON-LD."""
import json, re, trust

PAGE = ('<!doctype html><html lang="%s"><head><script type="application/ld+json">{"@type": "WebPage", "name": "x", "provider": {"@type": "Organization", "name": "CitedBy", "url": "https://citedby.eu"}}</script></head>'
        '<body><main id="main"><h1>t</h1></main><footer></footer></body></html>')


def run(path, lg="en", body=None):
    return trust.inject((body or PAGE % lg).encode(), path).decode()


def ld(h): return json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S).group(1))


def test_tool_page_gets_block_source_date_and_ld():
    h = run("/tools/llms-txt-checker")
    assert "data-trust" in h and "Engine rules last checked on" in h and 'href="https://llmstxt.org/"' in h and 'href="/methodology"' in h and 'href="/changes"' in h
    d = ld(h)
    assert "https://x.com/CitedByEU" in d["provider"]["sameAs"] and d["dateModified"] == trust.ledger_date()


def test_localised_and_prefixed_links():
    h = run("/fr/tools/findable-check", "fr")
    assert "Vérifié le" in h and 'href="/fr/changes"' in h and "oct." in h or "nov." in h


def test_data_page_uses_its_own_date_and_csv():
    body = PAGE % "en" + ""
    body = body.replace('"name": "x"', '"name": "x", "dateModified": "2026-10-19"')
    h = run("/data/launch-crawl-2026-10", body=body)
    assert "Checked on 19 Oct 2026" in h and "rfc9309" in h and "/data/launch-crawl-2026-10.csv" in h


def test_no_date_when_none_is_known_and_other_pages_untouched():
    assert "Checked on" not in run("/data/matelas-france")
    for p in ("/plans", "/data/x.csv", "/tools/unknown-tool", "/blog/a"):
        assert run(p) == PAGE % "en"
    assert run("/data/matelas-france") == run("/data/matelas-france").replace("data-trust", "data-trust")  # stable
    assert trust.inject(run("/tools/findable-check").encode(), "/tools/findable-check").decode().count("data-trust") == 1


def test_page_without_organization_gets_one():
    h = trust.inject(b'<html lang="en"><head></head><body><main>x</main></body></html>', "/tools/findable-check").decode()
    assert '"@type": "Organization"' in h and "https://x.com/CitedByEU" in h
