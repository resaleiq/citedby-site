"""RES-1071: cookieless PostHog (EU). The public/riq-a.js client sets no cookies and uses no storage; the project key is public by design.
POSTHOG_KEY="" switches the tag off (rollback without a redeploy of code)."""
import json, os, re, threading, urllib.request

KEY = os.environ.get("POSTHOG_KEY", "phc_r2uexPGqx2dCYjsFKnevTB8rf8Ez9B6twoMXcfFceHzD")
TAG = ('<script src="/riq-a.js?v=7" data-key="%s" data-site="citedby" data-endpoint="/riq-e" defer></script>' % KEY).encode()  # v changes with the script: it is served with max-age=604800


def inject(body):
    """Add the tag before </head> of an HTML page (or before <body> when the head is implied); fragments, or pages with the tag already, pass through."""
    if not KEY or TAG in body:
        return body
    if b"</head>" in body:
        return body.replace(b"</head>", TAG + b"</head>", 1)
    i = body.find(b"<body")  # RES-2130: the landing and app pages have no explicit </head> (implied head); a deferred script before <body> is valid there. Fragments stay untouched.
    if i < 0 or b"<html" not in body[:400].lower():
        return body
    return body[:i] + TAG + body[i:]


UPSTREAM = "https://eu.i.posthog.com/i/v0/e/"
TOKEN_PATH = re.compile(r"^((?:/(?:fr|de|es|nl))?/(?:login|reset|start|recount|report|t|r/os|r|trial/cancel))/[^/]+")  # RES-3940 F2: same list as riq-a.js; a copy of the script cached for a week may still send the token


def scrub(raw):
    """Replace a token path segment in $pathname, $current_url and $referrer; a body that is not a capture object passes through untouched."""
    try:
        d = json.loads(raw)
        p = d["properties"]
        for k in ("$pathname", "$current_url", "$referrer"):
            if isinstance(p.get(k), str):
                p[k] = re.sub(r"^(https?://[^/]+)(/.*)$", lambda m: m.group(1) + TOKEN_PATH.sub(r"\1/:token", m.group(2)), p[k]) if p[k].startswith("http") else TOKEN_PATH.sub(r"\1/:token", p[k])
        return json.dumps(d).encode()
    except (ValueError, KeyError, TypeError, AttributeError):
        return raw


def relay(raw, ip, ua):
    """Forward one capture body to PostHog in the background (the page never waits). The client IP goes in X-Forwarded-For for PostHog's daily cookieless hash; nothing is stored here."""
    raw = scrub(raw)

    def go():
        try:
            req = urllib.request.Request(UPSTREAM, raw, {"Content-Type": "text/plain", "X-Forwarded-For": ip, "User-Agent": ua or "riq-relay"}, method="POST")
            urllib.request.urlopen(req, timeout=5).read()
        except Exception:
            pass
    if KEY and 0 < len(raw) <= 8192:
        threading.Thread(target=go, daemon=True).start()
