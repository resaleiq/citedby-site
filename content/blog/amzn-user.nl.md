title: Amzn-User: wat het doet en wat blokkeren verandert
h1: Amzn-User: wat het doet en wat blokkeren verandert
description: Amzn-User (Amazon): door de gebruiker gestart ophalen. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert.
slug: amzn-user
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over Amzn-User: aanbieder Amazon, taak Door de gebruiker gestart ophalen, volgt robots.txt Niet altijd, adreslijst Lijst op zijn pagina
hero_sub: Amzn-User, beheerd door Amazon
hero_boxes: Aanbieder|Amazon; Taak|Door de gebruiker gestart ophalen; Volgt robots.txt|Niet altijd; Adreslijst|Lijst op zijn pagina
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/amzn-searchbot|Amzn-SearchBot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: Amzn-User is de Amazon-user agent die live pagina's ophaalt als een klant Alexa iets vraagt waarvoor actuele informatie nodig is. Amazon zegt dat hij niet crawlt voor het trainen van generatieve AI en mogelijk niet alle robots.txt-regels volgt, omdat de actie door de gebruiker wordt gestart. Amazonbot en Amzn-SearchBot hebben aparte instellingen.

## Wat Amzn-User is

Amzn-User is een Amazon-user agent die acties van gebruikers ondersteunt, zoals het beantwoorden van Alexa-vragen die actuele informatie nodig hebben. Amazon zegt dat Amzn-User live informatie van het web kan ophalen als een klant een vraag stelt, om namens de gebruiker nauwkeurige antwoorden te geven. Amazon zegt dat hij content niet crawlt voor het trainen van generatieve AI-modellen.

| Gegeven | Amzn-User |
| --- | --- |
| Aanbieder | Amazon |
| Taak | Door de gebruiker gestart ophalen |
| robots.txt-token | `Amzn-User` |
| Volgt robots.txt | Gedeeltelijk, volgt mogelijk niet alle robots.txt-regels omdat acties door de gebruiker kunnen worden gestart |
| IP-adressen | Lijst op de pagina van de aanbieder (developer.amazon.com/amazonbot/live-ip-addresses) |
| Pagina van de aanbieder gelezen op | 24 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “Because actions taken by Amzn-User can be initiated by a user, it may not follow all robots.txt directives.”

Bron: [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot), gelezen op 24 oktober 2026.

## Wat gebeurt er als je Amzn-User blokkeert

Amazon zegt dat Amzn-User mogelijk niet alle robots.txt-regels volgt, omdat zijn acties door een gebruiker kunnen worden gestart. Amazon zegt ook dat de instelling van elke user agent (Amazonbot, Amzn-SearchBot, Amzn-User) los staat van de andere en dat het ongeveer 24 uur kan duren voordat wijzigingen doorwerken.

## De robots.txt-regels

Om Amzn-User toe te staan:

```
User-agent: Amzn-User
Allow: /
```

Om Amzn-User te blokkeren:

```
User-agent: Amzn-User
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Amzn-User/0.1) Chrome/W.X.Y.Z Safari/537.36
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

Amazon publiceert de IP-adressen van Amzn-User op een webpagina die de lijst als JSON toont, en verwijst ernaar vanaf de documentatiepagina van Amazonbot.

## Vergelijk met Amzn-SearchBot

[Amzn-SearchBot](/nl/bots/amzn-searchbot): Amzn-SearchBot is een geautomatiseerde crawler voor zoekervaringen van Amazon die volgens Amazon robots.txt respecteert. Amzn-User haalt live informatie op als een klant erom vraagt en volgt mogelijk niet alle regels.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). Amzn-User is er niet bij: kijk in je robots.txt of er een groep `Amzn-User` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt Amzn-User robots.txt?

Niet altijd: volgt mogelijk niet alle robots.txt-regels omdat acties door de gebruiker kunnen worden gestart. Een regel voor Amzn-User in robots.txt houdt het dus mogelijk niet tegen. Wil je het zeker weigeren, gebruik dan een firewall- of CDN-regel die user agent en gepubliceerde adressen combineert.

### Hoe weet ik dat Amzn-User echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot)
- [Amazon: Amzn-User IP addresses (read 2026-10-24)](https://developer.amazon.com/amazonbot/live-ip-addresses/)
