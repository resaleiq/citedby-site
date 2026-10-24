"""RES-3798 part 2: the MCP server at /mcp. Protocol shape, the four tools, errors, and what is not allowed (no stream, no big bodies).
Run: python3 -m pytest -q test_res3798_mcp.py"""
import http.client, json, os, tempfile, threading
from http.server import BaseHTTPRequestHandler, HTTPServer
os.environ.update(OPTIN_SECRET="x" * 40, BASE_URL="http://t", DATA_DIR=tempfile.mkdtemp())
import pytest
import mcp, proxy, server

srv = server.ThreadingHTTPServer(("127.0.0.1", 0), server.H)
threading.Thread(target=srv.serve_forever, daemon=True).start()
PORT = srv.server_port
SEEN = []


class FakeApp(BaseHTTPRequestHandler):
    reply = (200, {"text": "ok text", "data": {"k": 1}})

    def log_message(self, *a): pass

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        SEEN.append((self.path, body, self.headers.get("X-Forwarded-For")))
        code, j = FakeApp.reply; b = json.dumps(j).encode()
        self.send_response(code); self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)


fake = HTTPServer(("127.0.0.1", 0), FakeApp); threading.Thread(target=fake.serve_forever, daemon=True).start()


@pytest.fixture(autouse=True)
def app(monkeypatch):
    monkeypatch.setattr(proxy, "UPSTREAM", f"http://127.0.0.1:{fake.server_port}"); FakeApp.reply = (200, {"text": "ok text", "data": {"k": 1}}); SEEN.clear()


