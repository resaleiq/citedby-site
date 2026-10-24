#!/usr/bin/env python3
"""RES-4195: write the AI-access API docs page in 5 languages (public/ai-access-api.html, public/<fr|nl|de|es>/ai-access-api.html) and the OpenAPI spec (public/openapi.json)
from the texts below, the sample result in data/ai-access-sample.json, and the sitemap and llms.txt lines. Run after editing them; idempotent. Standard library only.
The sample is a real result of a public site that is not ours, stored with its date (the API would answer a little differently on another day)."""
import html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import docshell

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PUB = os.path.join(ROOT, "public")
SITE = "https://citedby.eu"
E = html.escape
LANGS = ["en", "fr", "nl", "de", "es"]
SAMPLE = json.load(open(os.path.join(ROOT, "data", "ai-access-sample.json"), encoding="utf-8"))
MONTHS = {"en": "January February March April May June July August September October November December".split(),
          "fr": "janvier février mars avril mai juin juillet août septembre octobre novembre décembre".split(),
          "nl": "januari februari maart april mei juni juli augustus september oktober november december".split(),
          "de": "Januar Februar März April Mai Juni Juli August September Oktober November Dezember".split(),
          "es": "enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre".split()}
CODES = ["missing_url", "bad_url", "site_unreachable", "rate_limited", "busy", "unavailable"]
FIELDS = ["site", "checked_at", "robots_txt.state", "robots_txt.status", "robots_txt.blocks_all_crawlers", "summary", "crawlers[].id", "crawlers[].role", "crawlers[].robots_txt", "crawlers[].robots_txt_rule",
          "crawlers[].server", "crawlers[].access", "report_url", "audit_url", "attribution"]
NAMES = {"en": "English", "fr": "Français", "nl": "Nederlands", "de": "Deutsch", "es": "Español"}
ACCESS = ["allowed", "blocked_by_robots_txt", "blocked_by_server", "blocked_by_robots_txt_and_server", "server_error"]

