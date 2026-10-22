"""RES-2935: every HTML page links to the hubs from its footer, in its own language, once."""
import glob
import hub_links as h


def test_links_in_footer_per_language_and_once():
    for lg in h.LOCALES:
        out = h.inject(f'<!doctype html><html lang="{lg}"><body><main>x</main><footer>f</footer></body></html>'.encode()).decode()
        p = "" if lg == "en" else "/" + lg
        for href in (f"{p}/guides", f"{p}/blog", f"{p}/tools", f"{p}/ai-visibility-audit", "/bots", "/platforms", "/data", "/bot"):
            assert f'href="{href}"' in out, (lg, href)
        assert out.count("data-hub-links") == 1 and out.index("data-hub-links") < out.index("</footer>")
        assert f'href="/{lg}"' not in out or lg == "en"  # a page does not link its own language home as a switch target
        assert h.inject(out.encode()).decode() == out


def test_fragments_untouched_and_no_footer_falls_back_to_body_end():
    assert h.inject(b"<p>fragment</p>") == b"<p>fragment</p>"
    assert b"data-hub-links" in h.inject(b'<!doctype html><html lang="de"><body>x</body></html>').split(b"</body>")[0]


def test_every_static_page_gets_exactly_one_block():
    n = 0
    for f in glob.glob("public/**/*.html", recursive=True):
        b = open(f, "rb").read()
        if b"<html" not in b[:600].lower(): continue
        assert h.inject(b).count(b"data-hub-links") == 1, f; n += 1
    assert n > 80


def test_res3013_english_only_labels_localized_and_marked():
    for lg in ("fr", "nl", "de", "es"):
        out = h.inject(f'<!doctype html><html lang="{lg}"><body><footer>f</footer></body></html>'.encode()).decode()
        for en in ("AI bots", "Tool comparison", "Our crawler"):  # "Platforms" and "Data" are also Dutch words
            assert en not in out, (lg, en)
        assert out.count('hreflang="en"') == 6, lg
    assert ">Robots IA (en anglais)<" in h.inject(b'<html lang="fr"><body><footer></footer></body></html>').decode()
