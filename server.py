"""CitedBy: static site plus the free check. Standard library only.

Routes: GET static pages (clean URLs), POST /api/check, POST /api/request (410, retired), GET|POST /api/confirm and /api/unsubscribe (410, retired),
POST /api/event, GET /healthz, GET /health (status + db read, 503 on failure), GET /deploy-id (commit from the build). Data: one SQLite file under DATA_DIR. No cookies. Events are anonymous counters.
"""
import base64, hashlib, hmac, html, json, mimetypes, os, re, sqlite3, threading, time, urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

import analytics, backlinks, mcp, doorcheck, follow_link, home, hub_links, langroutes, legal_links, pages, proxy, safefetch, social, trust, withdraw_link

HERE = os.path.dirname(os.path.abspath(__file__))
SECRET = os.environ["OPTIN_SECRET"].encode()  # crash if missing (fail-secure)
if len(SECRET) < 32:
    raise SystemExit("OPTIN_SECRET must be at least 32 bytes")
BASE_URL = os.environ["BASE_URL"].rstrip("/")
DATA_DIR = os.environ.get("DATA_DIR", "/data")
SITE_DIR = os.environ.get("SITE_DIR", os.path.join(HERE, "public"))
CHECK_PER_IP = int(os.environ.get("CHECK_PER_IP_HOUR", "10"))
CHECK_PER_HOST = int(os.environ.get("CHECK_PER_HOST_HOUR", "4"))
DAILY_CAP = int(os.environ.get("DAILY_CAP", "20"))
INTERNAL_IPS = {x.split("#")[0].strip() for k in ("INTERNAL_CLIENT_IPS", "INTERNAL_IPS") for x in os.environ.get(k, "").split(",")} - {""}  # RES-2134: one own-traffic list (INTERNAL_CLIENT_IPS, same value in every container); the old name still works
LANGS = ("en", "fr", "nl")
CHECK_LANGS = LANGS + ("de", "es")  # RES-3935: the check is asked for in these (Accept-Language) and its events counted; mail text exists only for LANGS
COUNTRIES = ("BE", "FR", "NL", "IE", "DE", "ES", "GB", "OTHER")
NICHES = ("coffee", "tea", "beauty", "mattress", "supplements", "other")
def _deploy_id():  # commit sha from the image build (Dockerfile ARG GIT_SHA); env wins, then the baked file
    v = os.environ.get("DEPLOY_ID", "").strip()
    if not v:
        try: v = open(os.path.join(HERE, "DEPLOY_ID")).read().strip()
        except OSError: v = ""
    return v or "unknown"
DEPLOY_ID = _deploy_id()
SNAPSHOTS = json.load(open(os.path.join(HERE, "data", "snapshots.json")))
CHECK_SOURCES = {"wp-plugin": "free_check_started_wp_plugin", "cli": "free_check_started_cli", "action": "free_check_started_action"}  # who sent a free check: RES-3708 plugin, RES-3749 CLI and GitHub Action
EVENTS = ("check_start", "check_complete", "email_submitted", "fixpack_click", "first_screen_cta_click", "free_tool_start", "offer_view") + tuple(CHECK_SOURCES.values())

os.makedirs(DATA_DIR, exist_ok=True)
DB_PATH = os.path.join(DATA_DIR, "check.db")
_db = sqlite3.connect(DB_PATH, check_same_thread=False)
_db.execute("PRAGMA journal_mode=WAL")
_db.execute("""CREATE TABLE IF NOT EXISTS event_count(
  day TEXT NOT NULL, lang TEXT NOT NULL, type TEXT NOT NULL, n INTEGER NOT NULL DEFAULT 0, PRIMARY KEY(day,lang,type))""")
_db.commit()
_lock = threading.Lock()
_slots = threading.BoundedSemaphore(4)  # concurrent outbound checks
_hits = {}

