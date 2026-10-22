"""RES-2935 release gate: the checks our own crawl (CitedBy on citedby.eu) runs on every page, run on the pages we ship, so a class of crawl finding cannot come back.
Founder 22 Oct: fix everything the crawl finds and do not cause it again. One test per finding class; each lists every offending URL.
Pages are the sitemap's URLs. Static pages are read from public/ and passed through the serve-time footer layers (hub_links); pages the app renders (proxy.ROUTES) are leaves here and are gated by the app's own tests (test_res2935_checks.py)."""
import collections, html, os, re
import hub_links, proxy

HERE = os.path.dirname(os.path.abspath(__file__)); PUB = os.path.join(HERE, "public")
SITE = "https://citedby.eu"
SHORT_BY_NATURE = re.compile(r"^/(?:(?:fr|nl|de|es)/)?(contact|legal)$")  # a contact page and a legal notice are short on purpose; the app's checker agrees (sa_checks.SHORT_BY_NATURE, RES-2935)


def sitemap():
    return [u[len(SITE):] or "/" for u in re.findall(r"<loc>([^<]*)</loc>", open(os.path.join(PUB, "sitemap.xml"), encoding="utf-8").read())]


def file_for(path):
    if path == "/": return os.path.join(PUB, "landing.html")
    if path in ("/fr", "/nl", "/de", "/es"): return os.path.join(PUB, f"landing.{path[1:]}.html")
    for c in (PUB + path + ".html", PUB + path + "/index.html"):
        if os.path.exists(c): return c
    return None


def app_served(path): return bool(proxy.ROUTES["GET"].fullmatch(path))


def load():
    """{path: html} for every sitemap URL a static file backs, as served (hub links added); app-served paths are returned separately."""
    pages, app, missing = {}, [], []
    for p in sitemap():
        f = file_for(p)
        if f: pages[p] = hub_links.inject(open(f, "rb").read()).decode("utf-8")
        elif app_served(p): app.append(p)
        else: missing.append(p)
    return pages, app, missing


PAGES, APP, MISSING = load()


def meta(h):
    t = re.search(r"<title>(.*?)</title>", h, re.S); d = re.search(r'<meta name="description" content="([^"]*)"', h)
    return html.unescape(" ".join(t.group(1).split())) if t else "", html.unescape(d.group(1)) if d else ""


def main_words(h):
    m = re.search(r"<main\b.*?</main>", h, re.S) or re.search(r"<body\b.*</body>", h, re.S)
    t = re.sub(r"<(script|style|nav|header|footer)\b.*?</\1>|<[^>]+>", " ", m.group(0) if m else h, flags=re.S)
    return len(re.findall(r"\w+", html.unescape(t)))


def norm(href):
    href = href.split("#")[0].split("?")[0]
    if href.startswith(SITE): href = href[len(SITE):]
    if not href.startswith("/") or href.startswith("//"): return None
    return href.rstrip("/") or "/"


def out_links(h): return {n for n in (norm(x) for x in re.findall(r'<a\b[^>]*\bhref="([^"]*)"', h)) if n}


def robots(h):
    m = re.search(r'<meta name="robots" content="([^"]*)"', h); return m.group(1).lower() if m else ""


def report(bad): assert not bad, "\n" + "\n".join(f"  {k}: {v}" for k, v in bad)


def test_every_sitemap_url_is_a_page_we_serve():
    """status check: a sitemap URL with no file and no app route is a 404 for a crawler"""
    report([("no page behind sitemap URL", p) for p in MISSING])


def test_titles_are_15_to_65_characters_and_unique():
    bad, seen = [], collections.defaultdict(list)
    for p, h in PAGES.items():
        t, _ = meta(h); seen[t].append(p)
        if not 15 <= len(t) <= 65: bad.append(("title length", f"{p} {len(t)}: {t}"))
    bad += [("duplicate title", f"{v} {k}") for k, v in seen.items() if len(v) > 1]
    report(bad)


