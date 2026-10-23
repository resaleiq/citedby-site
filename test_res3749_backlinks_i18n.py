"""RES-3749: /backlinks in fr, de, es, nl. Each page is in its language (no English source string), canonical + hreflang, locale number format, localized shell,
FR typography, answer first, working links in the same language, and the sitemap lists every locale. Run: python3 -m pytest -q test_res3749_backlinks_i18n.py"""
import html, json, os, re, sys
import backlinks as b
import backlinks_i18n as i
import langroutes

LOCALES = ("fr", "de", "es", "nl")
ALL = ("en",) + LOCALES
ENGLISH = ["Who links to", "Referring domain", "Method and limits", "Skip to content", "Look up another domain", "Strongest referring domains", "Common Crawl samples the web",
           "Can search engines", "Sign in", "Pricing", "Legal notice", "No sign-up", "Check semrush.com free", "Most-linked", "Language:", "not in the set"]


def visible(h):
    body = h[h.index("<body"):]
    body = re.sub(r"(?s)<script.*?</script>", " ", body)
    return html.unescape(re.sub(r"[ \t\r\n]+", " ", re.sub(r"<[^>]+>", " ", body)))   # ASCII whitespace only: \s would fold the narrow no-break spaces away


def pages(lg):
    return {
        "known": b.host_page("semrush.com", lg)[1],
        "zero": b.host_page("citedby.eu", lg)[1],
        "unknown": b.host_page("example-unknown-site.fr", lg)[1],
        "index": b.index_page("", lg),
        "index_error": b.index_page(i.T[lg]["bad_host"], lg),
    }


def test_each_page_is_in_its_language_and_has_no_english_source_string():
    for lg in LOCALES:
        for name, h in pages(lg).items():
            t = visible(h)
            assert f'<html lang="{lg}">' in h, (lg, name)
            for s in ENGLISH:
                assert s not in t, (lg, name, s)


def test_canonical_hreflang_and_og_locale():
    for lg in LOCALES:
        code, h = b.host_page("semrush.com", lg)
        assert code == 200
        assert f'<link rel="canonical" href="https://citedby.eu/{lg}/backlinks/semrush.com">' in h
        for l in ALL:
            href = "https://citedby.eu" + ("" if l == "en" else "/" + l) + "/backlinks/semrush.com"
            assert f'<link rel="alternate" hreflang="{l}" href="{href}">' in h, (lg, l)
        assert '<link rel="alternate" hreflang="x-default" href="https://citedby.eu/backlinks/semrush.com">' in h
        assert f'<meta property="og:locale" content="{langroutes.OG_LOCALE[lg]}">' in h
        idx = b.index_page("", lg)
        assert f'<link rel="canonical" href="https://citedby.eu/{lg}/backlinks">' in idx and '<link rel="alternate" hreflang="x-default" href="https://citedby.eu/backlinks">' in idx
    en = b.host_page("semrush.com")[1]
    assert '<link rel="alternate" hreflang="fr" href="https://citedby.eu/fr/backlinks/semrush.com">' in en and '<html lang="en">' in en


def test_noindex_pages_stay_noindex_in_every_language():
    for lg in LOCALES:
        h = b.host_page("example-unknown-site.fr", lg)[1]
        assert 'content="noindex,follow"' in h
        assert 'content="noindex' not in b.host_page("semrush.com", lg)[1]


def test_numbers_use_the_locale_format_and_the_answer_comes_first():
    want = {"fr": "68 317 domaines renvoient vers semrush.com", "de": "68.317 Domains verlinken", "es": "68.317 dominios enlazan a semrush.com", "nl": "68.317 domeinen linken naar semrush.com"}
    for lg, s in want.items():
        t = visible(b.host_page("semrush.com", lg)[1])
        assert s in t, (lg, s)
        assert t.index(s) < 0.45 * len(t), lg
    assert [i.fmt(1234567, lg) for lg in ALL] == ["1,234,567", "1 234 567", "1.234.567", "1.234.567", "1.234.567"]
    assert i.fmt(999, "fr") == "999" and i.fmt(1000, "fr") == "1 000"


