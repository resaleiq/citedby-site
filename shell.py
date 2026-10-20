"""One header, proof strip and footer for every marketing page (RES-1335 S2 check 1): home, /pricing, /data, /thanks, /faq.
The same functions render all of them; /data (a static file) gets them through tools/apply_shell.py. Standard library only."""
import datetime, hashlib, html, json, os

E = html.escape
HERE = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.join(HERE, "public")
MONTHS = {"en": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
          "fr": ["janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc."]}


def fmt_date(d, lang):
    return f"{d.day} {MONTHS['fr' if lang == 'fr' else 'en'][d.month - 1]} {d.year}"


def day0():
    """Our own day-0 audit, summarised from public/data/day0-citedby-eu.csv by tools/build_day0_summary.py."""
    return json.load(open(os.path.join(HERE, "data", "day0.json")))


def day0_date(lang):
    return fmt_date(datetime.date.fromisoformat(day0()["date"]), lang)


def asset_ver(name):
    try:
        return hashlib.sha256(open(os.path.join(PUBLIC, name), "rb").read()).hexdigest()[:8]
    except OSError:
        return ""


S = {
 "en": dict(
  skip="Skip to content", home="CitedBy home", main="Main", foot_nav="Footer", langlabel="Language", path="/", other="/fr",
  nav=(("/grade", "Scan"), ("/pricing", "Prices"), ("/data", "Data"), ("/faq", "FAQ")),
  own="OUR OWN SITE", proof="Named in {n} of {a} category answers. Counted {date}, {k} assistants.", proof_link="Read the count", proof_href="/#proof",
  foot=(("/grade", "Scan"), ("/pricing", "Prices"), ("/data", "Data"), ("/faq", "FAQ"), ("/sample-audit", "Sample audit"), ("/terms", "Terms"), ("/refund", "Refunds"),
        ("/contact", "Contact"), ("/legal", "Legal notice"), ("/privacy", "Privacy")),
  copy="© 2026 CitedBy."),
 "fr": dict(
  skip="Aller au contenu", home="Accueil CitedBy", main="Principal", foot_nav="Pied de page", langlabel="Langue", path="/fr", other="/",
  nav=(("/grade", "Test gratuit"), ("/pricing", "Tarifs"), ("/data", "Données"), ("/fr#faq", "FAQ")),
  own="NOTRE PROPRE SITE", proof="Cité dans {n} réponse sur {a} (questions de catégorie). Compté le {date}, {k} assistants.", proof_link="Lire le décompte", proof_href="/fr#proof",
  foot=(("/grade", "Test gratuit"), ("/pricing", "Tarifs"), ("/data", "Données"), ("/fr#faq", "FAQ"), ("/sample-audit", "Exemple d'audit"), ("/terms", "Conditions"),
        ("/refund", "Remboursements"), ("/contact", "Contact"), ("/legal", "Mentions légales"), ("/privacy", "Confidentialité")),
  copy="© 2026 CitedBy."),
}


def header(lang="en", current=None):
    """Navy masthead (lockup v4, 4 links, EN/FR) plus the proof strip under it. `current` is the nav href of the open page."""
    t = S[lang]
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{E(n)}</a>' for h, n in t["nav"])
    sw = "".join(f'<a href="{p}" hreflang="{l}" lang="{l}"{" aria-current=\"true\"" if l == lang else ""}>{l.upper()}</a>' for l, p in (("en", "/"), ("fr", "/fr")))
    d = day0()
    if lang == "en":
        strip = f'<span>Named in <b class="big">{d["named"]} of {d["answers"]}</b> category answers. Counted {E(day0_date(lang))}, {len(d["assistants"])} assistants.</span>'
    else:
        strip = f'<span>Cité dans <b class="big">{d["named"]} réponse sur {d["answers"]}</b> (questions de catégorie). Compté le {E(day0_date(lang))}, {len(d["assistants"])} assistants.</span>'
    return (f'<a class="skip" href="#main">{E(t["skip"])}</a>\n'
            f'<header class="mast on-navy"><div class="wrap"><a class="brand" href="{t["path"]}" aria-label="{E(t["home"])}"><img src="/brand/citedby-lockup-v4-reverse.svg" alt="CitedBy" width="160" height="32"></a>'
            f'<nav class="nav" aria-label="{E(t["main"])}">{links}<span class="lang" role="group" aria-label="{E(t["langlabel"])}">{sw}</span></nav></div></header>\n')


def footer(lang="en"):
    t = S[lang]
    links = "".join(f'<a href="{h}">{E(n)}</a>' for h, n in t["foot"])
    return (f'<footer class="foot on-navy"><div class="wrap"><div class="grid"><div class="f1"><img src="/brand/citedby-lockup-v4-reverse.svg" alt="CitedBy" width="131" height="28">'
            f'<p>{E(t["copy"])} <a href="mailto:hello@citedby.eu">hello@citedby.eu</a></p></div><nav class="f2" aria-label="{E(t["foot_nav"])}">{links}</nav></div></div></footer>')


def document(lang, title, desc, path, main, *, ld=(), og_title=None, og_desc=None, current=None, robots=None, alts="", body_class="", extra_head=""):
    """The full page around `main`: head (icons, OG image, one stylesheet, preloaded heading face), shared header and footer."""
    t = S[lang]
    ogt, ogd = og_title or title, og_desc or desc
    ldj = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False).replace("</", "<\\/")}</script>' for x in ld)
    return f'''<!doctype html>
<html lang="{lang}"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">{f'<meta name="robots" content="{robots}">' if robots else ""}
<link rel="canonical" href="https://citedby.eu{path}">{alts}
<meta property="og:title" content="{E(ogt)}"><meta property="og:description" content="{E(ogd)}"><meta property="og:url" content="https://citedby.eu{path}"><meta property="og:type" content="website"><meta property="og:locale" content="{"fr_FR" if lang == "fr" else "en_IE"}"><meta property="og:image" content="https://citedby.eu/og-v2.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{E(ogt)}"><meta name="twitter:description" content="{E(ogd)}"><meta name="twitter:image" content="https://citedby.eu/og-v2.png">
<meta name="theme-color" content="#0F1B2D">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png"><link rel="icon" href="/favicon.ico" sizes="16x16 32x32 48x48"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preload" href="/fonts/newsreader-latin-600-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/site.css?v={asset_ver("site.css")}">{extra_head}
{ldj}
</head><body{f' class="{body_class}"' if body_class else ""}>
{header(lang, current)}
<main id="main">
{main}
</main>
{footer(lang)}
</body></html>
'''
