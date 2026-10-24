#!/usr/bin/env python3
"""One header, footer and stylesheet pair for the reading pages (RES-1551): terms, refund, privacy, legal, contact, bot, blog, guides, data.
`transform(html)` rewrites an old style.css page onto the saas.css shell and is idempotent. `python3 tools/docshell.py` applies it to every static page below.
Standard library only."""
import glob, hashlib, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC = os.path.join(HERE, "public")

TOPBAR = ('<a class="sr" href="#main">Skip to content</a>\n'
          '<header class="topbar"><div class="in"><a class="mark" href="/"><i></i>CitedBy</a>'
          '<nav aria-label="Main"><a class="opt" href="/#checks">What we check</a><a href="/plans">Pricing</a><a href="/blog">Guides</a><a class="opt" href="/data">Data</a></nav>'
          '<a class="signin" href="/signin?next=%2Fapp.html">Sign in</a><a class="btn sm go" href="/app.html#/new">Audit a site</a></div></header>')
FOOTER = ('<footer><div class="w"><span>© 2026 CitedBy · <a href="mailto:hello@citedby.eu">hello@citedby.eu</a></span>'
          '<a href="/plans">Pricing</a><a href="/blog">Guides</a><a href="/data">Data</a><a href="/methodology">Method</a><a href="/about">About</a><a href="/terms">Terms</a><a href="/privacy">Privacy</a>'
          '<a href="/refund">Refunds</a><a href="/contact">Contact</a><a href="/legal">Legal notice</a></div></footer>')


# RES-2616: fr/nl/de/es reading pages get the localized masthead and footer (labels from build_legal.UI), links to the page of that language where one exists
EXTRA = {"fr": ("Méthode", "À propos"), "nl": ("Methode", "Over ons"), "de": ("Methode", "Über uns"), "es": ("Método", "Sobre nosotros")}


def localize(h):
    m = re.search(r'<html lang="(fr|nl|de|es)"', h)
    if not m or TOPBAR not in h and FOOTER not in h:
        return h
    lg = m.group(1)
    import build_legal as L
    t, (meth, about) = L.UI[lg], EXTRA[lg]
    top = (f'<a class="sr" href="#main">{t["skip"]}</a>\n<header class="topbar"><div class="in"><a class="mark" href="{t["home"]}"><i></i>CitedBy</a>'
           f'<nav aria-label="{t["main"]}"><a class="opt" href="{t["home"]}#checks">{t["check"]}</a><a href="{t["plans_h"]}">{t["plans"]}</a><a href="{t["blog_h"]}">{t["blog"]}</a><a class="opt" href="/data">{t["data"]}</a></nav>'
           f'<a class="signin" href="/signin?next=%2Fapp.html">{t["signin"]}</a><a class="btn sm go" href="/app.html#/new">{t["cta"]}</a></div></header>')
    foot = (f'<footer><div class="w"><span>© 2026 CitedBy · <a href="mailto:hello@citedby.eu">hello@citedby.eu</a></span>'
            f'<a href="{t["plans_h"]}">{t["plans"]}</a><a href="{t["blog_h"]}">{t["blog"]}</a><a href="/data">{t["data"]}</a><a href="/methodology">{meth}</a><a href="/{lg}/about">{about}</a>'
            f'<a href="/{lg}/terms">{t["terms"]}</a><a href="/{lg}/privacy">{t["privacy"]}</a><a href="/{lg}/refund">{t["refund"]}</a><a href="/contact">{t["contact"]}</a><a href="/legal">{t["legal"]}</a></div></footer>')
    return h.replace(TOPBAR, top).replace(FOOTER, foot)


def ver(name="doc.css"):
    return hashlib.sha256(open(os.path.join(PUBLIC, name), "rb").read()).hexdigest()[:8]


def css_links():
    return f'<link rel="stylesheet" href="/saas.css"><link rel="stylesheet" href="/doc.css?v={ver()}">'


def transform(h):
    """Old shell -> new shell. Pages already on /doc.css only get the cache-buster refreshed."""
    if "/doc.css" in h:
        return localize(re.sub(r'/doc\.css\?v=\w+', f'/doc.css?v={ver()}', h))
    h = re.sub(r'<link rel="stylesheet" href="/style\.css[^"]*">', css_links(), h, count=1)
    h = re.sub(r'<body( class="([^"]*)")?>', lambda m: f'<body class="cb dc{" " + m.group(2) if m.group(2) else ""}">', h, count=1)
    h = re.sub(r'<a class="skip" href="#main">[^<]*</a>\s*', '', h)
    h = re.sub(r'<header class="top">.*?</header>', lambda m: TOPBAR, h, count=1, flags=re.S)
    h = re.sub(r'<footer>.*?</footer>', lambda m: FOOTER, h, count=1, flags=re.S)
    h = h.replace('<main class="doc wide">', '<main id="main" class="wide">').replace('<main class="doc">', '<main id="main">')
    return localize(h)


TARGETS = ["about", "fr/about", "nl/about", "de/about", "es/about", "methodology", "terms", "refund", "privacy", "legal", "contact", "bot", "ai-visibility-audit", "blog/*", "guides/*", "bots", "bots/*", "data/*"]


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

SLOT_BLOCKS = ("pre", "table", "ul", "ol", "blockquote", "figure", "details", "aside", "section", "nav")
def slot_index(lines, cut):
    """First line index at or after cut where every pre/table/list opened before it is closed again (the ad slot or its placeholder comment goes there); the nearest one before cut if none after; None if the body has no top-level boundary."""
    depth = [0]
    for ln in lines:
        d = depth[-1]
        for m in re.finditer(r"<(/?)(%s)\b" % "|".join(SLOT_BLOCKS), ln):
            d += -1 if m.group(1) else 1
        depth.append(d)
    after = [i for i in range(cut, len(lines)) if depth[i] == 0]
    if after: return after[0]
    before = [i for i in range(cut - 1, 0, -1) if depth[i] == 0]
    return before[0] if before else None
