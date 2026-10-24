title: MistralAI-User: Aufgabe und Wirkung einer Sperre
h1: MistralAI-User: Aufgabe und Wirkung einer Sperre
description: MistralAI-User (Mistral): Vom Nutzer ausgelöster Abruf. robots.txt-Token, Wirkung eines Disallow und Prüfung einer Anfrage.
slug: mistralai-user
section: bots
locale: de
cluster: KI-Crawler
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Vier Fakten zu MistralAI-User: Betreiber Mistral, Aufgabe Vom Nutzer ausgelöster Abruf, befolgt robots.txt Ja, Adressliste 4 Bereiche
hero_sub: MistralAI-User, betrieben von Mistral
hero_boxes: Betreiber|Mistral; Aufgabe|Vom Nutzer ausgelöster Abruf; Befolgt robots.txt|Ja; Adressliste|4 Bereiche
widget: on
related: /de/bots|Alle KI-Crawler im Vergleich; /de/bots/chatgpt-user|ChatGPT-User; /de/platforms|KI-Crawler-Einstellungen je Plattform; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen? Was darüber entscheidet
answer: MistralAI-User ist der Mistral-Agent, der eine Seite besuchen kann, wenn ein Nutzer Vibe eine Frage stellt, und die Quelle in der Antwort verlinkt. Laut Mistral wird er weder zum automatischen Crawlen noch für das Training generativer KI verwendet. Auf Mistrals Seite stehen außerdem MistralAI-Index und MistralAI-Training, jeweils mit eigenem Token.

## Was MistralAI-User ist

Mistrals Crawler-Seite führt drei Agenten auf: MistralAI-User für Nutzeraktionen in Vibe, MistralAI-Index zum Indexieren von Inhalten für die Mistral-Suche und MistralAI-Training, das Webinhalte crawlt, um Datensätze für das Training generativer KI-Modelle von Mistral aufzubauen. Webmaster können jeden davon in robots.txt per Disallow ausschließen.

| Angabe | MistralAI-User |
| --- | --- |
| Betreiber | Mistral |
| Aufgabe | Vom Nutzer ausgelöster Abruf |
| robots.txt-Token | `MistralAI-User` |
| Befolgt robots.txt | Opt-out über robots.txt |
| IP-Adressen | 4 Bereiche (mistral.ai/mistralai-user-ips.json, Datei vom 2025-02-19) |
| Seite des Betreibers gelesen am | 21. Oktober 2026 |

## Was der Betreiber sagt

Die Worte des Betreibers (englisches Original): “MistralAI-User is for user actions in Vibe. When users ask Vibe a question, it may visit a web page to help answer and include a link to the source in its response.”

Quelle: [Mistral Docs: Mistral crawlers](https://docs.mistral.ai/robots), gelesen am 21. Oktober 2026.

## Was passiert, wenn Sie MistralAI-User sperren

Wenn Sie MistralAI-User per Disallow ausschließen, öffnet dieser Agent Ihre Seite nicht mehr für die Frage eines Vibe-Nutzers; Index- und Trainings-Agent bleiben davon unberührt, sie haben eigene Tokens. Laut Mistral wird der User-Agent weder zum automatischen Crawlen des Webs noch zum Crawlen von Inhalten für das Training generativer KI verwendet, und Inhalte, die der Index-Agent crawlt, werden in keiner Form für das Training generativer KI verwendet.

## Die robots.txt-Zeilen

So erlauben Sie MistralAI-User:

```
User-agent: MistralAI-User
Allow: /
```

So sperren Sie MistralAI-User:

```
User-agent: MistralAI-User
Disallow: /
```

Fügen Sie einen Block in die robots.txt im Stammverzeichnis Ihres Hosts ein, zum Beispiel https://example.com/robots.txt. Eine Gruppe für ein Token gilt nicht für die anderen Crawler desselben Betreibers.

Der User-Agent-String laut Betreiber:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; MistralAI-User/1.0; +https://docs.mistral.ai/robots)
```

## Woran Sie eine echte von einer gefälschten Anfrage unterscheiden

Mistral veröffentlicht für die Agenten getrennte Adressdateien. mistral.ai/mistralai-user-ips.json enthielt am 21. Oktober 2026 4 Präfixe (Erstellungszeit 2025-02-19) und die Index-Datei 2 Präfixe (Erstellungszeit 2026-04-19). Zwei Einträge für einen Index-Crawler sind eine Liste, die eine Firewall-Regel genau abbilden kann.

## Vergleich mit ChatGPT-User

[ChatGPT-User](/de/bots/chatgpt-user): Dieselbe Aufgabe wie bei OpenAI, mit einem anderen robots.txt-Versprechen.

## Ihre eigene Website

Der kostenlose Check im Kasten oben testet acht Crawler (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot und Googlebot). MistralAI-User gehört nicht dazu: Lesen Sie Ihre robots.txt auf eine Gruppe `MistralAI-User` und suchen Sie den User-Agent in Ihrem Server-Log. Die vollständige Liste der Crawler steht im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Befolgt MistralAI-User die robots.txt?

Opt-out über robots.txt. Geben Sie MistralAI-User in der robots.txt eine eigene User-agent-Gruppe: Die anderen Crawler desselben Betreibers haben jeweils eigene Einstellungen.

### Woher weiß ich, dass MistralAI-User wirklich gesperrt ist?

Die robots.txt ist nur eine Ebene: Auch eine CDN- oder Firewall-Regel kann einen Crawler abweisen, und ein Crawler kann die Datei ignorieren. Suchen Sie den User-Agent in Ihrem Server-Log und testen Sie die Adresse von außerhalb Ihres Netzes.

## Sources

- [Mistral Docs: Mistral crawlers](https://docs.mistral.ai/robots)
- [mistral.ai/mistralai-user-ips.json](https://mistral.ai/mistralai-user-ips.json)
