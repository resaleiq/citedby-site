"""RES-4115: the llms.txt generator is a first-class tool page on the site: sitemap (5 languages, hreflang), llms.txt, trust layer, the how-to guide links to it."""
import re, xml.dom.minidom
import proxy, trust

PUB = __import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), "public")
LOCS = ("", "/fr", "/nl", "/de", "/es")


def test_sitemap_lists_the_generator_in_every_language_with_hreflang():
    s = open(f"{PUB}/sitemap.xml", encoding="utf-8").read(); xml.dom.minidom.parseString(s)
    for p in LOCS:
        m = re.search(rf"<url><loc>https://citedby.eu{p}/tools/llms-txt-generator</loc>(.*?)</url>", s); assert m, p
        assert len(re.findall(r'hreflang="(?:en|fr|nl|de|es)"', m.group(1))) == 5 and 'hreflang="x-default" href="https://citedby.eu/tools/llms-txt-generator"' in m.group(1)


def test_llms_txt_names_the_generator_once_with_what_it_does():
    t = open(f"{PUB}/llms.txt", encoding="utf-8").read()
    assert t.count("https://citedby.eu/tools/llms-txt-generator") == 1 and "free, no account" in t.split("llms-txt-generator")[1].split("\n")[0]


def test_generator_pages_get_the_trust_layer_like_the_other_tools():
    assert "llms-txt-generator" in trust.TOOLS and trust.SOURCES["llms-txt-generator"]
    for p in LOCS: assert proxy.ROUTES["GET"].fullmatch(f"{p}/tools/llms-txt-generator") and proxy.INDEXABLE.fullmatch(f"{p}/tools/llms-txt-generator")


def test_how_to_guide_links_to_the_generator():
    h = open(f"{PUB}/blog/how-to-create-an-llms-txt-file.html", encoding="utf-8").read()
    assert h.count('href="/tools/llms-txt-generator"') == 2 and "writes a first draft from your own pages" in h  # a step line and the Keep reading list
