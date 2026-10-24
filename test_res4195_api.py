"""RES-4195: GET /api/v1/ai-access (the free public AI-access API front door), /openapi.json and the docs page in 5 languages.
Run: python3 -m pytest -q test_res4195_api.py"""
import http.client, json, os, re, sqlite3, tempfile, threading
from http.server import BaseHTTPRequestHandler, HTTPServer
os.environ.update(OPTIN_SECRET="x" * 40, BASE_URL="http://t", DATA_DIR=tempfile.mkdtemp())
import pytest
import api_v1, proxy, server
from tools import build_ai_access_api as B

srv = server.ThreadingHTTPServer(("127.0.0.1", 0), server.H)
threading.Thread(target=srv.serve_forever, daemon=True).start()
PORT = srv.server_port
SEEN = []
PUB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")


class FakeApp(BaseHTTPRequestHandler):
    reply = (200, {"site": "acme.example"}, {})

    def log_message(self, *a): pass

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        SEEN.append((self.path, body, self.headers.get("X-Forwarded-For")))
        code, j, hdr = FakeApp.reply; b = json.dumps(j).encode()
        self.send_response(code); self.send_header("Content-Length", str(len(b)))
        for k, v in hdr.items(): self.send_header(k, v)
        self.end_headers(); self.wfile.write(b)


fake = HTTPServer(("127.0.0.1", 0), FakeApp); threading.Thread(target=fake.serve_forever, daemon=True).start()


@pytest.fixture(autouse=True)
def app(monkeypatch):
    monkeypatch.setattr(proxy, "UPSTREAM", f"http://127.0.0.1:{fake.server_port}"); FakeApp.reply = (200, {"site": "acme.example"}, {}); SEEN.clear()


def req(method, path, headers=None):
    c = http.client.HTTPConnection("127.0.0.1", PORT, timeout=20)
    try:
        c.request(method, path, headers=headers or {})
        r = c.getresponse(); b = r.read()
        return r.status, {k.lower(): v for k, v in r.getheaders()}, b
    finally: c.close()


def counted():
    c = sqlite3.connect(server.DB_PATH)
    try: return c.execute("SELECT coalesce(sum(n),0) FROM event_count WHERE type='api_ai_access'").fetchone()[0]
    finally: c.close()


def test_a_result_is_passed_through_with_cors_the_callers_address_and_is_counted_once():
    before = counted()
    st, hd, b = req("GET", "/api/v1/ai-access?url=https%3A%2F%2Facme.example%2Fshop")
    assert st == 200 and json.loads(b) == {"site": "acme.example"} and hd["content-type"].startswith("application/json")
    assert hd["access-control-allow-origin"] == "*" and "Retry-After" in hd["access-control-expose-headers"] and hd["cache-control"] == "no-store" and hd["x-robots-tag"] == "noindex"
    assert SEEN == [("/internal/api-ai-access", {"url": "https://acme.example/shop"}, "127.0.0.1")]
    assert counted() == before + 1


@pytest.mark.parametrize("path", ["/api/v1/ai-access", "/api/v1/ai-access?url=", "/api/v1/ai-access?url=%20%20", "/api/v1/ai-access?url=" + "a" * 2049])
def test_missing_or_oversize_url_is_a_400_json_error_with_no_app_call_and_no_count(path):
    before = counted()
    st, hd, b = req("GET", path)
    assert st == 400 and json.loads(b)["error"]["code"] in ("missing_url", "bad_url") and json.loads(b)["error"]["message"] and hd["access-control-allow-origin"] == "*"
    assert SEEN == [] and counted() == before


def test_refusals_keep_their_status_and_retry_after_and_are_not_counted():
    before = counted()
    for code, key, hdr in ((429, "rate_limited", {"Retry-After": "600"}), (422, "site_unreachable", {}), (503, "busy", {"Retry-After": "60"}), (202, "pending", {"Retry-After": "10"})):
        FakeApp.reply = (code, {"error": {"code": key, "message": "m"}}, hdr)
        st, hd, b = req("GET", "/api/v1/ai-access?url=acme.example")
        assert st == code and json.loads(b)["error"]["code"] == key and hd.get("retry-after") == hdr.get("Retry-After") and hd["access-control-allow-origin"] == "*", code
    assert counted() == before


