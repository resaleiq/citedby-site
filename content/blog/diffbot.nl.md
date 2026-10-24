title: Diffbot: wat het doet en wat blokkeren verandert
h1: Diffbot: wat het doet en wat blokkeren verandert
description: Diffbot (Diffbot): zoeken. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert, gelezen op de pagina van de aanbieder.
slug: diffbot
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over Diffbot: aanbieder Diffbot, taak Zoeken, volgt robots.txt Ja, adreslijst Geen
hero_sub: Diffbot, beheerd door Diffbot
hero_boxes: Aanbieder|Diffbot; Taak|Zoeken; Volgt robots.txt|Ja; Adreslijst|Geen
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/bingbot|Bingbot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: Diffbot beschrijft twee user agents. Diffbot crawlt het web proactief voor een algemene zoekmachine, zodat sites kunnen worden gevonden en geciteerd vanuit de Knowledge Graph. Diffbot-User haalt een URL op voor iemand die de software gebruikt. Diffbot zegt dat zijn crawls standaard robots.txt volgen, inclusief disallow en crawl-delay.

## Wat Diffbot is

Diffbot beschrijft twee user agents. Diffbot wordt gebruikt voor algemeen, proactief crawlen van het web om een algemene zoekmachine te bouwen, zodat sites kunnen worden gevonden en geciteerd vanuit de Diffbot Knowledge Graph en webzoekdiensten. Diffbot-User wordt gebruikt voor verzoeken namens een mens die met Diffbot-software een URL bekijkt.

| Gegeven | Diffbot |
| --- | --- |
| Aanbieder | Diffbot |
| Taak | Zoeken (algemene webcrawl) |
| robots.txt-token | `Diffbot` |
| Volgt robots.txt | Ja, standaard (disallow- en crawl-delay-regels) |
| IP-adressen | Niet gepubliceerd |
| Pagina van de aanbieder gelezen op | 24 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “By default Diffbot's web crawls adhere to a site’s robots.txt instructions, including the disallow and crawl-delay directives.”

Bron: [Diffbot: Does Diffbot respect robots.txt?](https://www.diffbot.com/docs/crawl/faq/robots-txt), gelezen op 24 oktober 2026.

## Wat gebeurt er als je Diffbot blokkeert

Diffbot zegt dat zijn webcrawls standaard robots.txt volgen, inclusief disallow en crawl-delay, en dat een regel in specifieke gevallen kan worden overschreven, zoals bij een partnerschap of overeenkomst met de site. Diffbot en Diffbot-User staan als aparte user agents vermeld. Gebruikers van de Extract- en Crawlbot-API's stellen volgens Diffbot hun eigen crawlparameters in en kunnen hun eigen User-Agent instellen.

## De robots.txt-regels

Om Diffbot toe te staan:

```
User-agent: Diffbot
Allow: /
```

Om Diffbot te blokkeren:

```
User-agent: Diffbot
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
Diffbot
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

Op de pagina van de aanbieder staat geen IP-lijst of verificatiemethode.

## Vergelijk met Bingbot

[Bingbot](/nl/bots/bingbot): Diffbot wordt door de aanbieder omschreven als vergelijkbaar met Googlebot en Bing: een algemene crawler voor een zoekindex. Volgens de aanbieder wordt hij niet gebruikt voor AI-training.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). Diffbot is er niet bij: kijk in je robots.txt of er een groep `Diffbot` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt Diffbot robots.txt?

Ja, standaard (disallow- en crawl-delay-regels). Geef Diffbot in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat Diffbot echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Diffbot: Does Diffbot respect robots.txt? (read 2026-10-24)](https://www.diffbot.com/docs/crawl/faq/robots-txt)
