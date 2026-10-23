"""RES-3683 trust layer: every fact page (/data, the free tools) shows where its facts come from, when they were checked, how we count and where changes are logged,
and its JSON-LD names CitedBy's accounts (sameAs) and a dateModified. Added at serve time like hub_links, so static, generated and app pages all get it.
The dates are real: a data page's own dateModified (the day its answers were collected); a tool's date is the newest `read_on` in the change ledger (the day someone re-read the engine docs)."""
import json, os, re

SAME_AS = ["https://citedby.eu/about", "https://citedby.eu/methodology", "https://x.com/CitedByEU"]
MARK = b"data-trust"
LOCALES = ("en", "fr", "nl", "de", "es")
_PATH = re.compile(r"^/(?:(fr|nl|de|es)/)?(data|tools|bots|platforms)(?:/([a-z0-9-]+))?/?$")
TOOLS = ("ai-crawler-check", "llms-txt-checker", "findable-check")
RFC9309 = ("https://www.rfc-editor.org/rfc/rfc9309", "RFC 9309 (robots.txt)")
SOURCES = {  # slug -> [(url, label)] outside pages that are the authority for what the page counts
    "launch-crawl-2026-10": [RFC9309],
    "study-chatgpt-buyer-questions": [("https://help.openai.com/en/articles/9237897-chatgpt-search", "ChatGPT search help page")],
    "study-buyer-questions-claude": [("https://support.claude.com/en/articles/10684626-enabling-and-using-web-search", "Claude web search help page")],
    "ai-crawler-check": [RFC9309],
    "llms-txt-checker": [("https://llmstxt.org/", "llmstxt.org proposal"), ("https://www.sitemaps.org/protocol.html", "sitemaps.org protocol")],
    "findable-check": [RFC9309, ("https://www.sitemaps.org/protocol.html", "sitemaps.org protocol")],
    "tools": [RFC9309, ("https://llmstxt.org/", "llmstxt.org proposal")],
}
L = {  # checked-on, source, shops, method, log, csv, months
    "en": ("Checked on", "Source", "Sites counted", "Method", "Change log", "Data (CSV)", ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")),
    "fr": ("Vérifié le", "Source", "Sites comptés", "Méthode", "Journal des changements", "Données (CSV)", ("janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc.")),
    "nl": ("Gecontroleerd op", "Bron", "Getelde sites", "Methode", "Wijzigingslogboek", "Gegevens (CSV)", ("jan.", "feb.", "mrt.", "apr.", "mei", "jun.", "jul.", "aug.", "sep.", "okt.", "nov.", "dec.")),
    "de": ("Geprüft am", "Quelle", "Gezählte Seiten", "Methode", "Änderungsprotokoll", "Daten (CSV)", ("Jan.", "Feb.", "März", "Apr.", "Mai", "Juni", "Juli", "Aug.", "Sept.", "Okt.", "Nov.", "Dez.")),
    "es": ("Comprobado el", "Fuente", "Sitios contados", "Método", "Registro de cambios", "Datos (CSV)", ("ene.", "feb.", "mar.", "abr.", "may.", "jun.", "jul.", "ago.", "sept.", "oct.", "nov.", "dic.")),
}
METHOD_TXT = {"en": "How CitedBy checks", "fr": "Comment CitedBy vérifie", "nl": "Hoe CitedBy controleert", "de": "So prüft CitedBy", "es": "Cómo comprueba CitedBy"}
LOG_TXT = {"en": "What changed", "fr": "Ce qui a changé", "nl": "Wat er veranderde", "de": "Was sich geändert hat", "es": "Qué ha cambiado"}
_LANG = re.compile(rb'<html[^>]*\blang="?([a-z]{2})')
_DM = re.compile(rb'"dateModified": ?"(\d{4}-\d\d-\d\d)"')
_SHOP = re.compile(r"<b>((?:[a-z0-9-]+\.)+[a-z]{2,})</b>")
_LD = re.compile(rb'(<script type="application/ld\+json">)(.*?)(</script>)', re.S)
_HERE = os.path.dirname(os.path.abspath(__file__))
_LEDGER = os.path.join(_HERE, "data", "engine-changes.json")


def ledger_date():
    try:
        return max(r["read_on"] for r in json.load(open(_LEDGER, encoding="utf-8")) if r.get("read_on"))
    except (OSError, ValueError, KeyError):
        return ""


def _fmt(iso, lg):
    y, m, d = iso.split("-")
    mo = L[lg][6][int(m) - 1]
    return f"{int(d)} {mo} {y}" if lg != "de" else f"{int(d)}. {mo} {y}"


def _walk(o, fn):
    if isinstance(o, dict):
        fn(o)
        for v in o.values(): _walk(v, fn)
    elif isinstance(o, list):
        for v in o: _walk(v, fn)


def _is_org(n):
    return n.get("@type") == "Organization" and n.get("name") == "CitedBy"


def _patch_ld(body, date):
    """sameAs on every CitedBy Organization node; dateModified on a WebPage that has none. An Organization node is added when the page has none."""
    seen = {"org": False}
    def one(m):
        try: data = json.loads(m.group(2))
        except ValueError: return m.group(0)
        def fix(n):
            if _is_org(n):
                seen["org"] = True
                n["sameAs"] = list(dict.fromkeys(list(n.get("sameAs", [])) + SAME_AS))
            if n.get("@type") in ("WebPage", "CollectionPage") and date and "dateModified" not in n: n["dateModified"] = date
        _walk(data, fix)
        return m.group(1) + json.dumps(data, ensure_ascii=False).encode() + m.group(3)
    out = _LD.sub(one, body)
    if not seen["org"]:
        org = {"@context": "https://schema.org", "@type": "Organization", "@id": "https://citedby.eu/#org", "name": "CitedBy", "url": "https://citedby.eu", "sameAs": SAME_AS}
        tag = b'<script type="application/ld+json">' + json.dumps(org).encode() + b"</script>"
        i = out.find(b"</head>")
        out = out[:i] + tag + out[i:] if i >= 0 else out
    return out


def inject(body, path):
    m = _PATH.match(path.split("?")[0])
    if not m or MARK in body or b"<html" not in body[:600].lower():
        return body
    lg0, kind, slug = m.groups()
    if kind in ("bots", "platforms"):  # these pages carry their own source, date, method and log; they only lack the entity links
        return _patch_ld(body, "")
    if b"</main>" not in body: return body
    if kind == "tools" and slug and slug not in TOOLS: return body
    lm = _LANG.search(body[:600]); lg = lm.group(1).decode() if lm and lm.group(1).decode() in LOCALES else "en"
    src_key = slug or ("tools" if kind == "tools" else None)
    t = L[lg]; p = "" if lg == "en" else "/" + lg
    if kind == "tools":
        date = ledger_date()
        label = {"en": "Engine rules last checked on"}.get(lg, t[0])
        date_html = f'{label} {_fmt(date, lg)} (<a href="{p}/changes">{t[4]}</a>)' if date else ""
    else:
        ds = [d.decode() for d in _DM.findall(body)]
        if not slug:  # the index: newest of its datasets
            d = os.path.join(_HERE, "public", "data")
            ds = [x.decode() for f in os.listdir(d) if f.endswith(".html") for x in _DM.findall(open(os.path.join(d, f), "rb").read())] if os.path.isdir(d) else []
        date = max(ds) if ds else ""
        date_html = f"{t[0]} {_fmt(date, lg)}" if date else ""
    items = []
    if date_html: items.append(date_html)
    srcs = [f'<a href="{u}" rel="noopener">{lb}</a>' for u, lb in SOURCES.get(src_key, [])]
    if kind == "data" and slug:
        shops = list(dict.fromkeys(_SHOP.findall(body.decode("utf-8", "ignore"))))[:3]
        srcs += [f'<a href="https://{s}" rel="noopener nofollow">{s}</a>' for s in shops]
        if os.path.exists(os.path.join(_HERE, "public", "data", slug + ".csv")):
            srcs.insert(0, f'<a href="/data/{slug}.csv">{t[5]}</a>')
    if srcs: items.append(f'{t[1]}: ' + " · ".join(srcs))
    items.append(f'{t[3]}: <a href="/methodology">{METHOD_TXT[lg]}</a>')
    if kind == "data": items.append(f'{t[4]}: <a href="{p}/changes">{LOG_TXT[lg]}</a>')
    block = ('<p class="src trust" data-trust style="margin:2rem auto 1rem;max-width:72ch;padding:0 16px;font-size:14px">' + " · ".join(items) + "</p>").encode()
    i = body.rfind(b"</main>")
    return _patch_ld(body[:i] + block + body[i:], date)
