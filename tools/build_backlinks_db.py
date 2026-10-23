#!/usr/bin/env python3
"""RES-3699 / RES-3703: data/backlinks.sqlite for /backlinks/<host>, cut from the Casa job's full table (METHOD.md host priority 1 + 2).
Run on the Casa: python3 build_backlinks_db.py ~/hxlab/work/cc-graph/backlinks.sqlite out.sqlite
Tier 1: our sites and rivals. Tier 2: top 5,000 domains under .eu .fr .de .es .nl .it .pt .be by referring domains. meta carries the graph id."""
import sqlite3, sys
SRC, OUT = sys.argv[1], sys.argv[2]
T1 = "citedby.eu hexaciv.com civiqpass.com resaleiq.dev revalx.eu semrush.com ahrefs.com peec.ai otterly.ai vinted.com vendoo.co nifty.ai moz.com sistrix.com accio.com".split()
TLDS = ("eu", "fr", "de", "es", "nl", "it", "pt", "be")
s = sqlite3.connect(SRC)
hosts = {h: 1 for h in T1}
for tld in TLDS:  # top 5,000 across the eight, not per TLD
    pass
rows = s.execute("select domain, referring_domains from dom order by referring_domains desc").fetchall()
n = 0
for d, r in rows:
    if d.rsplit(".", 1)[-1] in TLDS and d not in hosts:
        hosts[d] = 2; n += 1
        if n >= 5000: break
o = sqlite3.connect(OUT)
o.executescript("create table dom(domain text primary key, referring_domains int, tier int) without rowid; create table bl(domain text, rank int, referrer text, referrer_inlinks int); create table meta(k text primary key, v text);")
for h, t in hosts.items():
    r = s.execute("select referring_domains from dom where domain=?", (h,)).fetchone()
    if r is None: continue
    o.execute("insert into dom values (?,?,?)", (h, r[0], t))
    for i, (ref, inl) in enumerate(s.execute("select referrer, referrer_inlinks from bl where domain=? order by referrer_inlinks desc limit 20", (h,)), 1):
        o.execute("insert into bl values (?,?,?,?)", (h, i, ref, inl))
o.execute("create index bl_d on bl(domain, rank)")
o.executemany("insert into meta values (?,?)", [("graph", "cc-main-2026-aug-sep-oct"), ("domains", "134979706"), ("links", "1817202146"), ("read_on", "2026-10-23")])
o.commit(); print(o.execute("select count(*), sum(tier=1) from dom").fetchone(), o.execute("select count(*) from bl").fetchone())
