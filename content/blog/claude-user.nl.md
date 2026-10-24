title: Claude-User: wat het doet en wat blokkeren verandert
h1: Claude-User: wat het doet en wat blokkeren verandert
description: Claude-User (Anthropic): door de gebruiker gestart ophalen. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert.
slug: claude-user
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Vier feiten over Claude-User: aanbieder Anthropic, taak Door de gebruiker gestart ophalen, volgt robots.txt Ja, adreslijst Lijst, niet om te blokkeren
hero_sub: Claude-User, beheerd door Anthropic
hero_boxes: Aanbieder|Anthropic; Taak|Door de gebruiker gestart ophalen; Volgt robots.txt|Ja; Adreslijst|Lijst, niet om te blokkeren
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/claude-searchbot|Claude-SearchBot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: Claude-User is de agent die Claude kan gebruiken om een website te openen als iemand een vraag stelt. Anthropic zegt dat uitschakelen voorkomt dat je content wordt opgehaald als antwoord op een vraag van een gebruiker. Dat kan je zichtbaarheid voor door gebruikers gestuurd zoeken op het web verminderen. Hij staat los van ClaudeBot en Claude-SearchBot.

## Wat Claude-User is

Van de drie robots van Anthropic is Claude-User degene die aan de vraag van een persoon gekoppeld is. Hij verzamelt geen trainingsdata (dat doet [ClaudeBot](/nl/bots/claudebot)) en bouwt de zoekindex niet op (dat doet [Claude-SearchBot](/nl/bots/claude-searchbot)).

| Gegeven | Claude-User |
| --- | --- |
| Aanbieder | Anthropic |
| Taak | Door de gebruiker gestart ophalen |
| robots.txt-token | `Claude-User` |
| Volgt robots.txt | Ja, Anthropic zegt dat zijn robots robots.txt respecteren |
| IP-adressen | De aanbieder verwijst naar een lijst maar raadt blokkeren op IP af |
| Pagina van de aanbieder gelezen op | 21 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “Claude-User supports Claude AI users. When individuals ask questions to Claude, it may access websites using a Claude-User agent. Claude-User allows site owners to control which sites can be accessed through these user-initiated requests. Disabling Claude-User on your site prevents our system from retrieving your content in response to a user query, which may reduce your site's visibility for user-directed web search.”

Bron: [Anthropic Help Center: Does Anthropic crawl data from the web, and how can site owners block the crawler? (7 April 2026)](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler), gelezen op 21 oktober 2026.

## Wat gebeurt er als je Claude-User blokkeert

Hier is Anthropic het directst over de kosten: uitschakelen van Claude-User voorkomt ophalen „als antwoord op een vraag van een gebruiker“ en „kan de zichtbaarheid van je site voor door gebruikers gestuurd zoeken op het web verminderen“. Een shop die hem blokkeert, kan nog steeds uit andere bronnen bij het model bekend zijn, maar Claude kan de pagina niet openen als erom gevraagd wordt.

## De robots.txt-regels

Om Claude-User toe te staan:

```
User-agent: Claude-User
Allow: /
```

Om Claude-User te blokkeren:

```
User-agent: Claude-User
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De pagina van de aanbieder toont geen volledige user-agent-string voor Claude-User.

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

Het helpartikel van Anthropic noemt geen user-agent-string voor de drie robots en zegt dat de bron-IP-adressen op een gelinkte lijst staan. Anthropic zegt ook dat het blokkeren van die adressen kan voorkomen dat zijn robots robots.txt lezen. Het artikel adviseert daarom de toegang te regelen in robots.txt en niet op IP-niveau.

## Vergelijk met Claude-SearchBot

[Claude-SearchBot](/nl/bots/claude-searchbot): Robot voor zoekkwaliteit. Blokkeren raakt de indexering voor zoeken, niet de live vraag van een gebruiker.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). Claude-User is er niet bij: kijk in je robots.txt of er een groep `Claude-User` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt Claude-User robots.txt?

Ja, Anthropic zegt dat zijn robots robots.txt respecteren. Geef Claude-User in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat Claude-User echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Anthropic Help Center: Does Anthropic crawl data from the web, and how can site owners block the crawler? (7 April 2026)](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)
