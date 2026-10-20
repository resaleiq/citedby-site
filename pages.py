"""/pricing, /faq and /thanks on the shared shell (RES-1335 S2). Standard library only.
Prices are the six price points of PRODUCT-EXCELLENCE 2.3 and live here once (PRICES); test_s2_pages.py checks every price on the page against it.
Starter, Plus and the agency offers have no buy button: they open a mail to hello@citedby.eu until the buyable-state rule (2.3) flips."""
import html
from urllib.parse import quote

import home
import shell
from shell import E

PRICES = {"free": 0, "starter": 29, "plus": 79, "fix": 390, "kit": 59, "workspace": 249}
MAIL = "mailto:hello@citedby.eu?subject="


def eur(n): return f"€{n}"


def _rung(name, sub, bullets, price, unit, label, href, note=""):
    items = "".join(f"<li>{E(b)}</li>" for b in bullets)
    note_html = f'<p class="note">{E(note)}</p>' if note else ""
    return (f'<div class="rung"><div><h3>{E(name)}</h3><p>{E(sub)}</p></div><div class="mid"><details><summary>What is included</summary><ul>{items}</ul></details></div>'
            f'<div class="pr">{eur(price)}<small>{E(unit)}</small></div><div class="go"><a class="btn sec" href="{href}">{E(label)}</a>{note_html}</div></div>')


def pricing(engines):
    t = home.T["en"]
    d = shell.day0()
    live = bool(engines)
    buy = (f'<a class="btn" href="/go/fixpack" rel="noopener">Buy Audit + Fix, {eur(PRICES["fix"])}</a>' if live
           else f'<a class="btn" href="/grade">{E(t["go"])}</a>')
    tell = lambda n: MAIL + quote(f"Tell me when {n} opens")
    ask = lambda n: MAIL + quote(f"About {n}")
    keycard = (f'<section class="keycard" aria-labelledby="af"><div class="kl"><div><p class="pgroup" style="margin:0 0 var(--g2)">Offer 3 · have it done for you</p><h2 id="af">Audit + Fix</h2>'
               f'<p class="sub">The Fix Pack: changes made for you, counted twice</p><div class="price">{eur(PRICES["fix"])}<small>paid once</small></div>{buy}'
               f'<p class="guar">{E(t["g_btn"])} <a href="/refund">{E(t["g_link"])}</a></p></div>'
               f'<div class="kcb"><ul class="two"><li>40 questions, each asked twice, on every assistant we list</li><li>Competitor map: who is named instead of you</li>'
               f'<li>Changes made within 7 days of access, or ready-to-paste files</li><li>Day-30 recount, raw answers as CSV</li></ul>'
               f'</div></div>'
               f'<div class="pic" style="margin:0">{home.sample_html("en")}</div></section>')
    rungs = (
        '<p class="pgroup">Offer 1 · find out</p>'
        + _rung("Free scan", "One site, one snapshot", ["The full count on screen, who is named instead", "No card, no email"], PRICES["free"], "free", "Scan my site, free", "/grade")
        + '<p class="pgroup">Offer 2 · recount it yourself</p>'
        + _rung("Starter", "One site watched, recount every month", ["1 site, 1 market and language", "Monthly recount, before and after"], PRICES["starter"], "per month", "Tell me when it opens", tell("Starter"), "Payments open soon.")
        + _rung("Plus", "Weekly recount, 2 more competitors tracked", ["Everything in Starter", "Weekly recount", "2 more tracked competitors"], PRICES["plus"], "per month", "Tell me when it opens", tell("Plus"), "Payments open soon.")
        + '<p class="pgroup">Offer 4 · for agencies <span>(starting prices, confirmed with the first agencies)</span></p>'
        + _rung("Agency Kit", "Snapshots and leads, no recount per client", ["10 white-label client reports a month", "Embeddable result widget", "No recurring recount per client"], PRICES["kit"], "per month", "Ask about Agency Kit", ask("Agency Kit"))
        + _rung("Agency Workspace", "10 clients watched, with timelines", ["Everything in Kit", "10 clients watched with timelines", "About €24.90 per client"], PRICES["workspace"], "per month", "Ask about Workspace", ask("Agency Workspace")))
    main = (f'<section class="pagehead on-navy"><div class="wrap"><h1>{E(t["offers_h"])}</h1><p class="lede">{E(t["offers"])}</p></div></section>'
            f'<div class="wrap pstack">{keycard}{rungs}<p style="margin-top:var(--g5)"><a class="link" href="/faq">{E(t["faq_all"])}</a></p></div>')
    return shell.document("en", "Prices: CitedBy", "Four offers, every price in euros: a free scan, a recount, Audit + Fix at €390 paid once, and agency plans.", "/pricing", main, current="/pricing")


