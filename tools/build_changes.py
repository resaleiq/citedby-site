#!/usr/bin/env python3
"""Build /changes and /xx/changes (en, fr, nl, de, es) plus /changes.xml and /xx/changes.xml (RSS) from data/engine-changes.json (RES-2651, row 46).
Each record was read on the engine's own page (RES-2860): date, exact quote, source link. What the owner should do and what CitedBy checks are written here from our code.
A "checks" value starts with Y (CitedBy checks it), P (partly) or N (CitedBy does not check it); the page says which.
Adds the five pages to sitemap.xml and one line to llms.txt (idempotent). Run: python3 tools/build_changes.py [--check]. Standard library only."""
import datetime, email.utils, html, json, os, re, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB = os.path.join(HERE, "public")
SITE = "https://citedby.eu"
E = html.escape
LANGS = ("en", "fr", "nl", "de", "es")
BUILT = "2026-10-22"
REC = json.load(open(os.path.join(HERE, "data", "engine-changes.json"), encoding="utf-8"))

ENG = {"google-search": "Google Search", "google-ai-overviews": "AI Overviews", "google-ai-mode": "AI Mode", "google-discover": "Discover", "bing-copilot": "Bing and Copilot",
       "chatgpt": "ChatGPT", "gemini": "Gemini", "claude": "Claude", "copilot": "Copilot", "deepseek": "DeepSeek", "grok": "Grok", "chrome-lighthouse": "Lighthouse"}
MONTHS = {"en": "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec", "fr": "janv. févr. mars avr. mai juin juil. août sept. oct. nov. déc.", "nl": "jan feb mrt apr mei jun jul aug sep okt nov dec",
          "de": "Jan. Feb. März Apr. Mai Juni Juli Aug. Sept. Okt. Nov. Dez.", "es": "ene feb mar abr may jun jul ago sep oct nov dic"}
ENG_L = {"fr": {"bing-copilot": "Bing et Copilot"}, "nl": {"bing-copilot": "Bing en Copilot"}, "de": {"bing-copilot": "Bing und Copilot"}, "es": {"bing-copilot": "Bing y Copilot"}}
NOTE = {"en": "note added to the 3 June post", "fr": "note ajoutée à l'article du 3 juin", "nl": "notitie toegevoegd aan het bericht van 3 juni", "de": "Hinweis zum Beitrag vom 3. Juni ergänzt", "es": "nota añadida a la entrada del 3 de junio"}
FREE = {"google-llms-txt-guidance": ("llms-txt-checker", "free_llms"), "lighthouse-agentic-browsing-category": ("llms-txt-checker", "free_llms"),
        "gsc-generative-ai-reports-launch": ("findable-check", "free_find"), "bing-ai-performance-public-preview": ("findable-check", "free_find")}
def tp(l, p=""): return "/tools" + p if l == "en" else "/%s/tools%s" % (l, p)
RFC_MONTH = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()