def retire_mini_audit():
    """RES-3940 F3: the email mini-audit form (check.html, POST /api/request) is retired and /privacy never listed its data. Drop what it stored (address, site, country, niche, consent version; the 24-hour send log) and compact the file so the rows do not linger in free pages or the WAL."""
    with _lock:
        n = sum(_db.execute(f"SELECT count(*) FROM {t}").fetchone()[0] for t in ("request", "mail_log") if _db.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (t,)).fetchone())
        _db.execute("DROP TABLE IF EXISTS request"); _db.execute("DROP TABLE IF EXISTS mail_log"); _db.commit()
        _db.execute("PRAGMA wal_checkpoint(TRUNCATE)"); _db.execute("VACUUM")
    print("mini-audit retired: removed", n, "rows", flush=True)


def count_event(etype, lang, ip=""):
    if etype not in EVENTS or lang not in CHECK_LANGS or ip in INTERNAL_IPS:
        return
    day = time.strftime("%Y-%m-%d", time.gmtime())
    with _lock:
        for t in (etype,) + (("free_tool_start",) if etype == "check_start" else ()):  # free_tool_start: the server accepted the first free request (RES-2134)
            _db.execute("INSERT INTO event_count(day,lang,type,n) VALUES(?,?,?,1) ON CONFLICT(day,lang,type) DO UPDATE SET n=n+1", (day, lang, t))
        _db.commit()


def limited(key, limit):
    """True if key has used up its hourly allowance (and records the hit otherwise)."""
    now = time.time()
    with _lock:
        h = [t for t in _hits.get(key, []) if now - t < 3600]
        if len(h) >= limit:
            _hits[key] = h
            return True
        h.append(now)
        _hits[key] = h
        if len(_hits) > 5000:
            for k in [k for k, v in _hits.items() if not v or now - v[-1] > 3600]:
                del _hits[k]
    return False


def snapshot(country, lang, niche):
    s = SNAPSHOTS.get(f"{country}|{lang}|{niche}")
    other = False
    if not s:
        for k, v in SNAPSHOTS.items():
            c, _, n = k.split("|")
            if c == country and n == niche:
                s, other = v, k.split("|")[1]
                break
    if not s or not s["top"]:
        return None
    return {**s, "country": country, "niche": niche, "other_language": other}


def handle_check(data, ip):
    """Returns (http_status, body_dict)."""
    lang = data.get("lang") if data.get("lang") in CHECK_LANGS else "en"
    country = data.get("country") if data.get("country") in COUNTRIES else "OTHER"
    niche = data.get("niche") if data.get("niche") in NICHES else "other"
    try:
        root = doorcheck.normalize(str(data.get("url", "")))
    except safefetch.Blocked:
        return 400, {"ok": False, "error": "bad_url"}
    if limited("ip:" + ip, CHECK_PER_IP) or limited("host:" + root, CHECK_PER_HOST):
        return 429, {"ok": False, "error": "rate_limited"}
    if not _slots.acquire(timeout=5):
        return 503, {"ok": False, "error": "busy"}
    try:
        count_event("check_start", lang, ip)
        src = data.get("source")
        if isinstance(src, str) and src in CHECK_SOURCES:  # the WordPress plugin, the CLI and the GitHub Action tag their checks (RES-3708, RES-3749): counted per source, nothing else stored
            count_event(CHECK_SOURCES[src], lang, ip)
        try:
            res = doorcheck.run(root, lang)
        except safefetch.Blocked:
            return 400, {"ok": False, "error": "bad_url"}
    finally:
        _slots.release()
    if res.get("reachable"):
        count_event("check_complete", lang, ip)
    res["ok"] = True
    res["snapshot"] = None  # ChatGPT-app snapshots retired (RES-852)
    return 200, res


GONE_TXT = "This request form was closed and its data deleted; nothing more will be sent. / Ce formulaire est fermé et ses données sont supprimées ; rien d'autre ne sera envoyé. / Dit formulier is gesloten en de gegevens zijn gewist; er wordt niets meer verstuurd."


def asset_ver(name):
    with open(os.path.join(HERE, "public", name), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:8]


