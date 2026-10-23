"""RES-3706: the full /backlinks table (tier 3 = the on-demand rest) is served but never offered to search engines, the indexable pages keep
linking only inside the indexable set, the copy says what the loaded table covers, and the DB path follows the mount."""
import os, re, sqlite3, tempfile
import backlinks as b

SCHEMA = """create table dom(domain text primary key, referring_domains int not null, tier int not null) without rowid;
create table bl(domain text not null, rank int not null, referrer text not null, referrer_inlinks int not null, primary key(domain, rank)) without rowid;
create table meta(k text primary key, v text not null) without rowid;"""


def make_db(path, with_tier3=True):
    c = sqlite3.connect(path)
    c.executescript(SCHEMA)
    doms = [("semrush.com", 68317, 1), ("t2.fr", 4000, 2), ("big.fr", 900, 2)] + ([("t3.de", 150, 3), ("t3b.fr", 120, 3)] if with_tier3 else [])
    c.executemany("insert into dom values (?,?,?)", doms)
    refs = ["big.fr", "t2.fr", "google.com"] + (["t3.de", "t3b.fr"] if with_tier3 else []) + ["r%02d.org" % i for i in range(18)]
    for d, n, t in doms:
        c.executemany("insert into bl values (?,?,?,?)", [(d, i + 1, r, 1000 - i) for i, r in enumerate(refs) if r != d][:20])
    c.executemany("insert into meta values (?,?)", [("graph", "cc-main-2026-aug-sep-oct"), ("domains", "134979706"), ("links", "1817202146"), ("read_on", "2026-10-23")])
    c.commit(); c.close()


def using(path):
    old = b.DB
    b.DB = path
    return old


def test_tier3_page_is_served_with_data_but_noindex():
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "full.sqlite"); make_db(p); old = using(p)
        try:
            code, h = b.host_page("t3.de")
            assert code == 200 and 'content="noindex,follow"' in h and "150 domains link to t3.de" in h and h.count("<tr>") == 21
            for t2 in ("t2.fr", "semrush.com"):
                code, h = b.host_page(t2)
                assert code == 200 and 'name="robots"' not in h, t2
        finally:
            b.DB = old


def test_indexable_pages_link_only_to_indexable_referrers():
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "full.sqlite"); make_db(p); old = using(p)
        try:
            _, h = b.host_page("t2.fr")
            links = set(re.findall(r'href="/backlinks/([^"]+)"', h))
            assert "big.fr" in links and "t3.de" not in links and "t3b.fr" not in links and "google.com" not in links
            assert "t3.de</td>" in h  # still listed, just not a link
            assert b.tier("t3.de") == 3 and b.tier("t2.fr") == 2 and b.tier("semrush.com") == 1 and b.tier("nowhere.fr") == 0
        finally:
            b.DB = old


def test_sitemap_lists_only_tiers_1_and_2():
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "full.sqlite"); make_db(p); old = using(p)
        try:
            s = b.sitemap()
            assert "/backlinks/t2.fr" in s and "/backlinks/semrush.com" in s and "/backlinks/t3.de" not in s and "/backlinks/t3b.fr" not in s
            assert s.count("<url>") == 1 + 3
        finally:
            b.DB = old


def test_copy_says_what_the_loaded_table_covers():
    with tempfile.TemporaryDirectory() as d:
        full, cut = os.path.join(d, "full.sqlite"), os.path.join(d, "cut.sqlite")
        make_db(full); make_db(cut, with_tier3=False); old = b.DB
        try:
            b.DB = full
            idx = b.index_page(); _, nf = b.host_page("unknown-site.fr")
            assert "The lookup covers 5 domains: " + b.COVER_FULL in idx and b.COVER_FULL in nf and "16 more" in nf
            b.DB = cut
            idx = b.index_page(); _, nf = b.host_page("unknown-site.fr")
            assert "The lookup covers 3 domains: " + b.COVER_CUT in idx and b.COVER_CUT in nf and "16 more" not in nf
        finally:
            b.DB = old


def test_db_path_follows_the_mount_and_the_env():
    with tempfile.TemporaryDirectory() as d:
        mount, full = os.path.join(d, "backlinks.sqlite"), os.path.join(d, "src.sqlite")
        make_db(full)
        old_db, old_mount = b.DB, b.DB_MOUNT
        try:
            b.DB, b.DB_MOUNT = None, mount
            assert b._db() == b.DB_BAKED and b.tier("t3.de") == 0                 # no file: the baked cut, no tier 3
            os.rename(full, mount)
            assert b._db() == mount and b.tier("t3.de") == 3                       # file renamed in: the full table, same process, no restart
            b.DB = os.path.join(d, "override.sqlite")
            assert b._db() == b.DB                                                 # explicit override wins
            b.DB = None; os.rename(mount, full)
            assert b._db() == b.DB_BAKED                                           # renamed out: instant rollback
        finally:
            b.DB, b.DB_MOUNT = old_db, old_mount
    assert b.DB_MOUNT == "/backlinks/backlinks.sqlite" and b.DB_BAKED.endswith(os.path.join("data", "backlinks.sqlite"))
