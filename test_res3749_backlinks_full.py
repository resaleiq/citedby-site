"""RES-3749 part C: hosts outside the 5,011 shipped ones are answered from the full Casa table (/backlinks/backlinks.sqlite on the server, RES-3706): noindex, honest about coverage,
the shipped set always wins, a missing or broken file falls back to the shipped set. Run: python3 -m pytest -q test_res3749_backlinks_full.py"""
import html, json, os, re, sqlite3, tempfile
import pytest
import backlinks as b
import backlinks_i18n as i

ROWS = {  # domain: (referring_domains, [(referrer, referrer_inlinks)])  the Casa schema: dom, bl, index b on bl(domain); no rank, tier or meta
    "mittelstand-beispiel.de": (130, [("google.de", 400087), ("zeta-nur-hier.fr", 500), ("alpha-nur-hier.es", 500), ("unbekannt-irgendwo.com", 9000), ("semrush.com", 68317), ("slotmark1055.de", 300), ("lotto-beispiel.fr", 200)]),
    "kleine-seite.pl": (101, [("semrush.com", 68317)]),
    "einzelner-link.se": (100, []),
    "semrush.com": (999, [("only-in-full.example", 1)]),   # also in the shipped file: the shipped file must win
    "zeta-nur-hier.fr": (222, [("google.de", 10)]),
    "alpha-nur-hier.es": (111, [("google.de", 10)]),
    "slotmark1055.de": (120, [("google.de", 10)]),         # a casino-network name that exists in the full table (RES-3801: gambling and adult names are plain text, never links)
    "lotto-beispiel.fr": (140, [("google.de", 10)]),
}


def make_full(path, rows=ROWS):
    c = sqlite3.connect(path)
    c.executescript("create table dom(domain text primary key, referring_domains int); create table bl(domain text, referrer text, referrer_inlinks int); create index b on bl(domain);")
    for d, (n, refs) in rows.items():
        c.execute("insert into dom values (?,?)", (d, n))
        c.executemany("insert into bl values (?,?,?)", [(d, r, x) for r, x in refs])
    c.commit(); c.close()


@pytest.fixture()
def full(tmp_path, monkeypatch):
    p = str(tmp_path / "backlinks.sqlite")
    make_full(p)
    monkeypatch.setattr(b, "FULL_DB", p)
    return p


def text(h):
    body = h[h.index("<body"):]
    return html.unescape(re.sub(r"[ \t\r\n]+", " ", re.sub(r"<[^>]+>", " ", re.sub(r"(?s)<script.*?</script>", " ", body))))


def test_lookup_reads_the_full_table_when_the_shipped_file_has_no_row(full):
    assert "google.de" in b.commons()   # RES-3899: one of the referrers that go into the folded line, whatever host lists it
    n, rows = b.lookup("mittelstand-beispiel.de")
    assert n == 130
    # strongest first; equal strength alphabetical, so the page does not reshuffle between requests; google.de is folded, ranks close up
    assert rows == [(1, "semrush.com", 68317), (2, "unbekannt-irgendwo.com", 9000), (3, "alpha-nur-hier.es", 500), (4, "zeta-nur-hier.fr", 500),
                    (5, "slotmark1055.de", 300), (6, "lotto-beispiel.fr", 200)]
    assert b.split("mittelstand-beispiel.de")[2] == ["google.de"]
    assert b.lookup("einzelner-link.se") == (100, [])
    assert b.lookup("not-in-either.de") is None


def test_the_shipped_set_wins_and_stays_indexable(full):
    n, rows = b.lookup("semrush.com")
    assert n == 68317 and len(rows) == b.SHOWN             # not the 999 of the fixture
    code, h = b.host_page("semrush.com")
    assert 'name="robots"' not in h and 'type="application/ld+json"' in h and 'hreflang="fr"' in h


