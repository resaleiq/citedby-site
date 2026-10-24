title: Meta-ExternalAgent: Aufgabe und Wirkung einer Sperre
h1: Meta-ExternalAgent: Aufgabe und Wirkung einer Sperre
description: Meta-ExternalAgent (Meta): Mehrere Aufgaben. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: meta-externalagent
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Vier Fakten zu Meta-ExternalAgent: Betreiber Meta, Aufgabe Mehrere Aufgaben, befolgt robots.txt Ja, Adressliste Keine
hero_sub: Meta-ExternalAgent, betrieben von Meta
hero_boxes: Betreiber|Meta; Aufgabe|Mehrere Aufgaben; Befolgt robots.txt|Ja; Adressliste|Keine
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/gptbot|GPTBot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: Meta-ExternalAgent ist Metas Crawler für Anwendungsfälle wie das Training von KI-Foundation-Modellen oder die Verbesserung von Produkten durch direktes Indexieren von Inhalten. Metas Seite, aktualisiert am 21. Mai 2026, führt fünf Agenten auf. Laut Meta können Meta-ExternalFetcher und FacebookExternalHit robots.txt umgehen, und Änderungen können bis zu 24 Stunden dauern.

## Was Meta-ExternalAgent ist

Metas Seite führt fünf Crawler auf. FacebookExternalHit ruft eine Seite ab, wenn jemand einen Link auf Facebook, Instagram oder Messenger teilt, um Titel, Beschreibung und Vorschaubild zwischenzuspeichern. Meta-WebIndexer verbessert die Suchergebnisse von Meta AI, und laut Meta hilft es Meta, Ihre Inhalte in den Antworten von Meta AI zu zitieren und zu verlinken, wenn Sie ihn zulassen. Meta-ExternalAds crawlt für Werbe- und Geschäftsprodukte. Meta-ExternalAgent ist der für das Training von KI-Foundation-Modellen oder das Indexieren. Meta-ExternalFetcher ruft einzelne Links auf Wunsch eines Nutzers ab, auch um KI dabei zu helfen, auf Websites zu navigieren und Aufgaben für Nutzer zu erledigen.

| Angabe | Meta-ExternalAgent |
| --- | --- |
| Betreiber | Meta |
| Aufgabe | Training von KI-Modellen und Indexieren von Inhalten |
| robots.txt-Token | `meta-externalagent` |
| Befolgt robots.txt | Ja |
| IP-Adressen | Keine veröffentlicht |
| Seite des Betreibers gelesen am | 21. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “The Meta-ExternalAgent crawler crawls the web for use cases such as training foundation AI models or improving products by indexing content directly.”

Quelle: [Meta for Developers: Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers), gelesen am 21. Oktober 2026.

## Was passiert, wenn Sie Meta-ExternalAgent sperren

Ein Disallow für meta-externalagent betrifft nur diesen Agenten: Metas eigene Beispiele geben jedem Token eine eigene Gruppe, und die anderen vier haben ihre eigenen. Der, den man am ehesten versehentlich sperrt und der dann teuer wird, ist FacebookExternalHit, denn er erzeugt die Linkvorschau, wenn jemand Ihre Seite teilt. Zwei der fünf ignorieren Ihre robots.txt möglicherweise: Laut Meta kann Meta-ExternalFetcher robots.txt umgehen, weil er Abrufe ausführt, die der Nutzer angefordert hat, und FacebookExternalHit kann es für Sicherheits- oder Integritätsprüfungen wie Malware-Prüfungen umgehen.

## Die robots.txt-Zeilen

So erlauben Sie Meta-ExternalAgent:

```
User-agent: meta-externalagent
Allow: /
```

So sperren Sie Meta-ExternalAgent:

```
User-agent: meta-externalagent
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
meta-externalagent/1.1
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Metas Seite nennt die User-Agent-Strings (meta-externalagent/1.1 und die Version mit einem Link) und veröffentlicht in dem Text, den wir gelesen haben, keine IP-Liste, deshalb nennen wir keine Anzahl. Für FacebookExternalHit sagt Meta, Sie sollten entweder die User-Agent-Strings oder die IP-Adressen auf die Allowlist setzen, und nennt die Adressen die sicherere Option. Laut Meta können Crawler robots.txt bis zu 24 Stunden zwischenspeichern, warten Sie also so lange, bevor Sie eine Änderung beurteilen. Fragen gehen an webmasters@meta.com.

## Vergleich mit GPTBot

[GPTBot](/de/bots/gptbot): OpenAIs Crawler für das Training, der robots.txt ohne Metas Umgehungsfälle befolgt.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). Meta-ExternalAgent gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `meta-externalagent` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt Meta-ExternalAgent die robots.txt?

Ja. Geben Sie meta-externalagent in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass Meta-ExternalAgent wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Meta for Developers: Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers)
