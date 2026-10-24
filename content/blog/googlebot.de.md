title: Googlebot: Aufgabe und Wirkung einer Sperre
h1: Googlebot: Aufgabe und Wirkung einer Sperre
description: Googlebot (Google): Suche. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: googlebot
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Vier Fakten zu Googlebot: Betreiber Google, Aufgabe Suche, befolgt robots.txt Ja, Adressliste 317 Bereiche
hero_sub: Googlebot, betrieben von Google
hero_boxes: Betreiber|Google; Aufgabe|Suche; Befolgt robots.txt|Ja; Adressliste|317 Bereiche
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/google-extended|Google-Extended; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: Googlebot ist Googles wichtigster Crawler für die Suche. Laut Google befolgen seine gängigen Crawler beim automatischen Crawlen immer robots.txt-Regeln. Crawling-Einstellungen für das Token Googlebot wirken sich auf die Google Suche aus, einschließlich Discover, sowie auf Produkte wie Bilder, Video und News. Google veröffentlicht dafür 317 IP-Bereiche.

## Was Googlebot ist

Googlebot ist der Crawler, von dem jede Suchprüfung ausgeht. Googles Seite führt mehrere Crawler auf, und das eine Token Googlebot steuert die Suche, Discover und die Produkte, die auf demselben Crawl aufbauen, etwa Bilder, den Videomodus und News.

| Angabe | Googlebot |
| --- | --- |
| Betreiber | Google |
| Aufgabe | Suche (auch Bilder, Video, News, Discover) |
| robots.txt-Token | `Googlebot` |
| Befolgt robots.txt | Ja, beim automatischen Crawlen immer |
| IP-Adressen | 317 Bereiche (developers.google.com/static/search/apis/ipranges/googlebot.json, Datei vom 2026-10-20) |
| Seite des Betreibers gelesen am | 21. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “Google's common crawlers are used to find information for building Google's search indexes, perform other product specific crawls, and for analysis. They always obey robots.txt rules when crawling automatically.”

Quelle: [Google Search Central: Google's common crawlers (last updated 2026-10-15)](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers), gelesen am 21. Oktober 2026.

## Was passiert, wenn Sie Googlebot sperren

Ein Disallow für Googlebot ist kein schmaler KI-Opt-out; es wirkt sich laut Googles Liste der betroffenen Produkte auf die Google Suche selbst aus, einschließlich Discover und der darauf aufbauenden Funktionen. Die engere Steuerung für das Gemini-Training ist das getrennte Token [Google-Extended](/de/bots/google-extended).

## Die robots.txt-Zeilen

So erlauben Sie Googlebot:

```
User-agent: Googlebot
Allow: /
```

So sperren Sie Googlebot:

```
User-agent: Googlebot
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Google veröffentlicht die Bereiche, die seine gängigen Crawler nutzen. Die Googlebot-Datei enthielt am 21. Oktober 2026 317 Präfixe, Erstellungszeit 2026-10-20 14:46 UTC. Google dokumentiert außerdem eine Reverse-DNS-Maske zur Bestätigung eines Hostnamens, sodass sich eine Anfrage auf zwei Arten prüfen lässt: die Adresse gegen die Datei und die Reverse-Abfrage gegen die Maske. Die Seite selbst wurde zuletzt am 2026-10-15 aktualisiert.

## Vergleich mit Google-Extended

[Google-Extended](/de/bots/google-extended): Ein Steuer-Token für das Gemini-Training; es ruft nie eine Seite ab.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet Googlebot mit einer echten Anfrage und liest dafür die robots.txt. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt Googlebot die robots.txt?

Ja, beim automatischen Crawlen immer. Geben Sie Googlebot in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass Googlebot wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Google Search Central: Google's common crawlers (last updated 2026-10-15)](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers)
- [developers.google.com/static/search/apis/ipranges/googlebot.json](https://developers.google.com/static/crawling/ipranges/common-crawlers.json)
