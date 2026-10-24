title: Applebot-Extended: wat het doet en wat blokkeren verandert
h1: Applebot-Extended: wat het doet en wat blokkeren verandert
description: Applebot-Extended (Apple): controletoken. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert.
slug: applebot-extended
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Vier feiten over Applebot-Extended: aanbieder Apple, taak Controletoken, volgt robots.txt Alleen uit robots.txt gelezen, adreslijst Geen
hero_sub: Applebot-Extended, beheerd door Apple
hero_boxes: Aanbieder|Apple; Taak|Controletoken; Volgt robots.txt|Alleen uit robots.txt gelezen; Adreslijst|Geen
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/applebot|Applebot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: Applebot-Extended is een robots.txt-token. Apple zegt dat uitgevers kunnen voorkomen dat hun content wordt gebruikt om generatieve foundation-modellen te trainen, door het token met Disallow uit te sluiten. Applebot kan de pagina nog steeds crawlen, dus de content blijft vindbaar in Spotlight, Siri en Safari. Het token doet zelf geen verzoeken.

## Wat Applebot-Extended is

Op de pagina van Apple staat Applebot-Extended als de manier om content buiten de training van de foundation-modellen achter Apple Intelligence, diensten en ontwikkelaarstools te houden. Net als [Google-Extended](/nl/bots/google-extended) is het een controletoken: je vindt het niet in een log.

| Gegeven | Applebot-Extended |
| --- | --- |
| Aanbieder | Apple |
| Taak | Controletoken (doet zelf geen verzoeken) |
| robots.txt-token | `Applebot-Extended` |
| Volgt robots.txt | Wordt alleen uit robots.txt gelezen |
| IP-adressen | Geen: het haalt nooit pagina's op |
| Pagina van de aanbieder gelezen op | 21 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “Web publishers can opt-out from having their content used to train generative foundation models by disallowing Applebot-Extended in the robots.txt file.”

Bron: [Apple Support: About Applebot](https://support.apple.com/en-us/119829), gelezen op 21 oktober 2026.

## Wat gebeurt er als je Applebot-Extended blokkeert

Apple benoemt de grens zelf: als je Applebot-Extended met Disallow uitsluit en content ook markeert met de meta-tag nosnippet, kunnen jouw instructies Applebot nog steeds toestaan de pagina te crawlen, en blijft de content vindbaar via Spotlight, Siri en Safari. Op dezelfde pagina staat dat uitgevers zich kunnen afmelden voor gebruik in brede wereldkennis-antwoorden met deze robots.txt-instelling.

## De robots.txt-regels

Om Applebot-Extended toe te staan:

```
User-agent: Applebot-Extended
Allow: /
```

Om Applebot-Extended te blokkeren:

```
User-agent: Applebot-Extended
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

Voor een token dat geen verzoeken stuurt, bestaat geen netwerkcontrole. Lees robots.txt, op elke host, en controleer Applebot apart. De twee tokens staan los van elkaar en één groep `User-agent: Applebot-Extended` zegt niets over Applebot.

Applebot-Extended stuurt zelf geen verzoeken en staat dus nooit in je serverlog. Het wordt alleen uit robots.txt gelezen.

## Vergelijk met Applebot

[Applebot](/nl/bots/applebot): De crawler zelf: als je die toestaat, blijf je opgenomen in de zoekresultaten van Spotlight, Siri en Safari.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). Applebot-Extended is er niet bij: kijk in je robots.txt of er een groep `Applebot-Extended` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt Applebot-Extended robots.txt?

Wordt alleen uit robots.txt gelezen. Het stuurt zelf geen verzoeken, dus er valt niets te blokkeren in de firewall: de regel in robots.txt is de hele regeling.

### Hoe weet ik dat Applebot-Extended echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Apple Support: About Applebot](https://support.apple.com/en-us/119829)
