"""RES-3749: the words of /backlinks and /backlinks/<host> in en, fr, de, es and nl, and the locale helpers. Standard library only.
English is the source. fr, de, es and nl are written for this page (not native-read yet: QA's language pass checks them). Register: FR vous, DE Sie, ES tú, NL je.
UI = masthead and footer labels of the reading pages: the same values as tools/build_legal.UI and tools/docshell.EXTRA; test_res3749_backlinks_i18n.py pins them, so the server needs no tools/ at run time."""

LANGS = ("en", "fr", "de", "es", "nl")
NAMES = {"en": "English", "fr": "Français", "de": "Deutsch", "es": "Español", "nl": "Nederlands"}
HOME = {"en": "/", "fr": "/fr", "de": "/de", "es": "/es", "nl": "/nl"}
NNBSP = " "  # narrow no-break space: FR thousands separator and the space before ? : ; !

UI = {
    "fr": dict(check="Ce que nous vérifions", plans="Tarifs", blog="Guides", data="Données", signin="Connexion", cta="Auditer un site", skip="Aller au contenu", main="Principal",
               terms="Conditions", privacy="Confidentialité", refund="Remboursements", contact="Contact", legal="Mentions légales", home="/fr", plans_h="/fr/plans", blog_h="/fr/blog",
               method="Méthode", about="À propos"),
    "nl": dict(check="Wat wij controleren", plans="Prijzen", blog="Gidsen", data="Data", signin="Inloggen", cta="Een site auditen", skip="Naar de inhoud", main="Hoofdmenu",
               terms="Voorwaarden", privacy="Privacy", refund="Terugbetaling", contact="Contact", legal="Juridische informatie", home="/nl", plans_h="/nl/plans", blog_h="/nl/blog",
               method="Methode", about="Over ons"),
    "de": dict(check="Was wir prüfen", plans="Preise", blog="Ratgeber", data="Daten", signin="Anmelden", cta="Website prüfen", skip="Zum Inhalt", main="Hauptmenü",
               terms="AGB", privacy="Datenschutz", refund="Erstattungen", contact="Kontakt", legal="Impressum", home="/de", plans_h="/de/plans", blog_h="/de/blog",
               method="Methode", about="Über uns"),
    "es": dict(check="Qué comprobamos", plans="Precios", blog="Guías", data="Datos", signin="Iniciar sesión", cta="Auditar un sitio", skip="Saltar al contenido", main="Principal",
               terms="Condiciones", privacy="Privacidad", refund="Reembolsos", contact="Contacto", legal="Aviso legal", home="/es", plans_h="/es/plans", blog_h="/es/blog",
               method="Método", about="Sobre nosotros"),
}

_SCOPE = "nuestros propios sitios, herramientas SEO y los sitios más enlazados bajo .eu, .fr, .de, .es, .nl, .it, .pt y .be"

