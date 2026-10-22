"""Home page render rules (RES-873). Run: python3 test_home.py"""
import datetime, json, os, re, tempfile, unittest
import home

NOW = datetime.datetime(2026, 10, 16, 9, 0, tzinfo=datetime.timezone.utc)

def engines_file(rows):
    f = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False); json.dump({"engines": rows}, f); f.close(); return f.name

def live(*names, hours=2):
    t = (NOW - datetime.timedelta(hours=hours)).isoformat()
    return home.live_engines(engines_file([{"name": n, "route": "API", "tested": t} for n in names]), NOW)

class T(unittest.TestCase):
    def test_no_chatgpt_when_not_live(self):
        for lang in ("en", "fr"):
            self.assertEqual(home.render(lang, live("Claude")).lower().count("chatgpt"), 0)

    def test_chatgpt_only_in_engines_rendered_lines(self):
        h = home.render("en", live("Claude", "ChatGPT"))
        lines = [l for l in h.splitlines() if "chatgpt" in l.lower()]
        self.assertTrue(lines)
        self.assertTrue(all('id="engines"' in l or "application/ld+json" in l for l in lines), lines)  # hero line and JSON-LD description, both from engines.json

    def test_every_live_name_present_with_date(self):
        h = home.render("en", live("Claude", "Gemini"))
        self.assertIn("Claude<small>Tested 16 Oct 2026</small></span></li>", h)
        self.assertIn("Gemini<small>Tested 16 Oct 2026</small></span></li>", h)
        self.assertIn("Why several assistants?", h)

    def test_single_engine_has_no_several_faq(self):
        self.assertNotIn("Why several assistants?", home.render("en", live("Claude")))

    def test_stale_engine_dropped(self):
        self.assertEqual(live("Claude", hours=25), [])

    def test_future_or_garbage_dropped(self):
        self.assertEqual(live("Claude", hours=-3), [])
        self.assertEqual(home.live_engines("/nonexistent.json", NOW), [])
        self.assertEqual(home.live_engines(engines_file([{"name": "X", "tested": "not a date"}, {"tested": "2026-10-16T08:00:00Z"}]), NOW), [])

    def test_knowledge_group_never_in_web_search_line(self):
        t = (NOW - datetime.timedelta(hours=2)).isoformat()
        rows = [{"name": "Claude", "route": "API", "tested": t, "group": "web"},
                {"name": "Gemini", "route": "no tools", "tested": t, "group": "knowledge"},
                {"name": "Legacy", "route": "API", "tested": t}]
        got = [e["name"] for e in home.live_engines(engines_file(rows), NOW)]
        self.assertEqual(got, ["Claude", "Legacy"])
        probe = os.path.expanduser("~/work/ventures/citedby/engines.json")
        if os.path.exists(probe):
            raw = json.load(open(probe))
            raw["engines"] = [dict(r, tested=t) for r in raw["engines"]]
            f = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False); json.dump(raw, f); f.close()
            shown = home.live_engines(f.name, NOW)
            h = home.render("en", shown)
            web = {r["name"] for r in raw["engines"] if r.get("group", "web") == "web"}
            knowledge = {r["name"] for r in raw["engines"] if r.get("group", "web") != "web"}
            self.assertEqual({e["name"] for e in shown}, web)
            for n in knowledge:
                self.assertNotIn(n, h)

    def test_empty_renders_fallback_and_no_buy_button(self):
        h = home.render("en", [])
        self.assertIn("We are connecting assistants", h)
        self.assertNotIn("buy.stripe.com/3cI8wHgJK4q9atr9Y98N200", h)
        self.assertNotIn('"price": "390"', h)
        self.assertIn('action="/grade"', h)

    def test_guarantee_text_kept_and_no_monthly(self):
        h = home.render("en", live("Claude"))
        for s in ("What exactly do you guarantee?", "Late changes, full refund.", "No rise at day 30"):
            self.assertIn(s, pages_faq())
        for lang in ("en", "fr"):
            for h in (home.render(lang, live("Claude")), pages_faq()):
                self.assertNotIn("149", h); self.assertNotIn("Monthly", h)

    def test_what_you_sell_uses_the_field_instant_reads(self):
        # RES-1421: /instant prefills category_text, not "what"; the home field must use that name
        for lang in ("en", "fr"):
            h = home.render(lang, live("Claude"))
            self.assertIn('id="sl" name="category_text"', h)
            self.assertNotIn('name="what"', h)
            self.assertNotIn("Read from my site", h); self.assertNotIn("Lu sur mon site", h)

    def test_no_retired_blocks(self):
        h = home.render("en", live("Claude"))
        for s in ("127", "Logged-out", "logged-out"):
            self.assertNotIn(s, h)

    def test_steps_are_the_spec_wording(self):
        h = home.render("en", live("Claude"))
        for s in ("Paste your website address.", "We ask the AI assistants what your buyers ask.", "You get a dated report.", "put to the assistant listed on this page, twice each, today."):
            self.assertIn(s, h)

    def test_step2_count_follows_the_engine_row(self):
        rows = [{"name": f"E{i}", "route": "", "tested": datetime.datetime.now(datetime.timezone.utc)} for i in range(9)]
        for lang, word in (("en", "the nine assistants listed"), ("fr", "neuf assistants listés")):
            self.assertIn(word, home.render(lang, rows))
            self.assertIn(word.replace("nine", "two").replace("neuf", "deux"), home.render(lang, rows[:2]))
            h0 = home.render(lang, [])
            self.assertNotIn("nine", h0.split("hsteps")[1].split("</ol>")[0]); self.assertNotIn("neuf", h0.split("hsteps")[1].split("</ol>")[0])

    def test_no_third_party_sample(self):
        self.assertNotIn("roaster", home.render("en", live("Claude")).lower())

