"""RES-3275 S6 (dogfood): no page's meta, og or twitter description is a cut with an ellipsis; the legal pages carry whole sentences."""
import glob, re, os

def test_no_description_ends_with_an_ellipsis():
    bad = []
    for f in glob.glob(os.path.join("public", "**", "*.html"), recursive=True):
        h = open(f, encoding="utf-8").read()
        for m in re.finditer(r'(?:name="description"|property="og:description"|name="twitter:description") content="([^"]*)"', h):
            if m.group(1).rstrip().endswith(("...", "…")): bad.append((f, m.group(1)[-50:]))
    assert not bad, bad

def test_legal_page_descriptions_are_whole_sentences_of_70_to_155_characters():
    import html
    for page in ("privacy", "terms", "refund"):
        for lang in ("", "fr/", "nl/", "de/", "es/"):
            h = open(f"public/{lang}{page}.html", encoding="utf-8").read()
            d = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', h).group(1))
            assert 70 <= len(d) <= 155 and d.endswith((".", "?")) and d in h.replace("&#x27;", "'"), (lang, page, d)
