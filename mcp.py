"""RES-3798 part 2: CitedBy's MCP server at https://citedby.eu/mcp (MCP Streamable HTTP, JSON replies, no sessions, no sign-in).
Four read-only tools: one page's check, a site's AI-crawler access, its llms.txt, and a domain's referring domains (Common Crawl open data). The first three run in the app
(POST /internal/mcp-tool: CitedBot, robots.txt first, per-IP cap there); the fourth reads backlinks.sqlite here. Nothing writes, nothing signs a person in, no assistant call is spent."""
import json, os, urllib.error, urllib.request

import backlinks, proxy

SERVER = {"name": "citedby", "title": "CitedBy", "version": "1.0.0", "websiteUrl": "https://citedby.eu/mcp-server"}
PROTOCOLS = ("2025-11-25", "2025-06-18", "2025-03-26", "2024-11-05")
INSTRUCTIONS = ("CitedBy checks whether a website can be found and cited by AI assistants and search engines. Every tool is read-only and free. "
                "check_page fetches one page as CitedBot (robots.txt respected) and lists what to fix, with the fix. check_ai_crawler_access says which AI crawlers a site lets in. "
                "check_llms_txt reads /llms.txt. backlinks lists the domains that link to a site, from Common Crawl open data. A whole-site audit with every page needs a plan at https://citedby.eu/plans.")
