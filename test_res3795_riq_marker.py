"""RES-3795 F3: a server-rendered result page counts as a started check without running any inline script.
The tool pages send `script-src 'self'`, so the page cannot call window.riq itself: it marks its <main data-riq-event=... data-riq-kind=...> and public/riq-a.js sends the event.
These tests run the real public/riq-a.js in node against stubbed browser globals and read what it would POST to the same-origin relay."""
import json, os, shutil, subprocess
import pytest
import analytics

ROOT = os.path.dirname(os.path.abspath(__file__))
NODE = shutil.which("node") or os.path.expanduser("~/.hermes/node/bin/node")
pytestmark = pytest.mark.skipif(not os.path.exists(NODE), reason="node is not installed on this machine")

HARNESS = r"""
const fs = require("fs"), vm = require("vm");
const cfg = JSON.parse(process.argv[1]);  // node -e: argv[0] is node, the extra arguments follow
const src = fs.readFileSync(process.argv[2], "utf8");
const sent = [], docListeners = {}, store = cfg.internal ? { riq_internal: "1" } : {};  // a browser that opened ?internal=1 once keeps the flag
const attrs = { "data-key": "phc_test", "data-site": "citedby", "data-endpoint": "/riq-e" };
const marker = cfg.marker === undefined ? null : { getAttribute: (n) => (cfg.marker[n] === undefined ? null : cfg.marker[n]) };
const sandbox = {
  document: { currentScript: { getAttribute: (n) => (attrs[n] === undefined ? null : attrs[n]) }, referrer: "", cookie: "", readyState: cfg.readyState || "complete",
              querySelector: (sel) => (sel === "[data-riq-event]" ? marker : null), addEventListener: (t, f) => { (docListeners[t] = docListeners[t] || []).push(f); } },
  navigator: { userAgent: "UA", language: "en", doNotTrack: cfg.dnt ? "1" : null },
  location: { search: cfg.search || "", hostname: "citedby.eu", host: "citedby.eu", pathname: cfg.path || "/tools/ai-crawler-check/shop.eu", origin: "https://citedby.eu", href: "https://citedby.eu/" },
  localStorage: { getItem: (k) => (k in store ? store[k] : null), setItem: (k, v) => { store[k] = String(v); } },
  screen: { width: 390, height: 844 }, innerWidth: 390, innerHeight: 844, history: { pushState() {}, replaceState() {} }, addEventListener() {},
  Intl, URL, URLSearchParams, JSON, Object, String, Date, Promise,
  fetch: (url, init) => { sent.push({ url, body: JSON.parse(init.body) }); return Promise.resolve({ ok: true }); },
};
sandbox.window = sandbox;
vm.createContext(sandbox);
vm.runInContext(src, sandbox);
if (cfg.fireDomReady) (docListeners.DOMContentLoaded || []).forEach((f) => f());
const before = sent.map((s) => s.body.event);
console.log(JSON.stringify({ events: sent.map((s) => ({ event: s.body.event, kind: s.body.properties.kind, url: s.url, site: s.body.properties.site, path: s.body.properties.$pathname })), beforeDomReady: before }));
"""


def run(**cfg):
    out = subprocess.run([NODE, "-e", HARNESS, json.dumps(cfg), os.path.join(ROOT, "public", "riq-a.js")], capture_output=True, text=True, timeout=60)
    assert out.returncode == 0, out.stderr
    return json.loads(out.stdout.strip().splitlines()[-1])


def test_a_marked_result_page_sends_check_started_with_its_kind_after_the_pageview():
    r = run(marker={"data-riq-event": "check_started", "data-riq-kind": "crawlers"})
    assert [(e["event"], e.get("kind")) for e in r["events"]] == [("$pageview", None), ("check_started", "crawlers")]
    assert all(e["url"] == "/riq-e" and e["site"] == "citedby" and e["path"] == "/tools/ai-crawler-check/shop.eu" for e in r["events"])  # same-origin relay, path only


def test_a_page_without_the_marker_sends_only_the_pageview():
    assert [e["event"] for e in run()["events"]] == ["$pageview"]


def test_a_marker_can_only_send_the_free_check_events():
    """A marker fires on every view and every refresh, so it must never be able to send a money or sign-up event (those come from the server or a real click)."""
    for ok in ("check_started", "check_finished"):
        assert [e["event"] for e in run(marker={"data-riq-event": ok, "data-riq-kind": "x"})["events"]] == ["$pageview", ok]
    for bad in ("paid", "checkout_started", "checkout_completed", "signup", "cta_click", "mock_started", "evil_event", "$pageview", "constructor", "__proto__", "toString", ""):
        assert [e["event"] for e in run(marker={"data-riq-event": bad, "data-riq-kind": "x"})["events"]] == ["$pageview"], bad


def test_internal_browsers_and_do_not_track_send_nothing_for_the_marker_either():
    m = {"data-riq-event": "check_started", "data-riq-kind": "crawlers"}
    assert run(marker=m, internal=True)["events"] == [] and run(marker=m, dnt=True)["events"] == [] and run(marker=m, search="?internal=1")["events"] == []


def test_a_script_that_runs_before_the_page_is_parsed_waits_for_it():
    m = {"data-riq-event": "check_started", "data-riq-kind": "llms"}
    r = run(marker=m, readyState="loading", fireDomReady=True)
    assert [(e["event"], e.get("kind")) for e in r["events"]] == [("$pageview", None), ("check_started", "llms")] and r["beforeDomReady"] == ["$pageview", "check_started"]
    r = run(marker=m, readyState="loading")
    assert [e["event"] for e in r["events"]] == ["$pageview"]  # nothing until the DOM is ready


def test_the_kind_is_optional_and_capped():
    r = run(marker={"data-riq-event": "check_started"})
    assert r["events"][1]["event"] == "check_started" and r["events"][1].get("kind") is None
    assert len(run(marker={"data-riq-event": "check_started", "data-riq-kind": "k" * 200})["events"][1]["kind"]) == 80


def test_the_tag_carries_a_new_version_because_the_script_is_cached_for_a_week():
    """/riq-a.js is served with Cache-Control max-age=604800: a changed script under the old ?v=5 URL would not reach returning visitors."""
    assert b'src="/riq-a.js?v=7"' in analytics.TAG and b"?v=6" not in analytics.TAG
