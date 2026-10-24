"""RES-3708: the WordPress plugin zip, its Playground blueprint and the /wordpress-plugin page. Run: python3.12 -m pytest -q test_res3708_plugin.py"""
import http.client, io, json, os, re, tempfile, threading, zipfile
os.environ.update(OPTIN_SECRET="x" * 40, BASE_URL="http://t", DATA_DIR=tempfile.mkdtemp())
import server

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "wp-plugin", "citedby-ai-search-check")
srv = server.ThreadingHTTPServer(("127.0.0.1", 0), server.H)
threading.Thread(target=srv.serve_forever, daemon=True).start()


def get(path):
    c = http.client.HTTPConnection("127.0.0.1", srv.server_port, timeout=20)
    c.request("GET", path)
    r = c.getresponse()
    return r.status, {k.lower(): v for k, v in r.getheaders()}, r.read()


def version():
    return re.search(r"^ \* Version:\s*(\S+)", open(os.path.join(SRC, "citedby-ai-search-check.php")).read(), re.M).group(1)


def test_versions_agree_and_zip_matches_source():
    v = version()
    assert re.search(rf"^Stable tag: {re.escape(v)}$", open(os.path.join(SRC, "readme.txt")).read(), re.M)
    assert f"define( 'CITEDBY_ASC_VERSION', '{v}' )" in open(os.path.join(SRC, "citedby-ai-search-check.php")).read()
    st, hd, body = get(f"/downloads/citedby-ai-search-check-{v}.zip")
    assert st == 200 and hd["content-type"].startswith("application/zip") and hd["access-control-allow-origin"] == "*"
    z = zipfile.ZipFile(io.BytesIO(body))
    names = {n for n in z.namelist() if not n.endswith("/")}
    src = {"citedby-ai-search-check/" + os.path.relpath(os.path.join(d, f), SRC) for d, _, fs in os.walk(SRC) for f in fs}
    assert names == src
    for n in names:
        assert z.read(n) == open(os.path.join(SRC, n.split("/", 1)[1]), "rb").read(), n


def test_blueprint_points_at_the_zip_with_cors():
    st, hd, body = get("/downloads/citedby-ai-search-check.blueprint.json")
    assert st == 200 and hd["access-control-allow-origin"] == "*"
    bp = json.loads(body)
    step = bp["steps"][0]
    assert step["step"] == "installPlugin" and step["pluginData"]["url"] == f"https://citedby.eu/downloads/citedby-ai-search-check-{version()}.zip"
    assert bp["landingPage"].endswith("page=citedby-ai-search-check")


def test_other_files_have_no_cors():
    assert "access-control-allow-origin" not in get("/mcp-server")[1]


def test_page_listed_and_honest():
    st, hd, body = get("/wordpress-plugin")
    t = body.decode()
    assert st == 200 and "<h1>CitedBy AI-Search Check for WordPress</h1>" in t and 'rel="canonical" href="https://citedby.eu/wordpress-plugin"' in t
    assert f"citedby-ai-search-check-{version()}.zip" in t and "playground.wordpress.net/?blueprint-url=" in t
    assert not re.search(r"AI-powered|powered by AI|\bClaude\b(?!Bot|-SearchBot)", t)
    assert "<loc>https://citedby.eu/wordpress-plugin</loc>" in open(os.path.join(HERE, "public", "sitemap.xml")).read()
    assert "https://citedby.eu/wordpress-plugin" in open(os.path.join(HERE, "public", "llms.txt")).read()


def test_readme_has_no_ai_powered_wording():
    for f in ("readme.txt", "citedby-ai-search-check.php", "includes/class-citedby-asc-admin.php"):
        assert not re.search(r"AI-powered|powered by AI", open(os.path.join(SRC, f)).read(), re.I), f
