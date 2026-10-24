title: LinkupBot: wat het doet en wat blokkeren verandert
h1: LinkupBot: wat het doet en wat blokkeren verandert
description: LinkupBot (Linkup): zoeken. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert, gelezen op de pagina van de aanbieder.
slug: linkupbot
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over LinkupBot: aanbieder Linkup, taak Zoeken, volgt robots.txt Ja, adreslijst Lijst op zijn pagina
hero_sub: LinkupBot, beheerd door Linkup
hero_boxes: Aanbieder|Linkup; Taak|Zoeken; Volgt robots.txt|Ja; Adreslijst|Lijst op zijn pagina
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/perplexitybot|PerplexityBot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: LinkupBot is de webcrawler van Linkup. Hij haalt openbaar toegankelijke pagina's op om de zoekindex van Linkup te bouwen, die volgens Linkup zoeken en web grounding voor AI-toepassingen mogelijk maakt. Linkup zegt dat User-agent: LinkupBot met Disallow: / de hele site blokkeert en dat robots.txt geen toegangscontrolemechanisme is.

## Wat LinkupBot is

LinkupBot is de webcrawler van Linkup. Hij haalt openbaar toegankelijke pagina's op om de zoekindex van Linkup te bouwen en bij te houden, die volgens Linkup zoeken en web grounding voor AI-toepassingen mogelijk maakt.

| Gegeven | LinkupBot |
| --- | --- |
| Aanbieder | Linkup |
| Taak | Zoekindex voor AI-webzoeken |
| robots.txt-token | `LinkupBot` |
| Volgt robots.txt | Ja, de aanbieder zegt dat hij toepasselijke robots.txt-regels respecteert |
| IP-adressen | Lijst op de pagina van de aanbieder (www.linkup.so/linkupbot-ips.txt) |
| Pagina van de aanbieder gelezen op | 24 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “LinkupBot is Linkup’s web crawler. It discovers and retrieves publicly accessible webpages to build and maintain the Linkup web search index, which powers search and web grounding for AI applications.”

Bron: [Linkup: LinkupBot](https://www.linkup.so/bot), gelezen op 24 oktober 2026.

## Wat gebeurt er als je LinkupBot blokkeert

Volgens de aanbieder blokkeert User-agent: LinkupBot met Disallow: / in robots.txt de hele site. De aanbieder zegt ook dat robots-regels per host gelden, dat LinkupBot toestaan via een firewall robots.txt niet overschrijft en dat robots.txt geen toegangscontrolemechanisme is.

## De robots.txt-regels

Om LinkupBot toe te staan:

```
User-agent: LinkupBot
Allow: /
```

Om LinkupBot te blokkeren:

```
User-agent: LinkupBot
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
LinkupBot/1.0 (LinkupBot for web indexing; https://www.linkup.so/bot; bot@linkup.so)
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

De aanbieder zegt dat verzoeken afkomstig zijn van de CIDR-bereiken in zijn gepubliceerde lijst, en dat je moet verifiëren met zowel een bron-IP uit die lijst als een user agent met het token LinkupBot.

## Vergelijk met PerplexityBot

[PerplexityBot](/nl/bots/perplexitybot): Beide bouwen een zoekindex die AI-antwoorden voedt. De index van LinkupBot bedient AI-toepassingen via de zoek- en grounding-dienst van Linkup, en de IP-lijst is een tekstbestand, geen JSON.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). LinkupBot is er niet bij: kijk in je robots.txt of er een groep `LinkupBot` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt LinkupBot robots.txt?

Ja, de aanbieder zegt dat hij toepasselijke robots.txt-regels respecteert. Geef LinkupBot in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat LinkupBot echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Linkup: LinkupBot](https://www.linkup.so/bot)
- [Linkup: linkupbot-ips.txt (plain text, read 2026-10-24)](https://www.linkup.so/linkupbot-ips.txt)
