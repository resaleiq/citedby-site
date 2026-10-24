title: Framer: Eigene robots.txt mit Static Files hochladen
slug: framer
description: Framer erzeugt für jede Site eine robots.txt. Ändern geht nur per eigenem Upload über Static Files in Pro oder Enterprise, der die erzeugte Datei ersetzt.
section: platforms
locale: de
cluster: KI-Crawler nach Plattform
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu Framer: Wo Static Files, Tarife Pro und Enterprise, Standard Automatisch erzeugt, Eigene Datei Ersetzt den Standard
hero_sub: Einstellungen für KI-Crawler bei Framer
hero_boxes: Wo|Static Files; Tarife|Pro und Enterprise; Standard|Automatisch erzeugt; Eigene Datei|Ersetzt den Standard
widget: on
related: /de/platforms|Alle Plattformen im Vergleich; /de/platforms/webflow|Webflow; /de/bots|KI-Crawler im Vergleich; /de/guides/cms|Checkliste für KI-Sichtbarkeit bei Shopify, WooCommerce und mehr
answer: Framer erzeugt für jede veröffentlichte Site eine robots.txt. Um KI-Crawler zu erlauben oder zu sperren, laden Sie über Static Files Ihre eigene Datei hoch, mit dem Pfad /. Laut Framer ist das in den Tarifen Pro und Enterprise möglich, und Ihr Upload ersetzt die erzeugte Datei, statt sie zu ergänzen.

## Wo die Einstellung bei Framer liegt

Wählen Sie in Ihrem Projekt-Dashboard Ihre Domain aus, öffnen Sie den Tab Files und laden Sie Ihre Datei mit dem Pfad / hoch. Framers Hilfeseite nennt das Static Files. Um zuerst die aktuelle Datei zu sehen, hängen Sie im Browser /robots.txt an die Domain Ihrer Site an.

## Was nur Framers Seite sagt und die anderer Plattformen nicht

Framer bietet keinen robots.txt-Editor. Die Datei wird für Sie erzeugt, und Sie können sie nur ändern, indem Sie eine Ersatzdatei hochladen, was vom Tarif abhängt. Framers Seite sagt, dass Sie mit Static Files eine eigene robots.txt hochladen können, wenn Sie eine brauchen, und dass die neue Datei die automatisch erzeugte ersetzt. Die Einschränkung durch den Tarif folgt direkt danach.

Mit den Worten des Anbieters (englisches Original): “This is available on Pro and Enterprise plans.”

Quelle: [Framer Help: Access your robots.txt file](https://www.framer.com/help/articles/how-can-i-access-the-robots-txt-file/), gelesen am 24. Oktober 2026.

## Die Schritte

1. Schreiben Sie Ihre robots.txt als reine Textdatei auf Ihrem Computer.
2. Gehen Sie zu Ihrem Projekt-Dashboard und wählen Sie Ihre Domain aus.
3. Öffnen Sie den Tab Files.
4. Laden Sie Ihre Datei mit dem Pfad / hoch.
5. Öffnen Sie yourdomain.com/robots.txt in einem Browser, um zu bestätigen, dass die aktuelle Datei Ihre ist.

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

Weil Ihr Upload die erzeugte Datei ersetzt, ist alles verloren, was in ihr stand, wenn Sie es nicht zuvor kopieren. Framers Seite sagt nicht, was die erzeugte Datei enthält. Lesen Sie daher yourdomain.com/robots.txt, bevor Sie hochladen, und behalten Sie Zeilen, die Sie brauchen, etwa eine Sitemap-Zeile. Die Seite behandelt die robots.txt allgemein und nennt keine KI-Crawler beim Namen. Die User-Agents oben sind also Beispiele, die Sie mit der jeweiligen Seite des Anbieters abgleichen sollten. Die Framer-Seite wurde zuletzt am 15. September 2026 aktualisiert.

## Vergleich mit Webflow

[Webflow](/de/platforms/webflow): Regeln werden in ein Einstellungsfeld getippt, statt als Datei hochgeladen zu werden, dazu kommt ein Content-Signal-Header.

## Prüfen Sie Ihre eigene Website

Die kostenlose Prüfung im Feld oben liest die robots.txt für die KI-Crawler und sendet pro Crawler eine Live-Anfrage. So fällt eine Regel auf, die die Einstellungen Ihrer Plattform erlauben, eine Firewall aber ablehnt. Die vollständige Liste der Crawler finden Sie im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Kann ich die robots.txt in Framer bearbeiten?

Ja, per Upload. Framers Seite sagt, Sie sollen im Projekt-Dashboard den Tab Files für Ihre Domain öffnen und Ihre Datei mit dem Pfad / hochladen. Sie sagt, dass das in den Tarifen Pro und Enterprise möglich ist.

### Erstellt Framer automatisch eine robots.txt?

Ja. Framers Seite sagt, dass es für jede veröffentlichte Site eine robots.txt erzeugt und dass eine eigene Datei, die über Static Files hochgeladen wird, die Standarddatei ersetzt.

## Sources

- [Framer Help: Access your robots.txt file](https://www.framer.com/help/articles/how-can-i-access-the-robots-txt-file/), gelesen am 24. Oktober 2026
