"""RES-3940 F2: a sign-in, reset or trial-cancel token in the page path never reaches PostHog.
`/login/<token>` answers 200 with riq-a.js, and riq-a.js sends $pathname, $current_url and the next page's $referrer: the token was still valid when PostHog got it.
These tests run the real public/riq-a.js in node, and the relay that forwards its body."""
import json, os, shutil, subprocess
import pytest
import analytics

ROOT = os.path.dirname(os.path.abspath(__file__))
NODE = shutil.which("node") or os.path.expanduser("~/.hermes/node/bin/node")
needs_node = pytest.mark.skipif(not os.path.exists(NODE), reason="node is not installed on this machine")
TOKEN = "AAAAbbbbCCCC1234_-zzzz"
SUB = "sub_1QqXyZ.deadbeef0123"

HARNESS = r"""
const fs = require("fs"), vm = require("vm");
const cfg = JSON.parse(process.argv[1]), src = fs.readFileSync(process.argv[2], "utf8"), sent = [];
const attrs = { "data-key": "phc_test", "data-site": "citedby", "data-endpoint": "/riq-e" };
const sandbox = {
  document: { currentScript: { getAttribute: (n) => (attrs[n] === undefined ? null : attrs[n]) }, referrer: cfg.referrer || "", cookie: "", readyState: "complete",
              querySelector: () => null, addEventListener() {} },
  navigator: { userAgent: "UA", language: "en", doNotTrack: null },
  location: { search: cfg.search || "", hostname: "citedby.eu", host: "citedby.eu", pathname: cfg.path, origin: "https://citedby.eu", href: "https://citedby.eu" + cfg.path },
  localStorage: { getItem: () => null, setItem() {} }, screen: { width: 390, height: 844 }, innerWidth: 390, innerHeight: 844, history: { pushState() {}, replaceState() {} }, addEventListener() {},
  Intl, URL, URLSearchParams, JSON, Object, String, Date, Promise,
  fetch: (url, init) => { sent.push(JSON.parse(init.body).properties); return Promise.resolve({ ok: true }); },
};
sandbox.window = sandbox; vm.createContext(sandbox); vm.runInContext(src, sandbox);
console.log(JSON.stringify(sent));
"""


def props(path, referrer="", search=""):
    out = subprocess.run([NODE, "-e", HARNESS, json.dumps({"path": path, "referrer": referrer, "search": search}), os.path.join(ROOT, "public", "riq-a.js")], capture_output=True, text=True, timeout=60)
    assert out.returncode == 0, out.stderr
    return json.loads(out.stdout.strip().splitlines()[-1])[0]


CASES = [("/login/" + TOKEN, "/login/:token"), ("/reset/" + TOKEN, "/reset/:token"), ("/trial/cancel/" + SUB, "/trial/cancel/:token"),
         ("/start/" + TOKEN, "/start/:token"), ("/recount/" + TOKEN, "/recount/:token"), ("/report/" + TOKEN, "/report/:token"),
         ("/r/" + TOKEN, "/r/:token"), ("/r/os/" + TOKEN, "/r/os/:token"), ("/t/" + TOKEN, "/t/:token"),
         ("/fr/login/" + TOKEN, "/fr/login/:token"), ("/report/" + TOKEN + "/csv", "/report/:token/csv")]


@needs_node
@pytest.mark.parametrize("path,want", CASES)
def test_the_token_segment_is_replaced_in_pathname_current_url_and_referrer(path, want):
    p = props(path, referrer="https://citedby.eu" + path + "?x=1")
    assert p["$pathname"] == want and p["$current_url"] == "https://citedby.eu" + want and p["$referrer"] == "https://citedby.eu" + want
    assert TOKEN not in json.dumps(p) and "deadbeef" not in json.dumps(p) and "sub_1Qq" not in json.dumps(p)


@needs_node
def test_ordinary_paths_and_other_sites_referrers_are_sent_unchanged():
    p = props("/plans", referrer="https://www.google.com/search?q=x")
    assert p["$pathname"] == "/plans" and p["$current_url"] == "https://citedby.eu/plans" and p["$referrer"] == "https://www.google.com/search"
    assert props("/tools/ai-crawler-check/shop.eu")["$pathname"] == "/tools/ai-crawler-check/shop.eu"
    assert props("/login")["$pathname"] == "/login" and props("/blog/the-t-shirt-guide")["$pathname"] == "/blog/the-t-shirt-guide"


def test_the_tag_version_moved_so_cached_copies_of_the_old_script_are_replaced():
    assert b"riq-a.js?v=8" in analytics.TAG


def test_the_relay_scrubs_an_old_cached_script_too(monkeypatch):
    sent = []
    class R:
        def read(self): return b""
    monkeypatch.setattr(analytics.urllib.request, "urlopen", lambda req, timeout=0: sent.append(req.data) or R())
    class T:
        def __init__(self, target=None, daemon=None): self.t = target
        def start(self): self.t()
    monkeypatch.setattr(analytics.threading, "Thread", T)
    body = {"api_key": "k", "event": "$pageview", "properties": {"$pathname": "/login/" + TOKEN, "$current_url": "https://citedby.eu/login/" + TOKEN, "$referrer": "https://citedby.eu/trial/cancel/" + SUB, "$host": "citedby.eu"}}
    analytics.relay(json.dumps(body).encode(), "1.2.3.4", "ua")
    got = json.loads(sent[0])["properties"]
    assert got["$pathname"] == "/login/:token" and got["$referrer"] == "https://citedby.eu/trial/cancel/:token" and TOKEN not in sent[0].decode() and "deadbeef" not in sent[0].decode()
    analytics.relay(b"not json", "1.2.3.4", "ua")  # forwarded untouched, never raises
    assert sent[1] == b"not json"
