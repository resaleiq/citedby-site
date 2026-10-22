"""RES-2651 row 46: /changes in 5 locales and the RSS feeds come from data/engine-changes.json and say, per entry, whether CitedBy checks it."""
import json, os, re, subprocess, sys, unittest, xml.dom.minidom
HERE = os.path.dirname(os.path.abspath(__file__)); PUB = os.path.join(HERE, "public")
sys.path.insert(0, os.path.join(HERE, "tools"))
import build_changes as B
REC = json.load(open(os.path.join(HERE, "data", "engine-changes.json"), encoding="utf-8"))


def page(l): return open(os.path.join(PUB, B.path(l).lstrip("/") + ".html"), encoding="utf-8").read()


class Changes(unittest.TestCase):
    def test_built_files_are_current(self):
        self.assertEqual(subprocess.run([sys.executable, os.path.join(HERE, "tools", "build_changes.py"), "--check"], capture_output=True).returncode, 0)

    def test_every_record_in_every_locale_with_date_quote_and_link(self):
        for l in B.LANGS:
            h = page(l)
            self.assertIn('<html lang="%s">' % l, h)
            self.assertEqual(h.count("<article "), len(REC))
            for r in REC:
                self.assertIn('id="%s"' % r["id"], h); self.assertIn('datetime="%s"' % r["date"], h)
                self.assertIn(B.E(r["quote"]), h, (l, r["id"])); self.assertIn(B.E(r["source_url"]), h)
            self.assertEqual(len(re.findall(r'class="chip ', h)), len(REC))

    def test_newest_first(self):
        for l in B.LANGS:
            d = re.findall(r'<time datetime="([\d-]+)"', page(l)); self.assertEqual(d, sorted(d, reverse=True))

    def test_no_english_source_strings_in_other_locales(self):
        for l in B.LANGS[1:]:
            h = page(l)
            for r in REC:
                self.assertNotIn(B.E(r["owner_action"]), h, (l, r["id"]))
            for w in ("What you can do", "What CitedBy checks", "Newest first", "Not checked<", "Checked<"):
                self.assertNotIn(w, h, (l, w))
            self.assertNotIn("Audit my site", h)

    def test_each_entry_has_all_five_texts(self):
        for r in REC:
            self.assertEqual(set(B.C[r["id"]]), set(B.LANGS), r["id"])
        self.assertEqual({r["id"] for r in REC}, set(B.C))

    def test_checked_lines_match_code_claims(self):
        st = {i: v["en"][2] for i, v in B.C.items()}
        self.assertEqual(st["google-llms-txt-guidance"], "Y"); self.assertEqual(st["lighthouse-agentic-browsing-category"], "P")
        self.assertEqual(sum(1 for v in st.values() if v == "N"), len(st) - 2)

    def test_rss_parses_and_has_one_item_per_record(self):
        for l in B.LANGS:
            p = os.path.join(PUB, B.path(l, ".xml").lstrip("/")); d = xml.dom.minidom.parse(p)
            self.assertEqual(len(d.getElementsByTagName("item")), len(REC))
            self.assertIn('rel="alternate" type="application/rss+xml"', page(l))
            self.assertEqual(len(set(g.firstChild.data for g in d.getElementsByTagName("guid"))), len(REC))

    def test_sitemap_and_llms(self):
        s = open(os.path.join(PUB, "sitemap.xml"), encoding="utf-8").read()
        for l in B.LANGS: self.assertEqual(s.count("<loc>https://citedby.eu%s</loc>" % B.path(l)), 1)
        self.assertEqual(open(os.path.join(PUB, "llms.txt"), encoding="utf-8").read().count("(https://citedby.eu/changes)"), 1)

    def test_no_ranking_lever_or_ai_engine_claims(self):
        for l in B.LANGS:
            t = re.sub(r"<[^>]+>", " ", page(l)).lower()
            for w in ("claude to ", "powered by", "guarantee ranking", "boost your ranking"): self.assertNotIn(w, t)


if __name__ == "__main__":
    unittest.main()
