#!/usr/bin/env python3
"""Render content/blog/*.md into public/blog (EN) and public/<lang>/blog, plus each blog index, and refresh the blog URLs in public/sitemap.xml (RES-1478).

usage: python3 tools/build_blog.py [--check]     (--check only validates, writes nothing)

Article file = front matter, a blank line, then a small markdown subset:
  section ("compare" publishes at /compare/<slug> instead of /blog/<slug>, kept out of the blog index), title, h1, description, slug, locale (en|fr|nl|de|es), date, reviewed (YYYY-MM-DD), answer (40-60 words, quoted by assistants),
  hero (file in public/blog/img), og (PNG in public/blog/img, optional), related ("/path|Title; /path|Title"), translations ("fr=/fr/blog/x; nl=/nl/blog/y"),
  widget ("on" puts the free-check box after the answer; "off" omits it), howto ("on" adds HowTo schema from the first numbered list), ads ("off" never shows the slot).
  Body: ## / ### headings, paragraphs, - lists, 1. lists, | tables, ![alt](/blog/img/x.svg "caption") figures, ## FAQ (### question + answer), ## Sources (list).
Ads: ADS_ENABLED stays False until the CEO switches a cluster on (needs real traffic and an EU consent banner); never on /check, price or checkout pages."""
import datetime, glob, hashlib, html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import docshell
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PUB, SRC = os.path.join(ROOT, "public"), os.path.join(ROOT, "content", "blog")
SITE, E = "https://citedby.eu", html.escape
ADS_ENABLED = False
UI = {
 "en": dict(by_person='By', toc='On this page', price='Audit from €9, paid once. 14-day money-back guarantee.', blog="Guides", idx_h1="AI visibility guides for online shops", idx_lede="How AI assistants find, read and name online shops, and what to fix. Each guide ends with an audit you can run on your own site, from €9.", answer="Short answer", by="By the CitedBy editorial team", rev="Reviewed on", sources="Sources", related="Keep reading", faq="Questions people ask", f_h='Check your own site free: 10 pages, no account', f_go='Check my site free', f_note='Result in seconds. No account, no card.', src_n='{n} sources · method', w_h="Audit your own site (from €9, 14-day money-back guarantee)", w_ph="yourshop.com", w_go="Audit my site", w_note="We crawl your site up to your plan's page limit and give you the exact fix for each issue. Paid before the crawl.", cta_h="See what AI answers about your shop", cta_b="The audit crawls your site up to your plan's page limit, shows which AI crawlers it lets in and gives the exact fix for each issue. From €9, 14-day money-back guarantee.", cta="Audit my site", home="Home", chk="/", read="Read", skip="Skip to content", ad="Advertisement", langs="Languages", legal="Legal notice", privacy="Privacy"),
 "fr": dict(by_person='Par', toc='Dans cet article', price='Audit dès 9 €, payé une fois. Garantie 14 jours.', blog="Guides", idx_h1="Guides de visibilité IA pour les boutiques en ligne", idx_lede="Comment les assistants IA trouvent, lisent et citent les boutiques en ligne, et quoi corriger. Chaque guide se termine par un audit de votre site, dès 9 €.", answer="Réponse courte", by="Par la rédaction de CitedBy", rev="Vérifié le", sources="Sources", related="À lire aussi", faq="Questions fréquentes", f_h='Vérifiez votre site gratuitement : 10 pages, sans compte', f_go='Vérifier mon site gratuitement', f_note='Résultat en quelques secondes. Sans compte, sans carte.', src_n='{n} sources · méthode', w_h="Auditez votre site (dès 9 €, garantie 14 jours)", w_ph="votreboutique.fr", w_go="Auditer mon site", w_note="Nous explorons votre site jusqu'à la limite de votre offre et donnons le correctif exact. Payé avant l'exploration.", cta_h="Voyez ce que les IA répondent sur votre boutique", cta_b="L'audit explore votre site jusqu'à la limite de votre offre, montre quels robots IA il laisse entrer et donne le correctif exact. Dès 9 €, garantie 14 jours.", cta="Auditer mon site", home="Accueil", chk="/fr", read="Lire", skip="Aller au contenu", ad="Publicité", langs="Langues", legal="Mentions légales", privacy="Confidentialité"),
 "nl": dict(by_person='Door', toc='In dit artikel', price='Audit vanaf €9, eenmalig betaald. 14 dagen geld-terug-garantie.', blog="Gidsen", idx_h1="AI-zichtbaarheidsgidsen voor webshops", idx_lede="Hoe AI-assistenten webshops vinden, lezen en noemen, en wat je moet aanpassen. Elke gids eindigt met een audit van je eigen site, vanaf €9.", answer="Kort antwoord", by="Door de redactie van CitedBy", rev="Nagekeken op", sources="Bronnen", related="Lees ook", faq="Veelgestelde vragen", f_h="Check je eigen site gratis: 10 pagina's, zonder account", f_go='Check mijn site gratis', f_note='Resultaat in enkele seconden. Geen account, geen kaart.', src_n='{n} bronnen · methode', w_h="Audit je eigen site (vanaf €9, 14 dagen geld-terug-garantie)", w_ph="jouwwebshop.nl", w_go="Audit mijn site", w_note="We crawlen je site tot de paginalimiet van je abonnement en geven de exacte oplossing per probleem. Betaald vóór de crawl.", cta_h="Zie wat AI antwoordt over je webshop", cta_b="De audit crawlt je site tot de paginalimiet van je abonnement, toont welke AI-crawlers binnenkomen en geeft de exacte oplossing. Vanaf €9, 14 dagen geld-terug-garantie.", cta="Audit mijn site", home="Home", chk="/nl", read="Lees", skip="Naar de inhoud", ad="Advertentie", langs="Talen", legal="Juridische informatie", privacy="Privacy"),
 "de": dict(by_person='Von', toc='In diesem Artikel', price='Audit ab 9 €, einmal bezahlt. 14 Tage Geld-zurück-Garantie.', blog="Ratgeber", idx_h1="Ratgeber zur KI-Sichtbarkeit für Online-Shops", idx_lede="Wie KI-Assistenten Online-Shops finden, lesen und nennen, und was Sie korrigieren sollten. Jeder Ratgeber endet mit einem Audit Ihrer Seite ab 9 €.", answer="Kurz gesagt", by="Von der CitedBy-Redaktion", rev="Geprüft am", sources="Quellen", related="Weiterlesen", faq="Häufige Fragen", f_h='Prüfen Sie Ihre Seite kostenlos: 10 Seiten, ohne Konto', f_go='Meine Seite kostenlos prüfen', f_note='Ergebnis in Sekunden. Kein Konto, keine Karte.', src_n='{n} Quellen · Methode', w_h="Prüfen Sie Ihre Seite (ab 9 €, 14 Tage Geld-zurück-Garantie)", w_ph="ihr-shop.de", w_go="Meine Seite prüfen", w_note="Wir crawlen Ihre Website bis zum Seitenlimit Ihres Tarifs und liefern die genaue Korrektur. Vor dem Crawl bezahlt.", cta_h="Sehen Sie, was KI über Ihren Shop antwortet", cta_b="Das Audit crawlt Ihre Website bis zum Seitenlimit Ihres Tarifs, zeigt, welche KI-Crawler hereinkommen, und liefert die genaue Korrektur. Ab 9 €, 14 Tage Geld-zurück-Garantie.", cta="Meine Seite prüfen", home="Start", chk="/de", read="Lesen", skip="Zum Inhalt", ad="Anzeige", langs="Sprachen", legal="Impressum", privacy="Datenschutz"),
 "es": dict(by_person='Por', toc='En este artículo', price='Auditoría desde 9 €, pago único. Garantía de 14 días.', blog="Guías", idx_h1="Guías de visibilidad en IA para tiendas online", idx_lede="Cómo los asistentes de IA encuentran, leen y nombran las tiendas online, y qué corregir. Cada guía termina con una auditoría de tu web desde 9 €.", answer="Respuesta corta", by="Por la redacción de CitedBy", rev="Revisado el", sources="Fuentes", related="Sigue leyendo", faq="Preguntas frecuentes", f_h='Revisa tu web gratis: 10 páginas, sin cuenta', f_go='Revisar mi web gratis', f_note='Resultado en segundos. Sin cuenta, sin tarjeta.', src_n='{n} fuentes · método', w_h="Audita tu web (desde 9 €, garantía de 14 días)", w_ph="tutienda.es", w_go="Auditar mi web", w_note="Rastreamos tu web hasta el límite de páginas de tu plan y te damos la corrección exacta. Se paga antes del rastreo.", cta_h="Mira qué responde la IA sobre tu tienda", cta_b="La auditoría rastrea tu web hasta el límite de páginas de tu plan, muestra qué rastreadores de IA entran y da la corrección exacta. Desde 9 €, garantía de 14 días.", cta="Auditar mi web", home="Inicio", chk="/es", read="Leer", skip="Ir al contenido", ad="Publicidad", langs="Idiomas", legal="Aviso legal", privacy="Privacidad"),
}
def ver(name):
    p = os.path.join(PUB, name); return hashlib.sha256(open(p, "rb").read()).hexdigest()[:8] if os.path.exists(p) else "0"
