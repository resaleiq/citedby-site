"""RES-3725: every HTML page links to CitedBy's live social profile from its footer, in the page's language. Only profiles that exist (products/SOCIAL-ACCOUNTS.md):
X @CitedByEU today; Facebook Page and Instagram get a row here when they exist. The same URL is in the Organization sameAs (trust.SAME_AS). Added at serve time like hub_links."""
import re

_LANG = re.compile(rb'<html[^>]*\blang="?([a-z]{2})')
MARK = b"data-follow-links"
LOCALES = ("en", "fr", "nl", "de", "es")
PROFILES = (("x", "https://x.com/CitedByEU", {"en": "Follow CitedBy on X", "fr": "Suivre CitedBy sur X", "nl": "Volg CitedBy op X", "de": "CitedBy auf X folgen", "es": "Seguir a CitedBy en X"}),)
_BLOCK = '<p class="follow-links" data-follow-links style="margin:.75rem 0 0;padding:0 16px;text-align:center;font-size:14px">{links}</p>'


def inject(body):
    """Add the profile links inside the page's last <footer> (before </footer>), else before </body>; fragments and pages that already have them pass through."""
    if MARK in body or b"<html" not in body[:600].lower():
        return body
    m = _LANG.search(body[:600]); lg = m.group(1).decode() if m and m.group(1).decode() in LOCALES else "en"
    html = " · ".join(f'<a href="{u}" rel="me noopener" target="_blank" style="display:inline-block;padding:10px 4px;color:inherit;text-decoration:underline;text-underline-offset:3px">{l[lg]}</a>' for _, u, l in PROFILES)
    block = _BLOCK.format(links=html).encode()
    i = body.rfind(b"</footer>")
    if i >= 0:
        return body[:i] + block + body[i:]
    j = body.rfind(b"</body>")
    return body[:j] + block + body[j:] if j >= 0 else body + block
