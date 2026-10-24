title: Meta-ExternalFetcher: Aufgabe und Wirkung einer Sperre
h1: Meta-ExternalFetcher: Aufgabe und Wirkung einer Sperre
description: Meta-ExternalFetcher (Meta): Vom Nutzer ausgelöster Abruf. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage.
slug: meta-externalfetcher
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu Meta-ExternalFetcher: Betreiber Meta, Aufgabe Vom Nutzer ausgelöster Abruf, befolgt robots.txt Nicht immer, Adressliste Keine
hero_sub: Meta-ExternalFetcher, betrieben von Meta
hero_boxes: Betreiber|Meta; Aufgabe|Vom Nutzer ausgelöster Abruf; Befolgt robots.txt|Nicht immer; Adressliste|Keine
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/meta-externalagent|Meta-ExternalAgent; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: Meta-ExternalFetcher ist ein Meta-Crawler, der einzelne Links auf Wunsch eines Nutzers abruft. Laut Meta unterstützt er Produktfunktionen wie die Hilfe für KI, auf Websites zu navigieren und Aufgaben für Nutzer zu erledigen, und er kann robots.txt umgehen, weil ein Nutzer die Abrufe anfordert. Änderungen an robots.txt können bis zu 24 Stunden dauern.

## Was Meta-ExternalFetcher ist

Meta-ExternalFetcher ist ein Meta-Crawler, der einzelne Links auf Wunsch eines Nutzers abruft. Laut Meta unterstützt er Produktfunktionen wie das Bewerten und Verbessern agentischer KI-Fähigkeiten, darunter die Hilfe für KI, auf Websites zu navigieren und Aufgaben für Nutzer zu erledigen. Meta dokumentiert ihn auf einer Seite zusammen mit Meta-ExternalAgent, Meta-WebIndexer, Meta-ExternalAds und FacebookExternalHit.

| Angabe | Meta-ExternalFetcher |
| --- | --- |
| Betreiber | Meta |
| Aufgabe | Vom Nutzer ausgelöster Abruf |
| robots.txt-Token | `Meta-ExternalFetcher` |
| Befolgt robots.txt | Teilweise, kann robots.txt umgehen, weil die Abrufe von einem Nutzer angefordert werden |
| IP-Adressen | Keine veröffentlicht |
| Seite des Betreibers gelesen am | 24. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “The Meta-ExternalFetcher crawler fetches individual links at a user's request and supports product functions such as evaluating and improving agentic AI capabilities—including helping AI navigate websites to complete tasks for users. Accordingly, this crawler may bypass robots.txt rules.”

Quelle: [Meta: Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers), gelesen am 24. Oktober 2026.

## Was passiert, wenn Sie Meta-ExternalFetcher sperren

Meta sagt, Sie können seine Crawler sperren, indem Sie in robots.txt ein Disallow für den jeweiligen Crawler eintragen. Meta sagt außerdem, dass Meta-ExternalFetcher robots.txt umgehen kann, weil er Abrufe ausführt, die der Nutzer angefordert hat. Laut Meta können Änderungen an robots.txt bis zu 24 Stunden brauchen, weil Crawler die Datei bis zu 24 Stunden zwischenspeichern können.

## Die robots.txt-Zeilen

So erlauben Sie Meta-ExternalFetcher:

```
User-agent: Meta-ExternalFetcher
Allow: /
```

So sperren Sie Meta-ExternalFetcher:

```
User-agent: Meta-ExternalFetcher
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
meta-externalfetcher/1.1
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Metas Crawler-Seite nennt für diesen Crawler weder IP-Adressen noch ein Verifizierungsverfahren; sie identifiziert den Crawler über seinen User-Agent-String.

## Vergleich mit Meta-ExternalAgent

[Meta-ExternalAgent](/de/bots/meta-externalagent): Meta-ExternalAgent crawlt das Web im Hintergrund, auch für das Training von KI-Foundation-Modellen, während Meta-ExternalFetcher einzelne Links abruft, die ein Nutzer angefragt hat, und robots.txt umgehen kann.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). Meta-ExternalFetcher gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `Meta-ExternalFetcher` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt Meta-ExternalFetcher die robots.txt?

Nicht immer: kann robots.txt umgehen, weil die Abrufe von einem Nutzer angefordert werden. Eine Regel für Meta-ExternalFetcher in der robots.txt hält ihn deshalb möglicherweise nicht auf. Um ihn sicher abzuweisen, nutzen Sie eine Firewall- oder CDN-Regel, die User-Agent und veröffentlichte Adressen kombiniert.

### Woher weiß ich, dass Meta-ExternalFetcher wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Meta: Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers)
