"""Forward the CitedBy app's paths to the app container (RES-661 production cutover).
Off unless APP_UPSTREAM is set (for example http://citedby-app:8080); unsetting it is the rollback.
Only the paths in ROUTES are forwarded; the client IP is sent as one X-Forwarded-For value."""
import json, os, re, time, urllib.error, urllib.request
import analytics
from urllib.parse import urlparse

UPSTREAM = os.environ.get("APP_UPSTREAM", "").rstrip("/")
ROUTES = {
    "GET": re.compile(r"/((fr|nl)/instant|(fr|nl|de|es)/(plans|sample)|instant|plans|thanks|dashboard|account|report/[A-Za-z0-9_-]{20,64}|r/[A-Za-z0-9_-]{16,64}(\.csv)?|start/[A-Za-z0-9_-]{20,64}|api/account/export|api/guess|api/grade|ci|ci/ai-crawler-check\.sh|grade|api/snapshot/(\d+|[A-Za-z0-9_-]{16,64})|signin|login|signup|forgot|logout|auth/google(/callback)?|reset/[A-Za-z0-9_-]{20,64}|t/t_[A-Za-z0-9]{10,16}|api/teaser/(token|t_[A-Za-z0-9]{10,16})|app\.html|saas\.css|saas\.js|sample\.js|landing\.js|audit|sample|api/me|api/projects|api/audits(/[A-Za-z0-9_]{3,40}(/(pages|page))?)?|app/[a-z0-9]+\.(js|css)|api/usage|api/account|api/brand|api/team|api/audit/[A-Za-z0-9_]{3,40}(/(pages|page|pdf|compare|access|export|priorities|insights|structure|performance|duplicates|security|issue/[a-z0-9_]{2,60}))?|api/site|api/share/[A-Za-z0-9_]{3,40}|r/audit/[A-Za-z0-9_]{3,40}|login/[A-Za-z0-9_-]{20,64}|trial/cancel/[A-Za-z0-9_.-]{20,100}|recount/[A-Za-z0-9_-]{20,64}|api/crawl/[A-Za-z0-9_-]{1,64})"),
    "POST": re.compile(r"/(api/teaser|api/crawl|api/audits|api/audit|api/audit/[A-Za-z0-9_]{3,40}/recrawl|api/snapshot|api/stripe/webhook|api/fixpack/intake|api/account/(link|delete|signout-all)|api/brand(/domain-check)?|api/team(/(leave|remove))?|api/share/[A-Za-z0-9_]{3,40}/unlock|api/projects/[A-Za-z0-9._-]{1,80}(/[a-z]{3,12})?|api/audit/[A-Za-z0-9_]{3,40}/(share|schedule|recheck)|api/auth/(signup|login|forgot|reset)|api/portal|api/checkout|login/[A-Za-z0-9_-]{20,64}|trial/cancel/[A-Za-z0-9_.-]{20,100})"),
}
INDEXABLE = re.compile(r"/((fr|nl|de|es)/)?(plans|sample)")  # pricing and the sample report in every language are meant to be found (RES-1731); the rest of the app stays noindex
PASS = ("Content-Type", "Cache-Control", "Set-Cookie", "Location", "Referrer-Policy", "Content-Security-Policy")
_H = {"t": 0.0, "u": "", "v": None}


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k): return None

_opener = urllib.request.build_opener(_NoRedirect)


def _call(req, timeout):
    try:
        r = _opener.open(req, timeout=timeout)
    except urllib.error.HTTPError as e:
        r = e
    return r.status if hasattr(r, "status") else r.code, r.headers, r.read()


def handle(h, method):
    """True if the request was an app path (and was answered here)."""
    u = urlparse(h.path)
    if not UPSTREAM or not ROUTES[method].fullmatch(u.path):
        return False
    body = None
    if method == "POST":
        try: n = int(h.headers.get("Content-Length") or 0)
        except ValueError: n = -1
        if n < 0 or n > 65536:
            _send(h, 413, {}, b'{"error":"too large"}'); return True
        body = h.rfile.read(n) if n else b""
    hdr = {"X-Forwarded-For": h.ip()}
    for k in ("Content-Type", "Cookie", "Stripe-Signature", "Accept", "X-CitedBy-QA"):  # X-CitedBy-QA: the app skips the per-network teaser caps for a request with the QA token (RES-1785); # Accept: the app serves /account as HTML only when it contains text/html (RES-1595)
        if h.headers.get(k): hdr[k] = h.headers[k]
    try:
        code, rh, rb = _call(urllib.request.Request(UPSTREAM + h.path, body, hdr, method=method), 20)
    except (urllib.error.URLError, OSError, ValueError):
        _send(h, 502, {}, b'{"error":"app unavailable"}'); return True
    _send(h, code, {k: rh[k] for k in PASS if rh.get(k)}, rb, rh.get_all("Set-Cookie"), index_ok=bool(INDEXABLE.fullmatch(u.path)) and code == 200 and method == "GET")
    return True


def _send(h, code, headers, body, cookies=None, index_ok=False):
    if code == 200 and headers.get("Content-Type", "").startswith("text/html"):
        body = analytics.inject(body)  # RES-1071: cookieless analytics tag on the app pages too
    h.send_response(code)
    headers.setdefault("Content-Type", "application/json")
    headers.setdefault("Cache-Control", "no-store")
    headers.pop("Set-Cookie", None)
    for k, v in headers.items(): h.send_header(k, v)
    for c in cookies or []: h.send_header("Set-Cookie", c)
    if not index_ok: h.send_header("X-Robots-Tag", "noindex")
    h.send_header("X-Content-Type-Options", "nosniff")
    h.send_header("Strict-Transport-Security", "max-age=31536000")
    h.send_header("Content-Length", str(len(body)))
    h.end_headers()
    if h.command != "HEAD": h.wfile.write(body)


def app_health():
    """None when the proxy is off, else {"status","deploy"} from the app's /health (cached 10 s, 2 s timeout)."""
    if not UPSTREAM: return None
    now = time.time()
    if _H["u"] == UPSTREAM and now - _H["t"] < 10: return _H["v"]
    try:
        code, _, b = _call(urllib.request.Request(UPSTREAM + "/health"), 2)
        j = json.loads(b)
        v = {"status": "ok" if code == 200 and j.get("ok") else "error", "deploy": j.get("deploy")}
    except (urllib.error.URLError, OSError, ValueError):
        v = {"status": "error", "deploy": None}
    _H.update(t=now, u=UPSTREAM, v=v)
    return v
