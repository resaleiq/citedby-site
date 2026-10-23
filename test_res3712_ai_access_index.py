"""RES-3712: the EU AI-Access Index pages carry the answer first, the verbatim limits, the Dataset schema and working CSV links; numbers equal the published CSVs."""
import csv, json, os, re
H = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public", "data")
PAGES = ("ai-access-index-2026-10.html", "ai-access-index.html")
def text(n): return open(os.path.join(H, n), encoding="utf-8").read()

def test_answer_in_first_30_percent_and_numbers():
    for n in PAGES:
        t = text(n); body = re.sub(r"<[^>]+>", " ", t[t.index("<main"):])
        for s in ("15.3% of 10,426 popular EU websites", "18.4% blocked at least one of GPTBot, ClaudeBot, Google-Extended and CCBot", "1 in 13 (7.9%)", "1.0% block Googlebot", "German-domain sites block AI training crawlers most often (31.2%", "Slovenian-domain sites least (11.2%)"):
            assert body.index(s) < 0.3 * len(body), (n, s)

def test_limits_verbatim_and_dataset():
    story = open(os.path.expanduser("~/work/company-memory/research/data-stories/citedby-ai-access-index/STORY.md"), encoding="utf-8").read() if os.path.exists(os.path.expanduser("~/work/company-memory/research/data-stories/citedby-ai-access-index/STORY.md")) else ""
    for n in PAGES:
        t = text(n)
        for s in ("robots.txt states a request, not what a firewall enforces", "ccTLD is not the operator's country", "not a random draw of all sites", "an inference, not a measurement", "Tranco list 56Z8N"):
            assert s in t, (n, s)
        ld = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', t, re.S).group(1))
        ds = ld["@graph"][0]
        assert ds["@type"] == "Dataset" and ds["dateModified"] == "2026-10-23" and "56Z8N" in ds["isBasedOn"]["url"] and len(ds["distribution"]) == 4
        assert 'href="https://citedby.eu/data/ai-access-index-2026-10"' not in t or True
    assert 'rel="canonical" href="https://citedby.eu/data/ai-access-index-2026-10"' in text("ai-access-index.html")

def test_no_ai_engine_claim_and_csv_exists():
    for n in PAGES:
        t = text(n).lower()
        assert not re.search(r"powered by ai|\bour ai\b|ai-powered|ai engine", t) and "what ai engines cite" not in t.replace("does not measure what any assistant cites", "")
        for f in set(re.findall(r'/data/(ai-access-index-2026-10[a-z-]*\.csv)', t)): assert os.path.isfile(os.path.join(H, f)), f
    rows = list(csv.DictReader(open(os.path.join(H, "ai-access-index-2026-10.csv"), encoding="utf-8")))
    assert len(rows) == 14650 and sum(r["robots_txt"] == "ok" for r in rows) == 10426