def test_form_links_and_cta_stay_in_the_language():
    for lg in LOCALES:
        h = b.host_page("semrush.com", lg)[1]
        assert f'action="/{lg}/backlinks"' in h
        assert f'<a href="/{lg}">CitedBy</a>' in h and f'<a href="/{lg}/backlinks">Backlinks</a>' in h
        assert f'href="/{lg}?url=semrush.com&amp;utm_source=citedby_backlinks&amp;utm_medium=free_tool&amp;utm_campaign=backlinks"' in h
        for ref in re.findall(r'href="/(?:fr|de|es|nl)/backlinks/([^"]+)"', h):
            if ref != "semrush.com":
                assert b.lookup(ref) is not None, ref
        assert not re.search(r'href="/backlinks', re.sub(r'<p class="src langs">.*?</p>', "", h))   # no link back into English except the language switch's English entry
        assert h.count("<tr>") == 21


def test_language_switch_links_the_same_page_in_each_language():
    h = b.host_page("semrush.com", "fr")[1]
    for l, name in (("en", "English"), ("fr", "Français"), ("de", "Deutsch"), ("es", "Español"), ("nl", "Nederlands")):
        href = "/backlinks/semrush.com" if l == "en" else f"/{l}/backlinks/semrush.com"
        assert f'<a href="{href}" hreflang="{l}" lang="{l}"' in h and f">{name}</a>" in h, l
    assert 'aria-current="true"' in h
    assert re.search(r'<a href="/fr/backlinks/semrush.com" hreflang="fr" lang="fr" aria-current="true">', h)
    idx = b.index_page("", "de")
    assert '<a href="/backlinks" hreflang="en" lang="en">English</a>' in idx and 'href="/de/backlinks" hreflang="de" lang="de" aria-current="true"' in idx


def test_shell_is_localized_like_the_other_reading_pages():
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools"))
    import build_legal, docshell
    for lg in LOCALES:
        u, ref = i.UI[lg], build_legal.UI[lg]
        for k in ("check", "plans", "blog", "data", "signin", "cta", "skip", "main", "terms", "privacy", "refund", "contact", "legal", "home", "plans_h", "blog_h"):
            assert u[k] == ref[k], (lg, k)
        assert (u["method"], u["about"]) == docshell.EXTRA[lg]
        h = b.host_page("semrush.com", lg)[1]
        assert f'<a class="sr" href="#main">{u["skip"]}</a>' in h and f'>{u["legal"]}</a>' in h and f'href="/{lg}/privacy"' in h and f'href="/{lg}/terms"' in h
        assert "Legal notice" not in h and "Skip to content" not in h


def test_french_typography_non_breaking_space_before_question_mark_colon_semicolon():
    for name, h in pages("fr").items():
        t = visible(h)
        assert not re.search(r"[^\s ]\?", t), (name, re.findall(r".{12}[^\s ]\?", t))
        assert not re.search(r"(?<=\w) [:;?!]", t), name       # a plain space before : ; ? !
        assert not re.search(r"(?<=\w)[:;!](?= )", t), name     # nothing glued to the word before it
    assert " ?" in visible(b.host_page("semrush.com", "fr")[1])


def test_zero_and_unknown_states_in_each_language():
    zero = {"fr": "aucun domaine référent pour citedby.eu", "de": "keine verweisenden Domains für citedby.eu", "es": "no encontró dominios que enlacen a citedby.eu", "nl": "geen verwijzende domeinen voor citedby.eu"}
    unknown = {"fr": "ne figure pas encore", "de": "gehört noch nicht", "es": "aún no está en el conjunto", "nl": "zit nog niet in de set"}
    for lg in LOCALES:
        z = b.host_page("citedby.eu", lg)[1]
        assert zero[lg] in visible(z) and "<table" not in z, lg
        u = b.host_page("example-unknown-site.fr", lg)
        assert u[0] == 200 and unknown[lg] in visible(u[1]), lg


def test_meta_descriptions_end_at_a_sentence_end_and_stay_short():
    for lg in LOCALES + ("en",):
        for h in (b.host_page("semrush.com", lg)[1], b.host_page("citedby.eu", lg)[1], b.index_page("", lg)):
            d = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', h).group(1))
            assert d.rstrip()[-1] in ".?!" and len(d) <= 165, (lg, len(d), d)
            title = html.unescape(re.search(r"<title>(.*?)</title>", h).group(1))
            assert title.endswith("| CitedBy") and len(title) <= 100, (lg, title)


