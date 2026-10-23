"""RES-3749: /backlinks in fr, de, es, nl. Each page is in its language (no English source string), canonical + hreflang, locale number format, localized shell,
FR typography, answer first, working links in the same language, and the sitemap lists every locale. Run: python3 -m pytest -q test_res3749_backlinks_i18n.py"""
import html, json, os, re, sys
import backlinks as b
import backlinks_i18n as i
import langroutes

LOCALES = ("fr", "de", "es", "nl")
ALL = ("en",) + LOCALES
ENGLISH = ["Who links to", "Referring domain", "Method and limits", "Skip to content", "Look up another domain", "Strongest referring domains", "Common Crawl samples the web",
           "Can search engines", "Sign in", "Pricing", "Legal notice", "No sign-up", "Check semrush.com free", "Most-linked", "Language:", "not in the set"]


def visible(h):
    body = h[h.index("<body"):]
    body = re.sub(r"(?s)<script.*?</script>", " ", body)
    return html.unescape(re.sub(r"[ \t\r\n]+", " ", re.sub(r"<[^>]+>", " ", body)))   # ASCII whitespace only: \s would fold the narrow no-break spaces away


def pages(lg):
    return {
        "known": b.host_page("semrush.com", lg)[1],
        "zero": b.host_page("citedby.eu", lg)[1],
        "unknown": b.host_page("example-unknown-site.fr", lg)[1],
        "index": b.index_page("", lg),
        "index_error": b.index_page(i.T[lg]["bad_host"], lg),
    }


def test_each_page_is_in_its_language_and_has_no_english_source_string():
    for lg in LOCALES:
        for name, h in pages(lg).items():
            t = visible(h)
            assert f'<html lang="{lg}">' in h, (lg, name)
            for s in ENGLISH:
                assert s not in t, (lg, name, s)


def test_canonical_hreflang_and_og_locale():
    for lg in LOCALES:
        code, h = b.host_page("semrush.com", lg)
        assert code == 200
        assert f'<link rel="canonical" href="https://citedby.eu/{lg}/backlinks/semrush.com">' in h
        for l in ALL:
            href = "https://citedby.eu" + ("" if l == "en" else "/" + l) + "/backlinks/semrush.com"
            assert f'<link rel="alternate" hreflang="{l}" href="{href}">' in h, (lg, l)
        assert '<link rel="alternate" hreflang="x-default" href="https://citedby.eu/backlinks/semrush.com">' in h
        assert f'<meta property="og:locale" content="{langroutes.OG_LOCALE[lg]}">' in h
        idx = b.index_page("", lg)
        assert f'<link rel="canonical" href="https://citedby.eu/{lg}/backlinks">' in idx and '<link rel="alternate" hreflang="x-default" href="https://citedby.eu/backlinks">' in idx
    en = b.host_page("semrush.com")[1]
    assert '<link rel="alternate" hreflang="fr" href="https://citedby.eu/fr/backlinks/semrush.com">' in en and '<html lang="en">' in en


def test_noindex_pages_stay_noindex_in_every_language():
    for lg in LOCALES:
        h = b.host_page("example-unknown-site.fr", lg)[1]
        assert 'content="noindex,follow"' in h
        assert 'content="noindex' not in b.host_page("semrush.com", lg)[1]


def test_numbers_use_the_locale_format_and_the_answer_comes_first():
    want = {"fr": "68 317 domaines renvoient vers semrush.com", "de": "68.317 Domains verlinken", "es": "68.317 dominios enlazan a semrush.com", "nl": "68.317 domeinen linken naar semrush.com"}
    for lg, s in want.items():
        t = visible(b.host_page("semrush.com", lg)[1])
        assert s in t, (lg, s)
        assert t.index(s) < 0.45 * len(t), lg
    assert [i.fmt(1234567, lg) for lg in ALL] == ["1,234,567", "1 234 567", "1.234.567", "1.234.567", "1.234.567"]
    assert i.fmt(999, "fr") == "999" and i.fmt(1000, "fr") == "1 000"


def test_form_links_and_cta_stay_in_the_language():
    for lg in LOCALES:
        h = b.host_page("semrush.com", lg)[1]
        assert f'action="/{lg}/backlinks"' in h
        assert f'<a href="/{lg}">CitedBy</a>' in h and f'<a href="/{lg}/backlinks">Backlinks</a>' in h
        assert f'href="/{lg}?url=semrush.com&amp;utm_source=citedby_backlinks&amp;utm_medium=free_tool&amp;utm_campaign=backlinks"' in h
        for ref in re.findall(r'href="/(?:fr|de|es|nl)/backlinks/([^"]+)"', h):
            if ref != "semrush.com":
                assert b.lookup(ref) is not None, ref
        assert not re.search(r'href="/backlinks', re.sub(r'<p class="src langs">.*?</p>', "", h))   # no link back into English except the language switch's English entry
        assert h.count("<tr>") == 21


def test_language_switch_links_the_same_page_in_each_language():
    h = b.host_page("semrush.com", "fr")[1]
    for l, name in (("en", "English"), ("fr", "Français"), ("de", "Deutsch"), ("es", "Español"), ("nl", "Nederlands")):
        href = "/backlinks/semrush.com" if l == "en" else f"/{l}/backlinks/semrush.com"
        assert f'<a href="{href}" hreflang="{l}" lang="{l}"' in h and f">{name}</a>" in h, l
    assert 'aria-current="true"' in h
    assert re.search(r'<a href="/fr/backlinks/semrush.com" hreflang="fr" lang="fr" aria-current="true">', h)
    idx = b.index_page("", "de")
    assert '<a href="/backlinks" hreflang="en" lang="en">English</a>' in idx and 'href="/de/backlinks" hreflang="de" lang="de" aria-current="true"' in idx


