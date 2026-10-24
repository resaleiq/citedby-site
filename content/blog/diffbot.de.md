title: Diffbot: Aufgabe und Wirkung einer Sperre
h1: Diffbot: Aufgabe und Wirkung einer Sperre
description: Diffbot (Diffbot): Suche. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: diffbot
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu Diffbot: Betreiber Diffbot, Aufgabe Suche, befolgt robots.txt Ja, Adressliste Keine
hero_sub: Diffbot, betrieben von Diffbot
hero_boxes: Betreiber|Diffbot; Aufgabe|Suche; Befolgt robots.txt|Ja; Adressliste|Keine
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/bingbot|Bingbot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: Diffbot dokumentiert zwei User-Agents. Diffbot crawlt das Web proaktiv für eine allgemeine Suchmaschine, damit Websites aus seinem Knowledge Graph gefunden und zitiert werden können. Diffbot-User ruft eine URL für eine Person ab, die seine Software nutzt. Laut Diffbot folgen seine Crawls standardmäßig robots.txt, einschließlich disallow und crawl-delay.

## Was Diffbot ist

Diffbot dokumentiert zwei User-Agents. Diffbot dient dem allgemeinen, proaktiven Crawlen des Webs zum Aufbau einer allgemeinen Suchmaschine, damit Websites aus dem Diffbot Knowledge Graph und den Websuchdiensten gefunden und zitiert werden können. Diffbot-User dient Anfragen im Auftrag eines Menschen, der mit Diffbot-Software eine URL aufruft.

| Angabe | Diffbot |
| --- | --- |
| Betreiber | Diffbot |
| Aufgabe | Suche (allgemeiner Web-Crawl) |
| robots.txt-Token | `Diffbot` |
| Befolgt robots.txt | Ja, standardmäßig (Anweisungen disallow und crawl-delay) |
| IP-Adressen | Keine veröffentlicht |
| Seite des Betreibers gelesen am | 24. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “By default Diffbot's web crawls adhere to a site’s robots.txt instructions, including the disallow and crawl-delay directives.”

Quelle: [Diffbot: Does Diffbot respect robots.txt?](https://www.diffbot.com/docs/crawl/faq/robots-txt), gelesen am 24. Oktober 2026.

## Was passiert, wenn Sie Diffbot sperren

Diffbot sagt, seine Web-Crawls folgen standardmäßig robots.txt, einschließlich disallow und crawl-delay, und eine Regel könne in bestimmten Fällen überschrieben werden, etwa bei einer Partnerschaft oder Vereinbarung mit der Website. Diffbot und Diffbot-User nennt es als getrennte User-Agents. Nutzer seiner Extract- und Crawlbot-APIs legen laut Diffbot ihre eigenen Crawl-Parameter fest und können ihren eigenen User-Agent setzen.

## Die robots.txt-Zeilen

So erlauben Sie Diffbot:

```
User-agent: Diffbot
Allow: /
```

So sperren Sie Diffbot:

```
User-agent: Diffbot
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
Diffbot
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Die Anbieterseite beschreibt weder eine IP-Liste noch ein Verifizierungsverfahren.

## Vergleich mit Bingbot

[Bingbot](/de/bots/bingbot): Der Betreiber beschreibt Diffbot als ähnlich wie Googlebot und Bing, als allgemeinen Crawler für einen Suchindex, und sagt, er werde nicht für KI-Training verwendet.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). Diffbot gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `Diffbot` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt Diffbot die robots.txt?

Ja, standardmäßig (Anweisungen disallow und crawl-delay). Geben Sie Diffbot in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass Diffbot wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Diffbot: Does Diffbot respect robots.txt? (read 2026-10-24)](https://www.diffbot.com/docs/crawl/faq/robots-txt)
