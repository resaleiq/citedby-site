"""RES-2666 items 2 and 4: localized pages link localized pages; no page links a redirect hop."""
import glob, os, re, unittest

PUB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")
LOCALIZED = ("plans", "sample", "about", "terms", "privacy", "refund", "blog", "tools")  # each exists at /xx/<page>
SWITCH = re.compile(r'<a [^>]*hreflang=')  # the footer language switch legitimately links the English page


def pages(lg):
    return [p for p in glob.glob(PUB + f"/{lg}/**/*.html", recursive=True) + [PUB + f"/landing.{lg}.html"]]


def anchors(h):
    h = re.sub(r"<footer>.*?</footer>", lambda m: re.sub(SWITCH.pattern + r"[^>]*>[^<]*</a>", "", m.group(0)), h, flags=re.S)
    return re.findall(r'<a [^>]*href="(/[^"#?]*)', h)


class LocalizedLinks(unittest.TestCase):
    def test_localized_pages_do_not_link_english_pages(self):
        bad = []
        for lg in ("fr", "nl", "de", "es"):
            for p in pages(lg):
                h = open(p, encoding="utf-8").read()
                if p.endswith(f"/{lg}/check.html") or p.endswith(f"/{lg}/privacy.html") or p.endswith(f"/{lg}/terms.html") or p.endswith(f"/{lg}/refund.html"):
                    continue  # legal pages carry an "English version" link by design
                for u in anchors(h):
                    first = u.strip("/").split("/")[0]
                    if first in LOCALIZED:
                        bad.append((os.path.relpath(p, PUB), u))
        self.assertEqual(bad, [])

    def test_no_link_points_at_a_redirect_hop(self):
        bad = []
        for p in glob.glob(PUB + "/**/*.html", recursive=True):
            h = open(p, encoding="utf-8").read()
            for u in re.findall(r'href="(/(?:[a-z]{2}/)?(?:sample-audit|check))"', h):
                if not p.endswith("check.html"):
                    bad.append((os.path.relpath(p, PUB), u))
        self.assertEqual(bad, [])


if __name__ == "__main__":
    unittest.main()
