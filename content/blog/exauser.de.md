title: ExaUser: Aufgabe und Wirkung einer Sperre
h1: ExaUser: Aufgabe und Wirkung einer Sperre
description: ExaUser (Exa): Vom Nutzer ausgelöster Abruf. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: exauser
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu ExaUser: Betreiber Exa, Aufgabe Vom Nutzer ausgelöster Abruf, befolgt robots.txt Nicht immer, Adressliste Prüfwerkzeug
hero_sub: ExaUser, betrieben von Exa
hero_boxes: Betreiber|Exa; Aufgabe|Vom Nutzer ausgelöster Abruf; Befolgt robots.txt|Nicht immer; Adressliste|Prüfwerkzeug
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/exasearchbot|ExaSearchBot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: ExaUser ist der Agent, mit dem Exa eine Seite live abruft, wenn ein Nutzer oder eine auf der Exa API aufgebaute Anwendung ihren aktuellen Inhalt verlangt. Laut Exa gelten robots.txt-Regeln für solche vom Nutzer ausgelösten Abrufe möglicherweise nicht. Such-Opt-outs und automatisches Crawling steuern Sie stattdessen über das Token ExaSearchBot.

## Was ExaUser ist

ExaUser ist der Agent, mit dem Exa eine Seite live abruft, wenn ein Nutzer oder eine auf der Exa API aufgebaute Anwendung ihren aktuellen Inhalt verlangt. Laut Exa wird er nicht zum automatischen Crawlen des Webs genutzt; das übernimmt ExaSearchBot. Er versucht nicht, Logins, Paywalls oder CAPTCHAs zu umgehen, und sendet keine Formulare ab.

| Angabe | ExaUser |
| --- | --- |
| Betreiber | Exa |
| Aufgabe | Vom Nutzer ausgelöster Abruf |
| robots.txt-Token | `ExaUser` |
| Befolgt robots.txt | Teilweise, laut Anbieter gelten robots.txt-Regeln für vom Nutzer ausgelöste Abrufe möglicherweise nicht |
| IP-Adressen | Prüfwerkzeug |
| Seite des Betreibers gelesen am | 24. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “Exa uses ExaUser to fetch a page live when a user, or an application built on the Exa API, asks for its current content.”

Quelle: [Exa: ExaUser](https://crawler.exa.ai/exauser), gelesen am 24. Oktober 2026.

## Was passiert, wenn Sie ExaUser sperren

Exa sagt, dass robots.txt-Regeln für ExaUser möglicherweise nicht gelten, weil die Abrufe von einem Nutzer ausgelöst werden. Laut Exa wird ExaUser außerdem nicht verwendet, um zu entscheiden, ob Inhalte in der Exa-Suche erscheinen, und Such-Opt-outs sowie automatisches Crawling werden über das Token ExaSearchBot in robots.txt verwaltet.

## Die robots.txt-Zeilen

So erlauben Sie ExaUser:

```
User-agent: ExaUser
Allow: /
```

So sperren Sie ExaUser:

```
User-agent: ExaUser
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
Mozilla/5.0 (compatible; ExaUser/1.0; +https://crawler.exa.ai/exauser)
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Laut Anbieter ist jede Anfrage mit Web Bot Auth (RFC 9421) signiert, und er veröffentlicht seine Schlüssel in einem öffentlichen Verzeichnis; eine IP-Liste veröffentlicht er nicht.

## Vergleich mit ExaSearchBot

[ExaSearchBot](/de/bots/exasearchbot): ExaSearchBot crawlt automatisch, um Exas Suchindex aufzubauen, und folgt robots.txt, während ExaUser eine Seite nur abruft, wenn ein Nutzer oder eine Anwendung danach fragt, und robots.txt laut Anbieter möglicherweise nicht gilt.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). ExaUser gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `ExaUser` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt ExaUser die robots.txt?

Nicht immer: laut Anbieter gelten robots.txt-Regeln für vom Nutzer ausgelöste Abrufe möglicherweise nicht. Eine Regel für ExaUser in der robots.txt hält ihn deshalb möglicherweise nicht auf. Um ihn sicher abzuweisen, nutzen Sie eine Firewall- oder CDN-Regel, die User-Agent und veröffentlichte Adressen kombiniert.

### Woher weiß ich, dass ExaUser wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Exa: ExaUser](https://crawler.exa.ai/exauser)
- [Exa: Exa Search Crawler](https://crawler.exa.ai/)
