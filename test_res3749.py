"""RES-3749: /api/check counts free_check_started_cli and free_check_started_action for the open-source CLI and GitHub Action,
and the set of check ids the CLI knows is pinned here. Run: python3 test_res3749.py"""
import os, sqlite3, tempfile, unittest
os.environ.update(OPTIN_SECRET="x" * 40, BASE_URL="http://t", DATA_DIR=tempfile.mkdtemp(), CHECK_PER_IP_HOUR="1000", CHECK_PER_HOST_HOUR="1000")
import doorcheck, safefetch, server

# the ids and statuses packages/citedby-check (github.com/resaleiq/citedby-check) has labels for; a new id here means the CLI needs a label first
CLI_CHECK_IDS = {"crawlers", "raw_text", "org_schema", "product_schema", "product_price", "product_availability", "product_gtin", "llms_txt"}
CLI_STATUSES = {"pass", "fail", "warn", "info", "na", "unknown"}


class T(unittest.TestCase):
    def n(self, event):
        c = sqlite3.connect(server.DB_PATH)
        try: return c.execute("SELECT coalesce(sum(n),0) FROM event_count WHERE type=?", (event,)).fetchone()[0]
        finally: c.close()

    def setUp(self):
        self._run = doorcheck.run
        doorcheck.run = lambda root, lang: {"site": root, "checks": [], "reachable": True}

    def tearDown(self): doorcheck.run = self._run

    def test_cli_and_action_counted_apart(self):
        cli, act, wp = self.n("free_check_started_cli"), self.n("free_check_started_action"), self.n("free_check_started_wp_plugin")
        server.handle_check({"url": "example.com", "lang": "en", "source": "cli"}, "9.9.8.1")
        self.assertEqual((self.n("free_check_started_cli"), self.n("free_check_started_action"), self.n("free_check_started_wp_plugin")), (cli + 1, act, wp))
        server.handle_check({"url": "example.org", "lang": "en", "source": "action"}, "9.9.8.2")
        self.assertEqual((self.n("free_check_started_cli"), self.n("free_check_started_action"), self.n("free_check_started_wp_plugin")), (cli + 1, act + 1, wp))
        server.handle_check({"url": "example.net", "lang": "en", "source": "wp-plugin"}, "9.9.8.3")
        self.assertEqual((self.n("free_check_started_cli"), self.n("free_check_started_action"), self.n("free_check_started_wp_plugin")), (cli + 1, act + 1, wp + 1))

    def test_other_sources_not_counted(self):
        before = [self.n(e) for e in ("free_check_started_cli", "free_check_started_action", "free_check_started_wp_plugin")]
        for src in (None, "", "ci", "CLI", "cli ", "wp_plugin", "other", 5, ["cli"], {"a": 1}, True):   # junk must neither count nor crash the handler
            code, body = server.handle_check({"url": "example.com", "lang": "en", **({} if src is None else {"source": src})}, "9.9.8.4")
            self.assertEqual(code, 200, repr(src))
        self.assertEqual([self.n(e) for e in ("free_check_started_cli", "free_check_started_action", "free_check_started_wp_plugin")], before)

    def test_own_ip_not_counted(self):
        server.INTERNAL_IPS.add("9.9.8.9")
        try:
            b = self.n("free_check_started_cli")
            server.handle_check({"url": "example.com", "lang": "en", "source": "cli"}, "9.9.8.9")
            self.assertEqual(self.n("free_check_started_cli"), b)
        finally: server.INTERNAL_IPS.discard("9.9.8.9")

    def test_private_address_is_bad_url(self):          # the CLI prints its "public sites only" line on this answer
        doorcheck.run = self._run
        for u in ("http://127.0.0.1/", "localhost", "http://10.0.0.5:80/", "http://[::1]/"):
            code, body = server.handle_check({"url": u, "lang": "en", "source": "cli"}, "9.9.8.5")
            self.assertEqual((code, body), (400, {"ok": False, "error": "bad_url"}), u)


class Contract(unittest.TestCase):
    """The CLI prints a label per check id. doorcheck must not start emitting an id or status the CLI has no label for."""

    def run_check(self, home, robots="", llms="", product=""):
        pages = {"/robots.txt": robots, "/": home, "/llms.txt": llms}
        def fetch(url, deadline=None, accept_lang="en", **k):
            path = "/" + url.split("//", 1)[1].split("/", 1)[-1] if url.count("/") > 2 else "/"
            body = pages.get(path.split("?")[0], product if "/products/" in path else "")
            return {"status": 200 if body or path == "/" else 404, "body": body, "url": url, "error": ""}
        orig = safefetch.fetch
        safefetch.fetch = fetch
        try: return doorcheck.run("https://shop.example", "en")
        finally: safefetch.fetch = orig

    def test_ids_and_statuses_are_known_to_the_cli(self):
        home = '<html><body>' + "word " * 300 + '<a href="/products/x">x</a><script type="application/ld+json">{"@type":"Organization","name":"S"}</script></body></html>'
        product = '<script type="application/ld+json">{"@type":"Product","offers":{"price":"1","availability":"InStock"}}</script>'
        with_product = self.run_check(home, robots="User-agent: GPTBot\nDisallow: /\n", llms="x" * 80, product=product)
        no_product = self.run_check("<html><body>" + "word " * 10 + "</body></html>")
        empty = self.run_check("<html></html>")
        seen_ids, seen_status = set(), set()
        for res in (with_product, no_product, empty):
            for c in res["checks"]:
                seen_ids.add(c["id"]); seen_status.add(c["status"])
        self.assertLessEqual(seen_ids, CLI_CHECK_IDS)
        self.assertLessEqual(seen_status, CLI_STATUSES)
        self.assertEqual(seen_ids, CLI_CHECK_IDS)       # every id is reachable here, so the pin cannot go stale the other way
        self.assertTrue({"pass", "fail", "warn", "na", "info", "unknown"} <= seen_status | {"unknown"})


if __name__ == "__main__":
    unittest.main()
