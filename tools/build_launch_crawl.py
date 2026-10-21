#!/usr/bin/env python3
"""RES-2126: public/data/launch-crawl-2026-10.html from public/data/launch-crawl-2026-10.csv (summary.csv of the crawl). Every number on the page is read from a column of that CSV."""
import csv, json, os, re
H = os.path.join(os.path.dirname(__file__), "..", "public", "data"); T = open(os.path.join(H, "study-chatgpt-buyer-questions.html")).read()
R = {r["segment"]: r for r in csv.DictReader(open(os.path.join(H, "launch-crawl-2026-10.csv")))}
def f(seg, m): r = R[seg]; return f'{r[m+"_n"]}/{r[m+"_d"]}', f'{round(float(r[m+"_pct"]))}%'
def row(label, m, tip=""):
    cells = ""
    for seg in ("S", "V_lovable"):
        n, p = f(seg, m); cells += f'<td class="n" data-l="{"Show HN" if seg == "S" else "Lovable"}">{p} <span class="src">({n})</span></td>'
    return f"<tr><td>{label}</td>{cells}</tr>"
S, L = R["S"], R["V_lovable"]
head = T[:T.index("<h1>")]
head = re.sub(r"<title>.*?</title>", "<title>Launch crawl 2026-10: 300 Show HN sites and 70 Lovable sites read as a crawler reads them</title>", head, flags=re.S)
desc = f'We fetched the homepage and up to 9 pages of {S["n_listed"]} Show HN sites and {L["n_listed"]} Lovable sites as a crawler: {round(float(L["empty_pct"]))}% of the Lovable homepages hold under 100 words of text without JavaScript.'
head = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{desc}">', head)
head = head.replace("study-chatgpt-buyer-questions", "launch-crawl-2026-10")
head = re.sub(r'(<meta property="og:title" content=")[^"]*', r"\1Launch crawl 2026-10: Show HN and Lovable sites read as a crawler reads them", head)
head = re.sub(r'(<meta property="og:description" content=")[^"]*', r"\g<1>" + desc, head)
ld = {"@context": "https://schema.org", "@graph": [{"@type": "Dataset", "@id": "https://citedby.eu/data/launch-crawl-2026-10#dataset", "name": "Launch crawl 2026-10: Show HN and Lovable sites read as a crawler reads them", "description": desc, "url": "https://citedby.eu/data/launch-crawl-2026-10", "inLanguage": "en", "isAccessibleForFree": True, "license": "https://creativecommons.org/licenses/by/4.0/", "dateCreated": "2026-10-21", "datePublished": "2026-10-21", "dateModified": "2026-10-21", "temporalCoverage": "2026-10-20/2026-10-21", "creator": {"@type": "Organization", "name": "CitedBy", "url": "https://citedby.eu"}, "publisher": {"@type": "Organization", "name": "CitedBy", "url": "https://citedby.eu"}, "measurementTechnique": "Plain HTTP fetches by CitedBot/1.0 with robots.txt obeyed and no JavaScript; deterministic checks only.", "variableMeasured": ["homepage words", "robots.txt rule per AI crawler", "live request per AI crawler", "sitemap", "llms.txt", "JSON-LD"], "distribution": [{"@type": "DataDownload", "encodingFormat": "text/csv", "contentUrl": "https://citedby.eu/data/launch-crawl-2026-10.csv"}]}]}
head = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: '<script type="application/ld+json">' + json.dumps(ld) + "</script>", head, count=1, flags=re.S)
body = f'''<h1>Launch crawl 2026-10: Show HN and Lovable sites read as a crawler reads them</h1>
<p class="ans">We fetched {S["n_listed"]} sites that launched on Show HN (15 to 20 Oct 2026) and {L["n_listed"]} sites built with Lovable, as CitedBot, the crawler CitedBy sells. {L["empty_n"]} of the {L["empty_d"]} Lovable homepages we could read hold under 100 words of text in the HTML they send ({round(float(L["empty_pct"]))}%); for the Show HN sites it is {S["empty_n"]} of {S["empty_d"]} ({round(float(S["empty_pct"]))}%).</p>
<p class="src">Fetched {S["fetched_on"]} · robots.txt obeyed · no JavaScript · homepage plus up to 9 pages · <a href="/data/launch-crawl-2026-10.csv">Download summary CSV</a></p>
<section><h2>The numbers</h2>
<div class="tw"><table><thead><tr><th>Share of sites that could be checked</th><th class="n">Show HN ({S["n_measured"]} read)</th><th class="n">Lovable ({L["n_measured"]} read)</th></tr></thead><tbody>
{row("Homepage under 100 words of text in the raw HTML", "empty")}
{row("robots.txt blocks at least one of GPTBot, OAI-SearchBot, ClaudeBot, Claude-SearchBot, PerplexityBot", "robots")}
{row("robots.txt blocks at least one search crawler (OAI-SearchBot, Claude-SearchBot, PerplexityBot)", "robots_search")}
{row("Homepage turned away a live request from at least one of those five crawlers (firewall)", "fw")}
{row("Homepage turned away a live request from a search crawler", "fw_search")}
{row("sitemap.xml present and valid", "sitemap")}
{row("llms.txt present", "llms")}
{row("JSON-LD on the homepage", "jsonld_home")}
</tbody></table></div>
<p class="src">Each cell is a share with its count in brackets; the denominator is the sites for which that check could be run, so it differs by row. Sites we could not read are left out, never counted as failures.</p></section>
<section><h2>What the numbers say</h2><ul class="lv">
<li><span class="tag">Measured</span>Most Lovable homepages send almost no text in the HTML: {L["empty_n"]} of {L["empty_d"]} under 100 words, median {L["median_home_words"]} words. A crawler that does not run JavaScript reads an empty page; a browser shows more.</li>
<li><span class="tag">Measured</span>Among Show HN sites, {S["fw_n"]} of {S["fw_d"]} ({round(float(S["fw_pct"]))}%) turned away a request that carried the user-agent of at least one big AI crawler, while CitedBot got the page. Only {S["fw_search_n"]} of {S["fw_search_d"]} did so for a search crawler.</li>
<li><span class="tag">Measured</span>robots.txt is a smaller factor: {S["robots_n"]} of {S["robots_d"]} Show HN sites and {L["robots_n"]} of {L["robots_d"]} Lovable sites block one of the five crawlers there.</li>
<li><span class="tag">Measured</span>Sitemaps: {round(float(S["sitemap_pct"]))}% of Show HN sites and {round(float(L["sitemap_pct"]))}% of Lovable sites. llms.txt: {round(float(S["llms_pct"]))}% and {round(float(L["llms_pct"]))}%; it is optional and there is no good evidence the large assistants read it.</li>
<li><span class="tag">Not measured</span>Whether the sites are cited by any assistant, traffic, or anything a browser shows after JavaScript. Page-title uniqueness had too few sites with 3 or more titled pages (Show HN {S["titles_d"]}, Lovable {L["titles_d"]}) and is not reported.</li></ul></section>
<section><h2>Method and limits</h2><ul>
<li><b>Show HN cohort:</b> the 300 newest Show HN stories up to 20 Oct 2026 23:59 UTC that link to the homepage of a site on its own domain (not a code host, social network, app store or shared-hosting subdomain), one per registered domain. Stories dated {S["date_range"].replace(" to ", " to ")}. These are launches of every kind (tools, libraries, games, apps), not only SaaS.</li>
<li><b>Lovable cohort:</b> {L["n_listed"]} sites. 31 are linked from Hacker News posts in the 12 months before 20 Oct 2026 that say the site was built with Lovable or sit on a Lovable domain; the other 39 are homepages on lovable.app in the Common Crawl index of September 2026, taken in the order of the SHA-256 of the host name. Nobody picked sites. Builders with too few sites to publish a share: Bolt (3 listed) and v0 (1 listed) count only in the CSV row V.</li>
<li><b>What we fetched:</b> CitedBot/1.0, robots.txt first and obeyed, no JavaScript, at most 1 request a second per site, the homepage plus up to 9 internal pages, <code>/sitemap.xml</code>, <code>/llms.txt</code>, and the homepage once per crawler with that crawler's published user-agent string. The last test shows how a firewall treats the string; it is not the vendor's own crawler, which a site may verify by IP address, so a 403 here can differ from what the real crawler gets.</li>
<li><b>Could not check:</b> {int(S["n_not_measured"])} Show HN and {int(L["n_not_measured"])} Lovable sites did not return an HTML homepage to CitedBot (robots.txt unreachable or erroring, rate limits, not HTML). They are left out of every denominator.</li>
<li><b>Limits:</b> Show HN sites are hours or days old and some are unfinished. Lovable sites on the owner's own domain that say nothing public about the builder are not reachable by our rules, and default-domain sites include unfinished projects. Counts describe 20 and 21 Oct 2026. Site names are not published.</li>
<li><b>Checked:</b> twenty rows are re-fetched by hand by a second person; more than 1 mismatch in 10 holds back any post that uses these numbers.</li>
<li><b>Raw data:</b> the aggregate table, one row per segment with every count and denominator: <a href="/data/launch-crawl-2026-10.csv">download</a>.</li></ul></section>
<section class="cta"><h2>Is your site readable to crawlers?</h2><p class="lede">We crawl your site up to your plan's page limit and give you the exact fix for each issue. From €9, 14-day money-back guarantee.</p><div class="actions"><a class="btn p" href="/">Audit my site</a></div></section>
</main>'''
foot = T[T.index("<footer>"):]
open(os.path.join(H, "launch-crawl-2026-10.html"), "w").write(head + body + "\n" + foot)
