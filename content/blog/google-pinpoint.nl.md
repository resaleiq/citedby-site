title: Google-Pinpoint: wat het doet en wat blokkeren verandert
h1: Google-Pinpoint: wat het doet en wat blokkeren verandert
description: Google-Pinpoint (Google): door de gebruiker gestart ophalen. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert.
slug: google-pinpoint
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over Google-Pinpoint: aanbieder Google, taak Door de gebruiker gestart ophalen, volgt robots.txt Niet altijd, adreslijst Reverse DNS
hero_sub: Google-Pinpoint, beheerd door Google
hero_boxes: Aanbieder|Google; Taak|Door de gebruiker gestart ophalen; Volgt robots.txt|Niet altijd; Adreslijst|Reverse DNS
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/google-gemininotebook|Google-GeminiNotebook; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: Google-Pinpoint is een door de gebruiker gestarte fetcher die Google vermeldt. Hij vraagt losse URL's op die Pinpoint-gebruikers hebben opgegeven als bron voor hun persoonlijke documentverzamelingen. Google zegt dat zulke fetchers robots.txt-regels meestal negeren omdat een gebruiker het ophalen vroeg, en beschrijft er geen robots.txt-token voor.

## Wat Google-Pinpoint is

Google-Pinpoint is een door de gebruiker gestarte fetcher die Google vermeldt. Hij vraagt losse URL's op die Pinpoint-gebruikers hebben opgegeven als bron voor hun persoonlijke documentverzamelingen. Google vermeldt hem met de user agent Google-Pinpoint.

| Gegeven | Google-Pinpoint |
| --- | --- |
| Aanbieder | Google |
| Taak | Door de gebruiker gestart ophalen |
| robots.txt-token | `Google-Pinpoint` |
| Volgt robots.txt | Gedeeltelijk. Google zegt dat door de gebruiker gestarte fetchers robots.txt-regels meestal negeren, omdat een gebruiker het ophalen heeft gevraagd. |
| IP-adressen | Controle via reverse DNS |
| Pagina van de aanbieder gelezen op | 24 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “The Google-Pinpoint fetcher requests individual URLs that Pinpoint users specified as sources for their personal collections of documents.”

Bron: [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers), gelezen op 24 oktober 2026.

## Wat gebeurt er als je Google-Pinpoint blokkeert

Google zegt dat door de gebruiker gestarte fetchers robots.txt-regels meestal negeren, omdat een gebruiker het ophalen heeft gevraagd. De pagina van Google beschrijft geen robots.txt-token voor Google-Pinpoint.

## De robots.txt-regels

Om Google-Pinpoint toe te staan:

```
User-agent: Google-Pinpoint
Allow: /
```

Om Google-Pinpoint te blokkeren:

```
User-agent: Google-Pinpoint
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
Google-Pinpoint
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

Google zegt dat door de gebruiker gestarte fetchers IP-bereiken publiceren in user-triggered-fetchers.json, user-triggered-fetchers-google.json en user-triggered-agents.json, en dat het reverse DNS-masker overeenkomt met ***-***-***-***.gae.googleusercontent.com of google-proxy-***-***-***-***.google.com, afhankelijk van of de fetcher van Google is of van een gebruiker.

## Vergelijk met Google-GeminiNotebook

[Google-GeminiNotebook](/nl/bots/google-gemininotebook): Beide halen URL's op die gebruikers als bron hebben opgegeven in een Google-product, en beide vallen onder de regels van Google voor door de gebruiker gestarte fetchers.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). Google-Pinpoint is er niet bij: kijk in je robots.txt of er een groep `Google-Pinpoint` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt Google-Pinpoint robots.txt?

Niet altijd. Gedeeltelijk. Google zegt dat door de gebruiker gestarte fetchers robots.txt-regels meestal negeren, omdat een gebruiker het ophalen heeft gevraagd. Een regel voor Google-Pinpoint in robots.txt houdt het dus mogelijk niet tegen. Wil je het zeker weigeren, gebruik dan een firewall- of CDN-regel die user agent en gepubliceerde adressen combineert.

### Hoe weet ik dat Google-Pinpoint echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
