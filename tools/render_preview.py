#!/usr/bin/env python3
"""Render /pricing, /faq, /data and home to <outdir> as static files with file:// asset links, for screenshots.
Usage: python3 tools/render_preview.py /tmp/preview-dir   (the directory must already hold a copy of public/)"""
import datetime, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import home, pages

out = os.path.abspath(sys.argv[1])
now = datetime.datetime.now(datetime.timezone.utc)
eng = [{"name": n, "route": "API", "tested": now} for n in ("Claude Haiku 4.5", "GPT-5 mini", "Perplexity Sonar", "Grok 4.3", "Mistral Medium 3.1", "Gemini 3.5 Flash-Lite")]
for name, h in (("pricing", pages.pricing(eng)), ("faq", pages.faq(eng)), ("data", pages.data()), ("index", home.render("en", eng))):
    h = h.replace('href="/', f'href="file://{out}/').replace('src="/', f'src="file://{out}/')
    open(os.path.join(out, name + ".html"), "w", encoding="utf-8").write(h)
print("rendered to", out)
