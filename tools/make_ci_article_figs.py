#!/usr/bin/env python3
"""Figures for /blog/ai-crawler-check-in-ci (RES-3772), built only from saved data in data/ci-article-2026-10-23/.

  python3 tools/make_ci_article_figs.py            writes the SVGs and the WebP into public/blog/img/

Canvas is 800 px wide on purpose: the article column is 720 px, so type stays legible there, and at 390 px (scale 0.44) 22 px type is about 10 px.
Inputs (all real, 23 Oct 2026):
  ai-access-index-run1.json     numbers parsed from https://citedby.eu/data/ai-access-index-2026-10 (live page, fetched 2026-10-23T21:11Z)
  action-run-annotations.png    crop of the public Actions run page of github.com/resaleiq/citedby-check (annotations card only; the page header that names the pusher is not in the crop)
Brand tokens from public/style.css: navy #0F1B2D, accent #1F4FD8, wash #EEF2F7, muted #556070, rule #C9D0DA."""
import html, json, os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DATA = os.path.join(ROOT, "data", "ci-article-2026-10-23")
IMG = os.path.join(ROOT, "public", "blog", "img")
SLUG = "ai-crawler-check-in-ci"
E = html.escape
NAVY, ACCENT, WASH, MUTED, RULE = "#0F1B2D", "#1F4FD8", "#EEF2F7", "#556070", "#C9D0DA"
SANS = "system-ui,Arial,sans-serif"
SERIF = "Georgia,'Times New Roman',serif"


def head(w, h, title, desc):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" role="img" aria-labelledby="t d">'
            '<title id="t">%s</title><desc id="d">%s</desc>' % (w, h, w, h, E(title), E(desc)))


def write(name, svg):
    path = os.path.join(IMG, name)
    open(path, "w", encoding="utf-8").write(svg)
    print("wrote", os.path.relpath(path, ROOT), len(svg), "bytes")


def wrap(text, n):
    out, cur = [], ""
    for w in text.split():
        if cur and len(cur) + 1 + len(w) > n: out.append(cur); cur = w
        else: cur = (cur + " " + w).strip()
    return out + ([cur] if cur else [])


def chart():
    d = json.load(open(os.path.join(DATA, "ai-access-index-run1.json"), encoding="utf-8"))
    n = d["sample"]["read"]
    rows = [("GPTBot", True), ("Google-Extended", True), ("PerplexityBot", True), ("OAI-SearchBot", True), ("Bingbot", True), ("Googlebot", False)]
    rows = sorted(rows, key=lambda r: -d["crawlers"][r[0]]["blocks_pct"])
    W, H = 800, 610
    title = "Share of %s popular EU sites whose robots.txt blocks each crawler" % format(n, ",")
    desc = ("Bar chart, robots.txt read on 23 October 2026. " + "; ".join("%s %.1f%% (%s sites)" % (r[0], d["crawlers"][r[0]]["blocks_pct"], format(d["crawlers"][r[0]]["blocks_sites"], ",")) for r in rows)
            + ". Blue bars are the five crawlers the check looks at; Googlebot is a control.")
    o = [head(W, H, title, desc), '<rect width="%d" height="%d" fill="#fff"/>' % (W, H)]
    o.append('<text x="32" y="46" font-family="%s" font-size="28" font-weight="600" fill="%s">Share of %s popular EU sites</text>' % (SERIF, NAVY, format(n, ",")))
    o.append('<text x="32" y="80" font-family="%s" font-size="28" font-weight="600" fill="%s">whose robots.txt blocks each crawler</text>' % (SERIF, NAVY))
    o.append('<text x="32" y="112" font-family="%s" font-size="19" fill="%s">Read on 23 Oct 2026. Blocked: may not fetch the home page.</text>' % (SANS, MUTED))
    x0, scale, y0, step = 236, 24.0, 150, 62  # 24 px per percentage point: 20% = 480 px
    for pct in (0, 5, 10, 15, 20):
        x = x0 + pct * scale
        o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="1"/>' % (x, y0 - 12, x, y0 + step * len(rows) - 14, RULE))
        o.append('<text x="%.1f" y="%d" font-family="%s" font-size="17" fill="%s" text-anchor="middle">%d%%</text>' % (x, y0 + step * len(rows) + 8, SANS, MUTED, pct))
    for i, (name, in_check) in enumerate(rows):
        c = d["crawlers"][name]
        y = y0 + i * step
        o.append('<text x="%d" y="%d" font-family="%s" font-size="22" font-weight="600" fill="%s" text-anchor="end">%s</text>' % (x0 - 14, y + 28, SANS, NAVY, E(name)))
        w = c["blocks_pct"] * scale
        o.append('<rect x="%d" y="%d" width="%.1f" height="38" fill="%s"/>' % (x0, y + 2, w, ACCENT if in_check else MUTED))
        o.append('<text x="%.1f" y="%d" font-family="%s" font-size="24" font-weight="600" fill="%s">%.1f%%</text>' % (x0 + w + 10, y + 30, SANS, NAVY, c["blocks_pct"]))
    o.append('<rect x="32" y="%d" width="16" height="16" fill="%s"/><text x="56" y="%d" font-family="%s" font-size="18" fill="%s">The five crawlers the check looks at</text>' % (H - 50, ACCENT, H - 36, SANS, MUTED))
    o.append('<rect x="440" y="%d" width="16" height="16" fill="%s"/><text x="464" y="%d" font-family="%s" font-size="18" fill="%s">Googlebot, a control</text>' % (H - 50, MUTED, H - 36, SANS, MUTED))
    write(SLUG + "-chart.svg", "".join(o) + "</svg>")


