import glob, hashlib, os, re
P = os.path.join(os.path.dirname(__file__), "public")

def test_data_band_button_has_own_fill():
    css = open(os.path.join(P, "data.css")).read()
    assert ".dp .cta .btn.p{background:var(--navy);color:#fff}" in css

def test_data_pages_link_current_data_css():
    v = hashlib.sha256(open(os.path.join(P, "data.css"), "rb").read()).hexdigest()[:8]
    pages = glob.glob(os.path.join(P, "**", "data", "*.html"), recursive=True) + glob.glob(os.path.join(P, "data", "*.html"))
    assert pages
    for f in pages:
        t = open(f).read()
        if "data.css" in t:
            assert "/data.css?v=" + v in t, f
