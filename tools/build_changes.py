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
RFC_MONTH = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()

UI = {
 "en": dict(title="What changed in search and AI engines in 2026, and what CitedBy checks | CitedBy", desc="Dated changes from Google, Bing and Lighthouse that affect how sites are found and cited, each read on the engine's own page, with what to do and whether CitedBy checks it.",
  h1="What changed in search and AI engines, and what CitedBy checks", lead="Each entry is a change an engine published itself, with its date, one exact quote and a link. Under it: what a site owner can do, and whether CitedBy checks it or not. Newest first.",
  more="We only list a change after reading it on the engine's own page. Trade-press reports and vendor studies are not entries. Rows we could not confirm on a primary page are left out.", read="Read on", quote="Quote (original wording)", do="What you can do", checks="What CitedBy checks", src="Source",
  yes="Checked", part="Partly checked", no="Not checked", feed="RSS feed of these changes", cta_h="See what a crawler sees on your site", cta_b="We crawl your site up to your plan's page limit and give you the exact fix for each issue. From €9, 14-day money-back guarantee.", cta="Audit my site", ln="Engine changes", fr_note="Source page and quote are in French.", lang_note="Entries are written in each language; the quote is the source's own wording."),
 "fr": dict(title="Ce qui a changé dans la recherche et les moteurs IA en 2026, et ce que CitedBy vérifie | CitedBy", desc="Changements datés de Google, Bing et Lighthouse qui touchent la façon dont les sites sont trouvés et cités, chacun lu sur la page du moteur, avec quoi faire et si CitedBy le vérifie.",
  h1="Ce qui a changé dans la recherche et les moteurs IA, et ce que CitedBy vérifie", lead="Chaque entrée est un changement publié par le moteur lui-même, avec sa date, une citation exacte et un lien. En dessous : ce que vous pouvez faire, et si CitedBy le vérifie ou non. Le plus récent en premier.",
  more="Nous ne listons un changement qu'après l'avoir lu sur la page du moteur. Les articles de presse spécialisée et les études d'éditeurs ne sont pas des entrées. Les lignes que nous n'avons pas pu confirmer sur une page officielle sont écartées.", read="Lu le", quote="Citation (texte d'origine)", do="Ce que vous pouvez faire", checks="Ce que CitedBy vérifie", src="Source",
  yes="Vérifié", part="Vérifié en partie", no="Non vérifié", feed="Flux RSS de ces changements", cta_h="Voyez ce que voit un robot sur votre site", cta_b="Nous explorons votre site jusqu'à la limite de pages de votre offre et donnons le correctif exact de chaque problème. Dès 9 €, garantie de remboursement de 14 jours.", cta="Auditer mon site", ln="Changements des moteurs", fr_note="La page source et la citation sont en français.", lang_note="Les entrées sont rédigées dans chaque langue ; la citation reprend les mots de la source."),
 "nl": dict(title="Wat er in 2026 veranderde bij zoek- en AI-engines, en wat CitedBy controleert | CitedBy", desc="Gedateerde wijzigingen van Google, Bing en Lighthouse die bepalen hoe sites worden gevonden en geciteerd, elk gelezen op de pagina van de engine zelf, met wat je kunt doen en of CitedBy het controleert.",
  h1="Wat er veranderde bij zoek- en AI-engines, en wat CitedBy controleert", lead="Elk item is een wijziging die een engine zelf publiceerde, met datum, één exact citaat en een link. Eronder: wat je als site-eigenaar kunt doen en of CitedBy het controleert. Nieuwste eerst.",
  more="We nemen een wijziging pas op nadat we haar op de eigen pagina van de engine hebben gelezen. Berichten uit vakmedia en onderzoeken van leveranciers zijn geen items. Regels die we niet op een primaire pagina konden bevestigen, laten we weg.", read="Gelezen op", quote="Citaat (originele tekst)", do="Wat je kunt doen", checks="Wat CitedBy controleert", src="Bron",
  yes="Gecontroleerd", part="Gedeeltelijk gecontroleerd", no="Niet gecontroleerd", feed="RSS-feed van deze wijzigingen", cta_h="Zie wat een crawler op je site ziet", cta_b="We crawlen je site tot de paginalimiet van je abonnement en geven per probleem de exacte oplossing. Vanaf € 9, 14 dagen geld-terug-garantie.", cta="Mijn site auditen", ln="Wijzigingen bij engines", fr_note="De bronpagina en het citaat zijn in het Frans.", lang_note="De items zijn in elke taal geschreven; het citaat is de eigen tekst van de bron."),
 "de": dict(title="Was sich 2026 bei Such- und KI-Engines geändert hat, und was CitedBy prüft | CitedBy", desc="Datierte Änderungen von Google, Bing und Lighthouse, die beeinflussen, wie Websites gefunden und zitiert werden, jede auf der Seite der Engine gelesen, mit Handlungsempfehlung und ob CitedBy sie prüft.",
  h1="Was sich bei Such- und KI-Engines geändert hat, und was CitedBy prüft", lead="Jeder Eintrag ist eine Änderung, die eine Engine selbst veröffentlicht hat, mit Datum, einem wörtlichen Zitat und einem Link. Darunter: was Sie als Website-Betreiber tun können und ob CitedBy es prüft. Neueste zuerst.",
  more="Wir führen eine Änderung erst auf, nachdem wir sie auf der eigenen Seite der Engine gelesen haben. Berichte der Fachpresse und Studien von Anbietern sind keine Einträge. Zeilen, die wir auf keiner Primärseite bestätigen konnten, lassen wir weg.", read="Gelesen am", quote="Zitat (Originaltext)", do="Was Sie tun können", checks="Was CitedBy prüft", src="Quelle",
  yes="Geprüft", part="Teilweise geprüft", no="Nicht geprüft", feed="RSS-Feed dieser Änderungen", cta_h="Sehen Sie, was ein Crawler auf Ihrer Website sieht", cta_b="Wir crawlen Ihre Website bis zum Seitenlimit Ihres Tarifs und geben für jedes Problem die genaue Korrektur. Ab 9 €, 14 Tage Geld-zurück-Garantie.", cta="Meine Website prüfen", ln="Änderungen der Engines", fr_note="Quellseite und Zitat sind auf Französisch.", lang_note="Die Einträge sind in jeder Sprache geschrieben; das Zitat ist der Wortlaut der Quelle."),
 "es": dict(title="Qué cambió en los buscadores y motores de IA en 2026, y qué comprueba CitedBy | CitedBy", desc="Cambios fechados de Google, Bing y Lighthouse que afectan a cómo se encuentran y se citan los sitios, cada uno leído en la página del propio motor, con qué hacer y si CitedBy lo comprueba.",
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
 "nl": ("Het filter voor merkzoekopdrachten van Search Console komt naar alle in aanmerking komende sites", "Pas in het prestatierapport van Search Console het filter voor merk- en niet-merkzoekopdrachten toe en lees de twee groepen apart.", "N", "Niet gecontroleerd. Het verandert hoe je Search Console leest, niet hoe je pagina's zijn gebouwd."),
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
 "fr": ("Les rapports de performance de l'IA générative arrivent sur tous les sites dans le monde", "Vérifiez que le rapport de performance de l'IA générative est maintenant visible pour chaque propriété, dans chaque pays que vous servez.", "N", "Non lu. Comme pour l'entrée du lancement : CitedBy ne lit pas ce rapport."),
 "nl": ("Prestatierapporten voor generatieve AI komen wereldwijd naar alle sites", "Controleer of het prestatierapport voor generatieve AI nu zichtbaar is voor elke property, in elk land waar je actief bent.", "N", "Niet gelezen. Net als bij het item over de lancering: CitedBy leest dit rapport niet."),
 "de": ("Leistungsberichte für generative KI stehen weltweit allen Websites zur Verfügung", "Prüfen Sie, ob der Leistungsbericht für generative KI jetzt für jede Property sichtbar ist, in jedem Land, in dem Sie aktiv sind.", "N", "Nicht gelesen. Wie beim Eintrag zum Start: CitedBy liest diesen Bericht nicht."),
 "es": ("Los informes de rendimiento de IA generativa llegan a todos los sitios del mundo", "Comprueba que el informe de rendimiento de IA generativa ya es visible en cada propiedad, en cada país donde operas.", "N", "No se lee. Igual que la entrada del lanzamiento: CitedBy no lee este informe.")},
"gsc-search-generative-ai-control-worldwide": {
 "en": ("The Search generative AI control rolls out to all sites worldwide", "Open Settings > Search generative AI in Search Console and confirm each property is set to include the site, unless the owner chose otherwise.", "N", "Not checked. The setting lives in Search Console and CitedBy cannot see it."),
 "fr": ("Le contrôle de l'IA générative dans la recherche arrive sur tous les sites dans le monde", "Ouvrez Paramètres > IA générative dans la recherche dans Search Console et vérifiez que chaque propriété inclut le site, sauf choix contraire du propriétaire.", "N", "Non vérifié. Ce réglage se trouve dans Search Console et CitedBy ne peut pas le voir."),
 "nl": ("De instelling voor generatieve AI in Zoeken komt wereldwijd naar alle sites", "Open Instellingen > Generatieve AI in Zoeken in Search Console en controleer of elke property de site opneemt, tenzij de eigenaar anders koos.", "N", "Niet gecontroleerd. Deze instelling staat in Search Console en CitedBy kan haar niet zien."),
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
 "fr": ("Google précise que llms.txt n'est pas nécessaire pour la Recherche", "Gardez llms.txt facultatif : publiez-le pour d'autres outils si vous le souhaitez, mais n'en attendez pas de visibilité dans la Recherche Google.", "Y", "Vérifié. Un llms.txt absent apparaît comme un avis facultatif, jamais comme une erreur, car aucun grand assistant n'est confirmé comme le lisant."),
 "nl": ("Google zegt dat llms.txt niet nodig is voor Zoeken", "Houd llms.txt optioneel: publiceer het voor andere tools als je wilt, maar verwacht er geen zichtbaarheid in Google Zoeken van.", "Y", "Gecontroleerd. Een ontbrekend llms.txt verschijnt als optionele melding, nooit als fout, omdat van geen enkele grote assistent bevestigd is dat hij het leest."),
 "de": ("Google erklärt, dass llms.txt für die Suche nicht nötig ist", "Lassen Sie llms.txt optional: Veröffentlichen Sie sie für andere Tools, wenn Sie möchten, erwarten Sie davon aber keine Sichtbarkeit in der Google-Suche.", "Y", "Geprüft. Eine fehlende llms.txt erscheint als optionaler Hinweis, nie als Fehler, weil bei keinem großen Assistenten bestätigt ist, dass er sie liest."),
 "es": ("Google aclara que llms.txt no hace falta para la Búsqueda", "Mantén llms.txt como algo opcional: publícalo para otras herramientas si quieres, pero no esperes visibilidad en Google Search por ello.", "Y", "Comprobado. Un llms.txt ausente aparece como aviso opcional, nunca como error, porque no se ha confirmado que ningún asistente grande lo lea.")},
}


