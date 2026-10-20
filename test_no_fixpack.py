import pathlib, re, unittest

ROOT = pathlib.Path(__file__).parent / "public"
PAT = re.compile(r"fix ?pack|€ ?390|390 ?€|390 EUR", re.I)
SKIP = {"privacy.html", "style.css"}  # privacy keeps the historic event name


class NoFixPack(unittest.TestCase):
    def test_public_pages_do_not_sell_the_fix_pack(self):
        bad = [str(p.relative_to(ROOT)) for p in ROOT.rglob("*")
               if p.suffix in (".html", ".txt", ".xml") and p.name not in SKIP and PAT.search(p.read_text(errors="ignore"))]
        self.assertEqual(bad, [])

    def test_terms_have_no_empty_section(self):
        s = (ROOT / "terms.html").read_text()
        self.assertNotRegex(s, r"</h2>\s*<h2>")


if __name__ == "__main__":
    unittest.main()
