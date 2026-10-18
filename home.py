"""CitedBy home page (EN, FR), rendered per request from engines.json (RES-1335 S2). Standard library only.
Layout: the B&D v4 mocks (design/systems/citedby/mocks/home-v4.html). Words: PRODUCT-EXCELLENCE section 1.5 (the 3 steps), the live site strings
(FAQ, who is behind this, guarantee line) and the day-0 numbers in data/day0.json (built from the public CSV). The assistant list is data: only an engine whose
last web-grounded test succeeded in the last 24 hours is named anywhere on the page (engine row, JSON-LD, meta). An empty list renders the fallback line
and the buy button gives way to the free scan."""
import datetime, html, json, os

import shell
from shell import E, fmt_date

FIX_URL = "https://buy.stripe.com/3cI8wHgJK4q9atr9Y98N200"
MAX_AGE = datetime.timedelta(hours=24)
HERE = os.path.dirname(os.path.abspath(__file__))


def parse_ts(s):
    d = datetime.datetime.fromisoformat(s.replace("Z", "+00:00"))
    return d if d.tzinfo else d.replace(tzinfo=datetime.timezone.utc)


def live_engines(path, now=None):
    """Engines whose last successful web-grounded test is under 24 hours old. Bad or missing file: none."""
    now = now or datetime.datetime.now(datetime.timezone.utc)
    try:
        rows = json.load(open(path))["engines"]
    except (OSError, ValueError, KeyError, TypeError):
        return []
    out = []
    for r in rows:
        try:
            if r.get("group", "web") != "web":  # knowledge-only rows (no web search) never join the "web search on" line
                continue
            t = parse_ts(r["tested"])
            if r["name"] and datetime.timedelta(0) <= now - t < MAX_AGE:
                out.append({"name": str(r["name"]), "route": str(r.get("route", "")), "tested": t})
        except (KeyError, ValueError, TypeError, AttributeError):
            continue
    return out


def join_names(names, lang):
    if len(names) <= 1: return "".join(names)
    return ", ".join(names[:-1]) + (" et " if lang == "fr" else " and ") + names[-1]


