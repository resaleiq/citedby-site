title: DuckAssistBot: Aufgabe und Wirkung einer Sperre
h1: DuckAssistBot: Aufgabe und Wirkung einer Sperre
description: DuckAssistBot (DuckDuckGo): Vom Nutzer ausgelöster Abruf. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage.
slug: duckassistbot
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Vier Fakten zu DuckAssistBot: Betreiber DuckDuckGo, Aufgabe Vom Nutzer ausgelöster Abruf, befolgt robots.txt Ja, Adressliste 486 Adressen
hero_sub: DuckAssistBot, betrieben von DuckDuckGo
hero_boxes: Betreiber|DuckDuckGo; Aufgabe|Vom Nutzer ausgelöster Abruf; Befolgt robots.txt|Ja; Adressliste|486 Adressen
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/amazonbot|Amazonbot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: DuckAssistBot crawlt Seiten in Echtzeit für die KI-gestützten Antworten von DuckDuckGo, die ihre Quellen nennen. Laut DuckDuckGo werden die Daten nicht zum Training von KI-Modellen verwendet. Ein Disallow in robots.txt wirkt nach 72 Stunden und beeinflusst das organische Suchranking nicht. DuckDuckGo nennt 486 IP-Adressen.

## Was DuckAssistBot ist

DuckDuckGo betreibt zwei Bots, die oft verwechselt werden. DuckDuckBot ist der Such-Crawler, DuckAssistBot steckt hinter den KI-gestützten Antworten. Laut der Hilfeseite von DuckDuckGo nennen die Antworten ihre Quellen gut sichtbar, und die gecrawlten Daten werden nicht zum Training von KI-Modellen verwendet.

| Angabe | DuckAssistBot |
| --- | --- |
| Betreiber | DuckDuckGo |
| Aufgabe | Echtzeit-Abruf für KI-gestützte Antworten |
| robots.txt-Token | `DuckAssistBot` |
| Befolgt robots.txt | Ja, eine Änderung wirkt nach 72 Stunden |
| IP-Adressen | 486 Adressen (duckduckgo.com/duckassistbot.json, Datei vom 2026-09-01) |
| Seite des Betreibers gelesen am | 21. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “DuckAssistBot is a web crawler for DuckDuckGo Search that crawls pages in real-time for our AI-assisted answers, which prominently cite their sources. This data is not used in any way to train AI models.”

Quelle: [DuckDuckGo Help Pages: About DuckAssistBot](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot), gelesen am 21. Oktober 2026.

## Was passiert, wenn Sie DuckAssistBot sperren

DuckDuckGo sagt, dass eine Änderung nach 72 Stunden wirksam wird, sobald Sie DuckAssistBot per Disallow ausschließen, und dass der Opt-out das organische Suchranking nicht beeinflusst und nicht darüber entscheidet, ob Websites in den Suchergebnissen erscheinen. Die Kosten einer Sperre beschränken sich also auf die KI-gestützten Antworten und deren Quellenangaben. Probleme mit dem Opt-out gehen an die Adresse, die die Seite nennt: crawling@duckduckgo.com.

## Die robots.txt-Zeilen

So erlauben Sie DuckAssistBot:

```
User-agent: DuckAssistBot
Allow: /
```

So sperren Sie DuckAssistBot:

```
User-agent: DuckAssistBot
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
DuckAssistBot/1.2; (+http://duckduckgo.com/duckassistbot.html)
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

DuckDuckGo listet die Adressen im Hilfeartikel und als JSON unter duckduckgo.com/duckassistbot.json auf. Die Datei enthielt am 21. Oktober 2026 486 Einträge, Erstellungszeit 2026-09-01. Das ist länger als jede andere Adressliste, die wir für diese Auswahl gezählt haben, und sie enthält einzelne Adressen, wo die anderen CIDR-Bereiche veröffentlichen. Der User-Agent erscheint als `DuckAssistBot/1.2`.

## Vergleich mit Amazonbot

[Amazonbot](/de/bots/amazonbot): Amazons Familie aus drei Agenten, von denen einer robots.txt möglicherweise ignoriert.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). DuckAssistBot gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `DuckAssistBot` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt DuckAssistBot die robots.txt?

Ja, eine Änderung wirkt nach 72 Stunden. Geben Sie DuckAssistBot in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass DuckAssistBot wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [DuckDuckGo Help Pages: About DuckAssistBot](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot)
- [duckduckgo.com/duckassistbot.json](https://duckduckgo.com/duckassistbot.json)
