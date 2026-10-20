"""RES-2182: the "Withdraw from contract here" link is on every HTML page, in the page's language, and the app's /withdraw paths are proxied."""
import glob, os, re
import proxy, withdraw_link as w

def test_inject_in_footer_per_language():
    for lg, lab in w.LABELS.items():
        out = w.inject(f'<!doctype html><html lang="{lg}"><body><main>x</main><footer>f</footer></body></html>'.encode()).decode()
        assert f'{lab}</a></p></footer>' in out and f'href="{"/withdraw" if lg == "en" else "/" + lg + "/withdraw"}"' in out

def test_no_footer_falls_back_to_body_end_and_is_idempotent():
    out = w.inject(b'<!doctype html><html lang="en"><body>x</body></html>'); assert b"Withdraw from contract here</a></p></body>" in out and w.inject(out) == out

def test_fragments_and_the_form_page_itself_untouched():
    assert w.inject(b"<p>fragment</p>") == b"<p>fragment</p>" and b"data-withdraw" not in w.inject(b'<html lang="en"><body></body></html>', "/withdraw")

def test_every_static_page_gets_exactly_one_link():
    n = 0
    for f in glob.glob("public/**/*.html", recursive=True):
        b = open(f, "rb").read()
        if b"<html" not in b[:600].lower(): continue
        assert w.inject(b).count(b"data-withdraw") == 1, f; n += 1
    assert n > 80

def test_proxy_forwards_withdraw_in_five_languages():
    for p in ("/withdraw", "/fr/withdraw", "/de/withdraw", "/nl/withdraw", "/es/withdraw"): assert proxy.ROUTES["GET"].fullmatch(p), p
    for p in ("/withdraw", "/withdraw/confirm", "/fr/withdraw/confirm", "/es/withdraw"): assert proxy.ROUTES["POST"].fullmatch(p), p
    assert not proxy.ROUTES["GET"].fullmatch("/withdraw/confirm") and not proxy.ROUTES["POST"].fullmatch("/xx/withdraw")

def test_refund_and_terms_point_to_the_function():
    for f in ("public/refund.html", "public/terms.html"): assert 'href="/withdraw">Withdraw from contract here</a>' in open(f).read()
