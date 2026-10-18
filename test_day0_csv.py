import csv, sys
sys.path.insert(0, "tools")
from build_day0_csv import recount, COLS
rows = list(csv.DictReader(open("public/data/day0-citedby-eu.csv", encoding="utf-8")))
assert list(rows[0]) == COLS and len(rows) == 72
assert recount() == (0, 48), recount()
print("day0 csv ok: named 0 of 48")