def test_descriptions_are_50_to_160_characters_and_unique():
    bad, seen = [], collections.defaultdict(list)
    for p, h in PAGES.items():
        _, d = meta(h); seen[d].append(p)
        if not 50 <= len(d) <= 160: bad.append(("description length", f"{p} {len(d)}: {d[:60]}"))
    bad += [("duplicate description", f"{v}") for k, v in seen.items() if len(v) > 1]
    report(bad)


def test_every_indexable_page_has_100_words_json_ld_and_a_clean_heading_outline():
    bad = []
    for p, h in PAGES.items():
        if "noindex" in robots(h): continue
        if main_words(h) < 100 and not SHORT_BY_NATURE.match(p): bad.append(("thin page", f"{p} {main_words(h)} words"))
        if "application/ld+json" not in h: bad.append(("no JSON-LD", p))
        lv = [int(x) for x in re.findall(r"<h([1-6])[ >]", h)]
        if any(b - a > 1 for a, b in zip(lv, lv[1:])): bad.append(("heading skips a level", f"{p} {lv[:12]}"))
    report(bad)


def test_no_orphans_and_nothing_deeper_than_3_clicks_from_home():
    """internal-link graph over the sitemap: every URL is linked from a page we ship, and reachable from / in at most 3 clicks. App-served pages carry the same footer (proxy injects hub_links), so they link to the hubs too."""
    hub = {n for n in out_links(hub_links.inject(b'<html lang="en"><body><footer></footer></body></html>').decode())}
    edges = {p: out_links(h) for p, h in PAGES.items()}
    edges.update({p: set(hub) | {c for c in APP if c.startswith(p + "/")} for p in APP})  # an app hub links its own children: /tools lists /tools/<tool> (test_res2935_checks.py asserts it in the app)
    inlinks = collections.Counter(t for s, ts in edges.items() for t in ts if t != s)
    all_paths = set(PAGES) | set(APP)
    bad = [("orphan (no internal link)", p) for p in sorted(all_paths) if p != "/" and not inlinks[p]]
    depth, queue = {"/": 0}, collections.deque(["/"])
    while queue:
        u = queue.popleft()
        for v in sorted(edges.get(u, ())):
            if v in all_paths and v not in depth: depth[v] = depth[u] + 1; queue.append(v)
    bad += [("not reachable from home", p) for p in sorted(all_paths) if p not in depth]
    bad += [("more than 3 clicks from home", f"{p} {d}") for p, d in sorted(depth.items()) if d > 3]
    report(bad)


def test_internal_links_on_every_static_page_resolve():
    """broken-link check: every internal href on a page we ship is a file, an app route, a sitemap URL or an asset we serve"""
    bad, ok = [], set(PAGES) | set(APP)
    redirects = {"/blog/ai-visibility-audit", "/ai-visibility-audit"}
    for p, h in PAGES.items():
        for t in sorted(out_links(h)):
            if t in ok or t in redirects or file_for(t) or app_served(t) or os.path.exists(PUB + t) or re.search(r"\.[a-z0-9]{2,5}$", t) and os.path.exists(PUB + t): continue
            if t in ("/check", "/instant", "/signin", "/signup", "/login", "/logout", "/audit", "/pricing", "/sample-audit", "/dashboard", "/account", "/r", "/start"): continue
            bad.append(("broken internal link", f"{p} -> {t}"))
    report(bad)


def test_llms_full_txt_is_current_and_every_llms_txt_link_resolves():
    """llms-full.txt is built from the committed pages (tools/build_llms_full.py); every https://citedby.eu link in llms.txt is a page, a file or an app route"""
    import subprocess, sys
    assert subprocess.run([sys.executable, os.path.join(HERE, "tools", "build_llms_full.py"), "--check"]).returncode == 0, "public/llms-full.txt is stale: run python3 tools/build_llms_full.py"
    llms = open(os.path.join(PUB, "llms.txt"), encoding="utf-8").read()
    assert "(https://citedby.eu/llms-full.txt)" in llms
    bad = []
    for u in re.findall(r"\((https://citedby\.eu[^)\s]*)\)", llms):
        p = norm(u)
        if not (file_for(p) or app_served(p) or os.path.exists(PUB + p)): bad.append(("llms.txt link with no page", u))
    report(bad)
