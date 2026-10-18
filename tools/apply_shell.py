#!/usr/bin/env python3
"""Put the shared header, proof strip and footer (shell.py) into the static /data page (RES-1335 S2 check 1).
Usage: python3 tools/apply_shell.py   (idempotent: rewrites the blocks between the shell markers)"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
import shell
PAGES = {"data.html": "/data"}
HEAD_OLD = '<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n<link rel="stylesheet" href="/style.css"><link rel="stylesheet" href="/data.css">'
ICONS = ('<meta property="og:image" content="https://citedby.eu/og.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="https://citedby.eu/og.png">\n'
         '<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png"><link rel="icon" href="/favicon.ico" sizes="16x16 32x32 48x48"><link rel="apple-touch-icon" href="/apple-touch-icon.png">\n'
         '<link rel="preload" href="/fonts/newsreader-latin-600-normal.woff2" as="font" type="font/woff2" crossorigin>')


def apply(name, current):
    p = os.path.join(HERE, "..", "public", name)
    h = open(p, encoding="utf-8").read()
    head = ICONS + '\n<link rel="stylesheet" href="/style.css"><link rel="stylesheet" href="/data.css"><link rel="stylesheet" href="/site.css?v=%s">' % shell.asset_ver("site.css")
    if HEAD_OLD in h:
        h = h.replace(HEAD_OLD, "<!--shell:head-->" + head + "<!--/shell:head-->")
    else:
        h = re.sub(r"<!--shell:head-->.*?<!--/shell:head-->", lambda m: "<!--shell:head-->" + head + "<!--/shell:head-->", h, flags=re.S)
    top = "<!--shell:header-->" + shell.header("en", current) + "<!--/shell:header-->"
    h = re.sub(r"<header class=\"top\">.*?</header>|<!--shell:header-->.*?<!--/shell:header-->", lambda m: top, h, count=1, flags=re.S)
    bot = "<!--shell:footer-->" + shell.footer("en") + "<!--/shell:footer-->"
    h = re.sub(r"<footer>.*?</footer>|<!--shell:footer-->.*?<!--/shell:footer-->", lambda m: bot, h, count=1, flags=re.S)
    open(p, "w", encoding="utf-8").write(h)


if __name__ == "__main__":
    for n, c in PAGES.items():
        apply(n, c)
        print("shell applied to", n)
