title: Squarespace: KI-Crawler-Kästchen sperrt 26 Bots, nicht ChatGPT
slug: squarespace
description: Squarespaces Bereich Crawlers hat ein Kästchen für bekannte KI-Crawler. Die 26 Namen in der robots.txt lassen ChatGPTs Such- und User-Bots aus.
section: platforms
locale: de
cluster: KI-Crawler nach Plattform
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Vier Fakten zu Squarespace: Wo Settings, Crawlers, Gesperrte Namen 26, robots.txt bearbeiten Nein, Früheres Training Nicht entfernt
hero_sub: Einstellungen für KI-Crawler bei Squarespace
hero_boxes: Wo|Settings, Crawlers; Gesperrte Namen|26; robots.txt bearbeiten|Nein; Früheres Training|Nicht entfernt
widget: on
related: /de/platforms|Alle Plattformen im Vergleich; /de/platforms/wix|Wix; /de/bots|KI-Crawler im Vergleich; /de/guides/cms|Checkliste für KI-Sichtbarkeit bei Shopify, WooCommerce und mehr
answer: Squarespace hat ein einziges Kästchen: Settings, dann Crawlers, dann Block known artificial intelligence crawlers. Es trägt 26 benannte Bots in Ihre robots.txt ein. Die Liste enthält GPTBot, ClaudeBot und DuckAssistBot, aber nicht OAI-SearchBot, ChatGPT-User oder PerplexityBot, und Sie können die robots.txt nicht selbst bearbeiten.

## Wo die Einstellung bei Squarespace liegt

Öffnen Sie das Panel Settings, klicken Sie auf Crawlers und setzen Sie das Häkchen bei Block known artificial intelligence crawlers. Squarespaces Seite sagt, das Häkchen aktualisiere Ihre robots.txt für die unten aufgeführten Bots, und es könnten mit der Zeit weitere hinzukommen.

## Die 26 Namen, und welche fehlen

Squarespaces Hilfeseite listet genau 26 Namen auf: AI2Bot, Ai2Bot-Dolma, aiHitBot, Amazonbot, anthropic-ai, Applebot-Extended, Bytespider, CCBot, ClaudeBot, cohere-ai, cohere-training-data-crawler, DuckAssistBot, FacebookBot, Google-Extended, GoogleOther, GoogleOther-Image, GoogleOther-Video, GPTBot, img2dataset, Meta-ExternalAgent, MyCentralAIScraperBot, omgili, omgilibot, Quora-Bot, TikTokSpider und YouBot. Im Vergleich mit unseren eigenen Crawler-Seiten deckt das Kästchen die Trainings- und Datensatz-Crawler von OpenAI, Anthropic, Google, Apple, Meta und Common Crawl ab. Es nennt nicht [OAI-SearchBot](/de/bots/oai-searchbot), [ChatGPT-User](/de/bots/chatgpt-user), [PerplexityBot](/de/bots/perplexitybot), [Claude-SearchBot](/de/bots/claude-searchbot) oder [Claude-User](/de/bots/claude-user). Mit dem Häkchen verschwinden Sie also nicht aus der ChatGPT-Suche. Es nennt dagegen [DuckAssistBot](/de/bots/duckassistbot) und [Amazonbot](/de/bots/amazonbot), Crawler für KI-Antworten und für Produkte. Das Häkchen kann Sie daher auch die KI-Antworten von DuckDuckGo kosten.

Mit den Worten des Anbieters (englisches Original): “Checking the box updates your robots.txt file to tell the following bots not to crawl your site.”

Quelle: [Squarespace Help: Request that AI models exclude your site](https://support.squarespace.com/hc/en-us/articles/360022347072-Request-that-AI-models-exclude-your-site), gelesen am 21. Oktober 2026.

## Die Schritte

1. Öffnen Sie das Panel Settings Ihrer Squarespace-Site.
2. Klicken Sie auf Crawlers.
3. Setzen Sie das Häkchen bei Block known artificial intelligence crawlers, um die 26 Namen zu sperren, oder lassen Sie es leer, damit alle erlaubt bleiben.
4. Um einen weiteren Bot hinzufügen zu lassen, wenden Sie sich an Squarespace: Der Text der Seite selbst sagt, dass Sie das anfragen können.

## Die passenden Zeilen

Zum Erlauben:

```
# Squarespace sites are open to these crawlers while the box is unticked.
# You cannot add lines yourself, so there is nothing to paste.
```

Zum Sperren:

```
# Written by Squarespace when the box is ticked (excerpt):
User-agent: GPTBot
User-agent: ClaudeBot
User-agent: CCBot
Disallow: /
```

## Stolperfallen

Squarespace erklärt, dass das Häkchen keine Inhalte rückwirkend aus den Trainingsdaten von KI-Modellen entfernt, die bereits von Ihrer Site gesammelt wurden. Es sagt auch, die robots.txt sei nur eine Bitte, die freundliche Crawler zu befolgen angeboten hätten. Der Auszug oben ist unsere verkürzte Veranschaulichung der Art von Zeilen, die das Kästchen erzeugt. Die genaue Datei ist das, was Ihre Site unter /robots.txt ausliefert. Öffnen Sie sie also und lesen Sie sie.

## Vergleich mit Wix

[Wix](/de/platforms/wix): Ein echter robots.txt-Editor und eine Beispielliste mit vier Namen.

## Prüfen Sie Ihre eigene Website

Die kostenlose Prüfung im Feld oben liest die robots.txt für die KI-Crawler und sendet pro Crawler eine Live-Anfrage. So fällt eine Regel auf, die die Einstellungen Ihrer Plattform erlauben, eine Firewall aber ablehnt. Die vollständige Liste der Crawler finden Sie im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Kann ich bei Squarespace die ChatGPT-Suche erlauben, aber das Training sperren?

Teilweise. Das Häkchen schreibt eine Regel für GPTBot, und OAI-SearchBot gehört nicht zu den 26 Namen. Sie können keine eigenen Zeilen hinzufügen. Öffnen Sie daher Ihre aktuelle /robots.txt, um zu bestätigen, was darin steht.

### Kann ich die robots.txt bei Squarespace bearbeiten?

Squarespaces eigene Seite behandelt das Panel Crawlers als die Steuerung und bietet keinen robots.txt-Editor. Wix und Webflow bieten einen.

### Verhindert das Kästchen, dass Google meine Site indexiert?

Nein. Es ist von der Option für Suchmaschinen-Crawler im selben Panel getrennt. Das KI-Kästchen nennt Google-Extended und GoogleOther, nicht Googlebot.

## Sources

- [Squarespace Help: Request that AI models exclude your site](https://support.squarespace.com/hc/en-us/articles/360022347072-Request-that-AI-models-exclude-your-site), gelesen am 21. Oktober 2026
