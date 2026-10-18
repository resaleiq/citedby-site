#!/usr/bin/env python3
"""Render content/blog/*.md into public/blog (EN) and public/<lang>/blog, plus each blog index, and refresh the blog URLs in public/sitemap.xml (RES-1478).

usage: python3 tools/build_blog.py [--check]     (--check only validates, writes nothing)

Article file = front matter, a blank line, then a small markdown subset:
  title, h1, description, slug, locale (en|fr|nl|de|es), date, reviewed (YYYY-MM-DD), answer (40-60 words, quoted by assistants),
  hero (file in public/blog/img), og (PNG in public/blog/img, optional), related ("/path|Title; /path|Title"), translations ("fr=/fr/blog/x; nl=/nl/blog/y"),
  widget ("on" puts the free-check box after the answer; "off" omits it), howto ("on" adds HowTo schema from the first numbered list), ads ("off" never shows the slot).
  Body: ## / ### headings, paragraphs, - lists, 1. lists, | tables, ![alt](/blog/img/x.svg "caption") figures, ## FAQ (### question + answer), ## Sources (list).
Ads: ADS_ENABLED stays False until the CEO switches a cluster on (needs real traffic and an EU consent banner); never on /check, price or checkout pages."""
import datetime, glob, hashlib, html, json, os, re, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PUB, SRC = os.path.join(ROOT, "public"), os.path.join(ROOT, "content", "blog")
SITE, E = "https://citedby.eu", html.escape
ADS_ENABLED = False
UI = {
 "en": dict(blog="Guides", idx_h1="AI visibility guides for online shops", idx_lede="How AI assistants find, read and name online shops, and what to fix. Each guide ends with a free check you can run on your own site.", answer="Short answer", by="By the CitedBy editorial team", rev="Reviewed on", sources="Sources", related="Keep reading", faq="Questions people ask", w_h="Check your own site (free, about 10 seconds)", w_ph="yourshop.com", w_go="Run the free check", w_note="No email needed. We fetch your page the way AI crawlers do.", cta_h="See what AI answers about your shop", cta_b="The free check shows which AI crawlers your site lets in. The audit shows who gets named when buyers ask.", cta="Run the free check", home="Home", chk="/check", read="Read", skip="Skip to content", ad="Advertisement", langs="Languages", legal="Legal notice", privacy="Privacy"),
 "fr": dict(blog="Guides", idx_h1="Guides de visibilité IA pour les boutiques en ligne", idx_lede="Comment les assistants IA trouvent, lisent et citent les boutiques en ligne, et quoi corriger. Chaque guide se termine par un test gratuit pour votre site.", answer="Réponse courte", by="Par la rédaction de CitedBy", rev="Vérifié le", sources="Sources", related="À lire aussi", faq="Questions fréquentes", w_h="Testez votre site (gratuit, environ 10 secondes)", w_ph="votreboutique.fr", w_go="Lancer le test gratuit", w_note="Sans e-mail. Nous lisons votre page comme le font les robots des IA.", cta_h="Voyez ce que les IA répondent sur votre boutique", cta_b="Le test gratuit montre quels robots IA votre site laisse entrer. L'audit montre qui est cité quand vos clients posent la question.", cta="Lancer le test gratuit", home="Accueil", chk="/fr/check", read="Lire", skip="Aller au contenu", ad="Publicité", langs="Langues", legal="Mentions légales", privacy="Confidentialité"),
 "nl": dict(blog="Gidsen", idx_h1="AI-zichtbaarheidsgidsen voor webshops", idx_lede="Hoe AI-assistenten webshops vinden, lezen en noemen, en wat u moet aanpassen. Elke gids eindigt met een gratis check voor uw eigen site.", answer="Kort antwoord", by="Door de redactie van CitedBy", rev="Nagekeken op", sources="Bronnen", related="Lees ook", faq="Veelgestelde vragen", w_h="Check uw eigen site (gratis, ongeveer 10 seconden)", w_ph="uwwebshop.nl", w_go="Start de gratis check", w_note="Geen e-mail nodig. We lezen uw pagina zoals AI-crawlers dat doen.", cta_h="Zie wat AI antwoordt over uw webshop", cta_b="De gratis check toont welke AI-crawlers uw site binnenlaat. De audit toont wie genoemd wordt als kopers het vragen.", cta="Start de gratis check", home="Home", chk="/nl/check", read="Lees", skip="Naar de inhoud", ad="Advertentie", langs="Talen", legal="Juridische informatie", privacy="Privacy"),
 "de": dict(blog="Ratgeber", idx_h1="Ratgeber zur KI-Sichtbarkeit für Online-Shops", idx_lede="Wie KI-Assistenten Online-Shops finden, lesen und nennen, und was Sie korrigieren sollten. Jeder Ratgeber endet mit einem kostenlosen Check für Ihre Seite.", answer="Kurz gesagt", by="Von der CitedBy-Redaktion", rev="Geprüft am", sources="Quellen", related="Weiterlesen", faq="Häufige Fragen", w_h="Prüfen Sie Ihre Seite (kostenlos, etwa 10 Sekunden)", w_ph="ihr-shop.de", w_go="Kostenlosen Check starten", w_note="Keine E-Mail nötig. Wir rufen Ihre Seite so ab, wie es KI-Crawler tun.", cta_h="Sehen Sie, was KI über Ihren Shop antwortet", cta_b="Der kostenlose Check zeigt, welche KI-Crawler Ihre Seite hereinlässt. Das Audit zeigt, wer genannt wird, wenn Käufer fragen.", cta="Kostenlosen Check starten", home="Start", chk="/check", read="Lesen", skip="Zum Inhalt", ad="Anzeige", langs="Sprachen", legal="Impressum", privacy="Datenschutz"),
 "es": dict(blog="Guías", idx_h1="Guías de visibilidad en IA para tiendas online", idx_lede="Cómo los asistentes de IA encuentran, leen y nombran las tiendas online, y qué corregir. Cada guía termina con una prueba gratuita para tu web.", answer="Respuesta corta", by="Por la redacción de CitedBy", rev="Revisado el", sources="Fuentes", related="Sigue leyendo", faq="Preguntas frecuentes", w_h="Prueba tu web (gratis, unos 10 segundos)", w_ph="tutienda.es", w_go="Hacer la prueba gratuita", w_note="Sin correo. Leemos tu página como lo hacen los rastreadores de IA.", cta_h="Mira qué responde la IA sobre tu tienda", cta_b="La prueba gratuita muestra qué rastreadores de IA deja entrar tu web. La auditoría muestra quién sale nombrado cuando los compradores preguntan.", cta="Hacer la prueba gratuita", home="Inicio", chk="/check", read="Leer", skip="Ir al contenido", ad="Publicidad", langs="Idiomas", legal="Aviso legal", privacy="Privacidad"),
}
def ver(name):
    p = os.path.join(PUB, name); return hashlib.sha256(open(p, "rb").read()).hexdigest()[:8] if os.path.exists(p) else "0"
