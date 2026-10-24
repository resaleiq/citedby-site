"""Blog template (RES-1478): every article builds, has a 40-60 word answer, alt text on images, and its pages are in the sitemap."""
import glob, html, os, re, subprocess, sys, unittest
HERE = os.path.dirname(os.path.abspath(__file__))
class Blog(unittest.TestCase):
    def test_builds(self):
        r = subprocess.run([sys.executable, "tools/build_blog.py", "--check"], cwd=HERE, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr + r.stdout)
    def test_ad_slot_never_inside_code_table_or_list(self):  # RES-3935 F2: the marker (or the ad) was cut into two <pre> examples
        for f in glob.glob(os.path.join(HERE, "public/**/*.html"), recursive=True):
            s = open(f, encoding="utf-8").read()
            for tag in ("pre", "table", "ul", "ol"):
                for m in re.finditer(r"<%s\b.*?</%s>" % (tag, tag), s, re.S):
                    self.assertNotIn("ad-slot", m.group(0), "%s: ad-slot inside <%s>" % (f, tag))
    def test_wide_tables_stack_with_labels_on_phones(self):  # RES-4048: 3+ column tables overflowed their column at 390/360 (the last column was cut mid-word)
        seen = 0
        for f in glob.glob(os.path.join(HERE, "public/**/*.html"), recursive=True):
            s = open(f, encoding="utf-8").read()
            for m in re.finditer(r'<div class="(tw[^"]*)"><table><thead><tr>(.*?)</tr></thead><tbody>(.*?)</tbody></table></div>', s, re.S):
                cls, head, body = m.groups()
                if "/blog/" not in f and "/guides/" not in f: continue
                heads = [re.sub(r"<[^>]+>", "", h) for h in re.findall(r"<th[^>]*>(.*?)</th>", head, re.S)]
                if len(heads) < 3: self.assertNotIn("stack", cls.split(), f); continue
                seen += 1
                self.assertIn("stack", cls.split(), f)
                for row in re.findall(r"<tr>(.*?)</tr>", body, re.S):
                    labs = re.findall(r'<td data-label="([^"]*)">', row)
                    self.assertEqual([html.unescape(l) for l in labs], heads, f)
        self.assertGreater(seen, 15)
        css = open(os.path.join(HERE, "public/blog.css"), encoding="utf-8").read()
        for sel in (".art .tw.stack td::before{content:attr(data-label)", "@media(max-width:480px){.art .tw.stack table"): self.assertIn(sel, css)
    def test_slot_index_only_at_top_level(self):
        sys.path.insert(0, os.path.join(HERE, "tools")); import docshell
        lines = ["<p>a</p>", "<pre><code>x", "", "y</code></pre>", "<ul>", "<li>q</li>", "</ul>", "<p>b</p>", "<p>c</p>"]
        for cut in range(1, len(lines)):
            i = docshell.slot_index(lines, cut)
            before = "\n".join(lines[:i])
            self.assertEqual(before.count("<pre"), before.count("</pre>")); self.assertEqual(before.count("<ul"), before.count("</ul>"))
        self.assertEqual(docshell.slot_index(lines, 2), 4)  # cut inside the code block moves to after it
        self.assertEqual(docshell.slot_index(lines, 5), 7)  # cut inside the list moves to after it
        self.assertIsNone(docshell.slot_index(["<ul>", "<li>x</li>", "</ul>"][:2], 1))
    def test_own_repo_is_not_an_outside_source(self):  # RES-3935 L2: the byline counted github.com/resaleiq/citedby-check
        art = open(os.path.join(HERE, "public/blog/ai-crawler-check-in-ci.html"), encoding="utf-8").read()
        self.assertIn("2 sources", art); self.assertNotIn("3 sources", art)
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
