#!/usr/bin/env python3
"""RES-2935: write public/llms-full.txt, the plain text of the site's English key pages (home, about, method, crawler, hubs, guides, bot and platform pages), so an assistant that wants
the content in one fetch gets it. Built from the committed pages; `--check` exits 1 if the committed file differs. Standard library only.
Run after any change to those pages (test_seo_gate.py fails when the file is stale)."""
import html, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PUB = os.path.join(ROOT, "public"); SITE = "https://citedby.eu"
HEAD = ("# CitedBy: full text of the key pages\n\n> The plain text of the English pages listed in /llms.txt, in one file. "
        "CitedBy crawls your site up to your plan's page limit and gives the exact fix for each issue. The only domain is citedby.eu.\n")
FIRST = ["/", "/about", "/methodology", "/data", "/bot", "/bots", "/platforms", "/guides", "/blog"]


def pages():
    out = list(FIRST)
    for d in ("guides", "bots", "platforms", "blog"):
        out += sorted("/%s/%s" % (d, f[:-5]) for f in os.listdir(os.path.join(PUB, d)) if f.endswith(".html") and f != "index.html")
    return list(dict.fromkeys(out))


def file_for(path):
    if path == "/": return os.path.join(PUB, "landing.html")
    for c in (PUB + path + ".html", PUB + path + "/index.html"):
        if os.path.exists(c): return c


def text(h):
    m = re.search(r"<main\b.*?</main>", h, re.S) or re.search(r"<body\b.*</body>", h, re.S)
    t = re.sub(r"<!--N-->.*?<!--/N-->", "", m.group(0), flags=re.S)  # the no-trial wording of the home page: the live site runs with the trial on (server.landing_html)
    t = re.sub(r"<(script|style|svg|form)\b.*?</\1>|<!--.*?-->", " ", t, flags=re.S)
    t = re.sub(r"</(p|li|h[1-6]|tr|div|section|details|summary|pre|ul|ol|table)>|<br\s*/?>", "\n", t)
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    lines = [re.sub(r"[ \t ]+", " ", ln).strip() for ln in t.split("\n")]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(l for l in lines if l or True)).strip()


def build():
    parts = [HEAD]
    for p in pages():
        f = file_for(p)
        if not f: continue
        h = open(f, encoding="utf-8").read()
        title = html.unescape(re.search(r"<title>(.*?)</title>", h, re.S).group(1)).strip()
        parts.append("\n## %s\nSource: %s%s\n\n%s\n" % (title, SITE, p, text(h)))
    return "".join(parts)


if __name__ == "__main__":
    out, new = os.path.join(PUB, "llms-full.txt"), build()
    if "--check" in sys.argv:
        sys.exit(0 if os.path.exists(out) and open(out, encoding="utf-8").read() == new else 1)
    open(out, "w", encoding="utf-8").write(new); print("wrote llms-full.txt, %d bytes" % len(new.encode()))
