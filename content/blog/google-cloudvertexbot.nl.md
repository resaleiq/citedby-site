title: Google-CloudVertexBot: wat het doet en wat blokkeren verandert
h1: Google-CloudVertexBot: wat het doet en wat blokkeren verandert
description: Google-CloudVertexBot (Google): meerdere taken. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert.
slug: google-cloudvertexbot
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over Google-CloudVertexBot: aanbieder Google, taak Meerdere taken, volgt robots.txt Ja, adreslijst 317 bereiken
hero_sub: Google-CloudVertexBot, beheerd door Google
hero_boxes: Aanbieder|Google; Taak|Meerdere taken; Volgt robots.txt|Ja; Adreslijst|317 bereiken
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/googlebot|Googlebot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: Google-CloudVertexBot is een Google-crawler die crawls uitvoert die site-eigenaren aanvragen om Vertex AI Agents te bouwen. Google rekent hem tot zijn algemene crawlers, die bij automatisch crawlen altijd robots.txt volgen. Google zegt dat regels voor deze crawler geen effect hebben op Google Search of andere Google-producten.

## Wat Google-CloudVertexBot is

Google-CloudVertexBot is een Google-crawler die tot de algemene crawlers van Google hoort. Google zegt dat hij crawls uitvoert die site-eigenaren aanvragen om Vertex AI Agents te bouwen. Google toont hem als een deelstring van de user agent, niet als volledige user-agent-string.

| Gegeven | Google-CloudVertexBot |
| --- | --- |
| Aanbieder | Google |
| Taak | Crawl aangevraagd door site-eigenaren voor Vertex AI Agents |
| robots.txt-token | `Google-CloudVertexBot` |
| Volgt robots.txt | Ja. Google zegt dat algemene crawlers bij automatisch crawlen altijd robots.txt-regels volgen. |
| IP-adressen | 317 bereiken (developers.google.com/static/crawling/ipranges/common-crawlers.json, bestand van 2026-10-23) |
| Pagina van de aanbieder gelezen op | 24 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “Crawling preferences addressed to the Google-CloudVertexBot user agent affect crawls requested by the site owners' for building Vertex AI Agents”

Bron: [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers), gelezen op 24 oktober 2026.

## Wat gebeurt er als je Google-CloudVertexBot blokkeert

Google zegt dat voorkeuren voor de user agent Google-CloudVertexBot gelden voor crawls die site-eigenaren aanvragen om Vertex AI Agents te bouwen. Volgens Google heeft dit geen effect op Google Search of andere producten.

## De robots.txt-regels

Om Google-CloudVertexBot toe te staan:

```
User-agent: Google-CloudVertexBot
Allow: /
```

Om Google-CloudVertexBot te blokkeren:

```
User-agent: Google-CloudVertexBot
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
Google-CloudVertexBot
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

Het bestand developers.google.com/static/crawling/ipranges/common-crawlers.json bevatte op 24 oktober 2026 317 bereiken, bestand van 2026-10-23.

Google zegt dat de algemene crawlers meestal crawlen vanuit de bereiken in common-crawlers.json en dat de reverse DNS-naam overeenkomt met crawl-***-***-***-***.googlebot.com of geo-crawl-***-***-***-***.geo.googlebot.com.

## Vergelijk met Googlebot

[Googlebot](/nl/bots/googlebot): Googlebot crawlt voor Google Search, terwijl Google-CloudVertexBot alleen crawlt als een site-eigenaar een crawl heeft aangevraagd om Vertex AI Agents te bouwen.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). Google-CloudVertexBot is er niet bij: kijk in je robots.txt of er een groep `Google-CloudVertexBot` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt Google-CloudVertexBot robots.txt?

Ja. Google zegt dat algemene crawlers bij automatisch crawlen altijd robots.txt-regels volgen. Geef Google-CloudVertexBot in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat Google-CloudVertexBot echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers)
- [Google: common-crawlers.json (read 2026-10-24, creationTime 2026-10-23)](https://developers.google.com/static/crawling/ipranges/common-crawlers.json)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
