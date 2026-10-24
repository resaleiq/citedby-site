title: Perplexity-User: Aufgabe und Wirkung einer Sperre
h1: Perplexity-User: Aufgabe und Wirkung einer Sperre
description: Perplexity-User (Perplexity): Vom Nutzer ausgelöster Abruf. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage.
slug: perplexity-user
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu Perplexity-User: Betreiber Perplexity, Aufgabe Vom Nutzer ausgelöster Abruf, befolgt robots.txt Nicht immer, Adressliste 4 Bereiche
hero_sub: Perplexity-User, betrieben von Perplexity
hero_boxes: Betreiber|Perplexity; Aufgabe|Vom Nutzer ausgelöster Abruf; Befolgt robots.txt|Nicht immer; Adressliste|4 Bereiche
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/perplexitybot|PerplexityBot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: Perplexity-User ist Perplexitys Fetcher für Nutzeraktionen: Stellt ein Nutzer eine Frage, kann Perplexity-User eine Seite besuchen, um genau zu antworten, und auf sie verlinken. Laut Perplexity wird er weder zum Web-Crawling noch zum Training von KI-Modellen verwendet und ignoriert robots.txt-Regeln in der Regel, weil ein Nutzer den Abruf angefordert hat.

## Was Perplexity-User ist

Perplexity-User ist Perplexitys Fetcher für Nutzeraktionen. Wenn ein Nutzer Perplexity eine Frage stellt, kann Perplexity-User eine Webseite besuchen, um eine genaue Antwort zu liefern, und in der Antwort einen Link auf die Seite aufnehmen. Laut Perplexity wird er weder zum Web-Crawling noch zum Sammeln von Inhalten für das Training von KI-Foundation-Modellen verwendet, und er ist von PerplexityBot getrennt, der Websites in den Perplexity-Suchergebnissen anzeigt und verlinkt.

| Angabe | Perplexity-User |
| --- | --- |
| Betreiber | Perplexity |
| Aufgabe | Vom Nutzer ausgelöster Abruf |
| robots.txt-Token | `Perplexity-User` |
| Befolgt robots.txt | Ignoriert robots.txt-Regeln in der Regel, weil ein Nutzer den Abruf angefordert hat |
| IP-Adressen | 4 Bereiche (www.perplexity.com/perplexity-user.json, Datei vom 2025-10-17) |
| Seite des Betreibers gelesen am | 24. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “Since a user requested the fetch, this fetcher generally ignores robots.txt rules.”

Quelle: [Perplexity: Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers), gelesen am 24. Oktober 2026.

## Was passiert, wenn Sie Perplexity-User sperren

Perplexity führt Perplexity-User als robots.txt-Token auf und sagt, es steuere, auf welche Websites diese Nutzeranfragen zugreifen können. Perplexity sagt außerdem, dass dieser Fetcher robots.txt-Regeln in der Regel ignoriert, weil ein Nutzer den Abruf angefordert hat. Laut Perplexity wirkt jede seiner robots.txt-Einstellungen unabhängig, und Änderungen können bis zu 24 Stunden brauchen.

## Die robots.txt-Zeilen

So erlauben Sie Perplexity-User:

```
User-agent: Perplexity-User
Allow: /
```

So sperren Sie Perplexity-User:

```
User-agent: Perplexity-User
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Perplexity-User/1.0; +https://perplexity.ai/perplexity-user)
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Die Datei www.perplexity.com/perplexity-user.json enthielt am 24. Oktober 2026 4 Bereiche, Datei vom 2025-10-17.

Perplexity veröffentlicht die IP-Adressen von Perplexity-User als JSON-Datei und sagt, man solle sie zusammen mit dem User-Agent-String als maßgebliche Quelle für Allow-Regeln verwenden.

## Vergleich mit PerplexityBot

[PerplexityBot](/de/bots/perplexitybot): PerplexityBot zeigt Websites in den Perplexity-Suchergebnissen an und verlinkt sie, während Perplexity-User eine Seite abruft, wenn die Frage eines Nutzers sie braucht, und robots.txt in der Regel ignoriert.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). Perplexity-User gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `Perplexity-User` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt Perplexity-User die robots.txt?

Ignoriert robots.txt-Regeln in der Regel, weil ein Nutzer den Abruf angefordert hat. Eine Regel für Perplexity-User in der robots.txt hält ihn deshalb möglicherweise nicht auf. Um ihn sicher abzuweisen, nutzen Sie eine Firewall- oder CDN-Regel, die User-Agent und veröffentlichte Adressen kombiniert.

### Woher weiß ich, dass Perplexity-User wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Perplexity: Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers)
- [Perplexity: Perplexity-User IP addresses JSON (read 2026-10-24)](https://www.perplexity.com/perplexity-user.json)
