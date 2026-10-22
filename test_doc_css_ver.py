"""RES-2986: every public page links the current doc.css?v=<sha256[:8]>, so a cached older copy is never kept."""
import glob, os, re, sys, unittest
HERE = os.path.dirname(os.path.abspath(__file__)); PUB = os.path.join(HERE, "public")
sys.path.insert(0, os.path.join(HERE, "tools"))
import docshell


class DocCssVer(unittest.TestCase):
    def test_every_link_is_current(self):
        want, bad, seen = docshell.ver(), [], 0
        for f in glob.glob(os.path.join(PUB, "**", "*.html"), recursive=True):
            for v in re.findall(r"/doc\.css\?v=(\w+)", open(f, encoding="utf-8").read()):
                seen += 1
                if v != want: bad.append((os.path.relpath(f, PUB), v))
        self.assertGreater(seen, 100)
        self.assertEqual(bad, [])


if __name__ == "__main__":
    unittest.main()
