title: Baiduspider: wat het doet en wat blokkeren verandert
h1: Baiduspider: wat het doet en wat blokkeren verandert
description: Baiduspider (Baidu): zoeken. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert, gelezen op de pagina van de aanbieder.
slug: baiduspider
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over Baiduspider: aanbieder Baidu, taak Zoeken, volgt robots.txt Ja, adreslijst Reverse DNS
hero_sub: Baiduspider, beheerd door Baidu
hero_boxes: Aanbieder|Baidu; Taak|Zoeken; Volgt robots.txt|Ja; Adreslijst|Reverse DNS
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/bingbot|Bingbot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: Baiduspider is de crawler van de zoekmachine Baidu. Baidu zegt dat hij het robots.txt-protocol volgt en dat het blokkeren van Baiduspider alle Baidu-user agents blokkeert, zodat je pagina's niet in Baidu-resultaten te vinden zijn. Baiduspider-cpro en Baiduspider-ads werken op basis van klantafspraken en volgen robots.txt-records niet.

## Wat Baiduspider is

Baiduspider is de crawler van de zoekmachine Baidu. Hij bezoekt pagina's en neemt ze op in de Baidu-index. Baidu gebruikt verschillende user agents voor verschillende producten, bijvoorbeeld Baiduspider voor pc- en mobiel zoeken en Baiduspider-image, Baiduspider-video en Baiduspider-news voor die zoekopdrachten.

| Gegeven | Baiduspider |
| --- | --- |
| Aanbieder | Baidu |
| Taak | Zoeken |
| robots.txt-token | `Baiduspider` |
| Volgt robots.txt | Ja voor Baiduspider; Baiduspider-cpro en Baiduspider-ads volgen robots.txt-records niet |
| IP-adressen | Controle via reverse DNS |
| Pagina van de aanbieder gelezen op | 24 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “Baiduspider is Baidu search engine program which is used to visit pages on the internet and build information into Baidu index.”

Bron: [Baidu Help Center: FAQs of Baiduspider](https://help.baidu.com/question?prod_id=99&class=0&id=3001), gelezen op 24 oktober 2026.

## Wat gebeurt er als je Baiduspider blokkeert

Baidu zegt dat Baiduspider werkt op basis van het robots.txt-protocol en dat je pagina's bij blokkeren niet te vinden zijn in Baidu-zoekresultaten of in andere resultaten die Baidu levert. Je kunt verschillende regels instellen voor verschillende Baidu-user agents. Als je Baiduspider blokkeert, blokkeer je alle Baidu-user agents. Baiduspider-cpro en Baiduspider-ads werken op basis van afspraken met klanten en volgen robots.txt-records niet.

## De robots.txt-regels

Om Baiduspider toe te staan:

```
User-agent: Baiduspider
Allow: /
```

Om Baiduspider te blokkeren:

```
User-agent: Baiduspider
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
Baiduspider
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

Baidu raadt een reverse DNS-lookup op het bezoekende IP-adres aan. De hostnaam van Baiduspider is *.baidu.com of *.baidu.jp. Andere hostnamen zijn nep.

## Vergelijk met Bingbot

[Bingbot](/nl/bots/bingbot): Beide crawlen voor een zoekmachine. Baidu beschrijft meerdere productspecifieke user agents (afbeeldingen, video, nieuws, advertenties) onder de naam Baiduspider en verifieert via de hostnaam van reverse DNS.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). Baiduspider is er niet bij: kijk in je robots.txt of er een groep `Baiduspider` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt Baiduspider robots.txt?

Ja voor Baiduspider; Baiduspider-cpro en Baiduspider-ads volgen robots.txt-records niet. Geef Baiduspider in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat Baiduspider echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Baidu Help Center: FAQs of Baiduspider](https://help.baidu.com/question?prod_id=99&class=0&id=3001)
- [Baidu Help Center: How to block the crawling (robots.txt)](https://www.baidu.com/search/robots_english.html)
