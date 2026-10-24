title: Applebot: wat het doet en wat blokkeren verandert
h1: Applebot: wat het doet en wat blokkeren verandert
description: Applebot (Apple): meerdere taken. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert, gelezen op de pagina van de aanbieder.
slug: applebot
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over Applebot: aanbieder Apple, taak Meerdere taken, volgt robots.txt Ja, adreslijst 24 bereiken
hero_sub: Applebot, beheerd door Apple
hero_boxes: Aanbieder|Apple; Taak|Meerdere taken; Volgt robots.txt|Ja; Adreslijst|24 bereiken
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/applebot-extended|Applebot-Extended; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: Applebot is de webcrawler van Apple. Apple zegt dat de data zoeken in Spotlight, Siri en Safari mogelijk maakt en ook kan helpen bij het trainen van de foundation-modellen van Apple. Met Disallow voor Applebot-Extended sluit je content alleen uit van training. Noemt robots.txt Applebot niet maar wel Googlebot, dan volgt Applebot de Googlebot-regels.

## Wat Applebot is

Applebot is de webcrawler van Apple. Apple zegt dat de data zoektechnologie in Spotlight, Siri en Safari mogelijk maakt, en ook kan worden gebruikt om foundation-modellen van Apple te trainen en om context te geven als AI-modellen in Apple-producten uitvoer genereren. Apple beschrijft ook een apart token Applebot-Extended en een iTMS-user agent voor Apple Podcasts.

| Gegeven | Applebot |
| --- | --- |
| Aanbieder | Apple |
| Taak | Zoeken (gecrawlde data kan ook helpen bij het trainen van Apple-modellen) |
| robots.txt-token | `Applebot` |
| Volgt robots.txt | Ja, voor algemene zoekcrawls die op Applebot gericht zijn |
| IP-adressen | 24 bereiken (search.developer.apple.com/applebot.json, bestand van 2026-09-15) |
| Pagina van de aanbieder gelezen op | 24 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “Applebot respects standard robots.txt directives in general search crawls that are targeted at Applebot.”

Bron: [Apple: About Applebot](https://support.apple.com/en-us/119829), gelezen op 24 oktober 2026.

## Wat gebeurt er als je Applebot blokkeert

Apple zegt dat je met Disallow voor Applebot-Extended content uitsluit van de training van de generatieve foundation-modellen van Apple, maar dat Applebot de site nog steeds kan crawlen en dat die vindbaar blijft via Spotlight, Siri en Safari. Een Disallow voor Applebot zelf geldt voor algemene zoekcrawls die op Applebot gericht zijn. Apple zegt dat Applebot de Googlebot-instructies volgt als robots.txt Applebot niet noemt maar Googlebot wel. Apple zegt dat de meta-tag nosnippet content uitsluit van antwoorden op basis van brede wereldkennis.

## De robots.txt-regels

Om Applebot toe te staan:

```
User-agent: Applebot
Allow: /
```

Om Applebot te blokkeren:

```
User-agent: Applebot
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15 (Applebot/0.1; +http://www.apple.com/go/applebot)
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

Het bestand search.developer.apple.com/applebot.json bevatte op 24 oktober 2026 24 bereiken, bestand van 2026-09-15.

Apple zegt dat Applebot-verkeer meestal te herkennen is via reverse DNS in het domein *.applebot.apple.com, of door het IP-adres te vergelijken met een CIDR-prefix in het gepubliceerde JSON-bestand.

## Vergelijk met Applebot-Extended

[Applebot-Extended](/nl/bots/applebot-extended): Applebot is de crawler die pagina's ophaalt voor de zoekfuncties van Apple. Applebot-Extended is het robots.txt-token dat bepaalt of gecrawlde content wordt gebruikt om de generatieve modellen van Apple te trainen.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). Applebot is er niet bij: kijk in je robots.txt of er een groep `Applebot` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt Applebot robots.txt?

Ja, voor algemene zoekcrawls die op Applebot gericht zijn. Geef Applebot in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat Applebot echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Apple: About Applebot](https://support.apple.com/en-us/119829)
- [Apple: Applebot IP CIDRs JSON (read 2026-10-24)](https://search.developer.apple.com/applebot.json)
