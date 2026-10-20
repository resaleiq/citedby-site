"""Share tags for every HTML page we serve (RES-2106): og:title, og:description, og:image and twitter:card are added from the page's own <title> and
meta description when the page lacks them, so a page that already carries its own is left alone. Standard library only."""
import re

IMG = "https://citedby.eu/og.png"  # 1200x630
_TITLE = re.compile(rb"<title>(.*?)</title>", re.S)
_DESC = re.compile(rb'<meta name="?description"? content="([^"]*)"')


def ensure(body):
    m = _TITLE.search(body)
    if not m or b"<html" not in body[:400].lower():
        return body
    head = body[:body.find(b"</head>")] if b"</head>" in body else body[:6000]
    d = _DESC.search(head)
    add = b""
    def has(k): return (b'property="%s"' % k) in head or (b'name="%s"' % k) in head
    q = lambda b: b.replace(b'"', b"&quot;")
    if not has(b"og:title"): add += b'<meta property="og:title" content="' + q(m.group(1)) + b'">'
    if d and not has(b"og:description"): add += b'<meta property="og:description" content="' + d.group(1) + b'">'
    if not has(b"og:image"): add += b'<meta property="og:image" content="' + IMG.encode() + b'">'
    if not has(b"og:type"): add += b'<meta property="og:type" content="website">'
    if not has(b"twitter:card"): add += b'<meta name="twitter:card" content="summary_large_image">'
    if not has(b"twitter:image"): add += b'<meta name="twitter:image" content="' + IMG.encode() + b'">'
    return body[:m.end()] + add + body[m.end():] if add else body