def test_shell_is_localized_like_the_other_reading_pages():
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools"))
    import build_legal, docshell
    for lg in LOCALES:
        u, ref = i.UI[lg], build_legal.UI[lg]
        for k in ("check", "plans", "blog", "data", "signin", "cta", "skip", "main", "terms", "privacy", "refund", "contact", "legal", "home", "plans_h", "blog_h"):
            assert u[k] == ref[k], (lg, k)
        assert (u["method"], u["about"]) == docshell.EXTRA[lg]
        h = b.host_page("semrush.com", lg)[1]
        assert f'<a class="sr" href="#main">{u["skip"]}</a>' in h and f'>{u["legal"]}</a>' in h and f'href="/{lg}/privacy"' in h and f'href="/{lg}/terms"' in h
        assert "Legal notice" not in h and "Skip to content" not in h


def test_french_typography_non_breaking_space_before_question_mark_colon_semicolon():
    for name, h in pages("fr").items():
        t = visible(h)
        assert not re.search(r"[^\s ]\?", t), (name, re.findall(r".{12}[^\s ]\?", t))
        assert not re.search(r"(?<=\w) [:;?!]", t), name       # a plain space before : ; ? !
        assert not re.search(r"(?<=\w)[:;!](?= )", t), name     # nothing glued to the word before it
    assert " ?" in visible(b.host_page("semrush.com", "fr")[1])


def test_zero_and_unknown_states_in_each_language():
    zero = {"fr": "aucun domaine référent pour citedby.eu", "de": "keine verweisenden Domains für citedby.eu", "es": "no encontró dominios que enlacen a citedby.eu", "nl": "geen verwijzende domeinen voor citedby.eu"}
    unknown = {"fr": "ne figure pas encore", "de": "gehört noch nicht", "es": "aún no está en el conjunto", "nl": "zit nog niet in de set"}
    for lg in LOCALES:
        z = b.host_page("citedby.eu", lg)[1]
        assert zero[lg] in visible(z) and "<table" not in z, lg
        u = b.host_page("example-unknown-site.fr", lg)
        assert u[0] == 200 and unknown[lg] in visible(u[1]), lg


def test_meta_descriptions_end_at_a_sentence_end_and_stay_short():
    for lg in LOCALES + ("en",):
        for h in (b.host_page("semrush.com", lg)[1], b.host_page("citedby.eu", lg)[1], b.index_page("", lg)):
            d = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', h).group(1))
            assert d.rstrip()[-1] in ".?!" and len(d) <= 165, (lg, len(d), d)
            title = html.unescape(re.search(r"<title>(.*?)</title>", h).group(1))
            assert title.endswith("| CitedBy") and len(title) <= 100, (lg, title)


def test_dataset_schema_is_localized():
    for lg in LOCALES:
        h = b.host_page("semrush.com", lg)[1]
        ld = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S).group(1))
        assert ld["@type"] == "Dataset" and ld["inLanguage"] == lg and ld["url"] == f"https://citedby.eu/{lg}/backlinks/semrush.com"
        assert ld["license"] == "https://commoncrawl.org/terms-of-use" and ld["temporalCoverage"] == "2026-08/2026-10"
        assert "Referring domains of" not in ld["name"]


def test_no_ai_engine_wording_and_register():
    for lg in LOCALES:
        for h in pages(lg).values():
            assert not re.search(r"powered by ai|ai-powered|\bour ai\b|propulsé par l.ia|ki-gestützt|con ia propia|aangedreven door ai", h.lower()), lg
    reg = {"fr": ("vous", r"\btu\b"), "de": ("Sie", r"\bdu\b"), "es": ("tú|tu ", r"\busted\b"), "nl": (r"\bje\b", r"\bu\b")}
    for lg, (yes, no) in reg.items():
        t = visible(b.host_page("citedby.eu", lg)[1])
        assert re.search(yes, t), (lg, "register word missing")
        assert not re.search(no, t), (lg, "wrong register")


def test_sitemap_lists_every_locale():
    s = b.sitemap()
    assert s.count("<url>") == 5 * 5012
    for lg in LOCALES:
        assert f"<loc>https://citedby.eu/{lg}/backlinks</loc>" in s and f"<loc>https://citedby.eu/{lg}/backlinks/semrush.com</loc>" in s
    assert "<loc>https://citedby.eu/backlinks/semrush.com</loc>" in s


def test_plural_and_formats_helpers():
    assert i.plural_key(1) == "one" and i.plural_key(2) == "other" and i.plural_key(0) == "other"
    for lg in ALL:
        assert i.T[lg]["ans_n_one"] and i.T[lg]["desc_n_one"], lg


def test_every_locale_has_every_string():
    keys = set(i.T["en"])
    for lg in LOCALES:
        assert set(i.T[lg]) == keys, (lg, set(i.T[lg]) ^ keys)
        for k, v in i.T[lg].items():
            assert v and (v != i.T["en"][k] or k in ("form_ph", "form_label", "crumb_home", "crumb_bl", "th_rank", "dl_rank")), (lg, k)
