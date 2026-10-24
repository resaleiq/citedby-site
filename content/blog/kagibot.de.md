title: Kagibot: Aufgabe und Wirkung einer Sperre
h1: Kagibot: Aufgabe und Wirkung einer Sperre
description: Kagibot (Kagi): Suche. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: kagibot
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu Kagibot: Betreiber Kagi, Aufgabe Suche, befolgt robots.txt Ja, Adressliste Liste auf seiner Seite
hero_sub: Kagibot, betrieben von Kagi
hero_boxes: Betreiber|Kagi; Aufgabe|Suche; Befolgt robots.txt|Ja; Adressliste|Liste auf seiner Seite
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/googlebot|Googlebot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: Kagibot ist der Web-Crawler der Suchmaschine Kagi. Laut Kagi werden Standard-robots.txt-Anweisungen respektiert, die Kagibot betreffen, und wenn keine Regel Kagibot betrifft, aber eine Googlebot, folgt Kagibot den Anweisungen für Googlebot. Kagi veröffentlicht seinen User-Agent-String und die IP-Adressen, von denen seine Anfragen kommen.

## Was Kagibot ist

Kagibot ist der Web-Crawler der Suchmaschine Kagi. Kagi veröffentlicht seinen User-Agent-String und die IP-Adressen, von denen Kagibot-Anfragen ausgehen.

| Angabe | Kagibot |
| --- | --- |
| Betreiber | Kagi |
| Aufgabe | Suche |
| robots.txt-Token | `Kagibot` |
| Befolgt robots.txt | Ja, Standard-robots.txt-Anweisungen, die Kagibot betreffen, werden respektiert |
| IP-Adressen | Liste auf der Seite des Betreibers (kagi.com/bot) |
| Seite des Betreibers gelesen am | 24. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “Standard directives in robots.txt that target Kagibot are respected.”

Quelle: [Kagi: About KagiBot](https://kagi.com/bot), gelesen am 24. Oktober 2026.

## Was passiert, wenn Sie Kagibot sperren

Kagi sagt, dass Standard-robots.txt-Anweisungen, die Kagibot betreffen, respektiert werden, zum Beispiel Disallow-Regeln für einen Pfad. Gibt es keine Regel für Kagibot, aber eine für Googlebot, folgt Kagibot den Anweisungen für Googlebot.

## Die robots.txt-Zeilen

So erlauben Sie Kagibot:

```
User-agent: Kagibot
Allow: /
```

So sperren Sie Kagibot:

```
User-agent: Kagibot
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
Mozilla/5.0 (compatible; Kagibot/1.0; +https://kagi.com/bot)
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Kagi listet auf seiner Bot-Seite die IP-Adressen (mit Hostnamen unter kagibot.org) auf, von denen Kagibot-Anfragen ausgehen.

## Vergleich mit Googlebot

[Googlebot](/de/bots/googlebot): Kagibot folgt seinen eigenen robots.txt-Regeln und greift auf die Regeln für Googlebot zurück, wenn keine Kagibot betrifft.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). Kagibot gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `Kagibot` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt Kagibot die robots.txt?

Ja, Standard-robots.txt-Anweisungen, die Kagibot betreffen, werden respektiert. Geben Sie Kagibot in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass Kagibot wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Kagi: About KagiBot (read 2026-10-24)](https://kagi.com/bot)
