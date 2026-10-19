#!/usr/bin/env python3
"""RES-1785: rewrite the sample numbers on the home pages from the public sample audit, so nothing about the sample is typed by hand.
    python3 tools/refresh_sample_band.py [https://citedby.eu/api/sample-facts | facts.json]
Fetches the facts (default: the live app endpoint), saves them as data/sample_facts.json and rewrites the product band, the hero label and the caption in
public/landing{,.fr,.nl,.de,.es}.html. test_sample_band.py fails when the pages and the snapshot disagree. Run it after every re-crawl of the sample."""
import html, json, os, re, sys, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = {"en": "landing.html", "fr": "landing.fr.html", "nl": "landing.nl.html", "de": "landing.de.html", "es": "landing.es.html"}
MON = {"en": "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec", "fr": "janv. févr. mars avr. mai juin juil. août sept. oct. nov. déc.", "nl": "jan. feb. mrt. apr. mei jun. jul. aug. sep. okt. nov. dec.",
       "de": "Jan. Feb. März Apr. Mai Juni Juli Aug. Sept. Okt. Nov. Dez.", "es": "ene. feb. mar. abr. may. jun. jul. ago. sept. oct. nov. dic."}
SEV = {"en": {"error": "Error", "warning": "Warning", "notice": "Notice"}, "fr": {"error": "Erreur", "warning": "Avertissement", "notice": "Info"}, "nl": {"error": "Fout", "warning": "Waarschuwing", "notice": "Opmerking"},
       "de": {"error": "Fehler", "warning": "Warnung", "notice": "Hinweis"}, "es": {"error": "Error", "warning": "Aviso", "notice": "Aviso"}}
PG = {"en": ("page", "pages"), "fr": ("page", "pages"), "nl": ("pagina", "pagina's"), "de": ("Seite", "Seiten"), "es": ("página", "páginas")}
ONE_OF = {"en": "one of {n} pages, fix written from this page's own text", "fr": "une des {n} pages, correction écrite d'après le texte de cette page", "nl": "een van {n} pagina's, oplossing geschreven op basis van de tekst van deze pagina",
          "de": "eine von {n} Seiten, Lösung aus dem Text dieser Seite geschrieben", "es": "una de {n} páginas, solución escrita con el texto de esta página"}
ARIA = {"en": "Health score {s} out of 100", "fr": "Score de santé {s} sur 100", "nl": "Gezondheidsscore {s} van 100", "de": "Gesundheitswert {s} von 100", "es": "Puntuación de salud {s} sobre 100"}

def date(ts, lang, short=False):
    t = time.gmtime(ts); m = MON[lang].split()[t.tm_mon - 1]
    if short and lang == "nl": m = m.rstrip(".")
    d = f"{t.tm_mday}." if lang == "de" else str(t.tm_mday)
    return f"{d} {m}" + ("" if short else f" {t.tm_year}")