def not_found_page():
    """RES-1785: a 404 that leads somewhere (was a bare "Not found")."""
    sv, cv = asset_ver("style.css"), asset_ver("check.css")
    return (f'<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="robots" content="noindex"><title>Page not found | CitedBy</title><link rel="stylesheet" href="/style.css?v={sv}"><link rel="stylesheet" href="/check.css?v={cv}">'
            '<body><main class="doc"><p><b>Error 404</b></p><h1>We could not find that page</h1>'
            '<p>The address may be mistyped, or the page has moved. These pages exist:</p>'
            '<ul><li><a href="/">Check your site free</a>: score and the 3 issues to fix first</li>'
            '<li><a href="/sample">See a full sample report</a></li><li><a href="/plans">Plans and prices</a></li>'
            '<li><a href="/blog">Articles</a></li></ul><p><a href="/">CitedBy</a></p></main>').encode()


def page(msg, lang="en", form=None):
    sv, cv = asset_ver("style.css"), asset_ver("check.css")
    return (f'<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="robots" content="noindex"><title>CitedBy</title><link rel="stylesheet" href="/style.css?v={sv}"><link rel="stylesheet" href="/check.css?v={cv}">'
            f'<body><main class="doc"><p>{html.escape(msg)}</p>{form or ""}<p><a href="/">CitedBy</a></p></main>').encode()


def engines_file():  # cron writes /data/engines.json (tools/engine_probe.py); the image carries a seed so a fresh container is not empty
    f = os.environ.get("ENGINES_FILE") or os.path.join(DATA_DIR, "engines.json")
    return f if os.path.isfile(f) else os.path.join(HERE, "data", "engines.json")


HOME_ROUTES = {"/": "en", "/fr": "fr"}


def render_home(lang):  # the assistant list is read on every request: a stale test date drops the engine from the page
    return home.render(lang, home.live_engines(engines_file())).encode()


PAGE_ROUTES = {"/pricing": "pricing", "/faq": "faq", "/thanks": "thanks"}  # shared-shell pages (RES-1335); /thanks is the app's when proxy.py forwards it


def render_page(name):
    eng = home.live_engines(engines_file())
    return (pages.thanks() if name == "thanks" else pages.data() if name == "data" else getattr(pages, name)(eng)).encode()


def landing_html(s):
    """Trial wording (blocks <!--T-->..<!--/T-->) only when CITEDBY_TRIAL=1; the no-trial wording (<!--N-->) otherwise. Same markers as the app's landing."""
    import re as _re
    if os.environ.get("CITEDBY_TRIAL") == "1": return _re.sub(r"<!--/?T-->", "", _re.sub(r"<!--N-->.*?<!--/N-->", "", s, flags=_re.S))
    return _re.sub(r"<!--/?N-->", "", _re.sub(r"<!--T-->.*?<!--/T-->", "", s, flags=_re.S))

HOST_Q = re.compile(r"^[a-z0-9]([a-z0-9.-]{0,251}[a-z0-9])?\.[a-z]{2,24}$")
def prefill_host(raw_path):
    """The bare host from ?url= on a landing path, or "" (hostname characters only, so it is safe inside the attribute)."""
    v = (parse_qs(urlparse(raw_path).query).get("url", [""])[0]).strip().lower()
    v = re.sub(r"^[a-z]+://", "", v).split("/")[0].split("?")[0]
    v = re.sub(r"^www\.", "", v)
    return v if HOST_Q.match(v) else ""

GONE = {"/data/" + n + ext for n in ("the-france", "cafe-france", "cafe-belgique", "koffie-belgie", "coffee-ireland") for ext in ("", ".csv")}  # RES-1459 row 6: retired tea/coffee studies answer 410
LAUNCH_REDIRECTS = {"/pricing": "/plans", **{f"/{l}/pricing": f"/{l}/plans" for l in ("fr", "nl", "de", "es")}, "/faq": "/#faq", "/help": "/#faq", "/docs": "/#faq", "/sample-audit": "/sample", "/check": "/", "/partners": "/", "/fr/check": "/", "/nl/check": "/", "/fixpack": "/plans", "/fix-pack": "/plans", **{f"/{l}/{p}": f"/{p}" for l in ("fr", "nl", "de", "es") for p in ("legal", "data", "methodology")}}  # RES-2895: no localized copy of these three, so a typed /xx/ URL lands on the English page
GO = {  # RES-2130: short links for posts; one fixed UTM set per link (UTM.md: lowercase [a-z0-9_]); other query params (e.g. internal=1) are forwarded, utm_* from the caller are dropped
    "/go/hn": {"utm_source": "hackernews", "utm_medium": "organic_social", "utm_campaign": "citedby_202610", "utm_content": "show_hn_01"},
}
ROUTES = {"/legal": "legal.html", "/privacy": "privacy.html"}
CSP = ("default-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; script-src 'self'; connect-src 'self'; "
       "base-uri 'self'; form-action 'self' https://buy.stripe.com mailto:; frame-ancestors 'none'")


