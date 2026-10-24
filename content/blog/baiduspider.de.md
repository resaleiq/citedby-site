title: Baiduspider: Aufgabe und Wirkung einer Sperre
h1: Baiduspider: Aufgabe und Wirkung einer Sperre
description: Baiduspider (Baidu): Suche. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: baiduspider
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu Baiduspider: Betreiber Baidu, Aufgabe Suche, befolgt robots.txt Ja, Adressliste Reverse-DNS
hero_sub: Baiduspider, betrieben von Baidu
hero_boxes: Betreiber|Baidu; Aufgabe|Suche; Befolgt robots.txt|Ja; Adressliste|Reverse-DNS
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/bingbot|Bingbot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: Baiduspider ist der Crawler der Suchmaschine Baidu. Laut Baidu befolgt er das robots.txt-Protokoll. Wer Baiduspider sperrt, sperrt alle Baidu-User-Agents, und die Seiten werden in den Baidu-Ergebnissen nicht gefunden. Baiduspider-cpro und Baiduspider-ads arbeiten auf Basis von Kundenvereinbarungen und befolgen keine robots.txt-Einträge.

## Was Baiduspider ist

Baiduspider ist der Crawler der Suchmaschine Baidu. Er besucht Seiten und nimmt sie in den Baidu-Index auf. Baidu verwendet für verschiedene Produkte unterschiedliche User-Agents, zum Beispiel Baiduspider für die PC- und Mobilsuche sowie Baiduspider-image, Baiduspider-video und Baiduspider-news für die jeweilige Suche.

| Angabe | Baiduspider |
| --- | --- |
| Betreiber | Baidu |
| Aufgabe | Suche |
| robots.txt-Token | `Baiduspider` |
| Befolgt robots.txt | Ja bei Baiduspider; Baiduspider-cpro und Baiduspider-ads befolgen keine robots.txt-Einträge |
| IP-Adressen | Prüfung per Reverse-DNS |
| Seite des Betreibers gelesen am | 24. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “Baiduspider is Baidu search engine program which is used to visit pages on the internet and build information into Baidu index.”

Quelle: [Baidu Help Center: FAQs of Baiduspider](https://help.baidu.com/question?prod_id=99&class=0&id=3001), gelesen am 24. Oktober 2026.

## Was passiert, wenn Sie Baiduspider sperren

Baidu sagt, Baiduspider arbeite nach dem robots.txt-Protokoll. Wenn Sie ihn sperren, werden Ihre Seiten in den Baidu-Suchergebnissen und in allen anderen Ergebnissen von Baidu nicht gefunden. Sie können für verschiedene Baidu-User-Agents unterschiedliche Regeln festlegen, aber wer Baiduspider sperrt, sperrt alle Baidu-User-Agents. Baiduspider-cpro und Baiduspider-ads arbeiten auf Basis von Vereinbarungen mit Kunden und befolgen keine robots.txt-Einträge.

## Die robots.txt-Zeilen

So erlauben Sie Baiduspider:

```
User-agent: Baiduspider
Allow: /
```

So sperren Sie Baiduspider:

```
User-agent: Baiduspider
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
Baiduspider
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Baidu empfiehlt eine Reverse-DNS-Abfrage der besuchenden IP. Der Hostname von Baiduspider lautet *.baidu.com oder *.baidu.jp, andere Hostnamen sind gefälscht.

## Vergleich mit Bingbot

[Bingbot](/de/bots/bingbot): Beide crawlen für eine Suchmaschine. Baidu dokumentiert mehrere produktspezifische User-Agents (Bild, Video, News, Werbung) unter dem Namen Baiduspider und prüft per Hostname über Reverse-DNS.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). Baiduspider gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `Baiduspider` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt Baiduspider die robots.txt?

Ja bei Baiduspider; Baiduspider-cpro und Baiduspider-ads befolgen keine robots.txt-Einträge. Geben Sie Baiduspider in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass Baiduspider wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Baidu Help Center: FAQs of Baiduspider](https://help.baidu.com/question?prod_id=99&class=0&id=3001)
- [Baidu Help Center: How to block the crawling (robots.txt)](https://www.baidu.com/search/robots_english.html)