def prefix(loc): return "" if loc == "en" else "/" + loc
def inline(s):
    s = E(s, quote=False)
    codes = []
    def keep(m): codes.append("<code>%s</code>" % m.group(1)); return "\x00%d\x00" % (len(codes) - 1)
    s = re.sub(r"`([^`]+)`", keep, s)  # RES-2616: code spans stay literal, never become live links
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda m: '<a href="%s"%s>%s</a>' % (m.group(2), ' rel="noopener"' if m.group(2).startswith("http") else "", m.group(1)), s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    return re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], s)
def plain(s): return re.sub(r"<[^>]+>", "", inline(s))
def slugify(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:48]


def wrap(txt, n):
    out, cur = [], ""
    for w in txt.split():
        if cur and len(cur) + 1 + len(w) > n: out.append(cur); cur = w
        else: cur = (cur + " " + w).strip()
    return out + ([cur] if cur else [])
SVG_HEAD = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630" role="img" aria-labelledby="t d"><title id="t">%s</title><desc id="d">%s</desc><rect width="1200" height="630" fill="#EEF2F7"/><rect width="1200" height="12" fill="#0F1B2D"/>'
def boxes_svg(boxes, y0, h, per=None):
    y0s = y0; n = per or len(boxes); w = (1056 - 33 * (n - 1)) // n; o = ['<g font-family="system-ui,Arial,sans-serif" fill="#0F1B2D">']
    for i, (b, sub) in enumerate(boxes):
        x = 72 + (i % n) * (w + 33); y0 = y0 if not per else y0s + (i // n) * (h + 20)
        o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="#fff" stroke="#0F1B2D" stroke-width="3"/><text x="%d" y="%d" font-size="40" font-weight="600" fill="#1F4FD8">%d</text>' % (x, y0, w, h, x + 22, y0 + 46, i + 1))
        for k, ln in enumerate(wrap(b, max(8, w // 15))[:3]): o.append('<text x="%d" y="%d" font-size="24" font-weight="600">%s</text>' % (x + 22, y0 + 94 + 30 * k, E(ln)))
        for k, ln in enumerate(wrap(sub, max(10, w // 11))[:2]): o.append('<text x="%d" y="%d" font-size="19" fill="#556070">%s</text>' % (x + 22, y0 + h - 44 + 24 * k, E(ln)))
    return "".join(o) + "</g>"
def make_hero(fm, slug):
    if check_only(): return
    bx = [(a.split("|")[0].strip(), (a.split("|") + [""])[1].strip()) for a in fm["hero_boxes"].split(";") if a.strip()][:4]
    t = wrap(fm["h1"], 24)[:3]; fs = 60 if len(t) < 3 else 52
    o = SVG_HEAD % (E(fm["h1"]), E(fm.get("hero_alt", fm["h1"])))
    for i, ln in enumerate(t): o += '<text x="72" y="%d" font-family="Georgia,\'Times New Roman\',serif" font-size="%d" font-weight="600" fill="#0F1B2D">%s</text>' % (118 + i * (fs + 12), fs, E(ln))
    o += '<text x="72" y="%d" font-family="system-ui,Arial,sans-serif" font-size="26" fill="#556070">%s</text>' % (118 + len(t) * (fs + 12) + 14, E(fm.get("hero_sub", "")[:70]))
    o += boxes_svg(bx, 340, 230) + "</svg>"
    open(os.path.join(PUB, "blog", "img", slug + "-hero.svg"), "w", encoding="utf-8").write(o)
def make_steps(slug, title, steps):
    st = [(re.split(r"[:;]|\.(?=\s)", plain(x))[0], "") for x in steps][:6]
    st = [(" ".join(a.split()[:9]), "") for a, _ in st]
    o = SVG_HEAD % (E(title), E(" / ".join(a for a, _ in st)))
    tl = wrap(title, 42)[:2]
    for k, ln in enumerate(tl): o += '<text x="72" y="%d" font-family="Georgia,serif" font-size="42" font-weight="600" fill="#0F1B2D">%s</text>' % (96 + 52 * k, E(ln))
    o += (boxes_svg(st, 185, 175, 3) if len(st) > 4 else boxes_svg(st, 220, 330)) + "</svg>"
    open(os.path.join(PUB, "blog", "img", slug + "-steps.svg"), "w", encoding="utf-8").write(o)
def authors():
    p = os.path.join(ROOT, "data", "authors.json")
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}

def check_only(): return "--check" in sys.argv

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
        if ln.startswith("```"):
            flush_para(buf); buf = []; i += 1; code = []
            while i < len(lines) and not lines[i].startswith("```"):
                code.append(lines[i]); i += 1
            i += 1; out.append("<pre><code>%s</code></pre>" % E("\n".join(code), quote=False)); continue
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
    return ('<form class="bw" action="/app.html#/new" method="get" aria-labelledby="bw-h"><h2 id="bw-h">%s</h2>'
            '<input type="hidden" name="utm_source" value="blog"><input type="hidden" name="utm_medium" value="article"><input type="hidden" name="utm_campaign" value="%s">'
            '<div class="bwr"><label class="sr" for="bw-u">URL</label><input id="bw-u" name="url" type="text" inputmode="url" autocomplete="url" autocapitalize="off" spellcheck="false" placeholder="%s" required>'
            '<button class="btn p" type="submit">%s</button></div><p class="gloss">%s</p></form>') % (E(t["w_h"]), E(slug), E(t["w_ph"]), E(t["w_go"]), E(t["w_note"]))

def free_box(loc, slug):  # RES-3089: the free 10-page check sits right after the short answer; the EUR 9 audit box sits lower
    t = UI[loc]
    return ('<form class="bw bwf" action="%s" method="get" aria-labelledby="fw-h"><h2 id="fw-h">%s</h2>'
            '<input type="hidden" name="utm_source" value="blog"><input type="hidden" name="utm_medium" value="article"><input type="hidden" name="utm_campaign" value="%s"><input type="hidden" name="utm_content" value="free-box">'
            '<div class="bwr"><label class="sr" for="fw-u">URL</label><input id="fw-u" name="url" type="text" inputmode="url" autocomplete="url" autocapitalize="off" spellcheck="false" placeholder="%s" required>'
            '<button class="btn p" type="submit">%s</button></div><p class="gloss">%s</p></form>') % (E(t["chk"]), E(t["f_h"]), E(slug), E(t["w_ph"]), E(t["f_go"]), E(t["f_note"]))

def shell(loc, title, desc, canon, alts, og, jsonld, main, extra_head=""):
    t = UI[loc]
    ld = "".join('<script type="application/ld+json">%s</script>' % json.dumps(j, ensure_ascii=False).replace("</", "<\\/") for j in jsonld)
    alt = "".join('<link rel="alternate" hreflang="%s" href="%s%s">' % (l, SITE, p) for l, p in alts)
    return docshell.transform(f'''<!doctype html>
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
''')

GROUPS = {("root", "ai-visibility-audit"): [("en", "/ai-visibility-audit")]}  # EN page is static HTML
def article_path(fm):
    loc, slug = fm["locale"], fm["slug"]
    return ("%s/%s/%s" % (prefix(loc), fm.get("section", "blog"), slug)) if fm.get("section") != "root" else "%s/%s" % (prefix(loc), slug)

def fr_typo(doc):  # RES-3165: French typography, U+202F before ? ! : ; in text nodes and meta/alt text, never in code, scripts or URLs
    def fix(t): return re.sub(r"(?<=[^\s<>&])[ \u00a0]([?!:;])(?=\s|$|<|[\"'])", "\u202f\\1", t)
    parts = re.split(r"(<script(?! type=\"application/ld\+json\")\b.*?</script>|<(?:style|pre|code)\b.*?</(?:style|pre|code)>|<[^>]+>)", doc, flags=re.S)
    out = []
    for x in parts:
        if x.startswith("<"):
            if x.startswith(("<meta", "<img")): x = re.sub(r'((?:content|alt)=")([^"]*)', lambda m: m.group(1) + fix(m.group(2)), x)
            out.append(x)
        else: out.append(fix(x))
    return "".join(out)

def build_article(fm, body, arts):
    loc, slug = fm["locale"], fm["slug"]
    t, state = UI[loc], {"imgs": 0}
    path = ("%s/%s/%s" % (prefix(loc), fm.get("section", "blog"), slug)) if fm.get("section") != "root" else "%s/%s" % (prefix(loc), slug)
    html_body, faq, steps, srcs = render_body(body, fm, loc, state)
    if state["imgs"] < 1 and fm.get("hero") is None: sys.exit("%s: needs images" % slug)
    img = slug if loc == "en" else slug + "-" + loc
    if fm.get("hero") == "auto":
        make_hero(fm, img); fm["hero"] = img + "-hero.svg"
    if fm.get("steps_img") == "on" and not steps:  # no numbered list: the image lists the first four sections instead
        steps = [re.sub(r"<[^>]+>", "", h) for i, h in re.findall(r'<h2 id="([^"]+)">(.+?)</h2>', html_body) if i not in ("faq", "sources")][:4]
        sect_fig = True
    else: sect_fig = False
    if fm.get("steps_img") == "on" and steps and not check_only():
        make_steps(img, fm["h1"], steps)
        fig = '<figure><img src="/blog/img/%s-steps.svg" alt="%s" width="1200" height="630" loading="lazy" decoding="async"></figure>' % (img, E(fm["h1"] + ": " + " / ".join(" ".join(plain(x).split()[:7]) for x in steps[:5])))
        if sect_fig:
            parts = html_body.split("<h2 ", 3); html_body = "<h2 ".join(parts[:2]) + "<h2 " + parts[2] + fig + "<h2 " + parts[3] if len(parts) > 3 else html_body + fig
        else: html_body = html_body.replace('<ol class="steps">', fig + '<ol class="steps">', 1)
    hero = fm.get("hero", "")
    og = "/blog/img/%s" % fm["og"] if fm.get("og") else "/og-v2.png"
    ans = '<aside class="answer" aria-label="%s"><b>%s</b><p>%s</p></aside>' % (E(t["answer"]), E(t["answer"]), E(fm["answer"]))
    w = widget(loc, slug) if fm.get("widget", "on") != "off" else ""
    fb = free_box(loc, slug) if fm.get("widget", "on") != "off" else ""
    ad = '<aside class="ad-slot" aria-label="%s" data-slot="in-article"></aside>' % E(t["ad"]) if ADS_ENABLED and fm.get("ads") != "off" else "<!-- ad-slot:in-article (off) -->"
    rel = [r.split("|", 1) for r in fm.get("related", "").split(";") if "|" in r]
    rel_h = ('<nav class="rel" aria-label="%s"><h2>%s</h2><ul>%s</ul></nav>' % (E(t["related"]), E(t["related"]), "".join('<li><a href="%s">%s</a></li>' % (E(u.strip()), E(x.strip())) for u, x in rel))) if rel else ""
    cta = '<section class="cta2"><h2>%s</h2><p>%s</p><a class="btn p" href="%s?utm_source=blog&amp;utm_medium=article&amp;utm_campaign=%s&amp;utm_content=cta">%s</a><p class="gloss">%s</p></section>' % (E(t["cta_h"]), E(t["cta_b"]), t["chk"], E(slug), E(t["cta"]), E(t["price"]))
    hero_h = '<figure class="hero"><img src="/blog/img/%s" alt="%s" width="1200" height="630" fetchpriority="high" decoding="async"></figure>' % (E(hero), E(fm.get("hero_alt", fm["h1"]))) if hero else ""
    if hero and not fm.get("hero_alt"): sys.exit("%s: hero needs hero_alt" % slug)
    alts = [(l, p) for l, p in (kv.split("=", 1) for kv in fm.get("translations", "").split(";") if "=" in kv)]
    if not alts and len(GROUPS.get((fm.get("section", "blog"), slug), [])) > 1:
        alts = [(l, p) for l, p in GROUPS[(fm.get("section", "blog"), slug)] if l != loc]
    if alts: alts = [(loc, path)] + [(l.strip(), p.strip()) for l, p in alts]; alts.append(("x-default", next((p for l, p in alts if l == "en"), path)))
    org = {"@type": "Organization", "name": "CitedBy", "url": SITE + "/"}
    art = {"@context": "https://schema.org", "@type": "Article", "headline": fm["h1"], "description": fm["description"], "inLanguage": loc, "datePublished": fm["date"], "dateModified": fm["reviewed"],
           "author": {"@type": "Organization", "name": "CitedBy editorial team", "url": SITE + prefix(loc) + "/about#editorial"}, "publisher": org, "mainEntityOfPage": SITE + path,
           "image": [SITE + og] + ([SITE + "/blog/img/" + hero] if hero else [])}
    ld = [art, {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": t["home"], "item": SITE + (prefix(loc) or "/")},
        {"@type": "ListItem", "position": 2, "name": SECT_NAME.get(fm.get("section"), t["blog"]), "item": SITE + prefix(loc) + "/" + SECT_PATH.get(fm.get("section"), "blog")},
        {"@type": "ListItem", "position": 3, "name": fm["h1"], "item": SITE + path}]}]
    if faq: ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": html.unescape(plain(" ".join(a)))}} for q, a in faq]})
    if fm.get("howto") == "on" and steps: ld.append({"@context": "https://schema.org", "@type": "HowTo", "name": fm["h1"], "step": [{"@type": "HowToStep", "position": n + 1, "text": html.unescape(plain(s))} for n, s in enumerate(steps)]})
    # ad slot sits after the first third of the body, never beside the widget or CTA
    parts = html_body.split("\n"); cut = max(1, len(parts) // 3)
    body_h = "\n".join(parts[:cut] + [ad] + parts[cut:])
    heads = re.findall(r'<h2 id="([^"]+)">(.+?)</h2>', html_body)
    toc = '<nav class="toc" aria-label="%s"><b>%s</b><ol>%s</ol></nav>' % (E(t["toc"]), E(t["toc"]), "".join('<li><a href="#%s">%s</a></li>' % (i, h) for i, h in heads)) if len(heads) >= 3 else ""
    au = authors().get(fm.get("author", ""))
    byline = ('%s <a href="/authors/%s" rel="author">%s</a>, %s · ' % (E(t["by_person"]), E(fm["author"]), E(au["name"]), E(au["role"].get(loc, au["role"]["en"])))) if au else '<a href="%s/about#editorial">%s</a> · ' % (prefix(loc), E(t["by"]))
    if au: art["author"] = {"@type": "Person", "name": au["name"], "jobTitle": au["role"]["en"], "url": SITE + "/authors/" + fm["author"]}
    def own_src(x):  # RES-3141: our own pages stay in the list but are not an outside check
        m = re.search(r'\]\(([^)\s]+)', x); u = m.group(1) if m else ""
        return u.startswith("/") or re.match(r"https?://(www\.)?citedby\.eu(/|$)", u) is not None
    n_ext = sum(1 for x in srcs if not own_src(x))
    en_tag = "" if loc == "en" else " (EN)"  # RES-3165: /methodology exists in English only
    meth = t["src_n"].format(n=n_ext) if n_ext >= 2 else t["src_n"].split(" · ")[-1]  # RES-3165: keep the bare method link when the count is hidden
    srcn = ' · <a href="/methodology">%s</a>%s' % (E(meth), en_tag)
    main = f'''<main id="main" class="art"><article>
<p class="dateline"><a href="{prefix(loc)}/{SECT_PATH.get(fm.get("section"), "blog")}">{E(SECT_NAME.get(fm.get("section"), t["blog"]))}</a> / {E(fm.get("cluster", ""))}</p>
<h1>{E(fm["h1"])}</h1>
<p class="byline">{byline}{E(t["rev"])} <time datetime="{fm["reviewed"]}">{fm["reviewed"]}</time>{srcn}</p>
{ans}
{fb}
{hero_h}
{toc}
{body_h}
{w}
{cta}
{rel_h}
</article></main>'''
    return path, shell(loc, fm["title"], fm["description"], path, alts, og, ld, main)

INDEX_LOCALES = {"blog": ("en", "fr", "nl", "de", "es"), "guides": ("en", "fr", "nl", "de", "es"), "bots": ("en",), "platforms": ("en",)}
SECT_NAME, SECT_PATH = {"bots": "AI crawlers", "platforms": "AI crawler settings by platform"}, {"bots": "bots", "platforms": "platforms"}  # sections that have their own hub (H3 page sets)
BOTS_IDX = ("AI crawlers: who they are, what they do, how to allow or block them", "One page per AI crawler, with the operator, the robots.txt token, the vendor's own sentence, what blocking costs and the vendor's published address list, each read from the vendor's page on the date shown.")
PLATFORMS_IDX = ("How to allow or block AI crawlers on Shopify, Squarespace, Wix, Webflow, WordPress.com and Cloudflare", "One page per platform: where its own help page says the setting lives, what it does and does not cover, and the one thing that page says that the others do not, each read on the date shown.")
BLOG_IDX = {'en': ('AI visibility blog for online shops', 'Notes and data on how AI assistants treat online shops, plus our step-by-step guides. Each post ends with an audit you can run on your own site.'), 'fr': ('Blog visibilité IA pour boutiques en ligne', 'Notes et données sur la façon dont les assistants IA traitent les boutiques en ligne, et nos guides pas à pas. Chaque article mène à un audit de votre site.'), 'nl': ('Blog AI-zichtbaarheid voor webshops', 'Notities en data over hoe AI-assistenten webshops behandelen, plus onze stap-voor-stap-gidsen. Elk artikel leidt naar een audit van je site.'), 'de': ('Blog zur KI-Sichtbarkeit für Online-Shops', 'Notizen und Daten dazu, wie KI-Assistenten Online-Shops behandeln, plus unsere Schritt-für-Schritt-Ratgeber. Jeder Beitrag führt zu einem Audit Ihrer Seite.'), 'es': ('Blog de visibilidad en IA para tiendas online', 'Notas y datos sobre cómo los asistentes de IA tratan las tiendas online, más nuestras guías paso a paso. Cada artículo lleva a una auditoría de tu web.')}

IDX_INTRO = {  # RES-2935: a second paragraph that says what the hub holds, with facts only from the pages it lists (a hub of titles alone is thin and gives an assistant nothing to quote)
    ("guides", "en"): "These guides cover where to edit robots.txt and find the sitemap on Shopify and WooCommerce, how to check product JSON-LD, ten technical checks you can run by hand, how to see whether ChatGPT, Perplexity and Gemini name your shop, and how the AI visibility tools compare on price.",
    ("guides", "fr"): "Ces guides expliquent où modifier robots.txt et trouver le sitemap sur Shopify et WooCommerce, comment vérifier le JSON-LD produit et quelles vérifications techniques faire à la main pour qu'un assistant IA lise votre boutique.",
    ("guides", "nl"): "Deze gidsen laten zien waar je robots.txt aanpast en de sitemap vindt op Shopify en WooCommerce, hoe je product-JSON-LD controleert en welke technische controles je zelf doet zodat een AI-assistent je webshop kan lezen.",
    ("guides", "de"): "Diese Ratgeber zeigen, wo Sie bei Shopify und WooCommerce robots.txt bearbeiten und die Sitemap finden, wie Sie Produkt-JSON-LD prüfen und welche technischen Prüfungen Sie von Hand machen, damit ein KI-Assistent Ihren Shop lesen kann.",
    ("guides", "es"): "Estas guías explican dónde editar robots.txt y encontrar el sitemap en Shopify y WooCommerce, cómo revisar el JSON-LD de producto y qué comprobaciones técnicas puedes hacer a mano para que un asistente de IA lea tu tienda.",
    ("blog", "en"): "The posts cover whether ChatGPT can read your website, whether llms.txt works, how to track AI referral traffic in GA4, how to check what AI says about your brand and what to do when an assistant shows a wrong price.",
    ("blog", "fr"): "Les articles expliquent si ChatGPT peut lire votre site, si llms.txt fonctionne, comment suivre le trafic de référence IA dans GA4, comment vérifier ce que l'IA dit de votre marque et que faire quand un assistant affiche un mauvais prix.",
    ("blog", "nl"): "De artikelen gaan over of ChatGPT je website kan lezen, of llms.txt werkt, hoe je AI-verwijzingsverkeer in GA4 volgt, hoe je controleert wat AI over je merk zegt en wat te doen als een assistent een verkeerde prijs toont.",
    ("blog", "de"): "Die Beiträge behandeln, ob ChatGPT Ihre Website lesen kann, ob llms.txt funktioniert, wie Sie KI-Verweisverkehr in GA4 verfolgen, wie Sie prüfen, was KI über Ihre Marke sagt, und was bei einem falschen Preis in einem Assistenten zu tun ist.",
    ("blog", "es"): "Los artículos tratan si ChatGPT puede leer tu web, si funciona llms.txt, cómo medir el tráfico de referencia de IA en GA4, cómo comprobar qué dice la IA de tu marca y qué hacer cuando un asistente muestra un precio equivocado.",
    ("bots", "en"): "An AI crawler is a bot that fetches pages for an assistant such as ChatGPT, Claude, Perplexity or Gemini. Each page below names the operator, the robots.txt token, what blocking costs and the vendor's published address list, so you can decide per bot whether to allow it.",
    ("platforms", "en"): "Each page names the platform's own help page, where the AI-crawler setting sits, what it covers and what it does not: Shopify, Squarespace, Wix, Webflow, WordPress.com and Cloudflare.",
}

IDX_META = {"bots": ("AI crawlers: what they do, how to allow or block them", "One page per AI crawler: operator, robots.txt token, what blocking costs and the vendor's published address list, each read from the vendor's page."),
            "platforms": ("Allow or block AI crawlers on six site platforms", "One page per platform: where its help page says the setting lives, what it covers and does not cover, and what only that page says, each read on a stated date.")}  # RES-2935: title 15-65 and description 50-160, not the long H1 and lede

def build_index(loc, arts, sect="blog"):
    t = dict(UI[loc])  # /blog and /guides get their own title, H1 and description (RES-2210)
    if sect == "blog": t["idx_h1"], t["idx_lede"] = BLOG_IDX[loc]
    if sect == "bots": t["idx_h1"], t["idx_lede"] = BOTS_IDX
    if sect == "platforms": t["idx_h1"], t["idx_lede"] = PLATFORMS_IDX
    path = prefix(loc) + "/" + sect
    cards = "".join('<li><a href="%s/%s/%s"><b>%s</b><span>%s</span><time datetime="%s">%s %s</time></a></li>' % (prefix(loc), a.get("section", "blog"), a["slug"], E(a["h1"]), E(a["description"]), a["reviewed"], E(t["rev"]), a["reviewed"]) for a in sorted(arts, key=lambda a: a["reviewed"], reverse=True))
    ld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": t["idx_h1"], "inLanguage": loc, "url": SITE + path},
          {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": n + 1, "url": "%s%s/%s/%s" % (SITE, prefix(loc), a.get("section", "blog"), a["slug"])} for n, a in enumerate(arts)]}]
    main = '<main id="main" class="art idx"><h1>%s</h1><p class="lede">%s</p>%s<ul class="cards">%s</ul></main>' % (E(t["idx_h1"]), E(t["idx_lede"]), ("<p>%s</p>" % E(IDX_INTRO[(sect, loc)])) if (sect, loc) in IDX_INTRO else "", cards)
    alts = [(l, prefix(l) + "/" + sect) for l in UI if l in INDEX_LOCALES[sect]] + [("x-default", "/" + sect)]  # reciprocal hreflang across the 5 indexes (RES-2210)
    ti, de = IDX_META.get(sect, (t["idx_h1"], t["idx_lede"]))
    return path, shell(loc, ti + ". CitedBy", de, path, alts, "/og-v2.png", ld, main)

def main():
    check = "--check" in sys.argv
    arts = {}
    for p in sorted(glob.glob(os.path.join(SRC, "*.md"))):
        fm, body = parse(p); arts.setdefault(fm["locale"], []).append((fm, body))
    urls, written = [], []
    for loc, items in arts.items():
        for fm, _ in items: GROUPS.setdefault((fm.get("section", "blog"), fm["slug"]), []).append((loc, article_path(fm)))
    for loc, items in arts.items():
        for fm, body in items:
            path, doc = build_article(fm, body, items); urls.append((path, fm["reviewed"])); written.append((path, doc))
        bl = [f for f, _ in items if f.get("section", "blog") in ("blog", "guides")]
        path, doc = build_index(loc, bl); urls.append((path, max(f["reviewed"] for f in bl))); written.append((path, doc))
        gl = [f for f in bl if f.get("section") == "guides"]
        if gl:
            path, doc = build_index(loc, gl, "guides"); urls.append((path, max(f["reviewed"] for f in gl))); written.append((path, doc))
        bt = [f for f, _ in items if f.get("section") == "bots"]
        if bt:
            path, doc = build_index(loc, bt, "bots"); urls.append((path, max(f["reviewed"] for f in bt))); written.append((path, doc))
        pt = [f for f, _ in items if f.get("section") == "platforms"]
        if pt:
            path, doc = build_index(loc, pt, "platforms"); urls.append((path, max(f["reviewed"] for f in pt))); written.append((path, doc))
    if check: print("ok: %d pages" % len(written)); return
    for path, doc in written:
        if path.startswith("/fr/"): doc = fr_typo(doc)
        out = os.path.join(PUB, path.lstrip("/"))
        if path.endswith(("/blog", "/guides", "/bots", "/platforms")): out = os.path.join(out, "index.html")
        else: out += ".html"
        os.makedirs(os.path.dirname(out), exist_ok=True); open(out, "w", encoding="utf-8").write(doc)
    sm = os.path.join(PUB, "sitemap.xml"); s = open(sm, encoding="utf-8").read()
    s = re.sub(r"<url><loc>%s(?:/[a-z]{2}/ai-visibility-audit|(?:/[a-z]{2})?/(?:blog|compare|guides|bots|platforms)[^<]*)</loc>(<lastmod>[^<]*</lastmod>)?</url>" % re.escape(SITE), "", s)
    s = s.replace("</urlset>", "".join("<url><loc>%s%s</loc><lastmod>%s</lastmod></url>" % (SITE, p, d) for p, d in urls) + "</urlset>")
    for extra in ("/data", "/bot", "/ci", "/data/study-chatgpt-buyer-questions", "/fr/about", "/nl/about", "/de/about", "/es/about"):  # live pages the sitemap lacked (RES-1998)
        if "<loc>%s%s</loc>" % (SITE, extra) not in s: s = s.replace("</urlset>", "<url><loc>%s%s</loc><lastmod>2026-10-20</lastmod></url></urlset>" % (SITE, extra))
    open(sm, "w", encoding="utf-8").write(s)
    print("wrote %d pages" % len(written))
main()
