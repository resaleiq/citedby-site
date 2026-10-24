title: Meta-WebIndexer: Aufgabe und Wirkung einer Sperre
h1: Meta-WebIndexer: Aufgabe und Wirkung einer Sperre
description: Meta-WebIndexer (Meta): Suche. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: meta-webindexer
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu Meta-WebIndexer: Betreiber Meta, Aufgabe Suche, befolgt robots.txt Ja, Adressliste Keine
hero_sub: Meta-WebIndexer, betrieben von Meta
hero_boxes: Betreiber|Meta; Aufgabe|Suche; Befolgt robots.txt|Ja; Adressliste|Keine
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/meta-externalagent|Meta-ExternalAgent; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: Meta-WebIndexer ist ein Meta-Crawler, der das Web durchläuft, um die Suchergebnisse von Meta AI zu verbessern. Laut Meta hilft es Meta, Ihre Inhalte in den Antworten von Meta AI zu zitieren und zu verlinken, wenn Sie ihn in robots.txt zulassen. Sperren können Sie Metas Crawler mit einem Disallow, Änderungen brauchen bis zu 24 Stunden.

## Was Meta-WebIndexer ist

Meta-WebIndexer ist ein Meta-Crawler, der das Web durchläuft, um die Qualität der Suchergebnisse von Meta AI für Nutzer zu verbessern. Laut Meta hilft es Meta, Ihre Inhalte in den Antworten von Meta AI zu zitieren und zu verlinken, wenn Sie ihn in robots.txt zulassen. Meta dokumentiert ihn auf einer Seite zusammen mit Meta-ExternalAgent, Meta-ExternalFetcher, Meta-ExternalAds und FacebookExternalHit.

| Angabe | Meta-WebIndexer |
| --- | --- |
| Betreiber | Meta |
| Aufgabe | Suche |
| robots.txt-Token | `Meta-WebIndexer` |
| Befolgt robots.txt | Ja, Änderungen können bis zu 24 Stunden dauern |
| IP-Adressen | Keine veröffentlicht |
| Seite des Betreibers gelesen am | 24. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “The Meta-WebIndexer crawler navigates the web to improve Meta AI search result quality for users. In doing so, Meta analyzes online content to enhance the relevance and accuracy of Meta AI.”

Quelle: [Meta: Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers), gelesen am 24. Oktober 2026.

## Was passiert, wenn Sie Meta-WebIndexer sperren

Meta sagt, Sie können seine Crawler sperren, indem Sie in robots.txt ein Disallow für den jeweiligen Crawler eintragen, und Änderungen an robots.txt können bis zu 24 Stunden brauchen, bis sie wirken. Laut Meta hilft es Meta, Ihre Inhalte in den Antworten von Meta AI zu zitieren und zu verlinken, wenn Sie Meta-WebIndexer zulassen. Metas Seite sagt nicht, ob ein Disallow für Meta-WebIndexer seine anderen Crawler betrifft.

## Die robots.txt-Zeilen

So erlauben Sie Meta-WebIndexer:

```
User-agent: Meta-WebIndexer
Allow: /
```

So sperren Sie Meta-WebIndexer:

```
User-agent: Meta-WebIndexer
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
meta-webindexer/1.1
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Metas Crawler-Seite nennt für diesen Crawler weder IP-Adressen noch ein Verifizierungsverfahren; sie identifiziert den Crawler über seinen User-Agent-String.

## Vergleich mit Meta-ExternalAgent

[Meta-ExternalAgent](/de/bots/meta-externalagent): Meta-WebIndexer ist für die Suchergebnisse und Zitate von Meta AI gedacht, während Meta-ExternalAgent laut Meta für Zwecke wie das Training von KI-Foundation-Modellen oder das direkte Indexieren von Inhalten crawlt.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). Meta-WebIndexer gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `Meta-WebIndexer` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt Meta-WebIndexer die robots.txt?

Ja, Änderungen können bis zu 24 Stunden dauern. Geben Sie Meta-WebIndexer in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass Meta-WebIndexer wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Meta: Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers)
