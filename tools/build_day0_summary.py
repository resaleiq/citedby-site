#!/usr/bin/env python3
"""Numbers shown on the site for citedby.eu's own day-0 audit (RES-1228), read from the public raw CSV, never typed by hand.
Usage: python3 tools/build_day0_summary.py   (reads public/data/day0-citedby-eu.csv, writes data/day0.json)"""
import collections, csv, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_day0_csv import recount
CSV = os.path.join(HERE, "..", "public", "data", "day0-citedby-eu.csv")
OUT = os.path.join(HERE, "..", "data", "day0.json")
NAMES = {"claude-haiku-4-5-20251001": "Claude Haiku 4.5", "openai/gpt-5-mini": "GPT-5 mini", "perplexity/sonar": "Perplexity Sonar", "google/gemini-3.5-flash-lite": "Gemini 3.5 Flash-Lite"}
HOST = re.compile(r"https?://(?:www\.)?([^/\s\"',;)]+)")


def summary(path=CSV):
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    cat = [r for r in rows if r["counted"] == "yes"]
    named, total = recount(path)
    cited = collections.Counter(h for r in cat for h in set(HOST.findall(r["urls"])))
    models = sorted({r["model"] for r in rows}, key=lambda m: list(NAMES).index(m) if m in NAMES else 99)
    return {"date": rows[0]["date"], "named": named, "answers": total, "kept": len(rows),
            "linked": sum("citedby.eu" in r["urls"] for r in cat),
            "assistants": [NAMES.get(m, m) for m in models], "questions": len({r["prompt_id"] for r in rows}), "category_questions": len({r["prompt_id"] for r in cat}),
            "cited": sorted(cited.items(), key=lambda kv: (-kv[1], kv[0]))[:5]}


if __name__ == "__main__":
    s = summary()
    json.dump(s, open(OUT, "w"), indent=1, ensure_ascii=False); open(OUT, "a").write("\n")
    print(json.dumps(s, ensure_ascii=False))
