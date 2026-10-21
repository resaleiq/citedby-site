"""RES-2343 F4: /<lang>?url=<host> prefills the landing field on the server. Run: python3 -m pytest test_res2343_prefill.py"""
import os, tempfile
os.environ.setdefault("OPTIN_SECRET", "x" * 40); os.environ.setdefault("BASE_URL", "http://t"); os.environ.setdefault("DATA_DIR", tempfile.mkdtemp())
import server

def test_prefill_host_accepts_hosts_and_urls():
    assert server.prefill_host("/fr?url=lemonde.fr") == "lemonde.fr"
    assert server.prefill_host("/?url=https://www.Stripe.com/docs?a=1") == "stripe.com"

def test_prefill_host_rejects_markup_and_junk():
    for bad in ('x"><script>.com', "localhost", "a b.com", ""):
        assert server.prefill_host("/?url=" + bad) == ""
    assert server.prefill_host("/") == ""
