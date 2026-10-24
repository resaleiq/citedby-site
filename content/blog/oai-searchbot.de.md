title: OAI-SearchBot: Aufgabe und Wirkung einer Sperre
h1: OAI-SearchBot: Aufgabe und Wirkung einer Sperre
description: OAI-SearchBot (OpenAI): Suche. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: oai-searchbot
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Vier Fakten zu OAI-SearchBot: Betreiber OpenAI, Aufgabe Suche, befolgt robots.txt Ja, Adressliste 39 Bereiche
hero_sub: OAI-SearchBot, betrieben von OpenAI
hero_boxes: Betreiber|OpenAI; Aufgabe|Suche; Befolgt robots.txt|Ja; Adressliste|39 Bereiche
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/gptbot|GPTBot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: OAI-SearchBot ist OpenAIs Crawler für die ChatGPT-Suche. Laut OpenAI werden Websites, die ihm per Opt-out widersprechen, in den Antworten der ChatGPT-Suche nicht angezeigt, können aber weiterhin als Navigationslinks erscheinen. Der Bot befolgt robots.txt unter dem Token OAI-SearchBot, und OpenAI veröffentlicht 39 IP-Bereiche dafür.

## Was OAI-SearchBot ist

OpenAI betreibt mehrere Crawler und sagt, dass jede Einstellung unabhängig von den anderen gilt. OAI-SearchBot entscheidet darüber, ob Ihre Seiten in den Suchfunktionen von ChatGPT erscheinen können. Er ist nicht der Crawler für das Training (das ist [GPTBot](/de/bots/gptbot)) und nicht der Abrufer, der eine Seite öffnet, wenn jemand danach fragt (das ist [ChatGPT-User](/de/bots/chatgpt-user)).

| Angabe | OAI-SearchBot |
| --- | --- |
| Betreiber | OpenAI |
| Aufgabe | Suche |
| robots.txt-Token | `OAI-SearchBot` |
| Befolgt robots.txt | Ja, er befolgt robots.txt |
| IP-Adressen | 39 Bereiche (openai.com/searchbot.json, Datei vom 2026-01-02) |
| Seite des Betreibers gelesen am | 21. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “OAI-SearchBot is used to surface websites in search results in ChatGPT's search features. Sites that are opted out of OAI-SearchBot will not be shown in ChatGPT search answers, though can still appear as navigational links.”

Quelle: [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots), gelesen am 21. Oktober 2026.

## Was passiert, wenn Sie OAI-SearchBot sperren

OpenAIs eigene Formulierung lautet, dass Websites mit Opt-out „in den Antworten der ChatGPT-Suche nicht angezeigt werden“. Das sind die Kosten: Ein Shop, der OAI-SearchBot sperrt, verzichtet auf den Teil von ChatGPT, der auf Quellen verlinkt. Für Websites, die erscheinen wollen, empfiehlt OpenAI das Gegenteil: OAI-SearchBot in robots.txt zulassen und Anfragen aus seinen veröffentlichten IP-Bereichen zulassen.

## Die robots.txt-Zeilen

So erlauben Sie OAI-SearchBot:

```
User-agent: OAI-SearchBot
Allow: /
```

So sperren Sie OAI-SearchBot:

```
User-agent: OAI-SearchBot
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36; compatible; OAI-SearchBot/1.4; +https://openai.com/searchbot
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

OpenAI veröffentlicht die Adressen, die OAI-SearchBot nutzt, unter openai.com/searchbot.json. Am 21. Oktober 2026 enthielt die Datei 39 Präfixe und trug die Erstellungszeit 2026-01-02. Gleichen Sie die Adresse in Ihrem Serverlog mit diesen Präfixen ab, bevor Sie einer Anfrage trauen, die den Namen nur im User-Agent behauptet. OpenAI sagt außerdem, dass es beim Abruf von robots.txt einen Marker `robots.txt` an den User-Agent-String anhängen kann, sodass sich diese Anfragen in Logs ohne Pfade leicht unterscheiden lassen.

## Vergleich mit GPTBot

[GPTBot](/de/bots/gptbot): GPTBot ist für das Training; wenn Sie ihn sperren, verschwinden Sie nicht aus der ChatGPT-Suche, weil die Einstellungen unabhängig sind.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet OAI-SearchBot mit einer echten Anfrage und liest dafür die robots.txt. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt OAI-SearchBot die robots.txt?

Ja, er befolgt robots.txt. Geben Sie OAI-SearchBot in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass OAI-SearchBot wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots)
- [openai.com/searchbot.json](https://openai.com/searchbot.json)
