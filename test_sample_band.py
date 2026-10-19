"""RES-1785: the sample numbers on the five home pages are the ones in data/sample_facts.json, which tools/refresh_sample_band.py reads from the sample audit."""
import json, os, re, tempfile

import pytest

ROOT = os.path.dirname(os.path.abspath(__file__))
F = json.load(open(os.path.join(ROOT, "data", "sample_facts.json")))
FILES = {"en": "landing.html", "fr": "landing.fr.html", "nl": "landing.nl.html", "de": "landing.de.html", "es": "landing.es.html"}


@pytest.mark.parametrize("lang", list(FILES))
def test_band_matches_the_snapshot(lang):
    import sys; sys.path.insert(0, os.path.join(ROOT, "tools")); import refresh_sample_band as R
    t = open(os.path.join(ROOT, "public", FILES[lang]), encoding="utf-8").read()
    assert R.apply(t, lang, F) == t, "run python3 tools/refresh_sample_band.py after a re-crawl"          # idempotent: nothing typed differs from the audit
    assert f'<div class="n">{F["score"]} <small>' in t and f'<b>{F["pages"]}</b>' in t and F["example"]["path"] in t
    assert "403 pages" not in t.replace(f'{F["pages"]} pages', "") or F["pages"] == 403
    assert R.date(F["ts"], lang) in t


def test_no_stale_numbers_from_the_first_sample_remain():
    for name in FILES.values():
        t = open(os.path.join(ROOT, "public", name), encoding="utf-8").read()
        assert "27 pages" not in t and "27 pagina" not in t and "27 Seiten" not in t and "27 páginas" not in t and "18 Oct" not in t and "A- 91" not in t
