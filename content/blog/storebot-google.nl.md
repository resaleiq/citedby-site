title: Storebot-Google: wat het doet en wat blokkeren verandert
h1: Storebot-Google: wat het doet en wat blokkeren verandert
description: Storebot-Google (Google): zoeken. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert, gelezen op de pagina van de aanbieder.
slug: storebot-google
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over Storebot-Google: aanbieder Google, taak Zoeken, volgt robots.txt Ja, adreslijst 317 bereiken
hero_sub: Storebot-Google, beheerd door Google
hero_boxes: Aanbieder|Google; Taak|Zoeken; Volgt robots.txt|Ja; Adreslijst|317 bereiken
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/googlebot|Googlebot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: Storebot-Google is de crawler die Google tussen zijn algemene crawlers beschrijft als Google StoreBot. Google zegt dat een Disallow voor zijn token alle onderdelen van Google Shopping raakt, zoals het tabblad Shopping in Google Search en Google Shopping. Googlebot is een apart token met eigen getroffen producten.

## Wat Storebot-Google is

Storebot-Google is de Google-crawler die tussen de algemene crawlers wordt beschreven als Google StoreBot. Google zegt dat regels voor deze crawler alle onderdelen van Google Shopping raken. Google geeft aparte user-agent-strings voor desktop en mobiel.

| Gegeven | Storebot-Google |
| --- | --- |
| Aanbieder | Google |
| Taak | Zoeken (onderdelen van Google Shopping) |
| robots.txt-token | `Storebot-Google` |
| Volgt robots.txt | Ja. Google zegt dat algemene crawlers bij automatisch crawlen altijd robots.txt-regels volgen. |
| IP-adressen | 317 bereiken (developers.google.com/static/crawling/ipranges/common-crawlers.json, bestand van 2026-10-23) |
| Pagina van de aanbieder gelezen op | 24 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “Crawling preferences addressed to the Storebot-Google user agent affect all surfaces of Google Shopping”

Bron: [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers), gelezen op 24 oktober 2026.

## Wat gebeurt er als je Storebot-Google blokkeert

Google zegt dat een Disallow voor het token Storebot-Google alle onderdelen van Google Shopping raakt, zoals het tabblad Shopping in Google Search en Google Shopping. Op de pagina staat Googlebot als apart token met eigen getroffen producten.

## De robots.txt-regels

Om Storebot-Google toe te staan:

```
User-agent: Storebot-Google
Allow: /
```

Om Storebot-Google te blokkeren:

```
User-agent: Storebot-Google
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
Mozilla/5.0 (X11; Linux x86_64; Storebot-Google/1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z Safari/537.36
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

Het bestand developers.google.com/static/crawling/ipranges/common-crawlers.json bevatte op 24 oktober 2026 317 bereiken, bestand van 2026-10-23.

Google zegt dat de algemene crawlers meestal crawlen vanuit de bereiken in common-crawlers.json en dat de reverse DNS-naam overeenkomt met crawl-***-***-***-***.googlebot.com of geo-crawl-***-***-***-***.geo.googlebot.com.

## Vergelijk met Googlebot

[Googlebot](/nl/bots/googlebot): De regels voor Googlebot raken Google Search en gerelateerde producten, terwijl de regels voor Storebot-Google onderdelen van Google Shopping raken.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). Storebot-Google is er niet bij: kijk in je robots.txt of er een groep `Storebot-Google` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt Storebot-Google robots.txt?

Ja. Google zegt dat algemene crawlers bij automatisch crawlen altijd robots.txt-regels volgen. Geef Storebot-Google in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat Storebot-Google echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers)
- [Google: common-crawlers.json (read 2026-10-24, creationTime 2026-10-23)](https://developers.google.com/static/crawling/ipranges/common-crawlers.json)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