class H(BaseHTTPRequestHandler):
    timeout = 15  # idle or half-sent connections must not hold a thread
    server_version = "citedby"
    sys_version = ""

    def log_message(self, fmt, *a):  # no query strings (tokens) or IPs in logs
        print(self.command, urlparse(self.path).path, a[1] if len(a) > 1 else "", flush=True)

    def ip(self):
        xf = self.headers.get("X-Forwarded-For", "")
        return xf.split(",")[-1].strip() if xf else self.client_address[0]

    def out(self, code, body, ctype="text/html; charset=utf-8", extra=None):
        if code == 200 and ctype.startswith("text/html"):
            body = legal_links.localize(withdraw_link.inject(follow_link.inject(hub_links.inject(social.ensure(analytics.inject(trust.inject(body, self.path)))))))
        elif code == 404 and ctype.startswith("text/html"):
            body = withdraw_link.inject(body)  # RES-2199: the EU withdrawal link is on every page, error pages included (no analytics or share tags there)
        cache = "no-store"
        if code == 200 and not self.path.startswith(("/api/", "/health", "/deploy-id", "/mcp")):
            cache = "public, max-age=604800" if self.path.split("?")[0].endswith((".css", ".js", ".svg", ".png", ".ico", ".woff2")) and not self.path.startswith(("/saas.", "/landing.", "/sample.")) else "public, max-age=300"
        etag = None
        if cache != "no-store" and self.command in ("GET", "HEAD"):  # RES-3284: conditional requests for pages and assets (crawlers re-fetch with If-None-Match)
            etag = '"%s"' % hashlib.sha256(body).hexdigest()[:20]
            if self.headers.get("If-None-Match") == etag:
                code, body = 304, b""
        self.send_response(code)
        if code != 304:
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
        if etag:
            self.send_header("ETag", etag)
        self.send_header("Cache-Control", cache)
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        self.send_header("Content-Security-Policy", CSP)
        self.send_header("X-Frame-Options", "DENY"); self.send_header("Permissions-Policy", "camera=(), microphone=(), geolocation=(), payment=()")  # RES-2976
        self.send_header("Strict-Transport-Security", "max-age=31536000")
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def static(self, path):
        if path in GONE:
            return self.out(410, page("Gone"))
        if path in GO:
            from urllib.parse import urlencode
            keep = [(k, v) for k, vs in parse_qs(urlparse(self.path).query).items() if not k.startswith("utm_") for v in vs][:5]
            return self.out(302, b"", extra={"Location": "/?" + urlencode(list(GO[path].items()) + keep), "X-Robots-Tag": "noindex"})
        if path in LAUNCH_REDIRECTS:  # RES-1496: the old shop-scan pages are retired; their paths lead to the new landing
            return self.out(301, b"", extra={"Location": LAUNCH_REDIRECTS[path]})
        if path == "/" or path in langroutes.LANDING_PATHS:  # RES-1731 row 10: / is English, /fr /nl /de /es are real translations (tools/localize_landing.py)
            lang = langroutes.LANDING_PATHS.get(path, "en")
            with open(os.path.join(SITE_DIR, "landing.html" if lang == "en" else f"landing.{lang}.html"), encoding="utf-8") as f:
                page_html = landing_html(f.read())
            pre = prefill_host(self.path)  # RES-2343: /fr?url=lemonde.fr fills the field on the server, no JavaScript needed
            if pre: page_html = page_html.replace('id="u" name="url"', f'id="u" name="url" value="{pre}"', 1)
            return self.out(200, langroutes.head(page_html, lang).encode())
        if path == "/data/":
            return self.out(301, b"", extra={"Location": "/data"})
        if path in HOME_ROUTES:
            return self.out(200, render_home(HOME_ROUTES[path]))
        if path in PAGE_ROUTES:
            return self.out(200, render_page(PAGE_ROUTES[path]))
        rel = ROUTES.get(path) or path.lstrip("/")
        base = os.path.realpath(SITE_DIR)
        full = os.path.realpath(os.path.join(base, rel))
        for cand in (full, full + ".html", os.path.join(full, "index.html")):  # same clean URLs as the old nginx try_files
            if cand.startswith(base + os.sep) and os.path.isfile(cand):
                full = cand
                break
        if not full.startswith(base + os.sep) or not os.path.isfile(full):
            if len(path) > 1 and path.endswith("/"):  # RES-1785: /fr/ and /plans/ work like /fr and /plans
                return self.out(301, b"", extra={"Location": path.rstrip("/") or "/"})
            return self.out(404, not_found_page())
        ctype = mimetypes.guess_type(full)[0] or "application/octet-stream"
        if ctype.startswith("text/") or ctype in ("application/xml", "application/javascript"):
            ctype += "; charset=utf-8"
        with open(full, "rb") as f:
            # RES-3708: the plugin zip and its Playground blueprint are fetched by playground.wordpress.net from the browser, so they carry CORS
            self.out(200, f.read(), ctype, extra={"Access-Control-Allow-Origin": "*"} if path.startswith("/downloads/") else None)

    def backlinks(self, u):
        if u.path == "/sitemap-backlinks.xml":
            return self.out(200, backlinks.sitemap().encode(), "application/xml; charset=utf-8")
        m = backlinks.ROUTE.match(u.path)  # RES-3749: /backlinks and /fr|de|es|nl/backlinks
        lg, rest = m.group(1) or "en", m.group(2)
        p, no_index = backlinks.prefix(lg), {"X-Robots-Tag": "noindex"}
        if rest is None:
            raw = (parse_qs(u.query).get("host") or [""])[0]
            if not raw:
                return self.out(200, backlinks.index_page("", lg).encode())
            h = backlinks.norm(raw)
            if h:
                return self.out(302, b"", extra={"Location": p + "/backlinks/" + h, **no_index})
            return self.out(200, backlinks.index_page(backlinks.T[lg]["bad_host"], lg).encode(), extra=no_index)
        raw = rest.rstrip("/")
        if raw == "method":  # RES-3899: the method text, once
            return self.out(200, backlinks.method_page(lg).encode())
        h = backlinks.norm(raw)
        if not h:
            if lg == "en":
                return self.out(404, not_found_page())
            return self.out(404, backlinks.index_page(backlinks.T[lg]["bad_host"], lg).encode(), extra=no_index)  # a page in the visitor's language with the lookup form
        if h != raw:  # www., upper case, a pasted URL: one canonical address per domain
            return self.out(301, b"", extra={"Location": p + "/backlinks/" + h})
        code, body = backlinks.host_page(h, lg)
        self.out(code, body.encode())

    def do_HEAD(self): self.do_GET()

    MCP_CORS = {"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "Content-Type, Accept, Mcp-Session-Id, Mcp-Protocol-Version, Authorization", "Access-Control-Allow-Methods": "POST, GET, OPTIONS", "Access-Control-Expose-Headers": "Mcp-Session-Id", "X-Robots-Tag": "noindex"}

    def do_OPTIONS(self):  # RES-3798: the CORS preflight of a browser-based MCP client
        if urlparse(self.path).path != "/mcp": return self.out(404, not_found_page())
        self.out(204, b"", "application/json", extra=self.MCP_CORS)

    def do_GET(self):
        if proxy.handle(self, "GET"): return
        u = urlparse(self.path)
        if u.path == "/mcp":  # RES-3798: the MCP endpoint answers POST; a person who opens it in a browser is sent to the page that explains it, a client asking for an event stream is told there is none
            if "text/html" in (self.headers.get("Accept") or "") and "text/event-stream" not in (self.headers.get("Accept") or ""):
                return self.out(302, b"", extra={"Location": "/mcp-server", "X-Robots-Tag": "noindex"})
            return self.out(405, json.dumps({"error": "Use POST with a JSON-RPC message (MCP Streamable HTTP). There is no event stream."}).encode(), "application/json", extra={**self.MCP_CORS, "Allow": "POST, OPTIONS"})
        if backlinks.ROUTE.match(u.path) or u.path == "/sitemap-backlinks.xml":  # RES-3699: open-data referring-domain lookup; RES-3749: in fr, de, es and nl too
            return self.backlinks(u)
        if u.path == "/go/fixpack":  # RES-2134: the Payment Link leaves no trace of its own, so the button comes here first: count the open (not from our own addresses), then 302
            lg = (parse_qs(u.query).get("lang") or ["en"])[0]
            count_event("fixpack_click", lg if lg in LANGS else "en", self.ip())
            return self.out(302, b"", extra={"Location": "/plans", "Cache-Control": "no-store", "X-Robots-Tag": "noindex"})
        if u.path == "/health":
            try:  # a fresh read-only connection: fails if the file is missing, unreadable or corrupt, never creates it
                c = sqlite3.connect("file:%s?mode=ro" % DB_PATH, uri=True, timeout=2)
                try: c.execute("SELECT count(*) FROM event_count").fetchone()
                finally: c.close()
                ok = True
            except sqlite3.Error:
                ok = False
            body = {"status": "ok" if ok else "error", "db": "ok" if ok else "error", "time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
            app = proxy.app_health()  # the app's own status and deploy id; its failure never fails the site
            if app: body["app"] = app
            return self.out(200 if ok else 503, json.dumps(body).encode(), "application/json")
        if u.path == "/deploy-id":
            return self.out(200, json.dumps({"deploy_id": DEPLOY_ID}).encode(), "application/json")
        if u.path == "/healthz":
            return self.out(200, b'{"ok":true}', "application/json")
        if u.path in ("/api/confirm", "/api/unsubscribe"):  # links in mails sent before the form was retired (RES-3940 F3): nothing is stored any more
            return self.out(410, page(GONE_TXT))
        if u.path.startswith("/api/"):
            return self.out(404, b'{"ok":false}', "application/json")
        self.static(u.path)

    def do_POST(self):
        if proxy.handle(self, "POST"): return
        u = urlparse(self.path)
        if u.path == "/mcp":  # RES-3798
            try: n = int(self.headers.get("Content-Length") or 0)
            except ValueError: n = -1
            if n < 0 or n > 16384: return self.out(413, json.dumps({"error": "message too large"}).encode(), "application/json", extra=self.MCP_CORS)
            code, body = mcp.handle(self.rfile.read(n) if n else b"", self.ip())
            return self.out(code, body, "application/json", extra=self.MCP_CORS)
        try:
            n = int(self.headers.get("Content-Length") or 0)
        except ValueError:
            n = 0
        if u.path == "/riq-e":  # RES-1071: same-origin relay to PostHog, always 204
            if 0 < n <= 8192:
                analytics.relay(self.rfile.read(n), self.ip(), self.headers.get("User-Agent", ""))
            return self.out(204, b"", "application/json")
        if n > 4096:
            return self.out(413, b'{"ok":false}', "application/json")
        raw = self.rfile.read(n) if n else b""
        try:
            data = json.loads(raw or b"{}")
            if not isinstance(data, dict):
                raise ValueError
        except ValueError:
            data = None
        send = lambda code, d: self.out(code, json.dumps(d).encode(), "application/json")
        if data is None:
            return send(400, {"ok": False})
        if u.path == "/api/check":
            code, body = handle_check(data, self.ip())
            return send(code, body)
        if u.path == "/api/request":  # RES-3940 F3: the email mini-audit form is retired
            return send(410, {"ok": False, "error": "gone"})
        if u.path == "/api/event":
            if data.get("type") in ("fixpack_click", "first_screen_cta_click", "offer_view"):  # the events the browser reports; the rest are counted server-side
                count_event(data["type"], data.get("lang"), self.ip())
            return self.out(204, b"", "application/json")
        self.out(404, b'{"ok":false}', "application/json")


if __name__ == "__main__":
    retire_mini_audit()
    ThreadingHTTPServer(("0.0.0.0", int(os.environ.get("PORT", "8080"))), H).serve_forever()
