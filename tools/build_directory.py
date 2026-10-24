#!/usr/bin/env python3
"""Generate the AI crawler directory pages (RES-4194): data/directory/crawlers/<slug>.json + texts_<loc>.json -> content/blog/<slug>[.<loc>].md.
Then run tools/build_blog.py, which renders every md in all five locales and the /bots and /platforms hubs.

usage: python3 tools/build_directory.py [--check]
English pages that carry `en_handwritten: true` in their JSON stay as written in content/blog (they are the pages QA already passed); every other locale and every new crawler is generated.
Facts (token, job, IP list, vendor quote) are read from the operator's own page by hand and re-checked by `tools/verify_directory.py`; prose per crawler is in texts_<loc>.json; sentences common to all pages are in tools/directory_i18n.py."""
import glob, html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from directory_i18n import S, HUB, LOCS, date_txt
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DATA, OUT = os.path.join(ROOT, "data", "directory"), os.path.join(ROOT, "content", "blog")
E = html.escape
CHECKED = {"gptbot", "oai-searchbot", "chatgpt-user", "perplexitybot", "claudebot", "google-extended", "bingbot", "googlebot"}  # crawlers the free check tests with a live request (doorcheck.py + app crawl)
TRAIN = ["gptbot", "claudebot", "google-extended", "applebot-extended", "meta-externalagent", "amazonbot"]  # each operator's page says the crawler may be used for model training
SEARCH = ["oai-searchbot", "claude-searchbot", "perplexitybot", "amzn-searchbot", "meta-webindexer"]
DATE, ART = "2026-10-24", "can-chatgpt-read-my-website"
def prefix(loc): return "" if loc == "en" else "/" + loc

def load():
    ents = {}
    for p in sorted(glob.glob(os.path.join(DATA, "crawlers", "*.json"))):
        d = json.load(open(p, encoding="utf-8")); ents[d["slug"]] = d
    texts = {l: json.load(open(os.path.join(DATA, "texts_%s.json" % l), encoding="utf-8")) for l in LOCS}
    return ents, texts

def strip_table(t):  # the old English "What X is" sections carry the facts table; the template draws it
    return re.sub(r"\n*(?:^\|.*\n?)+", "\n\n", t, flags=re.M).strip()
def loc_links(t, loc):
    return re.sub(r"\]\(/(bots|platforms|blog|guides)(?=[/)])", lambda m: "](%s/%s" % (prefix(loc), m.group(1)), t) if loc != "en" else t
def path_of(url): return re.sub(r"^https?://", "", url or "").rstrip("/")

def ips_cell(d, s):
    i = d["ips"]; k = i["kind"]
    if k == "json_list": return s["ips_json"].format(n=i["count"], unit=s["unit_" + i["unit"]], path=path_of(i["url"]), date=i["file_date"])
    if k == "html_list": return s["ips_html"].format(path=path_of(i["url"])) if i.get("url") else s["ips_html0"]
    if k == "verify_tool": return s["ips_verify"]
    if k == "rdns": return s["ips_rdns"]
    if k == "advice": return s["ips_advice"]
    return s["ips_none_ctl"] if d["job"] == "control" else s["ips_none"]
def ip_short(d, s):
    i = d["ips"]; k = i["kind"]
    if k == "json_list": return "%s %s" % (i["count"], s["unit_" + i["unit"]])
    return {"html_list": s["ip_short_html"], "verify_tool": s["ip_short_verify"], "rdns": s["ip_short_rdns"], "advice": s["ip_short_advice"]}.get(k, s["ip_short_none"])
def has_ua(d): return bool(d.get("ua")) and not d["ua"].startswith("Not published")