T = {
"en": dict(
 title="Free AI crawler access API (JSON, no key) | CitedBy",
 desc="A free JSON API that says which AI crawlers can read a site: robots.txt and server answer for each one. No key, CORS open, OpenAPI spec.",
 h1="AI crawler access API",
 ans="One request tells you which AI crawlers can read a site: GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot. For each one you get what robots.txt says and what the server answers it. It is the result the free AI crawler check shows, as JSON. No key, no account, CORS open.",
 req_h="Request", req_p="One GET request with one parameter:", req_url="url", req_url_p="A domain or a full address, for example example.com or https://example.com/shop. Only the site is checked: the path, the port and www. are dropped.",
 ex_h="Example", ex_p="The check of {site} on {date}: a public site, not a CitedBy customer, in the result as the API returned it. Run it on another day and the answer can differ.",
 fields_h="What the response holds", fields_p="Every field below is in every successful response.",
 F={"site": "The domain that was checked.",
    "checked_at": "When CitedBy ran the check, in UTC. A site checked in the last 6 hours returns the stored result, so this can be earlier than your request.",
    "robots_txt.state": "found, not_found, unreachable or server_error. A server error on robots.txt means a crawler has to assume it may not crawl (RFC 9309), so every crawler then shows as blocked.",
    "robots_txt.status": "The HTTP status robots.txt answered with.",
    "robots_txt.blocks_all_crawlers": "true when the rules for all crawlers (*) close the whole site.",
    "summary": "How many of the 8 crawlers can read the site (allowed), and the names of those that cannot (blocked).",
    "crawlers[].id": "The crawler's name.",
    "crawlers[].role": "training (collects text to train models), search (can cite your pages in answers) or user_fetch (opens a page when a person asks about it).",
    "crawlers[].robots_txt": "allowed, disallowed or not_read (robots.txt could not be read).",
    "crawlers[].robots_txt_rule": "The robots.txt rule that closes the site to this crawler, or null.",
    "crawlers[].server": "ok, blocked (the server answers this crawler's user-agent with a refusal or a challenge page), down (an error) or not_tested. Google-Extended is a robots.txt token only, so it is never tested on the server.",
    "crawlers[].access": "The verdict for this crawler, one of the values below.",
    "report_url": "The full result page of the free check for this site.",
    "audit_url": "Where to audit the whole site.",
    "attribution": "The text and link to show when you display the result (see the terms)."},
 acc_h="The access values", acc_p="allowed means robots.txt does not close the site to the crawler and the server answered it. The others name what stands in the way:",
 A={"allowed": "the crawler can read the site.", "blocked_by_robots_txt": "robots.txt closes the site to this crawler.", "blocked_by_server": "the server turns this crawler's user-agent away or shows it a challenge page.",
    "blocked_by_robots_txt_and_server": "both.", "server_error": "the server answered this crawler with an error."},
 acc_note="Blocking a training crawler can be a choice. The API reports it as blocked and does not call it a problem.",
 err_h="Errors", err_p="A failure is an error, never a guess. The body is JSON: {\"error\": {\"code\", \"message\"}}.",
 E={"missing_url": "400: the url parameter is missing.", "bad_url": "400: not a public site address (a private address, a bad name, more than 2,048 characters).",
    "site_unreachable": "422: the site did not answer our crawler, so access cannot be judged. Nothing is guessed: there is no all-clear.",
    "rate_limited": "429: over the limits below. Retry-After says how many seconds to wait.", "busy": "503: CitedBy is running its maximum number of checks. Retry-After is 60 seconds.",
    "unavailable": "502 or 503: the checker did not answer. Try again in a minute."},
 pending="A slow site returns 202 with {\"status\": \"pending\"}: the check keeps running and its result is stored. Ask again after the Retry-After seconds.",
 lim_h="Limits", lim=["30 requests per hour for each IP address.", "At most 12 sites per hour that were not already checked in the last 6 hours. A site that was checked in that time is answered from the stored result and does not use this allowance.",
    "No key and no sign-up: the limits are the only gate. The result is cached for 6 hours."],
 not_h="What it does not return", nots=["No grade and no score. The API returns what the free check shows for each crawler.", "No page-by-page crawl, no exact fix per page and no llms.txt check: those are in the audit.",
    "It tests the home page with each crawler's user-agent string, from our own address. A firewall that checks the vendors' IP ranges can treat the real crawlers differently.",
    "A robots.txt that redirects to another domain is not followed: it shows as not_found with the redirect's status."],
 spec_h="OpenAPI", spec_p="The spec is at {link}. Load it in Postman, Insomnia or a code generator.",
 terms_h="Terms of use", terms=["Free to use, also in your own product, with no key or account.", "If you show our results to other people (a page, a report, a README, a tool), link to CitedBy: {docs} or the report_url of the site. The attribution field carries the text and the link.",
    "Do not present the result as your own check, and do not send bursts: the limits apply to each address, and we can change or end them. There is no uptime promise.",
    "We count the calls, as a number per day. The address you call from is used for the limits and is kept in memory, not in a database. More in {privacy}."],
 rel_h="Same check, other ways", rel=[("/free-ai-visibility-check", "The free check in your browser"), ("/mcp-server", "MCP server for Claude, Cursor and Codex"), ("/ci", "Command line and GitHub Action"), ("/wordpress-plugin", "WordPress plugin"), ("/badge", "A badge for your site")],
 cta="Need more than crawler access? A CitedBy audit crawls your site, up to your plan's page limit, and gives you the exact fix. See {plans}.", plans="the plans", privacy="Privacy"),
"fr": dict(
 title="API gratuite d'accès des robots IA (JSON, sans clé) | CitedBy",
 desc="Une API JSON gratuite qui dit quels robots IA peuvent lire un site : la réponse de robots.txt et du serveur pour chacun. Sans clé, CORS ouvert, spec OpenAPI.",
 h1="API d'accès des robots IA",
 ans="Une requête indique quels robots IA peuvent lire un site : GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot. Pour chacun, vous obtenez ce que dit robots.txt et ce que répond le serveur. C'est le résultat du contrôle gratuit des robots IA, en JSON. Sans clé, sans compte, CORS ouvert.",
 req_h="Requête", req_p="Une requête GET avec un paramètre :", req_url="url", req_url_p="Un domaine ou une adresse complète, par exemple example.com ou https://example.com/boutique. Seul le site est contrôlé : le chemin, le port et www. sont ignorés.",
 ex_h="Exemple", ex_p="Le contrôle de {site} le {date} : un site public, pas un client de CitedBy, avec le résultat tel que l'API l'a renvoyé. Lancé un autre jour, il peut différer.",
 fields_h="Ce que contient la réponse", fields_p="Chaque champ ci-dessous figure dans toute réponse réussie.",
 F={"site": "Le domaine contrôlé.",
    "checked_at": "Le moment où CitedBy a fait le contrôle, en UTC. Un site contrôlé au cours des 6 dernières heures renvoie le résultat conservé : la date peut donc précéder votre requête.",
    "robots_txt.state": "found, not_found, unreachable ou server_error. Une erreur serveur sur robots.txt oblige un robot à supposer qu'il n'a pas le droit d'explorer (RFC 9309) : tous les robots apparaissent alors comme bloqués.",
    "robots_txt.status": "Le statut HTTP de la réponse de robots.txt.",
    "robots_txt.blocks_all_crawlers": "true quand les règles pour tous les robots (*) ferment tout le site.",
    "summary": "Combien des 8 robots peuvent lire le site (allowed), et les noms de ceux qui ne le peuvent pas (blocked).",
    "crawlers[].id": "Le nom du robot.",
    "crawlers[].role": "training (collecte du texte pour entraîner des modèles), search (peut citer vos pages dans ses réponses) ou user_fetch (ouvre une page quand quelqu'un le demande).",
    "crawlers[].robots_txt": "allowed, disallowed ou not_read (robots.txt n'a pas pu être lu).",
    "crawlers[].robots_txt_rule": "La règle de robots.txt qui ferme le site à ce robot, ou null.",
    "crawlers[].server": "ok, blocked (le serveur répond à l'user-agent de ce robot par un refus ou une page de contrôle), down (une erreur) ou not_tested. Google-Extended n'est qu'un jeton de robots.txt : il n'est jamais testé sur le serveur.",
    "crawlers[].access": "Le verdict pour ce robot, l'une des valeurs ci-dessous.",
    "report_url": "La page de résultat complète du contrôle gratuit pour ce site.",
    "audit_url": "Où auditer le site entier.",
    "attribution": "Le texte et le lien à afficher quand vous montrez le résultat (voir les conditions)."},
 acc_h="Les valeurs d'accès", acc_p="allowed signifie que robots.txt ne ferme pas le site au robot et que le serveur lui a répondu. Les autres disent ce qui bloque :",
 A={"allowed": "le robot peut lire le site.", "blocked_by_robots_txt": "robots.txt ferme le site à ce robot.", "blocked_by_server": "le serveur refuse l'user-agent de ce robot ou lui montre une page de contrôle.",
    "blocked_by_robots_txt_and_server": "les deux.", "server_error": "le serveur a répondu à ce robot par une erreur."},
 acc_note="Bloquer un robot d'entraînement peut être un choix. L'API le signale comme bloqué et n'en fait pas un problème.",
 err_h="Erreurs", err_p="Un échec est une erreur, jamais une supposition. Le corps est du JSON : {\"error\": {\"code\", \"message\"}}.",
 E={"missing_url": "400 : le paramètre url manque.", "bad_url": "400 : ce n'est pas l'adresse d'un site public (adresse privée, nom invalide, plus de 2 048 caractères).",
    "site_unreachable": "422 : le site n'a pas répondu à notre robot, l'accès ne peut donc pas être jugé. Rien n'est supposé : il n'y a pas de feu vert.",
    "rate_limited": "429 : limites ci-dessous dépassées. Retry-After indique combien de secondes attendre.", "busy": "503 : CitedBy exécute son nombre maximal de contrôles. Retry-After vaut 60 secondes.",
    "unavailable": "502 ou 503 : le contrôleur n'a pas répondu. Réessayez dans une minute."},
 pending="Un site lent renvoie 202 avec {\"status\": \"pending\"} : le contrôle continue et son résultat est conservé. Redemandez après les secondes de Retry-After.",
 lim_h="Limites", lim=["30 requêtes par heure et par adresse IP.", "12 sites par heure au plus qui n'ont pas déjà été contrôlés dans les 6 dernières heures. Un site contrôlé pendant ce délai reçoit le résultat conservé et n'utilise pas ce quota.",
    "Ni clé ni inscription : les limites sont la seule barrière. Le résultat est conservé 6 heures."],
 not_h="Ce qu'elle ne renvoie pas", nots=["Ni note ni score. L'API renvoie ce que montre le contrôle gratuit pour chaque robot.", "Ni exploration page par page, ni correctif exact par page, ni contrôle de llms.txt : ils sont dans l'audit.",
    "Elle teste la page d'accueil avec la chaîne user-agent de chaque robot, depuis notre propre adresse. Un pare-feu qui vérifie les plages d'adresses des éditeurs peut traiter les vrais robots autrement.",
    "Un robots.txt qui redirige vers un autre domaine n'est pas suivi : il apparaît comme not_found avec le statut de la redirection."],
 spec_h="OpenAPI", spec_p="La spécification est à {link}. Chargez-la dans Postman, Insomnia ou un générateur de code.",
 terms_h="Conditions d'utilisation", terms=["Gratuite, y compris dans votre propre produit, sans clé ni compte.", "Si vous montrez nos résultats à d'autres personnes (une page, un rapport, un README, un outil), faites un lien vers CitedBy : {docs} ou le report_url du site. Le champ attribution contient le texte et le lien.",
    "Ne présentez pas le résultat comme votre propre contrôle et n'envoyez pas de rafales : les limites s'appliquent à chaque adresse, et nous pouvons les changer ou y mettre fin. Aucune promesse de disponibilité.",
    "Nous comptons les appels, en un nombre par jour. L'adresse depuis laquelle vous appelez sert aux limites et reste en mémoire, pas dans une base de données. Détails : {privacy}."],
 rel_h="Le même contrôle, autrement", rel=[("/fr/free-ai-visibility-check", "Le contrôle gratuit dans votre navigateur"), ("/mcp-server", "Serveur MCP pour Claude, Cursor et Codex"), ("/ci", "Ligne de commande et GitHub Action"), ("/wordpress-plugin", "Extension WordPress"), ("/fr/badge", "Un badge pour votre site")],
 cta="Besoin de plus que l'accès des robots ? Un audit CitedBy explore votre site, jusqu'à la limite de pages de votre formule, et donne le correctif exact. Voir {plans}.", plans="les formules", privacy="Confidentialité"),
"nl": dict(
 title="Gratis API: toegang van AI-crawlers (JSON) | CitedBy",
 desc="Gratis JSON-API: welke AI-crawlers een site kunnen lezen, met het antwoord van robots.txt en server per crawler. Zonder sleutel, met OpenAPI-spec.",
 h1="API voor AI-crawlertoegang",
 ans="Eén verzoek zegt welke AI-crawlers een site kunnen lezen: GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot. Per crawler krijg je wat robots.txt zegt en wat de server antwoordt. Het is het resultaat van de gratis AI-crawlercheck, als JSON. Zonder sleutel, zonder account, CORS open.",
 req_h="Verzoek", req_p="Eén GET-verzoek met één parameter:", req_url="url", req_url_p="Een domein of een volledig adres, bijvoorbeeld example.com of https://example.com/winkel. Alleen de site wordt gecontroleerd: pad, poort en www. vallen weg.",
 ex_h="Voorbeeld", ex_p="De check van {site} op {date}: een openbare site, geen klant van CitedBy, met het resultaat zoals de API het gaf. Op een andere dag kan het antwoord verschillen.",
 fields_h="Wat het antwoord bevat", fields_p="Elk veld hieronder staat in elk geslaagd antwoord.",
 F={"site": "Het gecontroleerde domein.",
    "checked_at": "Wanneer CitedBy de check deed, in UTC. Een site die in de laatste 6 uur is gecontroleerd geeft het bewaarde resultaat, dus dit kan eerder zijn dan je verzoek.",
    "robots_txt.state": "found, not_found, unreachable of server_error. Een serverfout op robots.txt betekent dat een crawler moet aannemen dat hij niet mag crawlen (RFC 9309): elke crawler staat dan als geblokkeerd.",
    "robots_txt.status": "De HTTP-status waarmee robots.txt antwoordde.",
    "robots_txt.blocks_all_crawlers": "true als de regels voor alle crawlers (*) de hele site afsluiten.",
    "summary": "Hoeveel van de 8 crawlers de site kunnen lezen (allowed) en de namen van wie dat niet kan (blocked).",
    "crawlers[].id": "De naam van de crawler.",
    "crawlers[].role": "training (verzamelt tekst om modellen te trainen), search (kan je pagina's noemen in antwoorden) of user_fetch (opent een pagina als iemand ernaar vraagt).",
    "crawlers[].robots_txt": "allowed, disallowed of not_read (robots.txt kon niet worden gelezen).",
    "crawlers[].robots_txt_rule": "De robots.txt-regel die de site voor deze crawler afsluit, of null.",
    "crawlers[].server": "ok, blocked (de server antwoordt de user-agent van deze crawler met een weigering of een controlepagina), down (een fout) of not_tested. Google-Extended is alleen een robots.txt-token en wordt dus nooit op de server getest.",
    "crawlers[].access": "Het oordeel voor deze crawler, een van de waarden hieronder.",
    "report_url": "De volledige resultaatpagina van de gratis check voor deze site.",
    "audit_url": "Waar je de hele site laat doorlichten.",
    "attribution": "De tekst en link om te tonen als je het resultaat laat zien (zie de voorwaarden)."},
 acc_h="De toegangswaarden", acc_p="allowed betekent dat robots.txt de site niet voor de crawler afsluit en dat de server hem antwoordde. De andere waarden zeggen wat in de weg staat:",
 A={"allowed": "de crawler kan de site lezen.", "blocked_by_robots_txt": "robots.txt sluit de site voor deze crawler af.", "blocked_by_server": "de server wijst de user-agent van deze crawler af of toont hem een controlepagina.",
    "blocked_by_robots_txt_and_server": "allebei.", "server_error": "de server antwoordde deze crawler met een fout."},
 acc_note="Een trainingscrawler blokkeren kan een keuze zijn. De API meldt het als geblokkeerd en noemt het geen probleem.",
 err_h="Fouten", err_p="Een mislukking is een fout, nooit een gok. De inhoud is JSON: {\"error\": {\"code\", \"message\"}}.",
 E={"missing_url": "400: de parameter url ontbreekt.", "bad_url": "400: geen openbaar siteadres (een privéadres, een ongeldige naam, meer dan 2.048 tekens).",
    "site_unreachable": "422: de site antwoordde onze crawler niet, dus de toegang kan niet worden beoordeeld. Er wordt niets geraden: er is geen groen licht.",
    "rate_limited": "429: boven de limieten hieronder. Retry-After zegt hoeveel seconden je moet wachten.", "busy": "503: CitedBy voert zijn maximale aantal checks uit. Retry-After is 60 seconden.",
    "unavailable": "502 of 503: de checker antwoordde niet. Probeer het over een minuut opnieuw."},
 pending="Een trage site geeft 202 met {\"status\": \"pending\"}: de check loopt door en het resultaat wordt bewaard. Vraag opnieuw na de seconden van Retry-After.",
 lim_h="Limieten", lim=["30 verzoeken per uur per IP-adres.", "Hoogstens 12 sites per uur die niet in de laatste 6 uur al zijn gecontroleerd. Een site die in die tijd is gecontroleerd krijgt het bewaarde resultaat en gebruikt deze ruimte niet.",
    "Geen sleutel en geen aanmelding: de limieten zijn de enige drempel. Het resultaat wordt 6 uur bewaard."],
 not_h="Wat ze niet teruggeeft", nots=["Geen cijfer en geen score. De API geeft wat de gratis check per crawler toont.", "Geen crawl per pagina, geen exacte oplossing per pagina en geen llms.txt-check: die zitten in de audit.",
    "Ze test de homepage met de user-agent-tekst van elke crawler, vanaf ons eigen adres. Een firewall die de IP-bereiken van de aanbieders controleert kan de echte crawlers anders behandelen.",
    "Een robots.txt die naar een ander domein doorverwijst wordt niet gevolgd: hij staat als not_found met de status van de doorverwijzing."],
 spec_h="OpenAPI", spec_p="De spec staat op {link}. Laad hem in Postman, Insomnia of een codegenerator.",
 terms_h="Gebruiksvoorwaarden", terms=["Gratis te gebruiken, ook in je eigen product, zonder sleutel of account.", "Laat je onze resultaten aan anderen zien (een pagina, een rapport, een README, een tool), link dan naar CitedBy: {docs} of de report_url van de site. Het veld attribution bevat de tekst en de link.",
    "Presenteer het resultaat niet als je eigen check en stuur geen stortvloeden: de limieten gelden per adres en we kunnen ze wijzigen of beëindigen. Geen belofte over beschikbaarheid.",
    "We tellen de aanroepen, als één getal per dag. Het adres waarvandaan je aanroept dient voor de limieten en blijft in het geheugen, niet in een database. Meer in {privacy}."],
 rel_h="Dezelfde check, op andere manieren", rel=[("/nl/free-ai-visibility-check", "De gratis check in je browser"), ("/mcp-server", "MCP-server voor Claude, Cursor en Codex"), ("/ci", "Opdrachtregel en GitHub Action"), ("/wordpress-plugin", "WordPress-plugin"), ("/nl/badge", "Een badge voor je site")],
 cta="Meer nodig dan crawlertoegang? Een CitedBy-audit crawlt je site, tot de paginalimiet van je abonnement, en geeft je de exacte oplossing. Zie {plans}.", plans="de abonnementen", privacy="Privacy"),
"de": dict(
 title="Kostenlose API: Zugriff von KI-Crawlern (JSON) | CitedBy",
 desc="Kostenlose JSON-API: welche KI-Crawler eine Website lesen können, mit Antwort von robots.txt und Server je Crawler. Ohne Schlüssel, mit OpenAPI.",
 h1="API für den Zugriff von KI-Crawlern",
 ans="Eine Anfrage sagt, welche KI-Crawler eine Website lesen können: GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot. Für jeden erhalten Sie, was robots.txt sagt und was der Server antwortet. Es ist das Ergebnis des kostenlosen KI-Crawler-Checks, als JSON. Ohne Schlüssel, ohne Konto, CORS offen.",
 req_h="Anfrage", req_p="Eine GET-Anfrage mit einem Parameter:", req_url="url", req_url_p="Eine Domain oder eine vollständige Adresse, zum Beispiel example.com oder https://example.com/shop. Geprüft wird nur die Website: Pfad, Port und www. entfallen.",
 ex_h="Beispiel", ex_p="Die Prüfung von {site} am {date}: eine öffentliche Website, kein CitedBy-Kunde, mit dem Ergebnis, wie die API es geliefert hat. An einem anderen Tag kann die Antwort abweichen.",
 fields_h="Was die Antwort enthält", fields_p="Jedes Feld unten steht in jeder erfolgreichen Antwort.",
 F={"site": "Die geprüfte Domain.",
    "checked_at": "Wann CitedBy die Prüfung durchgeführt hat, in UTC. Eine Website, die in den letzten 6 Stunden geprüft wurde, liefert das gespeicherte Ergebnis; der Zeitpunkt kann also vor Ihrer Anfrage liegen.",
    "robots_txt.state": "found, not_found, unreachable oder server_error. Ein Serverfehler bei robots.txt heißt, dass ein Crawler annehmen muss, nicht crawlen zu dürfen (RFC 9309); dann gilt jeder Crawler als blockiert.",
    "robots_txt.status": "Der HTTP-Status, mit dem robots.txt geantwortet hat.",
    "robots_txt.blocks_all_crawlers": "true, wenn die Regeln für alle Crawler (*) die ganze Website sperren.",
    "summary": "Wie viele der 8 Crawler die Website lesen können (allowed) und die Namen derer, die es nicht können (blocked).",
    "crawlers[].id": "Der Name des Crawlers.",
    "crawlers[].role": "training (sammelt Text zum Training von Modellen), search (kann Ihre Seiten in Antworten nennen) oder user_fetch (öffnet eine Seite, wenn eine Person danach fragt).",
    "crawlers[].robots_txt": "allowed, disallowed oder not_read (robots.txt konnte nicht gelesen werden).",
    "crawlers[].robots_txt_rule": "Die robots.txt-Regel, die die Website für diesen Crawler sperrt, oder null.",
    "crawlers[].server": "ok, blocked (der Server beantwortet den User-Agent dieses Crawlers mit einer Abweisung oder einer Prüfseite), down (ein Fehler) oder not_tested. Google-Extended ist nur ein robots.txt-Token und wird nie auf dem Server getestet.",
    "crawlers[].access": "Das Urteil für diesen Crawler, einer der Werte unten.",
    "report_url": "Die vollständige Ergebnisseite des kostenlosen Checks für diese Website.",
    "audit_url": "Wo Sie die ganze Website prüfen lassen.",
    "attribution": "Der Text und der Link, die Sie anzeigen, wenn Sie das Ergebnis zeigen (siehe die Bedingungen)."},
 acc_h="Die Zugriffswerte", acc_p="allowed heißt: robots.txt sperrt die Website nicht für den Crawler, und der Server hat ihm geantwortet. Die anderen nennen, was im Weg steht:",
 A={"allowed": "der Crawler kann die Website lesen.", "blocked_by_robots_txt": "robots.txt sperrt die Website für diesen Crawler.", "blocked_by_server": "der Server weist den User-Agent dieses Crawlers ab oder zeigt ihm eine Prüfseite.",
    "blocked_by_robots_txt_and_server": "beides.", "server_error": "der Server hat diesem Crawler mit einem Fehler geantwortet."},
 acc_note="Einen Trainings-Crawler zu blockieren kann eine Entscheidung sein. Die API meldet ihn als blockiert und nennt das kein Problem.",
 err_h="Fehler", err_p="Ein Misserfolg ist ein Fehler, nie eine Vermutung. Der Inhalt ist JSON: {\"error\": {\"code\", \"message\"}}.",
 E={"missing_url": "400: der Parameter url fehlt.", "bad_url": "400: keine öffentliche Website-Adresse (eine private Adresse, ein ungültiger Name, mehr als 2.048 Zeichen).",
    "site_unreachable": "422: die Website hat unserem Crawler nicht geantwortet, der Zugriff lässt sich daher nicht beurteilen. Es wird nichts vermutet: Es gibt kein Okay.",
    "rate_limited": "429: die Grenzen unten sind überschritten. Retry-After nennt die Sekunden bis zum nächsten Versuch.", "busy": "503: CitedBy führt die maximale Zahl an Prüfungen aus. Retry-After beträgt 60 Sekunden.",
    "unavailable": "502 oder 503: der Checker hat nicht geantwortet. Versuchen Sie es in einer Minute erneut."},
 pending="Eine langsame Website liefert 202 mit {\"status\": \"pending\"}: die Prüfung läuft weiter und ihr Ergebnis wird gespeichert. Fragen Sie nach den Sekunden aus Retry-After erneut.",
 lim_h="Grenzen", lim=["30 Anfragen pro Stunde je IP-Adresse.", "Höchstens 12 Websites pro Stunde, die nicht schon in den letzten 6 Stunden geprüft wurden. Eine Website, die in dieser Zeit geprüft wurde, erhält das gespeicherte Ergebnis und verbraucht dieses Kontingent nicht.",
    "Kein Schlüssel und keine Anmeldung: Die Grenzen sind die einzige Hürde. Das Ergebnis wird 6 Stunden gespeichert."],
 not_h="Was sie nicht liefert", nots=["Keine Note und keinen Score. Die API liefert, was der kostenlose Check je Crawler zeigt.", "Keinen Crawl Seite für Seite, keine exakte Korrektur je Seite und keine llms.txt-Prüfung: Das gehört zum Audit.",
    "Sie testet die Startseite mit dem User-Agent-String jedes Crawlers, von unserer eigenen Adresse aus. Eine Firewall, die die IP-Bereiche der Anbieter prüft, kann die echten Crawler anders behandeln.",
    "Eine robots.txt, die auf eine andere Domain weiterleitet, wird nicht verfolgt: Sie erscheint als not_found mit dem Status der Weiterleitung."],
 spec_h="OpenAPI", spec_p="Die Spezifikation liegt unter {link}. Laden Sie sie in Postman, Insomnia oder einen Codegenerator.",
 terms_h="Nutzungsbedingungen", terms=["Kostenlos nutzbar, auch in Ihrem eigenen Produkt, ohne Schlüssel oder Konto.", "Wenn Sie unsere Ergebnisse anderen zeigen (eine Seite, ein Bericht, eine README, ein Tool), verlinken Sie CitedBy: {docs} oder die report_url der Website. Das Feld attribution enthält Text und Link.",
    "Geben Sie das Ergebnis nicht als eigene Prüfung aus und senden Sie keine Schübe: Die Grenzen gelten je Adresse, und wir können sie ändern oder beenden. Es gibt kein Verfügbarkeitsversprechen.",
    "Wir zählen die Aufrufe, als eine Zahl pro Tag. Die Adresse, von der Sie aufrufen, dient den Grenzen und bleibt im Arbeitsspeicher, nicht in einer Datenbank. Mehr unter {privacy}."],
 rel_h="Derselbe Check, anders", rel=[("/de/free-ai-visibility-check", "Der kostenlose Check im Browser"), ("/mcp-server", "MCP-Server für Claude, Cursor und Codex"), ("/ci", "Kommandozeile und GitHub Action"), ("/wordpress-plugin", "WordPress-Plugin"), ("/de/badge", "Ein Badge für Ihre Website")],
 cta="Brauchen Sie mehr als den Crawler-Zugriff? Ein CitedBy-Audit crawlt Ihre Website, bis zum Seitenlimit Ihres Tarifs, und liefert die exakte Korrektur. Siehe {plans}.", plans="die Tarife", privacy="Datenschutz"),
"es": dict(
 title="API gratuita: acceso de rastreadores de IA (JSON) | CitedBy",
 desc="API JSON gratuita: qué rastreadores de IA pueden leer un sitio, con la respuesta de robots.txt y del servidor. Sin clave, con especificación OpenAPI.",
 h1="API de acceso de rastreadores de IA",
 ans="Una petición dice qué rastreadores de IA pueden leer un sitio: GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot. De cada uno obtienes lo que dice robots.txt y lo que responde el servidor. Es el resultado de la comprobación gratuita de rastreadores de IA, en JSON. Sin clave, sin cuenta, CORS abierto.",
 req_h="Petición", req_p="Una petición GET con un parámetro:", req_url="url", req_url_p="Un dominio o una dirección completa, por ejemplo example.com o https://example.com/tienda. Solo se comprueba el sitio: se descartan la ruta, el puerto y www.",
 ex_h="Ejemplo", ex_p="La comprobación de {site} el {date}: un sitio público, no cliente de CitedBy, con el resultado tal como lo devolvió la API. Otro día la respuesta puede ser distinta.",
 fields_h="Qué contiene la respuesta", fields_p="Cada campo de abajo está en toda respuesta correcta.",
 F={"site": "El dominio comprobado.",
    "checked_at": "Cuándo hizo CitedBy la comprobación, en UTC. Un sitio comprobado en las últimas 6 horas devuelve el resultado guardado, así que puede ser anterior a tu petición.",
    "robots_txt.state": "found, not_found, unreachable o server_error. Un error de servidor en robots.txt obliga al rastreador a suponer que no puede rastrear (RFC 9309), así que todos aparecen como bloqueados.",
    "robots_txt.status": "El estado HTTP con el que respondió robots.txt.",
    "robots_txt.blocks_all_crawlers": "true cuando las reglas para todos los rastreadores (*) cierran todo el sitio.",
    "summary": "Cuántos de los 8 rastreadores pueden leer el sitio (allowed) y los nombres de los que no pueden (blocked).",
    "crawlers[].id": "El nombre del rastreador.",
    "crawlers[].role": "training (recoge texto para entrenar modelos), search (puede citar tus páginas en las respuestas) o user_fetch (abre una página cuando una persona lo pide).",
    "crawlers[].robots_txt": "allowed, disallowed o not_read (no se pudo leer robots.txt).",
    "crawlers[].robots_txt_rule": "La regla de robots.txt que cierra el sitio a este rastreador, o null.",
    "crawlers[].server": "ok, blocked (el servidor responde al user-agent de este rastreador con un rechazo o una página de verificación), down (un error) o not_tested. Google-Extended es solo un token de robots.txt, así que nunca se prueba en el servidor.",
    "crawlers[].access": "El veredicto para este rastreador, uno de los valores de abajo.",
    "report_url": "La página de resultado completa de la comprobación gratuita de este sitio.",
    "audit_url": "Dónde auditar el sitio entero.",
    "attribution": "El texto y el enlace que debes mostrar cuando enseñes el resultado (ver las condiciones)."},
 acc_h="Los valores de acceso", acc_p="allowed significa que robots.txt no cierra el sitio al rastreador y que el servidor le respondió. Los demás dicen qué lo impide:",
 A={"allowed": "el rastreador puede leer el sitio.", "blocked_by_robots_txt": "robots.txt cierra el sitio a este rastreador.", "blocked_by_server": "el servidor rechaza el user-agent de este rastreador o le muestra una página de verificación.",
    "blocked_by_robots_txt_and_server": "las dos cosas.", "server_error": "el servidor respondió a este rastreador con un error."},
 acc_note="Bloquear a un rastreador de entrenamiento puede ser una decisión. La API lo marca como bloqueado y no lo presenta como un problema.",
 err_h="Errores", err_p="Un fallo es un error, nunca una suposición. El cuerpo es JSON: {\"error\": {\"code\", \"message\"}}.",
 E={"missing_url": "400: falta el parámetro url.", "bad_url": "400: no es la dirección de un sitio público (una dirección privada, un nombre no válido, más de 2.048 caracteres).",
    "site_unreachable": "422: el sitio no respondió a nuestro rastreador, así que el acceso no se puede juzgar. No se supone nada: no hay luz verde.",
    "rate_limited": "429: se superaron los límites de abajo. Retry-After indica cuántos segundos esperar.", "busy": "503: CitedBy está ejecutando su máximo de comprobaciones. Retry-After es de 60 segundos.",
    "unavailable": "502 o 503: el comprobador no respondió. Inténtalo de nuevo en un minuto."},
 pending="Un sitio lento devuelve 202 con {\"status\": \"pending\"}: la comprobación sigue y su resultado se guarda. Vuelve a preguntar pasados los segundos de Retry-After.",
 lim_h="Límites", lim=["30 peticiones por hora por dirección IP.", "Como máximo 12 sitios por hora que no se hayan comprobado ya en las últimas 6 horas. Un sitio comprobado en ese plazo recibe el resultado guardado y no gasta este cupo.",
    "Sin clave ni registro: los límites son la única barrera. El resultado se guarda 6 horas."],
 not_h="Lo que no devuelve", nots=["Ni nota ni puntuación. La API devuelve lo que muestra la comprobación gratuita para cada rastreador.", "Ni rastreo página por página, ni corrección exacta por página, ni comprobación de llms.txt: eso está en la auditoría.",
    "Prueba la página de inicio con la cadena user-agent de cada rastreador, desde nuestra propia dirección. Un cortafuegos que verifica los rangos de IP de los proveedores puede tratar de otro modo a los rastreadores reales.",
    "Un robots.txt que redirige a otro dominio no se sigue: aparece como not_found con el estado de la redirección."],
 spec_h="OpenAPI", spec_p="La especificación está en {link}. Cárgala en Postman, Insomnia o un generador de código.",
 terms_h="Condiciones de uso", terms=["Uso gratuito, también en tu propio producto, sin clave ni cuenta.", "Si enseñas nuestros resultados a otras personas (una página, un informe, un README, una herramienta), enlaza a CitedBy: {docs} o el report_url del sitio. El campo attribution trae el texto y el enlace.",
    "No presentes el resultado como una comprobación propia y no envíes ráfagas: los límites se aplican a cada dirección y podemos cambiarlos o acabar con ellos. No prometemos disponibilidad.",
    "Contamos las llamadas, como un número por día. La dirección desde la que llamas sirve para los límites y se queda en memoria, no en una base de datos. Más en {privacy}."],
 rel_h="La misma comprobación, de otras formas", rel=[("/es/free-ai-visibility-check", "La comprobación gratuita en tu navegador"), ("/mcp-server", "Servidor MCP para Claude, Cursor y Codex"), ("/ci", "Línea de comandos y GitHub Action"), ("/wordpress-plugin", "Plugin de WordPress"), ("/es/badge", "Una insignia para tu web")],
 cta="¿Necesitas más que el acceso de los rastreadores? Una auditoría de CitedBy rastrea tu sitio, hasta el límite de páginas de tu plan, y te da la corrección exacta. Mira {plans}.", plans="los planes", privacy="Privacidad"),
}


