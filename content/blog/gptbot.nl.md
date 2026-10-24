title: GPTBot: wat het doet en wat blokkeren verandert
h1: GPTBot: wat het doet en wat blokkeren verandert
description: GPTBot (OpenAI): training. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert, gelezen op de pagina van de aanbieder.
slug: gptbot
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Vier feiten over GPTBot: aanbieder OpenAI, taak Training, volgt robots.txt Ja, adreslijst 18 bereiken
hero_sub: GPTBot, beheerd door OpenAI
hero_boxes: Aanbieder|OpenAI; Taak|Training; Volgt robots.txt|Ja; Adreslijst|18 bereiken
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/oai-searchbot|OAI-SearchBot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: GPTBot is de trainingscrawler van OpenAI. Met een Disallow in robots.txt laat je OpenAI weten dat de content van de site niet mag worden gebruikt om zijn generatieve AI-foundation-modellen te trainen. Het regelt het zoeken in ChatGPT niet, want dat gebruikt OAI-SearchBot. OpenAI publiceert 18 IP-bereiken voor GPTBot.

## Wat GPTBot is

GPTBot is de crawler die mensen meestal bedoelen als ze zeggen „blokkeer OpenAI“. Volgens de pagina van OpenAI wordt hij gebruikt om content te crawlen die kan worden gebruikt bij het trainen van zijn modellen. Hij is een van de drie crawlers in de OpenAI-documentatie voor de ChatGPT-productfamilie, naast [OAI-SearchBot](/nl/bots/oai-searchbot) en [ChatGPT-User](/nl/bots/chatgpt-user).

| Gegeven | GPTBot |
| --- | --- |
| Aanbieder | OpenAI |
| Taak | Training |
| robots.txt-token | `GPTBot` |
| Volgt robots.txt | Ja, volgt robots.txt |
| IP-adressen | 18 bereiken (openai.com/gptbot.json, bestand van 2026-09-22) |
| Pagina van de aanbieder gelezen op | 21 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “GPTBot is used to make our generative AI foundation models more useful and safe. It is used to crawl content that may be used in training our generative AI foundation models. Disallowing GPTBot indicates a site's content should not be used in training generative AI foundation models.”

Bron: [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots), gelezen op 21 oktober 2026.

## Wat gebeurt er als je GPTBot blokkeert

OpenAI ziet een Disallow voor GPTBot als een signaal over training: de content mag niet worden gebruikt om generatieve AI-foundation-modellen te trainen. Op dezelfde pagina staat een voorbeeld van een site die OAI-SearchBot toestaat om in zoekresultaten te verschijnen en GPTBot uitsluit. Een blokkade hier haalt je dus niet vanzelf uit de zoekantwoorden van ChatGPT. Of je blokkeert, is een zakelijke keuze. Beide zijn legitiem.

## De robots.txt-regels

Om GPTBot toe te staan:

```
User-agent: GPTBot
Allow: /
```

Om GPTBot te blokkeren:

```
User-agent: GPTBot
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.4; +https://openai.com/gptbot
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

De GPTBot-lijst op openai.com/gptbot.json is de kortste van de drie OpenAI-bestanden die we hebben geteld: 18 prefixen op 21 oktober 2026, met aanmaaktijd 2026-09-22. Komt een verzoek met de naam GPTBot van een adres buiten die lijst, dan bewijst de naam alleen niets.

## Vergelijk met OAI-SearchBot

[OAI-SearchBot](/nl/bots/oai-searchbot): Sta die toe en sluit GPTBot uit om in het zoeken van ChatGPT te blijven en je af te melden voor training.

## Je eigen site

De gratis check in het kader hierboven test GPTBot met een echt verzoek en leest daarvoor robots.txt. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt GPTBot robots.txt?

Ja, volgt robots.txt. Geef GPTBot in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat GPTBot echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots)
- [openai.com/gptbot.json](https://openai.com/gptbot.json)
