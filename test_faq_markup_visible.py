"""RES-3275 (R10): every question named in a page's FAQPage JSON-LD is written in the page's visible text. CitedBy's own audit flags the same thing as `faq_not_visible`
(it found /ai-visibility-audit marking up 'What is an AI visibility audit?' and 'What does the CitedBy audit cost?' while the page showed other wording)."""
import html, json, pathlib, re

PUBLIC = pathlib.Path(__file__).parent / "public"
norm = lambda s: " ".join(re.findall(r"\w+", html.unescape(re.sub(r"<[^>]+>", " ", s)).lower()))

def faq_names(raw):
    out = []
    def walk(o):
        if isinstance(o, list): [walk(x) for x in o]
        elif isinstance(o, dict):
            if o.get("@type") == "FAQPage":
                me = o.get("mainEntity"); [out.append(q["name"]) for q in (me if isinstance(me, list) else [me] if me else []) if isinstance(q, dict) and isinstance(q.get("name"), str)]
            walk(o.get("@graph"))
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', raw, re.S):
        try: walk(json.loads(b))
        except ValueError: pass
    return out

def test_faq_questions_are_on_the_page():
    bad, n = [], 0
    for f in sorted(PUBLIC.rglob("*.html")):
        raw = f.read_text(encoding="utf-8", errors="replace")
        names = faq_names(raw)
        if not names: continue
        n += 1; text = norm(re.sub(r"<script.*?</script>|<style.*?</style>", " ", raw, flags=re.S))
        bad += [f"{f.relative_to(PUBLIC)}: {q}" for q in names if norm(q) not in text]
    assert n >= 10 and not bad, "\n".join(bad[:20])
