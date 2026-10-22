#!/usr/bin/env python3
"""Write /privacy, /terms, /refund and /<fr|nl|de|es>/{privacy,terms,refund} from the legal v2 texts (RES-2203).
Source: <company-memory>/products/citedby/legal-v2/<lang>/<page>.md (default path below, or argv[1]). Output: public/[<lang>/]<page>.html, committed, so the
image needs no access to the texts. Run after editing them; `--check` exits 1 if a committed page differs. Standard library only."""
import datetime, html, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import docshell
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PUB = os.path.join(ROOT, "public"); SITE = "https://citedby.eu"; E = html.escape
SRC = next((a for a in sys.argv[1:] if not a.startswith("--")), os.path.expanduser("~/work/company-memory/products/citedby/legal-v2"))
LANGS = ["en", "fr", "nl", "de", "es"]
PAGES = ["privacy", "terms", "refund"]
UI = {  # masthead and footer labels, per language
    "en": dict(check="What we check", plans="Pricing", blog="Guides", data="Data", signin="Sign in", cta="Audit a site", skip="Skip to content", main="Main",
               terms="Terms", privacy="Privacy", refund="Refunds", contact="Contact", legal="Legal notice", home="/", plans_h="/plans", blog_h="/blog", sw="Language"),
    "fr": dict(check="Ce que nous vérifions", plans="Tarifs", blog="Guides", data="Données", signin="Connexion", cta="Auditer un site", skip="Aller au contenu", main="Principal",
               terms="Conditions", privacy="Confidentialité", refund="Remboursements", contact="Contact", legal="Mentions légales", home="/fr", plans_h="/fr/plans", blog_h="/fr/blog", sw="Langue"),
    "nl": dict(check="Wat wij controleren", plans="Prijzen", blog="Gidsen", data="Data", signin="Inloggen", cta="Een site auditen", skip="Naar de inhoud", main="Hoofdmenu",
               terms="Voorwaarden", privacy="Privacy", refund="Terugbetaling", contact="Contact", legal="Juridische informatie", home="/nl", plans_h="/nl/plans", blog_h="/nl/blog", sw="Taal"),
    "de": dict(check="Was wir prüfen", plans="Preise", blog="Ratgeber", data="Daten", signin="Anmelden", cta="Website prüfen", skip="Zum Inhalt", main="Hauptmenü",
               terms="AGB", privacy="Datenschutz", refund="Erstattungen", contact="Kontakt", legal="Impressum", home="/de", plans_h="/de/plans", blog_h="/de/blog", sw="Sprache"),
    "es": dict(check="Qué comprobamos", plans="Precios", blog="Guías", data="Datos", signin="Iniciar sesión", cta="Auditar un sitio", skip="Saltar al contenido", main="Principal",
               terms="Condiciones", privacy="Privacidad", refund="Reembolsos", contact="Contacto", legal="Aviso legal", home="/es", plans_h="/es/plans", blog_h="/es/blog", sw="Idioma"),
}
TABLE_CSS = (".lt{overflow-x:auto}@media(min-width:641px){.lt table{min-width:620px}}"
             "@media(max-width:640px){.lt table,.lt tbody,.lt tr,.lt td{display:block;width:100%}.lt thead{position:absolute;left:-9999px}"
             ".lt tr{border-bottom:2px solid var(--rule);padding:10px 0}.lt td{border:0;padding:6px 0}"
             ".lt td::before{content:attr(data-label);display:block;font-weight:600;color:var(--navy);font-size:13px}}")
TITLES = {  # <title> and JSON-LD name per page (15-65 characters in total, unique per language); the H1 stays the legal text's own heading (RES-2935)
    "terms": {"en": "Terms of service", "fr": "Conditions générales", "nl": "Algemene voorwaarden", "de": "Allgemeine Geschäftsbedingungen", "es": "Condiciones del servicio"},
    "privacy": {"en": "Privacy policy", "fr": "Politique de confidentialité", "nl": "Privacyverklaring", "de": "Datenschutzerklärung", "es": "Política de privacidad"}}
NAMES = {"en": "English", "fr": "Français", "nl": "Nederlands", "de": "Deutsch", "es": "Español"}
LOC_PAGES = ("/privacy", "/terms", "/refund", "/withdraw")  # link targets that exist once per language


def path(lang, page): return f"/{page}" if lang == "en" else f"/{lang}/{page}"


def inline(s, lang):
    s = E(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    def link(m):
        href = m.group(2)
        if lang != "en" and href in LOC_PAGES: href = f"/{lang}{href}"
        ext = ' rel="noopener"' if href.startswith("http") else ""
        return f'<a href="{href}"{ext}>{m.group(1)}</a>'
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, s)
    return re.sub(r"(?<![\w/])(hello@citedby\.eu)(?![\w<])", r'<a href="mailto:\1">\1</a>', s) if "mailto:" not in s else s


