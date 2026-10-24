title: Claude-SearchBot: wat het doet en wat blokkeren verandert
h1: Claude-SearchBot: wat het doet en wat blokkeren verandert
description: Claude-SearchBot (Anthropic): zoeken. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert, gelezen op de pagina van de aanbieder.
slug: claude-searchbot
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Vier feiten over Claude-SearchBot: aanbieder Anthropic, taak Zoeken, volgt robots.txt Ja, adreslijst Lijst, niet om te blokkeren
hero_sub: Claude-SearchBot, beheerd door Anthropic
hero_boxes: Aanbieder|Anthropic; Taak|Zoeken; Volgt robots.txt|Ja; Adreslijst|Lijst, niet om te blokkeren
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/claudebot|ClaudeBot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: Claude-SearchBot is de Anthropic-robot die het web doorzoekt om de kwaliteit van zoekresultaten te verbeteren. Anthropic zegt dat uitschakelen voorkomt dat je content wordt geïndexeerd voor zoekoptimalisatie. Dat kan je zichtbaarheid en de nauwkeurigheid in zoekresultaten van gebruikers verminderen. Het robots.txt-token is Claude-SearchBot.

## Wat Claude-SearchBot is

Claude-SearchBot is de indexerende kant van de zoekfunctie van Anthropic. Anthropic beschrijft hem als een robot die online content analyseert om de relevantie en nauwkeurigheid van zoekantwoorden te verbeteren. [ClaudeBot](/nl/bots/claudebot) verzamelt voor training en [Claude-User](/nl/bots/claude-user) beantwoordt een live vraag.

| Gegeven | Claude-SearchBot |
| --- | --- |
| Aanbieder | Anthropic |
| Taak | Zoeken |
| robots.txt-token | `Claude-SearchBot` |
| Volgt robots.txt | Ja, Anthropic zegt dat zijn robots robots.txt respecteren |
| IP-adressen | De aanbieder verwijst naar een lijst maar raadt blokkeren op IP af |
| Pagina van de aanbieder gelezen op | 21 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “Claude-SearchBot navigates the web to improve search result quality for users. It analyzes online content specifically to enhance the relevance and accuracy of search responses. Disabling Claude-SearchBot on your site prevents our system from indexing your content for search optimization, which may reduce your site's visibility and accuracy in user search results.”

Bron: [Anthropic Help Center: Does Anthropic crawl data from the web, and how can site owners block the crawler? (7 April 2026)](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler), gelezen op 21 oktober 2026.

## Wat gebeurt er als je Claude-SearchBot blokkeert

Anthropic noemt twee gevolgen van uitschakelen: je content wordt niet geïndexeerd voor zoekoptimalisatie, en de zichtbaarheid en nauwkeurigheid van je site in zoekresultaten van gebruikers kunnen dalen.

## De robots.txt-regels

Om Claude-SearchBot toe te staan:

```
User-agent: Claude-SearchBot
Allow: /
```

Om Claude-SearchBot te blokkeren:

```
User-agent: Claude-SearchBot
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De pagina van de aanbieder toont geen volledige user-agent-string voor Claude-SearchBot.

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

Het helpartikel is gedateerd 7 april 2026. Er staat geen user-agent-string in, dus een logregel die Claude-SearchBot noemt, is een bewering die je niet alleen met het artikel kunt bevestigen. Anthropic zegt dat verkeer vanaf een adres op de gelinkte lijst van Anthropic is. Het vraagt site-eigenaren die denken dat een robot zich misdraagt om te mailen vanaf een e-mailadres op het betreffende domein.

## Vergelijk met ClaudeBot

[ClaudeBot](/nl/bots/claudebot): Als je ClaudeBot blokkeert, sluit je je alleen uit van training. Je verdwijnt niet uit de zoekindex van Claude.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). Claude-SearchBot is er niet bij: kijk in je robots.txt of er een groep `Claude-SearchBot` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt Claude-SearchBot robots.txt?

Ja, Anthropic zegt dat zijn robots robots.txt respecteren. Geef Claude-SearchBot in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat Claude-SearchBot echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Anthropic Help Center: Does Anthropic crawl data from the web, and how can site owners block the crawler? (7 April 2026)](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)
