"""RES-2935: every HTML page links to the site's hubs from its footer, so no page is an orphan or more than 3 clicks from the home page (the crawl found 98 deep pages and the 5 /guides hubs with no link).
Added at serve time like withdraw_link, so static, generated and app pages all get it, in the page's language. Hubs that exist in one language only (data, tool comparison, our crawler, CI check) link to that page."""
import re

_LANG = re.compile(rb'<html[^>]*\blang="?([a-z]{2})')
MARK = b"data-hub-links"
LOCALES = ("en", "fr", "nl", "de", "es")
LABELS = {  # (guides, blog, tools, audit, changes, findable check)
    "en": ("Guides", "Blog", "Free tools", "AI visibility audit", "What changed", "Findable check"), "fr": ("Guides", "Blog", "Outils gratuits", "Audit de visibilité IA", "Ce qui a changé", "Contrôle de visibilité"),
    "nl": ("Gidsen", "Blog", "Gratis tools", "AI-zichtbaarheidsaudit", "Wat er veranderde", "Vindbaarheidscheck"), "de": ("Ratgeber", "Blog", "Kostenlose Tools", "KI-Sichtbarkeits-Audit", "Was sich geändert hat", "Auffindbarkeits-Check"),
    "es": ("Guías", "Blog", "Herramientas gratis", "Auditoría de visibilidad en IA", "Qué ha cambiado", "Comprobación de visibilidad")}
LOCAL_HUBS = {  # RES-4194: /bots and /platforms now exist in all five languages
    "en": ("AI bots", "Platforms"), "fr": ("Robots IA", "Plateformes"), "nl": ("AI-bots", "Platforms"), "de": ("KI-Bots", "Plattformen"), "es": ("Bots de IA", "Plataformas")}
ENGLISH_ONLY = (("/data", "Data"), ("/compare/profound-vs-peec-vs-otterly", "Tool comparison"), ("/bot", "Our crawler"), ("/ci", "Free CI check"))
ENGLISH_ONLY_LABELS = {  # RES-3013: these links go to English-only pages, so each other language names them in its own words and says "(in English)"
    "fr": ("Données (en anglais)", "Comparatif d'outils (en anglais)", "Notre robot (en anglais)", "Contrôle CI gratuit (en anglais)"),
    "nl": ("Data (in het Engels)", "Toolvergelijking (in het Engels)", "Onze crawler (in het Engels)", "Gratis CI-check (in het Engels)"),
    "de": ("Daten (auf Englisch)", "Tool-Vergleich (auf Englisch)", "Unser Crawler (auf Englisch)", "Kostenloser CI-Check (auf Englisch)"),
    "es": ("Datos (en inglés)", "Comparativa de herramientas (en inglés)", "Nuestro rastreador (en inglés)", "Comprobación CI gratis (en inglés)")}
HOMES = (("en", "/", "English"), ("fr", "/fr", "Français"), ("nl", "/nl", "Nederlands"), ("de", "/de", "Deutsch"), ("es", "/es", "Español"))  # the home pages in each language: the only <a> path to /fr, /nl, /de, /es
_BLOCK = '<p class="hub-links" data-hub-links style="margin:.75rem 0 0;padding:0 16px;text-align:center;font-size:14px">{links}</p>'


def links(lg):
    p = "" if lg == "en" else "/" + lg
    g, b, t, a, c, f = LABELS[lg]
    out = [(f"{p}/guides", g, lg), (f"{p}/blog", b, lg), (f"{p}/tools", t, lg), (f"{p}/ai-visibility-audit", a, lg), (f"{p}/changes", c, lg), (f"{p}/tools/findable-check", f, lg)]
    out += [(f"{p}/bots", LOCAL_HUBS[lg][0], lg), (f"{p}/platforms", LOCAL_HUBS[lg][1], lg)]
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
