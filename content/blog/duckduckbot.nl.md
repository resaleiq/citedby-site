title: DuckDuckBot: wat het doet en wat blokkeren verandert
h1: DuckDuckBot: wat het doet en wat blokkeren verandert
description: DuckDuckBot (DuckDuckGo): zoeken. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert, gelezen op de pagina van de aanbieder.
slug: duckduckbot
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over DuckDuckBot: aanbieder DuckDuckGo, taak Zoeken, volgt robots.txt Ja, adreslijst 486 adressen
hero_sub: DuckDuckBot, beheerd door DuckDuckGo
hero_boxes: Aanbieder|DuckDuckGo; Taak|Zoeken; Volgt robots.txt|Ja; Adreslijst|486 adressen
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/duckassistbot|DuckAssistBot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: DuckDuckBot is de webcrawler van DuckDuckGo. Volgens DuckDuckGo is zijn taak de zoekresultaten van DuckDuckGo te verbeteren. DuckDuckGo zegt dat hij WWW::RobotRules respecteert en zijn IP-adressen als lijst in JSON-vorm publiceert. DuckAssistBot, de ophaalrobot voor AI-ondersteunde antwoorden, staat op een aparte helppagina van DuckDuckGo.

## Wat DuckDuckBot is

DuckDuckBot is de webcrawler van DuckDuckGo. DuckDuckGo zegt dat zijn taak is de zoekresultaten van DuckDuckGo te verbeteren. In de helppagina's van DuckDuckGo staat DuckAssistBot op een aparte pagina.

| Gegeven | DuckDuckBot |
| --- | --- |
| Aanbieder | DuckDuckGo |
| Taak | Zoeken |
| robots.txt-token | `DuckDuckBot` |
| Volgt robots.txt | Ja, respecteert WWW::RobotRules (geen opmerking over timing gepubliceerd) |
| IP-adressen | 486 adressen (duckduckgo.com/duckduckbot.json, bestand van 2026-09-01) |
| Pagina van de aanbieder gelezen op | 24 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “DuckDuckBot’s job is to constantly improve our search results and offer users the best and most secure search experience possible.”

Bron: [DuckDuckGo Help Pages: Is DuckDuckBot related to DuckDuckGo?](https://duckduckgo.com/duckduckgo-help-pages/results/duckduckbot), gelezen op 24 oktober 2026.

## Wat gebeurt er als je DuckDuckBot blokkeert

DuckDuckGo zegt dat DuckDuckBot WWW::RobotRules respecteert, dus een Disallow-regel voor DuckDuckBot in robots.txt geldt voor deze crawler. De pagina zegt niets over wat blokkeren verandert in de resultaten van DuckDuckGo, en niets over DuckAssistBot.

## De robots.txt-regels

Om DuckDuckBot toe te staan:

```
User-agent: DuckDuckBot
Allow: /
```

Om DuckDuckBot te blokkeren:

```
User-agent: DuckDuckBot
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
DuckDuckBot/1.1; (+http://duckduckgo.com/duckduckbot.html)
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

Het bestand duckduckgo.com/duckduckbot.json bevatte op 24 oktober 2026 486 adressen, bestand van 2026-09-01.

DuckDuckGo zegt dat de crawler afkomstig is van de IP-adressen op zijn helppagina, ook beschikbaar als JSON op duckduckgo.com/duckduckbot.json.

## Vergelijk met DuckAssistBot

[DuckAssistBot](/nl/bots/duckassistbot): DuckDuckBot is de crawler voor de zoekresultaten van DuckDuckGo, terwijl DuckAssistBot door DuckDuckGo op een eigen helppagina wordt beschreven.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). DuckDuckBot is er niet bij: kijk in je robots.txt of er een groep `DuckDuckBot` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt DuckDuckBot robots.txt?

Ja, respecteert WWW::RobotRules (geen opmerking over timing gepubliceerd). Geef DuckDuckBot in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat DuckDuckBot echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [DuckDuckGo Help Pages: Is DuckDuckBot related to DuckDuckGo?](https://duckduckgo.com/duckduckgo-help-pages/results/duckduckbot)
- [DuckDuckBot IP list (JSON, creationTime 2026-09-01, read 2026-10-24)](https://duckduckgo.com/duckduckbot.json)
