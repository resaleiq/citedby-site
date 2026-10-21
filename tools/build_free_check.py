#!/usr/bin/env python3
"""Build /free-ai-visibility-check in en, fr, nl, de, es (RES-2498): one page for the free check, the same /api/teaser form as the home page.
The example comes from data/sample_facts.json (the /sample crawl), never typed. Adds the five URLs to sitemap.xml (idempotent).
Run: python3 tools/build_free_check.py [--check]. Standard library only."""
import datetime, html, json, os, re, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB = os.path.join(HERE, "public")
SITE = "https://citedby.eu"
E = html.escape
LANGS = ("en", "fr", "nl", "de", "es")
LASTMOD = "2026-10-21"
MONTHS = {"en": "October", "fr": "octobre", "nl": "oktober", "de": "Oktober", "es": "octubre"}


def pfx(l): return "" if l == "en" else "/" + l


T = {
"en": dict(
    title="Free AI visibility check: ChatGPT, Claude, Gemini, Perplexity | CitedBy",
    desc="Free AI visibility check, no account: we crawl up to 10 pages and show your score, your AI crawler access and the 3 fixes to make first.",
    h1="Free AI visibility check for your website",
    lede="See what stops AI assistants such as ChatGPT, Claude, Gemini and Perplexity from reading your site, and the three fixes to make first.",
    free="Free, no account. We crawl up to 10 pages. No card, no email.",
    label="Your website address", ph="yourwebsite.com", btn="Check my site free", hp="Leave this empty",
    nav=("Pricing", "Guides"), signin="Sign in", skip="Skip to content",
    h_shows="What the free check shows",
    shows=[("Your score", "One health score out of 100 for the pages we crawl, with a letter grade."),
           ("Your AI crawler access", "Whether robots.txt and your server let the crawlers of ChatGPT, Claude and Perplexity in, with the status each one gets."),
           ("The 3 issues to fix first", "The three problems that matter most on those pages, ranked, so you know where to start.")],
    h_ex="One real example", ex_intro="This is a real crawl of {host} on {date}, {pages} pages, score {score} ({grade}). {host} is not a CitedBy customer. One issue from that report, with the fix:",
    ex_issue="Issue", ex_page="Example page", ex_fix="The fix, ready to paste", ex_more="Open the full report",
    h_paid="Want every page, not 10?", paid="The free check reads up to 10 pages. A full audit reads up to your plan's page limit (up to 500 pages for €9, once) and gives the exact fix for every issue, with a 14-day money-back guarantee.",
    paid_cta="See plans and prices", more_tool="Only want to know if GPTBot is blocked? Use the free AI crawler checker.",
    h_faq="Questions about the free check",
    faq=[("Is the AI visibility check really free?", "Yes. You need no account, no card and no email. We crawl up to 10 pages of your site and show the result on a page you can open straight away. Each network can run 3 free checks a day."),
         ("What does the free check look at?", "It reads up to 10 public pages and checks the HTML each one serves, robots.txt, your sitemap and whether the crawlers of ChatGPT, Claude and Perplexity can get in. It shows your score, your AI crawler access and the 3 issues to fix first."),
         ("Does it ask ChatGPT, Claude, Gemini or Perplexity about my business?", "No. It does not query any assistant. It checks what stops those assistants from reading your pages. For Google's crawlers, which Gemini relies on, use the AI crawler checker, which tests Google-Extended and Googlebot too."),
         ("Will fixing the issues make ChatGPT mention my site?", "We cannot promise that, and nobody can: assistants decide what to name. The check finds what blocks or weakens your pages for AI search and gives you the fix. That is the part you control."),
         ("What is the difference between the free check and the paid audit?", "The free check reads 10 pages and shows the score, crawler access and 3 issues. The audit reads up to your plan's page limit, groups repeated problems into single fixes and writes the exact code for each one. From €9, once, with a 14-day money-back guarantee.")],
    h_who="Who runs the crawl", who="Our crawler is CitedBot. We read public pages only and never log in. It is documented at citedby.eu/bot.",
    footer=("About", "Method", "Terms", "Privacy", "Refunds"), wa_desc="Free AI visibility check for a website: score, AI crawler access and the 3 issues to fix first.",
),
"fr": dict(
    title="Test gratuit de visibilité IA : ChatGPT, Claude, Gemini, Perplexity | CitedBy",
    desc="Test gratuit de visibilité IA, sans compte : nous lisons jusqu'à 10 pages et montrons votre score, l'accès des robots IA et les 3 corrections à faire d'abord.",
    h1="Test gratuit de visibilité IA pour votre site",
    lede="Voyez ce qui empêche des assistants IA comme ChatGPT, Claude, Gemini et Perplexity de lire votre site, et les trois corrections à faire en premier.",
    free="Gratuit, sans compte. Nous lisons jusqu'à 10 pages. Ni carte, ni e-mail.",
    label="L'adresse de votre site", ph="votresite.fr", btn="Tester mon site gratuitement", hp="Laissez ce champ vide",
    nav=("Tarifs", "Guides"), signin="Connexion", skip="Aller au contenu",
    h_shows="Ce que montre le test gratuit",
    shows=[("Votre score", "Un score de santé sur 100 pour les pages lues, avec une note en lettre."),
           ("L'accès des robots IA", "Si robots.txt et votre serveur laissent entrer les robots de ChatGPT, Claude et Perplexity, avec le statut reçu par chacun."),
           ("Les 3 problèmes à corriger d'abord", "Les trois problèmes les plus importants sur ces pages, classés, pour savoir par où commencer.")],
    h_ex="Un exemple réel", ex_intro="Voici un vrai passage sur {host} le {date}, {pages} pages, score {score} ({grade}). {host} n'est pas client de CitedBy. Un problème de ce rapport, avec sa correction :",
    ex_issue="Problème", ex_page="Page d'exemple", ex_fix="La correction, à copier", ex_more="Ouvrir le rapport complet",
    h_paid="Toutes les pages, pas seulement 10 ?", paid="Le test gratuit lit jusqu'à 10 pages. Un audit complet lit jusqu'à la limite de votre offre (jusqu'à 500 pages pour 9 €, une fois) et donne la correction exacte de chaque problème, avec 14 jours de remboursement.",
    paid_cta="Voir les offres et les prix", more_tool="Vous voulez seulement savoir si GPTBot est bloqué ? Utilisez le vérificateur gratuit des robots IA.",
    h_faq="Questions sur le test gratuit",
    faq=[("Le test de visibilité IA est-il vraiment gratuit ?", "Oui. Ni compte, ni carte, ni e-mail. Nous lisons jusqu'à 10 pages de votre site et le résultat s'affiche tout de suite. Chaque réseau peut lancer 3 tests gratuits par jour."),
         ("Que regarde le test gratuit ?", "Il lit jusqu'à 10 pages publiques et vérifie le HTML servi par chacune, robots.txt, votre sitemap et si les robots de ChatGPT, Claude et Perplexity peuvent entrer. Il montre votre score, l'accès des robots IA et les 3 problèmes à corriger d'abord."),
         ("Interroge-t-il ChatGPT, Claude, Gemini ou Perplexity sur mon entreprise ?", "Non. Il n'interroge aucun assistant. Il vérifie ce qui empêche ces assistants de lire vos pages. Pour les robots de Google, dont Gemini dépend, utilisez le vérificateur de robots IA, qui teste aussi Google-Extended et Googlebot."),
         ("Corriger les problèmes fera-t-il citer mon site par ChatGPT ?", "Nous ne pouvons pas le promettre, personne ne le peut : ce sont les assistants qui décident. Le test trouve ce qui bloque ou affaiblit vos pages pour la recherche IA et donne la correction. C'est la part que vous maîtrisez."),
         ("Quelle différence entre le test gratuit et l'audit payant ?", "Le test gratuit lit 10 pages et montre le score, l'accès des robots et 3 problèmes. L'audit lit jusqu'à la limite de votre offre, regroupe les problèmes répétés en une seule correction et écrit le code exact de chacune. Dès 9 €, une fois, avec 14 jours de remboursement.")],
    h_who="Qui lit votre site", who="Notre robot s'appelle CitedBot. Nous lisons uniquement des pages publiques, sans jamais nous connecter. Il est documenté sur citedby.eu/bot.",
    footer=("À propos", "Méthode", "CGV", "Confidentialité", "Remboursements"), wa_desc="Test gratuit de visibilité IA d'un site : score, accès des robots IA et les 3 problèmes à corriger d'abord.",
),
"nl": dict(
    title="Gratis AI-zichtbaarheidscheck: ChatGPT, Claude, Gemini, Perplexity | CitedBy",
    desc="Gratis AI-zichtbaarheidscheck zonder account: we lezen tot 10 pagina's en tonen je score, de toegang van AI-crawlers en de 3 fixes om eerst te doen.",
    h1="Gratis AI-zichtbaarheidscheck voor je website",
    lede="Zie wat AI-assistenten zoals ChatGPT, Claude, Gemini en Perplexity beletten je site te lezen, en de drie fixes om als eerste te doen.",
    free="Gratis, zonder account. We lezen tot 10 pagina's. Geen kaart, geen e-mail.",
    label="Het adres van je website", ph="jouwwebsite.nl", btn="Check mijn site gratis", hp="Laat dit leeg",
    nav=("Prijzen", "Gidsen"), signin="Inloggen", skip="Naar de inhoud",
    h_shows="Wat de gratis check laat zien",
    shows=[("Je score", "Eén gezondheidsscore op 100 voor de gelezen pagina's, met een lettercijfer."),
           ("De toegang van AI-crawlers", "Of robots.txt en je server de crawlers van ChatGPT, Claude en Perplexity toelaten, met de status die elk krijgt."),
           ("De 3 problemen om eerst op te lossen", "De drie belangrijkste problemen op die pagina's, op volgorde, zodat je weet waar je begint.")],
    h_ex="Een echt voorbeeld", ex_intro="Dit is een echte crawl van {host} op {date}, {pages} pagina's, score {score} ({grade}). {host} is geen klant van CitedBy. Eén probleem uit dat rapport, met de fix:",
    ex_issue="Probleem", ex_page="Voorbeeldpagina", ex_fix="De fix, klaar om te plakken", ex_more="Open het volledige rapport",
    h_paid="Alle pagina's, niet maar 10?", paid="De gratis check leest tot 10 pagina's. Een volledige audit leest tot de paginalimiet van je abonnement (tot 500 pagina's voor €9, eenmalig) en geeft de exacte fix voor elk probleem, met 14 dagen geld-terug.",
    paid_cta="Bekijk abonnementen en prijzen", more_tool="Wil je alleen weten of GPTBot geblokkeerd is? Gebruik de gratis AI-crawlercheck.",
    h_faq="Vragen over de gratis check",
    faq=[("Is de AI-zichtbaarheidscheck echt gratis?", "Ja. Geen account, geen kaart, geen e-mail. We lezen tot 10 pagina's van je site en het resultaat staat meteen op een pagina die je kunt openen. Elk netwerk kan 3 gratis checks per dag doen."),
         ("Waar kijkt de gratis check naar?", "Hij leest tot 10 openbare pagina's en controleert de HTML die elke pagina serveert, robots.txt, je sitemap en of de crawlers van ChatGPT, Claude en Perplexity binnenkomen. Hij toont je score, de toegang van AI-crawlers en de 3 problemen om eerst op te lossen."),
         ("Vraagt hij ChatGPT, Claude, Gemini of Perplexity naar mijn bedrijf?", "Nee. Hij bevraagt geen enkele assistent. Hij controleert wat die assistenten beletten je pagina's te lezen. Voor de crawlers van Google, waar Gemini op leunt, gebruik je de AI-crawlercheck, die ook Google-Extended en Googlebot test."),
         ("Zorgt het oplossen ervoor dat ChatGPT mijn site noemt?", "Dat kunnen we niet beloven en niemand kan dat: de assistenten beslissen wat ze noemen. De check vindt wat je pagina's voor AI-zoeken blokkeert of verzwakt en geeft de fix. Dat deel heb je zelf in de hand."),
         ("Wat is het verschil tussen de gratis check en de betaalde audit?", "De gratis check leest 10 pagina's en toont de score, de crawlertoegang en 3 problemen. De audit leest tot de paginalimiet van je abonnement, bundelt herhaalde problemen tot één fix en schrijft de exacte code voor elk. Vanaf €9, eenmalig, met 14 dagen geld-terug.")],
    h_who="Wie je site leest", who="Onze crawler heet CitedBot. We lezen alleen openbare pagina's en loggen nooit in. Hij is beschreven op citedby.eu/bot.",
    footer=("Over ons", "Methode", "Voorwaarden", "Privacy", "Terugbetalingen"), wa_desc="Gratis AI-zichtbaarheidscheck voor een website: score, toegang van AI-crawlers en de 3 problemen om eerst op te lossen.",
),
"de": dict(
    title="Kostenloser KI-Sichtbarkeits-Check: ChatGPT, Claude, Gemini, Perplexity | CitedBy",
    desc="Kostenloser KI-Sichtbarkeits-Check ohne Konto: Wir lesen bis zu 10 Seiten und zeigen Ihren Score, den Zugang der KI-Crawler und die 3 wichtigsten Korrekturen.",
    h1="Kostenloser KI-Sichtbarkeits-Check für Ihre Website",
    lede="Sehen Sie, was KI-Assistenten wie ChatGPT, Claude, Gemini und Perplexity daran hindert, Ihre Website zu lesen, und welche drei Korrekturen zuerst anstehen.",
    free="Kostenlos, ohne Konto. Wir lesen bis zu 10 Seiten. Keine Karte, keine E-Mail.",
    label="Adresse Ihrer Website", ph="ihrewebsite.de", btn="Meine Website kostenlos prüfen", hp="Bitte leer lassen",
    nav=("Preise", "Ratgeber"), signin="Anmelden", skip="Zum Inhalt springen",
    h_shows="Was der kostenlose Check zeigt",
    shows=[("Ihr Score", "Ein Gesundheits-Score von 100 für die gelesenen Seiten, mit Buchstabennote."),
           ("Der Zugang der KI-Crawler", "Ob robots.txt und Ihr Server die Crawler von ChatGPT, Claude und Perplexity hereinlassen, mit dem Status, den jeder erhält."),
           ("Die 3 Probleme zuerst", "Die drei wichtigsten Probleme auf diesen Seiten, nach Rang sortiert, damit Sie wissen, wo Sie anfangen.")],
    h_ex="Ein echtes Beispiel", ex_intro="Das ist ein echter Crawl von {host} am {date}, {pages} Seiten, Score {score} ({grade}). {host} ist kein CitedBy-Kunde. Ein Problem aus diesem Bericht, mit der Korrektur:",
    ex_issue="Problem", ex_page="Beispielseite", ex_fix="Die Korrektur zum Einfügen", ex_more="Den ganzen Bericht öffnen",
    h_paid="Alle Seiten statt nur 10?", paid="Der kostenlose Check liest bis zu 10 Seiten. Ein vollständiges Audit liest bis zum Seitenlimit Ihres Tarifs (bis zu 500 Seiten für 9 €, einmalig) und liefert für jedes Problem die genaue Korrektur, mit 14 Tagen Geld-zurück-Garantie.",
    paid_cta="Tarife und Preise ansehen", more_tool="Sie wollen nur wissen, ob GPTBot blockiert ist? Nutzen Sie den kostenlosen KI-Crawler-Check.",
    h_faq="Fragen zum kostenlosen Check",
    faq=[("Ist der KI-Sichtbarkeits-Check wirklich kostenlos?", "Ja. Kein Konto, keine Karte, keine E-Mail. Wir lesen bis zu 10 Seiten Ihrer Website und das Ergebnis steht sofort auf einer Seite, die Sie öffnen können. Jedes Netzwerk kann 3 kostenlose Checks pro Tag starten."),
         ("Was prüft der kostenlose Check?", "Er liest bis zu 10 öffentliche Seiten und prüft das HTML jeder Seite, die robots.txt, Ihre Sitemap und ob die Crawler von ChatGPT, Claude und Perplexity hereinkommen. Er zeigt Ihren Score, den Zugang der KI-Crawler und die 3 Probleme, die zuerst anstehen."),
         ("Fragt er ChatGPT, Claude, Gemini oder Perplexity nach meinem Unternehmen?", "Nein. Er befragt keinen Assistenten. Er prüft, was diese Assistenten daran hindert, Ihre Seiten zu lesen. Für die Crawler von Google, auf die Gemini baut, nutzen Sie den KI-Crawler-Check, der auch Google-Extended und Googlebot testet."),
         ("Nennt ChatGPT meine Website, wenn ich die Probleme behebe?", "Das können wir nicht versprechen, und niemand kann es: Die Assistenten entscheiden, was sie nennen. Der Check findet, was Ihre Seiten für die KI-Suche blockiert oder schwächt, und liefert die Korrektur. Das ist der Teil, den Sie steuern."),
         ("Was unterscheidet den kostenlosen Check vom bezahlten Audit?", "Der kostenlose Check liest 10 Seiten und zeigt Score, Crawler-Zugang und 3 Probleme. Das Audit liest bis zum Seitenlimit Ihres Tarifs, fasst wiederholte Probleme zu einer Korrektur zusammen und schreibt für jede den genauen Code. Ab 9 €, einmalig, mit 14 Tagen Geld-zurück-Garantie.")],
    h_who="Wer Ihre Website liest", who="Unser Crawler heißt CitedBot. Wir lesen nur öffentliche Seiten und melden uns nie an. Er ist unter citedby.eu/bot beschrieben.",
    footer=("Über uns", "Methode", "AGB", "Datenschutz", "Rückerstattungen"), wa_desc="Kostenloser KI-Sichtbarkeits-Check für eine Website: Score, Zugang der KI-Crawler und die 3 wichtigsten Probleme.",
),
"es": dict(
    title="Revisión gratis de visibilidad en IA: ChatGPT, Claude, Gemini, Perplexity | CitedBy",
    desc="Revisión gratis de visibilidad en IA, sin cuenta: leemos hasta 10 páginas y te mostramos tu puntuación, el acceso de los robots de IA y las 3 correcciones primero.",
    h1="Revisión gratis de visibilidad en IA para tu web",
    lede="Mira qué impide que asistentes de IA como ChatGPT, Claude, Gemini y Perplexity lean tu web, y las tres correcciones que debes hacer primero.",
    free="Gratis, sin cuenta. Leemos hasta 10 páginas. Sin tarjeta, sin correo.",
    label="La dirección de tu web", ph="tuweb.es", btn="Revisar mi web gratis", hp="Deja esto vacío",
    nav=("Precios", "Guías"), signin="Entrar", skip="Saltar al contenido",
    h_shows="Qué muestra la revisión gratis",
    shows=[("Tu puntuación", "Una puntuación de salud sobre 100 para las páginas leídas, con una nota en letra."),
           ("El acceso de los robots de IA", "Si robots.txt y tu servidor dejan entrar a los robots de ChatGPT, Claude y Perplexity, con el estado que recibe cada uno."),
           ("Los 3 problemas que corregir primero", "Los tres problemas más importantes en esas páginas, ordenados, para saber por dónde empezar.")],
    h_ex="Un ejemplo real", ex_intro="Este es un rastreo real de {host} el {date}, {pages} páginas, puntuación {score} ({grade}). {host} no es cliente de CitedBy. Un problema de ese informe, con su corrección:",
    ex_issue="Problema", ex_page="Página de ejemplo", ex_fix="La corrección, lista para pegar", ex_more="Abrir el informe completo",
    h_paid="¿Todas las páginas, no solo 10?", paid="La revisión gratis lee hasta 10 páginas. Una auditoría completa lee hasta el límite de tu plan (hasta 500 páginas por 9 €, una vez) y da la corrección exacta de cada problema, con 14 días de devolución.",
    paid_cta="Ver planes y precios", more_tool="¿Solo quieres saber si GPTBot está bloqueado? Usa el verificador gratis de robots de IA.",
    h_faq="Preguntas sobre la revisión gratis",
    faq=[("¿La revisión de visibilidad en IA es gratis de verdad?", "Sí. Sin cuenta, sin tarjeta, sin correo. Leemos hasta 10 páginas de tu web y el resultado aparece enseguida en una página que puedes abrir. Cada red puede hacer 3 revisiones gratis al día."),
         ("¿Qué mira la revisión gratis?", "Lee hasta 10 páginas públicas y comprueba el HTML que sirve cada una, robots.txt, tu sitemap y si los robots de ChatGPT, Claude y Perplexity pueden entrar. Muestra tu puntuación, el acceso de los robots de IA y los 3 problemas que corregir primero."),
         ("¿Pregunta a ChatGPT, Claude, Gemini o Perplexity por mi negocio?", "No. No consulta a ningún asistente. Comprueba qué impide que esos asistentes lean tus páginas. Para los robots de Google, de los que depende Gemini, usa el verificador de robots de IA, que también prueba Google-Extended y Googlebot."),
         ("¿Si corrijo los problemas, ChatGPT mencionará mi web?", "No podemos prometerlo y nadie puede: los asistentes deciden qué nombran. La revisión encuentra lo que bloquea o debilita tus páginas para la búsqueda con IA y te da la corrección. Esa parte sí depende de ti."),
         ("¿Qué diferencia hay entre la revisión gratis y la auditoría de pago?", "La revisión gratis lee 10 páginas y muestra la puntuación, el acceso de los robots y 3 problemas. La auditoría lee hasta el límite de tu plan, agrupa los problemas repetidos en una sola corrección y escribe el código exacto de cada una. Desde 9 €, una vez, con 14 días de devolución.")],
    h_who="Quién lee tu web", who="Nuestro robot se llama CitedBot. Solo leemos páginas públicas y nunca iniciamos sesión. Está documentado en citedby.eu/bot.",
    footer=("Acerca de", "Método", "Condiciones", "Privacidad", "Reembolsos"), wa_desc="Revisión gratis de visibilidad en IA de una web: puntuación, acceso de los robots de IA y los 3 problemas que corregir primero.",
),
}


