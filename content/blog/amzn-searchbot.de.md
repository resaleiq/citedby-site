title: Amzn-SearchBot: Aufgabe und Wirkung einer Sperre
h1: Amzn-SearchBot: Aufgabe und Wirkung einer Sperre
description: Amzn-SearchBot (Amazon): Suche. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: amzn-searchbot
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu Amzn-SearchBot: Betreiber Amazon, Aufgabe Suche, befolgt robots.txt Ja, Adressliste Liste auf seiner Seite
hero_sub: Amzn-SearchBot, betrieben von Amazon
hero_boxes: Betreiber|Amazon; Aufgabe|Suche; Befolgt robots.txt|Ja; Adressliste|Liste auf seiner Seite
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/amazonbot|Amazonbot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: Amzn-SearchBot ist ein Amazon-Crawler, der Suchfunktionen wie Alexa verbessern soll. Laut Amazon kommen Ihre Inhalte dort für die Anzeige infrage, wenn Sie ihn zulassen, und er crawlt nicht für das Training generativer KI-Modelle. Seine Einstellung gilt unabhängig von Amazonbot und Amzn-User, eine Änderung kann etwa 24 Stunden dauern.

## Was Amzn-SearchBot ist

Amzn-SearchBot ist ein Amazon-Crawler, der Suchfunktionen in Amazon-Produkten und -Diensten verbessern soll. Laut Amazon kommen Ihre Inhalte in Suchfunktionen wie Alexa infrage, wenn Sie ihn zulassen, und er crawlt keine Inhalte für das Training generativer KI-Modelle. Er ist einer von drei Amazon-User-Agents (Amazonbot, Amzn-SearchBot, Amzn-User), die Amazon auf einer Seite dokumentiert.

| Angabe | Amzn-SearchBot |
| --- | --- |
| Betreiber | Amazon |
| Aufgabe | Suche |
| robots.txt-Token | `Amzn-SearchBot` |
| Befolgt robots.txt | Ja, Änderungen können etwa 24 Stunden dauern |
| IP-Adressen | Liste auf der Seite des Betreibers (developer.amazon.com/amazonbot/searchbot-ip-addresses) |
| Seite des Betreibers gelesen am | 24. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “If robots.txt files don’t mention Amzn-SearchBot but allow other search bots, Amzn-SearchBot will crawl in accordance with the robots.txt directives given to other search bots.”

Quelle: [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot), gelesen am 24. Oktober 2026.

## Was passiert, wenn Sie Amzn-SearchBot sperren

Amazon sagt, dass automatisiertes Crawling durch die aufgeführten User-Agents das Robots Exclusion Protocol respektiert und die Anweisungen zu User-Agent sowie Allow und Disallow befolgt. Laut Amazon gilt die Einstellung jedes User-Agents unabhängig von den anderen und kann etwa 24 Stunden brauchen, bis sie wirkt. Erwähnt robots.txt Amzn-SearchBot nicht, lässt aber andere Suchbots zu, folgt er den Anweisungen für diese anderen Suchbots.

## Die robots.txt-Zeilen

So erlauben Sie Amzn-SearchBot:

```
User-agent: Amzn-SearchBot
Allow: /
```

So sperren Sie Amzn-SearchBot:

```
User-agent: Amzn-SearchBot
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Amzn-SearchBot/0.1) Chrome/W.X.Y.Z Safari/537.36
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Amazon veröffentlicht die IP-Adressen von Amzn-SearchBot auf einer Webseite, die die Liste als JSON zeigt, und verlinkt sie von der Dokumentationsseite zu Amazonbot.

## Vergleich mit Amazonbot

[Amazonbot](/de/bots/amazonbot): Amazonbot dient dazu, Amazon-Produkte und -Dienste zu verbessern, und kann zum Training von KI-Modellen von Amazon eingesetzt werden. Amzn-SearchBot ist für Suchfunktionen gedacht, und laut Amazon crawlt er nicht für das Training generativer KI-Modelle.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). Amzn-SearchBot gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `Amzn-SearchBot` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt Amzn-SearchBot die robots.txt?

Ja, Änderungen können etwa 24 Stunden dauern. Geben Sie Amzn-SearchBot in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass Amzn-SearchBot wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot)
- [Amazon: Amzn-SearchBot IP addresses (read 2026-10-24)](https://developer.amazon.com/amazonbot/searchbot-ip-addresses/)