UI = {
 "en": dict(sum_h='All changes at a glance', legend="Chip: Checked = CitedBy checks it · Partly checked = CitedBy checks part of it · Not checked = you check it in the engine's own tool.", free_llms='Check yours free: llms.txt checker', free_find='Check yours free: Findable? check', cta2='Free tools', title="Search and AI engine changes in 2026, and what we check | CitedBy", desc="Dated changes from Google, Bing and Lighthouse that affect how sites are found and cited, each read on the engine's page, with what to do.",
  h1="What changed in search and AI engines, and what CitedBy checks", lead="Each entry is a change an engine published itself, with its date, one exact quote and a link. Under it: what a site owner can do, and whether CitedBy checks it or not. Newest first.",
  more="We only list a change after reading it on the engine's own page. Trade-press reports and vendor studies are not entries. Rows we could not confirm on a primary page are left out.", read="Read on", quote="Quote (original wording)", do="What you can do", checks="What CitedBy checks", src="Source",
  yes="Checked", part="Partly checked", no="Not checked", feed="RSS feed of these changes", cta_h="See what a crawler sees on your site", cta_b="We crawl your site up to your plan's page limit and give you the exact fix for each issue. From €9, 14-day money-back guarantee.", cta="Audit my site", ln="Engine changes", fr_note="Source page and quote are in French.", lang_note="Entries are written in each language; the quote is the source's own wording."),
 "fr": dict(sum_h="Tous les changements en un coup d'œil", legend="Pastille : Vérifié = CitedBy le vérifie · Vérifié en partie = CitedBy en vérifie une partie · Non vérifié = à contrôler dans l'outil du moteur.", free_llms='Testez le vôtre gratuitement : vérificateur llms.txt', free_find='Testez le vôtre gratuitement : contrôle « Trouvable ? »', cta2='Outils gratuits', title="Recherche et moteurs IA : les changements de 2026 | CitedBy", desc="Changements datés de Google, Bing et Lighthouse qui touchent la façon dont les sites sont trouvés et cités, lus sur la page du moteur, avec quoi faire.",
  h1="Ce qui a changé dans la recherche et les moteurs IA, et ce que CitedBy vérifie", lead="Chaque entrée est un changement publié par le moteur lui-même, avec sa date, une citation exacte et un lien. En dessous : ce que vous pouvez faire, et si CitedBy le vérifie ou non. Le plus récent en premier.",
  more="Nous ne listons un changement qu'après l'avoir lu sur la page du moteur. Les articles de presse spécialisée et les études d'éditeurs ne sont pas des entrées. Les lignes que nous n'avons pas pu confirmer sur une page officielle sont écartées.", read="Lu le", quote="Citation (texte d'origine)", do="Ce que vous pouvez faire", checks="Ce que CitedBy vérifie", src="Source",
  yes="Vérifié", part="Vérifié en partie", no="Non vérifié", feed="Flux RSS de ces changements", cta_h="Voyez ce que voit un robot sur votre site", cta_b="Nous explorons votre site jusqu'à la limite de pages de votre offre et donnons le correctif exact de chaque problème. Dès 9 €, garantie de remboursement de 14 jours.", cta="Auditer mon site", ln="Changements des moteurs", fr_note="La page source et la citation sont en français.", lang_note="Les entrées sont rédigées dans chaque langue ; la citation reprend les mots de la source."),
 "nl": dict(sum_h='Alle wijzigingen in één oogopslag', legend='Label: Gecontroleerd = CitedBy controleert het · Gedeeltelijk gecontroleerd = CitedBy controleert een deel · Niet gecontroleerd = jij controleert het in de eigen tool van de engine.', free_llms='Check die van jou gratis: llms.txt-checker', free_find='Check die van jou gratis: Vindbaar?-check', cta2='Gratis tools', title="Wijzigingen bij zoek- en AI-engines in 2026 | CitedBy", desc="Gedateerde wijzigingen van Google, Bing en Lighthouse die bepalen hoe sites worden gevonden en geciteerd, gelezen bij de engine, met wat je kunt doen.",
  h1="Wat er veranderde bij zoek- en AI-engines, en wat CitedBy controleert", lead="Elk item is een wijziging die een engine zelf publiceerde, met datum, één exact citaat en een link. Eronder: wat je als site-eigenaar kunt doen en of CitedBy het controleert. Nieuwste eerst.",
  more="We nemen een wijziging pas op nadat we haar op de eigen pagina van de engine hebben gelezen. Berichten uit vakmedia en onderzoeken van leveranciers zijn geen items. Regels die we niet op een primaire pagina konden bevestigen, laten we weg.", read="Gelezen op", quote="Citaat (originele tekst)", do="Wat je kunt doen", checks="Wat CitedBy controleert", src="Bron",
  yes="Gecontroleerd", part="Gedeeltelijk gecontroleerd", no="Niet gecontroleerd", feed="RSS-feed van deze wijzigingen", cta_h="Zie wat een crawler op je site ziet", cta_b="We crawlen je site tot de paginalimiet van je abonnement en geven per probleem de exacte oplossing. Vanaf € 9, 14 dagen geld-terug-garantie.", cta="Mijn site auditen", ln="Wijzigingen bij engines", fr_note="De bronpagina en het citaat zijn in het Frans.", lang_note="De items zijn in elke taal geschreven; het citaat is de eigen tekst van de bron."),
 "de": dict(sum_h='Alle Änderungen auf einen Blick', legend='Kennzeichen: Geprüft = CitedBy prüft es · Teilweise geprüft = CitedBy prüft einen Teil · Nicht geprüft = Sie prüfen es im eigenen Tool der Engine.', free_llms='Prüfen Sie Ihre Website kostenlos: llms.txt-Checker', free_find='Prüfen Sie Ihre Website kostenlos: Auffindbarkeits-Check', cta2='Kostenlose Tools', title="Änderungen bei Such- und KI-Engines 2026 | CitedBy", desc="Datierte Änderungen von Google, Bing und Lighthouse, die beeinflussen, wie Websites gefunden und zitiert werden, auf der Engine-Seite gelesen, mit Empfehlung.",
  h1="Was sich bei Such- und KI-Engines geändert hat, und was CitedBy prüft", lead="Jeder Eintrag ist eine Änderung, die eine Engine selbst veröffentlicht hat, mit Datum, einem wörtlichen Zitat und einem Link. Darunter: was Sie als Website-Betreiber tun können und ob CitedBy es prüft. Neueste zuerst.",
  more="Wir führen eine Änderung erst auf, nachdem wir sie auf der eigenen Seite der Engine gelesen haben. Berichte der Fachpresse und Studien von Anbietern sind keine Einträge. Zeilen, die wir auf keiner Primärseite bestätigen konnten, lassen wir weg.", read="Gelesen am", quote="Zitat (Originaltext)", do="Was Sie tun können", checks="Was CitedBy prüft", src="Quelle",
  yes="Geprüft", part="Teilweise geprüft", no="Nicht geprüft", feed="RSS-Feed dieser Änderungen", cta_h="Sehen Sie, was ein Crawler auf Ihrer Website sieht", cta_b="Wir crawlen Ihre Website bis zum Seitenlimit Ihres Tarifs und geben für jedes Problem die genaue Korrektur. Ab 9 €, 14 Tage Geld-zurück-Garantie.", cta="Meine Website prüfen", ln="Änderungen der Engines", fr_note="Quellseite und Zitat sind auf Französisch.", lang_note="Die Einträge sind in jeder Sprache geschrieben; das Zitat ist der Wortlaut der Quelle."),
 "es": dict(sum_h='Todos los cambios de un vistazo', legend='Etiqueta: Comprobado = CitedBy lo comprueba · Comprobado en parte = CitedBy comprueba una parte · No comprobado = lo compruebas en la herramienta del propio motor.', free_llms='Comprueba el tuyo gratis: verificador de llms.txt', free_find='Comprueba el tuyo gratis: comprobación «¿Encontrable?»', cta2='Herramientas gratuitas', title="Cambios en buscadores y motores de IA en 2026 | CitedBy", desc="Cambios fechados de Google, Bing y Lighthouse que afectan a cómo se encuentran y se citan los sitios, leídos en la página del motor, con qué hacer.",
  h1="Qué cambió en los buscadores y motores de IA, y qué comprueba CitedBy", lead="Cada entrada es un cambio que publicó el propio motor, con su fecha, una cita exacta y un enlace. Debajo: qué puedes hacer como dueño del sitio y si CitedBy lo comprueba o no. Lo más reciente primero.",
  more="Solo listamos un cambio después de leerlo en la página del propio motor. Las noticias de la prensa del sector y los estudios de proveedores no son entradas. Las filas que no pudimos confirmar en una página oficial se dejan fuera.", read="Leído el", quote="Cita (texto original)", do="Qué puedes hacer", checks="Qué comprueba CitedBy", src="Fuente",
  yes="Comprobado", part="Comprobado en parte", no="No comprobado", feed="Feed RSS de estos cambios", cta_h="Mira lo que ve un rastreador en tu sitio", cta_b="Rastreamos tu sitio hasta el límite de páginas de tu plan y te damos la corrección exacta de cada problema. Desde 9 €, garantía de devolución de 14 días.", cta="Auditar mi sitio", ln="Cambios de los motores", fr_note="La página de origen y la cita están en francés.", lang_note="Las entradas están escritas en cada idioma; la cita es el texto de la fuente."),
}