ANN = {"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
TOOLS = [
    {"name": "check_page", "title": "Check one page for AI-search and SEO problems", "annotations": {**ANN, "title": "Check one page"},
     "description": "Fetch one public web page as CitedBot (robots.txt respected) and return what is wrong with it for AI answers and search: title, description, headings, structured data, canonical, language, links and more. Each finding has why it matters and the exact fix. Deterministic checks only; says so when the page cannot be fetched.",
     "inputSchema": {"type": "object", "properties": {"url": {"type": "string", "description": "Full page address, for example https://example.com/pricing"}}, "required": ["url"], "additionalProperties": False}},
    {"name": "check_ai_crawler_access", "title": "Which AI crawlers can read this site", "annotations": {**ANN, "title": "AI crawler access"},
     "description": "Read a site's robots.txt and test the server for GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot. Returns, per crawler, whether robots.txt allows it and whether the server answers it, so you can see who is blocked and by what.",
     "inputSchema": {"type": "object", "properties": {"site": {"type": "string", "description": "Domain or address of the site, for example example.com"}}, "required": ["site"], "additionalProperties": False}},
    {"name": "check_llms_txt", "title": "Check a site's llms.txt", "annotations": {**ANN, "title": "llms.txt check"},
     "description": "Fetch /llms.txt of a site and report whether it exists, whether its links work, and whether /llms-full.txt exists. When there is none, the full report holds a draft built from the site's own pages.",
     "inputSchema": {"type": "object", "properties": {"site": {"type": "string", "description": "Domain or address of the site, for example example.com"}}, "required": ["site"], "additionalProperties": False}},
    {"name": "backlinks", "title": "Referring domains of a domain (open data)", "annotations": {**ANN, "title": "Referring domains", "openWorldHint": False},
     "description": "How many other domains link to a domain, and the strongest referrers, from the Common Crawl domain web graph. Covers domains with 100 or more referring domains under .eu, EU and UK country domains, plus the 5,000 most-linked sites; says plainly when a domain is not in the data.",
     "inputSchema": {"type": "object", "properties": {"domain": {"type": "string", "description": "Domain, for example example.com"}}, "required": ["domain"], "additionalProperties": False}},
]
APP_TOOL = {"check_page": ("page", "url"), "check_ai_crawler_access": ("crawlers", "site"), "check_llms_txt": ("llms", "site")}
LISTED = 20


def _err(id_, code, msg): return {"jsonrpc": "2.0", "id": id_, "error": {"code": code, "message": msg}}


def _result(text, data=None, error=False):
    r = {"content": [{"type": "text", "text": text}]}
    if data is not None: r["structuredContent"] = data
    if error: r["isError"] = True
    return r


def _app(tool, target, ip):
    if not proxy.UPSTREAM: return _result("CitedBy's checker is not available right now. Try again later.", error=True)
    req = urllib.request.Request(proxy.UPSTREAM + "/internal/mcp-tool", json.dumps({"tool": tool, "target": target}).encode(), {"Content-Type": "application/json", "X-Forwarded-For": ip}, method="POST")
    try:
        code, _, body = proxy._call(req, 45)
        j = json.loads(body)
    except (urllib.error.URLError, OSError, ValueError):
        return _result("CitedBy's checker did not answer in time. Try again in a minute.", error=True)
    if code == 429: return _result(j.get("error") or "Too many checks from this address. Try again later.", error=True)
    if j.get("error") or not j.get("text"): return _result(j.get("error") or "The check failed. Try again in a minute.", error=True)
    return _result(j["text"], j.get("data"))


def _backlinks(domain):
    h = backlinks.norm(domain)
    if not h: return _result("That is not a domain address. Pass a domain such as example.com.", error=True)
    if not os.path.exists(backlinks.DB): return _result("The backlink data is not available right now. Try again later.", error=True)
    m, url = backlinks.meta(), f"https://citedby.eu/backlinks/{h}"
    got = backlinks.split(h)
    src = f"Common Crawl domain web graph {backlinks.GRAPH}, read {m.get('read_on')}"
    if got is None:
        full = backlinks.full_info()
        base = f"{h} is not in the data. It covers domains with 100 or more referring domains under .eu, EU and UK country domains" + (f" ({full['n']:,} domains)" if full else "") + f" and the most-linked sites; that says nothing about how many links {h} has."
        return _result(base + f"\nSource: {src}.", {"domain": h, "in_data": False, "source": src})
    n, rows, folded = got
    shown = [r for r in rows if not backlinks.LINK_DENY.search(r[1])][:LISTED]
    cut = len(rows) - len([r for r in rows if not backlinks.LINK_DENY.search(r[1])])
    lines = [f"{h} has {n:,} referring domain(s) in the {src}." + ("" if shown else " No referrers are listed for it.") + (" New or small sites are often missing from the graph; it does not mean you have none." if n == 0 else "")]
    lines += [f"{rank}. {ref} (itself linked from {inl:,} domains)" for rank, ref, inl in shown]
    if cut: lines.append(f"({cut} referrer(s) with adult- or gambling-looking names are left out of the list.)")
    if folded: lines.append("Referrers common to most sites in the set (folded): " + ", ".join(folded) + ".")
    lines.append(f"Method and the page for this domain: {url}\nAudit the site itself, free for one page: https://citedby.eu/?url={h}&utm_source=mcp&utm_medium=assistant&utm_campaign=mcp_server")
    return _result("\n".join(lines), {"domain": h, "in_data": True, "referring_domains": n, "referrers": [{"rank": r, "domain": d, "domains_linking_to_referrer": i} for r, d, i in shown], "omitted_by_name": cut, "folded_common_referrers": list(folded or []), "source": src, "page": url})


def call_tool(name, args, ip):
    if not isinstance(args, dict): args = {}
    if name == "backlinks": return _backlinks(str(args.get("domain", ""))[:300])
    tool, key = APP_TOOL[name]
    return _app(tool, str(args.get(key, ""))[:2048], ip)


def rpc(msg, ip):
    """One JSON-RPC message -> a response dict, or None for a notification."""
    if not isinstance(msg, dict) or msg.get("jsonrpc") != "2.0" or not isinstance(msg.get("method"), str): return _err(msg.get("id") if isinstance(msg, dict) else None, -32600, "Invalid request")
    method, id_, p = msg["method"], msg.get("id"), msg.get("params") if isinstance(msg.get("params"), dict) else {}
    if "id" not in msg: return None  # a notification (notifications/initialized, notifications/cancelled ...): no reply
    if method == "initialize":
        want = p.get("protocolVersion")
        return {"jsonrpc": "2.0", "id": id_, "result": {"protocolVersion": want if want in PROTOCOLS else PROTOCOLS[0], "capabilities": {"tools": {"listChanged": False}}, "serverInfo": SERVER, "instructions": INSTRUCTIONS}}
    if method == "ping": return {"jsonrpc": "2.0", "id": id_, "result": {}}
    if method == "tools/list": return {"jsonrpc": "2.0", "id": id_, "result": {"tools": TOOLS}}
    if method == "tools/call":
        name = p.get("name")
        if name not in {t["name"] for t in TOOLS}: return _err(id_, -32602, f"Unknown tool: {str(name)[:60]}")
        return {"jsonrpc": "2.0", "id": id_, "result": call_tool(name, p.get("arguments"), ip)}
    return _err(id_, -32601, "Method not found")


def handle(raw, ip):
    """POST /mcp body -> (status, response bytes). 202 and no body when the message was only notifications."""
    try: msg = json.loads(raw.decode("utf-8"))
    except (ValueError, UnicodeDecodeError): return 400, json.dumps(_err(None, -32700, "Parse error")).encode()
    if isinstance(msg, list):
        out = [r for r in (rpc(m, ip) for m in msg[:10]) if r is not None]
        return (200, json.dumps(out).encode()) if out else (202, b"")
    r = rpc(msg, ip)
    return (200, json.dumps(r).encode()) if r is not None else (202, b"")
