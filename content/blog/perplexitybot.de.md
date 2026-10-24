title: PerplexityBot: Aufgabe und Wirkung einer Sperre
h1: PerplexityBot: Aufgabe und Wirkung einer Sperre
description: PerplexityBot (Perplexity): Suche. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: perplexitybot
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Vier Fakten zu PerplexityBot: Betreiber Perplexity, Aufgabe Suche, befolgt robots.txt Ja, Adressliste 8 Bereiche
hero_sub: PerplexityBot, betrieben von Perplexity
hero_boxes: Betreiber|Perplexity; Aufgabe|Suche; Befolgt robots.txt|Ja; Adressliste|8 Bereiche
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/perplexity-user|Perplexity-User; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: PerplexityBot ist Perplexitys Crawler, mit dem Websites in den Suchergebnissen von Perplexity angezeigt und verlinkt werden. Laut Perplexity wird er nicht verwendet, um Inhalte für KI-Foundation-Modelle zu crawlen. Er befolgt robots.txt, Änderungen können bis zu 24 Stunden dauern, und Perplexity veröffentlicht 8 IP-Bereiche für ihn.

## Was PerplexityBot ist

Perplexity nennt zwei Agenten. PerplexityBot baut den Suchindex auf, Perplexity-User besucht eine Seite, wenn jemand danach fragt. Perplexitys Seite enthält Konfigurationsrichtlinien für gängige WAF-Anbieter, weil eine Firewall den Crawler stoppen kann, bevor robots.txt überhaupt eine Rolle spielt.

| Angabe | PerplexityBot |
| --- | --- |
| Betreiber | Perplexity |
| Aufgabe | Suche |
| robots.txt-Token | `PerplexityBot` |
| Befolgt robots.txt | Ja, er befolgt robots.txt |
| IP-Adressen | 8 Bereiche (perplexity.com/perplexitybot.json, Datei vom 2025-02-07) |
| Seite des Betreibers gelesen am | 21. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “PerplexityBot is designed to surface and link websites in search results on Perplexity. It is not used to crawl content for AI foundation models.”

Quelle: [Perplexity: Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers), gelesen am 21. Oktober 2026.

## Was passiert, wenn Sie PerplexityBot sperren

Perplexity empfiehlt, PerplexityBot in robots.txt zuzulassen und Anfragen aus seinen veröffentlichten IP-Bereichen zu erlauben, wenn Sie in den Suchergebnissen erscheinen wollen. Laut Perplexity kann es außerdem bis zu 24 Stunden dauern, bis sich Änderungen an Ihrer robots.txt in seinen Systemen zeigen, daher beweist eine Prüfung eine Stunde nach einer Änderung wenig.

## Die robots.txt-Zeilen

So erlauben Sie PerplexityBot:

```
User-agent: PerplexityBot
Allow: /
```

So sperren Sie PerplexityBot:

```
User-agent: PerplexityBot
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Perplexitys Datei unter perplexity.com/perplexitybot.json enthielt am 21. Oktober 2026 8 Präfixe, Erstellungszeit 2025-02-07. Ihr WAF-Abschnitt schlägt eine Regel vor, die User-Agent und IP-Bedingung kombiniert, sodass eine Anfrage, die den Namen von einer anderen Adresse aus behauptet, nicht durchkommt.

## Vergleich mit Perplexity-User

[Perplexity-User](/de/bots/perplexity-user): Der vom Nutzer ausgelöste Fetcher; laut Perplexity ignoriert er robots.txt in der Regel.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet PerplexityBot mit einer echten Anfrage und liest dafür die robots.txt. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt PerplexityBot die robots.txt?

Ja, er befolgt robots.txt. Geben Sie PerplexityBot in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass PerplexityBot wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Perplexity: Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers)
- [perplexity.com/perplexitybot.json](https://www.perplexity.ai/perplexitybot.json)
