title: ImagesiftBot: wat het doet en wat blokkeren verandert
h1: ImagesiftBot: wat het doet en wat blokkeren verandert
description: ImagesiftBot (Hive (ImageSift)): zoeken. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert.
slug: imagesiftbot
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over ImagesiftBot: aanbieder Hive (ImageSift), taak Zoeken, volgt robots.txt Ja, adreslijst Geen
hero_sub: ImagesiftBot, beheerd door Hive (ImageSift)
hero_boxes: Aanbieder|Hive (ImageSift); Taak|Zoeken; Volgt robots.txt|Ja; Adreslijst|Geen
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/googlebot|Googlebot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: ImagesiftBot is de crawler van ImageSift, een product van Hive. Hij verzamelt openbaar beschikbare afbeeldingen met de host-URL, paginatekst en alt-tekst van de afbeelding voor een index waarmee je op vergelijkbare afbeeldingen zoekt. De aanbieder zegt dat hij robots.txt en Crawl-delay respecteert en de Googlebot-regels volgt als er geen regels voor hem zijn.

## Wat ImagesiftBot is

ImageSiftBot is de crawler van ImageSift, een product van Hive. Hij verzamelt openbaar beschikbare afbeeldingen, samen met de host-URL, paginatekst en alt-tekst van de afbeelding. ImageSift slaat de data op in een index die zijn producten gebruiken om vergelijkbare afbeeldingen te zoeken en op te halen.

| Gegeven | ImagesiftBot |
| --- | --- |
| Aanbieder | Hive (ImageSift) |
| Taak | Afbeeldingsindex voor zoeken naar vergelijkbare afbeeldingen |
| robots.txt-token | `ImagesiftBot` |
| Volgt robots.txt | Ja, en hij ondersteunt Crawl-delay |
| IP-adressen | Niet gepubliceerd |
| Pagina van de aanbieder gelezen op | 24 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “ImageSiftBot is a web crawler that scrapes the internet for publicly available images to support our suite of web intelligence products”

Bron: [Imagesift by Hive: ImageSift Bot](https://imagesift.com/about), gelezen op 24 oktober 2026.

## Wat gebeurt er als je ImagesiftBot blokkeert

De aanbieder zegt dat standaard robots.txt-regels die op ImagesiftBot gericht zijn worden gerespecteerd en dat Crawl-delay wordt ondersteund. Is er geen regel voor ImagesiftBot maar wel voor Googlebot, dan volgt hij de Googlebot-regels. Op de pagina staat ook support@imagesift.com voor opt-outverzoeken.

## De robots.txt-regels

Om ImagesiftBot toe te staan:

```
User-agent: ImagesiftBot
Allow: /
```

Om ImagesiftBot te blokkeren:

```
User-agent: ImagesiftBot
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
Mozilla/5.0 (compatible; ImagesiftBot; +imagesift.com)
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

De pagina van de aanbieder publiceert geen IP-lijst of verificatiemethode.

## Vergelijk met Googlebot

[Googlebot](/nl/bots/googlebot): ImagesiftBot valt terug op de robots.txt-regels van Googlebot als hij geen eigen regels heeft, en hij verzamelt afbeeldingen voor een index van vergelijkbare afbeeldingen, niet voor algemeen zoeken op het web.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). ImagesiftBot is er niet bij: kijk in je robots.txt of er een groep `ImagesiftBot` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt ImagesiftBot robots.txt?

Ja, en hij ondersteunt Crawl-delay. Geef ImagesiftBot in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat ImagesiftBot echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Imagesift by Hive: ImageSift Bot](https://imagesift.com/about)
