title: ClaudeBot: Aufgabe und Wirkung einer Sperre
h1: ClaudeBot: Aufgabe und Wirkung einer Sperre
description: ClaudeBot (Anthropic): Training. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: claudebot
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Vier Fakten zu ClaudeBot: Betreiber Anthropic, Aufgabe Training, befolgt robots.txt Ja, Adressliste Liste, nicht zum Sperren
hero_sub: ClaudeBot, betrieben von Anthropic
hero_boxes: Betreiber|Anthropic; Aufgabe|Training; Befolgt robots.txt|Ja; Adressliste|Liste, nicht zum Sperren
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/claude-searchbot|Claude-SearchBot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: ClaudeBot ist Anthropics Crawler für Inhalte, die zum Modelltraining beitragen könnten. Ein Disallow in robots.txt signalisiert, dass künftige Materialien einer Website aus Trainingsdatensätzen ausgeschlossen werden sollen. Anthropic beachtet Crawl-delay und warnt, dass das Sperren seiner IP-Adressen verhindern kann, dass er robots.txt liest. Nutzen Sie deshalb robots.txt.

## Was ClaudeBot ist

Anthropic nennt in seinem Hilfeartikel drei Bots: ClaudeBot für Trainingsdaten, [Claude-User](/de/bots/claude-user) für Seiten, die auf Wunsch eines Nutzers abgerufen werden, und [Claude-SearchBot](/de/bots/claude-searchbot) für die Suchqualität. ClaudeBot ist der für das Training. Der Artikel ist auf den 7. April 2026 datiert.

| Angabe | ClaudeBot |
| --- | --- |
| Betreiber | Anthropic |
| Aufgabe | Training |
| robots.txt-Token | `ClaudeBot` |
| Befolgt robots.txt | Ja, er befolgt robots.txt und Crawl-delay |
| IP-Adressen | Der Betreiber verweist auf eine Liste, rät aber von einer Sperre per IP ab |
| Seite des Betreibers gelesen am | 21. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “ClaudeBot helps enhance the utility and safety of our generative AI models by collecting web content that could potentially contribute to their training. When a site restricts ClaudeBot access, it signals that the site's future materials should be excluded from our AI model training datasets.”

Quelle: [Anthropic Help Center: Does Anthropic crawl data from the web, and how can site owners block the crawler? (7 April 2026)](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler), gelesen am 21. Oktober 2026.

## Was passiert, wenn Sie ClaudeBot sperren

Anthropic sagt, eine Einschränkung signalisiere, dass die künftigen Materialien der Website aus seinen Trainingsdatensätzen ausgeschlossen werden sollen. Die Formulierung lautet „künftige Materialien“; sie sagt nicht, was mit bereits gesammelten Inhalten geschieht. Die beiden anderen Claude-Bots sind getrennt, deshalb bleiben ihre Regeln unberührt, wenn Sie ClaudeBot sperren.

## Die robots.txt-Zeilen

So erlauben Sie ClaudeBot:

```
User-agent: ClaudeBot
Allow: /
```

So sperren Sie ClaudeBot:

```
User-agent: ClaudeBot
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Die Seite des Betreibers nennt keinen vollständigen User-Agent-String für ClaudeBot.

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Anthropics Artikel sagt, seine Bots respektierten „Nicht crawlen“-Signale in robots.txt und versuchten nicht, CAPTCHAs zu umgehen. Er unterstützt die nicht standardisierte Anweisung Crawl-delay, zum Beispiel `User-agent: ClaudeBot` gefolgt von `Crawl-delay: 1`. Außerdem sagt Anthropic, dass das Sperren per IP-Adresse möglicherweise keinen dauerhaften Opt-out bewirkt, weil der Bot dann robots.txt nicht lesen kann. Laut Anthropics Artikel muss robots.txt für jede Subdomain gesetzt werden, die Sie ausschließen wollen.

## Vergleich mit Claude-SearchBot

[Claude-SearchBot](/de/bots/claude-searchbot): Ein getrennter Such-Bot: Eine Sperre von ClaudeBot betrifft ihn nicht.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet ClaudeBot mit einer echten Anfrage und liest dafür die robots.txt. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt ClaudeBot die robots.txt?

Ja, er befolgt robots.txt und Crawl-delay. Geben Sie ClaudeBot in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass ClaudeBot wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Anthropic Help Center: Does Anthropic crawl data from the web, and how can site owners block the crawler? (7 April 2026)](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)
