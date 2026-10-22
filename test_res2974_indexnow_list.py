"""RES-2974: /privacy names every IndexNow participant in the registry (Internet Archive included) x5."""
import pathlib
import unittest

ROOT = pathlib.Path(__file__).parent / "public"
PAGES = ["privacy.html", "nl/privacy.html", "de/privacy.html", "fr/privacy.html", "es/privacy.html"]
ENGINES = ["Amazon", "Bing", "Internet Archive", "Naver", "Seznam.cz", "Yandex", "Yep"]


class IndexNowList(unittest.TestCase):
    def test_every_participant_named_and_registry_linked(self):
        for p in PAGES:
            t = (ROOT / p).read_text(encoding="utf8")
            self.assertIn("https://www.indexnow.org/searchengines.json", t, p)
            i = t.index("Amazon, Bing")
            seg = t[i:i + 120]
            for e in ENGINES:
                self.assertIn(e, seg, (p, e))

    def test_section5_names_internet_archive_as_us(self):
        for p in PAGES:
            t = (ROOT / p).read_text(encoding="utf8")
            s5 = t[t.index("<h2>5."):t.index("<h2>6.")]
            self.assertIn("Internet Archive", s5, p)


if __name__ == "__main__":
    unittest.main()
