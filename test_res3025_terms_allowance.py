"""RES-3025: every locale's /terms plan rows state 10 / 160 / 800 crawls per 30 days (cf60f97 dropped them x4)."""
import os, re, unittest

PUB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")
PAGES = {"en": "terms.html", "fr": "fr/terms.html", "nl": "nl/terms.html", "de": "de/terms.html", "es": "es/terms.html"}


class TermsAllowance(unittest.TestCase):
    def test_each_plan_row_has_allowance(self):
        for lang, p in PAGES.items():
            t = open(os.path.join(PUB, p), encoding="utf-8").read()
            for n in ("10", "160", "800"):
                self.assertTrue(re.search(r"(?<![\d.,])%s (crawls|analyses|Crawls|rastreos)\b" % n, t), (lang, n))

    def test_single_row_has_no_30_day_access(self):
        for lang, p in PAGES.items():
            t = open(os.path.join(PUB, p), encoding="utf-8").read()
            row = re.search(r"<tbody><tr>.*?</tr>", t, re.S).group(0)
            self.assertNotRegex(row, r"30 (days|jours|dagen|Tage|días)", lang)


if __name__ == "__main__":
    unittest.main()
