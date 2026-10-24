title: Google-GeminiNotebook: Aufgabe und Wirkung einer Sperre
h1: Google-GeminiNotebook: Aufgabe und Wirkung einer Sperre
description: Google-GeminiNotebook (Google): Vom Nutzer ausgelöster Abruf. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage.
slug: google-gemininotebook
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu Google-GeminiNotebook: Betreiber Google, Aufgabe Vom Nutzer ausgelöster Abruf, befolgt robots.txt Nicht immer, Adressliste Reverse-DNS
hero_sub: Google-GeminiNotebook, betrieben von Google
hero_boxes: Betreiber|Google; Aufgabe|Vom Nutzer ausgelöster Abruf; Befolgt robots.txt|Nicht immer; Adressliste|Reverse-DNS
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/chatgpt-user|ChatGPT-User; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: Google-GeminiNotebook ist der User-Agent des Gemini-Notebook-Fetchers. Er ruft einzelne URLs ab, die Nutzer als Quellen für ihre Projekte hinzugefügt haben. Google führt ihn unter den vom Nutzer ausgelösten Fetchern auf, die robots.txt in der Regel ignorieren, weil ein Nutzer den Abruf angefordert hat. Als früheren Agenten nennt Googles Seite Google-NotebookLM.

## Was Google-GeminiNotebook ist

Google-GeminiNotebook ist der User-Agent des Gemini-Notebook-Fetchers, den Google unter seinen vom Nutzer ausgelösten Fetchern aufführt. Er ruft einzelne URLs ab, die Nutzer als Quellen für ihre Projekte angegeben haben. Googles Seite nennt Google-NotebookLM als früheren Agenten, der bis August 2026 unterstützt wurde.

| Angabe | Google-GeminiNotebook |
| --- | --- |
| Betreiber | Google |
| Aufgabe | Vom Nutzer ausgelöster Abruf |
| robots.txt-Token | `Google-GeminiNotebook` |
| Befolgt robots.txt | Teilweise. Google sagt, vom Nutzer ausgelöste Fetcher ignorieren robots.txt-Regeln in der Regel, weil ein Nutzer den Abruf angefordert hat. |
| IP-Adressen | Prüfung per Reverse-DNS |
| Seite des Betreibers gelesen am | 24. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “The Gemini Notebook fetcher requests individual URLs that Gemini Notebook users have provided as sources for their projects.”

Quelle: [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers), gelesen am 24. Oktober 2026.

## Was passiert, wenn Sie Google-GeminiNotebook sperren

Google sagt, dass vom Nutzer ausgelöste Fetcher robots.txt-Regeln in der Regel ignorieren, weil der Abruf von einem Nutzer angefordert wurde. Die Google-Seite dokumentiert kein robots.txt-Token für diesen Fetcher.

## Die robots.txt-Zeilen

So erlauben Sie Google-GeminiNotebook:

```
User-agent: Google-GeminiNotebook
Allow: /
```

So sperren Sie Google-GeminiNotebook:

```
User-agent: Google-GeminiNotebook
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 (compatible; Google-GeminiNotebook; +https://developers.google.com/crawling/docs/crawlers-fetchers/google-gemininotebook)
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Google sagt, vom Nutzer ausgelöste Fetcher veröffentlichen IP-Bereiche in user-triggered-fetchers.json, user-triggered-fetchers-google.json und user-triggered-agents.json, und die Reverse-DNS-Maske entspreche ***-***-***-***.gae.googleusercontent.com oder google-proxy-***-***-***-***.google.com, je nachdem, ob der Fetcher Google oder einem Nutzer gehört.

## Vergleich mit ChatGPT-User

[ChatGPT-User](/de/bots/chatgpt-user): Beide rufen einzelne URLs ab, weil ein Nutzer ein Assistenzprodukt gebeten hat, sie zu verwenden, und beide Anbieter sagen, dass diese Abrufe robots.txt-Regeln möglicherweise nicht befolgen.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). Google-GeminiNotebook gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `Google-GeminiNotebook` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt Google-GeminiNotebook die robots.txt?

Nicht immer. Google sagt, vom Nutzer ausgelöste Fetcher ignorieren robots.txt-Regeln in der Regel, weil ein Nutzer den Abruf angefordert hat. Eine Regel für Google-GeminiNotebook in der robots.txt hält ihn deshalb möglicherweise nicht auf. Um ihn sicher abzuweisen, nutzen Sie eine Firewall- oder CDN-Regel, die User-Agent und veröffentlichte Adressen kombiniert.

### Woher weiß ich, dass Google-GeminiNotebook wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
