title: Google-Agent: wat het doet en wat blokkeren verandert
h1: Google-Agent: wat het doet en wat blokkeren verandert
description: Google-Agent (Google): door de gebruiker gestart ophalen. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert.
slug: google-agent
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over Google-Agent: aanbieder Google, taak Door de gebruiker gestart ophalen, volgt robots.txt Niet altijd, adreslijst 20 bereiken
hero_sub: Google-Agent, beheerd door Google
hero_boxes: Aanbieder|Google; Taak|Door de gebruiker gestart ophalen; Volgt robots.txt|Niet altijd; Adreslijst|20 bereiken
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/chatgpt-user|ChatGPT-User; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: Google-Agent is een door de gebruiker gestarte fetcher. Google zegt dat agents die op de infrastructuur van Google draaien hem gebruiken om het web te doorzoeken en namens een gebruiker te handelen. Volgens Google negeren zulke fetchers robots.txt meestal, omdat een gebruiker het ophalen vroeg. Google publiceert zijn IP-bereiken in user-triggered-agents.json.

## Wat Google-Agent is

Google-Agent is een door de gebruiker gestarte fetcher. Volgens Google gebruiken agents die op de infrastructuur van Google draaien hem om het web te doorzoeken en acties uit te voeren op verzoek van een gebruiker. Google geeft aparte user-agent-strings voor mobiel en desktop. Google zegt ook dat het experimenteert met het Web Bot Auth-protocol met de identiteit https://agent.bot.goog.

| Gegeven | Google-Agent |
| --- | --- |
| Aanbieder | Google |
| Taak | Door de gebruiker gestart ophalen (agents die namens een gebruiker handelen) |
| robots.txt-token | `Google-Agent` |
| Volgt robots.txt | Gedeeltelijk. Google zegt dat door de gebruiker gestarte fetchers robots.txt-regels meestal negeren, omdat een gebruiker het ophalen heeft gevraagd. |
| IP-adressen | 20 bereiken (developers.google.com/static/crawling/ipranges/user-triggered-agents.json, bestand van 2026-10-23) |
| Pagina van de aanbieder gelezen op | 24 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “Google-Agent is used by agents hosted on Google infrastructure to navigate the web and perform actions upon user request.”

Bron: [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers), gelezen op 24 oktober 2026.

## Wat gebeurt er als je Google-Agent blokkeert

Google zegt dat door de gebruiker gestarte fetchers robots.txt-regels meestal negeren, omdat een gebruiker het ophalen heeft gevraagd. De pagina van Google beschrijft geen robots.txt-token voor Google-Agent.

## De robots.txt-regels

Om Google-Agent toe te staan:

```
User-agent: Google-Agent
Allow: /
```

Om Google-Agent te blokkeren:

```
User-agent: Google-Agent
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko; compatible; Google-Agent; +https://developers.google.com/crawling/docs/crawlers-fetchers/google-agent) Chrome/W.X.Y.Z Safari/537.36
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

Het bestand developers.google.com/static/crawling/ipranges/user-triggered-agents.json bevatte op 24 oktober 2026 20 bereiken, bestand van 2026-10-23.

Google zegt dat Google-Agent IP-bereiken uit user-triggered-agents.json gebruikt en dat het reverse DNS-masker van door de gebruiker gestarte fetchers overeenkomt met ***-***-***-***.gae.googleusercontent.com of google-proxy-***-***-***-***.google.com, afhankelijk van of de fetcher van Google is of van een gebruiker.

## Vergelijk met ChatGPT-User

[ChatGPT-User](/nl/bots/chatgpt-user): Beide handelen op verzoek van een gebruiker in plaats van zelf te crawlen. Google-Agent wordt omschreven als een fetcher die het web doorzoekt en acties voor de gebruiker uitvoert.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). Google-Agent is er niet bij: kijk in je robots.txt of er een groep `Google-Agent` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt Google-Agent robots.txt?

Niet altijd. Gedeeltelijk. Google zegt dat door de gebruiker gestarte fetchers robots.txt-regels meestal negeren, omdat een gebruiker het ophalen heeft gevraagd. Een regel voor Google-Agent in robots.txt houdt het dus mogelijk niet tegen. Wil je het zeker weigeren, gebruik dan een firewall- of CDN-regel die user agent en gepubliceerde adressen combineert.

### Hoe weet ik dat Google-Agent echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers)
- [Google: user-triggered-agents.json (read 2026-10-24, creationTime 2026-10-23)](https://developers.google.com/static/crawling/ipranges/user-triggered-agents.json)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
