"""RES-2182: the EU withdrawal link (Directive (EU) 2023/2673, Art. 11a). Every HTML page we serve carries "Withdraw from contract here" next to its footer,
in the page's own language, always visible. Added at serve time so no page (static, generated or proxied from the app) can miss it."""
import re

LABELS = {"en": "Withdraw from contract here", "fr": "Renoncer au contrat ici", "de": "Vertrag widerrufen", "nl": "Hier de overeenkomst herroepen", "es": "Desistir del contrato aquí"}
_LANG = re.compile(rb'<html[^>]*\blang="?([a-z]{2})')
MARK = b'data-withdraw'
_BLOCK = '<p class="wd-link" style="margin:.75rem 0 0;padding:0 16px;text-align:center;font-size:14px"><a data-withdraw href="{href}" style="color:inherit;text-decoration:underline;text-underline-offset:3px">{label}</a></p>'


def inject(body, path=""):  # path kept for callers
    """Add the link inside the page's last <footer> (before </footer>), else before </body>; fragments and pages that already have it pass through."""
    if MARK in body or b"<html" not in body[:600].lower():
        return body
    m = _LANG.search(body[:600]); lg = m.group(1).decode() if m and m.group(1).decode() in LABELS else "en"
    block = _BLOCK.format(href="/withdraw" if lg == "en" else f"/{lg}/withdraw", label=LABELS[lg]).encode()
    i = body.rfind(b"</footer>")
    if i >= 0:
        return body[:i] + block + body[i:]
    j = body.rfind(b"</body>")
    return body[:j] + block + body[j:] if j >= 0 else body + block