def faq_list(engines):
    t = home.T["en"]
    extra = [("Do I need an account or an email?", "No. One field, no signup, no email."),
             ("Why a count and not a score out of 100?", "Assistants answer differently from run to run. A count with the raw answers behind it is checkable; a composite score is not.")]
    return extra + home.faq_items("en", engines)


def faq(engines):
    t = home.T["en"]
    items = faq_list(engines)
    ld = [{"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": "en",
           "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}]
    main = (f'<section class="pagehead on-navy"><div class="wrap"><h1>Straight answers before you scan or pay</h1><p class="lede">{E(t["g_btn"])} <a href="/refund">{E(t["g_link"])}</a></p></div></section>'
            f'<section class="sect" style="border-top:0"><div class="wrap"><div class="faq">{home.details(items, first_open=True)}</div></div></section>'
            f'<section class="endcta band"><div class="wrap"><h2>{E(t["end_h"])}</h2><p class="lede">{E(t["micro"])}</p><p><a class="btn" href="/grade">{E(t["go"])}</a></p></div></section>')
    return shell.document("en", "FAQ: CitedBy", "Answers about which assistants CitedBy asks, how the count works, what the Fix Pack includes and what happens after you pay.", "/faq", main, ld=ld, current="/faq")


def thanks():
    main = ('<section class="plain"><div class="wrap"><h1>Payment received</h1>'
            '<p>Thanks, we are running your audit. The report and a private link are emailed to the address you gave, usually within 15 minutes. If nothing arrives, check your spam folder.</p></div></section>')
    return shell.document("en", "Payment received: CitedBy", "Payment received.", "/thanks", main, robots="noindex")


def data():
    """/data index on the shared shell (was a static file on the old stylesheet)."""
    t = home.T["en"]
    ld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": DATA_TITLE, "url": "https://citedby.eu/data", "inLanguage": "en",
           "hasPart": [{"@type": "Dataset", "name": n, "url": "https://citedby.eu" + h} for h, n, _ in DATA_ROWS]}]
    study = ('<li><a href="/data/study-buyer-questions-claude">64 Claude answers to 32 buyer questions in 2 EU niches: who gets linked</a></li>'
             '<li><a href="/data/study-chatgpt-buyer-questions">127 ChatGPT answers to 64 buyer questions in 5 EU niches: who gets linked</a></li>')
    rows = "".join(f'<li><a href="{h}" hreflang="{l}">{E(n)}</a> <span class="src">({E(m)})</span></li>' for h, n, (l, m) in [(h, n, (m.split(",")[0].lower(), m)) for h, n, m in DATA_ROWS])
    main = (f'<section class="pagehead on-navy"><div class="wrap"><h1>Who AI assistants link when buyers ask where to shop</h1>'
            f'<p class="lede">Dated counts from our own runs of Claude and ChatGPT with web search on: which shop sites appear in the answers to buyer questions, by niche and country. Every page shows the questions, the method and the raw counts. Each page names the one assistant it counted.</p></div></section>'
            f'<div class="wrap dlist"><section><h2>Study</h2><ul>{study}</ul></section><section><h2>By niche and country</h2><ul>{rows}</ul></section></div>'
            f'<section class="endcta band"><div class="wrap"><h2>Want the same count for your shop?</h2><p class="lede">{E(t["micro"])}</p><p><a class="btn" href="/grade">{E(t["go"])}</a></p></div></section>')
    return shell.document("en", "CitedBy data: who Claude links when buyers ask where to shop", "Dated counts from our runs of Claude with web search: which shop sites get linked for buyer questions, by niche and country.", "/data", main, ld=ld, current="/data")


DATA_TITLE = "CitedBy data: who Claude links when buyers ask where to shop"
DATA_ROWS = [
             ("/data/matelas-france", "Matelas en ligne en France : les marques que ChatGPT cite", "FR, ChatGPT"),
             ("/data/complements-alimentaires-france", "Compléments alimentaires en France : les marques que ChatGPT cite", "FR, ChatGPT"),
             ("/data/complements-beaute-france", "Compléments beauté et collagène : les marques que ChatGPT cite", "FR, ChatGPT")]
