#!/usr/bin/env python3
"""RES-3712: public/data/ai-access-index-2026-10.html (run 1 archive) and public/data/ai-access-index.html (latest) from the CSVs Research publishes (RES-3675, research/data-stories/citedby-ai-access-index).
Every number on the page is read from those CSVs; the method and limits are STORY.md's, word for word.
Run 2: copy its CSVs as ai-access-index-<yyyy>-<mm>*.csv, change RUN / READ_ON / LIST_ID and the dates below, and rebuild; the run 1 page stays at its own URL."""
import csv, html, json, os
H = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "public", "data")
RUN, READ_ON, LIST_ID, MADE = "2026-10", "2026-10-23", "56Z8N", "22 Oct 2026"
E = html.escape
rows = lambda n: list(csv.reader(open(os.path.join(H, n), encoding="utf-8")))[1:]
SITES = list(csv.DictReader(open(os.path.join(H, f"ai-access-index-{RUN}.csv"), encoding="utf-8")))
BOT = {r[0]: r for r in rows(f"ai-access-index-{RUN}-by-crawler.csv")}  # crawler, blocked, n, blocked_pct, ci_lo, ci_hi, named, named_pct
CTRY = rows(f"ai-access-index-{RUN}-by-country.csv")  # country, tld, n, gpt k/%/lo/hi, claude k/%/lo/hi, train4 k/%/lo/hi, search3 k/%/lo/hi
CMS = rows(f"ai-access-index-{RUN}-by-cms.csv")  # cms, n, gptbot_k, gptbot_pct, train4_k, train4_pct
OK = [r for r in SITES if r["robots_txt"] == "ok"]; N = len(OK); T = len(SITES)
TRAIN = ("GPTBot", "ClaudeBot", "Google-Extended", "CCBot"); SEARCH = ("OAI-SearchBot", "Claude-SearchBot", "PerplexityBot")
def share(f): k = sum(1 for r in OK if f(r)); return k, round(100 * k / N, 1)
k_train, p_train = share(lambda r: any(r[b] == "blocked" for b in TRAIN)); k_all, p_all = share(lambda r: all(r[b] == "blocked" for b in TRAIN))
k_search, p_search = share(lambda r: any(r[b] == "blocked" for b in SEARCH))
p_gpt, k_gpt, p_google = BOT["GPTBot"][3], BOT["GPTBot"][1], BOT["Googlebot"][3]
assert N == int(BOT["GPTBot"][2]) and p_gpt == str(share(lambda r: r["GPTBot"] == "blocked")[1])  # the page and Research's tables must agree
cov = {}
for r in SITES:
    if r["robots_txt"] != "ok": cov[r["robots_txt"]] = cov.get(r["robots_txt"], 0) + 1
