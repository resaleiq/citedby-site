title: PrestaShop: robots.txt-Generator, ein Regelsatz für alle Bots
slug: prestashop
description: PrestaShops Leitfaden beschreibt die Schaltfläche Generate robots.txt: Sie ersetzt Ihre Datei und nutzt nur User-agent: *. Ergänzen Sie KI-Regeln erst danach.
section: platforms
locale: de
cluster: KI-Crawler nach Plattform
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu PrestaShop: Wo Traffic, SEO and URLs, Schaltfläche Generate robots.txt, User-agent nur Stern, Neu generieren Ersetzt die Datei
hero_sub: Einstellungen für KI-Crawler bei PrestaShop
hero_boxes: Wo|Traffic > SEO and URLs; Schaltfläche|Generate robots.txt; User-agent|nur *; Neu generieren|Ersetzt die Datei
widget: on
related: /de/platforms|Alle Plattformen im Vergleich; /de/platforms/shopify|Shopify; /de/bots|KI-Crawler im Vergleich; /de/guides/cms|Checkliste für KI-Sichtbarkeit bei Shopify, WooCommerce und mehr
answer: PrestaShops Benutzerhandbuch beschreibt ein Werkzeug Robots file generation unter Shop Parameters, Traffic, SEO and URLs. Es schreibt mit User-agent: * Ausschlussanweisungen für nicht öffentliche Dateien und nennt daher keinen KI-Crawler. Ein Klick auf Generate robots.txt ersetzt jede vorhandene Datei. Ergänzen Sie Ihre eigenen KI-Crawler-Regeln also erst nach dem Generieren.

## Wo die Einstellung bei PrestaShop liegt

Das Benutzerhandbuch von PrestaShop 8 führt sie unter Configuring your Shop Parameters auf, dann Traffic, dann SEO and URLs. Der Abschnitt heißt Robots file generation. Die Seite nennt darüber hinaus keinen Menüpfad im Back Office, und am Ende steht „Last updated 4 years ago“.

## Was nur PrestaShops Seite sagt und die anderer Plattformen nicht

PrestaShop gibt Ihnen kein Feld, in das Sie Regeln tippen. Es gibt Ihnen eine Schaltfläche, die die ganze Datei schreibt. Der Leitfaden sagt, der Generator „erstellt einfach eine Datei mit Ausschlussanweisungen für Dateien und Verzeichnisse, die nicht öffentlich sein sollen“, angewendet auf alle Bots über die Zeichenfolge „User-agent: *“. Er sagt auch, die schlimmsten Bots ignorierten die Datei, weil sie „rein beratend“ sei. Die Folge für KI-Crawler steht in den letzten beiden Sätzen des Abschnitts: Neu generieren löscht alles, was Sie ergänzt haben.

Mit den Worten des Anbieters (englisches Original): “Clicking on the "Generate robots.txt" button replaces any existing robots.txt file with a new one. Therefore, if you want to add your own rules, do it after PrestaShop has generated its version of the file.”

Quelle: [PrestaShop 8 User Guide: SEO and URLs](https://docs.prestashop-project.org/v.8-documentation/user-guide/configuring-shop/shop-parameters/traffic/seo-and-urls), gelesen am 24. Oktober 2026.

## Die Schritte

1. Öffnen Sie SEO and URLs im Bereich Traffic von Shop Parameters.
2. Gehen Sie zu Robots file generation.
3. Klicken Sie auf Generate robots.txt. Das ersetzt jede vorhandene robots.txt.
4. Ergänzen Sie Ihre eigenen Regeln, nachdem PrestaShop seine Version erzeugt hat. Die Seite sagt nicht, wie Sie die erzeugte Datei bearbeiten. Nutzen Sie daher den Dateizugriff, den Ihr Hosting bietet.
5. Öffnen Sie /robots.txt in Ihrem Shop, um zu prüfen, ob Ihre Regeln noch da sind. Wiederholen Sie Schritt 4 jedes Mal, wenn Sie die Schaltfläche erneut anklicken.

## Die passenden Zeilen

Zum Erlauben:

```
# Nothing to add: the generated file only lists files and directories that are not public.
# To name one explicitly, add after the generated block:
User-agent: OAI-SearchBot
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

Die erzeugte Datei spricht alle Bots gleich an, weil sie User-agent: * und sonst nichts verwendet. PrestaShops Werkzeug lässt Ihnen also keine Wahl pro Crawler. Der Leitfaden sagt, manchen Bots wollten Sie vollen Zugriff geben, etwa denen von Google, anderen nicht, etwa Spam-Bots und Content-Dieben. Diese Entscheidung treffen Sie in Ihren eigenen ergänzten Gruppen. Der Leitfaden erwähnt KI-Crawler überhaupt nicht beim Namen und verweist auch auf keine Einstellung und kein Modul für sie.

## Vergleich mit Shopify

[Shopify](/de/platforms/shopify): Eine Vorlage robots.txt.liquid, die Ihre Ergänzungen behält, während PrestaShops Schaltfläche sie überschreibt.

## Prüfen Sie Ihre eigene Website

Die kostenlose Prüfung im Feld oben liest die robots.txt für die KI-Crawler und sendet pro Crawler eine Live-Anfrage. So fällt eine Regel auf, die die Einstellungen Ihrer Plattform erlauben, eine Firewall aber ablehnt. Die vollständige Liste der Crawler finden Sie im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Löscht das Neu-Generieren der robots.txt in PrestaShop meine KI-Crawler-Regeln?

Ja, wenn Sie sie in der erzeugten Datei ergänzt haben. PrestaShops Leitfaden sagt, die Schaltfläche ersetze jede vorhandene robots.txt durch eine neue, und Sie sollten Ihre eigenen Regeln ergänzen, nachdem sie ihre Version erzeugt hat.

### Sperrt PrestaShop KI-Crawler standardmäßig?

Der Leitfaden sagt das nicht. Er beschreibt eine erzeugte Datei mit Ausschlussanweisungen für nicht öffentliche Dateien und Verzeichnisse unter User-agent: *, und er nennt keinen KI-Crawler.

## Sources

- [PrestaShop 8 User Guide: SEO and URLs](https://docs.prestashop-project.org/v.8-documentation/user-guide/configuring-shop/shop-parameters/traffic/seo-and-urls), gelesen am 24. Oktober 2026
