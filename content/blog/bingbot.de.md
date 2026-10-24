title: Bingbot: Aufgabe und Wirkung einer Sperre
h1: Bingbot: Aufgabe und Wirkung einer Sperre
description: Bingbot (Microsoft): Suche. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: bingbot
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Vier Fakten zu Bingbot: Betreiber Microsoft, Aufgabe Suche, befolgt robots.txt Ja, Adressliste Prüfwerkzeug
hero_sub: Bingbot, betrieben von Microsoft
hero_boxes: Betreiber|Microsoft; Aufgabe|Suche; Befolgt robots.txt|Ja; Adressliste|Prüfwerkzeug
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/googlebot|Googlebot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: Bingbot ist der Standard-Crawler von Microsoft und übernimmt den Großteil des Crawlings für Bing. Auf Bings Hilfeseite stehen fünf Crawler: Bingbot, AdIdxBot, BingPreview, MicrosoftPreview und BingVideoPreview. Sie steuern sie über robots.txt, die Crawl-Rate dagegen über das Tool „Crawl control“ in den Bing Webmaster Tools, nicht über robots.txt.

## Was Bingbot ist

Bings Seite trägt den Titel „Overview of Bing crawlers (user agents)“ und sagt, Bing betreibe derzeit diese Haupt-Crawler: Bingbot (der Standard-Crawler), AdIdxBot (von Bing Ads genutzt, crawlt Anzeigen und folgt ihren Websites zur Qualitätskontrolle), BingPreview (Seiten-Snapshots für Bing), MicrosoftPreview (Snapshots für Microsoft-Produkte) und BingVideoPreview (Videovorschauen, nur in Bing). Bingbot, AdIdxBot, BingPreview und BingVideoPreview gibt es als Desktop- und Mobilvariante. Die Seite nennt keinen eigenen KI-Crawler. Im selben Hilfebereich steht „How To Permanently Remove a URL or Page from Bing or Copilot“; das ist die Seite, die Sie lesen sollten, wenn es um Entfernung statt um Zugriff geht.

| Angabe | Bingbot |
| --- | --- |
| Betreiber | Microsoft |
| Aufgabe | Such-Crawler |
| robots.txt-Token | `bingbot` |
| Befolgt robots.txt | Ja |
| IP-Adressen | Prüfwerkzeug |
| Seite des Betreibers gelesen am | 21. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “Bingbot is our standard crawler and handles most of our crawling needs each day.”

Quelle: [Microsoft Bing Webmaster help: Which Crawlers Does Bing Use?](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0), gelesen am 21. Oktober 2026.

## Was passiert, wenn Sie Bingbot sperren

Bings Seite sagt nicht, was eine Sperre kostet; das ist unsere Einschätzung, nicht die von Bing. Bingbot ist der Crawler, der Bing speist. Wenn Sie ihn in robots.txt per Disallow ausschließen, crawlt Bing diese Seiten nicht mehr, und alles, was auf Bings Index beruht, verliert sie ebenfalls. Bing bietet zwei Steuerungen: robots.txt sagt seinen Crawlern, wie sie mit Ihrer Website umgehen sollen, und die Bing Webmaster Tools haben ein Tool „Crawl control“, das die Crawl-Rate pro Stunde festlegt.

## Die robots.txt-Zeilen

So erlauben Sie Bingbot:

```
User-agent: bingbot
Allow: /
```

So sperren Sie Bingbot:

```
User-agent: bingbot
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm) Chrome/W.X.Y.Z Safari/537.36
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Bing sagt, User-Agent-Strings ließen sich leicht fälschen, daher stamme nicht jede Anfrage mit ihnen von einem echten Bing-Crawler. Prüfen Sie die Adresse mit dem Tool „Verify Bingbot“ oder einer der anderen Verifizierungsmethoden, die Bing beschreibt. Im User-Agent-String steht W.X.Y.Z für die Version von Microsoft Edge, mit der Bing rendert und die Bing nach eigener Aussage regelmäßig aktualisiert. Auf dieser Seite haben wir keine IP-Liste gelesen, deshalb nennen wir keine Anzahl.

## Vergleich mit Googlebot

[Googlebot](/de/bots/googlebot): Der andere wichtige Such-Crawler: ein anderes Token und eine andere Verifizierung.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet Bingbot mit einer echten Anfrage und liest dafür die robots.txt. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt Bingbot die robots.txt?

Ja. Geben Sie bingbot in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass Bingbot wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Microsoft Bing Webmaster help: Which Crawlers Does Bing Use?](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0)