def fr_typo(s):
    for a in "?!;:":
        s = s.replace(" " + a, " " + a)
    return s


def facts():
    d = json.load(open(os.path.join(HERE, "data", "sample_facts.json"), encoding="utf-8"))
    return d, datetime.datetime.fromtimestamp(d["ts"], __import__("zoneinfo").ZoneInfo("Europe/Madrid"))  # same day as /sample and the home band


PG = {"en": "pages", "fr": "pages", "nl": "pagina's", "de": "Seiten", "es": "páginas"}


def render(l):
    t = T[l]
    d, when = facts()
    ex = d["example"]
    date = {"en": "%d %s %d", "fr": "%d %s %d", "nl": "%d %s %d", "de": "%d. %s %d", "es": "%d de %s de %d"}[l] % (when.day, MONTHS[l], when.year)
    title_ex = ex.get("title_l", {}).get(l) or ex["title"]
    path = pfx(l) + "/free-ai-visibility-check"
    url = SITE + path
    alts = "".join('<link rel="alternate" hreflang="%s" href="%s%s/free-ai-visibility-check">' % (x, SITE, pfx(x)) for x in LANGS)
    alts += '<link rel="alternate" hreflang="x-default" href="%s/free-ai-visibility-check">' % SITE
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebApplication", "name": t["h1"], "url": url, "description": t["wa_desc"], "applicationCategory": "BusinessApplication", "operatingSystem": "Web", "inLanguage": l,
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR", "url": url}, "publisher": {"@type": "Organization", "name": "CitedBy", "url": SITE}},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}]}
    shows = "".join("<li><b>%s.</b> %s</li>" % (E(h), E(p)) for h, p in t["shows"])
    faq = "".join("<h3>%s</h3><p>%s</p>" % (E(q), E(a)) for q, a in t["faq"])
    ex_intro = E(t["ex_intro"].format(host=d["host"], date=date, pages=d["pages"], score=d["score"], grade=d["grade"]))
    p = pfx(l)
    f = t["footer"]
    doc = f'''<!doctype html><html lang="{l}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#0F1B2D"><title>{E(t["title"])}</title><meta name="description" content="{E(t["desc"])}"><link rel="canonical" href="{url}">{alts}<meta property="og:title" content="{E(t["title"])}"><meta property="og:description" content="{E(t["desc"])}"><meta property="og:url" content="{url}"><meta property="og:type" content="website"><meta property="og:image" content="{SITE}/og-v2.png"><meta name="twitter:image" content="{SITE}/og-v2.png"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="preload" href="/fonts/newsreader-latin-600-normal.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/fonts/ibm-plex-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="/saas.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")}</script></head>
<body class="cb land"><a class="sr" href="#main">{E(t["skip"])}</a>
<header class="topbar"><div class="in"><a class="mark" href="{p or "/"}"><i></i>CitedBy</a><nav aria-label="Main"><a href="{p}/plans">{E(t["nav"][0])}</a><a href="{p}/blog">{E(t["nav"][1])}</a></nav><a href="/signin?next=%2Fapp.html" style="color:#C9D2DF;margin-right:12px">{E(t["signin"])}</a></div></header>
<main id="main">
<section class="band dark"><style>.fch{{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:36px;align-items:center}}.fcc{{background:#fff;color:#0F1B2D;border-radius:12px;padding:20px 22px;box-shadow:0 12px 32px -12px rgba(0,0,0,.5)}}.fcc h2{{font:600 .8rem var(--sans);text-transform:uppercase;letter-spacing:.05em;color:#556173;margin:0 0 10px}}.fcc .sc{{display:flex;align-items:baseline;gap:10px;margin:0 0 4px}}.fcc .sc b{{font:600 3rem/1 var(--serif)}}.fcc .sc span{{font-weight:600;color:#0F8F84}}.fcc p{{margin:0 0 8px;font-size:.9rem}}.fcc code{{overflow-wrap:anywhere;font-size:.82rem}}@media(max-width:800px){{.fch{{grid-template-columns:minmax(0,1fr);gap:20px}}}}</style><div class="w fch" style="max-width:1040px"><div>
<h1>{E(t["h1"])}</h1>
<p class="lede">{E(t["lede"])}</p>
<p class="tzn" id="tzn" style="font-weight:600;margin-bottom:10px">{E(t["free"])}</p>
<form class="urlf" id="tzf" action="/api/teaser" method="post" novalidate aria-describedby="tzn"><label class="sr" for="u">{E(t["label"])}</label><input class="fld" id="u" name="url" placeholder="{E(t["ph"])}" autocomplete="url" inputmode="url" required><span class="hp" aria-hidden="true"><label>{E(t["hp"])} <input name="fax" tabindex="-1" autocomplete="off"></label></span><button class="btn go" data-cta="primary" data-cta-id="free-check-page">{E(t["btn"])}</button></form>
<p class="tzm" id="tzm" role="alert" aria-live="polite"></p>
<ul class="trust"><li>{E(t["who"])}</li></ul>
</div><aside class="fcc" aria-label="{E(t["h_ex"])}"><h2>{E(t["h_ex"])}</h2><p class="sc"><b>{d["score"]}</b><span>/100 · {E(d["grade"])}</span></p><p>{E(d["host"])} · {d["pages"]} {PG[l]} · {date}</p><p><b>{E(t["ex_issue"])}:</b> {E(title_ex)}<br><b>{E(t["ex_page"])}:</b> <code>{E(ex["path"])}</code></p><p><a href="{p}/sample">{E(t["ex_more"])} &rarr;</a></p></aside></div></section>
<section class="band"><div class="w" style="max-width:760px">
<h2>{E(t["h_shows"])}</h2><ol>{shows}</ol>
<h2>{E(t["h_ex"])}</h2><p>{ex_intro}</p>
<p><b>{E(t["ex_issue"])}:</b> {E(title_ex)}<br><b>{E(t["ex_page"])}:</b> <code>{E(ex["path"])}</code></p>
<p><b>{E(t["ex_fix"])}:</b></p><pre style="white-space:pre-wrap;overflow-wrap:anywhere"><code>{E(ex["code"])}</code></pre>
<p><a href="{p}/sample">{E(t["ex_more"])} &rarr;</a></p>
<h2>{E(t["h_paid"])}</h2><p>{E(t["paid"])} <a href="{p}/plans">{E(t["paid_cta"])}</a>.</p>
<p><a href="{p}/tools/ai-crawler-check">{E(t["more_tool"])}</a></p>
<h2>{E(t["h_faq"])}</h2>{faq}
</div></section>
</main><footer><div class="w">CitedBy · hello@citedby.eu · <a href="{p}/about">{f[0]}</a> · <a href="/methodology">{f[1]}</a> · <a href="{p}/terms">{f[2]}</a> · <a href="{p}/privacy">{f[3]}</a> · <a href="{p}/refund">{f[4]}</a></div></footer>
<script src="/landing.js"></script></html>
'''
    return fr_typo(doc) if l == "fr" else doc


def sitemap():
    sm = os.path.join(PUB, "sitemap.xml")
    s = open(sm, encoding="utf-8").read()
    s = re.sub(r"<url><loc>%s(?:/[a-z]{2})?/free-ai-visibility-check</loc>.*?</url>" % re.escape(SITE), "", s)
    new = "".join("<url><loc>%s%s/free-ai-visibility-check</loc><lastmod>%s</lastmod></url>" % (SITE, pfx(l), LASTMOD) for l in LANGS)
    return sm, s.replace("</urlset>", new + "</urlset>")


def main():
    check = "--check" in sys.argv
    out = {os.path.join(PUB, pfx(l).lstrip("/"), "free-ai-visibility-check.html"): render(l) for l in LANGS}
    sm, sms = sitemap()
    out[sm] = sms
    for p, doc in out.items():
        if check:
            if not os.path.exists(p) or open(p, encoding="utf-8").read() != doc: sys.exit("stale: " + p)
        else:
            open(p, "w", encoding="utf-8").write(doc)
    print("ok" if check else "wrote %d files" % len(out))


if __name__ == "__main__":
    main()
