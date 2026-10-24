title: ImagesiftBot: Aufgabe und Wirkung einer Sperre
h1: ImagesiftBot: Aufgabe und Wirkung einer Sperre
description: ImagesiftBot (Hive (ImageSift)): Suche. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: imagesiftbot
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu ImagesiftBot: Betreiber Hive (ImageSift), Aufgabe Suche, befolgt robots.txt Ja, Adressliste Keine
hero_sub: ImagesiftBot, betrieben von Hive (ImageSift)
hero_boxes: Betreiber|Hive (ImageSift); Aufgabe|Suche; Befolgt robots.txt|Ja; Adressliste|Keine
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/googlebot|Googlebot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: ImagesiftBot ist der Crawler von ImageSift, einem Produkt von Hive. Er sammelt öffentlich verfügbare Bilder samt Host-URL, Seitentext und Alt-Text der Bilder für einen Index, mit dem nach ähnlichen Bildern gesucht wird. Laut Anbieter respektiert er robots.txt und Crawl-delay und folgt den Regeln für Googlebot, wenn keine ihn betrifft.

## Was ImagesiftBot ist

ImageSiftBot ist der Crawler von ImageSift, einem Produkt von Hive. Er sammelt öffentlich verfügbare Bilder zusammen mit der Host-URL, dem Seitentext und dem Alt-Text der Bilder. ImageSift speichert die Daten in einem Index, den seine Produkte für die Suche nach ähnlichen Bildern und deren Abruf nutzen.

| Angabe | ImagesiftBot |
| --- | --- |
| Betreiber | Hive (ImageSift) |
| Aufgabe | Bildindex für die Suche nach ähnlichen Bildern |
| robots.txt-Token | `ImagesiftBot` |
| Befolgt robots.txt | Ja, und er unterstützt Crawl-delay |
| IP-Adressen | Keine veröffentlicht |
| Seite des Betreibers gelesen am | 24. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “ImageSiftBot is a web crawler that scrapes the internet for publicly available images to support our suite of web intelligence products”

Quelle: [Imagesift by Hive: ImageSift Bot](https://imagesift.com/about), gelesen am 24. Oktober 2026.

## Was passiert, wenn Sie ImagesiftBot sperren

Der Anbieter sagt, dass Standard-robots.txt-Anweisungen, die ImagesiftBot betreffen, respektiert werden und dass er Crawl-delay unterstützt. Betrifft keine Regel ImagesiftBot, aber eine Googlebot, folgt er den Regeln für Googlebot. Für Opt-out-Anfragen nennt die Seite außerdem support@imagesift.com.

## Die robots.txt-Zeilen

So erlauben Sie ImagesiftBot:

```
User-agent: ImagesiftBot
Allow: /
```

So sperren Sie ImagesiftBot:

```
User-agent: ImagesiftBot
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
Mozilla/5.0 (compatible; ImagesiftBot; +imagesift.com)
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Die Anbieterseite veröffentlicht weder eine IP-Liste noch ein Verifizierungsverfahren.

## Vergleich mit Googlebot

[Googlebot](/de/bots/googlebot): ImagesiftBot greift auf die robots.txt-Regeln von Googlebot zurück, wenn er keine eigenen hat, und er sammelt Bilder für einen Index ähnlicher Bilder statt für eine allgemeine Websuche.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). ImagesiftBot gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `ImagesiftBot` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt ImagesiftBot die robots.txt?

Ja, und er unterstützt Crawl-delay. Geben Sie ImagesiftBot in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass ImagesiftBot wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Imagesift by Hive: ImageSift Bot](https://imagesift.com/about)