# id -> {lang: (title, action, checks-status, checks line)}
C = {
"bing-ai-performance-public-preview": {
 "en": ("Bing adds AI Performance to Webmaster Tools (public preview)", "Verify the site in Bing Webmaster Tools, open AI Performance and export citations, cited pages and grounding queries each month.", "N", "Not read. With a Bing Webmaster Tools API key CitedBy shows how many pages Bing holds, the sitemap's state and crawl errors; the AI Performance report is read in Bing Webmaster Tools itself."),
 "fr": ("Bing ajoute AI Performance aux Outils pour webmasters (préversion publique)", "Validez le site dans Bing Webmaster Tools, ouvrez AI Performance et exportez chaque mois les citations, les pages citées et les requêtes d'ancrage.", "N", "Non lu. Avec une clé d'API Bing Webmaster Tools, CitedBy montre combien de pages Bing détient, l'état du sitemap et les erreurs d'exploration ; le rapport AI Performance se lit dans Bing Webmaster Tools lui-même."),
 "nl": ("Bing voegt AI Performance toe aan Webmaster Tools (openbare preview)", "Verifieer de site in Bing Webmaster Tools, open AI Performance en exporteer elke maand citaten, geciteerde pagina's en grounding-zoekopdrachten.", "N", "Niet gelezen. Met een API-sleutel van Bing Webmaster Tools toont CitedBy hoeveel pagina's Bing heeft, de status van de sitemap en crawlfouten; het rapport AI Performance lees je in Bing Webmaster Tools zelf."),
 "de": ("Bing ergänzt die Webmaster Tools um AI Performance (öffentliche Vorschau)", "Bestätigen Sie die Website in den Bing Webmaster Tools, öffnen Sie AI Performance und exportieren Sie jeden Monat Zitate, zitierte Seiten und Grounding-Abfragen.", "N", "Nicht gelesen. Mit einem API-Schlüssel der Bing Webmaster Tools zeigt CitedBy, wie viele Seiten Bing kennt, den Stand der Sitemap und Crawling-Fehler; den Bericht AI Performance lesen Sie in den Bing Webmaster Tools selbst."),
 "es": ("Bing añade AI Performance a las Herramientas para webmasters (vista previa pública)", "Verifica el sitio en Bing Webmaster Tools, abre AI Performance y exporta cada mes las citas, las páginas citadas y las consultas de grounding.", "N", "No se lee. Con una clave de API de Bing Webmaster Tools, CitedBy muestra cuántas páginas tiene Bing, el estado del sitemap y los errores de rastreo; el informe AI Performance se lee en el propio Bing Webmaster Tools.")},
"gsc-branded-queries-all-eligible": {
 "en": ("Search Console's branded queries filter reaches all eligible sites", "In the Search Console Performance report, apply the branded and non-branded filter and read the two groups separately.", "N", "Not checked. It changes how you read Search Console, not how your pages are built."),
 "fr": ("Le filtre des requêtes de marque de Search Console arrive sur tous les sites éligibles", "Dans le rapport Performances de Search Console, appliquez le filtre requêtes de marque et hors marque et lisez les deux groupes séparément.", "N", "Non vérifié. Cela change la façon de lire Search Console, pas la façon dont vos pages sont construites."),
 "nl": ("Het filter voor merkzoekopdrachten van Search Console is nu beschikbaar voor alle sites die in aanmerking komen", "Pas in het prestatierapport van Search Console het filter voor merk- en niet-merkzoekopdrachten toe en lees de twee groepen apart.", "N", "Niet gecontroleerd. Het verandert hoe je Search Console leest, niet hoe je pagina's zijn gebouwd."),
 "de": ("Der Filter für Markenanfragen in der Search Console steht allen berechtigten Websites zur Verfügung", "Wenden Sie im Leistungsbericht der Search Console den Filter für Marken- und Nicht-Marken-Suchanfragen an und lesen Sie die beiden Gruppen getrennt.", "N", "Nicht geprüft. Es ändert, wie Sie die Search Console lesen, nicht, wie Ihre Seiten gebaut sind."),
 "es": ("El filtro de consultas de marca de Search Console llega a todos los sitios elegibles", "En el informe de rendimiento de Search Console, aplica el filtro de consultas de marca y sin marca y lee los dos grupos por separado.", "N", "No se comprueba. Cambia cómo lees Search Console, no cómo están construidas tus páginas.")},
"lighthouse-agentic-browsing-category": {
 "en": ("Lighthouse adds an agentic browsing category with an llms.txt audit", "Make /llms.txt answer 200 or 404, never a server error: Lighthouse flags server errors on it and marks a 404 Not Applicable.", "P", "Partly. Every crawl requests /llms.txt: 200 counts as present, 404 or 410 as missing (an optional notice). CitedBy does not flag a server error on it as an issue."),
 "fr": ("Lighthouse ajoute une catégorie de navigation agentique avec un audit llms.txt", "Faites répondre /llms.txt par un 200 ou un 404, jamais par une erreur serveur : Lighthouse signale les erreurs serveur et classe un 404 comme Non applicable.", "P", "En partie. Chaque exploration demande /llms.txt : un 200 compte comme présent, un 404 ou 410 comme absent (avis facultatif). CitedBy ne signale pas une erreur serveur sur ce fichier comme un problème."),
 "nl": ("Lighthouse voegt een categorie voor agentisch browsen toe, met een llms.txt-audit", "Laat /llms.txt met 200 of 404 antwoorden, nooit met een serverfout: Lighthouse markeert serverfouten en zet een 404 op Niet van toepassing.", "P", "Gedeeltelijk. Elke crawl vraagt /llms.txt op: 200 telt als aanwezig, 404 of 410 als ontbrekend (een optionele melding). CitedBy meldt een serverfout op dit bestand niet als probleem."),
 "de": ("Lighthouse ergänzt eine Kategorie für agentisches Browsen mit einem llms.txt-Audit", "Lassen Sie /llms.txt mit 200 oder 404 antworten, nie mit einem Serverfehler: Lighthouse markiert Serverfehler und stuft ein 404 als Nicht zutreffend ein.", "P", "Teilweise. Jeder Crawl ruft /llms.txt ab: 200 gilt als vorhanden, 404 oder 410 als fehlend (ein optionaler Hinweis). Einen Serverfehler auf dieser Datei meldet CitedBy nicht als Problem."),
 "es": ("Lighthouse añade una categoría de navegación agéntica con una auditoría de llms.txt", "Haz que /llms.txt responda 200 o 404, nunca con un error de servidor: Lighthouse marca los errores de servidor y trata un 404 como No aplicable.", "P", "En parte. Cada rastreo pide /llms.txt: un 200 cuenta como presente, un 404 o 410 como ausente (un aviso opcional). CitedBy no marca como problema un error de servidor en ese archivo.")},
"ga4-ai-assistant-channel": {
 "en": ("Google Analytics adds a channel for AI assistant traffic", "Open the Default Channel Group in GA4 reports, check that the AI Assistant channel shows, and add a custom rule only for AI referrers that still land in Referral.", "N", "Not checked. CitedBy reads your pages, not your analytics."),
 "fr": ("Google Analytics ajoute un canal pour le trafic des assistants IA", "Ouvrez le groupe de canaux par défaut dans les rapports GA4, vérifiez que le canal Assistant IA apparaît, et n'ajoutez une règle personnalisée que pour les sources IA qui atterrissent encore dans Référence.", "N", "Non vérifié. CitedBy lit vos pages, pas vos statistiques."),
 "nl": ("Google Analytics voegt een kanaal toe voor verkeer van AI-assistenten", "Open in GA4 de standaardkanaalgroep, controleer of het kanaal AI-assistent verschijnt en voeg alleen een eigen regel toe voor AI-verwijzers die nog onder Verwijzing vallen.", "N", "Niet gecontroleerd. CitedBy leest je pagina's, niet je analytics."),
 "de": ("Google Analytics ergänzt einen Kanal für Traffic von KI-Assistenten", "Öffnen Sie in GA4 die Standard-Kanalgruppe, prüfen Sie, ob der Kanal KI-Assistent erscheint, und ergänzen Sie eine eigene Regel nur für KI-Verweise, die noch unter Verweis landen.", "N", "Nicht geprüft. CitedBy liest Ihre Seiten, nicht Ihre Analytics-Daten."),
 "es": ("Google Analytics añade un canal para el tráfico de asistentes de IA", "Abre el grupo de canales predeterminado en los informes de GA4, comprueba que aparece el canal Asistente de IA y añade una regla propia solo para las referencias de IA que aún caen en Referral.", "N", "No se comprueba. CitedBy lee tus páginas, no tu analítica.")},
"gsc-generative-ai-reports-launch": {
 "en": ("Search Console launches Generative AI performance reports", "Open the Generative AI performance report in Search Console and read AI impressions by page, country and device.", "N", "Not read. The Search Console connection checks which pages Google has indexed; the Generative AI report is read in Search Console itself."),
 "fr": ("Search Console lance les rapports de performance de l'IA générative", "Ouvrez le rapport de performance de l'IA générative dans Search Console et lisez les impressions IA par page, pays et appareil.", "N", "Non lu. La connexion Search Console vérifie quelles pages Google a indexées ; le rapport d'IA générative se lit dans Search Console lui-même."),
 "nl": ("Search Console lanceert prestatierapporten voor generatieve AI", "Open het prestatierapport voor generatieve AI in Search Console en lees AI-vertoningen per pagina, land en apparaat.", "N", "Niet gelezen. De Search Console-koppeling controleert welke pagina's Google heeft geïndexeerd; het rapport voor generatieve AI lees je in Search Console zelf."),
 "de": ("Die Search Console startet Leistungsberichte für generative KI", "Öffnen Sie in der Search Console den Leistungsbericht für generative KI und lesen Sie die KI-Impressionen nach Seite, Land und Gerät.", "N", "Nicht gelesen. Die Search-Console-Verbindung prüft, welche Seiten Google indexiert hat; den Bericht zu generativer KI lesen Sie in der Search Console selbst."),
 "es": ("Search Console lanza informes de rendimiento de IA generativa", "Abre el informe de rendimiento de IA generativa en Search Console y lee las impresiones de IA por página, país y dispositivo.", "N", "No se lee. La conexión con Search Console comprueba qué páginas ha indexado Google; el informe de IA generativa se lee en la propia Search Console.")},
"gsc-generative-ai-reports-worldwide": {
 "en": ("Generative AI performance reports roll out to all sites worldwide", "Check the Generative AI performance report is now visible for every property, in every country you serve.", "N", "Not read. Same as the launch entry: CitedBy does not read this report."),
 "fr": ("Les rapports de performance de l'IA générative arrivent sur tous les sites dans le monde", "Vérifiez que le rapport de performance de l'IA générative est maintenant visible pour chaque propriété, dans chaque pays où vous êtes présent.", "N", "Non lu. Comme pour l'entrée du lancement : CitedBy ne lit pas ce rapport."),
 "nl": ("Prestatierapporten voor generatieve AI zijn nu wereldwijd beschikbaar voor alle sites", "Controleer of het prestatierapport voor generatieve AI nu zichtbaar is voor elke property, in elk land waar je actief bent.", "N", "Niet gelezen. Net als bij het item over de lancering: CitedBy leest dit rapport niet."),
 "de": ("Leistungsberichte für generative KI stehen weltweit allen Websites zur Verfügung", "Prüfen Sie, ob der Leistungsbericht für generative KI jetzt für jede Property sichtbar ist, in jedem Land, in dem Sie aktiv sind.", "N", "Nicht gelesen. Wie beim Eintrag zum Start: CitedBy liest diesen Bericht nicht."),
 "es": ("Los informes de rendimiento de IA generativa llegan a todos los sitios del mundo", "Comprueba que el informe de rendimiento de IA generativa ya es visible en cada propiedad, en cada país donde operas.", "N", "No se lee. Igual que la entrada del lanzamiento: CitedBy no lee este informe.")},
"gsc-search-generative-ai-control-worldwide": {
 "en": ("The Search generative AI control rolls out to all sites worldwide", "Open Settings > Search generative AI in Search Console and confirm each property is set to include the site, unless the owner chose otherwise.", "N", "Not checked. The setting lives in Search Console and CitedBy cannot see it."),
 "fr": ("Le contrôle de l'IA générative dans la recherche arrive sur tous les sites dans le monde", "Ouvrez Paramètres > IA générative dans la recherche dans Search Console et vérifiez que chaque propriété inclut le site, sauf choix contraire du propriétaire.", "N", "Non vérifié. Ce réglage se trouve dans Search Console et CitedBy ne peut pas le voir."),
 "nl": ("De instelling voor generatieve AI in Zoeken is nu wereldwijd beschikbaar voor alle sites", "Open Instellingen > Generatieve AI in Zoeken in Search Console en controleer of elke property de site opneemt, tenzij de eigenaar anders koos.", "N", "Niet gecontroleerd. Deze instelling staat in Search Console en CitedBy kan haar niet zien."),
 "de": ("Die Steuerung für generative KI in der Suche steht weltweit allen Websites zur Verfügung", "Öffnen Sie in der Search Console Einstellungen > Generative KI in der Suche und prüfen Sie, dass jede Property die Website einbezieht, sofern Sie nichts anderes gewählt haben.", "N", "Nicht geprüft. Die Einstellung liegt in der Search Console und CitedBy kann sie nicht sehen."),
 "es": ("El control de IA generativa en Búsqueda llega a todos los sitios del mundo", "Abre Ajustes > IA generativa en Búsqueda en Search Console y confirma que cada propiedad incluye el sitio, salvo que el propietario haya elegido otra cosa.", "N", "No se comprueba. El ajuste está en Search Console y CitedBy no puede verlo.")},
"google-ai-overviews-ai-mode-france": {
 "en": ("Google launches AI Overviews and AI Mode in France", "Read the French AI impressions in the Generative AI performance report and check which French questions now show an AI Overview.", "N", "Not checked. CitedBy does not measure whether a question shows an AI Overview."),
 "fr": ("Google lance les Aperçus IA et le Mode IA en France", "Lisez les impressions IA françaises dans le rapport de performance de l'IA générative et vérifiez quelles questions en français affichent maintenant un Aperçu IA.", "N", "Non vérifié. CitedBy ne mesure pas si une question affiche un Aperçu IA."),
 "nl": ("Google lanceert AI Overviews en AI Mode in Frankrijk", "Lees de Franse AI-vertoningen in het prestatierapport voor generatieve AI en kijk bij welke Franse vragen nu een AI Overview staat.", "N", "Niet gecontroleerd. CitedBy meet niet of een vraag een AI Overview toont."),
 "de": ("Google startet AI Overviews und AI Mode in Frankreich", "Lesen Sie die französischen KI-Impressionen im Leistungsbericht für generative KI und prüfen Sie, bei welchen französischen Fragen jetzt eine AI Overview erscheint.", "N", "Nicht geprüft. CitedBy misst nicht, ob eine Frage eine AI Overview zeigt."),
 "es": ("Google lanza AI Overviews y AI Mode en Francia", "Lee las impresiones de IA en francés en el informe de rendimiento de IA generativa y comprueba qué preguntas en francés muestran ya un AI Overview.", "N", "No se comprueba. CitedBy no mide si una pregunta muestra un AI Overview.")},
"google-llms-txt-guidance": {
 "en": ("Google says llms.txt is not needed for Search", "Keep llms.txt optional: publish it for other tools if wanted, but do not expect Google Search visibility from it.", "Y", "Checked. A missing llms.txt shows as an optional notice, never an error, because no major assistant is confirmed to read it."),
 "fr": ("Google précise que llms.txt n'est pas nécessaire pour la Recherche", "Gardez llms.txt facultatif : publiez-le pour d'autres outils si vous le souhaitez, mais n'en attendez pas de visibilité dans la Recherche Google.", "Y", "Vérifié. Un llms.txt absent apparaît comme un avis facultatif, jamais comme une erreur, car il n'est pas confirmé qu'un grand assistant le lise."),
 "nl": ("Google zegt dat llms.txt niet nodig is voor Zoeken", "Houd llms.txt optioneel: publiceer het voor andere tools als je wilt, maar verwacht er geen zichtbaarheid in Google Zoeken van.", "Y", "Gecontroleerd. Een ontbrekend llms.txt verschijnt als optionele melding, nooit als fout, omdat van geen enkele grote assistent bevestigd is dat hij het leest."),
 "de": ("Google erklärt, dass llms.txt für die Suche nicht nötig ist", "Lassen Sie llms.txt optional: Veröffentlichen Sie sie für andere Tools, wenn Sie möchten, erwarten Sie davon aber keine Sichtbarkeit in der Google-Suche.", "Y", "Geprüft. Eine fehlende llms.txt erscheint als optionaler Hinweis, nie als Fehler, weil bei keinem großen Assistenten bestätigt ist, dass er sie liest."),
 "es": ("Google aclara que llms.txt no hace falta para la Búsqueda", "Mantén llms.txt como algo opcional: publícalo para otras herramientas si quieres, pero no esperes visibilidad en Google Search por ello.", "Y", "Comprobado. Un llms.txt ausente aparece como aviso opcional, nunca como error, porque no se ha confirmado que ningún gran asistente lo lea.")},
"bing-topics-portfolio-beta": {
 "en": ("Bing adds Topics Portfolio (beta) to AI Performance", "In Bing Webmaster Tools open AI Performance > Topics Portfolio and read Top Opportunity Queries: topics where other sites are cited and yours is not.", "N", "Not read. CitedBy does not read the AI Performance report; you read it in Bing Webmaster Tools itself."),
 "fr": ("Bing ajoute Topics Portfolio (bêta) à AI Performance", "Dans Bing Webmaster Tools, ouvrez AI Performance > Topics Portfolio et lisez Top Opportunity Queries : les sujets où d'autres sites sont cités et pas le vôtre.", "N", "Non lu. CitedBy ne lit pas le rapport AI Performance ; il se lit dans Bing Webmaster Tools lui-même."),
 "nl": ("Bing voegt Topics Portfolio (bèta) toe aan AI Performance", "Open in Bing Webmaster Tools AI Performance > Topics Portfolio en lees Top Opportunity Queries: onderwerpen waarbij andere sites worden geciteerd en de jouwe niet.", "N", "Niet gelezen. CitedBy leest het rapport AI Performance niet; je leest het in Bing Webmaster Tools zelf."),
 "de": ("Bing ergänzt AI Performance um Topics Portfolio (Beta)", "Öffnen Sie in den Bing Webmaster Tools AI Performance > Topics Portfolio und lesen Sie Top Opportunity Queries: Themen, bei denen andere Websites zitiert werden und Ihre nicht.", "N", "Nicht gelesen. CitedBy liest den Bericht AI Performance nicht; Sie lesen ihn in den Bing Webmaster Tools selbst."),
 "es": ("Bing añade Topics Portfolio (beta) a AI Performance", "En Bing Webmaster Tools abre AI Performance > Topics Portfolio y lee Top Opportunity Queries: temas en los que se cita a otros sitios y no al tuyo.", "N", "No se lee. CitedBy no lee el informe AI Performance; lo lees en la propia Bing Webmaster Tools.")},
"gsc-web-multimodal-reporting": {
 "en": ("Search Console reports web multimodal search", "In the Search Console performance reports, use the new multimodal search type filter to see visits that began with an image search (Lens, Circle to Search) and export them.", "N", "Not read. The Search Console connection checks which pages Google has indexed; the performance reports are read in Search Console itself."),
 "fr": ("Search Console rapporte la recherche multimodale sur le web", "Dans les rapports de performances de Search Console, utilisez le nouveau filtre de type de recherche multimodale pour voir les visites parties d'une recherche par image (Lens, Circle to Search) et exportez-les.", "N", "Non lu. La connexion Search Console vérifie quelles pages Google a indexées ; les rapports de performances se lisent dans Search Console lui-même."),
 "nl": ("Search Console rapporteert multimodaal zoeken op het web", "Gebruik in de prestatierapporten van Search Console het nieuwe filter voor multimodaal zoeken om bezoeken te zien die met een beeldzoekopdracht begonnen (Lens, Circle to Search) en exporteer ze.", "N", "Niet gelezen. De Search Console-koppeling controleert welke pagina's Google heeft geïndexeerd; de prestatierapporten lees je in Search Console zelf."),
 "de": ("Die Search Console berichtet über multimodale Websuche", "Nutzen Sie in den Leistungsberichten der Search Console den neuen Filter für multimodale Suche, um Besuche zu sehen, die mit einer Bildsuche begannen (Lens, Circle to Search), und exportieren Sie sie.", "N", "Nicht gelesen. Die Search-Console-Verbindung prüft, welche Seiten Google indexiert hat; die Leistungsberichte lesen Sie in der Search Console selbst."),
 "es": ("Search Console informa de la búsqueda multimodal en la web", "En los informes de rendimiento de Search Console usa el nuevo filtro de búsqueda multimodal para ver las visitas que empezaron con una búsqueda por imagen (Lens, Circle to Search) y expórtalas.", "N", "No se lee. La conexión con Search Console comprueba qué páginas ha indexado Google; los informes de rendimiento se leen en la propia Search Console.")},
"google-preferred-sources-ai-mode": {
 "en": ("Google brings preferred sources to AI Overviews and AI Mode", "If the site publishes articles or news, check it in Google's source preferences tool and add the preferred-source button; the site must be included in Search generative AI features.", "N", "Not checked. The setting and the button are on Google's side, and a crawl cannot see whether readers chose your site."),
 "fr": ("Google étend les sources préférées aux Aperçus IA et au Mode IA", "Si le site publie des articles ou des actualités, vérifiez-le dans l'outil de préférences de sources de Google et ajoutez le bouton de source préférée ; le site doit être inclus dans les fonctionnalités d'IA générative de la Recherche.", "N", "Non vérifié. Le réglage et le bouton se trouvent côté Google, et une exploration ne peut pas voir si des lecteurs ont choisi votre site."),
 "nl": ("Google brengt voorkeursbronnen naar AI Overviews en AI Mode", "Publiceert de site artikelen of nieuws, controleer hem dan in de tool voor bronvoorkeuren van Google en voeg de knop voor voorkeursbronnen toe; de site moet zijn opgenomen in de generatieve AI-functies van Zoeken.", "N", "Niet gecontroleerd. De instelling en de knop staan aan de kant van Google, en een crawl kan niet zien of lezers jouw site hebben gekozen."),
 "de": ("Google bringt bevorzugte Quellen in AI Overviews und AI Mode", "Wenn die Website Artikel oder Nachrichten veröffentlicht, prüfen Sie sie im Tool für Quellenpräferenzen von Google und fügen Sie die Schaltfläche für bevorzugte Quellen hinzu; die Website muss in den generativen KI-Funktionen der Suche enthalten sein.", "N", "Nicht geprüft. Einstellung und Schaltfläche liegen auf Seiten von Google, und ein Crawl kann nicht sehen, ob Leser Ihre Website gewählt haben."),
 "es": ("Google lleva las fuentes preferidas a AI Overviews y AI Mode", "Si el sitio publica artículos o noticias, compruébalo en la herramienta de preferencias de fuentes de Google y añade el botón de fuente preferida; el sitio debe estar incluido en las funciones de IA generativa de la Búsqueda.", "N", "No se comprueba. El ajuste y el botón están del lado de Google, y un rastreo no puede ver si los lectores eligieron tu sitio.")},
"google-ai-optimization-guide": {
 "en": ("Google publishes a guide on optimizing for generative AI features", "Read Google's guide on optimizing for generative AI features, its \"AEO/GEO\" mythbusting section first, before paying for an AI-specific fix.", "N", "Not checked. It is guidance, not a rule a crawl can test."),
 "fr": ("Google publie un guide sur l'optimisation pour les fonctionnalités d'IA générative", "Lisez le guide de Google sur l'optimisation pour les fonctionnalités d'IA générative, en commençant par sa section de démystification « AEO/GEO », avant de payer pour une correction propre à l'IA.", "N", "Non vérifié. C'est un conseil, pas une règle qu'une exploration peut tester."),
 "nl": ("Google publiceert een gids over optimaliseren voor generatieve AI-functies", "Lees de gids van Google over optimaliseren voor generatieve AI-functies, eerst het deel waarin hij de mythes rond «AEO/GEO» ontkracht, voordat je betaalt voor een AI-specifieke oplossing.", "N", "Niet gecontroleerd. Het is advies, geen regel die een crawl kan testen."),
 "de": ("Google veröffentlicht einen Leitfaden zur Optimierung für generative KI-Funktionen", "Lesen Sie Googles Leitfaden zur Optimierung für generative KI-Funktionen, zuerst den Abschnitt, der die „AEO/GEO“-Mythen aufklärt, bevor Sie für eine KI-spezifische Korrektur zahlen.", "N", "Nicht geprüft. Es ist eine Empfehlung, keine Regel, die ein Crawl testen kann."),
 "es": ("Google publica una guía para optimizar las funciones de IA generativa", "Lee la guía de Google sobre cómo optimizar para las funciones de IA generativa, primero su sección que desmonta los mitos de «AEO/GEO», antes de pagar por una corrección específica para IA.", "N", "No se comprueba. Es una recomendación, no una regla que un rastreo pueda probar.")},
"google-spam-policies-cover-ai-responses": {
 "en": ("Google says its spam policies also cover generative AI responses", "Do not publish mass-produced or deceptive pages meant to win AI citations: Google's spam policies now say they cover AI responses too.", "N", "Not checked. CitedBy does not test pages against Google's spam policies."),
 "fr": ("Google précise que ses règles anti-spam couvrent aussi les réponses d'IA générative", "Ne publiez pas de pages produites en masse ou trompeuses destinées à obtenir des citations d'IA : les règles anti-spam de Google disent désormais qu'elles couvrent aussi les réponses d'IA.", "N", "Non vérifié. CitedBy ne teste pas les pages au regard des règles anti-spam de Google."),
 "nl": ("Google zegt dat zijn spambeleid ook geldt voor generatieve AI-antwoorden", "Publiceer geen massaal geproduceerde of misleidende pagina's om AI-citaten te winnen: het spambeleid van Google zegt nu dat het ook voor AI-antwoorden geldt.", "N", "Niet gecontroleerd. CitedBy toetst pagina's niet aan het spambeleid van Google."),
 "de": ("Google erklärt, dass seine Spam-Richtlinien auch für generative KI-Antworten gelten", "Veröffentlichen Sie keine massenhaft erzeugten oder täuschenden Seiten, um KI-Zitate zu gewinnen: Googles Spam-Richtlinien gelten laut Google jetzt auch für KI-Antworten.", "N", "Nicht geprüft. CitedBy prüft Seiten nicht gegen Googles Spam-Richtlinien."),
 "es": ("Google aclara que sus políticas de spam también cubren las respuestas de IA generativa", "No publiques páginas producidas en masa o engañosas para conseguir citas de IA: las políticas de spam de Google dicen ahora que también cubren las respuestas de IA.", "N", "No se comprueba. CitedBy no prueba las páginas frente a las políticas de spam de Google.")},
"google-faq-rich-result-ended": {
 "en": ("Google ends the FAQ rich result in Search", "Stop treating FAQPage markup as a way to win an FAQ rich result in Google Search; the result no longer appears.", "P", "Partly. CitedBy still lists question pages without FAQPage markup as a notice and flags FAQPage markup that lacks answers. Neither promises a Google FAQ rich result."),
 "fr": ("Google met fin au résultat enrichi FAQ dans la Recherche", "Ne comptez plus sur le balisage FAQPage pour obtenir un résultat enrichi FAQ dans la Recherche Google ; ce résultat n'apparaît plus.", "P", "En partie. CitedBy signale encore, en simple avis, les pages de questions sans balisage FAQPage et repère un balisage FAQPage sans réponses. Aucun des deux ne promet un résultat enrichi FAQ dans Google."),
 "nl": ("Google stopt met het FAQ-rich result in Zoeken", "Reken niet meer op FAQPage-markup om een FAQ-rich result in Google Zoeken te winnen; dat resultaat verschijnt niet meer.", "P", "Gedeeltelijk. CitedBy meldt vraagpagina's zonder FAQPage-markup nog als melding en markeert FAQPage-markup zonder antwoorden. Geen van beide belooft een FAQ-rich result in Google."),
 "de": ("Google beendet das FAQ-Rich-Result in der Suche", "Betrachten Sie FAQPage-Markup nicht mehr als Weg zu einem FAQ-Rich-Result in der Google-Suche; das Ergebnis erscheint nicht mehr.", "P", "Teilweise. CitedBy führt Fragenseiten ohne FAQPage-Markup weiterhin als Hinweis auf und markiert FAQPage-Markup ohne Antworten. Beides verspricht kein FAQ-Rich-Result in Google."),
 "es": ("Google retira el resultado enriquecido de preguntas frecuentes en la Búsqueda", "Deja de ver el marcado FAQPage como una vía para conseguir un resultado enriquecido de preguntas frecuentes en Google Search; el resultado ya no aparece.", "P", "En parte. CitedBy sigue listando como aviso las páginas de preguntas sin marcado FAQPage y señala el marcado FAQPage sin respuestas. Ninguno de los dos promete un resultado enriquecido de preguntas frecuentes en Google.")},
"googlebot-2mb-fetch-limit": {
 "en": ("Google documents a 2 MB fetch limit per URL for Googlebot", "Keep each page's HTML under 2MB and put the title, canonical and key structured data near the top; move heavy inline CSS and JavaScript to external files.", "Y", "Checked. CitedBy flags HTML over 1 MB as a warning, well below Google's limit. It measures the HTML of each crawled page, for every crawler, not only Googlebot."),
 "fr": ("Google documente une limite de 2 Mo par URL pour Googlebot", "Gardez le HTML de chaque page sous 2 Mo et placez le titre, le canonique et les données structurées clés en haut ; déplacez le CSS et le JavaScript lourds en ligne vers des fichiers externes.", "Y", "Vérifié. CitedBy signale en avertissement un HTML de plus de 1 Mo, bien en dessous de la limite de Google. Il mesure le HTML de chaque page explorée, pour tous les robots, pas seulement Googlebot."),
 "nl": ("Google documenteert een ophaallimiet van 2 MB per URL voor Googlebot", "Houd de HTML van elke pagina onder 2 MB en zet de titel, de canonical en de belangrijkste gestructureerde data bovenaan; verplaats zware inline CSS en JavaScript naar externe bestanden.", "Y", "Gecontroleerd. CitedBy geeft een waarschuwing bij HTML boven 1 MB, ruim onder de limiet van Google. Het meet de HTML van elke gecrawlde pagina, voor elke crawler, niet alleen Googlebot."),
 "de": ("Google dokumentiert ein Abruflimit von 2 MB pro URL für Googlebot", "Halten Sie das HTML jeder Seite unter 2 MB und setzen Sie Titel, Canonical und wichtige strukturierte Daten nach oben; verlagern Sie umfangreiches Inline-CSS und JavaScript in externe Dateien.", "Y", "Geprüft. CitedBy warnt bei HTML über 1 MB, weit unter Googles Limit. Es misst das HTML jeder gecrawlten Seite, für jeden Crawler, nicht nur für Googlebot."),
 "es": ("Google documenta un límite de 2 MB por URL para Googlebot", "Mantén el HTML de cada página por debajo de 2 MB y pon el título, el canonical y los datos estructurados clave al principio; traslada el CSS y el JavaScript pesados en línea a archivos externos.", "Y", "Comprobado. CitedBy avisa cuando el HTML supera 1 MB, muy por debajo del límite de Google. Mide el HTML de cada página rastreada, para cualquier rastreador, no solo Googlebot.")},
}