def apply(t, lang, f):
    def sub(pat, fn, s, count=1, flags=re.S):
        out, k = re.subn(pat, fn, s, count=count, flags=flags)
        if k != count: raise SystemExit(f"{lang}: pattern {pat[:50]!r} matched {k} times, wanted {count}")
        return out
    sc = f["score"]; circ = 289.0
    t = sub(r'(<div class="bar2">[^<]*\([^,)]*, )[^)]*(\)</div>)', lambda m: m[1] + date(f["ts"], lang, True) + m[2], t)
    t = sub(r'(on|le|op|am|el) \d{1,2}\.? [^ <]+ 2026\.( \S+ )', lambda m: f"{m[1]} {date(f['ts'], lang)}.{m[2]}", t)
    t = sub(r'(<p class="mut" style="max-width:46em">[^<]*?\S+, )\d{1,2}\.? [^ ,<]+ 2026, \d+ ([^.<]+)\.', lambda m: f"{m[1]}{date(f['ts'], lang)}, {f['pages']} {m[2]}.", t)
    t = sub(r'stroke-dashoffset="[\d.]+"', f'stroke-dashoffset="{circ * (1 - sc / 100):.1f}"', t)
    t = sub(r'(<svg viewBox="0 0 112 112" role="img" aria-label=")[^"]*(")', lambda m: m[1] + ARIA[lang].format(s=sc) + m[2], t)
    t = sub(r'(font-weight="600" fill="#0F1B2D">)[^<]*(</text>)', lambda m: m[1] + html.escape(f["grade"]) + m[2], t)
    t = sub(r'(<div class="n">)\d+( <small>)', lambda m: f"{m[1]}{sc}{m[2]}", t)
    t = sub(r'(<div class="pbc"><span><b>)\d+(</b>[^<]*</span><span><b>)\d+(</b>[^<]*</span><span><b>)\d+(</b>)', lambda m: f"{m[1]}{f['errors']}{m[2]}{f['warnings']}{m[3]}{f['notices']}{m[4]}", t)
    t = sub(r'(<b>)\d+(</b> [^<]*</span></div></div></div><h3 style)', lambda m: f"{m[1]}{f['pages']}{m[2]}", t)
    secs = f["sections"]; assert len(secs) == 4
    it = iter(secs)
    def li(m):
        s = next(it); return f'<li class="{"pass" if s["score"] >= 90 else "wn"}">{m[1]}<b>{html.escape(s["grade"])} {s["score"]}</b><i><s style="width:{s["score"]}%"></s></i></li>'
    t = sub(r'<li class="(?:pass|wn|fl)">(<span>[^<]*</span>)<b>[^<]*</b><i><s style="width:\d+%"></s></i></li>', li, t, count=4)
    rows = "".join(f'<tr><td>{c["name"]}</td><td>{{allow}}</td><td>{c["live"]}</td></tr>' for c in f["crawlers"])
    allow = re.search(r'<td>PerplexityBot</td><td>([^<]*)</td>', t)[1]
    assert all(c["robots"] == "allowed" for c in f["crawlers"]), "a crawler is blocked on the sample: write that row by hand"
    t = sub(r'(<table class="pbt">.*?<tbody>).*?(</tbody>)', lambda m: m[1] + rows.replace("{allow}", allow) + m[2], t)
    ex = f["example"]; one = PG[lang][0 if ex["affected"] == 1 else 1]
    t = sub(r'(<div class="pbi"><span class="sv">)[^<]*(</span><b>)[^<]*(</b><span>)[^<]*(</span></div><p class="pgl">[^<]*<code>)[^<]*(</code>)[^<]*(</p>)',
            lambda m: f'{m[1]}{SEV[lang][ex["severity"]]}{m[2]}{html.escape(ex["title"] if lang == "en" else ex["title_l"][lang])}{m[3]}{ex["affected"]} {one}{m[4]}{html.escape(ex["path"])}{m[5]} ({ONE_OF[lang].format(n=ex["affected"])}){m[6]}', t)
    t = sub(r'(<pre><code>).*?(</code></pre>)', lambda m: m[1] + html.escape(ex["code"], quote=True) + m[2], t)
    return t

def main():
    src = sys.argv[1] if len(sys.argv) > 1 else "https://citedby.eu/api/sample-facts"
    f = json.load(open(src)) if os.path.exists(src) else json.load(urllib.request.urlopen(urllib.request.Request(src, headers={"User-Agent": "citedby-site-tool"}), timeout=30))
    json.dump(f, open(os.path.join(ROOT, "data", "sample_facts.json"), "w"), indent=1, ensure_ascii=False)
    for lang, name in FILES.items():
        p = os.path.join(ROOT, "public", name); t = open(p, encoding="utf-8").read()
        new = apply(t, lang, f)
        if new != t: open(p, "w", encoding="utf-8").write(new)
        print(lang, "changed" if new != t else "unchanged")

if __name__ == "__main__": main()
