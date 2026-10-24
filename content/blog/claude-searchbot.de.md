title: Claude-SearchBot: Aufgabe und Wirkung einer Sperre
h1: Claude-SearchBot: Aufgabe und Wirkung einer Sperre
description: Claude-SearchBot (Anthropic): Suche. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: claude-searchbot
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Vier Fakten zu Claude-SearchBot: Betreiber Anthropic, Aufgabe Suche, befolgt robots.txt Ja, Adressliste Liste, nicht zum Sperren
hero_sub: Claude-SearchBot, betrieben von Anthropic
hero_boxes: Betreiber|Anthropic; Aufgabe|Suche; Befolgt robots.txt|Ja; Adressliste|Liste, nicht zum Sperren
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/claudebot|ClaudeBot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: Claude-SearchBot ist der Anthropic-Bot, der das Web durchläuft, um die Qualität von Suchergebnissen zu verbessern. Laut Anthropic verhindert ein Deaktivieren, dass Ihre Inhalte für die Suchoptimierung indexiert werden, was Ihre Sichtbarkeit und Genauigkeit in den Suchergebnissen der Nutzer verringern kann. Sein robots.txt-Token ist Claude-SearchBot.

## Was Claude-SearchBot ist

Claude-SearchBot ist die Indexierungsseite von Anthropics Suche. Anthropic beschreibt ihn so, dass er Online-Inhalte analysiert, um die Relevanz und Genauigkeit von Suchantworten zu verbessern. [ClaudeBot](/de/bots/claudebot) sammelt für das Training, und [Claude-User](/de/bots/claude-user) beantwortet eine Live-Frage.

| Angabe | Claude-SearchBot |
| --- | --- |
| Betreiber | Anthropic |
| Aufgabe | Suche |
| robots.txt-Token | `Claude-SearchBot` |
| Befolgt robots.txt | Ja, laut Anthropic beachten seine Bots robots.txt |
| IP-Adressen | Der Betreiber verweist auf eine Liste, rät aber von einer Sperre per IP ab |
| Seite des Betreibers gelesen am | 21. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “Claude-SearchBot navigates the web to improve search result quality for users. It analyzes online content specifically to enhance the relevance and accuracy of search responses. Disabling Claude-SearchBot on your site prevents our system from indexing your content for search optimization, which may reduce your site's visibility and accuracy in user search results.”

Quelle: [Anthropic Help Center: Does Anthropic crawl data from the web, and how can site owners block the crawler? (7 April 2026)](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler), gelesen am 21. Oktober 2026.

## Was passiert, wenn Sie Claude-SearchBot sperren

Anthropic nennt zwei Folgen, wenn Sie ihn deaktivieren: Ihre Inhalte werden nicht für die Suchoptimierung indexiert, und die Sichtbarkeit und Genauigkeit Ihrer Website in den Suchergebnissen der Nutzer kann sinken.

## Die robots.txt-Zeilen

So erlauben Sie Claude-SearchBot:

```
User-agent: Claude-SearchBot
Allow: /
```

So sperren Sie Claude-SearchBot:

```
User-agent: Claude-SearchBot
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Die Seite des Betreibers nennt keinen vollständigen User-Agent-String für Claude-SearchBot.

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Der Hilfeartikel ist auf den 7. April 2026 datiert. Er nennt keinen User-Agent-String, eine Logzeile mit Claude-SearchBot ist deshalb eine Behauptung, die Sie allein mit dem Artikel nicht bestätigen können. Laut Anthropic stammt Traffic von einer Adresse auf der verlinkten Liste von Anthropic, und Websitebetreiber, die ein Fehlverhalten eines Bots vermuten, sollen von einer E-Mail-Adresse der betroffenen Domain aus schreiben.

## Vergleich mit ClaudeBot

[ClaudeBot](/de/bots/claudebot): Wer ClaudeBot sperrt, widerspricht nur dem Training; Sie verschwinden dadurch nicht aus Claudes Suchindex.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). Claude-SearchBot gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `Claude-SearchBot` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt Claude-SearchBot die robots.txt?

Ja, laut Anthropic beachten seine Bots robots.txt. Geben Sie Claude-SearchBot in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass Claude-SearchBot wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Anthropic Help Center: Does Anthropic crawl data from the web, and how can site owners block the crawler? (7 April 2026)](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)
