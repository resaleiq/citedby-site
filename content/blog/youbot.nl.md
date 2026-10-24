title: YouBot: wat het doet en wat blokkeren verandert
h1: YouBot: wat het doet en wat blokkeren verandert
description: YouBot (You.com): zoeken. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert, gelezen op de pagina van de aanbieder.
slug: youbot
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over YouBot: aanbieder You.com, taak Zoeken, volgt robots.txt Ja, adreslijst Lijst op zijn pagina
hero_sub: YouBot, beheerd door You.com
hero_boxes: Aanbieder|You.com; Taak|Zoeken; Volgt robots.txt|Ja; Adreslijst|Lijst op zijn pagina
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/mojeekbot|MojeekBot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: YouBot is de webcrawler achter de zoekmachine You.com. Hij ontdekt en indexeert pagina's voor de resultaten. You.com zegt dat hij robots.txt respecteert, Crawl-delay honoreert en robots.txt 30 minuten cachet. User-agent: YouBot met Disallow: / blokkeert hem voor de hele site.

## Wat YouBot is

YouBot is de webcrawler achter de zoekmachine You.com. Hij ontdekt en indexeert webpagina's voor de zoekresultaten van You.com. You.com zegt dat X.X.X.X in de user agent staat voor het versienummer van Google Chrome.

| Gegeven | YouBot |
| --- | --- |
| Aanbieder | You.com |
| Taak | Zoeken |
| robots.txt-token | `YouBot` |
| Volgt robots.txt | Ja, robots.txt wordt 30 minuten gecachet, dus wijzigingen kunnen tot 30 minuten duren |
| IP-adressen | Lijst op de pagina van de aanbieder (you.com/docs/youbot) |
| Pagina van de aanbieder gelezen op | 24 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “YouBot is the web crawler that powers the You.com search engine.”

Bron: [You.com Docs: YouBot: You.com's Web Crawler](https://docs.you.com/youbot), gelezen op 24 oktober 2026.

## Wat gebeurt er als je YouBot blokkeert

You.com zegt dat YouBot robots.txt respecteert en noemt User-agent: YouBot met Disallow: / als manier om hem van de hele site te blokkeren. Hij honoreert ook Crawl-delay en cachet robots.txt 30 minuten. De pagina beschrijft geen andere agents van You.com.

## De robots.txt-regels

Om YouBot toe te staan:

```
User-agent: YouBot
Allow: /
```

Om YouBot te blokkeren:

```
User-agent: YouBot
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; YouBot/1.0; +https://docs.you.com/youbot; env:prod) Chrome/X.X.X.X Safari/537.36
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

You.com zegt dat verzoeken afkomstig zijn van 68.67.112.0/24, dat hosts worden omgezet naar youbot-{octets-with-hyphens}.search.you.com en dat verzoeken Cloudflare Web Bot Auth-handtekeningen dragen, met openbare sleutels op you.com/.well-known/http-message-signatures-directory.

## Vergelijk met MojeekBot

[MojeekBot](/nl/bots/mojeekbot): Beide zijn crawlers van een zoekmachine die robots.txt volgen. You.com ondersteunt Crawl-delay en ondertekent verzoeken met Web Bot Auth, terwijl Mojeek Crawl-delay niet ondersteunt.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). YouBot is er niet bij: kijk in je robots.txt of er een groep `YouBot` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt YouBot robots.txt?

Ja, robots.txt wordt 30 minuten gecachet, dus wijzigingen kunnen tot 30 minuten duren. Geef YouBot in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat YouBot echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [You.com Docs: YouBot: You.com's Web Crawler](https://docs.you.com/youbot)