CSS = (".dc article{margin:0 0 28px;padding-top:24px;border-top:1px solid #DCE3EC}.dc article h2{margin:0 0 6px}.dc article blockquote{margin:12px 0 4px;padding:8px 14px;border-left:3px solid #9FB0C7;color:#26364D;overflow-wrap:anywhere}"
       ".dc .chip{display:inline-block;padding:2px 9px;border-radius:999px;font-size:13px;font-weight:600;background:#EEF2F7;color:#26364D}.dc .chip.ok{background:#DDF3E4;color:#14532D}.dc .chip.part{background:#FDF0D0;color:#6B4A00}"
       ".dc article p{overflow-wrap:anywhere}.dc a.free{font-weight:600;white-space:normal}"
       ".dc .sum{margin:20px 0 8px;padding:16px 18px;border:1px solid #DCE3EC;border-radius:12px;background:#F7F9FC}.dc .sum h2{margin:0 0 10px;font-size:20px}.dc .sum ul{list-style:none;margin:0;padding:0}"
       ".dc .sum li{display:flex;flex-wrap:wrap;align-items:center;gap:4px 10px;padding:8px 0;border-top:1px solid #E5EAF1}.dc .sum li:first-child{border-top:0}.dc .sum li a{display:flex;flex:1 1 260px;gap:10px;text-decoration:none;color:#14213A}"
       ".dc .sum li a:hover .t{text-decoration:underline}.dc .sum time{flex:0 0 92px;color:#51607A;font-size:14px;font-variant-numeric:tabular-nums}.dc .sum .t{font-weight:600}.dc .sum .src{margin:10px 0 0}")


