"""RES-4201: riq-a.js tags events from automated browsers (navigator.webdriver true) with automation:true, and keeps sending them."""
import json, os, shutil, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
JS = os.path.join(HERE, "public", "riq-a.js")
RUNNER = r"""
const fs = require("fs"), vm = require("vm");
const [file, webdriver] = [process.argv[1], process.argv[2]];
const sent = [];
const nav = { userAgent: "t", language: "en", doNotTrack: null };
if (webdriver !== "absent") nav.webdriver = webdriver === "true";
const loc = { search: "", host: "x.test", pathname: "/p", origin: "https://x.test", href: "https://x.test/p", hostname: "x.test" };
const script = { getAttribute: (k) => ({ "data-key": "phc_x", "data-site": "citedby", "data-endpoint": "/riq-e" }[k]) };
const ctx = { navigator: nav, location: loc, screen: { width: 1, height: 1 }, innerWidth: 1, innerHeight: 1, history: {}, URLSearchParams, URL, Date, JSON, Intl,
  document: { currentScript: script, cookie: "", referrer: "", readyState: "complete", querySelector: () => null, addEventListener() {} }, addEventListener() {}, localStorage: { getItem: () => null },
  fetch: (u, o) => { sent.push(JSON.parse(o.body)); return Promise.resolve({ ok: true }); } };
ctx.window = ctx;
vm.runInNewContext(fs.readFileSync(file, "utf8"), ctx);
ctx.riq("checkout_started", { via: "t" });
console.log(JSON.stringify(sent.map((s) => ({ event: s.event, automation: s.properties.automation, has: "automation" in s.properties }))));
"""


def run(webdriver):
    node = shutil.which("node")
    assert node, "node is required for this test"
    out = subprocess.run([node, "-e", RUNNER, JS, webdriver], capture_output=True, text=True, timeout=30)
    assert out.returncode == 0, out.stderr
    return json.loads(out.stdout)


def test_webdriver_true_tags_every_event_and_still_sends():
    ev = run("true")
    assert [e["event"] for e in ev] == ["$pageview", "checkout_started"]  # still sent: QA checks that assert an event fires keep passing
    assert all(e["automation"] is True for e in ev)


def test_human_browser_has_no_automation_property():
    for wd in ("false", "absent"):
        ev = run(wd)
        assert [e["event"] for e in ev] == ["$pageview", "checkout_started"]
        assert not any(e["has"] for e in ev), wd
