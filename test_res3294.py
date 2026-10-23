"""RES-3294: while the answer-first check is off (/methodology says so), no selling page claims it."""
import glob, os
HERE = os.path.dirname(os.path.abspath(__file__))
BAD = ("answer-first content", "contenu qui répond d'abord", "contenido que responde primero", "Inhalte, die zuerst antworten",
       "inhoud die eerst antwoord geeft", "rewritten answer block", "about pages that get quoted")

def test_no_page_claims_answer_first_check():
    files = glob.glob(os.path.join(HERE, "public", "*.html")) + glob.glob(os.path.join(HERE, "public", "*", "about.html")) + \
        [os.path.join(HERE, "public", n) for n in ("llms.txt", "llms-full.txt")]
    hits = [(os.path.basename(f), b) for f in files for b in BAD if b in open(f, encoding="utf-8").read()]
    assert not hits, hits