def test_on_demand_page_answers_like_the_others_but_is_noindex_without_schema_or_alternates(full):
    code, h = b.host_page("mittelstand-beispiel.de")
    t = text(h)
    assert code == 200 and '<meta name="robots" content="noindex,follow">' in h
    assert "130 domains link to mittelstand-beispiel.de in the latest Common Crawl web graph" in t and t.index("130 domains") < 0.35 * len(t)
    assert 'type="application/ld+json"' not in h and 'rel="alternate" hreflang' not in h
    assert '<link rel="canonical" href="https://citedby.eu/backlinks/mittelstand-beispiel.de">' in h
    assert h.count("<tr>") == 1 + 6 and "Common Crawl samples the web" not in t and 'href="/backlinks/method">Method and limits</a>' in h
    assert "Left out of the table because they link to many domains in this data, for example: google.de." in t
    assert 'href="/?url=mittelstand-beispiel.de&amp;utm_source=citedby_backlinks' in h
    assert '<a href="/backlinks/mittelstand-beispiel.de" hreflang="en" lang="en" aria-current="true">English</a>' in h     # the language switch stays


def test_referrers_link_when_the_page_exists_in_either_file(full):
    h = b.host_page("mittelstand-beispiel.de")[1]
    assert '<a href="/backlinks/semrush.com">semrush.com</a>' in h              # shipped file
    assert '<a href="/backlinks/google.de">' not in h and "<td data-label=\"Referring domain\">google.de" not in h   # folded: named in one line, not a row
    assert '<a href="/backlinks/zeta-nur-hier.fr">zeta-nur-hier.fr</a>' in h   # full file only
    assert "unbekannt-irgendwo.com</td>" in h and "/backlinks/unbekannt-irgendwo.com" not in h   # in neither: plain text, no dead link


def test_gambling_and_adult_named_referrers_are_plain_text_never_links(full):   # RES-3801 is open: until it is decided the live rule stays "plain text, never links"
    h = b.host_page("mittelstand-beispiel.de")[1]
    assert "slotmark1055.de</td>" in h and "lotto-beispiel.fr</td>" in h
    assert "/backlinks/slotmark1055.de" not in h and "/backlinks/lotto-beispiel.fr" not in h
    assert '<a href="/backlinks/alpha-nur-hier.es">alpha-nur-hier.es</a>' in h          # an ordinary name in the same table still links
    sh = b.host_page("semrush.com")[1]
    for ref in re.findall(r'href="/backlinks/([^"]+)"', sh):
        assert not b.LINK_DENY.search(ref), ref
    for word in ("casino", "slot", "xxx", "poker", "escort", "viagra", "payday"):
        assert b.LINK_DENY.search(f"my{word}site.de"), word
    for ok in ("betaworks.de", "bettercloud.fr", "betweenus.nl", "bets-club.de", "wikipedia.org", "europa.eu"):
        assert not b.LINK_DENY.search(ok), ok                                            # the scan's own exceptions: bet followed by a, ter, ween or s


def test_a_host_in_neither_file_is_not_a_zero_and_says_what_the_set_covers(full):
    code, h = b.host_page("not-in-either.de")
    t = text(h)
    assert code == 200 and 'content="noindex,follow"' in h
    assert "every domain with at least 100 referring domains in the graph under .eu or under the country domains of the EU and the UK" in t
    assert "covers 8 domains" in t                                              # the count of the loaded full table, read from the file
    assert ".com" in t and "Common Crawl found no linking domains" not in t     # never a zero


def test_index_page_counts_and_lists_from_the_full_table(full):
    t = text(b.index_page())
    assert "The lookup covers 8 domains: every domain with at least 100 referring domains in the graph under .eu or under the country domains of the EU and the UK" in t
    assert b.index_page().index("zeta-nur-hier.fr") > 0                      # the most-linked list comes from the full table
    assert "Most-linked sites in the data" in t and "Most-linked EU sites" not in t


def test_the_index_list_skips_flagged_names_too(full):
    h = b.index_page()
    assert "slotmark1055.de" not in h and "lotto-beispiel.fr" not in h and "mittelstand-beispiel.de" in h


