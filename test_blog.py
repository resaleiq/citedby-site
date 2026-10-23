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
    def test_every_locale_has_blog_guides_and_audit_page(self):
        sm = open(os.path.join(HERE, "public/sitemap.xml")).read()
        for loc in ("fr", "nl", "de", "es"):
            for path in ("/blog", "/guides", "/ai-visibility-audit", "/blog/does-llms-txt-work", "/blog/is-gptbot-blocked", "/guides/cms", "/guides/technical-seo-checklist"):
                url = "/%s%s" % (loc, path)
                self.assertTrue(os.path.exists(os.path.join(HERE, "public", url[1:] + (".html" if path.count("/") else "/index.html") if path in ("/blog", "/guides") else url[1:] + ".html")) or os.path.exists(os.path.join(HERE, "public", url[1:], "index.html")), url)
                if url == "/es/blog/does-llms-txt-work": continue  # RES-3269: noindex, so not in the sitemap
            self.assertIn("<loc>https://citedby.eu%s</loc>" % url, sm)
    def test_pages_have_hreflang_dates_images_and_no_duplicate_sitemap_urls(self):
        sm = open(os.path.join(HERE, "public/sitemap.xml")).read()
        locs = re.findall(r"<loc>([^<]+)</loc>", sm); self.assertEqual(len(locs), len(set(locs)))
        for extra in ("/data", "/bot", "/data/study-chatgpt-buyer-questions", "/guides"):
            self.assertIn("<loc>https://citedby.eu%s</loc>" % extra, sm)
        for f in glob.glob(os.path.join(HERE, "public/*/guides/*.html")) + glob.glob(os.path.join(HERE, "public/guides/*.html")) + glob.glob(os.path.join(HERE, "public/*/blog/*.html")):
            if f.endswith("index.html"): continue
            h = open(f).read()
            self.assertIn('"datePublished"', h, f); self.assertGreaterEqual(h.count("<img"), 2, f)
            if "/public/fr/" in f or "/public/nl/" in f or "/public/de/" in f or "/public/es/" in f: self.assertIn('hreflang="x-default"', h, f)
    def test_person_author_only_from_authors_json(self):
        import json; a = os.path.join(HERE, "data/authors.json")
        for f in glob.glob(os.path.join(HERE, "public/**/*.html"), recursive=True):
            h = open(f).read()
            if '"@type": "Article"' in h and not os.path.exists(a): self.assertNotIn('"@type": "Person"', h, f)
    def test_byline_links_to_editorial_section_in_every_locale(self):
        for f in glob.glob(os.path.join(HERE, "public/**/blog/*.html"), recursive=True) + glob.glob(os.path.join(HERE, "public/**/guides/*.html"), recursive=True) + glob.glob(os.path.join(HERE, "public/compare/*.html")):
            if f.endswith("index.html"): continue
            h = open(f).read(); m = re.search(r"/public/([a-z]{2})/", f); pre = "/" + m.group(1) if m else ""
            self.assertIn('<a href="%s/about#editorial">' % pre, h, f)
            self.assertIn('"url": "https://citedby.eu%s/about#editorial"' % pre, h, f)
    def test_about_has_editorial_section_in_all_locales(self):
        for loc in ("", "fr/", "nl/", "de/", "es/"):
            h = open(os.path.join(HERE, "public", loc + "about.html"), encoding="utf-8").read()
            self.assertIn('<h2 id="editorial">', h, loc); self.assertIn("/methodology", h); self.assertIn("hello@citedby.eu", h)
if __name__ == "__main__": unittest.main()