def test_an_unreachable_or_missing_app_is_a_json_error_never_a_crash(monkeypatch):
    monkeypatch.setattr(proxy, "UPSTREAM", "http://127.0.0.1:9")
    st, _, b = req("GET", "/api/v1/ai-access?url=acme.example"); assert st == 502 and json.loads(b)["error"]["code"] == "unavailable"
    monkeypatch.setattr(proxy, "UPSTREAM", "")
    st, _, b = req("GET", "/api/v1/ai-access?url=acme.example"); assert st == 503 and json.loads(b)["error"]["code"] == "unavailable"
    monkeypatch.setattr(proxy, "UPSTREAM", f"http://127.0.0.1:{fake.server_port}")


def test_preflight_answers_cors_head_asks_nobody_and_other_api_paths_stay_404():
    st, hd, _ = req("OPTIONS", "/api/v1/ai-access", {"Origin": "https://x.example", "Access-Control-Request-Method": "GET"})
    assert st == 204 and hd["access-control-allow-origin"] == "*" and "GET" in hd["access-control-allow-methods"] and hd["access-control-max-age"] == "86400"
    st, hd, b = req("HEAD", "/api/v1/ai-access?url=acme.example"); assert st == 200 and b == b"" and SEEN == []
    assert req("GET", "/api/v1/other")[0] == 404 and req("OPTIONS", "/api/v1/other")[0] == 404 and req("POST", "/api/v1/ai-access")[0] == 404


# ---- the OpenAPI spec ----
def spec(): return json.load(open(os.path.join(PUB, "openapi.json"), encoding="utf-8"))


def test_the_spec_is_served_as_json_with_cors_and_describes_the_one_operation():
    st, hd, b = req("GET", "/openapi.json")
    assert st == 200 and hd["content-type"].startswith("application/json") and hd["access-control-allow-origin"] == "*"
    s = json.loads(b)
    assert s["openapi"] == "3.1.0" and s["servers"] == [{"url": "https://citedby.eu"}] and list(s["paths"]) == ["/api/v1/ai-access"]
    op = s["paths"]["/api/v1/ai-access"]["get"]
    assert op["parameters"][0]["name"] == "url" and op["parameters"][0]["required"] is True and "security" not in op and "securitySchemes" not in s.get("components", {})
    assert set(op["responses"]) == {"200", "202", "400", "422", "429", "502", "503"}
    assert s["info"]["termsOfService"] == "https://citedby.eu/ai-access-api#terms" and s["info"]["contact"]["email"] == "hello@citedby.eu"


def test_the_spec_has_no_grade_or_score_and_its_example_fits_its_schema():
    s = spec(); blob = json.dumps(s["components"]["schemas"]).lower()
    props = set(re.findall(r'"([a-z_]+)": \{', json.dumps(s["components"], indent=0).lower()))
    assert not props & {"grade", "score", "letter", "rating"}, props
    schema = s["components"]["schemas"]["AiAccess"]; ex = s["paths"]["/api/v1/ai-access"]["get"]["responses"]["200"]["content"]["application/json"]["example"]
    assert set(schema["required"]) <= set(ex) and set(ex) <= set(schema["properties"])
    cr = schema["properties"]["crawlers"]["items"]
    for row in ex["crawlers"]:
        assert set(cr["required"]) == set(row) and row["access"] in cr["properties"]["access"]["enum"] and row["role"] in cr["properties"]["role"]["enum"] and row["server"] in cr["properties"]["server"]["enum"]
    assert ex["summary"]["allowed"] == ex["summary"]["total"] - len(ex["summary"]["blocked"]) == sum(1 for r in ex["crawlers"] if r["access"] == "allowed")
    assert not any(w in json.dumps(ex).lower() for w in ("grade", "score"))
    assert set(s["components"]["schemas"]["Error"]["properties"]["error"]["properties"]["code"]["enum"]) == set(B.CODES)


