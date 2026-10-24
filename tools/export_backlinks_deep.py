#!/usr/bin/env python3
"""RES-3899: the 80 strongest referrers of every shipped host (the first build kept 20), so a page can fold the big platforms into one line and still list 20 of its own.
Casa, after topk80 (topk.c with K 80, targets = the 5,011 hosts of data/backlinks.sqlite) has written top80.tsv:
  python3 export_backlinks_deep.py <cc-graph dir> <res3899 dir> > deep.tsv      # domain, rank, referrer, referrer_inlinks (rank 1 = strongest)
Then, on the Mac: python3 tools/build_backlinks_deep.py deep.tsv data/backlinks.sqlite"""
import gzip, sys
G, J = sys.argv[1], sys.argv[2]
rev = lambda n: ".".join(reversed(n.split(".")))
tg = {}
for l in open(f"{J}/targets.tsv"):
    s, i, n, c = l.rstrip("\n").split("\t"); tg[int(s)] = rev(n)
rows = [tuple(map(int, l.split("\t"))) for l in open(f"{J}/top80.tsv")]
need = {r[1] for r in rows}; nm = {}
with gzip.open(f"{G}/domain-vertices.txt.gz", "rt") as f:
    for line in f:
        i, n, _ = line.split("\t")
        if int(i) in need: nm[int(i)] = rev(n)
by = {}
for t, w, s in rows:
    if w in nm: by.setdefault(tg[t], []).append((s, nm[w]))
for d in sorted(by):
    for r, (s, ref) in enumerate(sorted(by[d], key=lambda x: (-x[0], x[1])), 1):  # strength, then name: the same order on every run (ties in the Casa file are first-seen)
        print(f"{d}\t{r}\t{ref}\t{s}")
