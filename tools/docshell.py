#!/usr/bin/env python3
"""One header, footer and stylesheet pair for the reading pages (RES-1551): terms, refund, privacy, legal, contact, bot, blog, guides, data.
`transform(html)` rewrites an old style.css page onto the saas.css shell and is idempotent. `python3 tools/docshell.py` applies it to every static page below.
Standard library only."""
import glob, hashlib, os, re

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC = os.path.join(HERE, "public")

TOPBAR = ('<a class="sr" href="#main">Skip to content</a>\n'
          '<header class="topbar"><div class="in"><a class="mark" href="/"><i></i>CitedBy</a>'
          '<nav aria-label="Main"><a class="opt" href="/#checks">What we check</a><a href="/plans">Pricing</a><a href="/blog">Guides</a><a class="opt" href="/data">Data</a></nav>'
          '<a class="signin" href="/signin?next=%2Fapp.html">Sign in</a><a class="btn sm go" href="/app.html#/new">Audit a site</a></div></header>')
FOOTER = ('<footer><div class="w"><span>© 2026 CitedBy · <a href="mailto:hello@citedby.eu">hello@citedby.eu</a></span>'
          '<a href="/plans">Pricing</a><a href="/blog">Guides</a><a href="/data">Data</a><a href="/methodology">Method</a><a href="/about">About</a><a href="/terms">Terms</a><a href="/privacy">Privacy</a>'
          '<a href="/refund">Refunds</a><a href="/contact">Contact</a><a href="/legal">Legal notice</a></div></footer>')


def ver(name="doc.css"):
    return hashlib.sha256(open(os.path.join(PUBLIC, name), "rb").read()).hexdigest()[:8]


def css_links():
    return f'<link rel="stylesheet" href="/saas.css"><link rel="stylesheet" href="/doc.css?v={ver()}">'


def transform(h):
    """Old shell -> new shell. Pages already on /doc.css only get the cache-buster refreshed."""
    if "/doc.css" in h:
        return re.sub(r'/doc\.css\?v=\w+', f'/doc.css?v={ver()}', h)
    h = re.sub(r'<link rel="stylesheet" href="/style\.css[^"]*">', css_links(), h, count=1)
    h = re.sub(r'<body( class="([^"]*)")?>', lambda m: f'<body class="cb dc{" " + m.group(2) if m.group(2) else ""}">', h, count=1)
    h = re.sub(r'<a class="skip" href="#main">[^<]*</a>\s*', '', h)
    h = re.sub(r'<header class="top">.*?</header>', lambda m: TOPBAR, h, count=1, flags=re.S)
    h = re.sub(r'<footer>.*?</footer>', lambda m: FOOTER, h, count=1, flags=re.S)
    h = h.replace('<main class="doc wide">', '<main id="main" class="wide">').replace('<main class="doc">', '<main id="main">')
    return h


TARGETS = ["about", "methodology", "terms", "refund", "privacy", "legal", "contact", "bot", "ai-visibility-audit", "blog/*", "guides/*", "data/*"]


def main():
    n = 0
    for pat in TARGETS:
        for p in sorted(glob.glob(os.path.join(PUBLIC, pat + ("" if "*" in pat else ".html")))):
            if not p.endswith(".html"):
                continue
            old = open(p, encoding="utf-8").read()
            new = transform(old)
            if new != old:
                open(p, "w", encoding="utf-8").write(new)
                n += 1
    print("rewrote", n, "pages")


if __name__ == "__main__":
    main()
