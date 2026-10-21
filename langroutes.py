"""Language routes, canonical + hreflang and the footer language switch for the five home pages (RES-1731 row 10)."""
import json

LANDING_PATHS = {"/fr": "fr", "/nl": "nl", "/de": "de", "/es": "es"}
LANG_NAMES = (("en", "English", ""), ("fr", "Français", "/fr"), ("nl", "Nederlands", "/nl"), ("de", "Deutsch", "/de"), ("es", "Español", "/es"))
SWITCH_LABEL = {"en": "Language", "fr": "Langue", "nl": "Taal", "de": "Sprache", "es": "Idioma"}
OG_LOCALE = {"en": "en_GB", "fr": "fr_FR", "nl": "nl_NL", "de": "de_DE", "es": "es_ES"}


SAME_AS = ["https://citedby.eu/about", "https://citedby.eu/methodology"]
_OFFERS = [("Single audit", "9"), ("Starter (monthly)", "19"), ("Pro (monthly)", "49"), ("Agency (monthly)", "99")]
LD = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": [
    {"@type": "Organization", "@id": "https://citedby.eu/#org", "name": "CitedBy", "url": "https://citedby.eu/", "logo": "https://citedby.eu/icon-192.png", "email": "hello@citedby.eu", "sameAs": SAME_AS},
    {"@type": "Product", "name": "CitedBy website audit", "brand": {"@id": "https://citedby.eu/#org"}, "description": "Crawls a website up to your plan's page limit and gives the exact fix for each issue.",
     "offers": [{"@type": "Offer", "name": n, "price": pr, "priceCurrency": "EUR", "url": "https://citedby.eu/plans"} for n, pr in _OFFERS]}]}, ensure_ascii=False).replace("</", "<\\/") + '</script>'


def head(doc, lang, suffix=""):
    """Canonical + hreflang for the five home pages, and a language switch in the footer."""
    base = "https://citedby.eu"
    pth = lambda p: (p + suffix) if (p or suffix) else "/"
    me = next(p for c, _, p in LANG_NAMES if c == lang)
    tags = f'<link rel="canonical" href="{base}{pth(me)}">' + "".join(
        f'<link rel="alternate" hreflang="{c}" href="{base}{pth(p)}">' for c, _, p in LANG_NAMES) + f'<link rel="alternate" hreflang="x-default" href="{base}{pth("")}">'
    tags += LD
    tags += f'<meta property="og:locale" content="{OG_LOCALE[lang]}">'
    doc = doc.replace('<meta name="theme-color" content="#0F1B2D">', '<meta name="theme-color" content="#0F1B2D">' + tags, 1)
    sw = f' · <span class="langsw" role="group" aria-label="{SWITCH_LABEL[lang]}">' + " · ".join(
        f'<a href="{pth(p)}" hreflang="{c}" lang="{c}"' + (' aria-current="true"' if c == lang else "") + f' data-lang="{c}">{n}</a>' for c, n, p in LANG_NAMES) + "</span>"
    return doc.replace("</div></footer>", sw + "</div></footer>", 1)

