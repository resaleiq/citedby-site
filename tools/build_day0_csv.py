#!/usr/bin/env python3
"""Day-0 own-site audit of citedby.eu (RES-1228) as a public raw CSV, plus the recount.
Usage: build_day0_csv.py <raw-citedby.eu.jsonl> [out.csv]   (writes public/data/day0-citedby-eu.csv)
       build_day0_csv.py --recount [csv]                     (prints 'named X of N')"""
import csv, json, re, sys
OUT = "public/data/day0-citedby-eu.csv"
COLS = ["prompt_id", "counted", "run", "assistant", "prompt", "answer", "urls", "model", "date"]
NAMED = re.compile(r"citedby", re.I)

def build(src, out=OUT):
    rows = {}
    for l in open(src, encoding="utf-8"):
        r = json.loads(l)
        if "error" not in r:
            rows[(r["id"], r["engine"])] = r
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(COLS)
        for (i, e), r in sorted(rows.items()):
            _, q, run = i.split("|")
            counted = "yes" if re.fullmatch(r"q[1-6]", q) else "no"
            w.writerow([f"{q}", counted, run, e, r["prompt"], r["answer"], " ".join(r.get("links", [])), r.get("model", ""), r["ts"][:10]])
    return len(rows)

def recount(path=OUT):
    rows = [r for r in csv.DictReader(open(path, encoding="utf-8")) if r["counted"] == "yes"]
    return sum(bool(NAMED.search(r["answer"])) for r in rows), len(rows)

if __name__ == "__main__":
    if sys.argv[1] == "--recount":
        n, t = recount(*sys.argv[2:3]); print(f"named {n} of {t}")
    else:
        print(build(*sys.argv[1:3]), "rows")
