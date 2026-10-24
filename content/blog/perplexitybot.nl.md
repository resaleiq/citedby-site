title: PerplexityBot: wat het doet en wat blokkeren verandert
h1: PerplexityBot: wat het doet en wat blokkeren verandert
description: PerplexityBot (Perplexity): zoeken. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert, gelezen op de pagina van de aanbieder.
slug: perplexitybot
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Vier feiten over PerplexityBot: aanbieder Perplexity, taak Zoeken, volgt robots.txt Ja, adreslijst 8 bereiken
hero_sub: PerplexityBot, beheerd door Perplexity
hero_boxes: Aanbieder|Perplexity; Taak|Zoeken; Volgt robots.txt|Ja; Adreslijst|8 bereiken
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/perplexity-user|Perplexity-User; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: PerplexityBot is de crawler van Perplexity om websites te tonen en te linken in zijn zoekresultaten. Perplexity zegt dat hij niet wordt gebruikt om content te crawlen voor AI-foundation-modellen. Hij volgt robots.txt, wijzigingen kunnen tot 24 uur duren en Perplexity publiceert 8 IP-bereiken voor de crawler.

## Wat PerplexityBot is

Perplexity noemt twee agents. PerplexityBot bouwt de zoekindex en Perplexity-User bezoekt een pagina als iemand erom vraagt. De pagina van Perplexity bevat configuratierichtlijnen voor populaire WAF-aanbieders, omdat een firewall de crawler kan stoppen voordat robots.txt ertoe doet.

| Gegeven | PerplexityBot |
| --- | --- |
| Aanbieder | Perplexity |
| Taak | Zoeken |
| robots.txt-token | `PerplexityBot` |
| Volgt robots.txt | Ja, volgt robots.txt |
| IP-adressen | 8 bereiken (perplexity.com/perplexitybot.json, bestand van 2025-02-07) |
| Pagina van de aanbieder gelezen op | 21 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “PerplexityBot is designed to surface and link websites in search results on Perplexity. It is not used to crawl content for AI foundation models.”

Bron: [Perplexity: Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers), gelezen op 21 oktober 2026.

## Wat gebeurt er als je PerplexityBot blokkeert

Perplexity adviseert PerplexityBot toe te staan in robots.txt en verzoeken van de gepubliceerde IP-bereiken toe te laten als je in de zoekresultaten wilt verschijnen. Perplexity zegt ook dat het tot 24 uur kan duren voordat wijzigingen in je robots.txt in zijn systemen zijn doorgevoerd. Een controle een uur na een aanpassing zegt dus weinig.

## De robots.txt-regels

Om PerplexityBot toe te staan:

```
User-agent: PerplexityBot
Allow: /
```

Om PerplexityBot te blokkeren:

```
User-agent: PerplexityBot
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

Het bestand van Perplexity op perplexity.com/perplexitybot.json bevatte op 21 oktober 2026 8 prefixen, met aanmaaktijd 2025-02-07. In het WAF-gedeelte stelt Perplexity een regel voor die de user agent combineert met de IP-voorwaarde, zodat een verzoek dat de naam claimt vanaf een ander adres niet doorkomt.

## Vergelijk met Perplexity-User

[Perplexity-User](/nl/bots/perplexity-user): De door de gebruiker gestarte fetcher. Perplexity zegt dat die robots.txt meestal negeert.

## Je eigen site

De gratis check in het kader hierboven test PerplexityBot met een echt verzoek en leest daarvoor robots.txt. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt PerplexityBot robots.txt?

Ja, volgt robots.txt. Geef PerplexityBot in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat PerplexityBot echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Perplexity: Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers)
- [perplexity.com/perplexitybot.json](https://www.perplexity.ai/perplexitybot.json)
