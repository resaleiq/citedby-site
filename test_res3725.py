"""RES-3725: footer link to the live X profile on every locale and static page; same URL in Organization sameAs."""
import glob
import follow_link as f
import trust


def test_link_per_locale_once_in_footer():
    want = {"en": "Follow CitedBy on X", "fr": "Suivre CitedBy sur X", "nl": "Volg CitedBy op X", "de": "CitedBy auf X folgen", "es": "Seguir a CitedBy en X"}
    for lg, text in want.items():
        out = f.inject(f'<!doctype html><html lang="{lg}"><body><footer>f</footer></body></html>'.encode()).decode()
        assert f'rel="me noopener"' in out and 'href="https://x.com/CitedByEU"' in out and f">{text}</a>" in out
        assert out.count("data-follow-links") == 1 and out.index("data-follow-links") < out.index("</footer>")
        assert f.inject(out.encode()).decode() == out
    assert "?" not in "".join(u for _, u, _ in f.PROFILES)


def test_fragment_untouched_and_sameas():
    assert f.inject(b"<p>x</p>") == b"<p>x</p>"
    assert all(u in trust.SAME_AS for _, u, _ in f.PROFILES)


def test_every_static_page_once():
    n = 0
    for p in glob.glob("public/**/*.html", recursive=True):
        b = open(p, "rb").read()
        if b"<html" not in b[:600].lower(): continue
        assert f.inject(b).count(b"data-follow-links") == 1, p; n += 1
    assert n > 80


def test_wired_into_server_and_proxy():
    assert "follow_link.inject" in open("server.py").read() and "follow_link.inject" in open("proxy.py").read()
