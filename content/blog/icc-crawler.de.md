title: ICC-Crawler: Aufgabe und Wirkung einer Sperre
h1: ICC-Crawler: Aufgabe und Wirkung einer Sperre
description: ICC-Crawler (NICT (Universal Communication Research Institute)): Training. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage.
slug: icc-crawler
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu ICC-Crawler: Betreiber NICT (Universal Communication Research Institute), Aufgabe Training, befolgt robots.txt Ja, Adressliste Liste auf seiner Seite
hero_sub: ICC-Crawler, betrieben von NICT (Universal Communication Research Institute)
hero_boxes: Betreiber|NICT (Universal Communication Research Institute); Aufgabe|Training; Befolgt robots.txt|Ja; Adressliste|Liste auf seiner Seite
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/gptbot|GPTBot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: ICC-Crawler wird vom Universal Communication Research Institute des japanischen NICT betrieben. Laut NICT nutzt das Institut die gesammelten Seiten für Forschung zur Informationsverarbeitung, darunter mehrsprachige Übersetzung, Informationsanalyse und künstliche Intelligenz. Der Crawler unterstützt das Robots Exclusion Protocol: User-agent: ICC-Crawler mit Disallow: / könne das Sammeln von allen Seiten deaktivieren.

## Was ICC-Crawler ist

ICC-Crawler ist ein Crawler, den das Universal Communication Research Institute am japanischen National Institute of Information and Communications Technology (NICT) betreibt. Laut NICT nutzt es die gesammelten Seiten für Forschung und Entwicklung von Informationsverarbeitungstechnologien, darunter mehrsprachige Übersetzung, Informationsanalyse und künstliche Intelligenz. NICT kann gesammelte Informationen oder Forschungsergebnisse im gesetzlich zulässigen Rahmen auch an Dritte weitergeben.

| Angabe | ICC-Crawler |
| --- | --- |
| Betreiber | NICT (Universal Communication Research Institute) |
| Aufgabe | Datensammlung für die Forschung (auch KI-Forschung und -Entwicklung) |
| robots.txt-Token | `ICC-Crawler` |
| Befolgt robots.txt | Ja, und bei einem Crawl-Delay nutzt er den größeren Wert aus diesem Intervall und seinem eigenen Minimum |
| IP-Adressen | Liste auf der Seite des Betreibers (ucri.nict.go.jp/en/icccrawler.html) |
| Seite des Betreibers gelesen am | 24. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “NICT uses the information it collects for research and development of advanced information processing technologies including multilingual translation, information analysis, and artificial intelligence technologies.”

Quelle: [NICT Universal Communication Research Institute: ICC-Crawler](https://ucri.nict.go.jp/en/icccrawler.html), gelesen am 24. Oktober 2026.

## Was passiert, wenn Sie ICC-Crawler sperren

NICT sagt, ICC-Crawler unterstütze das Robots Exclusion Protocol, und User-agent: ICC-Crawler mit Disallow: / in robots.txt könne das Sammeln von allen Seiten deaktivieren. Websitebetreiber können auch einen Pfad oder Dateityp sperren oder unter einem vollständigen Disallow ausgewählte Pfade erlauben. Wenn der Zugriff danach weitergeht, bittet NICT die Websitebetreiber, sich zu melden, damit es das Sammeln vom Host beenden kann.

## Die robots.txt-Zeilen

So erlauben Sie ICC-Crawler:

```
User-agent: ICC-Crawler
Allow: /
```

So sperren Sie ICC-Crawler:

```
User-agent: ICC-Crawler
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Die Seite des Betreibers nennt keinen vollständigen User-Agent-String für ICC-Crawler.

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Die Anbieterseite nennt die IP-Adressen des Crawlers im Klartext; eine maschinenlesbare Liste veröffentlicht sie nicht.

## Vergleich mit GPTBot

[GPTBot](/de/bots/gptbot): Beide sammeln Seiten, die in die KI-Entwicklung einfließen, aber ICC-Crawler wird von einem japanischen öffentlichen Forschungsinstitut für die eigene Forschung betrieben und nennt auf seiner Seite zwei IP-Adressen des Crawlers, während GPTBot von einem kommerziellen Unternehmen betrieben wird.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). ICC-Crawler gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `ICC-Crawler` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt ICC-Crawler die robots.txt?

Ja, und bei einem Crawl-Delay nutzt er den größeren Wert aus diesem Intervall und seinem eigenen Minimum. Geben Sie ICC-Crawler in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass ICC-Crawler wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [NICT Universal Communication Research Institute: ICC-Crawler](https://ucri.nict.go.jp/en/icccrawler.html)
