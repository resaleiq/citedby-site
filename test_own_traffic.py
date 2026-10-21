"""RES-2134: INTERNAL_CLIENT_IPS (the one own-traffic list) keeps staff out of the counters; /go/fixpack counts an outside open and redirects to the Payment Link either way;
free_tool_start follows check_start. Run: python3 test_own_traffic.py"""
import json, os, sqlite3, tempfile, threading, unittest, urllib.error, urllib.request
os.environ.update(OPTIN_SECRET="x" * 40, BASE_URL="http://t", DATA_DIR=tempfile.mkdtemp(), INTERNAL_CLIENT_IPS="203.0.113.7 # mac, 198.51.100.4", INTERNAL_IPS="192.0.2.9")
import home, server
from http.server import ThreadingHTTPServer


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k): return None


class T(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.srv = ThreadingHTTPServer(("127.0.0.1", 0), server.H)
        threading.Thread(target=cls.srv.serve_forever, daemon=True).start()
        cls.u = "http://127.0.0.1:%d" % cls.srv.server_address[1]

    @classmethod
    def tearDownClass(cls): cls.srv.shutdown()

    def n(self, typ):
        c = sqlite3.connect(server.DB_PATH)
        try: return c.execute("SELECT coalesce(sum(n),0) FROM event_count WHERE type=?", (typ,)).fetchone()[0]
        finally: c.close()

    def get(self, path, xff):
        try:
            urllib.request.build_opener(NoRedirect).open(urllib.request.Request(self.u + path, headers={"X-Forwarded-For": xff}))
        except urllib.error.HTTPError as e: return e.code, e.headers.get("Location")

    def test_both_env_names_are_read(self):
        self.assertTrue({"203.0.113.7", "198.51.100.4", "192.0.2.9"} <= server.INTERNAL_IPS and "" not in server.INTERNAL_IPS)

    def test_fixpack_redirect_counts_outsiders_only(self):
        b = self.n("fixpack_click")
        self.assertEqual(self.get("/go/fixpack?lang=fr", "9.9.9.9"), (302, "/plans"))
        self.assertEqual(self.n("fixpack_click"), b + 1)
        self.assertEqual(self.get("/go/fixpack", "203.0.113.7"), (302, "/plans"))
        self.assertEqual(self.get("/go/fixpack", "1.1.1.1, 192.0.2.9"), (302, "/plans"))
        self.assertEqual(self.n("fixpack_click"), b + 1)

    def test_browser_events(self):
        for typ in ("offer_view", "first_screen_cta_click"):
            b = self.n(typ)
            for ip in ("203.0.113.7", "9.9.9.9"):
                urllib.request.urlopen(urllib.request.Request(self.u + "/api/event", json.dumps({"type": typ, "lang": "en"}).encode(), {"X-Forwarded-For": ip}, method="POST"))
            self.assertEqual(self.n(typ), b + 1)

    def test_free_tool_start_follows_check_start(self):
        b, c = self.n("check_start"), self.n("free_tool_start")
        server.count_event("check_start", "en", "9.9.9.9"); server.count_event("check_start", "en", "203.0.113.7")
        self.assertEqual((self.n("check_start"), self.n("free_tool_start")), (b + 1, c + 1))


if __name__ == "__main__": unittest.main()
