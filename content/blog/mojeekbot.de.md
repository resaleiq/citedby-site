title: MojeekBot: Aufgabe und Wirkung einer Sperre
h1: MojeekBot: Aufgabe und Wirkung einer Sperre
description: MojeekBot (Mojeek): Suche. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: mojeekbot
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu MojeekBot: Betreiber Mojeek, Aufgabe Suche, befolgt robots.txt Ja, Adressliste 1 Bereiche
hero_sub: MojeekBot, betrieben von Mojeek
hero_boxes: Betreiber|Mojeek; Aufgabe|Suche; Befolgt robots.txt|Ja; Adressliste|1 Bereiche
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/bingbot|Bingbot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: MojeekBot ist der Web-Crawler der Suchmaschine Mojeek. Laut Mojeek befolgt er den Robots Exclusion Standard, nutzt den ersten Eintrag, dessen User-Agent MojeekBot enthält, und unterstützt die nicht standardisierte Anweisung crawl-delay nicht. Er soll von einer Website nicht mehr als eine Seite in derselben Sekunde abrufen.

## Was MojeekBot ist

MojeekBot ist der Web-Crawler der Suchmaschine Mojeek. Laut Mojeek soll er innerhalb derselben 1-Sekunden-Spanne nicht mehr als eine Seite von einer Website abrufen. Er befolgt die Meta-Tags noindex, nocache und nofollow.

| Angabe | MojeekBot |
| --- | --- |
| Betreiber | Mojeek |
| Aufgabe | Suche |
| robots.txt-Token | `MojeekBot` |
| Befolgt robots.txt | Ja, befolgt den Robots Exclusion Standard; crawl-delay wird nicht unterstützt |
| IP-Adressen | 1 Bereiche (www.mojeek.com/mojeekbot.json, Datei vom 2025-05-14) |
| Seite des Betreibers gelesen am | 24. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “MojeekBot is the web crawler for the Mojeek search engine.”

Quelle: [Mojeek: MojeekBot](https://www.mojeek.com/bot.html), gelesen am 24. Oktober 2026.

## Was passiert, wenn Sie MojeekBot sperren

Mojeek sagt, MojeekBot befolge den ersten robots.txt-Eintrag, dessen User-Agent MojeekBot enthält, und sonst den ersten Eintrag für User-Agent *. Er ruft keine URLs ab, die eine untersagte Zeichenfolge enthalten. Die nicht standardisierte Anweisung crawl-delay unterstützt er nicht.

## Die robots.txt-Zeilen

So erlauben Sie MojeekBot:

```
User-agent: MojeekBot
Allow: /
```

So sperren Sie MojeekBot:

```
User-agent: MojeekBot
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
MojeekBot
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Die Datei www.mojeek.com/mojeekbot.json enthielt am 24. Oktober 2026 1 Bereiche, Datei vom 2025-05-14.

Mojeek sagt, man solle die besuchende IP per Reverse-Lookup zu einem Namen in der Domain mojeek.com auflösen und per Forward-Lookup wieder auf dieselbe IP zurückführen oder die IP mit der veröffentlichten Liste der MojeekBot-IP-Adressen abgleichen.

## Vergleich mit Bingbot

[Bingbot](/de/bots/bingbot): Beide crawlen für eine Suchmaschine; Mojeek veröffentlicht eine IP-Liste mit einem Bereich und eine Reverse-DNS-Prüfung und unterstützt crawl-delay nicht.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). MojeekBot gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `MojeekBot` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt MojeekBot die robots.txt?

Ja, befolgt den Robots Exclusion Standard; crawl-delay wird nicht unterstützt. Geben Sie MojeekBot in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass MojeekBot wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Mojeek: MojeekBot](https://www.mojeek.com/bot.html)
- [MojeekBot IP list (JSON, creationTime 2025-05-14, read 2026-10-24)](https://www.mojeek.com/mojeekbot.json)
