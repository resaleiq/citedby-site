title: Google-CloudVertexBot: Aufgabe und Wirkung einer Sperre
h1: Google-CloudVertexBot: Aufgabe und Wirkung einer Sperre
description: Google-CloudVertexBot (Google): Mehrere Aufgaben. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: google-cloudvertexbot
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu Google-CloudVertexBot: Betreiber Google, Aufgabe Mehrere Aufgaben, befolgt robots.txt Ja, Adressliste 317 Bereiche
hero_sub: Google-CloudVertexBot, betrieben von Google
hero_boxes: Betreiber|Google; Aufgabe|Mehrere Aufgaben; Befolgt robots.txt|Ja; Adressliste|317 Bereiche
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/googlebot|Googlebot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: Google-CloudVertexBot ist ein Google-Crawler, der von Website-Betreibern angeforderte Crawls ausführt, um Vertex AI Agents zu bauen. Google führt ihn unter seinen gängigen Crawlern auf, die beim automatischen Crawlen immer robots.txt befolgen. Laut Google haben Regeln für ihn keine Auswirkung auf die Google Suche oder andere Google-Produkte.

## Was Google-CloudVertexBot ist

Google-CloudVertexBot ist ein Google-Crawler, der unter den gängigen Crawlern aufgeführt ist. Laut Google führt er von Website-Betreibern angeforderte Crawls aus, um Vertex AI Agents zu bauen. Google zeigt ihn als Teilstring des User-Agents, nicht als vollständigen User-Agent-String.

| Angabe | Google-CloudVertexBot |
| --- | --- |
| Betreiber | Google |
| Aufgabe | Von Website-Betreibern angeforderter Crawl für Vertex AI Agents |
| robots.txt-Token | `Google-CloudVertexBot` |
| Befolgt robots.txt | Ja. Google sagt, gängige Crawler befolgen beim automatischen Crawlen immer robots.txt-Regeln. |
| IP-Adressen | 317 Bereiche (developers.google.com/static/crawling/ipranges/common-crawlers.json, Datei vom 2026-10-23) |
| Seite des Betreibers gelesen am | 24. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “Crawling preferences addressed to the Google-CloudVertexBot user agent affect crawls requested by the site owners' for building Vertex AI Agents”

Quelle: [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers), gelesen am 24. Oktober 2026.

## Was passiert, wenn Sie Google-CloudVertexBot sperren

Google sagt, dass Einstellungen für den User-Agent Google-CloudVertexBot Crawls betreffen, die Website-Betreiber zum Bau von Vertex AI Agents angefordert haben. Das habe keine Auswirkung auf die Google Suche oder andere Produkte.

## Die robots.txt-Zeilen

So erlauben Sie Google-CloudVertexBot:

```
User-agent: Google-CloudVertexBot
Allow: /
```

So sperren Sie Google-CloudVertexBot:

```
User-agent: Google-CloudVertexBot
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
Google-CloudVertexBot
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Die Datei developers.google.com/static/crawling/ipranges/common-crawlers.json enthielt am 24. Oktober 2026 317 Bereiche, Datei vom 2026-10-23.

Google sagt, die gängigen Crawler crawlen in der Regel aus den Bereichen in common-crawlers.json, und der Reverse-DNS-Name entspreche crawl-***-***-***-***.googlebot.com oder geo-crawl-***-***-***-***.geo.googlebot.com.

## Vergleich mit Googlebot

[Googlebot](/de/bots/googlebot): Googlebot crawlt für die Google Suche, während Google-CloudVertexBot nur crawlt, wenn ein Website-Betreiber einen Crawl zum Bau von Vertex AI Agents angefordert hat.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). Google-CloudVertexBot gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `Google-CloudVertexBot` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt Google-CloudVertexBot die robots.txt?

Ja. Google sagt, gängige Crawler befolgen beim automatischen Crawlen immer robots.txt-Regeln. Geben Sie Google-CloudVertexBot in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass Google-CloudVertexBot wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers)
- [Google: common-crawlers.json (read 2026-10-24, creationTime 2026-10-23)](https://developers.google.com/static/crawling/ipranges/common-crawlers.json)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
