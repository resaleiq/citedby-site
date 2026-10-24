title: Adobe Commerce: robots.txt unter Content, Design, Configuration
slug: adobe-commerce
description: Adobe Commerce bearbeitet die robots.txt im Admin unter Search Engine Robots. Cloud-Projekte brauchen Zusatzschritte, und Adobe nennt keinen KI-Crawler.
section: platforms
locale: de
cluster: KI-Crawler nach Plattform
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu Adobe Commerce: Wo Content, Design, Configuration, Bereich Search Engine Robots, Cloud Zusätzliche Schritte, KI-Namen Nicht genannt
hero_sub: Einstellungen für KI-Crawler bei Adobe Commerce
hero_boxes: Wo|Content > Design > Configuration; Bereich|Search Engine Robots; Cloud|Zusätzliche Schritte; KI-Namen|Nicht genannt
widget: on
related: /de/platforms|Alle Plattformen im Vergleich; /de/platforms/shopify|Shopify; /de/bots|KI-Crawler im Vergleich; /de/guides/cms|Checkliste für KI-Sichtbarkeit bei Shopify, WooCommerce und mehr
answer: Bei Adobe Commerce bearbeiten Sie die robots.txt im Admin: Content, Design, Configuration, die Zeile Global, dann Search Engine Robots und das Feld für eigene Anweisungen. Adobes Seiten sprechen allgemein von Web-Crawlern und Bots und nennen keinen KI-Crawler. KI-User-Agents fügen Sie also selbst hinzu. Cloud-Projekte haben zusätzliche Schritte zum Dateipfad.

## Wo die Einstellung bei Adobe Commerce liegt

Gehen Sie in der Seitenleiste des Admin zu Content, dann zu Design und dann zu Configuration. Laut Adobes SEO-Übersicht finden Sie die Global-Konfiguration in der ersten Zeile des Rasters. Klicken Sie auf Edit und öffnen Sie den Bereich Search Engine Robots. Dort liegt das Feld Edit Custom instruction of robots.txt file, dazu die Schaltfläche Reset to Default.

## Was nur die Seiten von Adobe Commerce sagen und die Seiten anderer Plattformen nicht

Bei Adobe Commerce auf Cloud-Infrastruktur hat die robots.txt ein Ortsproblem, das die anderen Plattformen nicht kennen. Laut Adobes Implementation Playbook tragen Sie den Inhalt im Admin ein. Das Dateisystem ist jedoch schreibgeschützt. Die Datei muss deshalb unter pub/media liegen, und ein eigenes Fastly-VCL-Snippet leitet /robots.txt dorthin um. Bei mehreren Sites in einem Projekt nennt das Playbook die Dateien pro Site, zum Beispiel domainone_robots.txt. Bei On-Premises-Installationen sollen die Dateien nach /path/to/commerce/pub/media/ oder /path/to/commerce/media geschrieben werden, je nachdem, was für Ihre Installation passt.

Mit den Worten des Anbieters (englisches Original): “Due to the read-only file system on Adobe Commerce on cloud infrastructure projects, you must specify the pub/media path before generating the file.”

Quelle: [Adobe Commerce Implementation Playbook: Best practices for configuring web crawlers](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/launch/robots-txt), gelesen am 24. Oktober 2026.

## Die Schritte

1. Gehen Sie in der Seitenleiste des Admin zu Content, dann zu Design und dann zu Configuration.
2. Suchen Sie die Global-Konfiguration in der ersten Zeile des Rasters und klicken Sie auf Edit.
3. Scrollen Sie nach unten und öffnen Sie Search Engine Robots.
4. Setzen Sie Default Robots auf INDEX, FOLLOW, NOINDEX, FOLLOW, INDEX, NOFOLLOW oder NOINDEX, NOFOLLOW. Adobe beschreibt diese Werte als Anweisungen an Crawler zum Indexieren und zum Folgen von Links.
5. Tragen Sie bei Bedarf eigene Regeln in das Feld Edit Custom instruction of robots.txt file ein. Reset to Default stellt Adobes Anweisungen wieder her.
6. Klicken Sie auf Save Configuration und öffnen Sie dann die /robots.txt Ihres Shops, um das Ergebnis zu sehen. Adobes Playbook weist darauf hin, dass Sie dort die automatisch erzeugte Datei einsehen können.

