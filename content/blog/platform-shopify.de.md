title: Shopify: KI-Crawler steuern und was die robots.txt nicht erfasst
slug: shopify
description: Mit robots.txt.liquid erlauben oder sperren Sie KI-Crawler bei Shopify. Laut Shopify trifft eine Sperre nur das offene Web, nicht Produktdaten an ChatGPT.
section: platforms
locale: de
cluster: KI-Crawler nach Plattform
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Vier Fakten zu Shopify: Wo robots.txt.liquid, Support Von Shopify nicht unterstützt, Catalog-Feed Nicht erfasst, Wirkung Sofort
hero_sub: Einstellungen für KI-Crawler bei Shopify
hero_boxes: Wo|robots.txt.liquid; Support|Von Shopify nicht unterstützt; Catalog-Feed|Nicht erfasst; Wirkung|Sofort
widget: on
related: /de/platforms|Alle Plattformen im Vergleich; /de/platforms/squarespace|Squarespace; /de/bots|KI-Crawler im Vergleich; /de/guides/cms|Checkliste für KI-Sichtbarkeit bei Shopify, WooCommerce und mehr
answer: Bei Shopify steuern Sie KI-Crawler, indem Sie Ihrem Theme eine Vorlage robots.txt.liquid hinzufügen. Laut Shopifys Hilfeseite betrifft eine Sperre dort nur die Auffindbarkeit im offenen Web: Produktdaten gehen über Shopify Catalog weiterhin an agentische Storefronts wie ChatGPT oder Microsoft Copilot, unabhängig von /robots.txt.

## Wo die Einstellung bei Shopify liegt

Online Store, dann beim Theme Edit code, dann Add a new template und robots wählen. Shopify sagt, das sei eine nicht unterstützte Anpassung: Der Support könne bei Änderungen nicht helfen, und falsche Verwendung „kann zum Verlust des gesamten Traffics führen“.

## Was nur Shopifys Seite sagt und die anderer Plattformen nicht

Shopify beschreibt zwei Ebenen der Steuerung. Die Netzwerkebene übernimmt Shopify für Shops bei Shopify, Sie müssen nichts tun. Die Ebene /robots.txt gehört Ihnen über robots.txt.liquid. Die Seite zieht dann die Linie, die für einen Shop zählt: Wenn Sie über agentische Storefronts wie ChatGPT oder Microsoft Copilot verkaufen, werden Ihre Produktdaten „unabhängig von /robots.txt“ über Shopify Catalog verbreitet, und das Blockieren von KI-Crawlern auf einer der beiden Ebenen „betrifft nur die Auffindbarkeit im offenen Web“. Was Catalog teilt, ändern Sie über die Einstellungen der agentischen Storefronts, nicht über die robots.txt.

Mit den Worten des Anbieters (englisches Original): “Blocking AI crawlers at the /robots.txt or network layer affects only open-web discoverability. It doesn't stop your product data from being sent by Shopify Catalog to the agentic storefronts that you've activated.”

Quelle: [Shopify Help Center: Editing robots.txt.liquid](https://help.shopify.com/en/manual/promoting-marketing/seo/editing-robots-txt), gelesen am 21. Oktober 2026.

## Die Schritte

1. Gehen Sie in Ihrem Shopify-Admin zu Online Store.
2. Öffnen Sie beim veröffentlichten Theme das Menü und wählen Sie Edit code.
3. Klicken Sie auf Add a new template, wählen Sie robots und dann Create template.
4. Behalten Sie das Liquid bei, das die Standard-Regelgruppen ausgibt, und fügen Sie Ihre eigenen Regeln darunter hinzu. Shopify empfiehlt das gegenüber dem Ersetzen der Datei durch reinen Text, weil reiner Text veraltet.
5. Speichern Sie im veröffentlichten Theme. Shopify sagt, Änderungen wirkten sofort, Crawler reagierten aber nicht immer sofort.

## Die passenden Zeilen

Zum Erlauben:

```
# Nothing to add: Shopify's default robots.txt allows crawlers that are not named.
# To name one explicitly, add under the default Liquid block:
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

Zwei Details von derselben Seite. Ein Theme, das im Bereich Themes des Admin hochgeladen wird, übernimmt robots.txt.liquid nicht; bei Änderungen über ThemeKit oder die Kommandozeile bleibt sie erhalten. Und wenn Ihre Vorlage die Standardgruppen ausgibt, löschen Sie sie, um Shopifys aktuellen Standard zu übernehmen. Er kann Regeln enthalten, die Ihrer älteren Kopie fehlen, etwa Disallow: /search.

## Vergleich mit Squarespace

[Squarespace](/de/platforms/squarespace): Ein Kästchen statt einer Vorlage und eine feste Liste von 26 Namen.

## Prüfen Sie Ihre eigene Website

Die kostenlose Prüfung im Feld oben liest die robots.txt für die KI-Crawler und sendet pro Crawler eine Live-Anfrage. So fällt eine Regel auf, die die Einstellungen Ihrer Plattform erlauben, eine Firewall aber ablehnt. Die vollständige Liste der Crawler finden Sie im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Verhindert das Sperren von GPTBot bei Shopify, dass ChatGPT meine Produkte zeigt?

Nicht von allein. Shopify sagt, robots.txt und Netzwerksperren beträfen nur die Auffindbarkeit im offenen Web, und Shopify Catalog sende Produktdaten unabhängig von /robots.txt an die agentischen Storefronts, die Sie aktiviert haben. Um diesen Feed zu steuern, nutzen Sie Shopifys Einstellungen für agentische Storefronts.

### Kann der Shopify-Support meine robots.txt.liquid reparieren?

Nein. Shopifys Seite sagt, der Support könne bei Änderungen an der Datei nicht helfen, und empfiehlt, einen Shopify Partner zu beauftragen.

### Brauche ich einen Cloudflare-Proxy vor Shopify?

Shopify sagt, das Bot-Management auf Netzwerkebene werde für Shops bei Shopify übernommen, und es empfehle keine Proxy-Konfiguration vor Shopify und unterstütze auch keine.

## Sources

- [Shopify Help Center: Editing robots.txt.liquid](https://help.shopify.com/en/manual/promoting-marketing/seo/editing-robots-txt), gelesen am 21. Oktober 2026
- [Shopify.dev: Customize robots.txt.liquid](https://shopify.dev/docs/storefronts/themes/seo/robots-txt), gelesen am 21. Oktober 2026
