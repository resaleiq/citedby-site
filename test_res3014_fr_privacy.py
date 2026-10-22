"""RES-3014 L2: /fr/privacy keeps a colon with the word before it (narrow no-break space), so it cannot wrap to the start of a line at 390."""
import re, pathlib

def test_fr_privacy_has_no_plain_space_before_french_punctuation():
    s = (pathlib.Path(__file__).parent / "public/fr/privacy.html").read_text(encoding="utf-8")
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", s, flags=re.S); t = re.sub(r"<[^>]+>", "\x00", s)
    assert not re.findall(r"[^\s  ] [:;?!»]", t)
