title: ICC-Crawler: wat het doet en wat blokkeren verandert
h1: ICC-Crawler: wat het doet en wat blokkeren verandert
description: ICC-Crawler (NICT (Universal Communication Research Institute)): training. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert.
slug: icc-crawler
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over ICC-Crawler: aanbieder NICT (Universal Communication Research Institute), taak Training, volgt robots.txt Ja, adreslijst Lijst op zijn pagina
hero_sub: ICC-Crawler, beheerd door NICT (Universal Communication Research Institute)
hero_boxes: Aanbieder|NICT (Universal Communication Research Institute); Taak|Training; Volgt robots.txt|Ja; Adreslijst|Lijst op zijn pagina
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/gptbot|GPTBot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: ICC-Crawler wordt beheerd door het Universal Communication Research Institute van het Japanse NICT. NICT zegt dat het verzamelde pagina's gebruikt voor onderzoek naar informatieverwerking, waaronder meertalige vertaling, informatieanalyse en kunstmatige intelligentie. Het ondersteunt het Robots Exclusion Protocol: User-agent: ICC-Crawler met Disallow: / kan het verzamelen van alle pagina's uitschakelen.

## Wat ICC-Crawler is

ICC-Crawler is een crawler die wordt beheerd door het Universal Communication Research Institute van het Japanse National Institute of Information and Communications Technology (NICT). NICT zegt dat het verzamelde pagina's gebruikt voor onderzoek en ontwikkeling van informatieverwerkingstechnologieën, waaronder meertalige vertaling, informatieanalyse en kunstmatige intelligentie. NICT kan verzamelde informatie of onderzoeksresultaten ook aan derden verstrekken, voor zover de wet dat toestaat.

| Gegeven | ICC-Crawler |
| --- | --- |
| Aanbieder | NICT (Universal Communication Research Institute) |
| Taak | Onderzoeksdata verzamelen (inclusief AI-onderzoek en -ontwikkeling) |
| robots.txt-token | `ICC-Crawler` |
| Volgt robots.txt | Ja, en bij een Crawl-Delay gebruikt hij het grootste van dat interval en zijn eigen minimum |
| IP-adressen | Lijst op de pagina van de aanbieder (ucri.nict.go.jp/en/icccrawler.html) |
| Pagina van de aanbieder gelezen op | 24 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “NICT uses the information it collects for research and development of advanced information processing technologies including multilingual translation, information analysis, and artificial intelligence technologies.”

Bron: [NICT Universal Communication Research Institute: ICC-Crawler](https://ucri.nict.go.jp/en/icccrawler.html), gelezen op 24 oktober 2026.

## Wat gebeurt er als je ICC-Crawler blokkeert

NICT zegt dat ICC-Crawler het Robots Exclusion Protocol ondersteunt en dat User-agent: ICC-Crawler met Disallow: / in robots.txt het verzamelen van alle pagina's kan uitschakelen. Site-eigenaren kunnen ook een pad of bestandstype blokkeren, of geselecteerde paden toestaan onder een volledige Disallow. Blijft de toegang daarna doorgaan, dan vraagt NICT site-eigenaren contact op te nemen, zodat het kan stoppen met verzamelen van de host.

## De robots.txt-regels

Om ICC-Crawler toe te staan:

```
User-agent: ICC-Crawler
Allow: /
```

Om ICC-Crawler te blokkeren:

```
User-agent: ICC-Crawler
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De pagina van de aanbieder toont geen volledige user-agent-string voor ICC-Crawler.

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

De pagina van de aanbieder vermeldt de IP-adressen van de crawler als platte tekst. Er is geen machineleesbare lijst.

## Vergelijk met GPTBot

[GPTBot](/nl/bots/gptbot): Beide verzamelen pagina's die bijdragen aan AI-ontwikkeling. ICC-Crawler wordt echter beheerd door een Japans publiek onderzoeksinstituut voor eigen onderzoek en publiceert twee IP-adressen van de crawler op zijn pagina. GPTBot wordt beheerd door een commercieel bedrijf.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). ICC-Crawler is er niet bij: kijk in je robots.txt of er een groep `ICC-Crawler` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt ICC-Crawler robots.txt?

Ja, en bij een Crawl-Delay gebruikt hij het grootste van dat interval en zijn eigen minimum. Geef ICC-Crawler in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat ICC-Crawler echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [NICT Universal Communication Research Institute: ICC-Crawler](https://ucri.nict.go.jp/en/icccrawler.html)
