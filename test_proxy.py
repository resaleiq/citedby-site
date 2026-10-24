"""App proxy rules (RES-661 prod cutover). Run: python3 test_proxy.py"""
import json, os, tempfile, threading, unittest, urllib.request, urllib.error
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import proxy

SEEN = []
SIG = []
ACCEPT = []
QA = []

class Stub(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def _do(self):
        n = int(self.headers.get("Content-Length") or 0)
        SEEN.append((self.command, self.path, self.headers.get("X-Forwarded-For"), self.headers.get("Cookie"), self.rfile.read(n)))
        SIG.append(self.headers.get("Stripe-Signature")); ACCEPT.append(self.headers.get("Accept")); QA.append(self.headers.get("X-CitedBy-QA"))
        if self.path.startswith("/health"):
            b = b'{"status":"ok","deploy":"abc1234","db":"ok","ok":true}'
        else:
            b = b"app-page"
        self.send_response(302 if self.path == "/login/" + "x" * 24 else 200)
        self.send_header("Content-Type", "text/html"); self.send_header("Content-Length", str(len(b)))
        self.send_header("Set-Cookie", "ci_session=v; Path=/; HttpOnly"); self.send_header("Server", "leak")
        if self.path == "/login/" + "x" * 24: self.send_header("Location", "/dashboard")
        self.end_headers(); self.wfile.write(b)
    do_GET = do_POST = _do

class H(BaseHTTPRequestHandler):  # minimal host that uses proxy like server.py does
    def log_message(self, *a): pass
    def ip(self): return "203.0.113.9"
    def do_GET(self):
        if not proxy.handle(self, "GET"): self.send_response(404); self.send_header("Content-Length", "0"); self.end_headers()
    def do_POST(self):
        if not proxy.handle(self, "POST"): self.send_response(404); self.send_header("Content-Length", "0"); self.end_headers()

def serve(cls):
    s = ThreadingHTTPServer(("127.0.0.1", 0), cls); threading.Thread(target=s.serve_forever, daemon=True).start(); return s

class T(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = serve(Stub); cls.host = serve(H)
        cls.base = "http://127.0.0.1:%d" % cls.host.server_address[1]
    def setUp(self): SEEN.clear(); SIG.clear(); proxy.UPSTREAM = "http://127.0.0.1:%d" % self.app.server_address[1]
    def get(self, path, **kw):
        try:
            r = urllib.request.urlopen(urllib.request.Request(self.base + path, **kw)); return r.status, r.read(), r.headers
        except urllib.error.HTTPError as e: return e.code, e.read(), e.headers

    def test_off_by_default(self):
        proxy.UPSTREAM = ""
        self.assertEqual(self.get("/plans")[0], 404); self.assertEqual(SEEN, [])

    def test_allowlist_only(self):
        for p in ("/instant", "/fr/instant", "/nl/instant?domain=x.com", "/plans?billing=year", "/dashboard", "/os?tab=graph&host=citedby.eu", "/account", "/recount/" + "a" * 24, "/api/snapshot/7", "/r/" + "a" * 22 + ".csv", "/api/snapshot/" + "Hn-hGKmWgDksJUToqNLfgw", "/thanks", "/fr/plans", "/nl/plans?billing=year", "/de/plans", "/es/sample", "/fr/sample", "/thanks?session_id=cs_live_a1", "/report/" + "a" * 24, "/r/" + "a" * 22, "/start/" + "a" * 43, "/api/crawl/abc123", "/t/t_abcdefghij12", "/api/teaser/token", "/api/teaser/t_abcdefghij12"):
            self.assertEqual(self.get(p)[1], b"app-page", p)
        for p in ("/", "/fr", "/health-x", "/api/order", "/api/stripe/webhook", "/thanksx", "/report/short", "/r/short", "/r/" + "a" * 65, "/report/" + "a" * 65, "/start/short", "/start/" + "a" * 65, "/api/fixpack/intake", "/api/snapshot/short", "/api/snapshot/" + "a" * 65, "/api/snapshot/abc/def", "/plansx", "/instantx", "/../plans", "/de/instant", "/fr/plansx", "/pl/plans", "/fr/instantx", "/fr/dashboard", "/osx", "/os/x", "/bot", "/api/crawl/a/b", "/t/short", "/api/teaser/short", "/api/teaser"):
            self.assertEqual(self.get(p)[0], 404, p)

    def test_forwards_one_client_ip_and_cookie_not_spoofed_xff(self):
        self.get("/account", headers={"Cookie": "ci_session=abc", "X-Forwarded-For": "1.1.1.1, 2.2.2.2"})
        m, path, xff, ck, _ = SEEN[0]
        self.assertEqual(xff, "203.0.113.9"); self.assertEqual(ck, "ci_session=abc")

    def test_accept_header_is_forwarded(self):  # RES-1595: the app returns the HTML /account (or 303 to /signin) only for Accept: text/html
        QA.clear(); self.get("/api/teaser/token", headers={"X-CitedBy-QA": "tok"}); self.assertEqual(QA[0], "tok")  # RES-1785: QA header reaches the app
        ACCEPT.clear(); self.get("/account", headers={"Accept": "text/html,application/xhtml+xml"})
        self.assertEqual(ACCEPT[0], "text/html,application/xhtml+xml")

    def test_response_headers_are_filtered_and_robots_blocked(self):
        s, b, h = self.get("/plans")
        self.assertEqual(h["Set-Cookie"], "ci_session=v; Path=/; HttpOnly")
        self.assertIsNone(h["X-Robots-Tag"]); self.assertEqual(h["Cache-Control"], "no-store")  # RES-1731: pricing is meant to be found
        self.assertEqual(self.get("/dashboard")[2]["X-Robots-Tag"], "noindex"); self.assertIsNone(self.get("/fr/plans")[2]["X-Robots-Tag"])
        self.assertNotIn("leak", (h.get("Server") or ""))

    def test_post_body_and_redirect_pass_through(self):
        req = urllib.request.Request(self.base + "/api/snapshot", b'{"a":1}', {"Content-Type": "application/json"})
        self.assertEqual(urllib.request.urlopen(req).read(), b"app-page"); self.assertEqual(SEEN[0][4], b'{"a":1}')
        class NoRedir(urllib.request.HTTPRedirectHandler):
            def redirect_request(self, *a, **k): return None
        op = urllib.request.build_opener(NoRedir)
        with self.assertRaises(urllib.error.HTTPError) as c: op.open(self.base + "/login/" + "x" * 24)
        self.assertEqual(c.exception.code, 302); self.assertEqual(c.exception.headers["Location"], "/dashboard")

    def test_stripe_webhook_forwards_raw_body_and_signature(self):
        raw = b'{"id":"evt_1",  "type":"checkout.session.completed"}'
        req = urllib.request.Request(self.base + "/api/stripe/webhook", raw, {"Content-Type": "application/json", "Stripe-Signature": "t=1,v1=ab"})
        self.assertEqual(urllib.request.urlopen(req).read(), b"app-page"); self.assertEqual(SEEN[0][4], raw)
        self.assertEqual(SEEN[0][1], "/api/stripe/webhook"); self.assertEqual(SIG[-1], "t=1,v1=ab")

    def test_fixpack_intake_post_is_forwarded(self):
        req = urllib.request.Request(self.base + "/api/fixpack/intake", b'{"token":"t"}', {"Content-Type": "application/json"})
        self.assertEqual(urllib.request.urlopen(req).read(), b"app-page"); self.assertEqual(SEEN[0][1], "/api/fixpack/intake")

    # RES-2572: the app's project routes. Keep in step with citedby-app sa_projects.PROJECT_ROUTES (its test pins the same table): a route missing here is a 404 on citedby.eu.
    APP_PROJECT_ROUTES = {"monitors": ("GET", "POST"), "settings": ("GET", "POST"), "history": ("GET",), "progress": ("GET",), "crawl": ("POST",), "verify": ("GET", "POST"), "sitemap": ("GET", "POST"), "remove": ("POST",), "gsc": ("GET", "POST"), "gsc/clear": ("POST",), "logs": ("GET", "POST"), "logs/clear": ("POST",), "conn": ("GET",), "conn/refresh": ("POST",), "conn/bing": ("POST",), "conn/google": ("POST",), "conn/clear": ("POST",), "indexnow": ("GET", "POST"), "os/graph": ("GET",), "os/query": ("GET",), "os/page": ("GET",), "os/sources": ("GET",), "os/sos": ("GET",), "os/quickwins": ("GET",), "os/gaps": ("GET",), "os/decay": ("GET",), "os/rivals": ("GET",), "os/ai-gaps": ("GET",), "os/cannibal": ("GET",), "os/index": ("GET",), "os/next": ("GET",)}

    def test_every_app_project_route_is_forwarded(self):
        for what, methods in self.APP_PROJECT_ROUTES.items():
            for m in ("GET", "POST"):
                p = "/api/projects/example.com/" + what; SEEN.clear()
                if m == "GET": code, body = self.get(p)[:2]
                else:
                    try: r = urllib.request.urlopen(urllib.request.Request(self.base + p, b"{}", {"Content-Type": "application/json"})); code, body = r.status, r.read()
                    except urllib.error.HTTPError as e: code, body = e.code, e.read()
                if m in methods: self.assertEqual((code, body), (200, b"app-page"), m + " " + p)
                else: self.assertEqual(code, 404, m + " " + p)   # the app answers 405 itself for these; the proxy never forwards a method the app does not serve
        for p in ("/api/projects/ab/settings", "/api/projects/example.com/other", "/api/projects/example.com", "/api/projects/example.com/settings/x", "/api/projects/Exa_mple/settings"):
            self.assertEqual(self.get(p)[0], 404, p)

    def test_project_upload_bodies_use_the_apps_caps(self):
        def post(path, n):
            try: return urllib.request.urlopen(urllib.request.Request(self.base + path, b"x" * n, {"Content-Type": "application/json"})).status
            except urllib.error.HTTPError as e: return e.code
            except urllib.error.URLError: return 413   # the proxy answers 413 without reading the body, so the client may see a reset
        self.assertEqual(post("/api/projects/example.com/sitemap", 1_500_000), 200)
        self.assertEqual(post("/api/projects/example.com/gsc", 5_000_000), 200)
        self.assertEqual(post("/api/projects/example.com/logs", 5_000_000), 200)
        self.assertEqual(post("/api/projects/example.com/settings", 70_000), 413)
        self.assertEqual(post("/api/projects/example.com/sitemap", 2_200_000), 413)

    def test_upstream_down_is_502_not_a_crash(self):
        proxy.UPSTREAM = "http://127.0.0.1:1"
        self.assertEqual(self.get("/plans")[0], 502)

    def test_res2738_upstream_down_gives_html_to_a_browser_json_to_the_rest(self):
        proxy.UPSTREAM = "http://127.0.0.1:1"
        c, b, h = self.get("/fr/tools/findable-check/webmd.com", headers={"Accept": "text/html,application/xhtml+xml"})
        self.assertEqual(c, 502); self.assertIn("text/html", h["Content-Type"]); self.assertTrue(b.startswith(b"<!doctype html>")); self.assertIn("CitedBy est occup", b.decode()); self.assertNotIn(b"app unavailable", b)
        c, b, h = self.get("/tools/findable-check/webmd.com", headers={"Accept": "text/html"}); self.assertIn(b"CitedBy is busy", b)
        c, b, h = self.get("/api/me", headers={"Accept": "text/html"}); self.assertEqual(b, b'{"error":"app unavailable"}')

    def test_app_health_summary(self):
        self.assertEqual(proxy.app_health(), {"status": "ok", "deploy": "abc1234"})
        proxy.UPSTREAM = ""; self.assertIsNone(proxy.app_health())
        proxy.UPSTREAM = "http://127.0.0.1:1"; proxy._H.update(t=0); self.assertEqual(proxy.app_health(), {"status": "error", "deploy": None})

if __name__ == "__main__": unittest.main()


class RouteTable(unittest.TestCase):
    def test_launch_routes_are_forwarded(self):
        g, p = proxy.ROUTES["GET"], proxy.ROUTES["POST"]
        for path in ("/signin", "/login", "/signup", "/logout", "/api/me", "/api/projects", "/api/audits", "/api/audits/a_k3j2h1", "/api/audits/a_k3j2h1/pages", "/api/audits/a_k3j2h1/page", "/api/audit/a_k3j2h1/pdf", "/r/audit/a_k3j2h1", "/r/os/abcdefghijklmnopqrstuvwx", "/plans", "/app.html", "/saas.js", "/saas.css", "/sample.js", "/landing.js", "/sample"):
            self.assertTrue(g.fullmatch(path), path)
        for path in ("/api/audits", "/api/audit", "/api/audit/a_k3j2h1/recrawl", "/api/checkout"):
            self.assertTrue(p.fullmatch(path), path)
        for path in ("/api/audits/../x", "/api/audits/a_k3j2h1/other", "/admin"):
            self.assertFalse(g.fullmatch(path), path)

def test_auth_routes_are_forwarded_res1641():
    import proxy
    for p in ("/forgot", "/reset/" + "a" * 30, "/auth/google", "/auth/google/callback", "/api/gsc/callback"): assert proxy.ROUTES["GET"].fullmatch(p), p
    for p in ("/api/auth/signup", "/api/auth/login", "/api/auth/forgot", "/api/auth/reset"): assert proxy.ROUTES["POST"].fullmatch(p), p


def test_trial_cancel_paths_are_forwarded():
    import proxy
    p = "/trial/cancel/sub_1ABC.deadbeefdeadbeefdeadbeef"
    assert proxy.ROUTES["GET"].fullmatch(p) and proxy.ROUTES["POST"].fullmatch(p)


def test_app_v2_routes_are_forwarded():
    import proxy
    for p in ("/app/app.css", "/app/report2.js", "/api/usage", "/api/account", "/api/brand", "/api/team", "/api/audit/a_k3j2h1/structure", "/api/audit/a_k3j2h1/compare", "/api/audit/a_k3j2h1/discovery"): assert proxy.ROUTES["GET"].fullmatch(p), p
    for p in ("/api/account/signout-all", "/api/brand", "/api/brand/domain-check", "/api/team/remove", "/api/share/a_k3j2h1/unlock", "/api/audit/a_k3j2h1/share", "/api/audit/a_k3j2h1/schedule", "/api/projects/example.com/verify"): assert proxy.ROUTES["POST"].fullmatch(p), p
    for p in ("/app/../x", "/app/x/y.js", "/api/admin/audit/a_k3j2h1"): assert not proxy.ROUTES["GET"].fullmatch(p), p


def test_free_tools_paths_are_forwarded_and_only_tool_pages_are_indexable():
    """RES-2323: /tools, both tools and their result pages in every language reach the app; results stay noindex."""
    for p in ("/tools", "/fr/tools", "/tools/ai-crawler-check", "/de/tools/llms-txt-checker", "/es/tools/ai-crawler-check/elpais.com", "/tools/llms-txt-checker/www.shop.co.uk", "/tools/findable-check", "/fr/tools/findable-check/elpais.com", "/tools/llms-txt-generator", "/nl/tools/llms-txt-generator", "/de/tools/llms-txt-generator/bundesregierung.de"):  # RES-4115: the generator and its result pages
        assert proxy.ROUTES["GET"].fullmatch(p), p
    for p in ("/tools/other", "/tools/ai-crawler-check/a/b", "/xx/tools", "/tools/ai-crawler-check/a_b.com"): assert not proxy.ROUTES["GET"].fullmatch(p), p
    for p in ("/tools", "/de/tools/llms-txt-checker", "/fr/tools/llms-txt-checker", "/es/tools/llms-txt-checker", "/de/tools/ai-crawler-check", "/de/tools/findable-check", "/ci", "/sample") + tuple(f"{p}/tools/llms-txt-generator" for p in ("", "/fr", "/nl", "/de", "/es")): assert proxy.INDEXABLE.fullmatch(p), p
    for p in ("/nl/tools/llms-txt-checker", "/es/tools/ai-crawler-check", "/nl/tools/ai-crawler-check", "/fr/sample"): assert not proxy.INDEXABLE.fullmatch(p), p  # RES-3269: noindex translations
    assert not proxy.INDEXABLE.fullmatch("/tools/ai-crawler-check/shop.eu") and not proxy.INDEXABLE.fullmatch("/tools/llms-txt-generator/shop.eu")  # a result page is noindex

def test_res3836_badge_page_and_svg_are_forwarded_and_only_the_page_is_indexable():
    """RES-3836: /badge in 5 languages and /badge/<host>.svg reach the app; the page is indexable, the image is not."""
    for p in ("/badge", "/fr/badge", "/nl/badge", "/de/badge", "/es/badge", "/badge/shop.eu.svg", "/badge/www.shop.co.uk.svg"):
        assert proxy.ROUTES["GET"].fullmatch(p), p
    for p in ("/badge/", "/xx/badge", "/badge/shop.eu.png", "/badge/a/b.svg", "/badge/a_b.com.svg", "/fr/badge/shop.eu.svg", "/badge/.svg"): assert not proxy.ROUTES["GET"].fullmatch(p), p
    for p in ("/badge", "/fr/badge", "/nl/badge", "/de/badge", "/es/badge"): assert proxy.INDEXABLE.fullmatch(p), p
    assert not proxy.INDEXABLE.fullmatch("/badge/shop.eu.svg")


def test_res3836_badge_is_in_the_sitemap_with_hreflang_and_in_llms_txt():
    import os
    sm = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "public/sitemap.xml"), encoding="utf-8").read()
    llms = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "public/llms.txt"), encoding="utf-8").read()
    for l in ("", "/fr", "/nl", "/de", "/es"):
        assert sm.count(f"<loc>https://citedby.eu{l}/badge</loc>") == 1, l
        assert f'hreflang="{(l or "/en")[1:]}" href="https://citedby.eu{l}/badge"' in sm
    assert 'hreflang="x-default" href="https://citedby.eu/badge"' in sm
    assert llms.count("(https://citedby.eu/badge)") == 1


