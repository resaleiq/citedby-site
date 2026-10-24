title: GoogleOther: wat het doet en wat blokkeren verandert
h1: GoogleOther: wat het doet en wat blokkeren verandert
description: GoogleOther (Google): meerdere taken. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert, gelezen op de pagina van de aanbieder.
slug: googleother
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over GoogleOther: aanbieder Google, taak Meerdere taken, volgt robots.txt Ja, adreslijst 317 bereiken
hero_sub: GoogleOther, beheerd door Google
hero_boxes: Aanbieder|Google; Taak|Meerdere taken; Volgt robots.txt|Ja; Adreslijst|317 bereiken
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/googlebot|Googlebot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: GoogleOther is de generieke crawler van Google. Verschillende productteams van Google gebruiken hem om openbaar toegankelijke content op te halen, bijvoorbeeld bij eenmalige crawls voor intern onderzoek en ontwikkeling. Google zegt dat regels voor GoogleOther geen invloed hebben op een specifiek product. GoogleOther-Image en GoogleOther-Video staan als aparte tokens beschreven.

## Wat GoogleOther is

GoogleOther is de generieke crawler van Google, die verschillende productteams van Google gebruiken om openbaar toegankelijke content op te halen, bijvoorbeeld bij eenmalige crawls voor intern onderzoek en ontwikkeling. Google rekent hem tot zijn algemene crawlers, naast Googlebot, en beschrijft ook GoogleOther-Image en GoogleOther-Video als versies die zijn geoptimaliseerd voor afbeeldings- en video-URL's. Op de pagina van Google staat niet dat hij voor AI-training wordt gebruikt.

| Gegeven | GoogleOther |
| --- | --- |
| Aanbieder | Google |
| Taak | Generieke crawl voor verschillende productteams van Google |
| robots.txt-token | `GoogleOther` |
| Volgt robots.txt | Ja. Google zegt dat algemene crawlers bij automatisch crawlen altijd robots.txt-regels volgen. |
| IP-adressen | 317 bereiken (developers.google.com/static/crawling/ipranges/common-crawlers.json, bestand van 2026-10-23) |
| Pagina van de aanbieder gelezen op | 24 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “GoogleOther is the generic crawler that may be used by various product teams for fetching publicly accessible content from sites. For example, it may be used for one-off crawls for internal research and development.”

Bron: [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers), gelezen op 24 oktober 2026.

## Wat gebeurt er als je GoogleOther blokkeert

Google zegt dat crawlvoorkeuren voor de user agent GoogleOther geen invloed hebben op een specifiek product. Google beschrijft GoogleOther-Image en GoogleOther-Video als aparte robots.txt-tokens. Er staat dus nergens dat een regel voor GoogleOther ze dekt, en het token Googlebot is weer een ander token.

## De robots.txt-regels

Om GoogleOther toe te staan:

```
User-agent: GoogleOther
Allow: /
```

Om GoogleOther te blokkeren:

```
User-agent: GoogleOther
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GoogleOther) Chrome/W.X.Y.Z Safari/537.36
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

Het bestand developers.google.com/static/crawling/ipranges/common-crawlers.json bevatte op 24 oktober 2026 317 bereiken, bestand van 2026-10-23.

Google zegt dat de algemene crawlers meestal crawlen vanuit de bereiken in common-crawlers.json en dat de reverse DNS-naam overeenkomt met crawl-***-***-***-***.googlebot.com of geo-crawl-***-***-***-***.geo.googlebot.com.

## Vergelijk met Googlebot

[Googlebot](/nl/bots/googlebot): Googlebot crawlt voor Google Search en gerelateerde producten, terwijl GoogleOther een generieke crawler is waarvan de robots.txt-regels geen invloed hebben op een specifiek Google-product.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). GoogleOther is er niet bij: kijk in je robots.txt of er een groep `GoogleOther` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt GoogleOther robots.txt?

Ja. Google zegt dat algemene crawlers bij automatisch crawlen altijd robots.txt-regels volgen. Geef GoogleOther in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat GoogleOther echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers)
- [Google: common-crawlers.json (read 2026-10-24, creationTime 2026-10-23)](https://developers.google.com/static/crawling/ipranges/common-crawlers.json)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
