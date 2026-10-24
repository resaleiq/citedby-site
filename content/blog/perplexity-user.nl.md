title: Perplexity-User: wat het doet en wat blokkeren verandert
h1: Perplexity-User: wat het doet en wat blokkeren verandert
description: Perplexity-User (Perplexity): door de gebruiker gestart ophalen. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert.
slug: perplexity-user
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over Perplexity-User: aanbieder Perplexity, taak Door de gebruiker gestart ophalen, volgt robots.txt Niet altijd, adreslijst 4 bereiken
hero_sub: Perplexity-User, beheerd door Perplexity
hero_boxes: Aanbieder|Perplexity; Taak|Door de gebruiker gestart ophalen; Volgt robots.txt|Niet altijd; Adreslijst|4 bereiken
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/perplexitybot|PerplexityBot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: Perplexity-User is de fetcher van Perplexity voor gebruikersacties: als een gebruiker een vraag stelt, kan hij een pagina bezoeken om nauwkeurig te antwoorden en ernaar te linken. Perplexity zegt dat hij niet wordt gebruikt om het web te crawlen of AI-modellen te trainen, en dat hij robots.txt-regels meestal negeert omdat een gebruiker het ophalen vroeg.

## Wat Perplexity-User is

Perplexity-User is de fetcher van Perplexity voor gebruikersacties. Als een gebruiker Perplexity een vraag stelt, kan hij een webpagina bezoeken voor een nauwkeurig antwoord en een link naar de pagina in het antwoord opnemen. Perplexity zegt dat hij niet wordt gebruikt voor webcrawling of om content te verzamelen voor het trainen van AI-foundation-modellen, en dat hij los staat van PerplexityBot, die websites toont en linkt in de zoekresultaten van Perplexity.

| Gegeven | Perplexity-User |
| --- | --- |
| Aanbieder | Perplexity |
| Taak | Door de gebruiker gestart ophalen |
| robots.txt-token | `Perplexity-User` |
| Volgt robots.txt | Negeert robots.txt-regels meestal, omdat een gebruiker het ophalen vroeg |
| IP-adressen | 4 bereiken (www.perplexity.com/perplexity-user.json, bestand van 2025-10-17) |
| Pagina van de aanbieder gelezen op | 24 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “Since a user requested the fetch, this fetcher generally ignores robots.txt rules.”

Bron: [Perplexity: Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers), gelezen op 24 oktober 2026.

## Wat gebeurt er als je Perplexity-User blokkeert

Perplexity noemt Perplexity-User als robots.txt-token en zegt dat het bepaalt tot welke sites deze gebruikersverzoeken toegang hebben. Perplexity zegt ook dat deze fetcher robots.txt-regels meestal negeert omdat een gebruiker het ophalen vroeg. Volgens Perplexity werkt elke robots.txt-instelling onafhankelijk en kunnen wijzigingen tot 24 uur duren.

## De robots.txt-regels

Om Perplexity-User toe te staan:

```
User-agent: Perplexity-User
Allow: /
```

Om Perplexity-User te blokkeren:

```
User-agent: Perplexity-User
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Perplexity-User/1.0; +https://perplexity.ai/perplexity-user)
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

Het bestand www.perplexity.com/perplexity-user.json bevatte op 24 oktober 2026 4 bereiken, bestand van 2025-10-17.

Perplexity publiceert de IP-adressen van Perplexity-User als JSON-bestand en zegt dat je dat moet gebruiken als bron van waarheid voor allow-regels, in combinatie met de user-agent-string.

## Vergelijk met PerplexityBot

[PerplexityBot](/nl/bots/perplexitybot): PerplexityBot toont en linkt sites in de zoekresultaten van Perplexity, terwijl Perplexity-User een pagina ophaalt als de vraag van een gebruiker dat nodig heeft en robots.txt meestal negeert.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). Perplexity-User is er niet bij: kijk in je robots.txt of er een groep `Perplexity-User` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt Perplexity-User robots.txt?

Negeert robots.txt-regels meestal, omdat een gebruiker het ophalen vroeg. Een regel voor Perplexity-User in robots.txt houdt het dus mogelijk niet tegen. Wil je het zeker weigeren, gebruik dan een firewall- of CDN-regel die user agent en gepubliceerde adressen combineert.

### Hoe weet ik dat Perplexity-User echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Perplexity: Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers)
- [Perplexity: Perplexity-User IP addresses JSON (read 2026-10-24)](https://www.perplexity.com/perplexity-user.json)
