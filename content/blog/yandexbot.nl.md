title: YandexBot: wat het doet en wat blokkeren verandert
h1: YandexBot: wat het doet en wat blokkeren verandert
description: YandexBot (Yandex): zoeken. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert, gelezen op de pagina van de aanbieder.
slug: yandexbot
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over YandexBot: aanbieder Yandex, taak Zoeken, volgt robots.txt Ja, adreslijst Reverse DNS
hero_sub: YandexBot, beheerd door Yandex
hero_boxes: Aanbieder|Yandex; Taak|Zoeken; Volgt robots.txt|Ja; Adreslijst|Reverse DNS
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/googlebot|Googlebot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: YandexBot is door Yandex aangemerkt als zijn belangrijkste indexeringsrobot, een van de vele Yandex-robots met een eigen user agent. Yandex zegt dat sommige ervan pagina's downloaden voor andere doelen dan indexering en beperkende regels voor alle robots (User-agent: *) kunnen negeren. Yandex publiceert geen IP-lijst.

## Wat YandexBot is

Yandex noemt YandexBot de belangrijkste indexeringsrobot. Yandex heeft veel andere robots met eigen user agents (voor afbeeldingen, video, advertenties, mobiele pagina's, favicons en meer), die op dezelfde pagina staan. Yandex publiceert geen IP-lijst voor zijn bots.

| Gegeven | YandexBot |
| --- | --- |
| Aanbieder | Yandex |
| Taak | Zoeken (belangrijkste indexeringsrobot) |
| robots.txt-token | `Yandex` |
| Volgt robots.txt | Ja, houdt rekening met de algemene regels in robots.txt (User-agent: *) |
| IP-adressen | Controle via reverse DNS |
| Pagina van de aanbieder gelezen op | 24 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “Some robots can disguise themselves as Yandex robots by indicating the relevant User Agent. You can check the authenticity of a robot using a reverse DNS lookup.”

Bron: [Yandex Webmaster: How to check that a robot belongs to Yandex](https://yandex.com/support/webmaster/en/robot-workings/check-yandex-robots), gelezen op 24 oktober 2026.

## Wat gebeurt er als je YandexBot blokkeert

Yandex zegt dat een aantal van zijn robots pagina's downloadt voor andere doelen dan indexering en beperkende regels voor alle robots (User-agent: *) kan negeren. Om die robots te beperken heb je regels nodig die speciaal voor hen zijn geschreven, bijvoorbeeld User-agent: YandexCalendar. Yandex voegt toe dat een document waar de belangrijkste Yandex-robot niet bij kan, nooit wordt geïndexeerd of in zoekresultaten te vinden is.

## De robots.txt-regels

Om YandexBot toe te staan:

```
User-agent: Yandex
Allow: /
```

Om YandexBot te blokkeren:

```
User-agent: Yandex
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

Yandex zegt dat je een reverse DNS-lookup op het IP-adres moet doen, moet controleren of de hostnaam eindigt op yandex.ru, yandex.net of yandex.com, en dat moet bevestigen met een forward lookup. Yandex biedt ook een tool om IP-adressen te controleren.

## Vergelijk met Googlebot

[Googlebot](/nl/bots/googlebot): Beide zijn de belangrijkste crawler voor zoekindexering van hun aanbieder. Yandex noemt veel aparte robots, waarvan sommige algemene robots.txt-regels negeren, en zegt geen IP-lijst te publiceren.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). YandexBot is er niet bij: kijk in je robots.txt of er een groep `Yandex` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt YandexBot robots.txt?

Ja, houdt rekening met de algemene regels in robots.txt (User-agent: *). Geef Yandex in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat YandexBot echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Yandex Webmaster: How to check that a robot belongs to Yandex](https://yandex.com/support/webmaster/en/robot-workings/check-yandex-robots)
- [Yandex Webmaster: Using robots.txt](https://yandex.com/support/webmaster/en/controlling-robot/robots-txt)
