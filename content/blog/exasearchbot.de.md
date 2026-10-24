title: ExaSearchBot: Aufgabe und Wirkung einer Sperre
h1: ExaSearchBot: Aufgabe und Wirkung einer Sperre
description: ExaSearchBot (Exa): Suche. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: exasearchbot
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu ExaSearchBot: Betreiber Exa, Aufgabe Suche, befolgt robots.txt Ja, Adressliste Prüfwerkzeug
hero_sub: ExaSearchBot, betrieben von Exa
hero_boxes: Betreiber|Exa; Aufgabe|Suche; Befolgt robots.txt|Ja; Adressliste|Prüfwerkzeug
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/perplexitybot|PerplexityBot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: ExaSearchBot ist der Crawler von Exa, einer Suchmaschine, die für Suche und Retrieval gebaut ist, damit Seiten gefunden und zitiert werden können. Laut Exa prüft er vor dem Abruf robots.txt, und User-agent: ExaSearchBot mit Disallow: / sperrt die ganze Website. Jede Anfrage ist kryptografisch signiert, die Verifizierung hängt also nicht von einer IP-Adresse ab.

## Was ExaSearchBot ist

ExaSearchBot ist der Crawler von Exa, einer Suchmaschine. Laut Exa dient er der Suche und dem Retrieval, damit Seiten auffindbar werden und zitiert werden können. Seiten, die Exa auf Anfrage eines Nutzers statt per Crawling abruft, werden als ExaUser abgerufen.

| Angabe | ExaSearchBot |
| --- | --- |
| Betreiber | Exa |
| Aufgabe | Index für Suche und Retrieval |
| robots.txt-Token | `ExaSearchBot` |
| Befolgt robots.txt | Ja, laut Anbieter prüft er robots.txt vor dem Abruf |
| IP-Adressen | Prüfwerkzeug |
| Seite des Betreibers gelesen am | 24. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “Exa is a search engine. Similar to other search engines, Exa uses a robot (ExaSearchBot) to discover and index pages on the public web.”

Quelle: [Exa: Exa Search Crawler](https://crawler.exa.ai/), gelesen am 24. Oktober 2026.

## Was passiert, wenn Sie ExaSearchBot sperren

Exa sagt, dass User-agent: ExaSearchBot mit Disallow: / ExaSearchBot von der ganzen Website ausschließt. Gibt es keine Gruppe für ExaSearchBot, folgt er den Regeln, die für große Suchmaschinen gelten, sonst der Gruppe *. Laut Anbieter steuert robots.txt das Crawling, nicht die Indexierung; bereits indexierte Seiten entfernen Sie mit einem noindex-Meta-Tag oder einem X-Robots-Tag-Header.

## Die robots.txt-Zeilen

So erlauben Sie ExaSearchBot:

```
User-agent: ExaSearchBot
Allow: /
```

So sperren Sie ExaSearchBot:

```
User-agent: ExaSearchBot
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
Mozilla/5.0 (compatible; ExaSearchBot/1.0; +https://crawler.exa.ai/)
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Laut Anbieter ist jede Anfrage mit HTTP Message Signatures (Web Bot Auth) kryptografisch signiert. Der Anbieter nennt ein Verzeichnis öffentlicher Schlüssel zur Prüfung und sagt, dass die Verifizierung unabhängig von der IP-Adresse gilt.

## Vergleich mit PerplexityBot

[PerplexityBot](/de/bots/perplexitybot): Beide sind Such-Crawler für einen Index, der KI-Antworten mit zitierten Quellen speist. ExaSearchBot signiert seine Anfragen mit Web Bot Auth und greift auf die Regeln großer Suchmaschinen zurück, wenn er keine eigene Gruppe hat.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). ExaSearchBot gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `ExaSearchBot` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt ExaSearchBot die robots.txt?

Ja, laut Anbieter prüft er robots.txt vor dem Abruf. Geben Sie ExaSearchBot in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass ExaSearchBot wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Exa: Exa Search Crawler](https://crawler.exa.ai/)
- [Exa: FAQs](https://exa.ai/docs/admin/faqs)
