"""Insert JSON-LD into static pages that lack it (RES-1280). Idempotent. Usage: python3 tools/add_jsonld.py"""
import html, json, os, re
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "public")
ORG = {"@type": "Organization", "@id": "https://citedby.eu/#org", "name": "CitedBy", "url": "https://citedby.eu"}
PAGES = {  # file -> (path, @type, lang)
    "check.html": ("/check", "WebApplication", "en"), "fr/check.html": ("/fr/check", "WebApplication", "fr"),
    "nl/check.html": ("/nl/check", "WebApplication", "nl"), "sample-audit.html": ("/sample-audit", "WebPage", "en"),
    "terms.html": ("/terms", "WebPage", "en"), "refund.html": ("/refund", "WebPage", "en"),
    "contact.html": ("/contact", "ContactPage", "en"), "legal.html": ("/legal", "WebPage", "en"),
    "privacy.html": ("/privacy", "WebPage", "en"),
}
def one(f, path, typ, lang):
    p = os.path.join(ROOT, f); s = open(p, encoding="utf-8").read()
    if "application/ld+json" in s: return False
    name = html.unescape(re.search(r"<title>(.*?)</title>", s, re.S).group(1)).strip()
    m = re.search(r'<meta name="description" content="(.*?)"', s)
    d = {"@context": "https://schema.org", "@type": typ, "name": name, "url": "https://citedby.eu" + path, "inLanguage": lang, "publisher": ORG}
    if m: d["description"] = html.unescape(m.group(1))
    if typ == "WebApplication":
        d.update(applicationCategory="BusinessApplication", operatingSystem="Web", offers={"@type": "Offer", "price": "0", "priceCurrency": "EUR"})
    d["isPartOf"] = {"@type": "WebSite", "name": "CitedBy", "url": "https://citedby.eu"}
    tag = '<script type="application/ld+json">%s</script>' % json.dumps(d, ensure_ascii=False).replace("</", "<\\/")
    s = s.replace("</head>", tag + "</head>", 1)
    open(p, "w", encoding="utf-8").write(s); return True
if __name__ == "__main__":
    for f, a in PAGES.items(): print(f, one(f, *a))