NUM = {"en": {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"},
       "fr": {1: "un", 2: "deux", 3: "trois", 4: "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit", 9: "neuf", 10: "dix"}}

# Existing live text (home FAQ, who is behind this, guarantee line). Edits against the live strings: the Monthly question is gone, the Monthly sentences are gone
# from "What happens after I pay?" (Monthly EUR 149 is archived), and "the line at the top of this page" now says "the list on our home page".
KEEP = {'en': {'faq': [('Which assistants do you check?',
                 'The ones we can ask through an API with web search switched on, on the day you order. The list on our home page is that list, with its date. We do not script the chat apps '
                 'themselves: their consumer terms forbid automated extraction, and we will not build your results on an account that can be banned. When we add an assistant, it joins your recount '
                 'at no charge.'),
                ('Is an API answer what my buyer sees in the app?',
                 'Not always. An API call has no chat history and no personal profile, and the app can answer differently. That is why we ask every question twice, show you each answer and count the '
                 'same way before and after. The count shows change. It does not forecast your traffic.'),
                ('Can you guarantee an assistant will recommend us?',
                 'No. Nobody controls what an assistant answers. We guarantee the work: changes live (or files delivered) within 7 days, and if your count does not rise at the day-30 recount, we '
                 'keep working another 30 days at no charge.'),
                ('Do you need access to my shop?',
                 'For the Fix Pack, yes: a Shopify collaborator request or a CMS login, so we can make the changes. If you prefer, we send every change as ready-to-paste files and you apply them.'),
                ('Why not just use a tracking tool?',
                 'Trackers tell you whether you show up. They do not rewrite your pages, fix wrong facts or ask the guides the assistants read to list you. That work is what you pay us for.'),
                ('Which languages?', 'The free scan runs in English, French, Dutch, German or Spanish. The Fix Pack audit covers up to 2 languages: those five, plus Italian and Portuguese.'),
                ('How fast?', 'The mini-audit arrives within 2 working days. Fix Pack changes go live within 7 days of access, or the files reach you within 7 days, and the recount is at day 30.'),
                ('What exactly do you guarantee?',
                 'Late changes, full refund. If you give us access (a Shopify collaborator request or a CMS login), the changes are live within 7 days. If you choose ready-to-paste files, you get '
                 'them within 7 days. If we miss either date, we refund the €390. You do not have to ask. No rise at day 30, 30 more days free. We ask the same questions again, each twice, and count '
                 'the same way as in your first audit. If your shop is named in no more answers than before, we keep working another 30 days at no charge. We do not promise rankings, traffic or '
                 'sales. Nobody controls what an assistant answers.'),
                ('What happens after I pay?',
                 'Stripe emails your receipt. We email you for access, or for your choice of ready-to-paste files. The 7 days start the day you give us access, or the day you tell us you want the '
                 'files. If we miss the date, the refund is automatic. At day 30 you get the recount, before and after for each assistant, with the raw answers. Nothing renews.')],
        'faq_multi': ('Why several assistants?', 'A shop can be named by one assistant and missed by another, so each gets its own count. Your day-30 recount shows which one you moved on.'),
        'behind_h': 'Who is behind this',
        'behind': 'CitedBy is a small independent service run from Spain. We sell the fixes, which is why every audit lists the sites each assistant linked in each try: you can check our count '
                  'yourself.',
        'legal': 'Legal notice',
        'g_btn': 'Changes live in 7 days or the €390 is refunded. You do not have to ask.',
        'fc': ['16 answers about your category, in your language', 'Who is named instead of you', 'What the assistants say about you by name', '2 to 3 fixes, checked against your site']},
 'fr': {'faq': [('Quels assistants vérifiez-vous ?',
                 "Ceux que nous pouvons interroger par une API, recherche web activée, le jour de votre commande. La liste de notre page d'accueil est cette liste, avec sa date. Nous ne pilotons pas "
                 "les applications de chat elles-mêmes : leurs conditions grand public interdisent l'extraction automatisée, et nous ne bâtirons pas vos résultats sur un compte qui peut être banni. "
                 'Quand nous ajoutons un assistant, il rejoint votre recomptage sans frais.'),
                ("Une réponse d'API est-elle ce que voit mon acheteur dans l'application ?",
                 "Pas toujours. Un appel d'API n'a ni historique de conversation ni profil personnel, et l'application peut répondre autrement. C'est pourquoi nous posons chaque question deux fois, "
                 'vous montrons chaque réponse et comptons de la même façon avant et après. Le compte montre un changement. Il ne prévoit pas votre trafic.'),
                ("Pouvez-vous garantir qu'un assistant nous recommandera ?",
                 "Non. Personne ne contrôle ce qu'un assistant répond. Nous garantissons le travail : changements en ligne (ou fichiers livrés) sous 7 jours, et si votre compte n'a pas augmenté au "
                 'recomptage à 30 jours, nous continuons à travailler 30 jours de plus sans frais.'),
                ("Avez-vous besoin d'accéder à ma boutique ?",
                 'Pour le Fix Pack, oui : une demande de collaborateur Shopify ou un accès CMS, afin de faire les changements. Si vous préférez, nous envoyons chaque changement en fichiers prêts à '
                 'coller et vous les appliquez.'),
                ('Pourquoi pas un simple outil de suivi ?',
                 'Un outil de suivi dit si vous apparaissez. Il ne réécrit pas vos pages, ne corrige pas les faits erronés et ne demande pas aux guides que les assistants lisent de vous référencer. '
                 'Ce travail est ce que vous payez.'),
                ('Quelles langues ?',
                 "Le test gratuit fonctionne en anglais, français, néerlandais, allemand ou espagnol. L'audit du Fix Pack couvre 2 langues au plus : ces cinq-là, plus l'italien et le portugais."),
                ('En combien de temps ?',
                 "Le mini-audit arrive sous 2 jours ouvrés. Les changements du Fix Pack sont en ligne sous 7 jours après l'accès, ou les fichiers vous parviennent sous 7 jours, et le recomptage a "
                 'lieu à 30 jours.'),
                ('Que garantissez-vous exactement ?',
                 "Changements en retard, remboursement total. Si vous nous donnez l'accès (une demande de collaborateur Shopify ou un accès CMS), les changements sont en ligne sous 7 jours. Si vous "
                 "choisissez les fichiers prêts à coller, vous les recevez sous 7 jours. Si nous manquons l'une des deux dates, nous vous remboursons les 390 €. Vous n'avez rien à demander. Pas de "
                 "hausse à 30 jours, 30 jours de plus offerts. Nous reposons les mêmes questions, deux fois chacune, et comptons comme dans votre premier audit. Si votre boutique n'est pas citée "
                 "dans plus de réponses qu'avant, nous continuons à travailler 30 jours de plus sans frais. Nous ne promettons ni classement, ni trafic, ni ventes. Personne ne contrôle ce qu'un "
                 'assistant répond.'),
                ('Que se passe-t-il après le paiement ?',
                 "Stripe vous envoie le reçu. Nous vous écrivons pour obtenir l'accès, ou pour que vous choisissiez les fichiers prêts à coller. Les 7 jours commencent le jour où vous donnez "
                 "l'accès, ou le jour où vous nous dites que vous voulez les fichiers. Si nous manquons la date, le remboursement est automatique. À 30 jours, vous recevez le recomptage, avant et "
                 'après pour chaque assistant, avec les réponses brutes. Rien ne se renouvelle.')],
        'faq_multi': ('Pourquoi plusieurs assistants ?',
                      "Une boutique peut être citée par un assistant et absente d'un autre : chacun a donc son compte. Votre recomptage à 30 jours montre sur lequel vous avez progressé."),
        'behind_h': 'Qui est derrière CitedBy',
        'behind': "CitedBy est un petit service indépendant exploité depuis l'Espagne. Nous vendons les corrections, c'est pourquoi chaque audit liste les sites que chaque assistant a liés à chaque "
                  'essai : vous pouvez vérifier notre compte vous-même.',
        'legal': 'Mentions légales',
        'g_btn': 'Changements en ligne sous 7 jours, sinon les 390 € vous sont remboursés. Sans rien demander.',
        'fc': ['16 réponses sur votre catégorie, dans votre langue',
               'Qui est cité à votre place',
               'Ce que les assistants disent de vous quand on les interroge par votre nom',
               '2 à 3 corrections, vérifiées sur votre site']}}


T = {
 "en": dict(
  path="/", locale="en", nav_current=None,
  title="CitedBy: who do AI assistants name instead of your shop?",
  desc="We ask AI assistants your buyers' questions and count who gets named. Free scan, no email. Then the changes made for you, paid once at €390, and a recount at day 30.",
  ogt="Who do AI assistants name instead of your shop?", ogd="Paste your site address. We ask AI assistants what your buyers ask and show who they name instead of you.",
  h1="Is an AI assistant sending your customers to a competitor?",
  lede="CitedBy is an AI visibility audit for online shops, not a citation tool: we ask AI assistants the questions your buyers ask, in their language, and count who gets named. Then we fix what keeps your shop out of the answers and count again 30 days later.",
  f_label="Your website address", f_ph="example-shop.eu", go="Scan my site, free", micro="No email, no card. Result in about 2 minutes.",
  more="Change market, language or what you sell", mk="Market", lg="Language", sl="What you sell", sl_ph="e.g. coffee beans", auto="Read from my site",
  countries=(("BE", "Belgium"), ("FR", "France"), ("NL", "Netherlands"), ("DE", "Germany"), ("ES", "Spain"), ("IE", "Ireland"), ("GB", "United Kingdom")),
  langs=(("fr", "Français"), ("nl", "Nederlands"), ("de", "Deutsch"), ("en", "English"), ("es", "Español")),
  steps_label="How it works",
  steps=(("Paste your website address.", "One field. No signup, no email."),
         ("We ask the AI assistants what your buyers ask.", "Real buyer questions, in your language, put to {assistants}, twice each, today."),
         ("You get a dated report.", "Who the assistants name instead of you, whether what they say about you is true, and what to change first. Share it, print it, run it again.")),
  sheet_h="Audit · citedby.eu", sheet_tag="Our own site, day 0", sheet_day="DAY 0 · {date}", sheet_cap="category answers name CitedBy",
  d30_h="DAY 30", d30="Empty until the changes are live and recounted. Nothing shown before it exists.", cited_h="Pages cited instead (of {a} answers)",
  sheet_src="Source: our own day-0 audit of citedby.eu, {k} assistants, raw answers in the CSV.", art_cap="Built from our own day-0 audit of citedby.eu, {date}. Not a customer result.",
  eng_h="The {n} assistants we ask", eng_sub="Tested {date}. Each one through an API, with web search on.", eng_none="We are connecting assistants. Write to us before you buy.", eng_one="Tested {date}",
  engines="Assistants we measured on {date}: {names}. Each one through an API, with web search on.",
  proof_h_zero="We audited ourselves first. We are not named.", proof_h="We audited ourselves first.",
  how_run="<b>How it was run.</b> {k} assistants ({names}), official APIs, web search on. {q} questions, each asked {r} times: {kept} answers. {cq} buyer questions count as category ({a} answers); the questions that contain the brand name are not counted as visibility. API answers can differ from the signed-in apps.",
  csv="Read the {kept} answers", csv_href="/data/day0-citedby-eu.csv",
  st1="category answers that name CitedBy", st2="answers that link citedby.eu", st3="answers kept, {date}, raw text in the CSV",
  card_h="Pages the assistants cited for these questions instead", card_note="Number of the {a} category answers that linked the page.",
  own_note="<b>Own site, not a customer result.</b> No customer card exists yet, so none is shown.",
  offers_h="Four offers. Every price in euros, before you scan.", offers="Start with the free count. Pay for a recount, for the changes made, or for client reports.", prices="See the prices",
  faq_h="Questions", faq_all="All questions", behind_h_key="behind_h",
  end_h="See where you stand, free",
  svc="CitedBy: AI assistant visibility audit and fixes", svc_type="AI search visibility for online shops", free_offer="Free scan", fp_offer="Audit + Fix (paid once)",
  org_desc="CitedBy (citedby.eu) audits how AI assistants answer buyers' questions about online shops. It is a different service from citedby.co and from academic citation tools.",
 ),
 "fr": dict(
  path="/fr", locale="fr",
  title="CitedBy : qui les IA citent-elles à votre place ?",
  desc="Nous posons aux assistants IA les questions de vos acheteurs et comptons qui est cité. Scan gratuit, sans e-mail. Puis les changements faits pour vous, payés une fois 390 €, et un recomptage à 30 jours.",
  ogt="Qui les assistants IA citent-ils à la place de votre boutique ?", ogd="Collez l'adresse de votre site. Nous posons aux assistants IA les questions de vos acheteurs et montrons qui ils citent à votre place.",
  h1="Un assistant IA envoie-t-il vos clients chez un concurrent ?",
  lede="CitedBy est un audit de visibilité IA pour boutiques en ligne, pas un outil de citations : nous posons aux assistants IA les questions de vos acheteurs, dans leur langue, et nous comptons qui est cité. Puis nous corrigeons ce qui vous écarte des réponses et nous recomptons 30 jours plus tard.",
  f_label="L'adresse de votre site", f_ph="exemple-boutique.fr", go="Tester ma boutique, gratuitement", micro="Sans e-mail, sans carte. Résultat en environ 2 minutes.",
  more="Changer de marché, de langue ou de ce que vous vendez", mk="Marché", lg="Langue", sl="Ce que vous vendez", sl_ph="p. ex. café en grains", auto="Lu sur mon site",
  countries=(("FR", "France"), ("BE", "Belgique"), ("NL", "Pays-Bas"), ("DE", "Allemagne"), ("ES", "Espagne"), ("IE", "Irlande"), ("GB", "Royaume-Uni")),
  langs=(("fr", "Français"), ("nl", "Nederlands"), ("de", "Deutsch"), ("en", "English"), ("es", "Español")),
  steps_label="Comment ça marche",
  steps=(("Collez l'adresse de votre site.", "Un seul champ. Sans inscription, sans e-mail."),
         ("Nous posons aux assistants IA les questions de vos acheteurs.", "De vraies questions d'acheteurs, dans votre langue, posées à {assistants}, deux fois chacune, aujourd'hui."),
         ("Vous recevez un rapport daté.", "Qui les assistants citent à votre place, si ce qu'ils disent de vous est vrai, et quoi changer en premier. Partagez-le, imprimez-le, relancez-le.")),
  sheet_h="Audit · citedby.eu", sheet_tag="Notre propre site, jour 0", sheet_day="JOUR 0 · {date}", sheet_cap="réponses de catégorie citent CitedBy",
  d30_h="JOUR 30", d30="Vide tant que les changements ne sont pas en ligne et recomptés. Rien n'est affiché avant.", cited_h="Pages citées à la place (sur {a} réponses)",
  sheet_src="Source : notre propre audit du jour 0 de citedby.eu, {k} assistants, réponses brutes dans le CSV.", art_cap="Construit à partir de notre propre audit du jour 0 de citedby.eu, {date}. Pas un résultat client.",
  eng_h="Les {n} assistants que nous interrogeons", eng_sub="Testés le {date}. Chacun par une API, recherche web activée.", eng_none="Nous connectons des assistants. Écrivez-nous avant d'acheter.", eng_one="Testé le {date}",
  engines="Assistants mesurés le {date} : {names}. Chacun par une API, recherche web activée.",
  proof_h_zero="Nous nous sommes audités en premier. Nous ne sommes pas cités.", proof_h="Nous nous sommes audités en premier.",
  how_run="<b>Comment c'est mesuré.</b> {k} assistants ({names}), API officielles, recherche web activée. {q} questions, chacune posée {r} fois : {kept} réponses. {cq} questions d'acheteurs comptent comme catégorie ({a} réponses) ; les questions qui contiennent le nom de la marque ne comptent pas comme visibilité. Les réponses d'API peuvent différer des applications.",
  csv="Lire les {kept} réponses", csv_href="/data/day0-citedby-eu.csv",
  st1="réponses de catégorie qui citent CitedBy", st2="réponses qui renvoient vers citedby.eu", st3="réponses conservées, {date}, texte brut dans le CSV",
  card_h="Pages citées à la place par les assistants pour ces questions", card_note="Nombre des {a} réponses de catégorie qui renvoyaient vers la page.",
  own_note="<b>Notre propre site, pas un résultat client.</b> Aucun résultat client n'existe encore, donc aucun n'est affiché.",
  offers_h="Quatre offres. Chaque prix en euros, avant de tester.", offers="Commencez par le décompte gratuit. Payez pour un recomptage, pour les changements faits ou pour des rapports clients.", prices="Voir les tarifs",
  faq_h="Questions", faq_all="Toutes les questions",
  end_h="Voyez où vous en êtes, gratuitement",
  svc="CitedBy : audit et corrections de visibilité dans les assistants IA", svc_type="Visibilité IA pour boutiques en ligne", free_offer="Scan gratuit", fp_offer="Audit + Fix (payé une fois)",
  org_desc="CitedBy (citedby.eu) mesure comment les assistants IA répondent aux questions des acheteurs sur les boutiques en ligne. C'est un autre service que citedby.co et que les outils de citations académiques.",
 ),
}
for _l in T:
    T[_l].update(KEEP[_l])
    # "How fast?" quotes a 2-working-day mini-audit, which contradicts the one time sentence on these pages (about 2 minutes): left off until the GM rewrites it.
    T[_l]["faq"] = [(q, a) for q, a in T[_l]["faq"] if q not in ("How fast?", "En combien de temps ?")]
HOME_FAQ_N = 5


def eline_plain(t, day, names, lang):
    return t["engines"].format(date=fmt_date(day, lang), names=join_names(names, lang))


def assistants_phrase(lang, n):
    """Step 2's claim, built from the same live list as the engine row: it cannot name a number the row does not show."""
    w = NUM[lang].get(n, str(n))
    if lang == "fr":
        return "l'assistant listé sur cette page" if n == 1 else f"{w} assistants listés sur cette page" if n else "les assistants IA que nous connectons"
    return "the assistant listed on this page" if n == 1 else f"the {w} assistants listed on this page" if n else "the AI assistants we are connecting"


def steps_html(t, lang, engines):
    ph = assistants_phrase(lang, len(engines))
    return "".join(f"<li><span><b>{E(h)}</b>{E(b.replace('{assistants}', ph))}</span></li>" for h, b in t["steps"])


def faq_items(lang, engines):
    t = T[lang]
    faq = list(t["faq"])
    if len(engines) >= 2: faq.insert(1, t["faq_multi"])
    return faq


def details(items, first_open=False):
    return "".join(f'<details{" open" if first_open and i == 0 else ""}><summary>{E(q)}</summary><p>{E(a)}</p></details>' for i, (q, a) in enumerate(items))


def engines_html(lang, engines):
    t = T[lang]
    if not engines:
        return f'<section class="engsec"><div class="wrap"><p class="engnone" id="engines">{E(t["eng_none"])}</p></div></section>'
    day = max(e["tested"] for e in engines)
    n = NUM[lang].get(len(engines), str(len(engines)))
    lis = "".join(f'<li><span class="chip" aria-hidden="true">{E(e["name"][:1])}</span><span class="en">{E(e["name"])}<small>{E(t["eng_one"].format(date=fmt_date(e["tested"], lang)))}</small></span></li>' for e in engines)
    return (f'<section class="engsec" aria-labelledby="eng-h"><div class="wrap"><h2 id="eng-h">{E(t["eng_h"].format(n=n))}</h2>'
            f'<p class="sub"><time datetime="{day.isoformat(timespec="minutes")}">{E(t["eng_sub"].format(date=fmt_date(day, lang)))}</time></p>'
            f'<ul class="eng9" id="engines">{lis}</ul></div></section>')


def sheet_html(lang, d):
    """The hero artefact: our own day-0 audit, every number read from data/day0.json."""
    t = T[lang]
    top = max(n for _, n in d["cited"])
    bars = "".join(f'<li><span>{E(h)}</span><span class="bx"><i style="width:{n / top * 100:.0f}%"></i></span><span class="c">{n}</span></li>' for h, n in d["cited"])
    dt = shell.day0_date(lang)
    of = " of " if lang == "en" else " sur "
    return (f'<figure class="sheet"><div class="sh"><span>{E(t["sheet_h"])}</span><span>{E(t["sheet_tag"])}</span></div><div class="sb">'
            f'<p class="kick">{E(t["sheet_day"].format(date=dt.upper() if lang == "en" else dt))}</p>'
            f'<p class="big">{d["named"]}<small>{of}{d["answers"]}</small></p><p class="cap1">{E(t["sheet_cap"])}</p>'
            f'<p class="d30"><b>{E(t["d30_h"])}</b>{E(t["d30"])}</p><p class="h3">{E(t["cited_h"].format(a=d["answers"]))}</p><ul class="nbars">{bars}</ul>'
            f'<p class="src">{E(t["sheet_src"].format(k=len(d["assistants"])))}</p></div></figure>')


def art_caption(lang, d):
    t = T[lang]
    return f'<p class="shotcap"><span class="own">{E(shell.S[lang]["own"])}</span>{E(t["art_cap"].format(date=shell.day0_date(lang)))}</p>'


def proof_html(lang, d):
    t = T[lang]
    dt = shell.day0_date(lang)
    runs = d["kept"] // (d["questions"] * len(d["assistants"]))
    h = t["proof_h_zero"] if d["named"] == 0 else t["proof_h"]
    how = t["how_run"].format(k=len(d["assistants"]), names=join_names(d["assistants"], lang), q=d["questions"], r=runs, kept=d["kept"], cq=d["category_questions"], a=d["answers"])
    of = " of " if lang == "en" else " sur "
    rows = "".join(f'<tr><td>{E(h)}</td><td class="n">{n}</td></tr>' for h, n in d["cited"])
    return (f'<section class="tintband" id="proof" aria-labelledby="proof-h"><div class="wrap"><span class="eyebrow-bar"></span><h2 class="h2b" id="proof-h">{E(h)}</h2>'
            f'<p class="how">{how} <a class="csvl" href="{t["csv_href"]}" download>{E(t["csv"].format(kept=d["kept"]))}</a></p>'
            f'<div class="stats"><div><div class="stat-n bad">{d["named"]}<small>{of}{d["answers"]}</small></div><div class="stat-l">{E(t["st1"])}</div></div>'
            f'<div><div class="stat-n bad">{d["linked"]}</div><div class="stat-l">{E(t["st2"])}</div></div>'
            f'<div><div class="stat-n">{d["kept"]}</div><div class="stat-l">{E(t["st3"].format(date=dt))}</div></div></div>'
            f'<div class="card"><h3>{E(t["card_h"])}</h3><table class="top-t"><tbody>{rows}</tbody></table><p class="proofmeta">{E(t["card_note"].format(a=d["answers"]))}</p></div>'
            f'<p class="proofmeta">{t["own_note"]}</p></div></section>')


def render(lang, engines):
    t = T[lang]
    live = bool(engines)
    day = max((e["tested"] for e in engines), default=None)
    names = [e["name"] for e in engines]
    d = shell.day0()
    base = "/instant" if lang == "en" else "/fr/instant"
    opts = lambda rows: f'<option value="">{E(t["auto"])}</option>' + "".join(f'<option value="{v}">{E(n)}</option>' for v, n in rows)
    form = (f'<form class="scan" action="{base}" method="get" aria-label="{E(t["go"])}"><label for="site">{E(t["f_label"])}</label>'
            f'<div class="row"><input id="site" name="domain" type="text" inputmode="url" autocomplete="url" autocapitalize="off" spellcheck="false" placeholder="{E(t["f_ph"])}" required>'
            f'<button class="btn" type="submit">{E(t["go"])}</button></div><p class="micro">{E(t["micro"])}</p>'
            f'<details><summary>{E(t["more"])}</summary><div class="opts"><div><label for="mk">{E(t["mk"])}</label><select id="mk" name="country">{opts(t["countries"])}</select></div>'
            f'<div><label for="lg">{E(t["lg"])}</label><select id="lg" name="lang">{opts(t["langs"])}</select></div>'
            f'<div><label for="sl">{E(t["sl"])}</label><input id="sl" name="what" type="text" maxlength="60" placeholder="{E(t["sl_ph"])}" autocomplete="off"></div></div></details></form>')
    items = faq_items(lang, engines)
    faq_n = items[:HOME_FAQ_N + (1 if len(engines) >= 2 else 0)] if lang == "en" else items
    faq_more = f'<p><a class="link" href="/faq">{E(t["faq_all"])}</a></p>' if lang == "en" else ""
    ld = [{"@context": "https://schema.org", "@type": "Organization", "name": "CitedBy", "url": "https://citedby.eu", "logo": "https://citedby.eu/icon-192.png", "email": "hello@citedby.eu",
           "disambiguatingDescription": t["org_desc"]},
          {"@context": "https://schema.org", "@type": "Service", "name": t["svc"], "serviceType": t["svc_type"],
           "provider": {"@type": "Organization", "name": "CitedBy", "url": "https://citedby.eu", "disambiguatingDescription": "Not citedby.co or citedby.ai, and not an academic citation tool."}, "areaServed": "EU", "inLanguage": t["locale"],
           "offers": [{"@type": "Offer", "name": t["free_offer"], "price": "0", "priceCurrency": "EUR", "url": f"https://citedby.eu{t['path']}"}]
           + ([{"@type": "Offer", "name": t["fp_offer"], "price": "390", "priceCurrency": "EUR", "url": FIX_URL}] if live else [])}]
    if live:
        ld[1]["description"] = eline_plain(t, day, names, lang)
    alts = '<link rel="alternate" hreflang="en" href="https://citedby.eu/"><link rel="alternate" hreflang="fr" href="https://citedby.eu/fr"><link rel="alternate" hreflang="x-default" href="https://citedby.eu/">'
    behind = f'<section id="behind" class="sect"><div class="wrap"><h2>{E(t["behind_h"])}</h2><p>{E(t["behind"])} <a href="/legal">{E(t["legal"])}</a>.</p></div></section>'
    prices_lnk = "/pricing"
    main = f'''<section class="hero on-navy" id="scan"><div class="wrap"><div class="cols"><div class="lcol"><h1>{E(t["h1"])}</h1><p class="lede">{E(t["lede"])}</p>
{form}
<ol class="hsteps" aria-label="{E(t["steps_label"])}">{steps_html(t, lang, engines)}</ol></div><div class="rcol">{sheet_html(lang, d)}{art_caption(lang, d)}</div></div></div></section>
{engines_html(lang, engines)}
{proof_html(lang, d)}
<section class="band" id="prices"><div class="wrap"><div class="offers"><h2>{E(t["offers_h"])}</h2><div><p>{E(t["offers"])}</p><a class="btn sec" href="{prices_lnk}">{E(t["prices"])}</a></div></div></div></section>
<section class="sect" id="faq"><div class="wrap"><h2 class="h2b">{E(t["faq_h"])}</h2><div class="faq">{details(faq_n, first_open=True)}</div>{faq_more}</div></section>
{behind}
<section class="sect"><div class="wrap"><h2>{E(t["end_h"])}</h2><p><a class="btn sec" href="{base}">{E(t["go"])}</a></p></div></section>'''
    return shell.document(lang, t["title"], t["desc"], t["path"], main, ld=ld, og_title=t["ogt"], og_desc=t["ogd"], current=None, alts=alts)
