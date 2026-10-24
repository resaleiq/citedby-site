title: Google-Pinpoint: Aufgabe und Wirkung einer Sperre
h1: Google-Pinpoint: Aufgabe und Wirkung einer Sperre
description: Google-Pinpoint (Google): Vom Nutzer ausgelöster Abruf. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage.
slug: google-pinpoint
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu Google-Pinpoint: Betreiber Google, Aufgabe Vom Nutzer ausgelöster Abruf, befolgt robots.txt Nicht immer, Adressliste Reverse-DNS
hero_sub: Google-Pinpoint, betrieben von Google
hero_boxes: Betreiber|Google; Aufgabe|Vom Nutzer ausgelöster Abruf; Befolgt robots.txt|Nicht immer; Adressliste|Reverse-DNS
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/google-gemininotebook|Google-GeminiNotebook; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: Google-Pinpoint ist ein von Google aufgeführter, vom Nutzer ausgelöster Fetcher. Er ruft einzelne URLs ab, die Pinpoint-Nutzer als Quellen für ihre persönlichen Dokumentsammlungen angegeben haben. Laut Google ignorieren vom Nutzer ausgelöste Fetcher robots.txt-Regeln in der Regel, weil ein Nutzer den Abruf angefordert hat, und ein robots.txt-Token dafür dokumentiert Google nicht.

## Was Google-Pinpoint ist

Google-Pinpoint ist ein von Google aufgeführter, vom Nutzer ausgelöster Fetcher. Er ruft einzelne URLs ab, die Pinpoint-Nutzer als Quellen für ihre persönlichen Dokumentsammlungen angegeben haben. Google führt ihn mit dem User-Agent Google-Pinpoint auf.

| Angabe | Google-Pinpoint |
| --- | --- |
| Betreiber | Google |
| Aufgabe | Vom Nutzer ausgelöster Abruf |
| robots.txt-Token | `Google-Pinpoint` |
| Befolgt robots.txt | Teilweise. Google sagt, vom Nutzer ausgelöste Fetcher ignorieren robots.txt-Regeln in der Regel, weil ein Nutzer den Abruf angefordert hat. |
| IP-Adressen | Prüfung per Reverse-DNS |
| Seite des Betreibers gelesen am | 24. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “The Google-Pinpoint fetcher requests individual URLs that Pinpoint users specified as sources for their personal collections of documents.”

Quelle: [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers), gelesen am 24. Oktober 2026.

## Was passiert, wenn Sie Google-Pinpoint sperren

Google sagt, dass vom Nutzer ausgelöste Fetcher robots.txt-Regeln in der Regel ignorieren, weil der Abruf von einem Nutzer angefordert wurde. Die Google-Seite dokumentiert kein robots.txt-Token für Google-Pinpoint.

## Die robots.txt-Zeilen

So erlauben Sie Google-Pinpoint:

```
User-agent: Google-Pinpoint
Allow: /
```

So sperren Sie Google-Pinpoint:

```
User-agent: Google-Pinpoint
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
Google-Pinpoint
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Google sagt, vom Nutzer ausgelöste Fetcher veröffentlichen IP-Bereiche in user-triggered-fetchers.json, user-triggered-fetchers-google.json und user-triggered-agents.json, und die Reverse-DNS-Maske entspreche ***-***-***-***.gae.googleusercontent.com oder google-proxy-***-***-***-***.google.com, je nachdem, ob der Fetcher Google oder einem Nutzer gehört.

## Vergleich mit Google-GeminiNotebook

[Google-GeminiNotebook](/de/bots/google-gemininotebook): Beide rufen URLs ab, die Nutzer in einem Google-Produkt als Quellen angegeben haben, und beide fallen unter Googles Regeln für vom Nutzer ausgelöste Fetcher.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). Google-Pinpoint gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `Google-Pinpoint` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt Google-Pinpoint die robots.txt?

Nicht immer. Teilweise. Google sagt, vom Nutzer ausgelöste Fetcher ignorieren robots.txt-Regeln in der Regel, weil ein Nutzer den Abruf angefordert hat. Eine Regel für Google-Pinpoint in der robots.txt hält ihn deshalb möglicherweise nicht auf. Um ihn sicher abzuweisen, nutzen Sie eine Firewall- oder CDN-Regel, die User-Agent und veröffentlichte Adressen kombiniert.

### Woher weiß ich, dass Google-Pinpoint wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
