title: Ghost: robots.txt im Theme: KI-Crawler erlauben oder sperren
slug: ghost
description: Ghost hat im Admin keine robots.txt-Einstellung. Laut Hilfeseite liegt die Datei im Theme-Stammverzeichnis und ersetzt den Standard.
section: platforms
locale: de
cluster: KI-Crawler nach Plattform
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu Ghost: Wo Stammverzeichnis des Themes, Datei robots.txt, Wirkung Ersetzt den Standard, Ghost(Pro) Tarif Creator oder höher
hero_sub: Einstellungen für KI-Crawler bei Ghost
hero_boxes: Wo|Stammverzeichnis des Themes; Datei|robots.txt; Wirkung|Ersetzt den Standard; Ghost(Pro)|Creator oder höher
widget: on
related: /de/platforms|Alle Plattformen im Vergleich; /de/platforms/wordpress-com|WordPress.com; /de/bots|KI-Crawler im Vergleich; /de/guides/cms|Checkliste für KI-Sichtbarkeit bei Shopify, WooCommerce und mehr
answer: Ghost liefert eine Standard-robots.txt aus. Um sie zu ändern, speichern Sie Ihre eigene robots.txt im Stammverzeichnis Ihres Themes und installieren und aktivieren dann die neue Theme-Version. Laut Ghosts Hilfeseite brauchen eigene Themes bei Ghost(Pro) den Tarif Creator oder höher. Ihr Tarif entscheidet also, ob Sie die Datei bearbeiten können.

## Wo die Einstellung bei Ghost liegt

Im Admin gibt es kein Feld für die robots.txt. Ghosts Hilfeseite sagt, die Datei liegt im Theme Ihrer Site: Schreiben Sie Ihre robots.txt und speichern Sie sie im Stammverzeichnis des Themes. Ghosts Theme-Dokumentation sagt dasselbe in einem Satz: Themes können eine robots.txt enthalten, die die von Ghost mitgelieferte Standard-robots.txt überschreibt.

## Was nur Ghosts Seite sagt und die anderer Plattformen nicht

Bei Ghost wandert die Datei mit dem Theme, also entscheidet Ihr Tarif, ob Sie sie ändern können. Ghosts Hilfeseite sagt, Sie müssten sich damit wohlfühlen, Ihre eigene robots.txt zu schreiben und eine neue Version Ihres Themes zu installieren. Dann nennt sie eine Tarifgrenze für Ghost(Pro), Ghosts gehosteten Dienst: Für die Installation eines eigenen Themes ist der Tarif Creator oder höher nötig. Was danach geschieht, beschreibt die Seite so.

Mit den Worten des Anbieters (englisches Original): “Once the new version of the theme is installed and activated, the theme's robots.txt will be used in place of Ghost's default robots.txt.”

Quelle: [Ghost Help: Modifying robots.txt](https://ghost.org/help/modifying-robots-txt/), gelesen am 24. Oktober 2026.

## Die Schritte

1. Schreiben Sie Ihre robots.txt-Datei.
2. Speichern Sie sie im Stammverzeichnis Ihres Themes.
3. Installieren Sie die neue Version des Themes und aktivieren Sie sie. Ghost sagt, dass die robots.txt des Themes anstelle des Standards verwendet wird, sobald die neue Version installiert und aktiviert ist.
4. Prüfen Sie bei Ghost(Pro) zuerst Ihren Tarif: Ghost sagt, dass für die Installation eines eigenen Themes der Tarif Creator oder höher nötig ist.

## Die passenden Zeilen

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

## Stolperfallen

Die Datei des Themes wird anstelle von Ghosts Standard verwendet, nicht zusätzlich dazu. Ghosts Seiten sagen nicht, was der Standard enthält. Öffnen Sie daher yoursite.com/robots.txt, bevor Sie ihn ersetzen, und übernehmen Sie Zeilen, die Sie behalten möchten, etwa eine Sitemap-Zeile. Die Seite warnt außerdem, dass dieser Weg voraussetzt, dass Sie sich damit wohlfühlen, die Datei selbst zu schreiben, und sie behandelt KI-Crawler nicht beim Namen.

## Vergleich mit WordPress.com

[WordPress.com](/de/platforms/wordpress-com): Der KI-Opt-out ist eine Freigabe-Einstellung, keine Datei, die Sie schreiben.

## Prüfen Sie Ihre eigene Website

Die kostenlose Prüfung im Feld oben liest die robots.txt für die KI-Crawler und sendet pro Crawler eine Live-Anfrage. So fällt eine Regel auf, die die Einstellungen Ihrer Plattform erlauben, eine Firewall aber ablehnt. Die vollständige Liste der Crawler finden Sie im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Wo lege ich bei Ghost eine eigene robots.txt ab?

Im Stammverzeichnis Ihres Themes. Ghosts Hilfeseite sagt, dass die robots.txt des Themes anstelle von Ghosts Standard verwendet wird, sobald die neue Theme-Version installiert und aktiviert ist.

### Brauche ich einen kostenpflichtigen Tarif, um die robots.txt bei Ghost(Pro) zu bearbeiten?

Ghosts Seite sagt, dass die Installation eines eigenen Themes bei Ghost(Pro) ein Abonnement des Tarifs Creator oder höher erfordert. Weil die Datei Teil des Themes ist, gilt das auch für eine eigene robots.txt.

## Sources

- [Ghost Help: Modifying robots.txt](https://ghost.org/help/modifying-robots-txt/), gelesen am 24. Oktober 2026
- [Ghost Docs: Theme structure](https://docs.ghost.org/themes/structure), gelesen am 24. Oktober 2026
