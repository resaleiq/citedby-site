title: Applebot-Extended: Aufgabe und Wirkung einer Sperre
h1: Applebot-Extended: Aufgabe und Wirkung einer Sperre
description: Applebot-Extended (Apple): Steuer-Token. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage, gelesen auf der Seite des Betreibers.
slug: applebot-extended
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Vier Fakten zu Applebot-Extended: Betreiber Apple, Aufgabe Steuer-Token, befolgt robots.txt Nur aus robots.txt gelesen, Adressliste Keine
hero_sub: Applebot-Extended, betrieben von Apple
hero_boxes: Betreiber|Apple; Aufgabe|Steuer-Token; Befolgt robots.txt|Nur aus robots.txt gelesen; Adressliste|Keine
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/applebot|Applebot; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: Applebot-Extended ist ein robots.txt-Token. Laut Apple können Publisher mit einem Disallow dafür sorgen, dass ihre Inhalte nicht zum Training generativer Foundation-Modelle verwendet werden. Applebot darf die Seite trotzdem crawlen, sodass der Inhalt in Spotlight, Siri und Safari auffindbar bleibt. Das Token stellt selbst keine Anfragen.

## Was Applebot-Extended ist

Apples Seite beschreibt Applebot-Extended als Weg, Inhalte aus dem Training der Foundation-Modelle hinter Apple Intelligence, Diensten und Entwicklerwerkzeugen herauszuhalten. Wie [Google-Extended](/de/bots/google-extended) ist es ein Steuer-Token: In einem Log finden Sie es nicht.

| Angabe | Applebot-Extended |
| --- | --- |
| Betreiber | Apple |
| Aufgabe | Steuer-Token (stellt keine eigenen Anfragen) |
| robots.txt-Token | `Applebot-Extended` |
| Befolgt robots.txt | Wird nur aus robots.txt gelesen |
| IP-Adressen | Keine: Es ruft nie Seiten ab |
| Seite des Betreibers gelesen am | 21. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “Web publishers can opt-out from having their content used to train generative foundation models by disallowing Applebot-Extended in the robots.txt file.”

Quelle: [Apple Support: About Applebot](https://support.apple.com/en-us/119829), gelesen am 21. Oktober 2026.

## Was passiert, wenn Sie Applebot-Extended sperren

Apple nennt die Grenze ausdrücklich: Wenn Sie Applebot-Extended per Disallow ausschließen und Inhalte zusätzlich mit dem Meta-Tag nosnippet kennzeichnen, erlauben Ihre Anweisungen Applebot möglicherweise trotzdem, die Seite zu crawlen, und der Inhalt bleibt über Spotlight, Siri und Safari auffindbar. Laut derselben Seite können Publisher der Verwendung in Antworten mit breitem Weltwissen widersprechen, indem sie diese robots.txt-Steuerung anwenden.

## Die robots.txt-Zeilen

So erlauben Sie Applebot-Extended:

```
User-agent: Applebot-Extended
Allow: /
```

So sperren Sie Applebot-Extended:

```
User-agent: Applebot-Extended
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Für ein Token, das keine Anfragen sendet, gibt es keine Prüfung im Netzwerk. Lesen Sie robots.txt auf jedem Host und prüfen Sie Applebot getrennt, denn die beiden Tokens sind unabhängig, und eine einzelne Gruppe `User-agent: Applebot-Extended` sagt nichts über Applebot aus.

Applebot-Extended sendet selbst keine Anfragen und taucht deshalb nie in Ihrem Server-Log auf. Es wird nur aus der robots.txt gelesen.

## Vergleich mit Applebot

[Applebot](/de/bots/applebot): Der Crawler selbst: Wenn Sie ihn zulassen, bleiben Sie in der Suche von Spotlight, Siri und Safari.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). Applebot-Extended gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `Applebot-Extended` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt Applebot-Extended die robots.txt?

Wird nur aus robots.txt gelesen. Es sendet selbst keine Anfragen, an der Firewall gibt es also nichts zu sperren: Die Regel in der robots.txt ist die ganze Steuerung.

### Woher weiß ich, dass Applebot-Extended wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Apple Support: About Applebot](https://support.apple.com/en-us/119829)
