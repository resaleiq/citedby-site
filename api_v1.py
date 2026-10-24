"""RES-4195: GET /api/v1/ai-access?url=<site>, the free public AI-access API. The check itself runs in the app (POST /internal/api-ai-access: CitedBot-style
fetches, SSRF guard, a 6-hour result store, per-IP caps); this front door adds the CORS headers, checks the parameter, passes the caller's address on and
counts a returned result. No key, no account, no grade."""
import json, urllib.error, urllib.request

import proxy

CORS = {"Access-Control-Allow-Origin": "*", "Access-Control-Expose-Headers": "Retry-After", "X-Robots-Tag": "noindex"}
PREFLIGHT = {**CORS, "Access-Control-Allow-Methods": "GET, HEAD, OPTIONS", "Access-Control-Allow-Headers": "Content-Type, Accept", "Access-Control-Max-Age": "86400"}
PATH = "/api/v1/ai-access"
KEEP = ("Retry-After",)


def _err(code, key, message):
    return code, json.dumps({"error": {"code": key, "message": message}}).encode(), {}


def call(raw, ip):
    """-> (http status, JSON bytes, extra headers). `raw` is the url parameter, or None when it is missing."""
    if raw is None or not raw.strip():
        return _err(400, "missing_url", "Pass the site as ?url=, for example /api/v1/ai-access?url=example.com.")
    if len(raw) > 2048:
        return _err(400, "bad_url", "The url parameter is longer than 2048 characters.")
    if not proxy.UPSTREAM:
        return _err(503, "unavailable", "The checker is not available right now. Try again later.")
    req = urllib.request.Request(proxy.UPSTREAM + "/internal/api-ai-access", json.dumps({"url": raw}).encode(), {"Content-Type": "application/json", "X-Forwarded-For": ip}, method="POST")
    try:
        code, headers, body = proxy._call(req, 45)
        json.loads(body)
    except (urllib.error.URLError, OSError, ValueError):
        return _err(502, "unavailable", "The checker did not answer in time. Try again in a minute.")
    return code, body, {k: headers[k] for k in KEEP if headers.get(k)}