def _fr(x):  # surface contract: a narrow no-break space before : ; ? ! in French
    if isinstance(x, str): return re.sub(r"(?<=\S) ([:;?!])", "\u202f\\1", x)
    if isinstance(x, list): return [_fr(i) for i in x]
    if isinstance(x, tuple): return tuple(_fr(i) for i in x)
    if isinstance(x, dict): return {k: _fr(v) for k, v in x.items()}
    return x


T["fr"] = _fr(T["fr"])


def lp(lg): return "" if lg == "en" else "/" + lg
def url(lg): return f"{SITE}{lp(lg)}/ai-access-api"


def date_in(lg):
    y, m, d = SAMPLE["checked_at"][:10].split("-"); mo = MONTHS[lg][int(m) - 1]
    return {"de": f"{int(d)}. {mo} {y}", "es": f"{int(d)} de {mo} de {y}"}.get(lg, f"{int(d)} {mo} {y}")


def sample_json():
    s = SAMPLE; rows = ",\n".join("    " + json.dumps(c, ensure_ascii=False) for c in s["crawlers"])
    rest = {k: v for k, v in s.items() if k != "crawlers"}
    head = json.dumps({k: rest[k] for k in ("api_version", "site", "checked_at", "robots_txt", "summary")}, ensure_ascii=False)[:-1]
    tail = json.dumps({k: rest[k] for k in ("report_url", "audit_url", "attribution", "docs")}, ensure_ascii=False)[1:]
    return head + ',\n  "crawlers": [\n' + rows + "\n  ],\n  " + tail


