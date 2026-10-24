title: Wix: KI-Crawler im Robots.txt Editor sperren (vier Namen)
slug: wix
description: Wix' Hilfeseite sagt, Sie sollen vier User-Agents in den Robots.txt Editor einfügen. Wo der Editor liegt, was das Beispiel auslässt und die Option nosnippet.
section: platforms
locale: de
cluster: KI-Crawler nach Plattform
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Vier Fakten zu Wix: Wo Robots.txt Editor, Beispielnamen 4, Auf Seitenebene nosnippet-Tag, Support Nicht für Änderungen
hero_sub: Einstellungen für KI-Crawler bei Wix
hero_boxes: Wo|Robots.txt Editor; Beispielnamen|4; Auf Seitenebene|nosnippet-Tag; Support|Nicht für Änderungen
widget: on
related: /de/platforms|Alle Plattformen im Vergleich; /de/platforms/webflow|Webflow; /de/bots|KI-Crawler im Vergleich; /de/guides/cms|Checkliste für KI-Sichtbarkeit bei Shopify, WooCommerce und mehr
answer: Wix lässt Sie die robots.txt bearbeiten: SEO & GEO im Dashboard, dann Tools and settings, dann Robots.txt Editor. Die Hilfeseite fügt vier zu sperrende Namen ein: CCBot, GPTBot, ChatGPT-User und BingAI. ClaudeBot, PerplexityBot und Google-Extended fehlen in diesem Beispiel. Ergänzen Sie sie selbst, wenn Sie sie sperren möchten.

## Wo die Einstellung bei Wix liegt

Gehen Sie im Dashboard Ihrer Site zu SEO & GEO, scrollen Sie zu Tools and settings, klicken Sie auf Robots.txt Editor und dann auf View File. Wix' separate Anleitung zum Bearbeiten nennt das eine fortgeschrittene Funktion und sagt, der Wix Customer Care könne bei Änderungen, die Sie an der Datei vornehmen, nicht helfen.

## Das Beispiel sperrt vier Namen, und einer davon steht nicht auf Bings Liste

Wix' Hilfeseite sagt, ihre Liste „enthält einige bekannte KI-Crawler, aber Sie können jederzeit weitere hinzufügen“. Die vier, die sie ausgibt, sind CCBot, GPTBot, ChatGPT-User und BingAI. Es fehlen die Tokens von Anthropic, Perplexity, Google und Meta, die auf unseren anderen Seiten vorkommen. „BingAI“ fällt aus der Reihe: Microsofts Seite dazu, welche Crawler Bing nutzt, am selben Tag gelesen, führt Bingbot, AdIdxBot, BingPreview, MicrosoftPreview und BingVideoPreview auf, aber kein BingAI. Eine Regel für einen Namen, den kein Crawler verwendet, bewirkt nichts. Behandeln Sie Wix' Liste daher als Ausgangspunkt und gleichen Sie sie mit der Seite des jeweiligen Anbieters ab. Beachten Sie auch: [ChatGPT-User](/de/bots/chatgpt-user) ist der Fetcher, der eine Seite öffnet, wenn eine Person ChatGPT fragt. Wenn Sie ihn sperren, entfällt dieser Weg zu Ihren Seiten.

Mit den Worten des Anbieters (englisches Original): “This list includes some known AI crawlers, but you can always add more as needed.”

Quelle: [Wix Help Center: Blocking AI Crawlers from Your Site](https://support.wix.com/en/article/blocking-ai-crawlers-from-your-site), gelesen am 21. Oktober 2026.

## Die Schritte

1. Gehen Sie im Dashboard Ihrer Site zu SEO & GEO.
2. Scrollen Sie zu Tools and settings und klicken Sie auf Robots.txt Editor.
3. Klicken Sie auf View File und dann auf das Feld unter Your robots.txt file.
4. Fügen Sie die Anweisungen unter This is your current file hinzu, dann Save Changes und Save.
5. Nur für eine einzelne Seite: Öffnen Sie bei der Seite SEO basics, Advanced SEO, Robots meta tag und setzen Sie das Häkchen bei nosnippet. Wix sagt, das verhindere, dass der Inhalt als direkte Eingabe für KI-Übersichten verwendet wird.

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
User-agent: CCBot
Disallow: /

User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /
```

## Stolperfallen

Wix' FAQ sagt, das Blockieren von KI-Crawlern in der robots.txt könne die NLWeb-Funktionalität einschränken, weil KI-Agenten Zugriff auf Ihre strukturierten Inhalte brauchen. Sie sagt auch, manche Crawler ignorierten die robots.txt, eine Sperre sei also nicht lückenlos.

## Vergleich mit Webflow

[Webflow](/de/platforms/webflow): Ebenfalls ein robots.txt-Editor, dazu ein Content-Signal-Header.

## Prüfen Sie Ihre eigene Website

Die kostenlose Prüfung im Feld oben liest die robots.txt für die KI-Crawler und sendet pro Crawler eine Live-Anfrage. So fällt eine Regel auf, die die Einstellungen Ihrer Plattform erlauben, eine Firewall aber ablehnt. Die vollständige Liste der Crawler finden Sie im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Schadet das Sperren von KI-Crawlern meiner SEO bei Wix?

Wix sagt, das Sperren bestimmter KI-Crawler sollte die SEO nicht wesentlich beeinträchtigen, und empfiehlt, danach Ihre Analytics zu prüfen.

### Ist BingAI ein echter Crawler?

Er steht nicht auf Microsofts aktueller Liste der Bing-Crawler, die Bingbot, AdIdxBot, BingPreview, MicrosoftPreview und BingVideoPreview nennt. Siehe die [Bingbot-Seite](/de/bots/bingbot).

### Blockiert nosnippet KI-Crawler?

Wix beschreibt es als Mittel, das verhindert, dass Ihr Inhalt als direkte Eingabe für KI-Übersichten verwendet wird. Es ist ein Tag auf Seitenebene, keine Crawler-Sperre.

## Sources

- [Wix Help Center: Blocking AI Crawlers from Your Site](https://support.wix.com/en/article/blocking-ai-crawlers-from-your-site), gelesen am 21. Oktober 2026
- [Wix Help Center: Editing Your Site's Robots.txt File](https://support.wix.com/en/article/editing-your-sites-robotstxt-file), gelesen am 21. Oktober 2026
- [Microsoft Bing Webmaster help: Which Crawlers Does Bing Use?](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0), gelesen am 21. Oktober 2026
