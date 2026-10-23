"""RES-3795 (QA finding on RES-3719): the AI-Access Index page says what the crawler did, and its closing box leads to the free robots.txt check.
F1 the Fetch line and the Dataset's measurementTechnique; F2 the closing box; the data.css rule that makes its second button readable."""
import json, os, re
import pytest
import proxy

ROOT = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(ROOT, "public")
PAGES = ("ai-access-index-2026-10.html", "ai-access-index.html")
UA = "CitedBy-research/1.0 (+https://citedby.eu; robots.txt study, one request per site)"  # the header as the crawler sent it: a quote, never edited
STORY = os.path.expanduser("~/work/company-memory/research/data-stories/citedby-ai-access-index/STORY.md")


def page(n): return open(os.path.join(P, "data", n), encoding="utf-8").read()
def li(t, label): return re.search(r"<li><b>%s:</b>(.*?)</li>" % label, t, re.S).group(1)
def plain(h): return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", h)).strip()
def box(n): return re.search(r'<section class="cta">(.*?)</section>', page(n), re.S).group(1)


@pytest.mark.parametrize("n", PAGES)
def test_fetch_line_says_what_the_crawl_did(n):
    """crawl_robots.py probe(): after any answer but a readable 200 (403 and 429 too) it asks the next of https, https://www, http; a read file is followed by one home-page GET."""
    raw = li(page(n), "Fetch"); f = plain(raw)
    for s in ("/robots.txt was requested at https, then www, then http, stopping at the first readable file (HTTP 200 that is not an HTML page).",
              "A refusal (403, 429) did not stop the next variant, so a site could be asked at up to three addresses.",
              "Redirects were followed.",
              "Where a file was read, one GET of the home page followed, for the CMS signature.",
              "No login, no cookies, no browser identity."):
        assert s in f, s
    assert "no retry after a refusal" not in f.lower() and not f.startswith("one GET")
    assert "<code>" + UA + "</code>" in raw  # quoted unchanged
    assert 'the words "one request per site" in it did not describe the crawl' in f  # and the page says so next to the quote


@pytest.mark.parametrize("n", PAGES)
def test_dataset_measurement_technique_matches_the_fetch_line(n):
    ld = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', page(n), re.S).group(1))
    m = ld["@graph"][0]["measurementTechnique"]
    assert "at https, then www, then http, stopping at the first readable file" in m and "2026-10-23" in m and "RFC 9309" in m and "56Z8N" in m
    assert "One GET" not in m and "one GET" not in m


@pytest.mark.skipif(not os.path.exists(STORY), reason="STORY.md (company-memory, Research's file) is not on this machine")
@pytest.mark.parametrize("n", PAGES)
def test_fetch_line_is_storys_line_word_for_word(n):
    """The builder says the method is STORY.md's, word for word: the two must not drift (RES-3795 changed both)."""
    line = next(l for l in open(STORY, encoding="utf-8") if l.startswith("- **Fetch:**"))
    assert re.sub(r"\s+", " ", line[len("- **Fetch:**"):].replace("`", "")).strip() == plain(li(page(n), "Fetch"))


@pytest.mark.parametrize("n", PAGES)
def test_closing_box_leads_with_the_free_check_then_the_audit(n):
    b = box(n)
    btns = re.findall(r'<a class="(btn[^"]*)" href="([^"]*)"([^>]*)>([^<]*)</a>', b)
    assert [(c, h, t) for c, h, _a, t in btns] == [("btn p", "/tools/ai-crawler-check", "Check my robots.txt free"), ("btn", "/", "Audit my site")]
    assert b.count('class="btn p"') == 1  # one filled primary in the box
    assert 'data-cta="primary" data-cta-id="aiindex-check"' in btns[0][2] and 'data-cta="secondary" data-cta-id="aiindex-audit"' in btns[1][2]  # riq-a.js counts the click
    assert "The free check shows which AI crawlers your robots.txt and your server let in, with the exact fix." in plain(b)
    assert "we crawl your site up to your plan's page limit and give you the exact fix for each issue" in plain(b)  # the house line stays (CONTRACT: how the engine is described)
    assert proxy.ROUTES["GET"].fullmatch("/tools/ai-crawler-check")  # the first button's target is served (by the app, through this site)


def test_second_button_is_readable_on_the_light_data_band():
    """doc.css paints a non-primary a.btn in a .cta white on navy; data.css makes the band light, so without this rule the 'Audit my site' button is white on white (RES-3749 saw the same on /backlinks).
    A string test cannot see the cascade: the contrast is also measured in a real browser (res3749_btn_contrast.mjs, 4.5 or more)."""
    css = open(os.path.join(P, "data.css"), encoding="utf-8").read()
    assert ".dp .cta .actions a.btn:not(.p){background:#fff;color:var(--navy);border:2px solid var(--navy)}" in css
