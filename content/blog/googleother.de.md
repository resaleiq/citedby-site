title: GoogleOther: Aufgabe und Wirkung einer Sperre
h1: GoogleOther: Aufgabe und Wirkung einer Sperre
description: GoogleOther (Google): Mehrere Aufgaben. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: googleother
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu GoogleOther: Betreiber Google, Aufgabe Mehrere Aufgaben, befolgt robots.txt Ja, Adressliste 317 Bereiche
hero_sub: GoogleOther, betrieben von Google
hero_boxes: Betreiber|Google; Aufgabe|Mehrere Aufgaben; Befolgt robots.txt|Ja; Adressliste|317 Bereiche
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/googlebot|Googlebot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: GoogleOther ist Googles generischer Crawler. Verschiedene Google-Produktteams nutzen ihn, um öffentlich zugängliche Inhalte abzurufen, zum Beispiel bei einmaligen Crawls für interne Forschung und Entwicklung. Laut Google wirken sich Regeln für GoogleOther auf kein bestimmtes Produkt aus. GoogleOther-Image und GoogleOther-Video sind als getrennte Tokens dokumentiert.

## Was GoogleOther ist

GoogleOther ist Googles generischer Crawler, den verschiedene Google-Produktteams nutzen, um öffentlich zugängliche Inhalte abzurufen, zum Beispiel bei einmaligen Crawls für interne Forschung und Entwicklung. Google führt ihn unter seinen gängigen Crawlern neben Googlebot auf und dokumentiert außerdem GoogleOther-Image und GoogleOther-Video als Versionen, die für Bild- und Video-URLs optimiert sind. Die Google-Seite sagt nicht, dass er für KI-Training verwendet wird.

| Angabe | GoogleOther |
| --- | --- |
| Betreiber | Google |
| Aufgabe | Generischer Crawl für verschiedene Google-Produktteams |
| robots.txt-Token | `GoogleOther` |
| Befolgt robots.txt | Ja. Google sagt, gängige Crawler befolgen beim automatischen Crawlen immer robots.txt-Regeln. |
| IP-Adressen | 317 Bereiche (developers.google.com/static/crawling/ipranges/common-crawlers.json, Datei vom 2026-10-23) |
| Seite des Betreibers gelesen am | 24. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “GoogleOther is the generic crawler that may be used by various product teams for fetching publicly accessible content from sites. For example, it may be used for one-off crawls for internal research and development.”

Quelle: [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers), gelesen am 24. Oktober 2026.

## Was passiert, wenn Sie GoogleOther sperren

Google sagt, dass Crawling-Einstellungen für den User-Agent GoogleOther sich auf kein bestimmtes Produkt auswirken. Google dokumentiert GoogleOther-Image und GoogleOther-Video als getrennte robots.txt-Tokens, daher wird nicht gesagt, dass eine Regel für GoogleOther sie mit abdeckt, und das Token Googlebot ist noch einmal ein eigenes Token.

## Die robots.txt-Zeilen

So erlauben Sie GoogleOther:

```
User-agent: GoogleOther
Allow: /
```

So sperren Sie GoogleOther:

```
User-agent: GoogleOther
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GoogleOther) Chrome/W.X.Y.Z Safari/537.36
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Die Datei developers.google.com/static/crawling/ipranges/common-crawlers.json enthielt am 24. Oktober 2026 317 Bereiche, Datei vom 2026-10-23.

Google sagt, die gängigen Crawler crawlen in der Regel aus den Bereichen in common-crawlers.json, und der Reverse-DNS-Name entspreche crawl-***-***-***-***.googlebot.com oder geo-crawl-***-***-***-***.geo.googlebot.com.

## Vergleich mit Googlebot

[Googlebot](/de/bots/googlebot): Googlebot crawlt für die Google Suche und verwandte Produkte, während GoogleOther ein generischer Crawler ist, dessen robots.txt-Regeln sich auf kein bestimmtes Google-Produkt auswirken.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). GoogleOther gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `GoogleOther` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt GoogleOther die robots.txt?

Ja. Google sagt, gängige Crawler befolgen beim automatischen Crawlen immer robots.txt-Regeln. Geben Sie GoogleOther in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass GoogleOther wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers)
- [Google: common-crawlers.json (read 2026-10-24, creationTime 2026-10-23)](https://developers.google.com/static/crawling/ipranges/common-crawlers.json)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
