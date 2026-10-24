"""RES-3819 (decision RES-3801 B): hosts in data/backlinks-hide-adult.txt are left out of every /backlinks/<host> list, shipped table and full table, by exact match.
Run: python3 -m pytest -q test_res3819_backlinks_hide_adult.py"""
import html, os, re, sqlite3
import pytest
import backlinks as b
import backlinks_i18n as i

HERE = os.path.dirname(os.path.abspath(__file__))
HIDE = {l.strip() for l in open(os.path.join(HERE, "data", "backlinks-hide-adult.txt"), encoding="utf-8") if l.strip() and not l.startswith("#")}


def text(h):
    return html.unescape(re.sub(r"<[^>]+>", " ", h[h.index("<body"):]))


def full_db(path, rows):
    c = sqlite3.connect(path)
    c.executescript("create table dom(domain text primary key, referring_domains int); create table bl(domain text, referrer text, referrer_inlinks int); create index b on bl(domain);")
    for d, (n, refs) in rows.items():
        c.execute("insert into dom values (?,?)", (d, n))
        c.executemany("insert into bl values (?,?,?)", [(d, r, x) for r, x in refs])
    c.commit(); c.close()


def test_list_is_loaded_exactly():
    assert len(HIDE) == 356 and "xxxbold.com" in HIDE and "pornic.com" not in HIDE
    assert b.HIDE_ADULT == frozenset(HIDE)


def test_shipped_pages_never_list_a_hidden_host_and_keep_the_rest_in_order():
    c = sqlite3.connect("file:%s?mode=ro" % b.DB, uri=True)
    raw = {}
    for d, r, inl in c.execute("select domain, referrer, referrer_inlinks from bl order by domain, rank"):
        raw.setdefault(d, []).append((r, inl))
    hit = [d for d, rows in raw.items() if any(r in HIDE for r, _ in rows)]
    assert len(hit) == 103   # RES-3899: the file holds each host's 80 strongest referrers now (73 hosts had one in the first 20)
    com = b.commons()
    for d in hit:
        n, rows = b.lookup(d)
        assert not [r for _, r, _ in rows if r in HIDE]
        assert [(r, x) for _, r, x in rows] == [(r, x) for r, x in raw[d] if r not in HIDE and r not in com][:b.SHOWN]     # same order, only the hidden and the folded (common) hosts dropped
        assert [k for k, _, _ in rows] == list(range(1, len(rows) + 1))                        # ranks close up
        assert not [r for r in b.split(d)[2] if r in HIDE]                                      # nor does the folded line name one
        h = b.host_page(d)[1]
        assert not [x for x in HIDE if re.search(r"(?<![a-z0-9.-])%s(?![a-z0-9-])" % re.escape(x), text(h))]


def test_a_reviewed_false_positive_still_shows():
    c = sqlite3.connect("file:%s?mode=ro" % b.DB, uri=True)
    d = c.execute("select domain from bl where referrer='pornic.com' order by domain").fetchone()[0]
    assert "pornic.com" in [r for _, r, _ in b.lookup(d)[1]]
    assert "pornic.com</td>" in b.host_page(d)[1]


def test_full_table_pages_drop_hidden_hosts_and_show_up_to_30_of_the_rest(tmp_path, monkeypatch):
    p = str(tmp_path / "backlinks.sqlite")
    ok = [("ok%02d.de" % k, 1000 - k) for k in range(25)]
    full_db(p, {"viele.de": (400, [("xxxbold.com", 5000), ("1st4bdsm.com", 4999)] + ok), "wenige.de": (150, [("xxxbold.com", 9), ("pornic.com", 8)])})
    monkeypatch.setattr(b, "FULL_DB", p)
    n, rows = b.lookup("viele.de")
    assert n == 400 and [r for _, r, _ in rows] == [r for r, _ in ok[:25]] and [k for k, _, _ in rows] == list(range(1, 26))
    n, rows = b.lookup("wenige.de")
    assert rows == [(1, "pornic.com", 8)]
    t = text(b.host_page("wenige.de")[1])
    assert "xxxbold.com" not in t and "pornic.com" in t and "Below are 1 of the strongest" in t


def test_match_is_exact_not_a_keyword_or_substring(tmp_path, monkeypatch):
    p = str(tmp_path / "backlinks.sqlite")
    full_db(p, {"x.de": (100, [("xxxbold.com", 3), ("sub.xxxbold.com", 2), ("xxxbold.com.evil.example", 1), ("XXXLUTZ.de", 1), ("sexybank.de", 1)])})
    monkeypatch.setattr(b, "FULL_DB", p)
    assert [r for _, r, _ in b.lookup("x.de")[1]] == ["sub.xxxbold.com", "XXXLUTZ.de", "sexybank.de", "xxxbold.com.evil.example"]


def test_every_locale_says_it():
    for lg in ("en", "fr", "de", "es", "nl"):
        m = i.T[lg]["method"]
        assert "30" in m and "{graph}" in m, lg
    assert "Adult-content domains are left out of the list, so a page can show fewer than 30. Spam and link-network domains are shown as they are." in i.T["en"]["method"]
    assert "moins de 30" in b.method_page("fr")   # RES-3899: the method text is on /fr/backlinks/method only
