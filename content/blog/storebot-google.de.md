title: Storebot-Google: Aufgabe und Wirkung einer Sperre
h1: Storebot-Google: Aufgabe und Wirkung einer Sperre
description: Storebot-Google (Google): Suche. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: storebot-google
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu Storebot-Google: Betreiber Google, Aufgabe Suche, befolgt robots.txt Ja, Adressliste 317 Bereiche
hero_sub: Storebot-Google, betrieben von Google
hero_boxes: Betreiber|Google; Aufgabe|Suche; Befolgt robots.txt|Ja; Adressliste|317 Bereiche
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/googlebot|Googlebot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: Storebot-Google ist der Crawler, den Google unter seinen gängigen Crawlern als Google StoreBot dokumentiert. Laut Google wirkt ein Disallow für sein Token auf alle Oberflächen von Google Shopping, etwa den Shopping-Tab in der Google Suche und Google Shopping. Googlebot ist ein getrenntes Token mit eigenen betroffenen Produkten.

## Was Storebot-Google ist

Storebot-Google ist der Google-Crawler, der unter den gängigen Crawlern als Google StoreBot dokumentiert ist. Laut Google wirken Regeln für ihn auf alle Oberflächen von Google Shopping. Google nennt für ihn getrennte User-Agent-Strings für Desktop und Mobil.

| Angabe | Storebot-Google |
| --- | --- |
| Betreiber | Google |
| Aufgabe | Suche (Oberflächen von Google Shopping) |
| robots.txt-Token | `Storebot-Google` |
| Befolgt robots.txt | Ja. Google sagt, gängige Crawler befolgen beim automatischen Crawlen immer robots.txt-Regeln. |
| IP-Adressen | 317 Bereiche (developers.google.com/static/crawling/ipranges/common-crawlers.json, Datei vom 2026-10-23) |
| Seite des Betreibers gelesen am | 24. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “Crawling preferences addressed to the Storebot-Google user agent affect all surfaces of Google Shopping”

Quelle: [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers), gelesen am 24. Oktober 2026.

## Was passiert, wenn Sie Storebot-Google sperren

Google sagt, dass ein Disallow für das Token Storebot-Google alle Oberflächen von Google Shopping betrifft, etwa den Shopping-Tab in der Google Suche und Google Shopping. Die Seite führt Googlebot als getrenntes Token mit eigenen betroffenen Produkten auf.

## Die robots.txt-Zeilen

So erlauben Sie Storebot-Google:

```
User-agent: Storebot-Google
Allow: /
```

So sperren Sie Storebot-Google:

```
User-agent: Storebot-Google
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
Mozilla/5.0 (X11; Linux x86_64; Storebot-Google/1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z Safari/537.36
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Die Datei developers.google.com/static/crawling/ipranges/common-crawlers.json enthielt am 24. Oktober 2026 317 Bereiche, Datei vom 2026-10-23.

Google sagt, die gängigen Crawler crawlen in der Regel aus den Bereichen in common-crawlers.json, und der Reverse-DNS-Name entspreche crawl-***-***-***-***.googlebot.com oder geo-crawl-***-***-***-***.geo.googlebot.com.

## Vergleich mit Googlebot

[Googlebot](/de/bots/googlebot): Die Regeln für Googlebot wirken sich auf die Google Suche und verwandte Produkte aus, die Regeln für Storebot-Google auf Oberflächen von Google Shopping.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). Storebot-Google gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `Storebot-Google` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt Storebot-Google die robots.txt?

Ja. Google sagt, gängige Crawler befolgen beim automatischen Crawlen immer robots.txt-Regeln. Geben Sie Storebot-Google in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass Storebot-Google wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers)
- [Google: common-crawlers.json (read 2026-10-24, creationTime 2026-10-23)](https://developers.google.com/static/crawling/ipranges/common-crawlers.json)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
