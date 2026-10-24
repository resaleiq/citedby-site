title: Amzn-SearchBot: wat het doet en wat blokkeren verandert
h1: Amzn-SearchBot: wat het doet en wat blokkeren verandert
description: Amzn-SearchBot (Amazon): zoeken. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert, gelezen op de pagina van de aanbieder.
slug: amzn-searchbot
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over Amzn-SearchBot: aanbieder Amazon, taak Zoeken, volgt robots.txt Ja, adreslijst Lijst op zijn pagina
hero_sub: Amzn-SearchBot, beheerd door Amazon
hero_boxes: Aanbieder|Amazon; Taak|Zoeken; Volgt robots.txt|Ja; Adreslijst|Lijst op zijn pagina
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/amazonbot|Amazonbot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: Amzn-SearchBot is een Amazon-crawler die wordt gebruikt om zoekervaringen zoals Alexa te verbeteren. Amazon zegt dat je content in aanmerking komt om daar te verschijnen als je de crawler toestaat, en dat hij niet crawlt voor het trainen van generatieve AI-modellen. De instelling staat los van Amazonbot en Amzn-User. Een wijziging kan ongeveer 24 uur duren.

## Wat Amzn-SearchBot is

Amzn-SearchBot is een Amazon-crawler die wordt gebruikt om zoekervaringen in producten en diensten van Amazon te verbeteren. Amazon zegt dat je content in aanmerking komt om te verschijnen in zoekervaringen zoals Alexa als je de crawler toestaat, en dat hij content niet crawlt voor het trainen van generatieve AI-modellen. Het is een van drie Amazon-user agents (Amazonbot, Amzn-SearchBot, Amzn-User) die Amazon op één pagina beschrijft.

| Gegeven | Amzn-SearchBot |
| --- | --- |
| Aanbieder | Amazon |
| Taak | Zoeken |
| robots.txt-token | `Amzn-SearchBot` |
| Volgt robots.txt | Ja, wijzigingen kunnen ongeveer 24 uur duren |
| IP-adressen | Lijst op de pagina van de aanbieder (developer.amazon.com/amazonbot/searchbot-ip-addresses) |
| Pagina van de aanbieder gelezen op | 24 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “If robots.txt files don’t mention Amzn-SearchBot but allow other search bots, Amzn-SearchBot will crawl in accordance with the robots.txt directives given to other search bots.”

Bron: [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot), gelezen op 24 oktober 2026.

## Wat gebeurt er als je Amzn-SearchBot blokkeert

Amazon zegt dat geautomatiseerd crawlen door zijn genoemde user agents het Robots Exclusion Protocol respecteert, inclusief de user-agent- en allow/disallow-regels. Amazon zegt dat de instelling van elke user agent los staat van de andere en dat het ongeveer 24 uur kan duren voordat een wijziging werkt. Noemt robots.txt Amzn-SearchBot niet maar staat het andere zoekbots toe, dan volgt Amzn-SearchBot de regels die voor die andere zoekbots gelden.

## De robots.txt-regels

Om Amzn-SearchBot toe te staan:

```
User-agent: Amzn-SearchBot
Allow: /
```

Om Amzn-SearchBot te blokkeren:

```
User-agent: Amzn-SearchBot
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Amzn-SearchBot/0.1) Chrome/W.X.Y.Z Safari/537.36
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

Amazon publiceert de IP-adressen van Amzn-SearchBot op een webpagina die de lijst als JSON toont, en verwijst ernaar vanaf de documentatiepagina van Amazonbot.

## Vergelijk met Amazonbot

[Amazonbot](/nl/bots/amazonbot): Amazonbot wordt gebruikt om producten en diensten van Amazon te verbeteren en kan worden gebruikt om Amazon-AI-modellen te trainen. Amzn-SearchBot is bedoeld voor zoekervaringen en volgens Amazon crawlt die niet voor het trainen van generatieve AI-modellen.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). Amzn-SearchBot is er niet bij: kijk in je robots.txt of er een groep `Amzn-SearchBot` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt Amzn-SearchBot robots.txt?

Ja, wijzigingen kunnen ongeveer 24 uur duren. Geef Amzn-SearchBot in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat Amzn-SearchBot echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot)
- [Amazon: Amzn-SearchBot IP addresses (read 2026-10-24)](https://developer.amazon.com/amazonbot/searchbot-ip-addresses/)
