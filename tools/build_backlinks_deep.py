#!/usr/bin/env python3
"""RES-3899: refill data/backlinks.sqlite with each host's 80 strongest referrers (deep.tsv from export_backlinks_deep.py) and write the `common` table:
the referrers that are among the 80 strongest of at least COMMON_PCT % of the hosts. A page folds those into one line and lists 30 referrers of its own.
Then the `thin` table: hosts whose own list is too short (under MIN_ROWS referrers after the fold) or a near copy (Jaccard of the listed referrers >= TWIN_J) of a host kept before them (strongest host first, so one page of each link network stays indexable).
Tier 1 hosts (our sites, SEO tools) are exempt from the short-list rule only. Those pages answer and show their data, but are noindex and out of the sitemap: a search engine would read them as one page said again (CitedBy's own audit says so).
python3 tools/build_backlinks_deep.py deep.tsv data/backlinks.sqlite [pct] [min_rows] [twin_j]   (dom and meta stay as they are)"""
import collections, os, sqlite3, sys
SRC, DB = sys.argv[1], sys.argv[2]
COMMON_PCT = float(sys.argv[3]) if len(sys.argv) > 3 else 3.0
SHOWN = 30  # rows a page lists: the same number as backlinks.SHOWN
MIN_ROWS = int(sys.argv[4]) if len(sys.argv) > 4 else 8
TWIN_J = float(sys.argv[5]) if len(sys.argv) > 5 else 0.5
HIDE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "backlinks-hide-adult.txt")
db = sqlite3.connect(DB)
hosts = {d for (d,) in db.execute("select domain from dom")}
rows, df = [], collections.Counter()
for l in open(SRC, encoding="utf-8"):
    d, r, ref, s = l.rstrip("\n").split("\t")
    if d in hosts: rows.append((d, int(r), ref, int(s))); df[ref] += 1
n = len({r[0] for r in rows})
assert n == len(hosts), (n, len(hosts))
db.execute("delete from bl"); db.executemany("insert into bl values (?,?,?,?)", rows)
db.execute("drop table if exists common"); db.execute("create table common(referrer text primary key, hosts int) without rowid")
cut = n * COMMON_PCT / 100
db.executemany("insert into common values (?,?)", [(r, c) for r, c in df.items() if c >= cut])
db.execute("insert or replace into meta values ('common_pct', ?)", (("%g" % COMMON_PCT),)); db.execute("insert or replace into meta values ('common_hosts', ?)", (str(n),))
com = {r for (r,) in db.execute("select referrer from common")}
hide = {l.strip() for l in open(HIDE, encoding="utf-8") if l.strip() and not l.startswith("#")}  # the same two cuts backlinks.split() makes
own = {d: [] for d in hosts}
for d, ref in db.execute("select domain, referrer from bl order by domain, rank"):
    if ref not in com and ref not in hide and len(own[d]) < SHOWN: own[d].append(ref)
inv = collections.defaultdict(list)  # referrer -> kept hosts that list it
db.execute("drop table if exists thin"); db.execute("create table thin(domain text primary key, why text) without rowid")
thin = []
for d, tier in db.execute("select domain, tier from dom order by tier, referring_domains desc, domain").fetchall():
    mine = set(own[d])
    if tier != 1 and len(mine) < MIN_ROWS: thin.append((d, "rows")); continue  # our sites and the SEO tools people look up by name (resaleiq.dev, semrush.com) stay indexable on a short list
    hit = collections.Counter(e for r in mine for e in inv[r])
    if any(k / (len(mine) + len(own[e]) - k) >= TWIN_J for e, k in hit.items()): thin.append((d, "twin")); continue  # moz.com lists what ahrefs.com lists
    for r in mine: inv[r].append(d)
db.executemany("insert into thin values (?,?)", thin)
db.execute("insert or replace into meta values ('thin_min_rows', ?)", (str(MIN_ROWS),)); db.execute("insert or replace into meta values ('thin_twin_j', ?)", (str(TWIN_J),))
db.commit(); db.execute("vacuum")
print("thin", collections.Counter(w for _, w in thin), end="; ")
print("hosts", n, "bl rows", len(rows), "common referrers", db.execute("select count(*) from common").fetchone()[0], "cut", cut)
