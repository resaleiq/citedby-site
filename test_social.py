import social

PAGE = b'<!doctype html><html lang="en"><meta charset="utf-8"><title>Plans &amp; "prices"</title><meta name="description" content="Crawl every page."><body>x</body></html>'


def test_adds_all_share_tags_from_title_and_description():
    out = social.ensure(PAGE).decode()
    for t in ('property="og:title" content="Plans &amp; &quot;prices&quot;"', 'property="og:description" content="Crawl every page."',
              'property="og:image" content="https://citedby.eu/og-v2.png"', 'name="twitter:card" content="summary_large_image"'):
        assert t in out


def test_keeps_a_page_that_has_its_own():
    own = PAGE.replace(b"<body>", b'<meta property="og:title" content="Own"><meta property="og:image" content="https://citedby.eu/x.png"><meta name="twitter:card" content="summary_large_image"><body>')
    out = social.ensure(own).decode()
    assert out.count('og:title') == 1 and out.count('og:image') == 1 and out.count('twitter:card') == 1


def test_leaves_fragments_and_json_alone():
    assert social.ensure(b'{"a":1}') == b'{"a":1}' and social.ensure(b"<p>hi</p>") == b"<p>hi</p>"
