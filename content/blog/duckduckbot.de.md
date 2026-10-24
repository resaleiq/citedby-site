title: DuckDuckBot: Aufgabe und Wirkung einer Sperre
h1: DuckDuckBot: Aufgabe und Wirkung einer Sperre
description: DuckDuckBot (DuckDuckGo): Suche. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: duckduckbot
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu DuckDuckBot: Betreiber DuckDuckGo, Aufgabe Suche, befolgt robots.txt Ja, Adressliste 486 Adressen
hero_sub: DuckDuckBot, betrieben von DuckDuckGo
hero_boxes: Betreiber|DuckDuckGo; Aufgabe|Suche; Befolgt robots.txt|Ja; Adressliste|486 Adressen
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/duckassistbot|DuckAssistBot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: DuckDuckBot ist der Web-Crawler von DuckDuckGo, dessen erklärte Aufgabe es ist, die Suchergebnisse von DuckDuckGo zu verbessern. Laut DuckDuckGo respektiert er WWW::RobotRules und veröffentlicht seine IP-Adressen als Liste im JSON-Format. DuckAssistBot, der Abrufer für KI-gestützte Antworten, ist auf einer eigenen Hilfeseite von DuckDuckGo dokumentiert.

## Was DuckDuckBot ist

DuckDuckBot ist der Web-Crawler von DuckDuckGo. Laut DuckDuckGo besteht seine Aufgabe darin, die Suchergebnisse von DuckDuckGo zu verbessern. In den Hilfeseiten von DuckDuckGo ist DuckAssistBot auf einer eigenen Seite aufgeführt.

| Angabe | DuckDuckBot |
| --- | --- |
| Betreiber | DuckDuckGo |
| Aufgabe | Suche |
| robots.txt-Token | `DuckDuckBot` |
| Befolgt robots.txt | Ja, respektiert WWW::RobotRules (keine Angabe zur Zeitdauer veröffentlicht) |
| IP-Adressen | 486 Adressen (duckduckgo.com/duckduckbot.json, Datei vom 2026-09-01) |
| Seite des Betreibers gelesen am | 24. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “DuckDuckBot’s job is to constantly improve our search results and offer users the best and most secure search experience possible.”

Quelle: [DuckDuckGo Help Pages: Is DuckDuckBot related to DuckDuckGo?](https://duckduckgo.com/duckduckgo-help-pages/results/duckduckbot), gelesen am 24. Oktober 2026.

## Was passiert, wenn Sie DuckDuckBot sperren

DuckDuckGo sagt, DuckDuckBot respektiere WWW::RobotRules, daher gilt eine an DuckDuckBot gerichtete Disallow-Regel in robots.txt für diesen Crawler. Die Seite sagt nichts dazu, was eine Sperre an den DuckDuckGo-Ergebnissen ändert, und nichts zu DuckAssistBot.

## Die robots.txt-Zeilen

So erlauben Sie DuckDuckBot:

```
User-agent: DuckDuckBot
Allow: /
```

So sperren Sie DuckDuckBot:

```
User-agent: DuckDuckBot
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
DuckDuckBot/1.1; (+http://duckduckgo.com/duckduckbot.html)
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Die Datei duckduckgo.com/duckduckbot.json enthielt am 24. Oktober 2026 486 Adressen, Datei vom 2026-09-01.

DuckDuckGo sagt, der Crawler stamme von den IP-Adressen auf seiner Hilfeseite, die es auch als JSON unter duckduckgo.com/duckduckbot.json gibt.

## Vergleich mit DuckAssistBot

[DuckAssistBot](/de/bots/duckassistbot): DuckDuckBot ist der Crawler für die Suchergebnisse von DuckDuckGo, während DuckAssistBot von DuckDuckGo auf einer eigenen Hilfeseite dokumentiert ist.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). DuckDuckBot gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `DuckDuckBot` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt DuckDuckBot die robots.txt?

Ja, respektiert WWW::RobotRules (keine Angabe zur Zeitdauer veröffentlicht). Geben Sie DuckDuckBot in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass DuckDuckBot wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [DuckDuckGo Help Pages: Is DuckDuckBot related to DuckDuckGo?](https://duckduckgo.com/duckduckgo-help-pages/results/duckduckbot)
- [DuckDuckBot IP list (JSON, creationTime 2026-09-01, read 2026-10-24)](https://duckduckgo.com/duckduckbot.json)
