title: Kagibot: wat het doet en wat blokkeren verandert
h1: Kagibot: wat het doet en wat blokkeren verandert
description: Kagibot (Kagi): zoeken. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert, gelezen op de pagina van de aanbieder.
slug: kagibot
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over Kagibot: aanbieder Kagi, taak Zoeken, volgt robots.txt Ja, adreslijst Lijst op zijn pagina
hero_sub: Kagibot, beheerd door Kagi
hero_boxes: Aanbieder|Kagi; Taak|Zoeken; Volgt robots.txt|Ja; Adreslijst|Lijst op zijn pagina
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/googlebot|Googlebot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: Kagibot is de webcrawler van de zoekmachine Kagi. Kagi zegt dat standaard robots.txt-regels die op Kagibot gericht zijn worden gerespecteerd en dat Kagibot de Googlebot-regels volgt als er geen regel voor Kagibot is maar wel een voor Googlebot. Kagi publiceert zijn user-agent-string en de IP-adressen waarvan zijn verzoeken afkomstig zijn.

## Wat Kagibot is

Kagibot is de webcrawler van de zoekmachine Kagi. Kagi publiceert zijn user-agent-string en de IP-adressen waarvan de verzoeken van Kagibot afkomstig zijn.

| Gegeven | Kagibot |
| --- | --- |
| Aanbieder | Kagi |
| Taak | Zoeken |
| robots.txt-token | `Kagibot` |
| Volgt robots.txt | Ja, standaard robots.txt-regels die op Kagibot gericht zijn worden gerespecteerd |
| IP-adressen | Lijst op de pagina van de aanbieder (kagi.com/bot) |
| Pagina van de aanbieder gelezen op | 24 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “Standard directives in robots.txt that target Kagibot are respected.”

Bron: [Kagi: About KagiBot](https://kagi.com/bot), gelezen op 24 oktober 2026.

## Wat gebeurt er als je Kagibot blokkeert

Kagi zegt dat standaard robots.txt-regels die op Kagibot gericht zijn worden gerespecteerd, bijvoorbeeld Disallow-regels voor een pad. Is er geen regel voor Kagibot maar wel een voor Googlebot, dan volgt Kagibot de Googlebot-regels.

## De robots.txt-regels

Om Kagibot toe te staan:

```
User-agent: Kagibot
Allow: /
```

Om Kagibot te blokkeren:

```
User-agent: Kagibot
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
Mozilla/5.0 (compatible; Kagibot/1.0; +https://kagi.com/bot)
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

Kagi vermeldt op zijn botpagina de IP-adressen (met hostnamen onder kagibot.org) waarvan de verzoeken van Kagibot afkomstig zijn.

## Vergelijk met Googlebot

[Googlebot](/nl/bots/googlebot): Kagibot volgt zijn eigen robots.txt-regels en valt terug op de Googlebot-regels als er geen op Kagibot gericht zijn.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). Kagibot is er niet bij: kijk in je robots.txt of er een groep `Kagibot` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt Kagibot robots.txt?

Ja, standaard robots.txt-regels die op Kagibot gericht zijn worden gerespecteerd. Geef Kagibot in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat Kagibot echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Kagi: About KagiBot (read 2026-10-24)](https://kagi.com/bot)
