title: Applebot: Aufgabe und Wirkung einer Sperre
h1: Applebot: Aufgabe und Wirkung einer Sperre
description: Applebot (Apple): Mehrere Aufgaben. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: applebot
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu Applebot: Betreiber Apple, Aufgabe Mehrere Aufgaben, befolgt robots.txt Ja, Adressliste 24 Bereiche
hero_sub: Applebot, betrieben von Apple
hero_boxes: Betreiber|Apple; Aufgabe|Mehrere Aufgaben; Befolgt robots.txt|Ja; Adressliste|24 Bereiche
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/applebot-extended|Applebot-Extended; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: Applebot ist Apples Web-Crawler. Laut Apple speisen seine Daten die Suche in Spotlight, Siri und Safari und können auch beim Training von Apples Foundation-Modellen helfen. Ein Disallow für Applebot-Extended schließt Inhalte nur vom Training aus. Erwähnt robots.txt Applebot nicht, aber Googlebot, folgt Applebot den Regeln für Googlebot.

## Was Applebot ist

Applebot ist Apples Web-Crawler. Laut Apple speisen seine Daten die Suchtechnologie in Spotlight, Siri und Safari und können außerdem helfen, Apples Foundation-Modelle zu trainieren und KI-Modellen in Apple-Produkten Kontext für ihre Ausgaben zu liefern. Apple dokumentiert außerdem ein eigenes Token Applebot-Extended und einen User-Agent namens iTMS für Apple Podcasts.

| Angabe | Applebot |
| --- | --- |
| Betreiber | Apple |
| Aufgabe | Suche (gecrawlte Daten können auch beim Training von Apple-Modellen helfen) |
| robots.txt-Token | `Applebot` |
| Befolgt robots.txt | Ja, für allgemeine Suchcrawls, die an Applebot gerichtet sind |
| IP-Adressen | 24 Bereiche (search.developer.apple.com/applebot.json, Datei vom 2026-09-15) |
| Seite des Betreibers gelesen am | 24. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “Applebot respects standard robots.txt directives in general search crawls that are targeted at Applebot.”

Quelle: [Apple: About Applebot](https://support.apple.com/en-us/119829), gelesen am 24. Oktober 2026.

## Was passiert, wenn Sie Applebot sperren

Apple sagt, ein Disallow für Applebot-Extended schließe Inhalte vom Training von Apples generativen Foundation-Modellen aus, die Website könne aber weiterhin von Applebot gecrawlt werden und über Spotlight, Siri und Safari auffindbar bleiben. Ein Disallow für Applebot selbst gilt für allgemeine Suchcrawls, die an Applebot gerichtet sind. Laut Apple folgt Applebot den Anweisungen für Googlebot, wenn robots.txt Applebot nicht erwähnt, aber Googlebot. Apple sagt, das Meta-Tag nosnippet schließe Inhalte von Antworten mit breitem Weltwissen aus.

## Die robots.txt-Zeilen

So erlauben Sie Applebot:

```
User-agent: Applebot
Allow: /
```

So sperren Sie Applebot:

```
User-agent: Applebot
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15 (Applebot/0.1; +http://www.apple.com/go/applebot)
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Die Datei search.developer.apple.com/applebot.json enthielt am 24. Oktober 2026 24 Bereiche, Datei vom 2026-09-15.

Apple sagt, Applebot-Traffic lasse sich in der Regel über Reverse-DNS in der Domain *.applebot.apple.com erkennen oder indem man die IP-Adresse mit einem CIDR-Präfix in der veröffentlichten JSON-Datei abgleicht.

## Vergleich mit Applebot-Extended

[Applebot-Extended](/de/bots/applebot-extended): Applebot ist der Crawler, der Seiten für Apples Suchfunktionen abruft. Applebot-Extended ist dagegen das robots.txt-Token, das steuert, ob gecrawlte Inhalte zum Training generativer Apple-Modelle verwendet werden.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). Applebot gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `Applebot` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt Applebot die robots.txt?

Ja, für allgemeine Suchcrawls, die an Applebot gerichtet sind. Geben Sie Applebot in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass Applebot wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Apple: About Applebot](https://support.apple.com/en-us/119829)
- [Apple: Applebot IP CIDRs JSON (read 2026-10-24)](https://search.developer.apple.com/applebot.json)