def page(lg):
    t = T[lg]; docs = url(lg)
    curl = f'curl "{SITE}/api/v1/ai-access?url={SAMPLE["site"]}"'
    fields = "".join(f"<li><code>{E(f)}</code>: {E(t['F'][f])}</li>" for f in FIELDS)
    acc = "".join(f"<li><code>{E(a)}</code>: {E(t['A'][a])}</li>" for a in ACCESS)
    errs = "".join(f"<li><code>{E(c)}</code>: {E(t['E'][c])}</li>" for c in CODES)
    rel = "".join(f'<li><a href="{E(h)}">{E(x)}</a></li>' for h, x in t["rel"])
    terms = "".join(f"<li>{E(x).replace('{docs}', f'<a href=\"{docs}\">{docs}</a>').replace('{privacy}', f'<a href=\"{lp(lg)}/privacy\">{E(t['privacy'])}</a>')}</li>" for x in t["terms"])
    body = (f'<h1>{E(t["h1"])}</h1><p class="ans">{E(t["ans"])}</p>'
            f'<h2>{E(t["req_h"])}</h2><p>{E(t["req_p"])}</p><pre>GET {SITE}/api/v1/ai-access?url=example.com</pre><ul><li><code>{t["req_url"]}</code>: {E(t["req_url_p"])}</li></ul>'
            f'<h2>{E(t["ex_h"])}</h2><p>{E(t["ex_p"].format(site=SAMPLE["site"], date=date_in(lg)))}</p><pre>{E(curl)}</pre><pre>{E(sample_json())}</pre>'
            f'<h2>{E(t["fields_h"])}</h2><p>{E(t["fields_p"])}</p><ul>{fields}</ul>'
            f'<h2>{E(t["acc_h"])}</h2><p>{E(t["acc_p"])}</p><ul>{acc}</ul><p>{E(t["acc_note"])}</p>'
            f'<h2>{E(t["err_h"])}</h2><p>{E(t["err_p"])}</p><ul>{errs}</ul><p>{E(t["pending"])}</p>'
            f'<h2>{E(t["lim_h"])}</h2><ul>{"".join(f"<li>{E(x)}</li>" for x in t["lim"])}</ul>'
            f'<h2>{E(t["not_h"])}</h2><ul>{"".join(f"<li>{E(x)}</li>" for x in t["nots"])}</ul>'
            f'<h2>{E(t["spec_h"])}</h2><p>{E(t["spec_p"]).replace("{link}", f"<a href=\"/openapi.json\">{SITE}/openapi.json</a>")}</p>'
            f'<h2 id="terms">{E(t["terms_h"])}</h2><ul>{terms}</ul>'
            f'<h2>{E(t["rel_h"])}</h2><ul>{rel}</ul>'
            f'<p>{" · ".join(f"<a href=\"{url(l)}\" hreflang=\"{l}\">{NAMES[l]}</a>" if l != lg else NAMES[l] for l in LANGS)}</p>'
            f'<p>{E(t["cta"]).replace("{plans}", f"<a href=\"{lp(lg)}/plans\">{E(t['plans'])}</a>")}</p>')
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{url(l)}">' for l in LANGS) + f'<link rel="alternate" hreflang="x-default" href="{url("en")}">'
    ld = {"@context": "https://schema.org", "@type": "TechArticle", "name": t["h1"], "headline": t["h1"], "url": docs, "inLanguage": lg, "description": t["desc"],
          "isPartOf": {"@type": "WebSite", "name": "CitedBy", "url": SITE}, "publisher": {"@type": "Organization", "name": "CitedBy", "url": SITE}}
    head = (f'<!doctype html><html lang="{lg}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(t["title"])}</title>'
            f'<meta name="description" content="{E(t["desc"])}"><link rel="canonical" href="{docs}">{alts}<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">'
            f'<link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="stylesheet" href="/saas.css"><link rel="stylesheet" href="/doc.css?v={docshell.ver()}">'
            f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False).replace("</", "<\\/")}</script></head><body class="cb dc">')
    return docshell.localize(head + docshell.TOPBAR + '<main id="main">' + body + "</main>" + docshell.FOOTER + "</body></html>\n")