CSS = (".dc article{margin:0 0 28px;padding-top:24px;border-top:1px solid #DCE3EC}.dc article h2{margin:0 0 6px}.dc article blockquote{margin:12px 0 4px;padding:8px 14px;border-left:3px solid #9FB0C7;color:#26364D;overflow-wrap:anywhere}"
       ".dc .chip{display:inline-block;padding:2px 9px;border-radius:999px;font-size:13px;font-weight:600;background:#EEF2F7;color:#26364D}.dc .chip.ok{background:#DDF3E4;color:#14532D}.dc .chip.part{background:#FDF0D0;color:#6B4A00}"
       ".dc article p{overflow-wrap:anywhere}")


def path(l, ext=""): return ("/changes" if l == "en" else "/%s/changes" % l) + ext
def fr_typo(s):
    s = re.sub(r" ([:;!?»])", " \\1", s)
    return s.replace("« ", "« ")
def day(l, iso):
    y, m, d = (int(x) for x in iso.split("-")); mo = MONTHS[l].split()[m - 1]
    return "%d %s %d" % (d, mo, y) if l != "de" else "%d. %s %d" % (d, mo, y)
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
        c, lab = cls[st]; eng = " · ".join(E(ENG[e]) for e in r["engines"])
        qn = ' <span class="src">(%s)</span>' % E(u["fr_note"]) if r["id"] == "google-ai-overviews-ai-mode-france" and l != "fr" else ""
        art.append('<article id="%s"><h2>%s</h2><p class="src"><time datetime="%s">%s</time> · %s · %s <a href="%s">%s</a> · %s %s</p>'
                   '<blockquote lang="%s">“%s”</blockquote><p class="src">%s%s</p>'
                   '<p><b>%s.</b> %s</p><p><b>%s: <span class="chip %s">%s</span></b> %s</p></article>' % (
            r["id"], E(tx(ttl)), r["date"], E(day(l, r["date"])), eng, E(tx(u["src"])), E(r["source_url"]), E(r["source_name"]), E(tx(u["read"])), E(day(l, r["read_on"])),
            "fr" if r["id"] == "google-ai-overviews-ai-mode-france" else "en", E(r["quote"]), E(tx(u["quote"])), qn, E(tx(u["do"])), E(tx(act)), E(tx(u["checks"])), c, E(lab), E(tx(chk))))
    main = '<main id="main"><h1>%s</h1><p class="lead">%s</p><p class="src">%s <a href="%s">%s</a></p>\n%s\n<section class="cta"><h2>%s</h2><p class="lede">%s</p><div class="actions"><a class="btn p" href="%s">%s</a></div></section></main>' % (
        E(tx(u["h1"])), E(tx(u["lead"])), E(tx(u["more"])), path(l, ".xml"), E(tx(u["feed"])), "\n".join(art), E(tx(u["cta_h"])), E(tx(u["cta_b"])), "/" if l == "en" else "/%s/" % l, E(tx(u["cta"])))
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
