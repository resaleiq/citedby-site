"""RES-2203: the footer's Privacy / Terms / Refund links go to the visitor's language (/fr/privacy ...). Added at serve time, like withdraw_link, so every
page (static, generated or proxied from the app) gets it from its own <html lang>. English pages pass through."""
import re

LANGS = ("fr", "nl", "de", "es")
_LANG = re.compile(rb'<html[^>]*\blang="?([a-z]{2})')
_FOOTER = re.compile(rb"<footer\b.*?</footer>", re.S)
_HREF = re.compile(rb'href="/(privacy|terms|refund)(?=["?#])')


def localize(body):
    if b"<html" not in body[:600].lower() or b"<footer" not in body: return body
    m = _LANG.search(body[:600])
    lg = m.group(1).decode() if m else "en"
    if lg not in LANGS: return body
    return _FOOTER.sub(lambda f: _HREF.sub(lambda h: b'href="/' + lg.encode() + b"/" + h.group(1), f.group(0)), body)
