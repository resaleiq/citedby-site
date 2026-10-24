title: YouBot: Aufgabe und Wirkung einer Sperre
h1: YouBot: Aufgabe und Wirkung einer Sperre
description: YouBot (You.com): Suche. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: youbot
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu YouBot: Betreiber You.com, Aufgabe Suche, befolgt robots.txt Ja, Adressliste Liste auf seiner Seite
hero_sub: YouBot, betrieben von You.com
hero_boxes: Betreiber|You.com; Aufgabe|Suche; Befolgt robots.txt|Ja; Adressliste|Liste auf seiner Seite
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/mojeekbot|MojeekBot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: YouBot ist der Web-Crawler, der die Suchmaschine You.com antreibt und Seiten für ihre Ergebnisse entdeckt und indexiert. Laut You.com respektiert er robots.txt, beachtet Crawl-delay und speichert robots.txt 30 Minuten lang zwischen. User-agent: YouBot mit Disallow: / sperrt ihn für die ganze Website.

## Was YouBot ist

YouBot ist der Web-Crawler, der die Suchmaschine You.com antreibt. Er entdeckt und indexiert Webseiten für die Suchergebnisse von You.com. Laut You.com steht X.X.X.X im User-Agent für die Versionsnummer von Google Chrome.

| Angabe | YouBot |
| --- | --- |
| Betreiber | You.com |
| Aufgabe | Suche |
| robots.txt-Token | `YouBot` |
| Befolgt robots.txt | Ja, robots.txt wird 30 Minuten zwischengespeichert, Änderungen können also bis zu 30 Minuten dauern |
| IP-Adressen | Liste auf der Seite des Betreibers (you.com/docs/youbot) |
| Seite des Betreibers gelesen am | 24. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “YouBot is the web crawler that powers the You.com search engine.”

Quelle: [You.com Docs: YouBot: You.com's Web Crawler](https://docs.you.com/youbot), gelesen am 24. Oktober 2026.

## Was passiert, wenn Sie YouBot sperren

You.com sagt, YouBot respektiere robots.txt, und nennt User-agent: YouBot mit Disallow: / als Weg, ihn für die ganze Website zu sperren. Er beachtet außerdem Crawl-delay und speichert robots.txt 30 Minuten lang zwischen. Die Seite beschreibt keine weiteren Agenten von You.com.

## Die robots.txt-Zeilen

So erlauben Sie YouBot:

```
User-agent: YouBot
Allow: /
```

So sperren Sie YouBot:

```
User-agent: YouBot
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; YouBot/1.0; +https://docs.you.com/youbot; env:prod) Chrome/X.X.X.X Safari/537.36
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

You.com sagt, Anfragen stammen von 68.67.112.0/24, Hosts lösen als youbot-{octets-with-hyphens}.search.you.com auf, und Anfragen tragen Cloudflare-Web-Bot-Auth-Signaturen mit öffentlichen Schlüsseln unter you.com/.well-known/http-message-signatures-directory.

## Vergleich mit MojeekBot

[MojeekBot](/de/bots/mojeekbot): Beide sind Crawler von Suchmaschinen, die robots.txt befolgen; You.com unterstützt Crawl-delay und signiert Anfragen mit Web Bot Auth, während Mojeek Crawl-delay nicht unterstützt.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). YouBot gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `YouBot` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt YouBot die robots.txt?

Ja, robots.txt wird 30 Minuten zwischengespeichert, Änderungen können also bis zu 30 Minuten dauern. Geben Sie YouBot in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass YouBot wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [You.com Docs: YouBot: You.com's Web Crawler](https://docs.you.com/youbot)