def test_the_sample_is_a_real_dated_public_site_that_is_not_ours():
    ex = B.SAMPLE
    assert re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", ex["checked_at"]) and ex["site"] not in ("citedby.eu", "resaleiq.dev", "hexaciv.com", "civiqpass.com", "revalx.eu") and "citedby" not in ex["site"]


# ---- the docs page, five languages ----
LANGS = ["en", "fr", "nl", "de", "es"]


def path(lg): return "/ai-access-api" if lg == "en" else f"/{lg}/ai-access-api"


@pytest.mark.parametrize("lg", LANGS)
def test_the_docs_page_is_served_in_every_language_with_hreflang_the_spec_the_terms_and_the_example(lg):
    st, hd, b = req("GET", path(lg)); h = b.decode()
    assert st == 200 and f'<html lang="{lg}"' in h and f'<link rel="canonical" href="https://citedby.eu{path(lg)}">' in h and "noindex" not in h
    for l in LANGS: assert f'hreflang="{l}" href="https://citedby.eu{path(l)}"' in h
    assert 'hreflang="x-default" href="https://citedby.eu/ai-access-api"' in h
    assert 'href="/openapi.json"' in h and 'id="terms"' in h and 'curl &quot;https://citedby.eu/api/v1/ai-access?url=' + B.SAMPLE["site"] in h
    assert "<h1>" + B.E(B.T[lg]["h1"]) + "</h1>" in h and h.count("<h1>") == 1
    for f in B.FIELDS: assert f"<code>{f}</code>" in h, f
    for c in B.CODES + B.ACCESS: assert f"<code>{c}</code>" in h, c
    # the example is the stored real result, as JSON
    ex = re.search(r"<pre>(\{.*?)</pre>", h, re.S).group(1)
    import html as _h
    assert json.loads(_h.unescape(ex)) == B.SAMPLE
    assert f"{B.SAMPLE['site']}" in B.T[lg]["ex_p"].format(site=B.SAMPLE["site"], date=B.date_in(lg))


@pytest.mark.parametrize("lg", LANGS)
def test_the_docs_page_never_offers_a_grade_names_no_model_and_no_retired_product(lg):
    h = open(os.path.join(PUB, "ai-access-api.html" if lg == "en" else f"{lg}/ai-access-api.html"), encoding="utf-8").read()
    text = re.sub(r"(?s)<pre>.*?</pre>|<script.*?</script>", "", h)
    for w in ("Fix Pack", "€390", "recount", "Claude's engine", "an LLM", "A+", "letter grade"): assert w not in text, w
    assert "Anthropic" not in h and re.search(r"(?i)\bour (AI|model)\b", text) is None
    assert "30" in text and "12" in text and "6 " in text  # the limits are stated


def test_french_has_a_narrow_no_break_space_before_colons_in_its_text():
    h = open(os.path.join(PUB, "fr", "ai-access-api.html"), encoding="utf-8").read(); text = re.sub(r"(?s)<pre>.*?</pre>|<script.*?</script>|<style.*?</style>", "", h)
    assert not re.search(r"\S [:;?!]", text) and "\u202f:" in text


def test_the_page_matches_the_generator_so_a_hand_edit_or_a_stale_build_fails():
    for lg in LANGS:
        got = open(os.path.join(PUB, "ai-access-api.html" if lg == "en" else f"{lg}/ai-access-api.html"), encoding="utf-8").read()
        assert got == B.page(lg), lg
    assert open(os.path.join(PUB, "openapi.json"), encoding="utf-8").read() == json.dumps(B.openapi(), indent=2, ensure_ascii=False) + "\n"


def test_sitemap_llms_and_the_inbound_links_know_the_pages():
    sm = open(os.path.join(PUB, "sitemap.xml"), encoding="utf-8").read()
    for lg in LANGS: assert f"<loc>https://citedby.eu{path(lg)}</loc>" in sm
    assert sm.count("/ai-access-api</loc>") == 5
    assert "https://citedby.eu/ai-access-api" in open(os.path.join(PUB, "llms.txt"), encoding="utf-8").read()
    assert 'href="/ai-access-api"' in open(os.path.join(PUB, "mcp-server.html"), encoding="utf-8").read()


def test_the_counter_event_is_known_to_the_server():
    assert "api_ai_access" in server.EVENTS
