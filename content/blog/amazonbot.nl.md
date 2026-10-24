title: Amazonbot: wat het doet en wat blokkeren verandert
h1: Amazonbot: wat het doet en wat blokkeren verandert
description: Amazonbot (Amazon): meerdere taken. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert, gelezen op de pagina van de aanbieder.
slug: amazonbot
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Vier feiten over Amazonbot: aanbieder Amazon, taak Meerdere taken, volgt robots.txt Ja, adreslijst Lijst op zijn pagina
hero_sub: Amazonbot, beheerd door Amazon
hero_boxes: Aanbieder|Amazon; Taak|Meerdere taken; Volgt robots.txt|Ja; Adreslijst|Lijst op zijn pagina
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/duckassistbot|DuckAssistBot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: Amazonbot wordt gebruikt om de producten en diensten van Amazon te verbeteren en kan ook worden gebruikt om Amazon-AI-modellen te trainen. Op de pagina van Amazon staan ook Amzn-SearchBot, die content geschikt maakt voor zoekervaringen zoals Alexa, en Amzn-User, die mogelijk niet alle robots.txt-regels volgt. Elke instelling staat los van de andere.

## Wat Amazonbot is

Amazon beschrijft op zijn pagina drie user agents: Amazonbot, Amzn-SearchBot en Amzn-User. Amazon zegt dat elke instelling los staat van de andere en dat het ongeveer 24 uur kan duren voordat een wijziging werkt. Alleen de eerste wordt beschreven als mogelijk training van Amazon-AI-modellen.

| Gegeven | Amazonbot |
| --- | --- |
| Aanbieder | Amazon |
| Taak | Productverbetering, kan Amazon-AI-modellen trainen |
| robots.txt-token | `Amazonbot` |
| Volgt robots.txt | Ja, wijzigingen duren ongeveer 24 uur |
| IP-adressen | Lijst op de pagina van de aanbieder (developer.amazon.com/amazonbot/ip-addresses) |
| Pagina van de aanbieder gelezen op | 21 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “Amazonbot is used to improve our products and services. This helps us provide more accurate information to customers and may be used to train Amazon AI models.”

Bron: [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot), gelezen op 21 oktober 2026.

## Wat gebeurt er als je Amazonbot blokkeert

Amzn-SearchBot is bedoeld voor zoekervaringen zoals Alexa: sta je hem toe, dan komt je content in aanmerking om daar te verschijnen. Amzn-User beantwoordt live Alexa-vragen die actuele informatie nodig hebben. Amazon zegt dat deze mogelijk niet alle robots.txt-regels volgt en niet crawlt voor het trainen van generatieve AI. Een robots.txt die alleen Amazonbot noemt, beschrijft dus je beleid voor de andere twee niet.

## De robots.txt-regels

Om Amazonbot toe te staan:

```
User-agent: Amazonbot
Allow: /
```

Om Amazonbot te blokkeren:

```
User-agent: Amazonbot
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Amazonbot/0.1) Chrome/W.X.Y.Z Safari/537.36
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

Amazon publiceert de adressen voor Amazonbot en, op aparte pagina's, voor Amzn-SearchBot en voor live ophaalverzoeken. De lijsten zijn HTML-pagina's, geen JSON-bestand, dus we noemen geen aantal. Amazon zegt ook dat Amzn-SearchBot de regels in robots.txt volgt als dat bestand Amzn-SearchBot niet noemt maar andere zoekbots wel toestaat.

## Vergelijk met DuckAssistBot

[DuckAssistBot](/nl/bots/duckassistbot): Nog een ophaalrobot voor AI-antwoorden, met een vermelde opt-out en een vertraging van 72 uur.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). Amazonbot is er niet bij: kijk in je robots.txt of er een groep `Amazonbot` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt Amazonbot robots.txt?

Ja, wijzigingen duren ongeveer 24 uur. Geef Amazonbot in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat Amazonbot echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot)
- [developer.amazon.com/amazonbot/ip-addresses](https://developer.amazon.com/amazonbot/ip-addresses)
