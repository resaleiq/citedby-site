"""RES-3749: the HTTP routes of /backlinks in fr, de, es, nl: language prefix, redirects keep the language, errors are pages in the language, sitemap, English unchanged.
Run: python3 -m pytest -q test_res3749_backlinks_routes.py"""
import html, http.client, os, re, tempfile, threading
os.environ.update(OPTIN_SECRET="x" * 40, BASE_URL="http://t", DATA_DIR=tempfile.mkdtemp())
import server

srv = server.ThreadingHTTPServer(("127.0.0.1", 0), server.H)
threading.Thread(target=srv.serve_forever, daemon=True).start()
PORT = srv.server_port


def get(path):
    c = http.client.HTTPConnection("127.0.0.1", PORT, timeout=20)
    try:
        c.request("GET", path)
        r = c.getresponse()
        return r.status, {k.lower(): v for k, v in r.getheaders()}, r.read().decode("utf-8", "replace")
    finally:
        c.close()


def text(h):
    return html.unescape(re.sub(r"[ \t\r\n]+", " ", re.sub(r"<[^>]+>", " ", re.sub(r"(?s)<script.*?</script>", " ", h[h.index("<body"):]))))


def test_lookup_and_host_pages_answer_in_each_language():
    for lg, word in (("fr", "domaines renvoient vers semrush.com"), ("de", "Domains verlinken"), ("es", "dominios enlazan a semrush.com"), ("nl", "domeinen linken naar semrush.com")):
        st, hd, body = get(f"/{lg}/backlinks/semrush.com")
        assert st == 200 and f'<html lang="{lg}">' in body and word in text(body), lg
        assert "text/html" in hd["content-type"] and "noindex" not in hd.get("x-robots-tag", "") and 'name="robots"' not in body
        st, hd, idx = get(f"/{lg}/backlinks")
        assert st == 200 and f'<html lang="{lg}">' in idx and f'action="/{lg}/backlinks"' in idx, lg


def test_footer_hub_links_and_follow_link_are_added_in_the_page_language():
    st, hd, body = get("/es/backlinks/semrush.com")
    assert 'data-hub-links' in body and "Guías" in body and "Herramientas gratis" in body       # hub_links.inject reads <html lang="es">
    assert "/es/privacy" in body and "Aviso legal" in body and "Legal notice" not in body.replace("Aviso legal", "")


def test_form_submit_redirects_keep_the_language_and_the_canonical_host():
    for lg in ("fr", "de", "es", "nl"):
        st, hd, _ = get(f"/{lg}/backlinks?host=HTTPS%3A%2F%2Fwww.Semrush.com%2Fpricing")
        assert st == 302 and hd["location"] == f"/{lg}/backlinks/semrush.com" and hd["x-robots-tag"] == "noindex", lg
        st, hd, _ = get(f"/{lg}/backlinks/www.Semrush.com")
        assert st == 301 and hd["location"] == f"/{lg}/backlinks/semrush.com", lg
    st, hd, _ = get("/backlinks?host=semrush.com")
    assert st == 302 and hd["location"] == "/backlinks/semrush.com"                              # English unchanged


def test_bad_input_is_a_page_in_the_language_with_a_way_forward():
    bad = {"fr": "Cela ne ressemble pas à un nom de domaine", "de": "Das sieht nicht nach einem Domainnamen aus", "es": "Eso no parece un nombre de dominio", "nl": "Dat lijkt niet op een domeinnaam"}
    for lg, msg in bad.items():
        st, hd, body = get(f"/{lg}/backlinks?host=not%20a%20domain")
        assert st == 200 and msg in text(body) and hd["x-robots-tag"] == "noindex" and f'action="/{lg}/backlinks"' in body, lg
        st, hd, body = get(f"/{lg}/backlinks/not_a_domain")
        assert st == 404 and msg in text(body) and hd["x-robots-tag"] == "noindex" and f'<html lang="{lg}">' in body, lg
        assert "We could not find that page" not in body
    st, hd, body = get("/backlinks/not_a_domain")
    assert st == 404 and "We could not find that page" in body                                    # English unchanged


def test_sitemap_has_every_language_and_unsupported_prefixes_are_not_routes():
    st, hd, body = get("/sitemap-backlinks.xml")
    assert st == 200 and "xml" in hd["content-type"] and body.count("<url>") == 5 * 5012
    assert "https://citedby.eu/nl/backlinks/semrush.com" in body
    for p in ("/it/backlinks", "/xx/backlinks/semrush.com", "/frbacklinks", "/fr/backlinksx"):
        assert get(p)[0] == 404, p


def test_english_pages_now_carry_hreflang_alternates_and_the_language_switch():
    st, hd, body = get("/backlinks/semrush.com")
    assert st == 200 and '<link rel="alternate" hreflang="fr" href="https://citedby.eu/fr/backlinks/semrush.com">' in body and 'hreflang="x-default"' in body
    assert '<a href="/nl/backlinks/semrush.com" hreflang="nl" lang="nl">Nederlands</a>' in body
