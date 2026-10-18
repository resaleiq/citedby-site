"""Blog template (RES-1478): every article builds, has a 40-60 word answer, alt text on images, and its pages are in the sitemap."""
import glob, os, re, subprocess, sys, unittest
HERE = os.path.dirname(os.path.abspath(__file__))
class Blog(unittest.TestCase):
    def test_builds(self):
        r = subprocess.run([sys.executable, "tools/build_blog.py", "--check"], cwd=HERE, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr + r.stdout)
    def test_pages_in_sitemap_and_alt(self):
        sm = open(os.path.join(HERE, "public/sitemap.xml")).read()
        for f in glob.glob(os.path.join(HERE, "public/blog/*.html")):
            slug = os.path.basename(f)[:-5]
            loc = "https://citedby.eu/blog" + ("" if slug == "index" else "/" + slug)
            self.assertIn("<loc>%s</loc>" % loc, sm)
            self.assertFalse(re.findall(r'<img(?![^>]*\balt=")[^>]*>', open(f).read()))
if __name__ == "__main__": unittest.main()
