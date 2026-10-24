#!/usr/bin/env python3
"""tools/verify_directory.py [dir] (RES-4194): for each data/directory/crawlers/<slug>.json, re-fetch vendor_quote_source.url and check the quote is in the raw page text; for ips.kind json_list re-count prefixes.
Exit 1 if any fails. Known limit: a vendor page rendered by JavaScript (bingbot) cannot be read by curl and fails; markup that puts a space before punctuation (handled by norm()). Fetch with a plain research UA."""
import json, sys, os, re, html, urllib.request, glob
UA = "CitedBy-research/1.0 (+https://citedby.eu/bot)"
def get(url):
    r = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    return urllib.request.urlopen(r, timeout=40).read().decode("utf-8", "replace")
def norm(s):
    s = re.sub(r"<(script|style)\b.*?</\1>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<[^>]+>", " ", s); s = html.unescape(s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace(" ", " ").replace("‑", "-").replace("–", "-").replace("—", "-")
    s = re.sub(r"\s+", " ", s).strip().lower()
    return re.sub(r" ([.,;:)!?])", r"\1", re.sub(r"\( ", "(", s))  # markup around links leaves a space before punctuation
def count(j):
    n = 0
    def walk(x):
        nonlocal n
        if isinstance(x, dict):
            if any(k in x for k in ("ipv4Prefix", "ipv6Prefix", "ip_prefix", "ipv6_prefix", "cidr")): n += 1; return
            for v in x.values(): walk(v)
        elif isinstance(x, list):
            for v in x:
                if isinstance(v, str) and re.match(r"[0-9a-fA-F:.]+(/\d+)?$", v): n += 1
                else: walk(v)
    walk(j); return n
bad = 0
DIR = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "directory", "crawlers")
for p in sorted(glob.glob(os.path.join(DIR, "*.json"))):
    d = json.load(open(p)); slug = d.get("slug", os.path.basename(p)); msgs = []
    srcs = d.get("quotes") or ([{"quote": d["vendor_quote"], "url": d["vendor_quote_source"]["url"]}] if d.get("vendor_quote") else [])
    for q in srcs:
        try:
            ok = norm(q["quote"]) in norm(get(q["url"]))
        except Exception as e: ok = False; msgs.append("fetch %s: %s" % (q["url"], e))
        if not ok: msgs.append("QUOTE NOT FOUND in %s: %.70s" % (q["url"], q["quote"]))
    ips = d.get("ips") or {}
    if ips.get("kind") == "json_list" and ips.get("url"):
        try:
            n = count(json.loads(get(ips["url"])))
            if n != ips.get("count"): msgs.append("IP COUNT file %d vs data %s" % (n, ips.get("count")))
        except Exception as e: msgs.append("ips fetch: %s" % e)
    print(("FAIL " if msgs else "ok   ") + slug + ("  " + " | ".join(msgs) if msgs else ""))
    bad += bool(msgs)
sys.exit(1 if bad else 0)
