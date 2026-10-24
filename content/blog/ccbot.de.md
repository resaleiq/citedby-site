title: CCBot: Aufgabe und Wirkung einer Sperre
h1: CCBot: Aufgabe und Wirkung einer Sperre
description: CCBot (Common Crawl): Mehrere Aufgaben. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: ccbot
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu CCBot: Betreiber Common Crawl, Aufgabe Mehrere Aufgaben, befolgt robots.txt Ja, Adressliste Reverse-DNS
hero_sub: CCBot, betrieben von Common Crawl
hero_boxes: Betreiber|Common Crawl; Aufgabe|Mehrere Aufgaben; Befolgt robots.txt|Ja; Adressliste|Reverse-DNS
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/gptbot|GPTBot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: CCBot ist der Crawler von Common Crawl, einer gemeinnützigen Organisation, die ein offenes Archiv von Web-Crawl-Daten pflegt, auf das jeder zugreifen und das jeder analysieren kann. Laut Common Crawl hält User-agent: CCBot mit Disallow: / ihn vom Crawlen einer Website ab. Außerdem warnt Common Crawl, dass andere Crawler sich fälschlich als CCBot ausgeben; prüfen Sie Anfragen also.

## Was CCBot ist

CCBot ist der Crawler von Common Crawl, einer gemeinnützigen Stiftung, die ein offenes Archiv von Web-Crawl-Daten erstellt und pflegt, auf das jeder zugreifen und das jeder analysieren kann. Laut Anbieterseite sollen die Crawl-Daten Organisationen, Hochschulen und gemeinnützigen Einrichtungen frei zur Verfügung stehen.

| Angabe | CCBot |
| --- | --- |
| Betreiber | Common Crawl |
| Aufgabe | Offenes Web-Crawl-Archiv |
| robots.txt-Token | `CCBot` |
| Befolgt robots.txt | Ja, über eine robots.txt-Regel für CCBot |
| IP-Adressen | Prüfung per Reverse-DNS |
| Seite des Betreibers gelesen am | 24. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “To prevent Common Crawl from crawling your website, include the following in your robots.txt”

Quelle: [Common Crawl: CCBot](https://commoncrawl.org/ccbot), gelesen am 24. Oktober 2026.

## Was passiert, wenn Sie CCBot sperren

Common Crawl sagt, dass User-agent: CCBot mit Disallow: / in robots.txt verhindert, dass Common Crawl die Website crawlt. Die Seite sagt außerdem, man wisse von Crawlern, die sich fälschlich als CCBot ausgeben, und empfiehlt, User-Agent-Strings zu prüfen.

## Die robots.txt-Zeilen

So erlauben Sie CCBot:

```
User-agent: CCBot
Allow: /
```

So sperren Sie CCBot:

```
User-agent: CCBot
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
CCBot/2.0 (https://commoncrawl.org/faq/)
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Common Crawl sagt, CCBot laufe auf eigenen IP-Adressbereichen mit Reverse-DNS (nicht für IPv6). Eine protokollierte Anfrage lässt sich also mit einer Reverse-Abfrage prüfen, die zu einem Hostnamen unter crawl.commoncrawl.org aufgelöst wird; die Bereiche sind außerdem als JSON veröffentlicht, nämlich unter https://index.commoncrawl.org/ccbot.json.

## Vergleich mit GPTBot

[GPTBot](/de/bots/gptbot): CCBot baut ein öffentliches Crawl-Archiv auf, das andere nutzen können, während GPTBot Inhalte für OpenAIs eigene Zwecke sammelt.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). CCBot gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `CCBot` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt CCBot die robots.txt?

Ja, über eine robots.txt-Regel für CCBot. Geben Sie CCBot in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass CCBot wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Common Crawl: CCBot (read 2026-10-24)](https://commoncrawl.org/ccbot)