def pages_faq():
    import pages
    return pages.faq(live("Claude", "Gemini"))

if __name__ == "__main__":
    unittest.main()


class LandingVariants(unittest.TestCase):
    def test_trial_wording_follows_the_flag(self):
        import os, tempfile
        os.environ.setdefault("OPTIN_SECRET", "x" * 40); os.environ.setdefault("BASE_URL", "http://t"); os.environ.setdefault("DATA_DIR", tempfile.mkdtemp())
        import server
        raw = open(os.path.join(os.path.dirname(__file__), "public", "landing.html"), encoding="utf-8").read()
        for flag in ("", "1"):
            os.environ["CITEDBY_TRIAL"] = flag; h = server.landing_html(raw)
            self.assertEqual("7-day free trial" in h, flag == "1"); self.assertNotIn("<!--", h); self.assertNotIn("in one click", h.lower())
        os.environ.pop("CITEDBY_TRIAL", None)


def test_res1650_home_names_oai_searchbot_in_every_language():
    import os
    for k in ("", ".fr", ".nl", ".de", ".es"):
        html = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "public", f"landing{k}.html"), encoding="utf-8").read()
        assert "OAI-SearchBot (" in html and "GPTBot (" in html, k


def test_home_org_sameas_matches_about():
    import langroutes
    org = langroutes.LD
    assert '"sameAs": ["https://citedby.eu/about", "https://citedby.eu/methodology"]' in org


class TestHomeJsonLdRes2651(unittest.TestCase):
    def test_no_product_type_on_any_home(self):
        import json, re, langroutes
        m = re.search(r'<script type="application/ld\+json">(.*?)</script>', langroutes.LD)
        types = [n["@type"] for n in json.loads(m.group(1))["@graph"]]
        self.assertNotIn("Product", types)  # Google: merchant listing needs image + availability
        self.assertIn("Service", types)


def test_pricing_redirects_to_plans_in_every_locale_res2790():
    import server
    for l in ("fr", "nl", "de", "es"):
        assert server.LAUNCH_REDIRECTS[f"/{l}/pricing"] == f"/{l}/plans"
    assert server.LAUNCH_REDIRECTS["/pricing"] == "/plans"
    for lang in ("en", "fr"):
        h = home.render(lang, [])
        assert 'href="/pricing"' not in h and 'href="/fr/pricing"' not in h
        assert ("/plans" if lang == "en" else f"/{lang}/plans") in h


class FreeToolsLinks(unittest.TestCase):
    """RES-2857: every landing links, server-rendered, to /tools, both checkers and /bots."""
    def test_footer_links(self):
        import os, re
        pub = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")
        for lang, p in (("", ""), (".fr", "/fr"), (".nl", "/nl"), (".de", "/de"), (".es", "/es")):
            d = open(os.path.join(pub, f"landing{lang}.html"), encoding="utf-8").read()
            foot = d[d.index("<footer"):]
            for h in (f"{p}/tools", f"{p}/tools/ai-crawler-check", f"{p}/tools/llms-txt-checker", "/bots"):
                self.assertIn(f'<a href="{h}">', foot)
