"""RES-2203: 15 legal pages (EN + fr/nl/de/es x privacy/terms/refund) with hreflang, sitemap entries and locale footer links."""
import pathlib, re
import legal_links

PUB = pathlib.Path(__file__).parent / "public"
LANGS = ["en", "fr", "nl", "de", "es"]; PAGES = ["privacy", "terms", "refund"]
P = lambda l, pg: f"/{pg}" if l == "en" else f"/{l}/{pg}"
F = lambda l, pg: (PUB / (P(l, pg).lstrip("/") + ".html")).read_text(encoding="utf-8")


def test_all_15_pages_have_canonical_hreflang_and_x_default():
    for pg in PAGES:
        for l in LANGS:
            h = F(l, pg)
            assert f'<html lang="{l}">' in h
            assert f'<link rel="canonical" href="https://citedby.eu{P(l, pg)}">' in h
            for c in LANGS: assert f'hreflang="{c}" href="https://citedby.eu{P(c, pg)}"' in h
            assert f'hreflang="x-default" href="https://citedby.eu{P("en", pg)}"' in h


def test_no_markdown_left_over_and_h1_present():
    for pg in PAGES:
        for l in LANGS:
            h = F(l, pg); text = re.sub(r"<[^>]+>", "", h)
            assert h.count("<h1>") == 1 and "**" not in text and "](" not in text and "|---" not in text, (l, pg)


def test_footer_links_stay_in_the_pages_language():
    for pg in PAGES:
        for l in LANGS[1:]:
            h = F(l, pg).split("<footer>")[1].split("langsw")[0]
            for x in PAGES: assert f'href="/{l}/{x}"' in h and f'href="/{x}"' not in h


def test_internal_links_in_locale_pages_use_the_locale_pages():
    for l in LANGS[1:]:
        for pg in PAGES:
            h = F(l, pg).split("<main")[1].split("</main>")[0]
            assert 'href="/withdraw"' not in h and 'href="/refund"' not in h and 'href="/privacy"' not in h and 'href="/terms"' not in h


def test_sitemap_lists_all_15_with_alternates():
    s = (PUB / "sitemap.xml").read_text()
    for pg in PAGES:
        for l in LANGS:
            assert f"<loc>https://citedby.eu{P(l, pg)}</loc>" in s
        assert s.count(f'hreflang="x-default" href="https://citedby.eu/{pg}"') == 5


def test_legal_links_localizes_footer_only_for_non_english():
    fr = b'<html lang="fr"><body><a href="/privacy">x</a><footer><a href="/terms">t</a><a href="/privacy?x=1">p</a><a href="/refund">r</a><a href="/contact">c</a></footer></body></html>'
    out = legal_links.localize(fr)
    assert b'<a href="/privacy">x</a>' in out  # body link untouched
    assert b'href="/fr/terms"' in out and b'href="/fr/privacy?x=1"' in out and b'href="/fr/refund"' in out and b'href="/contact"' in out
    en = fr.replace(b'lang="fr"', b'lang="en"')
    assert legal_links.localize(en) == en
    assert legal_links.localize(b"<footer><a href=\"/terms\">") == b"<footer><a href=\"/terms\">"


def test_v2_texts_are_the_ones_served():
    assert "Last updated: 22 October 2026" in re.sub(r"<[^>]+>", "", F("en", "privacy")).replace("Last updated:", "Last updated:")


def test_switch_english_link_has_no_locale_prefix_after_serve_time_rewrite():
    for pg in PAGES:
        for l in LANGS[1:]:
            out = legal_links.localize(F(l, pg).encode()).decode()
            assert f'<a href="/{pg}" hreflang="en" lang="en">English</a>' in out, (l, pg)
            assert f'href="/{l}/{pg}" hreflang="{l}"' in out


def test_tables_stack_with_labels_on_phones():
    for l in LANGS:
        h = F(l, "privacy")
        assert 'data-label="' in h and "attr(data-label)" in h and 'style="min-width:620px"' not in h
        assert 'data-label=""' not in h