def page(d, loc, tx, ents, art_titles):
    s, slug, name = S[loc], d["slug"], d["name"]; co = " :" if loc == "fr" else ":"  # French puts a space before the colon (the build turns it into U+202F)
    jobs = s["jobs"][d["job"]]; obey = s[d["follows"]]; pre = prefix(loc)
    ip_cell, ipn = ips_cell(d, s), tx["ipnote"]
    desc = next(c for c in (x.format(name=name, operator=d["operator"], job=jobs.lower() if loc != "de" else jobs) for x in s["desc"]) if len(c) <= 158)
    title = s["title"].format(name=name)
    if len(title) > 65: title = s["title_short"].format(name=name)  # the SEO gate allows 15-65 characters
    comp = ents.get(d.get("compare")); related = ["%s/bots|%s" % (pre, s["rel_hub"])]
    if comp: related.append("%s/bots/%s|%s" % (pre, comp["slug"], comp["name"]))
    related += ["%s/platforms|%s" % (pre, s["rel_plat"]), "%s/blog/%s|%s" % (pre, ART, art_titles[loc])]
    boxes = "; ".join("%s|%s" % (a, b) for a, b in ((s["hero_op"], d["operator"]), (s["hero_job"], jobs), (s["hero_obey"], obey), (s["hero_ip"], ip_short(d, s))))
    fm = ["title: " + title, "h1: " + title, "description: " + desc, "slug: " + slug, "section: bots", "locale: " + loc, "cluster: " + s["cluster"], "date: " + DATE, "reviewed: " + d["read"],
          "hero: auto", "hero_alt: " + s["hero_alt"].format(name=name, operator=d["operator"], job=jobs, obey=obey, ip=ip_short(d, s)), "hero_sub: " + s["hero_sub"].format(name=name, operator=d["operator"]),
          "hero_boxes: " + boxes, "widget: on", "related: " + "; ".join(related), "answer: " + " ".join(tx["answer"].split())]
    q = d["vendor_quote_source"]; rd = date_txt(loc, d["read"])
    body = ["", "## " + s["h_what"].format(name=name), "", loc_links(strip_table(tx["what"]), loc), "",
            "| %s | %s |" % (s["fact"], name), "| --- | --- |", "| %s | %s |" % (s["operator"], d["operator"]), "| %s | %s |" % (s["job"], " ".join(tx["job"].split())),
            "| %s | `%s` |" % (s["token"], d["token"]), "| %s | %s |" % (s["follows"], " ".join(tx["follows"].split())), "| %s | %s |" % (s["ips"], ip_cell), "| %s | %s |" % (s["read"], rd), ""]
    if d.get("vendor_quote"):
        body += ["## " + s["h_vendor"], "", "%s%s “%s”" % (s["quote_lead"], co, d["vendor_quote"].strip()), "", "%s%s [%s](%s), %s %s." % (s["src_lead"], co, q["title"], q["url"], s["read_on"], rd), ""]
    body += ["## " + s["h_block"].format(name=name), "", loc_links(tx["block"], loc), "", "## " + s["h_lines"], "",
             s["allow"].format(name=name), "", "```", "User-agent: %s" % d["token"], "Allow: /", "```", "", s["block"].format(name=name), "", "```", "User-agent: %s" % d["token"], "Disallow: /", "```", "", s["paste"], ""]
    if has_ua(d): body += [s["ua"], "", "```", d["ua"], "```", ""]
    elif d["job"] != "control": body += [s["ua_none"].format(name=name), ""]
    body += ["## " + s["h_verify"], ""]
    if d["ips"]["kind"] == "json_list" and not d.get("en_handwritten"):
        body += [s["ips_json_lead"].format(path=path_of(d["ips"]["url"]), n=d["ips"]["count"], unit=s["unit_" + d["ips"]["unit"]], read=rd, date=d["ips"]["file_date"]), ""]
    body += [loc_links(tx["ipnote"], loc), ""]
    if d["job"] == "control": body += [s["ctl"].format(name=name), ""]
    if comp: body += ["## " + s["h_compare"].format(name=comp["name"]), "", "[%s](%s/bots/%s)%s %s" % (comp["name"], pre, comp["slug"], co, " ".join(tx["compare"].split())), ""]
    body += ["## " + s["h_check"], "", (s["check_in"] if slug in CHECKED else s["check_out"]).format(name=name, token=d["token"]), "", "## FAQ", "", "### " + s["q1"].format(name=name), "",
             s["a1_" + {"yes": "yes", "partial": "partial", "token_only": "token_only", "no": "partial", "unknown": "yes"}[d["follows"]]].format(name=name, token=d["token"], follows=" ".join(tx["follows"].split()).rstrip(".")), "",
             "### " + s["q2"].format(name=name), "", s["a2"], "", "## Sources", ""]
    seen = set()
    for x in d["sources"] + [{"title": q["title"], "url": q["url"]}]:
        if x["url"] in seen: continue
        seen.add(x["url"]); body.append("- [%s](%s)" % (x["title"], x["url"]))
    return "\n".join(fm + body) + "\n"

def art_titles():
    out = {}
    for l in LOCS:
        p = os.path.join(OUT, ART + (".%s" % l if l != "en" else "") + ".md")
        out[l] = re.search(r"^title: (.+)$", open(p, encoding="utf-8").read(), re.M).group(1)
    return out

def generate(check=False):
    ents, texts = load(); at = art_titles(); n = 0
    for slug, d in ents.items():
        for loc in LOCS:
            if loc == "en" and d.get("en_handwritten"): continue
            tx = texts[loc][slug]
            if loc == "en": tx = dict(tx, answer=d["answer_en"])
            md = page(d, loc, tx, ents, at); n += 1
            if not check: open(os.path.join(OUT, "%s%s.md" % (slug, "" if loc == "en" else "." + loc)), "w", encoding="utf-8").write(md)
    return n

def hub_extra(loc):
    """HTML under the /bots hub lede: the comparison table of every crawler and the two copy-paste robots.txt blocks (RES-4194)."""
    ents, texts = load(); s = S[loc]; pre = prefix(loc)
    rows = "".join('<tr><td data-label="%s"><a href="%s/bots/%s">%s</a></td><td data-label="%s">%s</td><td data-label="%s">%s</td><td data-label="%s">%s</td></tr>' % (
        E(s["tbl_h"][0]), pre, d["slug"], E(d["name"]), E(s["tbl_h"][1]), E(d["operator"]), E(s["tbl_h"][2]), E(" ".join(texts[loc][d["slug"]]["job"].split())), E(s["tbl_h"][3]), E(" ".join(texts[loc][d["slug"]]["follows"].split())))
        for d in sorted(ents.values(), key=lambda d: d["name"].lower()))
    tbl = '<div class="tw stack"><table><caption>%s</caption><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (E(s["tbl_cap"].format(n=len(ents))), "".join('<th scope="col">%s</th>' % E(h) for h in s["tbl_h"]), rows)
    tok = lambda sl: ents[sl]["token"]
    train = "\n\n".join("User-agent: %s\nDisallow: /" % tok(x) for x in TRAIN); allow = "\n\n".join("User-agent: %s\nAllow: /" % tok(x) for x in SEARCH)
    snip = '<h2>%s</h2><p>%s</p><h3>%s</h3><pre><code>%s</code></pre><h3>%s</h3><pre><code>%s</code></pre>' % (
        E(s["snip_h"]), E(s["snip_p"].format(names=", ".join(tok(x) for x in TRAIN), allow_names=", ".join(tok(x) for x in SEARCH))), E(s["snip_train"]), E(train), E(s["snip_search"]), E(allow))
    return tbl + snip

if __name__ == "__main__":
    n = generate("--check" in sys.argv); print("%s %d pages" % ("checked" if "--check" in sys.argv else "wrote", n))