T = {
    "en": dict(
        crumb_home="CitedBy", crumb_bl="Backlinks", lang_label="Language:", graph_label="Aug-Oct 2026",
        index_title="Who links to a website? Free referring-domain lookup | CitedBy", index_h1="Who links to a website? Free referring-domain lookup",
        index_desc="Free lookup of the strongest domains linking to a site, from Common Crawl's open web graph. Method and limits shown.",
        index_ans="Type a domain to see the 20 strongest domains that link to it in Common Crawl's latest open web graph, with the method shown. No sign-up.",
        form_label="Domain", form_ph="example.com", form_btn="Who links to it?",
        top_h2="Most-linked EU sites in the data",
        top_note="Count in brackets: referring domains. The lookup covers {n} domains: our own sites, SEO tools and the most-linked sites under .eu, .fr, .de, .es, .nl, .it, .pt and .be.",
        method_h2="Method and limits",
        method=("Source: Common Crawl's public domain web graph, built from three monthly crawls ({d} domains, {l} links). We count distinct linking domains, not pages, "
                "and do not use any third-party backlink index. Common Crawl samples the web, so counts are lower than a full index such as Ahrefs or Semrush; use them to compare sites "
                "and spot big referrers, not as an exact total. Updated each quarter, last graph: {graph}. Nofollow and link position are not in this data."),
        bad_host="That does not look like a domain name. Try something like example.com.",
        host_h1="Who links to {host}?", host_title="Who links to {host}? Referring domains from open data | CitedBy",
        desc_n="{n} domains link to {host} in Common Crawl's open web graph ({label}). The 20 strongest, with the method.",
        desc_n_one="1 domain links to {host} in Common Crawl's open web graph ({label}), with the method.",
        desc_0="Common Crawl found no linking domains for {host}. What that means and how the data is built.",
        ans_n="{n} domains link to {host} in the latest Common Crawl web graph ({label}). Below are the {k} strongest. Strength is how many domains link to that referrer.",
        ans_n_one="1 domain links to {host} in the latest Common Crawl web graph ({label}). Strength is how many domains link to that referrer.",
        ans_0="Common Crawl found no linking domains for {host}. New or small sites are often missing; it does not mean you have none.",
        src_line="Common Crawl graph {graph} · read {date} · {n} referring domains",
        table_h2="Strongest referring domains", th_rank="#", th_ref="Referring domain", th_str="Domains linking to it", dl_rank="#", dl_ref="Referring domain", dl_str="Strength",
        another_h2="Look up another domain",
        nis_title="Who links to {host}? Not in the data yet | CitedBy", nis_desc="{host} is not in CitedBy's backlink data set yet.",
        nis_ans=("{host} is not in the set we have loaded yet. The lookup covers our own sites, SEO tools and the most-linked sites under .eu, .fr, .de, .es, .nl, .it, .pt and .be. "
                 "It does not mean the site has no links. The set grows with each quarterly graph."),
        cta_h2="Can search engines and AI assistants read {name}?", cta_name="your site",
        cta_lede=("Links get a site noticed. Access and clean markup get it cited. We crawl your site up to your plan's page limit and give you the exact fix for each issue. "
                  "Free check first; full audits from €9, 14-day money-back guarantee."),
        cta_btn="Check {name} free",
        ld_name="Referring domains of {host} (Common Crawl web graph {graph})",
    ),
    "fr": dict(
        crumb_home="CitedBy", crumb_bl="Backlinks", lang_label="Langue :", graph_label="août-oct. 2026",
        index_title="Qui renvoie vers un site web ? Recherche gratuite de domaines référents | CitedBy", index_h1="Qui renvoie vers un site web ? Recherche gratuite de domaines référents",
        index_desc="Recherche gratuite des domaines qui renvoient le plus vers un site, d'après le graphe web ouvert de Common Crawl. Méthode et limites affichées.",
        index_ans="Saisissez un domaine pour voir les 20 domaines les plus forts qui renvoient vers lui dans le dernier graphe web ouvert de Common Crawl, avec la méthode. Sans inscription.",
        form_label="Domaine", form_ph="example.com", form_btn="Qui renvoie vers lui ?",
        top_h2="Les sites européens les plus liés dans les données",
        top_note="Entre parenthèses : le nombre de domaines référents. La recherche couvre {n} domaines : nos propres sites, des outils SEO et les sites les plus liés sous .eu, .fr, .de, .es, .nl, .it, .pt et .be.",
        method_h2="Méthode et limites",
        method=("Source : le graphe web de domaines public de Common Crawl, construit à partir de trois explorations mensuelles ({d} domaines, {l} liens). Nous comptons les domaines référents distincts, "
                "pas les pages, et n'utilisons aucun index de backlinks tiers. Common Crawl échantillonne le web : les chiffres sont donc inférieurs à ceux d'un index complet comme Ahrefs ou Semrush. "
                "Servez-vous-en pour comparer des sites et repérer les gros référents, pas comme un total exact. Mis à jour chaque trimestre, dernier graphe : {graph}. "
                "Le nofollow et la position du lien ne figurent pas dans ces données."),
        bad_host="Cela ne ressemble pas à un nom de domaine. Essayez par exemple example.com.",
        host_h1="Qui renvoie vers {host} ?", host_title="Qui renvoie vers {host} ? Domaines référents issus de données ouvertes | CitedBy",
        desc_n="{n} domaines renvoient vers {host} dans le graphe web ouvert de Common Crawl ({label}). Les 20 plus forts, avec la méthode.",
        desc_n_one="1 domaine renvoie vers {host} dans le graphe web ouvert de Common Crawl ({label}), avec la méthode.",
        desc_0="Common Crawl n'a trouvé aucun domaine référent pour {host}. Ce que cela signifie et comment les données sont construites.",
        ans_n="{n} domaines renvoient vers {host} dans le dernier graphe web de Common Crawl ({label}). Voici les {k} plus forts. La force correspond au nombre de domaines qui renvoient vers ce référent.",
        ans_n_one="1 domaine renvoie vers {host} dans le dernier graphe web de Common Crawl ({label}). La force correspond au nombre de domaines qui renvoient vers ce référent.",
        ans_0="Common Crawl n'a trouvé aucun domaine référent pour {host}. Les sites récents ou petits manquent souvent ; cela ne veut pas dire que vous n'en avez aucun.",
        src_line="Graphe Common Crawl {graph} · lu le {date} · {n} domaines référents",
        table_h2="Domaines référents les plus forts", th_rank="#", th_ref="Domaine référent", th_str="Domaines qui renvoient vers lui", dl_rank="#", dl_ref="Domaine référent", dl_str="Force",
        another_h2="Rechercher un autre domaine",
        nis_title="Qui renvoie vers {host} ? Pas encore dans les données | CitedBy", nis_desc="{host} ne figure pas encore dans l'ensemble de données de backlinks de CitedBy.",
        nis_ans=("{host} ne figure pas encore dans l'ensemble que nous avons chargé. La recherche couvre nos propres sites, des outils SEO et les sites les plus liés sous .eu, .fr, .de, .es, .nl, .it, .pt et .be. "
                 "Cela ne veut pas dire que le site n'a aucun lien. L'ensemble s'élargit à chaque graphe trimestriel."),
        cta_h2="Les moteurs de recherche et les assistants IA peuvent-ils lire {name} ?", cta_name="votre site",
        cta_lede=("Les liens font remarquer un site. L'accès et un balisage propre le font citer. Nous explorons votre site jusqu'à la limite de pages de votre offre et vous donnons la correction exacte de chaque problème. "
                  "Test gratuit d'abord ; audits complets dès 9 €, garantie de remboursement de 14 jours."),
        cta_btn="Tester {name} gratuitement",
        ld_name="Domaines référents de {host} (graphe web Common Crawl {graph})",
    ),
    "de": dict(
        crumb_home="CitedBy", crumb_bl="Backlinks", lang_label="Sprache:", graph_label="Aug.-Okt. 2026",
        index_title="Wer verlinkt auf eine Website? Kostenlose Abfrage verweisender Domains | CitedBy", index_h1="Wer verlinkt auf eine Website? Kostenlose Abfrage verweisender Domains",
        index_desc="Kostenlose Abfrage der stärksten Domains, die auf eine Website verlinken, aus dem offenen Web-Graphen von Common Crawl. Methode und Grenzen inklusive.",
        index_ans="Geben Sie eine Domain ein und sehen Sie die 20 stärksten Domains, die im aktuellen offenen Web-Graphen von Common Crawl auf sie verlinken, samt Methode. Ohne Anmeldung.",
        form_label="Domain", form_ph="example.com", form_btn="Wer verlinkt darauf?",
        top_h2="Die meistverlinkten EU-Seiten in den Daten",
        top_note="In Klammern: verweisende Domains. Die Abfrage deckt {n} Domains ab: unsere eigenen Seiten, SEO-Tools und die meistverlinkten Seiten unter .eu, .fr, .de, .es, .nl, .it, .pt und .be.",
        method_h2="Methode und Grenzen",
        method=("Quelle: der öffentliche Domain-Web-Graph von Common Crawl, aufgebaut aus drei monatlichen Crawls ({d} Domains, {l} Links). Wir zählen verschiedene verweisende Domains, keine Seiten, "
                "und nutzen keinen Backlink-Index von Dritten. Common Crawl erfasst das Web nur stichprobenartig, deshalb liegen die Zahlen unter denen eines vollständigen Index wie Ahrefs oder Semrush. "
                "Nutzen Sie sie, um Seiten zu vergleichen und große Verweisgeber zu finden, nicht als exakte Summe. Aktualisiert jedes Quartal, letzter Graph: {graph}. "
                "Nofollow und Linkposition sind in diesen Daten nicht enthalten."),
        bad_host="Das sieht nicht nach einem Domainnamen aus. Versuchen Sie es mit etwas wie example.com.",
        host_h1="Wer verlinkt auf {host}?", host_title="Wer verlinkt auf {host}? Verweisende Domains aus offenen Daten | CitedBy",
        desc_n="{n} Domains verlinken im offenen Web-Graphen von Common Crawl ({label}) auf {host}. Die 20 stärksten, mit Methode.",
        desc_n_one="1 Domain verlinkt im offenen Web-Graphen von Common Crawl ({label}) auf {host}, mit Methode.",
        desc_0="Common Crawl hat keine verweisenden Domains für {host} gefunden. Was das bedeutet und wie die Daten entstehen.",
        ans_n="{n} Domains verlinken im aktuellen Web-Graphen von Common Crawl ({label}) auf {host}. Unten stehen die {k} stärksten. Die Stärke zeigt, wie viele Domains auf diesen Verweisgeber verlinken.",
        ans_n_one="1 Domain verlinkt im aktuellen Web-Graphen von Common Crawl ({label}) auf {host}. Die Stärke zeigt, wie viele Domains auf diesen Verweisgeber verlinken.",
        ans_0="Common Crawl hat keine verweisenden Domains für {host} gefunden. Neue oder kleine Seiten fehlen oft; das heißt nicht, dass Sie keine Links haben.",
        src_line="Common-Crawl-Graph {graph} · gelesen am {date} · {n} verweisende Domains",
        table_h2="Stärkste verweisende Domains", th_rank="#", th_ref="Verweisende Domain", th_str="Domains, die darauf verlinken", dl_rank="#", dl_ref="Verweisende Domain", dl_str="Stärke",
        another_h2="Eine andere Domain abfragen",
        nis_title="Wer verlinkt auf {host}? Noch nicht in den Daten | CitedBy", nis_desc="{host} ist noch nicht im Backlink-Datensatz von CitedBy.",
        nis_ans=("{host} gehört noch nicht zu dem Datensatz, den wir geladen haben. Die Abfrage deckt unsere eigenen Seiten, SEO-Tools und die meistverlinkten Seiten unter .eu, .fr, .de, .es, .nl, .it, .pt und .be ab. "
                 "Das heißt nicht, dass die Seite keine Links hat. Der Datensatz wächst mit jedem Quartals-Graphen."),
        cta_h2="Können Suchmaschinen und KI-Assistenten {name} lesen?", cta_name="Ihre Website",
        cta_lede=("Links machen eine Website bekannt. Zugang und sauberes Markup machen sie zitierfähig. Wir crawlen Ihre Website bis zum Seitenlimit Ihres Tarifs und liefern für jedes Problem die genaue Korrektur. "
                  "Erst der kostenlose Check; vollständige Audits ab 9 €, 14 Tage Geld-zurück-Garantie."),
        cta_btn="{name} kostenlos prüfen",
        ld_name="Verweisende Domains von {host} (Common-Crawl-Web-Graph {graph})",
    ),
    "es": dict(
        crumb_home="CitedBy", crumb_bl="Backlinks", lang_label="Idioma:", graph_label="ago.-oct. 2026",
        index_title="¿Quién enlaza a una web? Consulta gratuita de dominios de referencia | CitedBy", index_h1="¿Quién enlaza a una web? Consulta gratuita de dominios de referencia",
        index_desc="Consulta gratuita de los dominios que más enlazan a un sitio, con el grafo web abierto de Common Crawl. Método y límites a la vista.",
        index_ans="Escribe un dominio para ver los 20 dominios más fuertes que enlazan a él en el último grafo web abierto de Common Crawl, con el método. Sin registro.",
        form_label="Dominio", form_ph="example.com", form_btn="¿Quién enlaza?",
        top_h2="Los sitios de la UE más enlazados en los datos",
        top_note="Entre paréntesis: dominios de referencia. La consulta cubre {n} dominios: " + _SCOPE + ".",
        method_h2="Método y límites",
        method=("Fuente: el grafo web de dominios público de Common Crawl, construido con tres rastreos mensuales ({d} dominios, {l} enlaces). Contamos dominios de referencia distintos, no páginas, "
                "y no usamos ningún índice de backlinks de terceros. Common Crawl muestrea la web, así que las cifras son menores que las de un índice completo como Ahrefs o Semrush. "
                "Úsalas para comparar sitios y detectar a los grandes referentes, no como un total exacto. Se actualiza cada trimestre; último grafo: {graph}. "
                "El nofollow y la posición del enlace no están en estos datos."),
        bad_host="Eso no parece un nombre de dominio. Prueba con algo como example.com.",
        host_h1="¿Quién enlaza a {host}?", host_title="¿Quién enlaza a {host}? Dominios de referencia con datos abiertos | CitedBy",
        desc_n="{n} dominios enlazan a {host} en el grafo web abierto de Common Crawl ({label}). Los 20 más fuertes, con el método.",
        desc_n_one="1 dominio enlaza a {host} en el grafo web abierto de Common Crawl ({label}), con el método.",
        desc_0="Common Crawl no encontró dominios que enlacen a {host}. Qué significa y cómo se construyen los datos.",
        ans_n="{n} dominios enlazan a {host} en el último grafo web de Common Crawl ({label}). Abajo están los {k} más fuertes. La fuerza es cuántos dominios enlazan a ese referente.",
        ans_n_one="1 dominio enlaza a {host} en el último grafo web de Common Crawl ({label}). La fuerza es cuántos dominios enlazan a ese referente.",
        ans_0="Common Crawl no encontró dominios que enlacen a {host}. Los sitios nuevos o pequeños suelen faltar; no significa que no tengas ninguno.",
        src_line="Grafo de Common Crawl {graph} · leído el {date} · {n} dominios de referencia",
        table_h2="Dominios de referencia más fuertes", th_rank="#", th_ref="Dominio de referencia", th_str="Dominios que enlazan a él", dl_rank="#", dl_ref="Dominio de referencia", dl_str="Fuerza",
        another_h2="Consultar otro dominio",
        nis_title="¿Quién enlaza a {host}? Aún no está en los datos | CitedBy", nis_desc="{host} aún no está en el conjunto de datos de backlinks de CitedBy.",
        nis_ans=("{host} aún no está en el conjunto que hemos cargado. La consulta cubre " + _SCOPE + ". "
                 "No significa que el sitio no tenga enlaces. El conjunto crece con cada grafo trimestral."),
        cta_h2="¿Pueden los buscadores y los asistentes de IA leer {name}?", cta_name="tu sitio",
        cta_lede=("Los enlaces hacen que se note un sitio. El acceso y un marcado limpio hacen que lo citen. Rastreamos tu sitio hasta el límite de páginas de tu plan y te damos la corrección exacta de cada problema. "
                  "Primero la comprobación gratuita; auditorías completas desde 9 €, garantía de devolución de 14 días."),
        cta_btn="Comprobar {name} gratis",
        ld_name="Dominios de referencia de {host} (grafo web de Common Crawl {graph})",
    ),
    "nl": dict(
        crumb_home="CitedBy", crumb_bl="Backlinks", lang_label="Taal:", graph_label="aug.-okt. 2026",
        index_title="Wie linkt naar een website? Gratis opzoeken van verwijzende domeinen | CitedBy", index_h1="Wie linkt naar een website? Gratis opzoeken van verwijzende domeinen",
        index_desc="Zoek gratis de sterkste domeinen op die naar een site linken, uit de open webgraaf van Common Crawl. Methode en beperkingen erbij.",
        index_ans="Typ een domein om de 20 sterkste domeinen te zien die ernaar linken in de nieuwste open webgraaf van Common Crawl, met de methode erbij. Zonder aanmelding.",
        form_label="Domein", form_ph="example.com", form_btn="Wie linkt ernaar?",
        top_h2="De meest gelinkte EU-sites in de data",
        top_note="Tussen haakjes: verwijzende domeinen. De zoekfunctie dekt {n} domeinen: onze eigen sites, SEO-tools en de meest gelinkte sites onder .eu, .fr, .de, .es, .nl, .it, .pt en .be.",
        method_h2="Methode en beperkingen",
        method=("Bron: de openbare domeinwebgraaf van Common Crawl, opgebouwd uit drie maandelijkse crawls ({d} domeinen, {l} links). We tellen unieke verwijzende domeinen, geen pagina's, "
                "en gebruiken geen backlinkindex van derden. Common Crawl neemt steekproeven van het web, dus de aantallen liggen lager dan bij een volledige index zoals Ahrefs of Semrush. "
                "Gebruik ze om sites te vergelijken en grote verwijzers te vinden, niet als exact totaal. Elk kwartaal bijgewerkt, laatste graaf: {graph}. "
                "Nofollow en de plek van de link zitten niet in deze data."),
        bad_host="Dat lijkt niet op een domeinnaam. Probeer iets als example.com.",
        host_h1="Wie linkt naar {host}?", host_title="Wie linkt naar {host}? Verwijzende domeinen uit open data | CitedBy",
        desc_n="{n} domeinen linken naar {host} in de open webgraaf van Common Crawl ({label}). De 20 sterkste, met de methode.",
        desc_n_one="1 domein linkt naar {host} in de open webgraaf van Common Crawl ({label}), met de methode.",
        desc_0="Common Crawl vond geen verwijzende domeinen voor {host}. Wat dat betekent en hoe de data is opgebouwd.",
        ans_n="{n} domeinen linken naar {host} in de nieuwste webgraaf van Common Crawl ({label}). Hieronder staan de {k} sterkste. Sterkte is hoeveel domeinen naar die verwijzer linken.",
        ans_n_one="1 domein linkt naar {host} in de nieuwste webgraaf van Common Crawl ({label}). Sterkte is hoeveel domeinen naar die verwijzer linken.",
        ans_0="Common Crawl vond geen verwijzende domeinen voor {host}. Nieuwe of kleine sites ontbreken vaak; het betekent niet dat je er geen hebt.",
        src_line="Common Crawl-graaf {graph} · gelezen op {date} · {n} verwijzende domeinen",
        table_h2="Sterkste verwijzende domeinen", th_rank="#", th_ref="Verwijzend domein", th_str="Domeinen die ernaar linken", dl_rank="#", dl_ref="Verwijzend domein", dl_str="Sterkte",
        another_h2="Zoek een ander domein op",
        nis_title="Wie linkt naar {host}? Nog niet in de data | CitedBy", nis_desc="{host} zit nog niet in de backlinkdataset van CitedBy.",
        nis_ans=("{host} zit nog niet in de set die we hebben geladen. De zoekfunctie dekt onze eigen sites, SEO-tools en de meest gelinkte sites onder .eu, .fr, .de, .es, .nl, .it, .pt en .be. "
                 "Het betekent niet dat de site geen links heeft. De set groeit met elke kwartaalgraaf."),
        cta_h2="Kunnen zoekmachines en AI-assistenten {name} lezen?", cta_name="je site",
        cta_lede=("Links zorgen dat een site opvalt. Toegang en schone markup zorgen dat hij wordt aangehaald. We crawlen je site tot de paginalimiet van je abonnement en geven de exacte fix voor elk probleem. "
                  "Eerst de gratis check; volledige audits vanaf €9, 14 dagen geld-terug-garantie."),
        cta_btn="Check {name} gratis",
        ld_name="Verwijzende domeinen van {host} (Common Crawl-webgraaf {graph})",
    ),
}


def _fr(s):
    """French typography: a narrow no-break space before ? : ; !"""
    for p in "?:;!":
        s = s.replace(" " + p, NNBSP + p)
    return s


T["fr"] = {k: _fr(v) for k, v in T["fr"].items()}

_SEP = {"en": ",", "fr": NNBSP, "de": ".", "es": ".", "nl": "."}


def fmt(n, lg):
    """1234567 -> 1,234,567 (en), 1 234 567 with narrow no-break spaces (fr), 1.234.567 (de, es, nl)."""
    return f"{int(n):,}".replace(",", _SEP[lg])


def plural_key(n):
    return "one" if n == 1 else "other"


def prefix(lg):
    return "" if lg == "en" else "/" + lg
