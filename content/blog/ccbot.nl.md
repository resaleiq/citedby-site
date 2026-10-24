title: CCBot: wat het doet en wat blokkeren verandert
h1: CCBot: wat het doet en wat blokkeren verandert
description: CCBot (Common Crawl): meerdere taken. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert, gelezen op de pagina van de aanbieder.
slug: ccbot
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over CCBot: aanbieder Common Crawl, taak Meerdere taken, volgt robots.txt Ja, adreslijst Reverse DNS
hero_sub: CCBot, beheerd door Common Crawl
hero_boxes: Aanbieder|Common Crawl; Taak|Meerdere taken; Volgt robots.txt|Ja; Adreslijst|Reverse DNS
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/gptbot|GPTBot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: CCBot is de crawler van Common Crawl, een non-profitorganisatie die een open archief van webcrawldata bijhoudt dat iedereen kan raadplegen en analyseren. Common Crawl zegt dat User-agent: CCBot met Disallow: / voorkomt dat de crawler een site bezoekt. Het waarschuwt ook dat andere crawlers zich ten onrechte als CCBot voordoen, dus controleer verzoeken.

## Wat CCBot is

CCBot is de crawler van Common Crawl, een non-profitstichting die een open archief van webcrawldata maakt en bijhoudt dat iedereen kan raadplegen en analyseren. Volgens de pagina van de aanbieder moet de crawldata vrij beschikbaar zijn voor organisaties, de academische wereld en non-profitorganisaties.

| Gegeven | CCBot |
| --- | --- |
| Aanbieder | Common Crawl |
| Taak | Open webcrawlarchief |
| robots.txt-token | `CCBot` |
| Volgt robots.txt | Ja, via een robots.txt-regel voor CCBot |
| IP-adressen | Controle via reverse DNS |
| Pagina van de aanbieder gelezen op | 24 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “To prevent Common Crawl from crawling your website, include the following in your robots.txt”

Bron: [Common Crawl: CCBot](https://commoncrawl.org/ccbot), gelezen op 24 oktober 2026.

## Wat gebeurt er als je CCBot blokkeert

Common Crawl zegt dat je met User-agent: CCBot en Disallow: / in robots.txt voorkomt dat Common Crawl de site crawlt. Op de pagina staat ook dat Common Crawl weet dat crawlers zich ten onrechte als CCBot voordoen, en het raadt aan user-agent-strings te verifiëren.

## De robots.txt-regels

Om CCBot toe te staan:

```
User-agent: CCBot
Allow: /
```

Om CCBot te blokkeren:

```
User-agent: CCBot
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
CCBot/2.0 (https://commoncrawl.org/faq/)
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

Common Crawl zegt dat CCBot draait op eigen IP-adresbereiken met reverse DNS (niet voor IPv6). Een gelogd verzoek kun je dus controleren met een reverse lookup die uitkomt op een hostnaam onder crawl.commoncrawl.org. De bereiken staan ook als JSON op https://index.commoncrawl.org/ccbot.json.

## Vergelijk met GPTBot

[GPTBot](/nl/bots/gptbot): CCBot bouwt een openbaar crawlarchief dat anderen kunnen gebruiken, terwijl GPTBot content verzamelt voor de eigen doeleinden van OpenAI.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). CCBot is er niet bij: kijk in je robots.txt of er een groep `CCBot` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt CCBot robots.txt?

Ja, via een robots.txt-regel voor CCBot. Geef CCBot in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat CCBot echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Common Crawl: CCBot (read 2026-10-24)](https://commoncrawl.org/ccbot)
