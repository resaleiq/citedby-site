title: Google-Extended: Aufgabe und Wirkung einer Sperre
h1: Google-Extended: Aufgabe und Wirkung einer Sperre
description: Google-Extended (Google): Steuer-Token. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: google-extended
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Vier Fakten zu Google-Extended: Betreiber Google, Aufgabe Steuer-Token, befolgt robots.txt Nur aus robots.txt gelesen, Adressliste Keine
hero_sub: Google-Extended, betrieben von Google
hero_boxes: Betreiber|Google; Aufgabe|Steuer-Token; Befolgt robots.txt|Nur aus robots.txt gelesen; Adressliste|Keine
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/googlebot|Googlebot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: Google-Extended ist ein robots.txt-Produkt-Token, mit dem Publisher steuern können, ob von Google gecrawlte Inhalte zum Training künftiger Gemini-Modelle verwendet werden dürfen. Es hat keinen eigenen HTTP-User-Agent und taucht deshalb nie in Ihren Logs auf. Laut Google hat es keinen Einfluss auf die Aufnahme in die Suche oder auf das Ranking.

## Was Google-Extended ist

Die meisten Seiten dieser Auswahl beschreiben einen Crawler, den Sie in einem Log finden können. Diesen nicht. Google sagt, Google-Extended „hat keinen eigenen HTTP-Request-User-Agent-String“: Das Crawling läuft über bestehende Google-User-Agents, und das robots.txt-Token dient der Steuerung.

| Angabe | Google-Extended |
| --- | --- |
| Betreiber | Google |
| Aufgabe | Steuer-Token (stellt keine eigenen Anfragen) |
| robots.txt-Token | `Google-Extended` |
| Befolgt robots.txt | Wird nur aus robots.txt gelesen; es gibt keinen eigenen User-Agent |
| IP-Adressen | Keine: Es ruft nie Seiten ab |
| Seite des Betreibers gelesen am | 21. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “Google-Extended is a standalone product token that web publishers can use to manage whether content Google crawls from their sites may be used for training future generations of Gemini models that power Gemini Apps and Vertex AI API for Gemini. Google-Extended does not impact a site's inclusion in Google Search nor is it used as a ranking signal in Google Search.”

Quelle: [Google Search Central: Google's common crawlers (last updated 2026-10-15)](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers), gelesen am 21. Oktober 2026.

## Was passiert, wenn Sie Google-Extended sperren

Wenn Sie `Disallow: /` unter Google-Extended eintragen, sagen Sie Google, dass es die Inhalte nicht zum Training künftiger Gemini-Modelle hinter den Gemini Apps und der Vertex AI API für Gemini verwenden darf. Google sagt außerdem, dass das die Aufnahme in die Google Suche nicht beeinflusst und kein Ranking-Signal ist. Unser Audit liest dieses Token in robots.txt als eine seiner Prüfungen; es ist das einzige Signal, das es gibt.

## Die robots.txt-Zeilen

So erlauben Sie Google-Extended:

```
User-agent: Google-Extended
Allow: /
```

So sperren Sie Google-Extended:

```
User-agent: Google-Extended
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Auf Netzwerkebene gibt es nichts zu prüfen: keinen User-Agent, keine Adressliste. Prüfen Sie robots.txt selbst, auf jedem Host, und denken Sie daran, dass eine Logsuche nach Google-Extended nichts findet, egal ob Sie es sperren oder nicht. Googles eigene Beispielgruppe zeigt, dass das Token wie jedes andere einen Allow- und einen Disallow-Pfad annehmen kann.

Google-Extended sendet selbst keine Anfragen und taucht deshalb nie in Ihrem Server-Log auf. Es wird nur aus der robots.txt gelesen.

## Vergleich mit Googlebot

[Googlebot](/de/bots/googlebot): Der Crawler, der Ihre Seiten tatsächlich für die Suche abruft.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet Google-Extended mit einer echten Anfrage und liest dafür die robots.txt. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt Google-Extended die robots.txt?

Wird nur aus robots.txt gelesen; es gibt keinen eigenen User-Agent. Es sendet selbst keine Anfragen, an der Firewall gibt es also nichts zu sperren: Die Regel in der robots.txt ist die ganze Steuerung.

### Woher weiß ich, dass Google-Extended wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Google Search Central: Google's common crawlers (last updated 2026-10-15)](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers)