## Die passenden Zeilen

Adobes eigene Beispiele verwenden User-agent: * für alle Crawler. Um einen bestimmten Crawler zu erlauben oder zu sperren, fügen Sie eine Gruppe mit seinem Namen hinzu:

Zum Erlauben:

```
User-agent: OAI-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /
```

Zum Sperren:

```
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /
```

Adobes Seiten sagen nicht, ob Text, den Sie eingeben, zu den Standardanweisungen hinzukommt oder sie ersetzt. Speichern Sie und lesen Sie dann /robots.txt, um zu prüfen, was ausgeliefert wird.

## Stolperfallen

Adobes Playbook sagt, Sie sollten Ihren Admin-Pfad nicht in der robots.txt preisgeben, weil das eine Schwachstelle für Hackerangriffe auf die Site und einen möglichen Datenverlust darstellt, und Sie sollten ihn entfernen. Adobes Standardanweisungen beginnen mit User-agent: * und einer Liste von Disallow-Zeilen wie /checkout/ und /catalog/. Prüfen Sie also, was Sie behalten. Für Cloud sagt ein Knowledge-Base-Artikel vom 18. August 2026, der Inhalt der robots.txt werde aus der Admin-Konfiguration erzeugt und in der Datenbank gespeichert, in diesem Szenario sei keine physische Datei nötig. Das Playbook dagegen beschreibt die Umleitung nach pub/media. Die beiden Seiten lesen sich unterschiedlich. Fragen Sie daher den Adobe Commerce Support, was für Ihr Projekt gilt. Das Playbook sagt außerdem, seine Hinweise gälten nur für den nativen Adobe-Commerce-Storefront, nicht für Headless- oder Adobe-Experience-Manager-Storefronts.

## Vergleich mit Shopify

[Shopify](/de/platforms/shopify): Eine Theme-Vorlage statt eines Admin-Feldes, und der Support korrigiert keine Änderungen daran.

## Prüfen Sie Ihre eigene Website

Die kostenlose Prüfung im Feld oben liest die robots.txt für die KI-Crawler und sendet pro Crawler eine Live-Anfrage. So fällt eine Regel auf, die die Einstellungen Ihrer Plattform erlauben, eine Firewall aber ablehnt. Die vollständige Liste der Crawler finden Sie im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Warum ändert sich meine eigene robots.txt bei Adobe Commerce Cloud nicht?

Laut Adobes Knowledge Base ist die übliche Ursache, dass die Indexierung durch Suchmaschinen deaktiviert ist. Dann wird eigener robots.txt-Inhalt nicht angewendet. Beheben Sie das in der Cloud Console oder mit der Einstellung restrict_robots der magento-cloud-CLI. Der Artikel ergänzt, dass bei Staging-Umgebungen die Indexierung standardmäßig deaktiviert ist und sich dort nicht aktivieren lässt.

### Listet Adobe Commerce KI-Crawler für die robots.txt auf?

Nicht in den Seiten, die wir gelesen haben. Sie sprechen von Web-Crawlern und Bots, und ihre Beispiele verwenden nur User-agent: *. Fügen Sie jeden KI-User-Agent, den Sie erlauben oder sperren möchten, als eigene Gruppe hinzu.

## Sources

- [Adobe Commerce Implementation Playbook: Best practices for configuring web crawlers](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/launch/robots-txt), gelesen am 24. Oktober 2026
- [Adobe Commerce Admin guide: SEO overview](https://experienceleague.adobe.com/en/docs/commerce-admin/marketing/seo/seo-overview), gelesen am 24. Oktober 2026
- [Adobe Commerce knowledge base: Resolve robots.txt not updating or displaying default settings](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/robots-txt-not-updated-or-displaying-default-settings), gelesen am 24. Oktober 2026
