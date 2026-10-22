"""RES-1731 row 10: /fr /nl /de /es are real translated pages with canonical + hreflang. Run: OPTIN_SECRET=xxxxxxxx... python3.12 test_localize.py"""
import os, re, sys, unittest
os.environ.setdefault("OPTIN_SECRET", "x" * 40)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util, langroutes
_s = importlib.util.spec_from_file_location("localize_landing", os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools", "localize_landing.py")); L = importlib.util.module_from_spec(_s); _s.loader.exec_module(L)

class T(unittest.TestCase):
    def test_free_check_form_is_in_every_language(self):
        """RES-1836: the hero has the no-account teaser form in the page's own language (the generator was retired in RES-1785: the four pages are edited by hand now)."""
        for lang in L.LANGS:
            d = open(os.path.join(L.PUB, f"landing.{lang}.html"), encoding="utf-8").read()
            self.assertIn('id="tzf" action="/api/teaser"', d); self.assertIn('name="fax"', d); self.assertIn('id="tzn"', d)
            self.assertNotIn("Check my site free", d); self.assertNotIn("Free, no account", d)
            self.assertNotIn('action="/app.html#/new"', d)
            self.assertIn('rel="preload" href="/fonts/newsreader-latin-600-normal.woff2"', d)

    def test_every_page_has_canonical_and_five_hreflangs(self):
        for lang, path in (("en", ""), ("fr", "/fr"), ("nl", "/nl"), ("de", "/de"), ("es", "/es")):
            f = "landing.html" if lang == "en" else f"landing.{lang}.html"
            doc = langroutes.head(open(os.path.join(L.PUB, f), encoding="utf-8").read(), lang)
            self.assertIn(f'<html lang="{lang}">', doc)
            self.assertIn(f'<link rel="canonical" href="https://citedby.eu{path or "/"}">', doc)
            self.assertEqual(len(re.findall(r'rel="alternate" hreflang="', doc)), 6)  # en fr nl de es x-default
            for c, p in (("en", "/"), ("fr", "/fr"), ("nl", "/nl"), ("de", "/de"), ("es", "/es"), ("x-default", "/")):
                self.assertIn(f'hreflang="{c}" href="https://citedby.eu{p}"', doc)

    def test_translations_are_not_english(self):
        for lang, must, banned in (("fr", "Votre audit affiche 300 erreurs", "Which ones actually matter"), ("nl", "Je SEO-tool toont 300 fouten", "300 errors"), ("de", "Ihr SEO-Tool meldet 300 Fehler", "300 errors"), ("es", "Tu auditoría marca 300 errores", "300 errors")):
            d = open(os.path.join(L.PUB, f"landing.{lang}.html"), encoding="utf-8").read()
            self.assertIn(must, d); self.assertNotIn(banned, d)
            self.assertNotIn("<summary>What do I get", d)  # the stray English toggle (RES-1753) is gone
            self.assertIn(f'href="/{lang}/plans?plan=', d); self.assertNotIn('href="/plans', d)  # RES-1897: pricing buttons pre-select their plan
            for w in ("Run my audit", "Questions</h2>", "Recommended", "Skip to content"): self.assertNotIn(w, d)

    def test_no_ai_wording_as_method(self):
        for lang in L.LANGS:
            d = open(os.path.join(L.PUB, f"landing.{lang}.html"), encoding="utf-8").read().lower()
            for w in ("claude haiku", "openrouter", "anthropic", "gpt-4"): self.assertNotIn(w, d)
            self.assertIsNone(re.search(r"\bllms?\b(?!\.txt|-txt)", d))

    def test_routes(self):
        self.assertEqual(langroutes.LANDING_PATHS, {"/fr": "fr", "/nl": "nl", "/de": "de", "/es": "es"})
        src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "server.py")).read()
        self.assertNotIn('LAUNCH_REDIRECTS = {"/fr"', src); self.assertIn("langroutes.head(", src)

if __name__ == "__main__": unittest.main()
