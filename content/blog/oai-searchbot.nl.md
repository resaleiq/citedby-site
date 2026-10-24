title: OAI-SearchBot: wat het doet en wat blokkeren verandert
h1: OAI-SearchBot: wat het doet en wat blokkeren verandert
description: OAI-SearchBot (OpenAI): zoeken. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert, gelezen op de pagina van de aanbieder.
slug: oai-searchbot
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Vier feiten over OAI-SearchBot: aanbieder OpenAI, taak Zoeken, volgt robots.txt Ja, adreslijst 39 bereiken
hero_sub: OAI-SearchBot, beheerd door OpenAI
hero_boxes: Aanbieder|OpenAI; Taak|Zoeken; Volgt robots.txt|Ja; Adreslijst|39 bereiken
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/gptbot|GPTBot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: OAI-SearchBot is de crawler van OpenAI voor het zoeken in ChatGPT. Sites die zich ervoor afmelden, worden niet getoond in de zoekantwoorden van ChatGPT, al kunnen ze nog wel als navigatielinks verschijnen. Hij volgt robots.txt onder het token OAI-SearchBot en OpenAI publiceert 39 IP-bereiken voor de crawler.

## Wat OAI-SearchBot is

OpenAI heeft meerdere crawlers en zegt dat elke instelling los staat van de andere. OAI-SearchBot bepaalt of je pagina's kunnen worden getoond in de zoekfuncties van ChatGPT. Hij is niet de trainingscrawler (dat is [GPTBot](/nl/bots/gptbot)) en ook niet de fetcher die een pagina opent als iemand erom vraagt (dat is [ChatGPT-User](/nl/bots/chatgpt-user)).

| Gegeven | OAI-SearchBot |
| --- | --- |
| Aanbieder | OpenAI |
| Taak | Zoeken |
| robots.txt-token | `OAI-SearchBot` |
| Volgt robots.txt | Ja, volgt robots.txt |
| IP-adressen | 39 bereiken (openai.com/searchbot.json, bestand van 2026-01-02) |
| Pagina van de aanbieder gelezen op | 21 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “OAI-SearchBot is used to surface websites in search results in ChatGPT's search features. Sites that are opted out of OAI-SearchBot will not be shown in ChatGPT search answers, though can still appear as navigational links.”

Bron: [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots), gelezen op 21 oktober 2026.

## Wat gebeurt er als je OAI-SearchBot blokkeert

OpenAI zegt zelf dat sites die zich afmelden „niet worden getoond in de zoekantwoorden van ChatGPT“. Dat zijn de kosten: een shop die OAI-SearchBot blokkeert, laat het deel van ChatGPT liggen dat naar bronnen linkt. Voor sites die willen verschijnen, adviseert OpenAI het omgekeerde: sta OAI-SearchBot toe in robots.txt en sta verzoeken van de gepubliceerde IP-bereiken toe.

## De robots.txt-regels

Om OAI-SearchBot toe te staan:

```
User-agent: OAI-SearchBot
Allow: /
```

Om OAI-SearchBot te blokkeren:

```
User-agent: OAI-SearchBot
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36; compatible; OAI-SearchBot/1.4; +https://openai.com/searchbot
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

OpenAI publiceert de adressen die OAI-SearchBot gebruikt op openai.com/searchbot.json. Dat bestand bevatte op 21 oktober 2026 39 prefixen en had aanmaaktijd 2026-01-02. Vergelijk het adres in je serverlog met die prefixen voordat je een verzoek vertrouwt dat alleen de naam in zijn user agent claimt. OpenAI zegt ook dat het een `robots.txt`-markering aan de user-agent-string kan toevoegen als het robots.txt ophaalt. Zulke verzoeken zijn in logs zonder paden dus makkelijk te onderscheiden.

## Vergelijk met GPTBot

[GPTBot](/nl/bots/gptbot): GPTBot is voor training. Als je hem blokkeert, verdwijn je niet uit het zoeken van ChatGPT, omdat de instellingen los van elkaar staan.

## Je eigen site

De gratis check in het kader hierboven test OAI-SearchBot met een echt verzoek en leest daarvoor robots.txt. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt OAI-SearchBot robots.txt?

Ja, volgt robots.txt. Geef OAI-SearchBot in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat OAI-SearchBot echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots)
- [openai.com/searchbot.json](https://openai.com/searchbot.json)