def path(l, ext=""): return ("/changes" if l == "en" else "/%s/changes" % l) + ext
def fr_typo(s):
    s = re.sub(r" ([:;!?»])", " \\1", s)
    return s.replace("« ", "« ")
def day(l, iso):
    y, m, d = (int(x) for x in iso.split("-")); mo = MONTHS[l].split()[m - 1]
    return "%d %s %d" % (d, mo, y) if l != "de" else "%d. %s %d" % (d, mo, y)
def free(l, rid):
    if rid not in FREE: return ""
    t, k = FREE[rid]
    return ' <a class="free" href="%s">%s</a>' % (tp(l, "/" + t), E(fr_typo(UI[l][k]) if l == "fr" else UI[l][k]))
def summary(l):
    u = UI[l]; tx = (lambda s: fr_typo(s)) if l == "fr" else (lambda s: s)
    cls = {"Y": ("ok", u["yes"]), "P": ("part", u["part"]), "N": ("no", u["no"])}
    rows = "".join('<li><a href="#%s"><time datetime="%s">%s</time><span class="t">%s</span></a><span class="chip %s">%s</span></li>' % (
        r["id"], r["date"], E(day(l, r["date"])), E(tx(C[r["id"]][l][0])), cls[C[r["id"]][l][2]][0], E(cls[C[r["id"]][l][2]][1])) for r in ordered())
    return '<section class="sum" aria-labelledby="sum-h"><h2 id="sum-h">%s</h2><ul>%s</ul><p class="src">%s</p></section>' % (E(tx(u["sum_h"])), rows, E(tx(u["legend"])))
