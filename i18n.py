"""Language routes, canonical + hreflang and the footer language switch for the five home pages (RES-1731 row 10)."""

LANDING_PATHS = {"/fr": "fr", "/nl": "nl", "/de": "de", "/es": "es"}
LANG_NAMES = (("en", "English", ""), ("fr", "Français", "/fr"), ("nl", "Nederlands", "/nl"), ("de", "Deutsch", "/de"), ("es", "Español", "/es"))
SWITCH_LABEL = {"en": "Language", "fr": "Langue", "nl": "Taal", "de": "Sprache", "es": "Idioma"}
OG_LOCALE = {"en": "en_GB", "fr": "fr_FR", "nl": "nl_NL", "de": "de_DE", "es": "es_ES"}


def head(doc, lang, suffix=""):
    """Canonical + hreflang for the five home pages, and a language switch in the footer."""
    base = "https://citedby.eu"
    pth = lambda p: (p + suffix) if (p or suffix) else "/"
    me = next(p for c, _, p in LANG_NAMES if c == lang)
    tags = f'<link rel="canonical" href="{base}{pth(me)}">' + "".join(
        f'<link rel="alternate" hreflang="{c}" href="{base}{pth(p)}">' for c, _, p in LANG_NAMES) + f'<link rel="alternate" hreflang="x-default" href="{base}{pth("")}">'
    tags += f'<meta property="og:locale" content="{OG_LOCALE[lang]}">'
    doc = doc.replace('<meta name="theme-color" content="#0F1B2D">', '<meta name="theme-color" content="#0F1B2D">' + tags, 1)
    sw = f' · <span class="langsw" role="group" aria-label="{SWITCH_LABEL[lang]}">' + " · ".join(
        f'<a href="{pth(p)}" hreflang="{c}" lang="{c}"' + (' aria-current="true"' if c == lang else "") + f' data-lang="{c}">{n}</a>' for c, n, p in LANG_NAMES) + "</span>"
    return doc.replace("</div></footer>", sw + "</div></footer>", 1)

