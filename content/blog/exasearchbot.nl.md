title: ExaSearchBot: wat het doet en wat blokkeren verandert
h1: ExaSearchBot: wat het doet en wat blokkeren verandert
description: ExaSearchBot (Exa): zoeken. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert, gelezen op de pagina van de aanbieder.
slug: exasearchbot
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over ExaSearchBot: aanbieder Exa, taak Zoeken, volgt robots.txt Ja, adreslijst Controletool
hero_sub: ExaSearchBot, beheerd door Exa
hero_boxes: Aanbieder|Exa; Taak|Zoeken; Volgt robots.txt|Ja; Adreslijst|Controletool
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/perplexitybot|PerplexityBot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: ExaSearchBot is de crawler van Exa, een zoekmachine voor zoeken en ophalen, zodat pagina's kunnen worden gevonden en geciteerd. Exa zegt dat hij robots.txt controleert voordat hij iets ophaalt en dat User-agent: ExaSearchBot met Disallow: / de hele site blokkeert. Elk verzoek is cryptografisch ondertekend, dus verificatie hangt niet af van een IP-adres.

## Wat ExaSearchBot is

ExaSearchBot is de crawler van Exa, een zoekmachine. Exa zegt dat het doel zoeken en ophalen is, zodat pagina's vindbaar worden en kunnen worden geciteerd. Pagina's die Exa op verzoek van een gebruiker ophaalt in plaats van te crawlen, gaan uit als ExaUser.

| Gegeven | ExaSearchBot |
| --- | --- |
| Aanbieder | Exa |
| Taak | Zoek- en ophaalindex |
| robots.txt-token | `ExaSearchBot` |
| Volgt robots.txt | Ja, de aanbieder zegt dat hij robots.txt controleert voordat hij iets ophaalt |
| IP-adressen | Controletool |
| Pagina van de aanbieder gelezen op | 24 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “Exa is a search engine. Similar to other search engines, Exa uses a robot (ExaSearchBot) to discover and index pages on the public web.”

Bron: [Exa: Exa Search Crawler](https://crawler.exa.ai/), gelezen op 24 oktober 2026.

## Wat gebeurt er als je ExaSearchBot blokkeert

Exa zegt dat User-agent: ExaSearchBot met Disallow: / ExaSearchBot van de hele site weert. Is er geen groep voor ExaSearchBot, dan volgt hij de regels voor grote zoekmachines, en anders de *-groep. Volgens de aanbieder regelt robots.txt het crawlen, niet het indexeren. Pagina's die al geïndexeerd zijn, haal je weg met een noindex-meta-tag of een X-Robots-Tag-header.

## De robots.txt-regels

Om ExaSearchBot toe te staan:

```
User-agent: ExaSearchBot
Allow: /
```

Om ExaSearchBot te blokkeren:

```
User-agent: ExaSearchBot
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
Mozilla/5.0 (compatible; ExaSearchBot/1.0; +https://crawler.exa.ai/)
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

De aanbieder zegt dat elk verzoek cryptografisch is ondertekend met HTTP Message Signatures (Web Bot Auth) en geeft een openbare sleuteldirectory om tegen te verifiëren. Volgens de aanbieder geldt die verificatie ongeacht het IP-adres.

## Vergelijk met PerplexityBot

[PerplexityBot](/nl/bots/perplexitybot): Beide zijn crawlers voor een zoekindex die AI-antwoorden voeden met geciteerde bronnen. ExaSearchBot ondertekent zijn verzoeken met Web Bot Auth en valt terug op de regels van grote zoekmachines als hij geen eigen groep heeft.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). ExaSearchBot is er niet bij: kijk in je robots.txt of er een groep `ExaSearchBot` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt ExaSearchBot robots.txt?

Ja, de aanbieder zegt dat hij robots.txt controleert voordat hij iets ophaalt. Geef ExaSearchBot in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat ExaSearchBot echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Exa: Exa Search Crawler](https://crawler.exa.ai/)
- [Exa: FAQs](https://exa.ai/docs/admin/faqs)
