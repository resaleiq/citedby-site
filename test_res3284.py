"""RES-3284: conditional requests (ETag / 304) and in-body links to the pages Google did not know."""
import http.client, os, re, tempfile, threading, unittest
os.environ.setdefault("OPTIN_SECRET", "x" * 40); os.environ.setdefault("BASE_URL", "http://t"); os.environ.setdefault("DATA_DIR", tempfile.mkdtemp())
from http.server import ThreadingHTTPServer
import server

PUB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")


class Etag(unittest.TestCase):
    def test_etag_and_304(self):
        srv = ThreadingHTTPServer(("127.0.0.1", 0), server.H)
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        try:
            def get(h=None):
                c = http.client.HTTPConnection("127.0.0.1", srv.server_port); c.request("GET", "/about", headers=h or {}); r = c.getresponse(); b = r.read(); return r, b
            r, b = get(); et = r.getheader("ETag")
            self.assertEqual(r.status, 200); self.assertTrue(et and et.startswith('"')); self.assertTrue(b)
            r2, b2 = get({"If-None-Match": et})
            self.assertEqual((r2.status, b2, r2.getheader("ETag")), (304, b"", et))
            r3, _ = get({"If-None-Match": '"other"'}); self.assertEqual(r3.status, 200)
        finally:
            srv.shutdown(); srv.server_close()


class InBodyLinks(unittest.TestCase):
    def main_links(self, rel):
        h = open(os.path.join(PUB, rel), encoding="utf-8").read()
        m = re.search(r"<main.*?</main>", h, re.S)
        return re.findall(r'href="([^"?#]*)', m.group(0))

    def test_each_target_linked_from_article_body(self):
        want = {"/tools/findable-check": "blog/is-gptbot-blocked.html", "/changes": "blog/geo-vs-aeo-vs-seo.html", "/compare/profound-vs-peec-vs-otterly": "blog/chatgpt-wrong-price.html"}
        for url, page in want.items():
            self.assertIn(url, self.main_links(page), (url, page))


if __name__ == "__main__":
    unittest.main()
