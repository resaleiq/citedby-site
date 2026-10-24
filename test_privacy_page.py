import pathlib, re
P = (pathlib.Path(__file__).parent / "public" / "privacy.html").read_text()
T = re.sub(r"<[^>]+>", "", P)  # visible text: the v2 page marks provider names up in <strong>

def test_privacy_does_not_deny_the_session_cookie():
    assert "sets no cookies" not in P
    assert "ci_session" in P and "30 days" in P

def test_privacy_covers_accounts_export_delete_and_the_mail_log():
    for needle in ("sign-in", "export", "delete your account", "mail log"):
        assert needle in P.lower().replace("sign in", "sign-in"), needle


def test_privacy_does_not_overclaim_the_export():
    html = open("public/privacy.html", encoding="utf-8").read()
    assert "export everything we hold" not in html
    assert "export your account data" in html


def test_privacy_names_the_server_location_res1909():
    assert "Hetzner Online GmbH (Germany; our servers are in Helsinki, Finland, EU)" in T


def test_privacy_names_every_recipient_res1406():
    for needle in ("OpenRouter", "PostHog", "Forward Email", "Google Ireland", "Resend", "Anthropic Ireland, Limited", "Hetzner", "Stripe Payments Europe"):
        assert needle in P, needle
    assert "These are the only recipients" not in P
    assert "We count anonymous events" not in P


def test_privacy_names_google_sign_in_res1406():
    assert "Continue with Google" in P and "independent controller" in P
    assert "policies.google.com/privacy" in P and "Art. 6(1)(b)" in P
    assert "email address only" in P


def test_privacy_names_all_three_cookies_res1406():
    assert "One cookie exists" not in P
    for needle in ("ci_session", "ci_gstate", "10 minutes", "password-protected shared report", "24 hours"):
        assert needle in P, needle


def test_privacy_google_data_is_stated_exactly_res1406():
    assert "We receive no name, photo, contacts or other Google data" not in P
    assert "openid and email scopes" in T and "contacts or Google token" in T


def test_privacy_names_slack_and_dns_res2087():
    for needle in ("under your agreement with Slack", "EU-US Data Privacy Framework", "webhook address you give us", "With none set, nothing goes to Slack", "Cloudflare, Inc.", "no account data"):
        assert needle in P, needle


def test_privacy_slack_and_cloudflare_res2196():
    assert "Standard Contractual Clauses) receives our project alerts" not in P
    assert "Slack Technologies Limited" not in P
    assert "check the custom domain for your branded reports" in P
    assert "that site address or domain" in P


def test_privacy_cloudflare_basis_is_dpf_not_sccs_res2198():
    assert "Cloudflare, Inc. (United States, under the EU-US Data Privacy Framework): answers" in T
    assert "Cloudflare, Inc. (United States; Standard Contractual Clauses)" not in P


def test_privacy_names_marks_fix_history_verification_and_analytics_fields_res2615():
    for loc in ("", "fr/", "nl/", "de/", "es/"):
        h = open(f"public/{loc}privacy.html", encoding="utf-8").read()
        for needle in ("500", "2.000" if loc in ("nl/", "de/", "es/") else ("2\u202f000" if loc == "fr/" else "2,000"), "300", "utm"):
            assert needle in h, (loc, needle)
        assert h.count("<tr>") >= 17, loc  # header + 16 rows (3 added)


def test_analytics_wording_names_user_agent_not_browser_type_and_report_30_days_res2657():
    for loc in ("", "fr/", "nl/", "de/", "es/"):
        h = open(f"public/{loc}privacy.html", encoding="utf-8").read()
        assert "user-agent" in h.lower() and "ref" in h and "Eén audit" not in h, loc
        for bad in ("language and browser type", "la langue et le type", "browsertaal en browsertype", "Browsersprache und Browsertyp", "el idioma y el tipo"): assert bad not in h, (loc, bad)
    assert "2 000" not in open("public/fr/privacy.html", encoding="utf-8").read()
    for f, bad in (("landing.html", "kept 30 days"), ("landing.fr.html", "conservé 30"), ("landing.nl.html", "30 dagen bewaard"), ("landing.de.html", "30 Tage gespeichert"), ("landing.es.html", "guardado 30"),
                   ("landing.html", "in your account for 30"), ("landing.fr.html", "dans votre compte 30"), ("landing.nl.html", "30 dagen in je account"), ("landing.de.html", "30 Tage in Ihrem Konto"), ("landing.es.html", "en tu cuenta 30")):
        assert bad not in open(f"public/{f}", encoding="utf-8").read(), (f, bad)


def test_res2797_every_locale_names_the_search_engine_recipients_and_rows():
    import re, pathlib
    root = pathlib.Path(__file__).parent / "public"
    pages = {l: (root / l / "privacy.html").read_text() for l in ("", "fr", "de", "es", "nl")}
    n = len(re.findall("<tr>", pages[""]))
    for l, t in pages.items():
        assert len(re.findall("<tr>", t)) == n, l                   # the same table rows in every language
        assert t.count("Microsoft") >= 2 and "Bing Webmaster Tools" in t, l   # section 4 entry and the section 5 transfer list
        assert "Search Console" in t and "4" in t
    assert "and keep no name, photo, contacts or Google token." not in pages[""] and "for sign-in, keep no name" in pages[""]
    assert "We never show the key or token again" not in pages[""] and "last 4 characters" in pages[""]


# RES-3875: agents read logs, support mail and prod records through Claude, so Anthropic gets personal data.
_LOC = {
    "": ("software tools to read server logs, support mail and, read-only, account and payment records", "goes to no one except the processors listed"),
    "fr": ("journaux du serveur, le courrier d'assistance et, en lecture seule, les données de compte et de paiement", "personne d'autre qu'aux sous-traitants énumérés"),
    "de": ("Serverprotokolle, Support-E-Mails und – mit reinem Lesezugriff – Konto- und Zahlungsdaten", "niemanden außer an die aufgeführten Auftragsverarbeiter"),
    "es": ("registros del servidor, el correo de soporte y, con acceso de solo lectura, los datos de cuenta y de pago", "salvo a los encargados del tratamiento indicados"),
    "nl": ("serverlogboeken, supportmail en, met alleen-leestoegang, account- en betalingsgegevens", "aan niemand verstrekt, behalve aan de genoemde verwerkers"),
}
_FALSE = ("It does not receive your email address", "not shared with anyone", "Il ne reçoit ni votre adresse", "rien n'est transmis à des tiers",
          "Es erhält weder Ihre E-Mail", "an niemanden weitergegeben", "No recibe su dirección de correo", "no se comparte con nadie",
          "Ontvangt uw e-mailadres of accountgegevens niet", "met niemand gedeeld")


def test_privacy_anthropic_agent_tools_res3875():
    root = pathlib.Path(__file__).parent / "public"
    for lang, (tools, note) in _LOC.items():
        t = (root / lang / "privacy.html").read_text(encoding="utf-8")
        for bad in _FALSE:
            assert bad not in t, (lang, bad)
        assert tools in t and note in t, lang
        entry = t[t.index("Anthropic Ireland, Limited"):]
        assert tools in entry[: entry.index("OpenRouter")], lang  # the tools use sits in the Anthropic entry
        assert "data processing addendum" not in t.lower() and "avenant" not in t.lower(), lang