def render_md(md, lang):
    out, lines, i = [], md.split("\n"), 0
    while i < len(lines):
        ln = lines[i]
        if not ln.strip(): i += 1; continue
        m = re.match(r"(#{1,3}) (.*)", ln)
        if m:
            n = len(m.group(1)); out.append(f"<h{n}>{inline(m.group(2), lang)}</h{n}>"); i += 1; continue
        if ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"): rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i += 1
            head, body = rows[0], [r for r in rows[2:]]
            t = "<thead><tr>" + "".join(f"<th>{inline(c, lang)}</th>" for c in head) + "</tr></thead><tbody>"
            t += "".join("<tr>" + "".join(f'<td data-label="{E(head[j] if j < len(head) else "", quote=True)}">{inline(c, lang)}</td>' for j, c in enumerate(r)) + "</tr>" for r in body) + "</tbody>"
            out.append(f'<div class="lt"><table>{t}</table></div>'); continue
        if ln.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "): items.append(inline(lines[i][2:], lang)); i += 1
            out.append("<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"); continue
        if re.match(r"\d+\. ", ln):
            items = []
            while i < len(lines) and re.match(r"\d+\. ", lines[i]): items.append(inline(re.sub(r"^\d+\. ", "", lines[i]), lang)); i += 1
            out.append("<ol>" + "".join(f"<li>{x}</li>" for x in items) + "</ol>"); continue
        if ln.startswith(">"):
            paras, cur = [], []
            while i < len(lines) and lines[i].startswith(">"):
                t = lines[i][1:].strip()
                if t: cur.append(inline(t, lang))
                elif cur: paras.append("<br>".join(cur)); cur = []
                i += 1
            if cur: paras.append("<br>".join(cur))
            out.append("<blockquote>" + "".join(f"<p>{p}</p>" for p in paras) + "</blockquote>"); continue
        para = []
        while i < len(lines) and lines[i].strip() and not re.match(r"(#{1,3} |\||- |\d+\. |>)", lines[i]): para.append(inline(lines[i], lang)); i += 1
        out.append("<p>" + " ".join(para) + "</p>")
    return "\n".join(out)


def shell(lang, page, title, desc, body_html):
    title = TITLES.get(page, {}).get(lang, title)
    t, base = UI[lang], f"{SITE}{path(lang, page)}"
    alts = "".join(f'<link rel="alternate" hreflang="{c}" href="{SITE}{path(c, page)}">' for c in LANGS) + f'<link rel="alternate" hreflang="x-default" href="{SITE}{path("en", page)}">'
    css = open(os.path.join(PUB, "privacy.html"), encoding="utf-8").read()
    ver = docshell.ver()
    ld = ('{"@context": "https://schema.org", "@type": "WebPage", "name": %s, "url": "%s", "inLanguage": "%s", "description": %s, "isPartOf": {"@type": "WebSite", "name": "CitedBy", "url": "https://citedby.eu"}, '
          '"publisher": {"@type": "Organization", "@id": "https://citedby.eu/#org", "name": "CitedBy", "url": "https://citedby.eu"}}')
    import json
    ld = ld % (json.dumps(title + ". CitedBy", ensure_ascii=False), base, lang, json.dumps(desc, ensure_ascii=False))
    sw = " · ".join(f'<a href="{path(c, page)}" hreflang="{c}" lang="{c}"' + (' aria-current="true"' if c == lang else "") + f">{NAMES[c]}</a>" for c in LANGS)
    return (f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(title)}. CitedBy</title>'
            f'<meta name="description" content="{E(desc)}"><link rel="canonical" href="{base}">{alts}<link rel="icon" href="/favicon.svg">'
            f'<link rel="stylesheet" href="/saas.css"><link rel="stylesheet" href="/doc.css?v={ver}"><style>{TABLE_CSS}</style><script type="application/ld+json">{ld}</script></head><body class="cb dc">'
            f'<a class="sr" href="#main">{E(t["skip"])}</a>\n<header class="topbar"><div class="in"><a class="mark" href="{t["home"]}"><i></i>CitedBy</a>'
            f'<nav aria-label="{E(t["main"])}"><a class="opt" href="{t["home"].rstrip("/")}/#checks">{E(t["check"])}</a><a href="{t["plans_h"]}">{E(t["plans"])}</a><a href="{t["blog_h"]}">{E(t["blog"])}</a><a class="opt" href="/data">{E(t["data"])}</a></nav>'
            f'<a class="signin" href="/signin?next=%2Fapp.html">{E(t["signin"])}</a><a class="btn sm go" href="/app.html#/new">{E(t["cta"])}</a></div></header>'
            f'<main id="main">{body_html}</main>'
            f'<footer><div class="w"><span>© 2026 CitedBy · <a href="mailto:hello@citedby.eu">hello@citedby.eu</a></span><a href="{t["plans_h"]}">{E(t["plans"])}</a><a href="{t["blog_h"]}">{E(t["blog"])}</a><a href="/data">{E(t["data"])}</a>'
            f'<a href="{path(lang, "terms")}">{E(t["terms"])}</a><a href="{path(lang, "privacy")}">{E(t["privacy"])}</a><a href="{path(lang, "refund")}">{E(t["refund"])}</a>'
            f'<a href="/contact">{E(t["contact"])}</a><a href="/legal">{E(t["legal"])}</a><span class="langsw" role="group" aria-label="{E(t["sw"])}">{sw}</span></div></footer></body></html>\n')


def build(lang, page):
    md = open(os.path.join(SRC, lang, page + ".md"), encoding="utf-8").read()
    m = re.match(r"# (.*)\n", md)
    title, rest = m.group(1).strip(), md[m.end():]
    body = f"<h1>{E(title)}</h1>\n" + render_md(rest, lang)
    first = next(p for p in re.findall(r"<p>(.*?)</p>", body, flags=re.S) if len(re.sub(r"<[^>]+>", "", p)) > 60)
    desc = html.unescape(re.sub(r"<[^>]+>", "", first)); desc = desc if len(desc) <= 155 else desc[:152].rsplit(" ", 1)[0] + "..."
    return shell(lang, page, title, desc, body)


def main():
    check, bad = "--check" in sys.argv, 0
    for lang in LANGS:
        for page in PAGES:
            out = os.path.join(PUB, path(lang, page).lstrip("/") + ".html")
            new = build(lang, page)
            if check:
                bad += (not os.path.exists(out)) or open(out, encoding="utf-8").read() != new
                continue
            os.makedirs(os.path.dirname(out), exist_ok=True)
            open(out, "w", encoding="utf-8").write(new)
    print("differs:" if check else "wrote 15 legal pages", bad if check else "")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