def test_dataset_schema_is_localized():
    for lg in LOCALES:
        h = b.host_page("semrush.com", lg)[1]
        ld = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S).group(1))
        assert ld["@type"] == "Dataset" and ld["inLanguage"] == lg and ld["url"] == f"https://citedby.eu/{lg}/backlinks/semrush.com"
        assert ld["license"] == "https://commoncrawl.org/terms-of-use" and ld["temporalCoverage"] == "2026-08/2026-10"
        assert "Referring domains of" not in ld["name"]


def test_no_ai_engine_wording_and_register():
    for lg in LOCALES:
        for h in pages(lg).values():
            assert not re.search(r"powered by ai|ai-powered|\bour ai\b|propulsé par l.ia|ki-gestützt|con ia propia|aangedreven door ai", h.lower()), lg
    reg = {"fr": ("vous", r"\btu\b"), "de": ("Sie", r"\bdu\b"), "es": ("tú|tu ", r"\busted\b"), "nl": (r"\bje\b", r"\bu\b")}
    for lg, (yes, no) in reg.items():
        t = visible(b.host_page("citedby.eu", lg)[1])
        assert re.search(yes, t), (lg, "register word missing")
        assert not re.search(no, t), (lg, "wrong register")


def test_sitemap_lists_every_locale():
    s = b.sitemap()
    assert s.count("<url>") == 5 * 5012
    for lg in LOCALES:
        assert f"<loc>https://citedby.eu/{lg}/backlinks</loc>" in s and f"<loc>https://citedby.eu/{lg}/backlinks/semrush.com</loc>" in s
    assert "<loc>https://citedby.eu/backlinks/semrush.com</loc>" in s


def test_plural_and_formats_helpers():
    assert i.plural_key(1) == "one" and i.plural_key(2) == "other" and i.plural_key(0) == "other"
    for lg in ALL:
        assert i.T[lg]["ans_n_one"] and i.T[lg]["desc_n_one"], lg


def test_every_locale_has_every_string():
    keys = set(i.T["en"])
    for lg in LOCALES:
        assert set(i.T[lg]) == keys, (lg, set(i.T[lg]) ^ keys)
        for k, v in i.T[lg].items():
            assert v and (v != i.T["en"][k] or k in ("form_ph", "form_label", "crumb_home", "crumb_bl", "th_rank", "dl_rank")), (lg, k)


def test_independent_language_read_corrections_stay_in(monkeypatch=None):
    """RES-3749: a second reader found calques and one ambiguous scope sentence; they must not come back."""
    bad = {"de": ("Verweisgeber", "Quartals-Graphen", "zitierfähig", "unsere eigenen Seiten", "meistverlinkten Seiten"),
           "es": ("referente", "¿Quién enlaza?", "dominios público"),
           "nl": ("verwijzer ", "verwijzers", "Sterkte is hoeveel"),
           "fr": ("gros référents", "ensemble que nous", "L'ensemble s'élargit", "manquent souvent", "domaines public", "domaines nationaux")}
    for lg, words in bad.items():
        blob = " ".join(i.T[lg].values())
        for w in words:
            assert w not in blob, (lg, w)


def test_the_coverage_sentence_puts_the_threshold_before_the_scope_in_every_language():
    """The Casa selection keeps a domain under .eu or an EU/UK country domain only with 100+ referring domains (select.py); the sentence must not read as "every .eu domain"."""
    for lg in ALL:
        for k in ("top_note_full", "nis_ans_full"):
            t = i.T[lg][k]
            assert "100" in t and ".eu" in t and t.index("100") < t.index(".eu"), (lg, k)


def buttons(h):
    return re.findall(r'<(?:a|button)\b[^>]*class="(btn[^"]*)"[^>]*>', h[h.index("<main"):h.index("</main>")])


def test_one_filled_primary_per_state_in_every_language():
    """Money-path state review (RES-3749): the lookup page's job is the lookup, a host page's job is the free check. Exactly one filled `btn p` in <main> per state; the other button is the outline style."""
    for lg in ALL:
        idx = buttons(b.index_page("", lg))
        assert idx.count("btn p") == 1 and len(idx) == 2, (lg, "index", idx)
        assert buttons(b.index_page(i.T[lg]["bad_host"], lg)).count("btn p") == 1, (lg, "index error")
        for host in ("semrush.com", "citedby.eu", "example-unknown-site.fr"):
            bt = buttons(b.host_page(host, lg)[1])
            assert bt.count("btn p") == 1 and len(bt) == 2, (lg, host, bt)
        h = b.host_page("semrush.com", lg)[1]
        assert re.search(r'<a class="btn p" href="[^"]*utm_campaign=backlinks', h), lg          # the filled one on a host page is the free-check link
        assert re.search(r'<button class="btn" type="submit">', h), lg                          # the lookup button is the outline style there
        assert re.search(r'<button class="btn p" type="submit">', b.index_page("", lg)), lg     # and the filled one on the lookup page