def test_without_the_file_nothing_changes(monkeypatch, tmp_path):
    monkeypatch.setattr(b, "FULL_DB", str(tmp_path / "missing.sqlite"))
    assert b.lookup("mittelstand-beispiel.de") is None
    code, h = b.host_page("mittelstand-beispiel.de")
    assert code == 200 and "not in the set we have loaded yet" in text(h) and 'content="noindex,follow"' in h
    assert "The lookup covers 5,011 domains: our own sites" in text(b.index_page())


def test_a_broken_file_falls_back_instead_of_failing(monkeypatch, tmp_path):
    for content in (b"this is not a database" * 100, b"", b"SQLite format 3\x00" + b"\x00" * 200):
        p = tmp_path / "bad.sqlite"
        p.write_bytes(content)
        monkeypatch.setattr(b, "FULL_DB", str(p))
        assert b.lookup("mittelstand-beispiel.de") is None
        assert b.host_page("mittelstand-beispiel.de")[0] == 200
        assert "5,011 domains" in text(b.index_page())
    q = sqlite3.connect(str(tmp_path / "wrong.sqlite")); q.execute("create table other(x)"); q.commit(); q.close()   # a valid database without our tables
    monkeypatch.setattr(b, "FULL_DB", str(tmp_path / "wrong.sqlite"))
    assert b.lookup("mittelstand-beispiel.de") is None and b.host_page("mittelstand-beispiel.de")[0] == 200


def test_a_replaced_file_is_picked_up_without_a_restart(tmp_path, monkeypatch):
    p = str(tmp_path / "backlinks.sqlite")
    make_full(p, {"alt-seite.de": (150, [("google.de", 1)]), "zweite-seite.de": (160, [])})
    monkeypatch.setattr(b, "FULL_DB", p)
    assert b.lookup("alt-seite.de")[0] == 150 and "covers 2 domains" in text(b.index_page())
    new = str(tmp_path / "new.sqlite")
    make_full(new, {"alt-seite.de": (155, [("google.de", 1)]), "zweite-seite.de": (160, []), "neue-seite.de": (170, [])})
    os.replace(new, p)                                                         # how the file arrives on the server: a rename
    assert b.lookup("alt-seite.de")[0] == 155 and b.lookup("neue-seite.de")[0] == 170
    assert "covers 3 domains" in text(b.index_page())


def test_every_language_gets_the_on_demand_texts(full):
    for lg in ("fr", "de", "es", "nl"):
        code, h = b.host_page("mittelstand-beispiel.de", lg)
        t = text(h)
        assert code == 200 and 'content="noindex,follow"' in h and f'<html lang="{lg}">' in h, lg
        assert i.fmt(130, lg) in t and "Who links to" not in t and "Common Crawl samples the web" not in t, lg
        n = text(b.host_page("not-in-either.de", lg)[1])
        assert "100" in n and ".com" in n and "not in the set" not in n and "Who links to" not in n, lg
        idx = text(b.index_page("", lg))
        assert "Most-linked" not in idx and "The lookup covers" not in idx and " 8 " in idx, lg
    assert set(i.T["en"]) == set(i.T["fr"]) == set(i.T["de"]) == set(i.T["es"]) == set(i.T["nl"])


def test_the_sitemap_lists_only_the_shipped_hosts(full):
    s = b.sitemap()
    assert s.count("<url>") == 5 * (2 + len(b.hosts()) - len(b.thin_hosts())) and "mittelstand-beispiel.de" not in s


def test_the_full_file_is_only_ever_opened_read_only(full):
    before = os.stat(full)
    b.host_page("mittelstand-beispiel.de"); b.index_page(); b.lookup("kleine-seite.pl")
    after = os.stat(full)
    assert (before.st_mtime_ns, before.st_size) == (after.st_mtime_ns, after.st_size)
    assert not [f for f in os.listdir(os.path.dirname(full)) if f.endswith(("-wal", "-shm", "-journal"))]
