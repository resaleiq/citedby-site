"""RES-1459 row 6: no tea/coffee study pages, roaster example or example-roaster.be anywhere in the shipped site."""
import glob, re, os
HERE = os.path.dirname(os.path.abspath(__file__))
SLUGS = ("the-france", "cafe-france", "cafe-belgique", "koffie-belgie", "coffee-ireland")

def test_retired_pages_not_shipped():
    for n in SLUGS:
        for ext in (".html", ".csv"):
            assert not os.path.exists(os.path.join(HERE, "public", "data", n + ext)), n + ext

def test_no_links_or_roaster_text():
    bad = []
    for f in glob.glob(os.path.join(HERE, "public", "**", "*"), recursive=True) + [os.path.join(HERE, "pages.py")] + glob.glob(os.path.join(HERE, "content", "blog", "*.md")):
        if not os.path.isfile(f) or f.endswith((".pdf", ".png", ".woff2", ".ico", ".csv", ".jpg", ".webp")): continue
        s = open(f, encoding="utf-8", errors="ignore").read().lower()
        if any("/data/" + n in s for n in SLUGS) or "example-roaster" in s or "coffee roaster" in s:
            bad.append(os.path.relpath(f, HERE))
    assert not bad, bad
