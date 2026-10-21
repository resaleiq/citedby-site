"""RES-2206 (row 6): drop the coffee and tea cells from the Claude /data study (html, JSON-LD, CSV).
Counts come from the 3 remaining cells' CSV rows, which are byte-identical to the per-cell CSVs (the other cells' pages are untouched).
Numbers: cells 3, answers 48, questions 24, most-linked 19-25%, top-3 17-32%, overlap 32-54%, own-site links 127/242, dead domains 2 (2 answers, 1 cell)
recomputed by the study builder (ventures/citedby/bin/build_data_pages_v2.py) with the five coffee/tea cells excluded."""
import csv, os, re
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(HERE, "public", "data")
KEEP = ("fr-mattress-fr", "fr-supp-fr", "fr-beauty-fr")

# CSV
src = os.path.join(P, "study-buyer-questions-claude.csv")
rows = list(csv.reader(open(src, encoding="utf-8")))
out = [rows[0]] + [r for r in rows[1:] if r[0] in KEEP]
with open(src, "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(out)
print("csv rows", len(rows) - 1, "->", len(out) - 1)

# HTML
f = os.path.join(P, "study-buyer-questions-claude.html")
s = open(f, encoding="utf-8").read()
NICHES = "beauty and collagen supplements, food supplements and mattresses"
OLD_NICHES = "beauty and collagen supplements, food supplements, loose-leaf tea, mattresses and specialty coffee"
rep = [
    ("128 Claude answers to 64 buyer questions in 5 EU niches", "48 Claude answers to 24 buyer questions in 3 EU niches"),
    ("We asked Claude 64 buyer questions", "We asked Claude 24 buyer questions"),
    (OLD_NICHES + " in Belgium, France and Ireland, twice each (128 answers, 18 Oct 2026 to 19 Oct 2026)", NICHES + " in France, twice each (48 answers, 19 Oct 2026)"),
    ("The most-linked shop appears in 19% to 56% of answers", "The most-linked shop appears in 19% to 25% of answers"),
    ("8 niche-and-country cells · 128 answers", "3 niche-and-country cells · 48 answers"),
    ("<h2>The 8 cells</h2>", "<h2>The 3 cells</h2>"),
    ("appears in 19% to 56% of a cell's answers", "appears in 19% to 25% of a cell's answers"),
    ("share only 32% to 77% of the shop sites", "share only 32% to 54% of the shop sites"),
    ("466 of 652 links across the 8 cells (71%)", "127 of 242 links across the 3 cells (52%)"),
    ("Claude linked 4 domains with no working page (confirmed by a second check), in 3 of the 8 cells, 4 times in total.", "Claude linked 2 domains with no working page (confirmed by a second check), in 1 of the 3 cells, 2 times in total."),
    ("64 buyer questions in English, French and Dutch (8 per cell), each asked twice, 128 calls in total. 128 complete answers kept", "24 buyer questions in French (8 per cell), each asked twice, 48 calls in total. 48 complete answers kept"),
    ("5 niches (" + OLD_NICHES + "), 3 countries (Belgium, France and Ireland), 3 languages. 128 answers is a small sample", "3 niches (" + NICHES + "), 1 country (France), 1 language. 48 answers is a small sample"),
    ("runs on 18 Oct 2026 to 19 Oct 2026;", "runs on 19 Oct 2026;"),
    ("we checked which ones load on 18 and 19 Oct 2026", "we checked which ones load on 18 and 19 Oct 2026"),
    ('"dateCreated": "2026-10-18"', '"dateCreated": "2026-10-19"'),
    ('"temporalCoverage": "2026-10-18/2026-10-19"', '"temporalCoverage": "2026-10-19/2026-10-19"'),
]
for a, b in rep:
    if a not in s:
        raise SystemExit("missing: " + a[:80])
    s = s.replace(a, b)
s = s.replace('"dateModified": "2026-10-19"', '"dateModified": "2026-10-20"')
# meta description is the first 158 chars of the answer, as before
m = re.search(r'<meta name="description" content="[^"]*">', s)
ans = re.search(r'"description": "(We asked Claude[^"]*)"', s).group(1)
s = s.replace(m.group(0), '<meta name="description" content="%s">' % ans[:158]).replace(
    re.search(r'<meta property="og:description" content="[^"]*">', s).group(0), '<meta property="og:description" content="%s">' % ans[:158])
open(f, "w", encoding="utf-8").write(s)

# ChatGPT study (retired method): same 3 cells. Its tech-hygiene finding was computed only on the tea/coffee cells and its dead-domain count
# only had coffee/tea hits (builder recompute: 0 dead domains in the 3 cells), so both bullets go.
src = os.path.join(P, "study-chatgpt-buyer-questions.csv")
rows = list(csv.reader(open(src, encoding="utf-8")))
out = [rows[0]] + [r for r in rows[1:] if r[0] in KEEP]
with open(src, "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(out)
print("chatgpt csv rows", len(rows) - 1, "->", len(out) - 1)
f = os.path.join(P, "study-chatgpt-buyer-questions.html")
s = open(f, encoding="utf-8").read()
for pat in (r'<li><span class="tag">Measured</span>Technical hygiene.*?</li>', r'<li><span class="tag">Measured</span>ChatGPT linked 13 domains.*?</li>'):
    s, k = re.subn(pat, "", s, flags=re.S)
    assert k == 1, pat
OLDN = "tea, coffee, mattresses, supplements and beauty supplements in France, Belgium and Ireland, twice each (127 answers, 13 Oct 2026 to 14 Oct 2026)"
rep = [
    ("127 ChatGPT answers to 64 buyer questions in 5 EU niches", "48 ChatGPT answers to 24 buyer questions in 3 EU niches"),
    ("We asked ChatGPT 64 buyer questions about " + OLDN, "We asked ChatGPT 24 buyer questions about mattresses, supplements and beauty supplements in France, twice each (48 answers, 14 Oct 2026)"),
    ("appears in 38% to 88% of answers, and the top three take 26% to 56%", "appears in 38% to 88% of answers, and the top three take 31% to 56%"),
    ("the top three shops take 26% to 56% of shop links", "the top three shops take 31% to 56% of shop links"),
    ("Collected 13 and 14 Oct 2026 from", "Collected 14 Oct 2026 from"),
    ("8 niche-and-country cells · 127 answers", "3 niche-and-country cells · 48 answers"),
    ("<h2>The eight cells</h2>", "<h2>The 3 cells</h2>"),
    ("share only 28% to 61% of the shop sites", "share only 40% to 61% of the shop sites"),
    ("476 of 506 links across the eight cells (94%)", "162 of 171 links across the 3 cells (95%)"),
    ("64 buyer questions in French, Dutch or English (8 per cell), each asked twice in fresh chats. 127 complete answers kept", "24 buyer questions in French (8 per cell), each asked twice in fresh chats. 48 complete answers kept"),
    ("5 niches, 3 countries, 3 languages. 127 answers is a small sample", "3 niches, 1 country, 1 language. 48 answers is a small sample"),
    ("runs from 13 Oct 2026 to 14 Oct 2026;", "runs on 14 Oct 2026;"),
    (" which ones load, and ran the technical checks that day.", " which ones load."),
    ('"dateCreated": "2026-10-13"', '"dateCreated": "2026-10-14"'),
    ('"temporalCoverage": "2026-10-13/2026-10-14"', '"temporalCoverage": "2026-10-14/2026-10-14"'),
]
for a, b in rep:
    if a not in s:
        raise SystemExit("missing: " + a[:80])
    s = s.replace(a, b)
ans = re.search(r'"description": "(We asked ChatGPT[^"]*)"', s).group(1)
s = s.replace(re.search(r'<meta name="description" content="[^"]*">', s).group(0), '<meta name="description" content="%s">' % ans[:158])
s = s.replace(re.search(r'<meta property="og:description" content="[^"]*">', s).group(0), '<meta property="og:description" content="%s">' % ans[:158])
open(f, "w", encoding="utf-8").write(s)