def ordered(): return sorted(REC, key=lambda r: (r["date"], r["id"]), reverse=True)


def render(l):
    u = UI[l]; tx = (lambda s: fr_typo(s)) if l == "fr" else (lambda s: s)
    base = open(os.path.join(PUB, "about.html" if l == "en" else "%s/about.html" % l), encoding="utf-8").read()
    head = base[:base.index("<main")]; foot = base[base.index("</main>") + len("</main>"):]
    alts = "".join('<link rel="alternate" hreflang="%s" href="%s%s">' % (x, SITE, path(x)) for x in LANGS) + '<link rel="alternate" hreflang="x-default" href="%s/changes">' % SITE
    feed = '<link rel="alternate" type="application/rss+xml" title="%s" href="%s">' % (E(tx(u["feed"])), path(l, ".xml"))
    head = re.sub(r"<title>[^<]*</title>", "<title>%s</title>" % E(tx(u["title"])), head, 1)
    head = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % E(tx(u["desc"])), head, 1)
    head = re.sub(r'<link rel="canonical" href="[^"]*">(<link rel="alternate" hreflang[^>]*>)*', '<link rel="canonical" href="%s%s">%s%s' % (SITE, path(l), alts, feed), head, 1)
    items = []
    for r in ordered():
        ttl, act, st, chk = C[r["id"]][l]
        items.append({"@type": "ListItem", "position": len(items) + 1, "item": {"@type": "Article", "headline": ttl, "datePublished": r["date"], "inLanguage": l, "url": "%s%s#%s" % (SITE, path(l), r["id"]),
                      "isBasedOn": r["source_url"], "author": {"@type": "Organization", "name": "CitedBy"}, "publisher": {"@type": "Organization", "name": "CitedBy", "url": SITE}}})
    ld = {"@context": "https://schema.org", "@graph": [{"@type": "CollectionPage", "@id": "%s%s#page" % (SITE, path(l)), "url": SITE + path(l), "name": u["h1"], "inLanguage": l, "dateModified": BUILT,
          "isPartOf": {"@type": "WebSite", "name": "CitedBy", "url": SITE}, "mainEntity": {"@type": "ItemList", "itemListElement": items}}]}
    head = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>", head, 1, flags=re.S)
    head = head.replace("</head>", "<style>" + CSS + "</style></head>", 1)
    cls = {"Y":("ok", u["yes"]), "P": ("part", u["part"]), "N": ("no", u["no"])}
    art = []
    for r in ordered():
        ttl, act, st, chk = C[r["id"]][l]
        c, lab = cls[st]; eng = " · ".join(E(ENG_L.get(l, {}).get(e, ENG[e])) for e in r["engines"]); sn = r["source_name"].replace("note added to the 3 June post", NOTE[l])
        qn = ' <span class="src">(%s)</span>' % E(u["fr_note"]) if r["id"] == "google-ai-overviews-ai-mode-france" and l != "fr" else ""
        art.append('<article id="%s"><h2>%s</h2><p class="src"><time datetime="%s">%s</time> · %s · %s <a href="%s">%s</a> · %s %s</p>'
                   '<blockquote lang="%s">“%s”</blockquote><p class="src">%s%s</p>'
                   '<p><b>%s.</b> %s</p><p><b>%s%s <span class="chip %s">%s</span></b> %s%s</p></article>' % (
            r["id"], E(tx(ttl)), r["date"], E(day(l, r["date"])), eng, E(tx(u["src"])), E(r["source_url"]), E(sn), E(tx(u["read"])), E(day(l, r["read_on"])),
            "fr" if r["id"] == "google-ai-overviews-ai-mode-france" else "en", E(r["quote"]), E(tx(u["quote"])), qn, E(tx(u["do"])), E(tx(act)), E(tx(u["checks"])), "\u202f:" if l == "fr" else ":", c, E(lab), E(tx(chk)), free(l, r["id"])))
    main = '<main id="main"><h1>%s</h1><p class="lead">%s</p><p class="src">%s <a href="%s">%s</a></p>\n%s\n%s\n<section class="cta"><h2>%s</h2><p class="lede">%s</p><div class="actions"><a class="btn p" href="%s">%s</a><a class="btn" href="%s">%s</a></div></section></main>' % (
        E(tx(u["h1"])), E(tx(u["lead"])), E(tx(u["more"])), path(l, ".xml"), E(tx(u["feed"])), summary(l), "\n".join(art), E(tx(u["cta_h"])), E(tx(u["cta_b"])), "/" if l == "en" else "/%s/" % l, E(tx(u["cta"])), tp(l), E(tx(u["cta2"])))
    return head + main + foot


