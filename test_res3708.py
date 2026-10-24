"""RES-3708: /api/check counts free_check_started_wp_plugin only for source=wp-plugin. Run: python3 test_res3708.py"""
import os, sqlite3, tempfile, unittest
os.environ.update(OPTIN_SECRET="x" * 40, BASE_URL="http://t", DATA_DIR=tempfile.mkdtemp())
import doorcheck, server


class T(unittest.TestCase):
    def n(self):
        c = sqlite3.connect(server.DB_PATH)
        try: return c.execute("SELECT coalesce(sum(n),0) FROM event_count WHERE type='free_check_started_wp_plugin'").fetchone()[0]
        finally: c.close()

    def test_source_counted(self):
        self.addCleanup(setattr, doorcheck, "run", doorcheck.run)  # other test files in the same process need the real one
        doorcheck.run = lambda root, lang: {"site": root, "checks": [], "reachable": True}
        b = self.n()
        server.handle_check({"url": "example.com", "lang": "en"}, "9.9.9.1")
        self.assertEqual(self.n(), b)
        server.handle_check({"url": "example.org", "lang": "en", "source": "wp-plugin"}, "9.9.9.2")
        server.handle_check({"url": "example.net", "lang": "en", "source": "other"}, "9.9.9.3")
        self.assertEqual(self.n(), b + 1)


if __name__ == "__main__":
    unittest.main()
