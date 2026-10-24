title: GPTBot: Aufgabe und Wirkung einer Sperre
h1: GPTBot: Aufgabe und Wirkung einer Sperre
description: GPTBot (OpenAI): Training. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: gptbot
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Vier Fakten zu GPTBot: Betreiber OpenAI, Aufgabe Training, befolgt robots.txt Ja, Adressliste 18 Bereiche
hero_sub: GPTBot, betrieben von OpenAI
hero_boxes: Betreiber|OpenAI; Aufgabe|Training; Befolgt robots.txt|Ja; Adressliste|18 Bereiche
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/oai-searchbot|OAI-SearchBot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: GPTBot ist OpenAIs Crawler für das Training. Wenn Sie ihn in robots.txt per Disallow ausschließen, teilen Sie OpenAI mit, dass die Inhalte der Website nicht zum Training seiner generativen KI-Foundation-Modelle verwendet werden sollen. Die ChatGPT-Suche steuert das nicht, denn sie nutzt OAI-SearchBot. OpenAI veröffentlicht 18 IP-Bereiche für GPTBot.

## Was GPTBot ist

GPTBot ist der Crawler, den die meisten meinen, wenn sie sagen „OpenAI sperren“. Laut OpenAIs Seite dient er dazu, Inhalte zu crawlen, die zum Training seiner Modelle verwendet werden können. Er ist einer von drei Crawlern, die OpenAI in der Dokumentation zur ChatGPT-Produktfamilie nennt, neben [OAI-SearchBot](/de/bots/oai-searchbot) und [ChatGPT-User](/de/bots/chatgpt-user).

| Angabe | GPTBot |
| --- | --- |
| Betreiber | OpenAI |
| Aufgabe | Training |
| robots.txt-Token | `GPTBot` |
| Befolgt robots.txt | Ja, er befolgt robots.txt |
| IP-Adressen | 18 Bereiche (openai.com/gptbot.json, Datei vom 2026-09-22) |
| Seite des Betreibers gelesen am | 21. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “GPTBot is used to make our generative AI foundation models more useful and safe. It is used to crawl content that may be used in training our generative AI foundation models. Disallowing GPTBot indicates a site's content should not be used in training generative AI foundation models.”

Quelle: [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots), gelesen am 21. Oktober 2026.

## Was passiert, wenn Sie GPTBot sperren

OpenAI versteht ein Disallow für GPTBot als Signal zum Training: Die Inhalte sollen nicht zum Training generativer KI-Foundation-Modelle verwendet werden. Auf derselben Seite steht ein Beispiel für eine Website, die OAI-SearchBot erlaubt, damit sie in Suchergebnissen erscheint, und GPTBot per Disallow ausschließt. Eine Sperre hier nimmt Sie also nicht von sich aus aus den Suchantworten von ChatGPT heraus. Ob Sie sperren, ist eine geschäftliche Entscheidung; beide Wege sind legitim.

## Die robots.txt-Zeilen

So erlauben Sie GPTBot:

```
User-agent: GPTBot
Allow: /
```

So sperren Sie GPTBot:

```
User-agent: GPTBot
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.4; +https://openai.com/gptbot
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Die GPTBot-Liste unter openai.com/gptbot.json ist die kürzeste der drei OpenAI-Dateien, die wir gezählt haben: 18 Präfixe am 21. Oktober 2026, Erstellungszeit 2026-09-22. Wenn eine Anfrage GPTBot nennt, aber von einer Adresse außerhalb dieser Liste kommt, beweist der Name allein nichts.

## Vergleich mit OAI-SearchBot

[OAI-SearchBot](/de/bots/oai-searchbot): Lassen Sie ihn zu und schließen Sie GPTBot per Disallow aus, um in der ChatGPT-Suche zu bleiben und dem Training zu widersprechen.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet GPTBot mit einer echten Anfrage und liest dafür die robots.txt. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt GPTBot die robots.txt?

Ja, er befolgt robots.txt. Geben Sie GPTBot in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass GPTBot wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots)
- [openai.com/gptbot.json](https://openai.com/gptbot.json)
