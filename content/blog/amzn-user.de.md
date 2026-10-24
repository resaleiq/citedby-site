title: Amzn-User: Aufgabe und Wirkung einer Sperre
h1: Amzn-User: Aufgabe und Wirkung einer Sperre
description: Amzn-User (Amazon): Vom Nutzer ausgelöster Abruf. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: amzn-user
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu Amzn-User: Betreiber Amazon, Aufgabe Vom Nutzer ausgelöster Abruf, befolgt robots.txt Nicht immer, Adressliste Liste auf seiner Seite
hero_sub: Amzn-User, betrieben von Amazon
hero_boxes: Betreiber|Amazon; Aufgabe|Vom Nutzer ausgelöster Abruf; Befolgt robots.txt|Nicht immer; Adressliste|Liste auf seiner Seite
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/amzn-searchbot|Amzn-SearchBot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: Amzn-User ist der Amazon-User-Agent, der Live-Seiten abruft, wenn ein Kunde Alexa etwas fragt, das aktuelle Informationen erfordert. Laut Amazon crawlt er nicht für das Training generativer KI und befolgt möglicherweise nicht alle robots.txt-Anweisungen, weil die Aktion vom Nutzer ausgeht. Amazonbot und Amzn-SearchBot sind getrennte Einstellungen.

## Was Amzn-User ist

Amzn-User ist ein Amazon-User-Agent, der Nutzeraktionen unterstützt, etwa das Beantworten von Alexa-Anfragen, die aktuelle Informationen erfordern. Amazon sagt, dass Amzn-User bei einer Kundenfrage live Informationen aus dem Web abrufen kann, um im Namen des Nutzers genaue Antworten zu geben. Laut Amazon crawlt er keine Inhalte für das Training generativer KI-Modelle.

| Angabe | Amzn-User |
| --- | --- |
| Betreiber | Amazon |
| Aufgabe | Vom Nutzer ausgelöster Abruf |
| robots.txt-Token | `Amzn-User` |
| Befolgt robots.txt | Teilweise, befolgt möglicherweise nicht alle robots.txt-Anweisungen, weil Aktionen vom Nutzer ausgehen können |
| IP-Adressen | Liste auf der Seite des Betreibers (developer.amazon.com/amazonbot/live-ip-addresses) |
| Seite des Betreibers gelesen am | 24. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “Because actions taken by Amzn-User can be initiated by a user, it may not follow all robots.txt directives.”

Quelle: [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot), gelesen am 24. Oktober 2026.

## Was passiert, wenn Sie Amzn-User sperren

Amazon sagt, Amzn-User befolge möglicherweise nicht alle robots.txt-Anweisungen, weil seine Aktionen von einem Nutzer ausgelöst werden können. Amazon sagt außerdem, dass die Einstellung jedes seiner User-Agents (Amazonbot, Amzn-SearchBot, Amzn-User) unabhängig von den anderen gilt und etwa 24 Stunden brauchen kann, bis Änderungen greifen.

## Die robots.txt-Zeilen

So erlauben Sie Amzn-User:

```
User-agent: Amzn-User
Allow: /
```

So sperren Sie Amzn-User:

```
User-agent: Amzn-User
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Amzn-User/0.1) Chrome/W.X.Y.Z Safari/537.36
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Amazon veröffentlicht die IP-Adressen von Amzn-User auf einer Webseite, die die Liste als JSON zeigt, und verlinkt sie von der Dokumentationsseite zu Amazonbot.

## Vergleich mit Amzn-SearchBot

[Amzn-SearchBot](/de/bots/amzn-searchbot): Amzn-SearchBot ist ein automatischer Crawler für Amazons Suchfunktionen, der laut Amazon robots.txt respektiert. Amzn-User ruft dagegen Live-Informationen ab, wenn ein Kunde fragt, und befolgt möglicherweise nicht alle Anweisungen.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). Amzn-User gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `Amzn-User` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt Amzn-User die robots.txt?

Nicht immer. Teilweise, befolgt möglicherweise nicht alle robots.txt-Anweisungen, weil Aktionen vom Nutzer ausgehen können. Eine Regel für Amzn-User in der robots.txt hält ihn deshalb möglicherweise nicht auf. Um ihn sicher abzuweisen, nutzen Sie eine Firewall- oder CDN-Regel, die User-Agent und veröffentlichte Adressen kombiniert.

### Woher weiß ich, dass Amzn-User wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot)
- [Amazon: Amzn-User IP addresses (read 2026-10-24)](https://developer.amazon.com/amazonbot/live-ip-addresses/)
