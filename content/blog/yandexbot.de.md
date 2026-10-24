title: YandexBot: Aufgabe und Wirkung einer Sperre
h1: YandexBot: Aufgabe und Wirkung einer Sperre
description: YandexBot (Yandex): Suche. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: yandexbot
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu YandexBot: Betreiber Yandex, Aufgabe Suche, befolgt robots.txt Ja, Adressliste Reverse-DNS
hero_sub: YandexBot, betrieben von Yandex
hero_boxes: Betreiber|Yandex; Aufgabe|Suche; Befolgt robots.txt|Ja; Adressliste|Reverse-DNS
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/googlebot|Googlebot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: YandexBot führt Yandex als seinen wichtigsten Indexierungsroboter auf, einen von vielen Yandex-Robotern mit eigenen User-Agents. Laut Yandex laden einige von ihnen Seiten zu anderen Zwecken als der Indexierung herunter und ignorieren möglicherweise restriktive Regeln, die für alle Roboter gelten (User-agent: *). Yandex veröffentlicht keine IP-Liste.

## Was YandexBot ist

YandexBot wird von Yandex als wichtigster Indexierungsroboter aufgeführt. Yandex betreibt viele weitere Roboter mit eigenen User-Agents (für Bilder, Video, Werbung, Mobilseiten, Favicons und mehr), die auf derselben Seite aufgeführt sind. Yandex veröffentlicht keine IP-Liste für seine Bots.

| Angabe | YandexBot |
| --- | --- |
| Betreiber | Yandex |
| Aufgabe | Suche (wichtigster Indexierungsroboter) |
| robots.txt-Token | `Yandex` |
| Befolgt robots.txt | Ja, berücksichtigt die allgemeinen Regeln in robots.txt (User-agent: *) |
| IP-Adressen | Prüfung per Reverse-DNS |
| Seite des Betreibers gelesen am | 24. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “Some robots can disguise themselves as Yandex robots by indicating the relevant User Agent. You can check the authenticity of a robot using a reverse DNS lookup.”

Quelle: [Yandex Webmaster: How to check that a robot belongs to Yandex](https://yandex.com/support/webmaster/en/robot-workings/check-yandex-robots), gelesen am 24. Oktober 2026.

## Was passiert, wenn Sie YandexBot sperren

Yandex sagt, dass eine Reihe seiner Roboter Seiten zu anderen Zwecken als der Indexierung herunterlädt und restriktive Regeln, die für alle Roboter gelten (User-agent: *), möglicherweise ignoriert. Um diese Roboter einzuschränken, brauchen Sie Anweisungen, die speziell für sie geschrieben sind, zum Beispiel User-agent: YandexCalendar. Yandex ergänzt, dass ein Dokument, auf das der wichtigste Yandex-Roboter nicht zugreifen kann, nie indexiert wird und in den Suchergebnissen nicht zu finden ist.

## Die robots.txt-Zeilen

So erlauben Sie YandexBot:

```
User-agent: Yandex
Allow: /
```

So sperren Sie YandexBot:

```
User-agent: Yandex
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Yandex sagt, man solle eine Reverse-DNS-Abfrage der IP durchführen, prüfen, ob der Hostname auf yandex.ru, yandex.net oder yandex.com endet, und das dann mit einer Forward-Abfrage bestätigen; außerdem gibt es ein Tool zur Prüfung von IP-Adressen.

## Vergleich mit Googlebot

[Googlebot](/de/bots/googlebot): Beide sind der wichtigste Such-Indexierungscrawler ihres Betreibers; Yandex führt viele getrennte Roboter auf, von denen einige allgemeine robots.txt-Regeln ignorieren, und sagt, dass es keine IP-Liste veröffentlicht.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). YandexBot gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `Yandex` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt YandexBot die robots.txt?

Ja, berücksichtigt die allgemeinen Regeln in robots.txt (User-agent: *). Geben Sie Yandex in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass YandexBot wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Yandex Webmaster: How to check that a robot belongs to Yandex](https://yandex.com/support/webmaster/en/robot-workings/check-yandex-robots)
- [Yandex Webmaster: Using robots.txt](https://yandex.com/support/webmaster/en/controlling-robot/robots-txt)
