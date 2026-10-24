"""RES-4124: a bare host.tld/path in a table cell sits in span.u (or a link / code), so only the address may break mid-word at 390/360."""
import glob, os, re, sys, unittest
HERE = os.path.dirname(os.path.abspath(__file__)); PUB = os.path.join(HERE, "public")
sys.path.insert(0, os.path.join(HERE, "tools"))
TD = re.compile(r"<td[^>]*>((?:(?!</td>).)*)</td>", re.S)
BARE = re.compile(r"(?<![\w./@-])[a-z0-9-]+(?:\.[a-z0-9-]+)*\.[a-z]{2,}/\S+")


class TableUrls(unittest.TestCase):
    def test_no_bare_address_in_a_cell(self):
        bad, cells = [], 0
        for f in glob.glob(os.path.join(PUB, "**", "*.html"), recursive=True):
            for m in TD.finditer(open(f, encoding="utf-8").read()):
                cells += 1
                c = re.sub(r'<a\b.*?</a>|<code>.*?</code>|<span class="u">.*?</span>', "", m.group(1), flags=re.S)
                bad += [(os.path.relpath(f, PUB), t[:60]) for t in BARE.findall(re.sub(r"<[^>]+>", "", c))]
        self.assertGreater(cells, 500)
        self.assertEqual(bad, [])

    def test_bots_pages_carry_the_span(self):
        for slug, host in (("googlebot", "developers.google.com/static/search/apis/ipranges/googlebot.json"), ("amazonbot", "developer.amazon.com/amazonbot/ip-addresses")):
            self.assertIn('<span class="u">%s</span>' % host, open(os.path.join(PUB, "bots", slug + ".html"), encoding="utf-8").read())

    def test_css_breaks_only_the_address(self):
        css = open(os.path.join(PUB, "blog.css"), encoding="utf-8").read()
        self.assertIn(".art td,.art th{overflow-wrap:break-word}", css)  # RES-3935: words stay whole
        self.assertIn(".art td .u{overflow-wrap:anywhere}", css)
        self.assertIn(".art .tw.stack td[data-label='']{font-weight:600}", css)  # stacked card title with an empty header

    def test_builder_wraps_and_leaves_links_and_code(self):
        src = open(os.path.join(HERE, "tools", "build_blog.py"), encoding="utf-8").read()
        ns = {"re": re, "inline": lambda s: s.replace("`a.io/x`", "<code>a.io/x</code>")}
        exec(src[src.index("BARE_URL = "):src.index("def plain")], ns)
        cell = ns["cell"]
        self.assertEqual(cell("see developer.amazon.com/a/b-c)."), 'see <span class="u">developer.amazon.com/a/b-c</span>).')
        self.assertEqual(cell("x.json (openai.com/gptbot.json, dated)"), 'x.json (<span class="u">openai.com/gptbot.json</span>, dated)')
        self.assertEqual(cell("`a.io/x`"), "<code>a.io/x</code>")
        self.assertEqual(cell('<a href="https://a.io/x">a.io/x</a>'), '<a href="https://a.io/x">a.io/x</a>')
        self.assertEqual(cell("plain words 2026-10-20 e.g. ok"), "plain words 2026-10-20 e.g. ok")


if __name__ == "__main__":
    unittest.main()