def prefix(loc): return "" if loc == "en" else "/" + loc
def inline(s):
    s = E(s, quote=False)
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda m: '<a href="%s"%s>%s</a>' % (m.group(2), ' rel="noopener"' if m.group(2).startswith("http") else "", m.group(1)), s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
def plain(s): return re.sub(r"<[^>]+>", "", inline(s))
def slugify(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:48]

def parse(path):
    raw = open(path, encoding="utf-8").read()
    head, _, body = raw.partition("\n\n")
    fm = {}
    for line in head.splitlines():
        k, _, v = line.partition(":"); fm[k.strip()] = v.strip()
    for k in ("title", "description", "slug", "date", "reviewed", "answer"):
        if not fm.get(k): sys.exit("%s: missing front matter %r" % (path, k))
    fm.setdefault("locale", "en"); fm.setdefault("h1", fm["title"])
    n = len(fm["answer"].split())
    if not 40 <= n <= 60: sys.exit("%s: answer is %d words, must be 40-60" % (path, n))
    return fm, body

def render_body(body, fm, loc, state):
    out, faq, steps, srcs, i, lines = [], [], [], [], 0, body.splitlines()
    sect = None
    def flush_para(buf):
        if buf: out.append("<p>%s</p>" % inline(" ".join(buf)))
    buf = []
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            flush_para(buf); buf = []; i += 1; continue
        m = re.match(r"(#{2,3}) (.+)", ln)
        if m:
            flush_para(buf); buf = []
            lvl, txt = len(m.group(1)), m.group(2).strip()
            if lvl == 2:
                sect = "faq" if txt.lower() == "faq" else "sources" if txt.lower() == "sources" else None
                if sect == "faq": out.append('<h2 id="faq">%s</h2>' % E(UI[loc]["faq"]))
                elif sect == "sources": out.append('<h2 id="sources">%s</h2>' % E(UI[loc]["sources"]))
                else: out.append('<h2 id="%s">%s</h2>' % (slugify(txt), inline(txt)))
            else:
                if sect == "faq":
                    faq.append([txt, []]); out.append('<h3>%s</h3>' % inline(txt))
                else: out.append('<h3 id="%s">%s</h3>' % (slugify(txt), inline(txt)))
            i += 1; continue
        if re.match(r"(- |\d+\. )", ln):
            flush_para(buf); buf = []
            ordered = bool(re.match(r"\d+\. ", ln)); items = []
            while i < len(lines) and re.match(r"(- |\d+\. )", lines[i]):
                items.append(re.sub(r"^(- |\d+\. )", "", lines[i])); i += 1
            if ordered and not steps: steps = items
            if sect == "sources": srcs.extend(items)
            out.append("<%s%s>%s</%s>" % ("ol" if ordered else "ul", ' class="steps"' if ordered else "", "".join("<li>%s</li>" % inline(x) for x in items), "ol" if ordered else "ul"))
            continue
        if ln.startswith("|"):
            flush_para(buf); buf = []; rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i += 1
            rows = [r for r in rows if not all(re.fullmatch(r":?-{2,}:?", c) for c in r)]
            th = "".join("<th scope=\"col\">%s</th>" % inline(c) for c in rows[0])
            tb = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % inline(c) for c in r) for r in rows[1:])
            out.append('<div class="tw"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (th, tb)); continue
        m = re.match(r'!\[([^\]]*)\]\(([^)\s]+)(?: "([^"]*)")?\)(?:\{(\d+)x(\d+)\})?$', ln.strip())
        if m:
            flush_para(buf); buf = []
            alt, src, cap, iw, ih = m.groups(); iw, ih = iw or 1200, ih or 630
            if not alt: sys.exit("%s: image %s has no alt text" % (fm["slug"], src))
            state["imgs"] += 1
            out.append('<figure><img src="%s" alt="%s" width="%s" height="%s" loading="%s" decoding="async">%s</figure>' % (E(src), E(alt), iw, ih, "lazy" if state["imgs"] > 1 else "eager", "<figcaption>%s</figcaption>" % inline(cap) if cap else ""))
            i += 1; continue
        if sect == "faq" and faq:
            faq[-1][1].append(ln.strip()); buf.append(ln.strip()); i += 1; continue
        buf.append(ln.strip()); i += 1
    flush_para(buf)
    return "\n".join(out), faq, steps, srcs

def widget(loc, slug):
    t = UI[loc]
    return ('<form class="bw" action="%s" method="get" aria-labelledby="bw-h"><h2 id="bw-h">%s</h2>'
            '<input type="hidden" name="utm_source" value="blog"><input type="hidden" name="utm_medium" value="article"><input type="hidden" name="utm_campaign" value="%s">'
            '<div class="bwr"><label class="sr" for="bw-u">URL</label><input id="bw-u" name="url" type="text" inputmode="url" autocomplete="url" autocapitalize="off" spellcheck="false" placeholder="%s" required>'
            '<button class="btn p" type="submit">%s</button></div><p class="gloss">%s</p></form>') % (t["chk"], E(t["w_h"]), E(slug), E(t["w_ph"]), E(t["w_go"]), E(t["w_note"]))

def shell(loc, title, desc, canon, alts, og, jsonld, main, extra_head=""):
    t = UI[loc]
    ld = "".join('<script type="application/ld+json">%s</script>' % json.dumps(j, ensure_ascii=False).replace("</", "<\\/") for j in jsonld)
    alt = "".join('<link rel="alternate" hreflang="%s" href="%s%s">' % (l, SITE, p) for l, p in alts)
    return f'''<!doctype html>
<html lang="{loc}"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{SITE}{canon}">{alt}
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{SITE}{canon}"><meta property="og:type" content="article"><meta property="og:image" content="{SITE}{og}"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0F1B2D">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/fonts/newsreader-latin-600-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/style.css?v={ver("style.css")}"><link rel="stylesheet" href="/blog.css?v={ver("blog.css")}">{ld}{extra_head}
</head><body>
<a class="skip" href="#main">{E(t["skip"])}</a>
<header class="top"><a class="logo" href="/" aria-label="CitedBy">CitedBy<i aria-hidden="true">1</i></a><div class="hnav"><nav aria-label="Main"><a href="{prefix(loc) or "/"}">{E(t["home"])}</a><a href="{prefix(loc)}/blog">{E(t["blog"])}</a><a href="{t["chk"]}">Check</a></nav></div></header>
{main}
<footer><span>© 2026 CitedBy. hello@citedby.eu</span><span><a href="/terms">Terms</a> &nbsp; <a href="/refund">Refunds</a> &nbsp; <a href="/about">About</a> &nbsp; <a href="/legal">{E(t["legal"])}</a> &nbsp; <a href="/privacy">{E(t["privacy"])}</a></span></footer>
</body></html>
'''

def build_article(fm, body, arts):
    loc, slug = fm["locale"], fm["slug"]
    t, state = UI[loc], {"imgs": 0}
    path = "%s/blog/%s" % (prefix(loc), slug)
    html_body, faq, steps, srcs = render_body(body, fm, loc, state)
    if state["imgs"] < 1 and fm.get("hero") is None: sys.exit("%s: needs images" % slug)
    hero = fm.get("hero", "")
    og = "/blog/img/%s" % fm["og"] if fm.get("og") else "/og.png"
    ans = '<aside class="answer" aria-label="%s"><b>%s</b><p>%s</p></aside>' % (E(t["answer"]), E(t["answer"]), E(fm["answer"]))
    w = widget(loc, slug) if fm.get("widget", "on") != "off" else ""
    ad = '<aside class="ad-slot" aria-label="%s" data-slot="in-article"></aside>' % E(t["ad"]) if ADS_ENABLED and fm.get("ads") != "off" else "<!-- ad-slot:in-article (off) -->"
    rel = [r.split("|", 1) for r in fm.get("related", "").split(";") if "|" in r]
    rel_h = ('<nav class="rel" aria-label="%s"><h2>%s</h2><ul>%s</ul></nav>' % (E(t["related"]), E(t["related"]), "".join('<li><a href="%s">%s</a></li>' % (E(u.strip()), E(x.strip())) for u, x in rel))) if rel else ""
    cta = '<section class="cta2"><h2>%s</h2><p>%s</p><a class="btn p" href="%s?utm_source=blog&amp;utm_medium=article&amp;utm_campaign=%s&amp;utm_content=cta">%s</a></section>' % (E(t["cta_h"]), E(t["cta_b"]), t["chk"], E(slug), E(t["cta"]))
    hero_h = '<figure class="hero"><img src="/blog/img/%s" alt="%s" width="1200" height="630" fetchpriority="high" decoding="async"></figure>' % (E(hero), E(fm.get("hero_alt", fm["h1"]))) if hero else ""
    if hero and not fm.get("hero_alt"): sys.exit("%s: hero needs hero_alt" % slug)
    alts = [(l, p) for l, p in (kv.split("=", 1) for kv in fm.get("translations", "").split(";") if "=" in kv)]
    if alts: alts = [(loc, path)] + [(l.strip(), p.strip()) for l, p in alts]; alts.append(("x-default", next((p for l, p in alts if l == "en"), path)))
    org = {"@type": "Organization", "name": "CitedBy", "url": SITE + "/"}
    art = {"@context": "https://schema.org", "@type": "Article", "headline": fm["h1"], "description": fm["description"], "inLanguage": loc, "datePublished": fm["date"], "dateModified": fm["reviewed"],
           "author": {"@type": "Organization", "name": "CitedBy editorial team", "url": SITE + "/about"}, "publisher": org, "mainEntityOfPage": SITE + path,
           "image": [SITE + og] + ([SITE + "/blog/img/" + hero] if hero else [])}
    ld = [art, {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": t["home"], "item": SITE + (prefix(loc) or "/")},
        {"@type": "ListItem", "position": 2, "name": t["blog"], "item": SITE + prefix(loc) + "/blog"},
        {"@type": "ListItem", "position": 3, "name": fm["h1"], "item": SITE + path}]}]
    if faq: ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plain(" ".join(a))}} for q, a in faq]})
    if fm.get("howto") == "on" and steps: ld.append({"@context": "https://schema.org", "@type": "HowTo", "name": fm["h1"], "step": [{"@type": "HowToStep", "position": n + 1, "text": plain(s)} for n, s in enumerate(steps)]})
    # ad slot sits after the first third of the body, never beside the widget or CTA
    parts = html_body.split("\n"); cut = max(1, len(parts) // 3)
    body_h = "\n".join(parts[:cut] + [ad] + parts[cut:])
    main = f'''<main id="main" class="art"><article>
<p class="dateline"><a href="{prefix(loc)}/blog">{E(t["blog"])}</a> / {E(fm.get("cluster", ""))}</p>
<h1>{E(fm["h1"])}</h1>
<p class="byline">{E(t["by"])} · {E(t["rev"])} <time datetime="{fm["reviewed"]}">{fm["reviewed"]}</time></p>
{ans}
{hero_h}
{w}
{body_h}
{cta}
{rel_h}
</article></main>'''
    return path, shell(loc, fm["title"], fm["description"], path, alts, og, ld, main)

def build_index(loc, arts):
    t = UI[loc]; path = prefix(loc) + "/blog"
    cards = "".join('<li><a href="%s/blog/%s"><b>%s</b><span>%s</span><time datetime="%s">%s %s</time></a></li>' % (prefix(loc), a["slug"], E(a["h1"]), E(a["description"]), a["reviewed"], E(t["rev"]), a["reviewed"]) for a in sorted(arts, key=lambda a: a["reviewed"], reverse=True))
    ld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": t["idx_h1"], "inLanguage": loc, "url": SITE + path},
          {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": n + 1, "url": "%s%s/blog/%s" % (SITE, prefix(loc), a["slug"])} for n, a in enumerate(arts)]}]
    main = '<main id="main" class="art idx"><h1>%s</h1><p class="lede">%s</p><ul class="cards">%s</ul></main>' % (E(t["idx_h1"]), E(t["idx_lede"]), cards)
    return path, shell(loc, t["idx_h1"] + ". CitedBy", t["idx_lede"], path, [], "/og.png", ld, main)

def main():
    check = "--check" in sys.argv
    arts = {}
    for p in sorted(glob.glob(os.path.join(SRC, "*.md"))):
        fm, body = parse(p); arts.setdefault(fm["locale"], []).append((fm, body))
    urls, written = [], []
    for loc, items in arts.items():
        for fm, body in items:
            path, doc = build_article(fm, body, items); urls.append((path, fm["reviewed"])); written.append((path, doc))
        path, doc = build_index(loc, [f for f, _ in items]); urls.append((path, max(f["reviewed"] for f, _ in items))); written.append((path, doc))
    if check: print("ok: %d pages" % len(written)); return
    for path, doc in written:
        out = os.path.join(PUB, path.lstrip("/"))
        if path.endswith("/blog"): out = os.path.join(out, "index.html")
        else: out += ".html"
        os.makedirs(os.path.dirname(out), exist_ok=True); open(out, "w", encoding="utf-8").write(doc)
    sm = os.path.join(PUB, "sitemap.xml"); s = open(sm, encoding="utf-8").read()
    s = re.sub(r"<url><loc>%s(/[a-z]{2})?/blog[^<]*</loc>(<lastmod>[^<]*</lastmod>)?</url>" % re.escape(SITE), "", s)
    s = s.replace("</urlset>", "".join("<url><loc>%s%s</loc><lastmod>%s</lastmod></url>" % (SITE, p, d) for p, d in urls) + "</urlset>")
    open(sm, "w", encoding="utf-8").write(s)
    print("wrote %d pages" % len(written))
main()
