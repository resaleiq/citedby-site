title: Meta-WebIndexer: wat het doet en wat blokkeren verandert
h1: Meta-WebIndexer: wat het doet en wat blokkeren verandert
description: Meta-WebIndexer (Meta): zoeken. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert, gelezen op de pagina van de aanbieder.
slug: meta-webindexer
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over Meta-WebIndexer: aanbieder Meta, taak Zoeken, volgt robots.txt Ja, adreslijst Geen
hero_sub: Meta-WebIndexer, beheerd door Meta
hero_boxes: Aanbieder|Meta; Taak|Zoeken; Volgt robots.txt|Ja; Adreslijst|Geen
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/meta-externalagent|Meta-ExternalAgent; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: Meta-WebIndexer is een Meta-crawler die het web doorzoekt om de kwaliteit van de zoekresultaten van Meta AI te verbeteren. Meta zegt dat het toestaan ervan in robots.txt Meta helpt je content te citeren en ernaar te linken in de antwoorden van Meta AI. Je blokkeert een crawler met een disallow voor die crawler. Een wijziging kan tot 24 uur duren.

## Wat Meta-WebIndexer is

Meta-WebIndexer is een Meta-crawler die het web doorzoekt om de kwaliteit van de zoekresultaten van Meta AI voor gebruikers te verbeteren. Meta zegt dat het toestaan ervan in robots.txt Meta helpt je content te citeren en ernaar te linken in de antwoorden van Meta AI. Meta beschrijft hem op één pagina samen met Meta-ExternalAgent, Meta-ExternalFetcher, Meta-ExternalAds en FacebookExternalHit.

| Gegeven | Meta-WebIndexer |
| --- | --- |
| Aanbieder | Meta |
| Taak | Zoeken |
| robots.txt-token | `Meta-WebIndexer` |
| Volgt robots.txt | Ja, wijzigingen kunnen tot 24 uur duren |
| IP-adressen | Niet gepubliceerd |
| Pagina van de aanbieder gelezen op | 24 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “The Meta-WebIndexer crawler navigates the web to improve Meta AI search result quality for users. In doing so, Meta analyzes online content to enhance the relevance and accuracy of Meta AI.”

Bron: [Meta: Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers), gelezen op 24 oktober 2026.

## Wat gebeurt er als je Meta-WebIndexer blokkeert

Meta zegt dat je zijn crawlers kunt blokkeren door een disallow voor de betreffende crawler aan robots.txt toe te voegen, en dat wijzigingen in robots.txt tot 24 uur kunnen duren. Meta zegt dat het toestaan van Meta-WebIndexer Meta helpt je content te citeren en ernaar te linken in de antwoorden van Meta AI. De pagina van Meta zegt niet of een disallow voor Meta-WebIndexer invloed heeft op zijn andere crawlers.

## De robots.txt-regels

Om Meta-WebIndexer toe te staan:

```
User-agent: Meta-WebIndexer
Allow: /
```

Om Meta-WebIndexer te blokkeren:

```
User-agent: Meta-WebIndexer
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
meta-webindexer/1.1
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

De crawlerpagina van Meta noemt voor deze crawler geen IP-adressen of verificatiemethode. De crawler wordt herkend aan zijn user-agent-string.

## Vergelijk met Meta-ExternalAgent

[Meta-ExternalAgent](/nl/bots/meta-externalagent): Meta-WebIndexer is voor zoekresultaten en bronvermeldingen van Meta AI, terwijl Meta Meta-ExternalAgent omschrijft als crawlen voor toepassingen zoals het trainen van AI-foundation-modellen of het rechtstreeks indexeren van content.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). Meta-WebIndexer is er niet bij: kijk in je robots.txt of er een groep `Meta-WebIndexer` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt Meta-WebIndexer robots.txt?

Ja, wijzigingen kunnen tot 24 uur duren. Geef Meta-WebIndexer in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat Meta-WebIndexer echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Meta: Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers)