def req(method, path="/mcp", body=None, headers=None):
    c = http.client.HTTPConnection("127.0.0.1", PORT, timeout=20)
    try:
        c.request(method, path, body if body is None or isinstance(body, bytes) else json.dumps(body).encode(), headers or {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"})
        r = c.getresponse(); b = r.read()
        return r.status, {k.lower(): v for k, v in r.getheaders()}, b
    finally: c.close()


def rpc(method, params=None, id_=1):
    st, hd, b = req("POST", body={"jsonrpc": "2.0", "id": id_, "method": method, **({"params": params} if params is not None else {})})
    return st, hd, json.loads(b) if b else None


def test_initialize_negotiates_a_version_and_names_the_server():
    st, hd, j = rpc("initialize", {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "t", "version": "1"}})
    assert st == 200 and hd["content-type"].startswith("application/json") and hd["access-control-allow-origin"] == "*" and hd["cache-control"] == "no-store"
    r = j["result"]; assert r["protocolVersion"] == "2025-06-18" and r["serverInfo"]["name"] == "citedby" and r["capabilities"] == {"tools": {"listChanged": False}} and "free" in r["instructions"]
    assert rpc("initialize", {"protocolVersion": "1999-01-01"})[2]["result"]["protocolVersion"] == mcp.PROTOCOLS[0]


def test_tools_list_every_tool_is_read_only_and_described():
    j = rpc("tools/list")[2]; tools = j["result"]["tools"]
    assert [t["name"] for t in tools] == ["check_page", "check_ai_crawler_access", "check_llms_txt", "backlinks"]
    for t in tools:
        assert t["annotations"]["readOnlyHint"] is True and t["annotations"]["destructiveHint"] is False and len(t["description"]) > 80 and t["inputSchema"]["required"] and t["title"]


def test_notification_gets_202_and_no_body_and_ping_works():
    st, _, b = req("POST", body={"jsonrpc": "2.0", "method": "notifications/initialized"}); assert (st, b) == (202, b"")
    assert rpc("ping")[2]["result"] == {}


def test_errors_are_json_rpc_errors():
    assert rpc("nope")[2]["error"]["code"] == -32601
    assert rpc("tools/call", {"name": "delete_everything", "arguments": {}})[2]["error"]["code"] == -32602
    st, _, b = req("POST", body=b"{not json"); assert st == 400 and json.loads(b)["error"]["code"] == -32700
    assert json.loads(req("POST", body=b'{"id":1,"method":"ping"}')[2])["error"]["code"] == -32600


def test_batch_returns_only_answers_to_requests():
    st, _, b = req("POST", body=[{"jsonrpc": "2.0", "id": 1, "method": "ping"}, {"jsonrpc": "2.0", "method": "notifications/initialized"}])
    assert st == 200 and [x["id"] for x in json.loads(b)] == [1]


def test_app_tools_go_to_the_app_with_the_callers_address_and_return_text_and_data():
    for name, key, tool in (("check_page", "url", "page"), ("check_ai_crawler_access", "site", "crawlers"), ("check_llms_txt", "site", "llms")):
        SEEN.clear()
        r = rpc("tools/call", {"name": name, "arguments": {key: "https://acme.example/x"}})[2]["result"]
        assert r["content"][0] == {"type": "text", "text": "ok text"} and r["structuredContent"] == {"k": 1} and "isError" not in r
        assert SEEN == [("/internal/mcp-tool", {"tool": tool, "target": "https://acme.example/x"}, "127.0.0.1")], name


def test_app_errors_and_an_unreachable_app_are_tool_errors_not_crashes(monkeypatch):
    FakeApp.reply = (200, {"error": "robots.txt disallows CitedBot"}); r = rpc("tools/call", {"name": "check_page", "arguments": {"url": "https://a.example/"}})[2]["result"]
    assert r["isError"] is True and "disallows" in r["content"][0]["text"] and "structuredContent" not in r
    FakeApp.reply = (429, {"error": "Too many checks"}); assert "Too many" in rpc("tools/call", {"name": "check_page", "arguments": {"url": "https://a.example/"}})[2]["result"]["content"][0]["text"]
    monkeypatch.setattr(proxy, "UPSTREAM", "http://127.0.0.1:9"); r = rpc("tools/call", {"name": "check_page", "arguments": {"url": "https://a.example/"}})[2]["result"]
    assert r["isError"] is True and "did not answer" in r["content"][0]["text"]
    monkeypatch.setattr(proxy, "UPSTREAM", ""); assert rpc("tools/call", {"name": "check_page", "arguments": {"url": "x"}})[2]["result"]["isError"] is True
    FakeApp.reply = (200, {"text": "ok text", "data": {"k": 1}}); monkeypatch.setattr(proxy, "UPSTREAM", f"http://127.0.0.1:{fake.server_port}"); assert rpc("tools/call", {"name": "check_page", "arguments": "not a dict"})[2]["result"]["content"][0]["text"] == "ok text" and SEEN[-1][1]["target"] == ""  # arguments that are not an object are an empty target, not an exception


def test_backlinks_reads_the_open_data_and_leaves_adult_and_gambling_names_out():
    r = rpc("tools/call", {"name": "backlinks", "arguments": {"domain": "https://www.Semrush.com/pricing"}})[2]["result"]
    d = r["structuredContent"]
    assert d["in_data"] is True and d["domain"] == "semrush.com" and d["referring_domains"] > 100 and 0 < len(d["referrers"]) <= 20 and "Common Crawl" in r["content"][0]["text"] and "citedby.eu/backlinks/semrush.com" in r["content"][0]["text"]
    assert not any(mcp.backlinks.LINK_DENY.search(x["domain"]) for x in d["referrers"]) and d["referrers"][0]["rank"] == 1
    assert SEEN == []  # answered here, no app call


def test_backlinks_domain_outside_the_data_says_what_is_covered_and_bad_input_is_an_error():
    r = rpc("tools/call", {"name": "backlinks", "arguments": {"domain": "tiny-shop-that-is-not-there.example"}})[2]["result"]
    assert r["structuredContent"]["in_data"] is False and "100 or more referring domains" in r["content"][0]["text"] and "says nothing about how many links" in r["content"][0]["text"] and "isError" not in r
    assert rpc("tools/call", {"name": "backlinks", "arguments": {"domain": "not a domain"}})[2]["result"]["isError"] is True
    assert rpc("tools/call", {"name": "backlinks", "arguments": {}})[2]["result"]["isError"] is True


def test_get_is_405_for_a_client_a_redirect_for_a_browser_and_options_answers_cors():
    st, hd, b = req("GET", headers={"Accept": "text/event-stream"}); assert st == 405 and hd["allow"] == "POST, OPTIONS" and "POST" in json.loads(b)["error"]
    st, hd, _ = req("GET", headers={"Accept": "text/html,application/xhtml+xml"}); assert st == 302 and hd["location"] == "/mcp-server"
    st, hd, _ = req("OPTIONS", headers={"Origin": "https://x.example", "Access-Control-Request-Method": "POST"}); assert st == 204 and "Content-Type" in hd["access-control-allow-headers"] and "POST" in hd["access-control-allow-methods"]
    assert req("OPTIONS", "/other")[0] == 404


def test_oversize_body_is_refused_before_reading():
    assert req("POST", body=b"x" * 20000)[0] == 413


def test_a_denied_name_is_left_out_and_counted(monkeypatch):
    monkeypatch.setattr(mcp.backlinks, "split", lambda h: (7, [(1, "nytimes.com", 5), (2, "best-casino-bonus.example", 4), (3, "wikipedia.org", 3)], ["google.com"]))
    r = rpc("tools/call", {"name": "backlinks", "arguments": {"domain": "acme.example"}})[2]["result"]
    d = r["structuredContent"]; assert [x["domain"] for x in d["referrers"]] == ["nytimes.com", "wikipedia.org"] and d["omitted_by_name"] == 1 and "casino" not in r["content"][0]["text"] and "left out" in r["content"][0]["text"]


def test_registry_auth_file_and_the_docs_page_are_served():
    st, hd, b = req("GET", "/.well-known/mcp-registry-auth", headers={}); assert st == 200 and b.decode().startswith("v=MCPv1; k=ed25519; p=") and len(b.decode().split("p=")[1].strip()) == 44
    st, hd, b = req("GET", "/mcp-server", headers={}); t = b.decode()
    assert st == 200 and "<h1>CitedBy in your AI tools</h1>" in t and "https://citedby.eu/mcp" in t and 'rel="canonical" href="https://citedby.eu/mcp-server"' in t
    for tool in [x["name"] for x in mcp.TOOLS]: assert f"<code>{tool}</code>" in t, tool       # the page lists exactly the tools the server serves
    assert "claude mcp add --transport http citedby https://citedby.eu/mcp" in t and "codex mcp add citedby --url https://citedby.eu/mcp" in t
    import base64; assert json.loads(base64.b64decode(t.split("config=")[1].split('"')[0].replace("&amp;", "&"))) == {"url": "https://citedby.eu/mcp"}


def test_llms_txt_and_sitemap_list_the_page_and_bot_page_names_the_new_way_it_is_used():
    base = os.path.join(os.path.dirname(__file__), "public")
    assert "https://citedby.eu/mcp-server" in open(os.path.join(base, "llms.txt")).read() and "<loc>https://citedby.eu/mcp-server</loc>" in open(os.path.join(base, "sitemap.xml")).read()
    assert 'href="/mcp-server"' in open(os.path.join(base, "bot.html")).read()
