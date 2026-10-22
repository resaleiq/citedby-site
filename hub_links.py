"""RES-2935: every HTML page links to the site's hubs from its footer, so no page is an orphan or more than 3 clicks from the home page (the crawl found 98 deep pages and the 5 /guides hubs with no link).
Added at serve time like withdraw_link, so static, generated and app pages all get it, in the page's language. Hubs that exist in one language only (bots, platforms, data) link to that page."""
import re

_LANG = re.compile(rb'<html[^>]*\blang="?([a-z]{2})')
MARK = b"data-hub-links"
LOCALES = ("en", "fr", "nl", "de", "es")
LABELS = {  # (guides, blog, tools, audit)
    "en": ("Guides", "Blog", "Free tools", "AI visibility audit"), "fr": ("Guides", "Blog", "Outils gratuits", "Audit de visibilité IA"),
    "nl": ("Gidsen", "Blog", "Gratis tools", "AI-zichtbaarheidsaudit"), "de": ("Ratgeber", "Blog", "Kostenlose Tools", "KI-Sichtbarkeits-Audit"),
    "es": ("Guías", "Blog", "Herramientas gratis", "Auditoría de visibilidad en IA")}
ENGLISH_ONLY = (("/bots", "AI bots"), ("/platforms", "Platforms"), ("/data", "Data"), ("/compare/profound-vs-peec-vs-otterly", "Tool comparison"), ("/bot", "Our crawler"))
ENGLISH_ONLY_LABELS = {  # RES-3013: the five links go to English-only pages, so each other language names them in its own words and says "(in English)"
    "fr": ("Robots IA (en anglais)", "Plateformes (en anglais)", "Données (en anglais)", "Comparatif d'outils (en anglais)", "Notre robot (en anglais)"),
    "nl": ("AI-bots (in het Engels)", "Platforms (in het Engels)", "Data (in het Engels)", "Toolvergelijking (in het Engels)", "Onze crawler (in het Engels)"),
    "de": ("KI-Bots (auf Englisch)", "Plattformen (auf Englisch)", "Daten (auf Englisch)", "Tool-Vergleich (auf Englisch)", "Unser Crawler (auf Englisch)"),
    "es": ("Bots de IA (en inglés)", "Plataformas (en inglés)", "Datos (en inglés)", "Comparativa de herramientas (en inglés)", "Nuestro rastreador (en inglés)")}
HOMES = (("en", "/", "English"), ("fr", "/fr", "Français"), ("nl", "/nl", "Nederlands"), ("de", "/de", "Deutsch"), ("es", "/es", "Español"))  # the home pages in each language: the only <a> path to /fr, /nl, /de, /es
_BLOCK = '<p class="hub-links" data-hub-links style="margin:.75rem 0 0;padding:0 16px;text-align:center;font-size:14px">{links}</p>'


def links(lg):
    p = "" if lg == "en" else "/" + lg
    g, b, t, a = LABELS[lg]
    out = [(f"{p}/guides", g, lg), (f"{p}/blog", b, lg), (f"{p}/tools", t, lg), (f"{p}/ai-visibility-audit", a, lg)]
    out += [(h, ENGLISH_ONLY_LABELS[lg][i] if lg in ENGLISH_ONLY_LABELS else l, "en") for i, (h, l) in enumerate(ENGLISH_ONLY)]
    return out


def inject(body):
    """Add the hub links inside the page's last <footer> (before </footer>), else before </body>; fragments and pages that already have them pass through."""
    if MARK in body or b"<html" not in body[:600].lower():
        return body
    m = _LANG.search(body[:600]); lg = m.group(1).decode() if m and m.group(1).decode() in LOCALES else "en"
    html = " · ".join(f'<a href="{h}" style="color:inherit;text-decoration:underline;text-underline-offset:3px"' + ("" if hl == lg else f' hreflang="{hl}" lang="{hl}"') + f">{l}</a>" for h, l, hl in links(lg))
    langs = " · ".join(f'<a href="{h}" hreflang="{c}" lang="{c}" style="color:inherit;text-decoration:underline;text-underline-offset:3px">{n}</a>' for c, h, n in HOMES if c != lg)
    block = (_BLOCK.format(links=html) + _BLOCK.format(links=langs).replace(" data-hub-links", "")).encode()
    i = body.rfind(b"</footer>")
    if i >= 0:
        return body[:i] + block + body[i:]
    j = body.rfind(b"</body>")
    return body[:j] + block + body[j:] if j >= 0 else body + block
