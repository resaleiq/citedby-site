title: Amazonbot: Aufgabe und Wirkung einer Sperre
h1: Amazonbot: Aufgabe und Wirkung einer Sperre
description: Amazonbot (Amazon): Mehrere Aufgaben. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: amazonbot
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Vier Fakten zu Amazonbot: Betreiber Amazon, Aufgabe Mehrere Aufgaben, befolgt robots.txt Ja, Adressliste Liste auf seiner Seite
hero_sub: Amazonbot, betrieben von Amazon
hero_boxes: Betreiber|Amazon; Aufgabe|Mehrere Aufgaben; Befolgt robots.txt|Ja; Adressliste|Liste auf seiner Seite
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/duckassistbot|DuckAssistBot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: Amazonbot dient dazu, Amazon-Produkte und -Dienste zu verbessern, und kann zum Training von KI-Modellen von Amazon eingesetzt werden. Auf Amazons Seite stehen auch Amzn-SearchBot, durch den Inhalte für Suchfunktionen wie Alexa infrage kommen, und Amzn-User, der möglicherweise nicht alle robots.txt-Anweisungen befolgt. Jede Einstellung gilt unabhängig von den anderen.

## Was Amazonbot ist

Amazons Seite behandelt drei User-Agents: Amazonbot, Amzn-SearchBot und Amzn-User. Laut Amazon gilt jede Einstellung unabhängig von den anderen und kann etwa 24 Stunden brauchen, bis sie wirkt. Nur beim ersten heißt es, dass er möglicherweise KI-Modelle von Amazon trainiert.

| Angabe | Amazonbot |
| --- | --- |
| Betreiber | Amazon |
| Aufgabe | Produktverbesserung, kann KI-Modelle von Amazon trainieren |
| robots.txt-Token | `Amazonbot` |
| Befolgt robots.txt | Ja, Änderungen brauchen etwa 24 Stunden |
| IP-Adressen | Liste auf der Seite des Betreibers (developer.amazon.com/amazonbot/ip-addresses) |
| Seite des Betreibers gelesen am | 21. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “Amazonbot is used to improve our products and services. This helps us provide more accurate information to customers and may be used to train Amazon AI models.”

Quelle: [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot), gelesen am 21. Oktober 2026.

## Was passiert, wenn Sie Amazonbot sperren

Amzn-SearchBot ist für Suchfunktionen wie Alexa gedacht: Wenn Sie ihn zulassen, kommen Ihre Inhalte dort für die Anzeige infrage. Amzn-User beantwortet Live-Anfragen an Alexa, die aktuelle Informationen brauchen. Laut Amazon befolgt er möglicherweise nicht alle robots.txt-Anweisungen und crawlt nicht für das Training generativer KI. Eine robots.txt, die nur Amazonbot nennt, beschreibt deshalb Ihre Regeln für die beiden anderen nicht.

## Die robots.txt-Zeilen

So erlauben Sie Amazonbot:

```
User-agent: Amazonbot
Allow: /
```

So sperren Sie Amazonbot:

```
User-agent: Amazonbot
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Amazonbot/0.1) Chrome/W.X.Y.Z Safari/537.36
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Amazon veröffentlicht die Adressen für Amazonbot und, auf eigenen Seiten, für Amzn-SearchBot und für Live-Abrufe. Die Listen sind HTML-Seiten, keine JSON-Datei, deshalb nennen wir keine Anzahl. Amazon sagt außerdem: Wenn robots.txt Amzn-SearchBot nicht erwähnt, aber andere Suchbots zulässt, crawlt Amzn-SearchBot nach dieser Datei.

## Vergleich mit DuckAssistBot

[DuckAssistBot](/de/bots/duckassistbot): Ein weiterer Abruf-Bot für KI-Antworten mit angegebenem Opt-out und 72 Stunden Verzögerung.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). Amazonbot gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `Amazonbot` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt Amazonbot die robots.txt?

Ja, Änderungen brauchen etwa 24 Stunden. Geben Sie Amazonbot in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass Amazonbot wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot)
- [developer.amazon.com/amazonbot/ip-addresses](https://developer.amazon.com/amazonbot/ip-addresses)