n_unread = T - N; pct_read = round(100 * N / T)
n_unreach, n_403, n_404, n_html = cov.get("unreachable", 0), cov.get("http403", 0), cov.get("http404", 0), cov.get("http200", 0)
n_other = n_unread - n_unreach - n_403 - n_404 - n_html
by_train = sorted(CTRY, key=lambda r: -float(r[12])); hi, lo = by_train[0], by_train[-1]
by_search = sorted(CTRY, key=lambda r: -float(r[16]))
fmt = lambda n: f"{int(n):,}"
S1 = f"On 23 October 2026, {p_gpt}% of {fmt(N)} popular EU websites (top domains under 25 country-code TLDs, Tranco list {LIST_ID}) asked OpenAI's GPTBot to stay out in robots.txt; {p_train}% blocked at least one of GPTBot, ClaudeBot, Google-Extended and CCBot (CitedBy AI-Access Index)."
S2 = f"1 in 13 ({p_search}%) of the same sites blocks at least one crawler that builds AI answer indexes (OAI-SearchBot, Claude-SearchBot or PerplexityBot); {p_google}% block Googlebot."
ADJ = {"Germany": "German", "Slovenia": "Slovenian"}
S3 = f"{ADJ[hi[0]]}-domain sites block AI training crawlers most often ({hi[12]}% block at least one of four), {ADJ[lo[0]]}-domain sites least ({lo[12]}%)."
assert round(1 / (p_search / 100)) == 13 and (hi[0], lo[0]) == ("Germany", "Slovenia")
TITLE = "EU AI-Access Index, run 1 (Oct 2026): who blocks AI crawlers"; TITLE_LATEST = "EU AI-Access Index: which EU sites block AI crawlers"; H1 = "EU AI-Access Index: which AI crawlers popular EU sites block"
DESC = f"{p_gpt}% of {fmt(N)} popular EU websites block GPTBot in robots.txt; {p_train}% block one of four AI training crawlers. Method, country and CMS tables, CSV."
DESC_LATEST = "Latest run: " + DESC
def td(label, v, sub=""): return f'<td class="n" data-l="{E(label)}">{v}{(" <span class=&quot;src&quot;>" + sub + "</span>") if sub else ""}</td>'.replace("&quot;", '"')
def page(url, canonical, latest):
    ld = {"@context": "https://schema.org", "@graph": [{"@type": "Dataset", "@id": "https://citedby.eu/data/ai-access-index-2026-10#dataset", "name": "EU AI-Access Index, run 1 (October 2026)", "description": DESC, "url": "https://citedby.eu/data/ai-access-index-2026-10", "inLanguage": "en", "isAccessibleForFree": True,
        "license": "https://creativecommons.org/licenses/by/4.0/", "dateCreated": READ_ON, "datePublished": READ_ON, "dateModified": READ_ON, "temporalCoverage": READ_ON, "spatialCoverage": "European Union (25 country-code top-level domains)",
        "creator": {"@type": "Organization", "name": "CitedBy", "url": "https://citedby.eu"}, "publisher": {"@type": "Organization", "name": "CitedBy", "url": "https://citedby.eu"},
        "isBasedOn": {"@type": "Dataset", "name": f"Tranco list {LIST_ID}", "url": f"https://tranco-list.eu/list/{LIST_ID}/1000000"},
        "measurementTechnique": f"One GET of /robots.txt per domain on {READ_ON}, read by the RFC 9309 rules; share base is the sites whose robots.txt was read. Tranco list {LIST_ID}.",
        "variableMeasured": [f"robots.txt verdict (blocked, partial, allowed) for {len(BOT)} crawlers", "country-code domain", "CMS home-page signature"],
        "distribution": [{"@type": "DataDownload", "encodingFormat": "text/csv", "name": n, "contentUrl": "https://citedby.eu/data/" + f} for f, n in (
            (f"ai-access-index-{RUN}.csv", "One row per domain"), (f"ai-access-index-{RUN}-by-country.csv", "By country"), (f"ai-access-index-{RUN}-by-cms.csv", "By CMS"), (f"ai-access-index-{RUN}-by-crawler.csv", "By crawler"))]}]}
    head = f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(TITLE_LATEST if latest else TITLE)}</title>
<meta name="description" content="{E(DESC_LATEST if latest else DESC)}">
<link rel="canonical" href="https://citedby.eu{canonical}">
<meta property="og:title" content="{E(TITLE)}"><meta property="og:description" content="{E(DESC)}"><meta property="og:url" content="https://citedby.eu{canonical}"><meta property="og:type" content="article"><meta property="og:locale" content="en_IE">
<meta name="theme-color" content="#0F1B2D">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/saas.css"><link rel="stylesheet" href="/doc.css?v=bbef868a"><link rel="stylesheet" href="/data.css?v=08430f8c">
<script type="application/ld+json">{json.dumps(ld)}</script>
</head><body class="cb dc dp">
<a class="sr" href="#main">Skip to content</a>
<header class="topbar"><div class="in"><a class="mark" href="/"><i></i>CitedBy</a><nav aria-label="Main"><a class="opt" href="/#checks">What we check</a><a href="/plans">Pricing</a><a href="/blog">Guides</a><a class="opt" href="/data">Data</a></nav><a class="signin" href="/signin?next=%2Fapp.html">Sign in</a><a class="btn sm go" href="/app.html#/new">Audit a site</a></div></header>
<main id="main" class="wide">
<p class="crumb"><a href="/">CitedBy</a> / <a href="/data">Data</a> / Index</p>
<p class="dateline">AI-Access Index · run 1 · read 23 Oct 2026</p>
'''
    crawl_rows = "".join(f'<tr><td>{E(b)}</td>{td("Blocks /", BOT[b][3] + "%", f"({fmt(BOT[b][1])})")}{td("Names it", BOT[b][7] + "%")}</tr>' for b in BOT)
    ctry_rows = "".join(f'<tr><td>{E(r[0])} (.{r[1]})</td>{td("Sites read", fmt(r[2]))}{td("GPTBot", r[4] + "%")}{td("At least one of 4 training crawlers", r[12] + "%", f"({r[13]} to {r[14]})")}{td("Answer-engine search crawler", r[16] + "%")}</tr>' for r in by_train)
    cms_rows = "".join(f'<tr><td>{E(lb)}</td>{td("Sites read", fmt(r[1]))}{td("GPTBot", r[3] + "%")}{td("At least one of 4 training crawlers", r[5] + "%")}</tr>' for r in CMS for lb in [{"unknown": "No signature matched", "unreadable": "Home page not fetched"}.get(r[0], r[0])])
    body = f'''<h1>EU AI-Access Index: which AI crawlers popular EU sites block</h1>