def test_host_page_titles_are_short_enough_to_show_in_search_results():
    """A title is the template plus the host name, so the longest host names give the longest titles: check those in every language (all 25k pages took two minutes)."""
    longest = sorted(b.hosts(), key=len)[-40:]
    worst = 0
    for lg in ALL:
        for host in longest:
            title = html.unescape(re.search(r"<title>(.*?)</title>", b.host_page(host, lg)[1]).group(1))
            worst = max(worst, len(title))
            assert title.endswith("| CitedBy") and len(title) <= 100, (lg, host, len(title))
    assert worst >= 60
    for lg in ALL:                                                                       # a typical host shows whole in a results page (about 60 characters)
        assert len(html.unescape(re.search(r"<title>(.*?)</title>", b.host_page("semrush.com", lg)[1]).group(1))) <= 62, lg


def test_the_outline_cta_button_is_readable_on_the_light_data_css_box():
    """doc.css paints a non-primary `a.btn` in a .cta white-on-navy; data.css turns the .cta box light, so on these pages that button was white on white (found on the live 390 screenshot, RES-3749).
    The pages carry the overriding rule after their stylesheet links, with the same specificity, so it wins by order. A first version of this rule had one class less and lost to doc.css: this string test cannot see that, so
    the contrast of every button is also measured in a real browser before and after a deploy (res3749_btn_contrast.mjs, 4.5 or more)."""
    rule = ".dc .cta a.btn:not(.p){background:#fff;color:var(--navy);border:2px solid var(--navy)}"     # doc.css's own selector, `.dc .cta a.btn:not(.p)`: equal specificity, so source order decides
    for lg in ALL:
        for h in (b.index_page("", lg), b.index_page(i.T[lg]["bad_host"], lg), b.host_page("semrush.com", lg)[1]):
            head = h[:h.index("</head>")]
            assert head.count(rule) == 1, lg
            assert head.index(rule) > head.rindex('rel="stylesheet"'), lg                 # after the three stylesheet links
    h = b.index_page("", "es")
    assert re.search(r'<a class="btn" href="[^"]*utm_campaign=backlinks">', h)               # the lookup page's CTA is the non-primary anchor this rule is for


def test_the_lookup_input_is_a_design_system_field_with_a_44px_touch_height():
    """Web-design standards pass (RES-3749): the lookup input was a bare browser input, 21 px tall with small type (iOS zooms into inputs under 16 px). saas.css has `.fld`: min-height 44, 16 px type, the site's border and radius."""
    for lg in ALL:
        for h in (b.index_page("", lg), b.index_page(i.T[lg]["bad_host"], lg), b.host_page("semrush.com", lg)[1], b.host_page("not-in-the-data.example", lg)[1]):
            assert re.search(r'<input class="fld" id="bl-host" name="host" type="text"', h), lg
            assert 'for="bl-host"' in h, lg                                                          # still labelled
            head = h[:h.index("</head>")]
            assert ".bl-form{display:flex;flex-wrap:wrap;align-items:center;gap:8px 12px}.bl-form .fld{flex:1 1 220px;max-width:420px}" in head, lg


def test_the_language_row_keeps_its_height_when_the_web_font_swaps_in():
    """PSI mobile showed CLS 0.277 on every host page (RES-3749): the language row is two lines (42 px) in the fallback font and one line (21 px) once IBM Plex Sans loads, so everything below it jumped 21 px.
    Its text is right at the wrap boundary for 360 to 412 px phones, so the row reserves two lines on small screens (3em = 2 x the 1.5 line height of 14 px type)."""
    rule = "@media(max-width:480px){.langs{min-height:3em}}"
    for lg in ALL:
        for h in (b.index_page("", lg), b.host_page("semrush.com", lg)[1], b.host_page("citedby.eu", lg)[1], b.host_page("not-in-the-data.example", lg)[1]):
            head = h[:h.index("</head>")]
            assert head.count(rule) == 1, lg
            assert 'class="src langs"' in h, lg