def flow():
    W, H = 800, 600
    title = "How the check runs: your pipeline, citedby.eu, the results, the exit code"
    desc = ("Four steps from top to bottom. 1 Your pipeline runs citedby-check or the Action after a deploy, against the live address. "
            "2 citedby.eu loads robots.txt, the home page and llms.txt over plain HTTP without JavaScript, plus one product page if it finds one. "
            "3 A result comes back for each check: crawlers in robots.txt, text in the HTML, Organization data, Product data, llms.txt. "
            "4 The command exits 0, 1 or 3, and the Action adds a job summary and annotations.")
    steps = [("Your pipeline", "runs citedby-check or the Action after a deploy, against the live address"),
             ("citedby.eu", "loads robots.txt, the home page and llms.txt over plain HTTP, no JavaScript, plus one product page if it finds one"),
             ("Results", "one per check: crawlers in robots.txt, text in the HTML, Organization data, Product data, llms.txt"),
             ("Exit code", "0 clean, 1 something to fix, 3 not measured. The Action adds a job summary and annotations")]
    o = [head(W, H, title, desc), '<rect width="%d" height="%d" fill="#fff"/>' % (W, H)]
    o.append('<text x="32" y="46" font-family="%s" font-size="28" font-weight="600" fill="%s">The check runs from outside your pipeline</text>' % (SERIF, NAVY))
    bx, bw, bh, y, gap = 32, 736, 98, 76, 24
    for i, (h, b) in enumerate(steps):
        yy = y + i * (bh + gap)
        o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="%s" stroke="%s" stroke-width="3"/>' % (bx, yy, bw, bh, WASH if i % 2 == 0 else "#fff", NAVY))
        o.append('<text x="%d" y="%d" font-family="%s" font-size="44" font-weight="600" fill="%s">%d</text>' % (bx + 22, yy + 62, SANS, ACCENT, i + 1))
        o.append('<text x="%d" y="%d" font-family="%s" font-size="25" font-weight="600" fill="%s">%s</text>' % (bx + 78, yy + 36, SANS, NAVY, E(h)))
        for k, ln in enumerate(wrap(b, 62)[:2]):
            o.append('<text x="%d" y="%d" font-family="%s" font-size="19" fill="%s">%s</text>' % (bx + 78, yy + 62 + 24 * k, SANS, MUTED, E(ln)))
        if i < len(steps) - 1:
            ax = bx + bw // 2
            o.append('<path d="M%d %d V%d" stroke="%s" stroke-width="3"/><path d="M%d %d l-8 -9 h16 z" fill="%s"/>' % (ax, yy + bh + 2, yy + bh + gap - 8, ACCENT, ax, yy + bh + gap - 1, ACCENT))
    o.append('<text x="32" y="%d" font-family="%s" font-size="17" fill="%s">Runs from outside: localhost, private networks and pages behind a login cannot be checked.</text>' % (H - 22, SANS, MUTED))
    write(SLUG + "-flow.svg", "".join(o) + "</svg>")


def action_shot():
    src = os.path.join(DATA, "action-run-annotations.png")
    from PIL import Image
    im = Image.open(src).convert("RGB")
    w, h = im.size
    im = im.crop((0, 0, w, 832))  # the card header and the first four annotations; the fifth item is a GitHub notice about runner images
    im = im.resize((800, round(im.size[1] * 800 / w)), Image.LANCZOS)
    out = os.path.join(IMG, SLUG + "-action.webp")
    im.save(out, "WEBP", quality=84, method=6)
    print("wrote", os.path.relpath(out, ROOT), os.path.getsize(out), "bytes", im.size)


if __name__ == "__main__":
    chart(); flow(); action_shot()