<p class="ans">{E(S1)} {E(S2)} {E(S3)}</p>
<p class="src">Run 1 · robots.txt read {READ_ON[8:]} Oct 2026 · Tranco list <a href="https://tranco-list.eu/list/{LIST_ID}/1000000" rel="noopener">{LIST_ID}</a> · {fmt(N)} of {fmt(T)} sites read · {"This is the latest run. " if latest else "Archive of run 1. "}<a href="/data/ai-access-index-{RUN}.csv">Download the per-site CSV</a></p>
<section><h2>What this measures</h2><p>This index records what each site's robots.txt asks AI crawlers to do. It does not measure what any assistant cites or links, and it does not show whether a crawler obeys the file.</p>
<ul><li><b>{p_gpt}%</b> ({fmt(k_gpt)} sites) block GPTBot; {BOT["ClaudeBot"][3]}% block ClaudeBot, {BOT["Google-Extended"][3]}% Google-Extended, {BOT["CCBot"][3]}% CCBot.</li>
<li><b>{p_train}%</b> ({fmt(k_train)}) block at least one of those four; {p_all}% ({fmt(k_all)}) block all four.</li>
<li><b>{p_search}%</b> ({fmt(k_search)}) block at least one answer-engine search crawler (OAI-SearchBot {BOT["OAI-SearchBot"][3]}%, PerplexityBot {BOT["PerplexityBot"][3]}%, Claude-SearchBot {BOT["Claude-SearchBot"][3]}%).</li>
<li><b>{p_google}%</b> block Googlebot, the control: sites that shut out AI crawlers almost never shut out ordinary search.</li></ul>
<p class="src">Shares use the {fmt(N)} sites whose robots.txt we could read as base. "Blocks" means the crawler may not fetch the home page path <code>/</code> under the file's rules.</p></section>
<section><h2>By crawler</h2>
<div class="tw"><table><thead><tr><th>Crawler</th><th class="n">Share of sites that block it</th><th class="n">Share that name it in robots.txt</th></tr></thead><tbody>
{crawl_rows}
</tbody></table></div>
<p class="src">Googlebot and Bingbot are controls. "Names it" means robots.txt has a group addressed to that crawler: the owner chose on purpose. <a href="/data/ai-access-index-{RUN}-by-crawler.csv">Download by crawler (CSV)</a></p></section>
<section><h2>By country-code domain</h2>
<div class="tw"><table><thead><tr><th>Country (ccTLD)</th><th class="n">Sites read</th><th class="n">Block GPTBot</th><th class="n">Block at least one of GPTBot, ClaudeBot, Google-Extended, CCBot (95% interval)</th><th class="n">Block an answer-engine search crawler</th></tr></thead><tbody>
{ctry_rows}
</tbody></table></div>
<p class="src">Sorted by the fourth column. Answer-engine search crawler blocked most: {by_search[0][0]} {by_search[0][16]}%, {by_search[1][0]} {by_search[1][16]}%, {by_search[2][0]} {by_search[2][16]}%; least: {by_search[-1][0]} {by_search[-1][16]}%. Luxembourg has {CTRY[[r[0] for r in CTRY].index("Luxembourg")][2]} sites read; its interval is wide. <a href="/data/ai-access-index-{RUN}-by-country.csv">Download by country (CSV)</a></p></section>
<section><h2>By CMS</h2>
<div class="tw"><table><thead><tr><th>CMS (home-page signature)</th><th class="n">Sites read</th><th class="n">Block GPTBot</th><th class="n">Block at least one of the four</th></tr></thead><tbody>
{cms_rows}
</tbody></table></div>
<p class="src">Only CMSs with at least 50 sites are shown; Shopify, Wix, Squarespace and Webflow have fewer and are not reported. The CMS is a signature in the home page, not a verified platform, and "No signature matched" is the largest group. <a href="/data/ai-access-index-{RUN}-by-cms.csv">Download by CMS (CSV)</a></p></section>
<section><h2>Method and limits</h2><ul>
<li><b>Question:</b> of the most popular sites under each EU country-code domain, which AI crawlers does robots.txt ask to stay out?</li>
<li><b>Sample:</b> the top 600 domains by Tranco rank under each of 25 EU ccTLDs (Luxembourg has 250), from Tranco list {LIST_ID} (created {MADE}; <a href="https://tranco-list.eu/list/{LIST_ID}/1000000" rel="noopener">tranco-list.eu/list/{LIST_ID}/1000000</a>). {fmt(T)} domains probed; robots.txt read on <b>{fmt(N)} ({pct_read}%)</b>.</li>
<li><b>Fetch:</b> one GET of <code>/robots.txt</code> (https, then www, then http) and one GET of the home page for a CMS signature. User-Agent <code>CitedBy-research/1.0 (+https://citedby.eu; robots.txt study, one request per site)</code>. No login, no cookies, no retry after a refusal, no browser identity.</li>
<li><b>Reading:</b> RFC 9309: the group naming the crawler wins, else the <code>*</code> group; longest rule wins; Allow wins a tie. "Blocks" = the crawler may not fetch <code>/</code>. 16 crawlers tracked (14 AI-related, Googlebot and Bingbot as controls).</li>
<li><b>Share base:</b> the {fmt(N)} sites whose robots.txt was read. The other {fmt(n_unread)} are coverage, not "allows": {fmt(n_unreach)} unreachable, {fmt(n_403)} answered HTTP 403 (to our research UA), {fmt(n_404)} had no robots.txt (404), {fmt(n_html)} returned an HTML page instead, {fmt(n_other)} other.</li>
<li><b>Precision check (23 Oct):</b> 20 sites drawn at random (8 verdict "blocked", 4 "allowed", 8 "partial" for GPTBot) re-fetched and the GPTBot / <code>*</code> lines read by eye: 0 contradictions. Two stacked-group cases (tv2.dk, veikkaus.fi) were not read to the end of the group.</li>
<li><b>Parser test:</b> 7 unit tests, including the <code>Disallow: /?</code> case that python's robotparser reads as <code>/</code> (our lesson from earlier work).</li>
<li><b>Limits:</b> robots.txt states a request, not what a firewall enforces: 7.8% of probes got HTTP 403 for our research user-agent, which may be a bot block but is not counted as one. ccTLD is not the operator's country (a German company can use .com; a .de site can be foreign-owned). Tranco ranks popularity, so the sample is the popular end of each ccTLD, not a random draw of all sites. Sites whose robots.txt we could not read (29%) may differ from those we could: of the readable sites, those whose home page we could not fetch block more often (GPTBot 23.9% vs 15.3% overall), so the unread 29% probably lean toward more blocking, not less (an inference, not a measurement). The first 2,900 probes used a 12 s timeout and 40 threads, the rest 8 s and 120 threads; this can only move a site between "read" and "unreachable". CMS is a home-page signature, not a verified platform ("No signature matched" is the largest group).</li>
<li><b>Raw data:</b> one row per domain with the verdict for each crawler, public robots.txt data only: <a href="/data/ai-access-index-{RUN}.csv">ai-access-index-{RUN}.csv</a> (2 MB). Licence: CC BY 4.0, cite as "CitedBy AI-Access Index, run 1, October 2026".</li></ul></section>
<section><h2>Run history</h2><p>The crawl is repeated each month on the newest Tranco list. This page is run 1 (read 23 Oct 2026) and stays at <a href="/data/ai-access-index-{RUN}">/data/ai-access-index-{RUN}</a>; <a href="/data/ai-access-index">/data/ai-access-index</a> always shows the latest run.</p></section>
<section class="cta"><h2>What does your robots.txt say to AI crawlers?</h2><p class="lede">We crawl your site up to your plan's page limit and give you the exact fix for each issue. From €9, 14-day money-back guarantee.</p><div class="actions"><a class="btn p" href="/">Audit my site</a></div></section>
</main>
'''
    foot = open(os.path.join(H, "launch-crawl-2026-10.html"), encoding="utf-8").read(); foot = foot[foot.index("<footer>"):]
    return head + body + foot
open(os.path.join(H, f"ai-access-index-{RUN}.html"), "w", encoding="utf-8").write(page(f"/data/ai-access-index-{RUN}", f"/data/ai-access-index-{RUN}", False))
open(os.path.join(H, "ai-access-index.html"), "w", encoding="utf-8").write(page("/data/ai-access-index", f"/data/ai-access-index-{RUN}", True))  # canonical stays on the archive until run 2 exists
print(S1, S2, S3, sep="\n")
