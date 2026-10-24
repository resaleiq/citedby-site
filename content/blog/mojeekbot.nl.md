title: MojeekBot: wat het doet en wat blokkeren verandert
h1: MojeekBot: wat het doet en wat blokkeren verandert
description: MojeekBot (Mojeek): zoeken. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert, gelezen op de pagina van de aanbieder.
slug: mojeekbot
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over MojeekBot: aanbieder Mojeek, taak Zoeken, volgt robots.txt Ja, adreslijst 1 bereiken
hero_sub: MojeekBot, beheerd door Mojeek
hero_boxes: Aanbieder|Mojeek; Taak|Zoeken; Volgt robots.txt|Ja; Adreslijst|1 bereiken
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/bingbot|Bingbot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: MojeekBot is de webcrawler van de zoekmachine Mojeek. Mojeek zegt dat hij de Robots Exclusion Standard volgt, het eerste record gebruikt waarvan de User-Agent MojeekBot bevat en de niet-standaard crawl-delay-regel niet ondersteunt. Hij hoort niet meer dan één pagina per seconde van een site op te vragen.

## Wat MojeekBot is

MojeekBot is de webcrawler van de zoekmachine Mojeek. Mojeek zegt dat hij niet meer dan één pagina van een site binnen dezelfde periode van 1 seconde hoort op te vragen. Hij volgt de meta-tags noindex, nocache en nofollow.

| Gegeven | MojeekBot |
| --- | --- |
| Aanbieder | Mojeek |
| Taak | Zoeken |
| robots.txt-token | `MojeekBot` |
| Volgt robots.txt | Ja, volgt de Robots Exclusion Standard; crawl-delay wordt niet ondersteund |
| IP-adressen | 1 bereiken (www.mojeek.com/mojeekbot.json, bestand van 2025-05-14) |
| Pagina van de aanbieder gelezen op | 24 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “MojeekBot is the web crawler for the Mojeek search engine.”

Bron: [Mojeek: MojeekBot](https://www.mojeek.com/bot.html), gelezen op 24 oktober 2026.

## Wat gebeurt er als je MojeekBot blokkeert

Mojeek zegt dat MojeekBot het eerste robots.txt-record volgt waarvan de User-Agent MojeekBot bevat, en anders het eerste record voor User-Agent *. Hij haalt geen URL's op die een uitgesloten tekenreeks bevatten. Hij ondersteunt de niet-standaard crawl-delay-regel niet.

## De robots.txt-regels

Om MojeekBot toe te staan:

```
User-agent: MojeekBot
Allow: /
```

Om MojeekBot te blokkeren:

```
User-agent: MojeekBot
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
MojeekBot
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

Het bestand www.mojeek.com/mojeekbot.json bevatte op 24 oktober 2026 1 bereiken, bestand van 2025-05-14.

Mojeek zegt dat je het bezoekende IP-adres reverse moet opzoeken naar een naam in het domein mojeek.com en die naam weer forward moet opzoeken naar hetzelfde IP-adres, of het IP-adres moet vergelijken met de gepubliceerde lijst met MojeekBot-IP-adressen.

## Vergelijk met Bingbot

[Bingbot](/nl/bots/bingbot): Beide crawlen voor een zoekmachine. Mojeek publiceert een IP-lijst met één bereik en een reverse DNS-controle, en ondersteunt crawl-delay niet.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). MojeekBot is er niet bij: kijk in je robots.txt of er een groep `MojeekBot` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt MojeekBot robots.txt?

Ja, volgt de Robots Exclusion Standard; crawl-delay wordt niet ondersteund. Geef MojeekBot in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat MojeekBot echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Mojeek: MojeekBot](https://www.mojeek.com/bot.html)
- [MojeekBot IP list (JSON, creationTime 2025-05-14, read 2026-10-24)](https://www.mojeek.com/mojeekbot.json)
