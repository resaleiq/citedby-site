"""S2 site pages (RES-1335): shared shell, own-audit numbers, price table, no placeholders. Run: python3 -m pytest test_s2_pages.py"""
import datetime, json, os, re
import home, pages, shell
sys_path = os.path.dirname(os.path.abspath(__file__))
import sys; sys.path.insert(0, os.path.join(sys_path, "tools"))
from build_day0_summary import summary

NOW = datetime.datetime.now(datetime.timezone.utc)
ENG = [{"name": n, "route": "API", "tested": NOW} for n in ("Claude Haiku 4.5", "GPT-5 mini", "Perplexity Sonar", "Grok 4.3", "Mistral Medium 3.1", "DeepSeek V4.1 Flash", "Qwen 3.7 Flash", "Gemini 3.5 Flash-Lite", "Llama 4 Scout")]
PAGES = {"/": home.render("en", ENG), "/fr": home.render("fr", ENG), "/pricing": pages.pricing(ENG), "/faq": pages.faq(ENG), "/thanks": pages.thanks()}
DATA = pages.data()


def block(h, tag): return re.search(r"<%s[ >].*?</%s>" % (tag, tag), h, re.S).group(0)


def test_one_shell_everywhere():
    for lang, paths in (("en", ("/", "/pricing", "/faq", "/thanks")), ("fr", ("/fr",))):
        for p in paths:
            assert shell.header(lang, None).split('aria-current="page"')[0][:200] in PAGES[p] or lang == "fr"
    assert shell.footer("en") in PAGES["/pricing"] and shell.footer("en") in DATA
    assert shell.header("en", "/data") in DATA


def test_day0_numbers_equal_the_csv():
    s = summary()
    assert (s["named"], s["answers"], s["kept"], s["linked"]) == (0, 48, 72, 0)
    assert s == {k: (v if k != "cited" else [list(x) for x in v]) for k, v in shell.day0().items()} or json.dumps(s) == json.dumps(shell.day0())
    # RES-1459 step 1 (founder 18 Oct): the self-audit never leads a page. The numbers stay on /data only.
    for p, h in PAGES.items():
        if p != "/data":
            assert "OUR OWN SITE" not in h and "0 of 48" not in h and "audited ourselves" not in h and 'href="/#proof"' not in h, p


def test_nine_names_with_date():
    h = PAGES["/"]
    assert h.count("<small>Tested ") == 9 and "The nine assistants we ask" in h


def test_prices_on_pricing_page_equal_table():
    h = PAGES["/pricing"]
    shown = sorted(int(x) for x in re.findall(r'class="pr">€(\d+)', h) + re.findall(r'class="price">€(\d+)', h))
    assert shown == sorted(pages.PRICES.values())
    assert "€149" not in h and "CitedBy Monthly" not in h
    assert h.count("Buy ") == 1 and "buy.stripe.com" in h
    for s in ("Tell me when it opens", "Ask about Agency Kit", "Ask about Workspace"): assert s in h


def test_one_amber_primary_per_page():
    for p, h in PAGES.items():
        assert len(re.findall(r'<a class="btn"|<button class="btn"', h)) <= 1, p


def test_no_placeholders_or_legal_inventions():
    for p, h in list(PAGES.items()) + [("/data", DATA)]:
        for bad in ("{id}", "{date}", "DESIGN TARGET", "GM owns the words", "(placeholder)", "testimonial"):
            assert bad not in h, (p, bad)
        assert len(re.findall(r"<h1[ >]", h)) == 1, p


def test_faq_schema_matches_dom():
    h = PAGES["/faq"]
    ld = json.loads(re.search(r'application/ld\+json">(.*?)</script>', h, re.S).group(1))
    assert ld["@type"] == "FAQPage" and len(ld["mainEntity"]) == h.count("<details")