def openapi():
    t = T["en"]
    err = lambda d: {"description": d, "content": {"application/json": {"schema": {"$ref": "#/components/schemas/Error"}}}}
    retry = {"Retry-After": {"description": "Seconds to wait before asking again.", "schema": {"type": "integer"}}}
    crawler = {"type": "object", "required": ["id", "role", "robots_txt", "robots_txt_rule", "server", "access"], "properties": {
        "id": {"type": "string", "enum": [c["id"] for c in SAMPLE["crawlers"]], "description": t["F"]["crawlers[].id"]},
        "role": {"type": "string", "enum": ["training", "search", "user_fetch"], "description": t["F"]["crawlers[].role"]},
        "robots_txt": {"type": "string", "enum": ["allowed", "disallowed", "not_read"], "description": t["F"]["crawlers[].robots_txt"]},
        "robots_txt_rule": {"type": ["string", "null"], "description": t["F"]["crawlers[].robots_txt_rule"]},
        "server": {"type": "string", "enum": ["ok", "blocked", "down", "not_tested"], "description": t["F"]["crawlers[].server"]},
        "access": {"type": "string", "enum": ACCESS, "description": t["F"]["crawlers[].access"] + " " + " ".join(f"{a}: {t['A'][a]}" for a in ACCESS)}}}
    result = {"type": "object", "required": ["api_version", "site", "checked_at", "robots_txt", "summary", "crawlers", "report_url", "audit_url", "attribution", "docs"], "properties": {
        "api_version": {"type": "string", "const": "1"}, "site": {"type": "string", "description": t["F"]["site"]},
        "checked_at": {"type": "string", "format": "date-time", "description": t["F"]["checked_at"]},
        "robots_txt": {"type": "object", "required": ["state", "status", "blocks_all_crawlers"], "properties": {
            "state": {"type": "string", "enum": ["found", "not_found", "unreachable", "server_error"], "description": t["F"]["robots_txt.state"]},
            "status": {"type": ["integer", "null"], "description": t["F"]["robots_txt.status"]},
            "blocks_all_crawlers": {"type": "boolean", "description": t["F"]["robots_txt.blocks_all_crawlers"]}}},
        "summary": {"type": "object", "required": ["total", "allowed", "blocked"], "description": t["F"]["summary"], "properties": {
            "total": {"type": "integer"}, "allowed": {"type": "integer"}, "blocked": {"type": "array", "items": {"type": "string"}}}},
        "crawlers": {"type": "array", "items": crawler},
        "report_url": {"type": "string", "format": "uri", "description": t["F"]["report_url"]}, "audit_url": {"type": "string", "format": "uri", "description": t["F"]["audit_url"]},
        "attribution": {"type": "object", "required": ["text", "url"], "description": t["F"]["attribution"], "properties": {"text": {"type": "string"}, "url": {"type": "string", "format": "uri"}}},
        "docs": {"type": "string", "format": "uri"}}}
    return {"openapi": "3.1.0",
            "info": {"title": "CitedBy AI crawler access API", "version": "1.0.0", "summary": "Which AI crawlers can read a site: robots.txt and server answer for each one.",
                     "description": t["ans"] + "\n\nNo key, no account, CORS open. Limits: 30 requests per hour per IP address, at most 12 sites per hour that were not checked in the last 6 hours. No grade and no score: the API returns only what the free check at https://citedby.eu/tools/ai-crawler-check shows.",
                     "termsOfService": f"{SITE}/ai-access-api#terms", "contact": {"name": "CitedBy", "email": "hello@citedby.eu", "url": f"{SITE}/contact"},
                     "x-logo": {"url": f"{SITE}/favicon.svg"}},
            "externalDocs": {"description": "Documentation in English, French, Dutch, German and Spanish", "url": f"{SITE}/ai-access-api"},
            "servers": [{"url": SITE}], "tags": [{"name": "AI access"}],
            "paths": {"/api/v1/ai-access": {"get": {
                "operationId": "getAiAccess", "tags": ["AI access"], "summary": "Which AI crawlers can read a site",
                "description": "Checks robots.txt and one live request per crawler for the site and returns one result per crawler. A site checked in the last 6 hours returns the stored result.",
                "parameters": [{"name": "url", "in": "query", "required": True, "schema": {"type": "string", "maxLength": 2048, "examples": ["example.com"]}, "description": t["req_url_p"]}],
                "responses": {
                    "200": {"description": "The result.", "content": {"application/json": {"schema": {"$ref": "#/components/schemas/AiAccess"}, "example": SAMPLE}}},
                    "202": {"description": t["pending"], "headers": retry, "content": {"application/json": {"schema": {"type": "object", "properties": {"status": {"const": "pending"}, "site": {"type": "string"}, "message": {"type": "string"}, "retry_after_seconds": {"type": "integer"}}}}}},
                    "400": err(t["E"]["missing_url"] + " " + t["E"]["bad_url"]),
                    "422": err(t["E"]["site_unreachable"]),
                    "429": {**err(t["E"]["rate_limited"]), "headers": retry},
                    "502": err(t["E"]["unavailable"]),
                    "503": {**err(t["E"]["busy"]), "headers": retry}}}}},
            "components": {"schemas": {"AiAccess": result, "Error": {"type": "object", "required": ["error"], "properties": {"error": {"type": "object", "required": ["code", "message"], "properties": {
                "code": {"type": "string", "enum": CODES}, "message": {"type": "string"}}}}}}}}


