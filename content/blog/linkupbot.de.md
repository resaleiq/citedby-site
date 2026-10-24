title: LinkupBot: Aufgabe und Wirkung einer Sperre
h1: LinkupBot: Aufgabe und Wirkung einer Sperre
description: LinkupBot (Linkup): Suche. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: linkupbot
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu LinkupBot: Betreiber Linkup, Aufgabe Suche, befolgt robots.txt Ja, Adressliste Liste auf seiner Seite
hero_sub: LinkupBot, betrieben von Linkup
hero_boxes: Betreiber|Linkup; Aufgabe|Suche; Befolgt robots.txt|Ja; Adressliste|Liste auf seiner Seite
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/perplexitybot|PerplexityBot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: LinkupBot ist der Web-Crawler von Linkup. Er ruft öffentlich zugängliche Seiten ab, um den Linkup-Suchindex aufzubauen, der laut Linkup Suche und Web-Grounding für KI-Anwendungen antreibt. Laut Linkup sperrt User-agent: LinkupBot mit Disallow: / die ganze Website, und robots.txt ist kein Mechanismus zur Zugriffskontrolle.

## Was LinkupBot ist

LinkupBot ist der Web-Crawler von Linkup. Er ruft öffentlich zugängliche Seiten ab, um den Linkup-Suchindex aufzubauen und zu pflegen, der laut Linkup Suche und Web-Grounding für KI-Anwendungen antreibt.

| Angabe | LinkupBot |
| --- | --- |
| Betreiber | Linkup |
| Aufgabe | Suchindex für KI-Websuche |
| robots.txt-Token | `LinkupBot` |
| Befolgt robots.txt | Ja, laut Anbieter respektiert er die geltenden robots.txt-Regeln |
| IP-Adressen | Liste auf der Seite des Betreibers (www.linkup.so/linkupbot-ips.txt) |
| Seite des Betreibers gelesen am | 24. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “LinkupBot is Linkup’s web crawler. It discovers and retrieves publicly accessible webpages to build and maintain the Linkup web search index, which powers search and web grounding for AI applications.”

Quelle: [Linkup: LinkupBot](https://www.linkup.so/bot), gelesen am 24. Oktober 2026.

## Was passiert, wenn Sie LinkupBot sperren

Laut Anbieter sperrt es die ganze Website, wenn Sie User-agent: LinkupBot mit Disallow: / in robots.txt eintragen. Der Anbieter sagt außerdem, dass robots-Regeln pro Host gelten, dass das Zulassen von LinkupBot in einer Firewall robots.txt nicht außer Kraft setzt und dass robots.txt kein Mechanismus zur Zugriffskontrolle ist.

## Die robots.txt-Zeilen

So erlauben Sie LinkupBot:

```
User-agent: LinkupBot
Allow: /
```

So sperren Sie LinkupBot:

```
User-agent: LinkupBot
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
LinkupBot/1.0 (LinkupBot for web indexing; https://www.linkup.so/bot; bot@linkup.so)
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Laut Anbieter kommen Anfragen aus den CIDR-Bereichen in seiner veröffentlichten Liste, und zur Verifizierung sollen Sie sowohl eine Quell-IP aus dieser Liste als auch einen User-Agent mit dem Token LinkupBot prüfen.

## Vergleich mit PerplexityBot

[PerplexityBot](/de/bots/perplexitybot): Beide bauen einen Suchindex auf, der KI-Antworten speist. Der Index von LinkupBot bedient KI-Anwendungen über Linkups Such- und Grounding-Dienst, und seine IP-Liste ist eine reine Textdatei statt JSON.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). LinkupBot gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `LinkupBot` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt LinkupBot die robots.txt?

Ja, laut Anbieter respektiert er die geltenden robots.txt-Regeln. Geben Sie LinkupBot in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass LinkupBot wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Linkup: LinkupBot](https://www.linkup.so/bot)
- [Linkup: linkupbot-ips.txt (plain text, read 2026-10-24)](https://www.linkup.so/linkupbot-ips.txt)