def test_res2423_wrong_mark_is_forwarded():
    import proxy
    assert proxy.ROUTES["POST"].fullmatch("/api/audit/a_k3j2h1/wrong")

def test_res2514_verify_bundle_timeline_are_forwarded():
    assert proxy.ROUTES["POST"].fullmatch("/api/audit/a_k3j2h1/verify")
    for w in ("bundle", "timeline"): assert proxy.ROUTES["GET"].fullmatch("/api/audit/a_k3j2h1/" + w)
    assert not proxy.ROUTES["GET"].fullmatch("/api/audit/a_k3j2h1/nope")


class Res2976(T):
    def test_every_proxied_page_is_unframable_and_gets_a_csp(self):
        for p in ("/plans", "/sample", "/signin", "/signup", "/forgot", "/withdraw/verify", "/fr/withdraw/verify"):
            s, b, h = self.get(p)
            self.assertEqual(h["X-Frame-Options"], "DENY", p); self.assertIn("frame-ancestors 'none'", h["Content-Security-Policy"], p); self.assertIn("camera=()", h["Permissions-Policy"], p)

    def test_security_txt_is_served_and_the_site_sends_the_same_headers(self):
        os.environ.setdefault("OPTIN_SECRET", "x" * 40); os.environ.setdefault("BASE_URL", "http://t"); os.environ.setdefault("DATA_DIR", tempfile.mkdtemp())
        import server
        s, b, h = serve_site(server)
        self.assertEqual(s, 200); self.assertIn(b"Contact: mailto:hello@citedby.eu", b); self.assertEqual(h["X-Frame-Options"], "DENY"); self.assertIn("frame-ancestors 'none'", h["Content-Security-Policy"])

def serve_site(server):
    s = ThreadingHTTPServer(("127.0.0.1", 0), server.H); threading.Thread(target=s.serve_forever, daemon=True).start()
    try:
        r = urllib.request.urlopen("http://127.0.0.1:%d/.well-known/security.txt" % s.server_address[1]); return r.status, r.read(), r.headers
    finally: s.shutdown()
