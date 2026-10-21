"""RES-2498: /free-ai-visibility-check in 5 locales is built, schema is WebPage + Service + Offer 0 + FAQPage with 5 questions, and the sitemap lists it."""
import json, os, re, subprocess, sys, unittest
HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = {"en": "public/free-ai-visibility-check.html", **{l: "public/%s/free-ai-visibility-check.html" % l for l in ("fr", "nl", "de", "es")}}

class T(unittest.TestCase):
    def test_built_files_are_current(self):
        r = subprocess.run([sys.executable, "tools/build_free_check.py", "--check"], cwd=HERE, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_schema_and_form(self):
        for l, p in PAGES.items():
            h = open(os.path.join(HERE, p), encoding="utf-8").read()
            g = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S).group(1))["@graph"]
            wp = next(x for x in g if x["@type"] == "WebPage")  # RES-2673: no WebApplication/SoftwareApplication (Google wants a rating or review)
            self.assertEqual((wp["mainEntity"]["@type"], wp["mainEntity"]["offers"]["@type"], wp["mainEntity"]["offers"]["price"]), ("Service", "Offer", "0"), l)
            self.assertNotIn("WebApplication", h); self.assertNotIn("SoftwareApplication", h)
            self.assertEqual(len(next(x for x in g if x["@type"] == "FAQPage")["mainEntity"]), 5, l)
            self.assertIn('action="/api/teaser"', h); self.assertIn('id="tzf"', h)
            for name in ("ChatGPT", "Claude", "Gemini", "Perplexity"): self.assertIn(name, re.search(r"<h1>.*?</h1>\s*<p class=\"lede\">.*?</p>", h, re.S).group(0), l)
            self.assertNotRegex(h, r"Claude (powers|runs)|AI-run")

    def test_sitemap(self):
        s = open(os.path.join(HERE, "public/sitemap.xml"), encoding="utf-8").read()
        self.assertEqual(len(re.findall(r"free-ai-visibility-check</loc>", s)), 5)

if __name__ == "__main__": unittest.main()
