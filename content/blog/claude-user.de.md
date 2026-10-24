title: Claude-User: Aufgabe und Wirkung einer Sperre
h1: Claude-User: Aufgabe und Wirkung einer Sperre
description: Claude-User (Anthropic): Vom Nutzer ausgelöster Abruf. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage.
slug: claude-user
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Vier Fakten zu Claude-User: Betreiber Anthropic, Aufgabe Vom Nutzer ausgelöster Abruf, befolgt robots.txt Ja, Adressliste Liste, nicht zum Sperren
hero_sub: Claude-User, betrieben von Anthropic
hero_boxes: Betreiber|Anthropic; Aufgabe|Vom Nutzer ausgelöster Abruf; Befolgt robots.txt|Ja; Adressliste|Liste, nicht zum Sperren
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/claude-searchbot|Claude-SearchBot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: Claude-User ist der Agent, den Claude nutzen kann, um auf eine Website zuzugreifen, wenn jemand ihm eine Frage stellt. Laut Anthropic verhindert ein Deaktivieren, dass Ihre Inhalte als Antwort auf eine Nutzeranfrage abgerufen werden, was Ihre Sichtbarkeit bei der nutzergesteuerten Websuche verringern kann. Er ist getrennt von ClaudeBot und Claude-SearchBot.

## Was Claude-User ist

Von Anthropics drei Bots ist Claude-User der, der an die Frage einer Person gebunden ist. Er sammelt keine Trainingsdaten (das tut [ClaudeBot](/de/bots/claudebot)) und baut nicht den Suchindex auf (das tut [Claude-SearchBot](/de/bots/claude-searchbot)).

| Angabe | Claude-User |
| --- | --- |
| Betreiber | Anthropic |
| Aufgabe | Vom Nutzer ausgelöster Abruf |
| robots.txt-Token | `Claude-User` |
| Befolgt robots.txt | Ja, laut Anthropic beachten seine Bots robots.txt |
| IP-Adressen | Der Betreiber verweist auf eine Liste, rät aber von einer Sperre per IP ab |
| Seite des Betreibers gelesen am | 21. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “Claude-User supports Claude AI users. When individuals ask questions to Claude, it may access websites using a Claude-User agent. Claude-User allows site owners to control which sites can be accessed through these user-initiated requests. Disabling Claude-User on your site prevents our system from retrieving your content in response to a user query, which may reduce your site's visibility for user-directed web search.”

Quelle: [Anthropic Help Center: Does Anthropic crawl data from the web, and how can site owners block the crawler? (7 April 2026)](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler), gelesen am 21. Oktober 2026.

## Was passiert, wenn Sie Claude-User sperren

Hier ist Anthropics Formulierung zu den Kosten am direktesten: Claude-User zu deaktivieren verhindert den Abruf „als Antwort auf eine Nutzeranfrage“ und „kann die Sichtbarkeit Ihrer Website bei der nutzergesteuerten Websuche verringern“. Ein Shop, der ihn sperrt, kann dem Modell aus anderen Quellen trotzdem bekannt sein, aber Claude kann die Seite auf Nachfrage nicht öffnen.

## Die robots.txt-Zeilen

So erlauben Sie Claude-User:

```
User-agent: Claude-User
Allow: /
```

So sperren Sie Claude-User:

```
User-agent: Claude-User
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Die Seite des Betreibers nennt keinen vollständigen User-Agent-String für Claude-User.

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Anthropics Hilfeartikel nennt für die drei Bots keinen User-Agent-String, und er sagt, die Quell-IP-Adressen stünden auf einer verlinkten Liste. Weil Anthropic außerdem sagt, dass das Sperren dieser Adressen verhindern kann, dass seine Bots robots.txt lesen, rät der Artikel dazu, den Zugriff in robots.txt zu steuern statt auf IP-Ebene.

## Vergleich mit Claude-SearchBot

[Claude-SearchBot](/de/bots/claude-searchbot): Bot für die Suchqualität; eine Sperre betrifft die Indexierung für die Suche, nicht die Live-Frage eines Nutzers.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). Claude-User gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `Claude-User` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt Claude-User die robots.txt?

Ja, laut Anthropic beachten seine Bots robots.txt. Geben Sie Claude-User in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass Claude-User wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Anthropic Help Center: Does Anthropic crawl data from the web, and how can site owners block the crawler? (7 April 2026)](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)
