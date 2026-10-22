"""Language routes, canonical + hreflang and the footer language switch for the five home pages (RES-1731 row 10)."""
import json

LANDING_PATHS = {"/fr": "fr", "/nl": "nl", "/de": "de", "/es": "es"}
LANG_NAMES = (("en", "English", ""), ("fr", "Français", "/fr"), ("nl", "Nederlands", "/nl"), ("de", "Deutsch", "/de"), ("es", "Español", "/es"))
SWITCH_LABEL = {"en": "Language", "fr": "Langue", "nl": "Taal", "de": "Sprache", "es": "Idioma"}
OG_LOCALE = {"en": "en_GB", "fr": "fr_FR", "nl": "nl_NL", "de": "de_DE", "es": "es_ES"}


SAME_AS = ["https://citedby.eu/about", "https://citedby.eu/methodology"]
# Service, not Product: Google reads Product as a merchant listing and rejects it without image and availability (RES-2651, Search Console 21 Oct).
_LD_WORDS = {  # offer names and descriptions in the page's language; the plan names are brand names (RES-2895)
    "en": ("Single audit", "monthly", "Website audit", "Crawls a website up to your plan's page limit and gives the exact fix for each issue."),
    "fr": ("Audit unique", "mensuel", "Audit de site web", "Explore un site web jusqu'à la limite de pages de votre offre et donne la correction exacte de chaque problème."),
    "nl": ("Eenmalige audit", "maandelijks", "Website-audit", "Crawlt een website tot de paginalimiet van je abonnement en geeft de exacte fix voor elk probleem."),
    "de": ("Einzelaudit", "monatlich", "Website-Audit", "Crawlt eine Website bis zum Seitenlimit Ihres Tarifs und liefert für jedes Problem die genaue Korrektur."),
    "es": ("Auditoría única", "mensual", "Auditoría web", "Rastrea una web hasta el límite de páginas de tu plan y da la corrección exacta de cada problema."),
}


def ld(lang="en"):
    single, monthly, stype, desc = _LD_WORDS[lang]
    offers = [(single, "9"), (f"Starter ({monthly})", "19"), (f"Pro ({monthly})", "49"), (f"Agency ({monthly})", "99")]
    plans = "https://citedby.eu/plans" if lang == "en" else f"https://citedby.eu/{lang}/plans"
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": [
        {"@type": "Organization", "@id": "https://citedby.eu/#org", "name": "CitedBy", "url": "https://citedby.eu/", "logo": "https://citedby.eu/icon-192.png", "email": "hello@citedby.eu", "sameAs": SAME_AS},
        {"@type": "Service", "name": "CitedBy website audit" if lang == "en" else f"CitedBy {stype}", "serviceType": stype, "provider": {"@id": "https://citedby.eu/#org"}, "areaServed": "Worldwide", "url": "https://citedby.eu/" if lang == "en" else f"https://citedby.eu/{lang}",
         "description": desc,
         "offers": [{"@type": "Offer", "name": n, "price": pr, "priceCurrency": "EUR", "url": plans} for n, pr in offers]}]}, ensure_ascii=False).replace("</", "<\\/") + '</script>'


LD = ld("en")


def head(doc, lang, suffix=""):
    """Canonical + hreflang for the five home pages, and a language switch in the footer."""
    base = "https://citedby.eu"
    pth = lambda p: (p + suffix) if (p or suffix) else "/"
    me = next(p for c, _, p in LANG_NAMES if c == lang)
    tags = f'<link rel="canonical" href="{base}{pth(me)}">' + "".join(
        f'<link rel="alternate" hreflang="{c}" href="{base}{pth(p)}">' for c, _, p in LANG_NAMES) + f'<link rel="alternate" hreflang="x-default" href="{base}{pth("")}">'
    tags += ld(lang)
    tags += f'<meta property="og:locale" content="{OG_LOCALE[lang]}">'
    doc = doc.replace('<meta name="theme-color" content="#0F1B2D">', '<meta name="theme-color" content="#0F1B2D">' + tags, 1)
    sw = f' · <span class="langsw" role="group" aria-label="{SWITCH_LABEL[lang]}">' + " · ".join(
        f'<a href="{pth(p)}" hreflang="{c}" lang="{c}"' + (' aria-current="true"' if c == lang else "") + f' data-lang="{c}">{n}</a>' for c, n, p in LANG_NAMES) + "</span>"
    return doc.replace("</div></footer>", sw + "</div></footer>", 1)