def sitemap_and_llms():
    p = os.path.join(PUB, "sitemap.xml"); s = open(p, encoding="utf-8").read()
    s = re.sub(r"<url><loc>https://citedby\.eu(?:/(?:fr|nl|de|es))?/ai-access-api</loc>.*?</url>", "", s)
    alts = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{url(l)}"/>' for l in LANGS) + f'<xhtml:link rel="alternate" hreflang="x-default" href="{url("en")}"/>'
    new = "".join(f"<url><loc>{url(l)}</loc><lastmod>{SAMPLE['checked_at'][:10]}</lastmod>{alts}</url>" for l in LANGS)
    s = s.replace("</urlset>", new + "</urlset>"); open(p, "w", encoding="utf-8").write(s)
    line = f"- [CitedBy AI crawler access API]({url('en')}): free JSON API, GET /api/v1/ai-access?url=example.com returns which AI crawlers can read a site (robots.txt and server, per crawler), no key, OpenAPI spec at {SITE}/openapi.json"
    for name in ("llms.txt",):
        p = os.path.join(PUB, name); s = open(p, encoding="utf-8").read()
        if "ai-access-api" in s: continue
        i = s.index("- [CitedBy AI-Search Check for WordPress]")
        j = s.index("\n", i) + 1
        open(p, "w", encoding="utf-8").write(s[:j] + line + "\n" + s[j:])


def main():
    for lg in LANGS:
        d = os.path.join(PUB, lg) if lg != "en" else PUB
        open(os.path.join(d, "ai-access-api.html"), "w", encoding="utf-8").write(page(lg))
    open(os.path.join(PUB, "openapi.json"), "w", encoding="utf-8").write(json.dumps(openapi(), indent=2, ensure_ascii=False) + "\n")
    sitemap_and_llms()
    print("wrote 5 pages, openapi.json, sitemap and llms lines")


if __name__ == "__main__":
    main()
