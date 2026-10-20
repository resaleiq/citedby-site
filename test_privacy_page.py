import pathlib
P = (pathlib.Path(__file__).parent / "public" / "privacy.html").read_text()

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
    assert "Hetzner Online GmbH (our servers, in Helsinki, Finland, EU)" in open("public/privacy.html").read()


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
    assert "an account ID" in P and "contacts or Google token" in P


def test_privacy_names_slack_and_dns_res2087():
    for needle in ("under your agreement with Slack", "EU-US Data Privacy Framework", "webhook address you give us", "with none set, nothing goes to Slack", "Cloudflare, Inc.", "no account data"):
        assert needle in P, needle


def test_privacy_slack_and_cloudflare_res2196():
    assert "Standard Contractual Clauses) receives our project alerts" not in P
    assert "Slack Technologies Limited" not in P
    assert "check the custom domain for your branded reports" in P
    assert "that site address or domain" in P


def test_privacy_cloudflare_basis_is_dpf_not_sccs_res2198():
    assert "Cloudflare, Inc. (United States, under the EU-US Data Privacy Framework) answers" in P
    assert "Cloudflare, Inc. (United States; Standard Contractual Clauses)" not in P