def rss(l):
    u = UI[l]; tx = (lambda s: fr_typo(s)) if l == "fr" else (lambda s: s); out = []
    for r in ordered():
        ttl, act, st, chk = C[r["id"]][l]
        y, m, d = (int(x) for x in r["date"].split("-")); dt = datetime.date(y, m, d)
        pub = "%s, %02d %s %d 00:00:00 +0000" % (["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][dt.weekday()], d, RFC_MONTH[m - 1], y)
        body = "<p>%s</p><p>%s: %s</p><p>%s: %s</p>" % (E(tx(act)), E(tx(u["checks"])), E(tx(chk)), E(tx(u["src"])), E(r["source_url"]))
        out.append("<item><title>%s</title><link>%s%s#%s</link><guid isPermaLink=\"false\">citedby-change-%s-%s</guid><pubDate>%s</pubDate><description>%s</description></item>" % (E(tx(ttl)), SITE, path(l), r["id"], l, r["id"], pub, E(body)))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel><title>%s</title><link>%s%s</link><atom:link href="%s%s" rel="self" type="application/rss+xml"/>'
            "<description>%s</description><language>%s</language><lastBuildDate>%s</lastBuildDate>\n%s\n</channel></rss>\n") % (
        E(tx(u["ln"])) + " | CitedBy", SITE, path(l), SITE, path(l, ".xml"), E(tx(u["desc"])), l, "Thu, 22 Oct 2026 00:00:00 +0000", "\n".join(out))


def sitemap():
    sm = os.path.join(PUB, "sitemap.xml"); s = open(sm, encoding="utf-8").read()
    s = re.sub(r"<url><loc>%s(?:/[a-z]{2})?/changes</loc>.*?</url>" % re.escape(SITE), "", s)
    alt = "".join('<xhtml:link rel="alternate" hreflang="%s" href="%s%s"/>' % (x, SITE, path(x)) for x in LANGS) + '<xhtml:link rel="alternate" hreflang="x-default" href="%s/changes"/>' % SITE
    new = "".join("<url><loc>%s%s</loc><lastmod>%s</lastmod>%s</url>" % (SITE, path(l), BUILT, alt) for l in LANGS)
    return sm, s.replace("</urlset>", new + "</urlset>")


def llms():
    p = os.path.join(PUB, "llms.txt"); s = open(p, encoding="utf-8").read()
    line = "- [Engine changes](%s/changes): dated changes from Google, Bing and Lighthouse, each read on the engine's own page, and whether CitedBy checks them\n" % SITE
    s = re.sub(r"- \[Engine changes\]\(.*\n", "", s)
    k = "- [About CitedBy]"
    return p, s.replace(k, line + k, 1)


def main():
    check = "--check" in sys.argv
    out = {}
    for l in LANGS:
        out[os.path.join(PUB, path(l).lstrip("/") + ".html")] = render(l)
        out[os.path.join(PUB, path(l, ".xml").lstrip("/"))] = rss(l)
    for p, doc in (sitemap(), llms()): out[p] = doc
    for p, doc in out.items():
        if check:
            if not os.path.exists(p) or open(p, encoding="utf-8").read() != doc: sys.exit("stale: " + p)
        else:
            open(p, "w", encoding="utf-8").write(doc)
    print("ok" if check else "wrote %d files" % len(out))


if __name__ == "__main__":
    main()
