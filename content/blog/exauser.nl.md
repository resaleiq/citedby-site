title: ExaUser: wat het doet en wat blokkeren verandert
h1: ExaUser: wat het doet en wat blokkeren verandert
description: ExaUser (Exa): door de gebruiker gestart ophalen. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert.
slug: exauser
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over ExaUser: aanbieder Exa, taak Door de gebruiker gestart ophalen, volgt robots.txt Niet altijd, adreslijst Controletool
hero_sub: ExaUser, beheerd door Exa
hero_boxes: Aanbieder|Exa; Taak|Door de gebruiker gestart ophalen; Volgt robots.txt|Niet altijd; Adreslijst|Controletool
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/exasearchbot|ExaSearchBot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: ExaUser is de agent waarmee Exa live een pagina ophaalt als een gebruiker, of een toepassing op basis van de Exa API, vraagt om de actuele content. Exa zegt dat robots.txt-regels mogelijk niet gelden voor zulke door de gebruiker gestarte verzoeken. Opt-outs voor zoeken en automatisch crawlen regel je met het token ExaSearchBot.

## Wat ExaUser is

ExaUser is de agent waarmee Exa live een pagina ophaalt als een gebruiker, of een toepassing op basis van de Exa API, vraagt om de actuele content. Exa zegt dat hij niet wordt gebruikt om het web automatisch te crawlen. Dat doet ExaSearchBot. Hij probeert geen logins, paywalls of CAPTCHA's te omzeilen en verstuurt geen formulieren.

| Gegeven | ExaUser |
| --- | --- |
| Aanbieder | Exa |
| Taak | Door de gebruiker gestart ophalen |
| robots.txt-token | `ExaUser` |
| Volgt robots.txt | Gedeeltelijk, de aanbieder zegt dat robots.txt-regels mogelijk niet gelden voor door de gebruiker gestarte verzoeken |
| IP-adressen | Controletool |
| Pagina van de aanbieder gelezen op | 24 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “Exa uses ExaUser to fetch a page live when a user, or an application built on the Exa API, asks for its current content.”

Bron: [Exa: ExaUser](https://crawler.exa.ai/exauser), gelezen op 24 oktober 2026.

## Wat gebeurt er als je ExaUser blokkeert

Exa zegt dat robots.txt-regels mogelijk niet gelden voor ExaUser, omdat gebruikers de verzoeken starten. Exa zegt ook dat ExaUser niet wordt gebruikt om te bepalen of content in het zoeken van Exa verschijnt, en dat opt-outs voor zoeken en automatisch crawlen worden geregeld met het token ExaSearchBot in robots.txt.

## De robots.txt-regels

Om ExaUser toe te staan:

```
User-agent: ExaUser
Allow: /
```

Om ExaUser te blokkeren:

```
User-agent: ExaUser
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
Mozilla/5.0 (compatible; ExaUser/1.0; +https://crawler.exa.ai/exauser)
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

De aanbieder zegt dat elk verzoek is ondertekend met Web Bot Auth (RFC 9421) en publiceert zijn sleutels in een openbare directory. Een IP-lijst publiceert hij niet.

## Vergelijk met ExaSearchBot

[ExaSearchBot](/nl/bots/exasearchbot): ExaSearchBot crawlt automatisch om de zoekindex van Exa op te bouwen en volgt robots.txt. ExaUser haalt een pagina alleen op als een gebruiker of toepassing erom vraagt, en volgens de aanbieder geldt robots.txt dan mogelijk niet.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). ExaUser is er niet bij: kijk in je robots.txt of er een groep `ExaUser` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt ExaUser robots.txt?

Niet altijd. Gedeeltelijk, de aanbieder zegt dat robots.txt-regels mogelijk niet gelden voor door de gebruiker gestarte verzoeken. Een regel voor ExaUser in robots.txt houdt het dus mogelijk niet tegen. Wil je het zeker weigeren, gebruik dan een firewall- of CDN-regel die user agent en gepubliceerde adressen combineert.

### Hoe weet ik dat ExaUser echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Exa: ExaUser](https://crawler.exa.ai/exauser)
- [Exa: Exa Search Crawler](https://crawler.exa.ai/)
