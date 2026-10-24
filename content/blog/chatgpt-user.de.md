title: ChatGPT-User: Aufgabe und Wirkung einer Sperre
h1: ChatGPT-User: Aufgabe und Wirkung einer Sperre
description: ChatGPT-User (OpenAI): Vom Nutzer ausgelöster Abruf. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: chatgpt-user
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Vier Fakten zu ChatGPT-User: Betreiber OpenAI, Aufgabe Vom Nutzer ausgelöster Abruf, befolgt robots.txt Nicht immer, Adressliste 234 Bereiche
hero_sub: ChatGPT-User, betrieben von OpenAI
hero_boxes: Betreiber|OpenAI; Aufgabe|Vom Nutzer ausgelöster Abruf; Befolgt robots.txt|Nicht immer; Adressliste|234 Bereiche
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/oai-searchbot|OAI-SearchBot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: ChatGPT-User besucht eine Webseite, wenn jemand ChatGPT oder einem Custom GPT eine Frage stellt, die diese Seite braucht. Laut OpenAI wird er nicht zum automatischen Crawlen genutzt, und weil ein Nutzer die Anfrage startet, gelten robots.txt-Regeln möglicherweise nicht. OpenAI nennt 234 IP-Bereiche dafür.

## Was ChatGPT-User ist

Anders als die übrigen OpenAI-Bots streift ChatGPT-User nicht von selbst durchs Web. OpenAI beschreibt ihn als den Agenten für bestimmte Nutzeraktionen in ChatGPT und Custom GPTs, einschließlich Seiten, die ein Custom GPT über GPT Actions erreicht. Jemand hat etwas eingetippt, und danach kam eine Anfrage bei Ihrem Server an.

| Angabe | ChatGPT-User |
| --- | --- |
| Betreiber | OpenAI |
| Aufgabe | Vom Nutzer ausgelöster Abruf |
| robots.txt-Token | `ChatGPT-User` |
| Befolgt robots.txt | robots.txt-Regeln gelten möglicherweise nicht |
| IP-Adressen | 234 Bereiche (openai.com/chatgpt-user.json, Datei vom 2026-10-20) |
| Seite des Betreibers gelesen am | 21. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “ChatGPT-User is not used for crawling the web in an automatic fashion. Because these actions are initiated by a user, robots.txt rules may not apply.”

Quelle: [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots), gelesen am 21. Oktober 2026.

## Was passiert, wenn Sie ChatGPT-User sperren

Weil der Besuch vom Nutzer ausgeht, warnt OpenAI, dass robots.txt-Regeln möglicherweise nicht gelten. Eine `Disallow`-Zeile für ChatGPT-User ist also kein garantierter Stopp. OpenAI sagt außerdem, ChatGPT-User werde nicht verwendet, um zu entscheiden, ob Inhalte in der Suche erscheinen, und verweist für Such-Opt-outs auf OAI-SearchBot. Wenn Sie diese Anfragen stoppen müssen, geschieht das auf Ihrem Server oder CDN, nicht allein in robots.txt.

## Die robots.txt-Zeilen

So erlauben Sie ChatGPT-User:

```
User-agent: ChatGPT-User
Allow: /
```

So sperren Sie ChatGPT-User:

```
User-agent: ChatGPT-User
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ChatGPT-User/1.0; +https://openai.com/bot
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Seine Adressliste ist die längste der drei OpenAI-Dateien, die wir gezählt haben: openai.com/chatgpt-user.json enthielt am 21. Oktober 2026 234 Präfixe, Erstellungszeit 2026-10-20, also einen Tag vor dieser Seite. Bei einer so langen Liste lohnt es sich, sie bei jeder Prüfung einer Logzeile neu abzurufen, statt sie einmal in eine Firewall zu kopieren.

## Vergleich mit OAI-SearchBot

[OAI-SearchBot](/de/bots/oai-searchbot): OAI-SearchBot ist der Such-Crawler und befolgt robots.txt.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet ChatGPT-User mit einer echten Anfrage und liest dafür die robots.txt. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt ChatGPT-User die robots.txt?

robots.txt-Regeln gelten möglicherweise nicht. Eine Regel für ChatGPT-User in der robots.txt hält ihn deshalb möglicherweise nicht auf. Um ihn sicher abzuweisen, nutzen Sie eine Firewall- oder CDN-Regel, die User-Agent und veröffentlichte Adressen kombiniert.

### Woher weiß ich, dass ChatGPT-User wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots)
- [openai.com/chatgpt-user.json](https://openai.com/chatgpt-user.json)
