"""RES-1996: only /privacy may name Anthropic; no model or API id on /data, /methodology or the CSVs."""
import glob, re, sys
BAD = re.compile(r"anthropic|claude-haiku|claude haiku|\bhaiku\b|\bAPI\b|API-|gpt-5|gemini-3|sonar\b", re.I)
files = glob.glob("public/data/*.html") + glob.glob("public/data/*.csv") + ["public/data.html", "public/methodology.html"]
hits = []
for f in files:
    for n, line in enumerate(open(f, encoding="utf-8"), 1):
        if "ai-access-index-2026-10" in f and f.endswith(".csv") and n > 1: continue  # RES-3712: the rows are third-party domain names (api.bg); only the header is ours
        if f.endswith("day0-citedby-eu.csv"):
            line = line.split(",", 1)[0]  # raw answers quote the web; only the header and ids are ours
            if n > 1: continue
        for m in BAD.finditer(line):
            hits.append((f, n, line[max(0, m.start() - 30):m.end() + 30].strip()))
assert not hits, hits[:10]
print("no vendor wording in", len(files), "files")
