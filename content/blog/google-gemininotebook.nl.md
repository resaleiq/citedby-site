title: Google-GeminiNotebook: wat het doet en wat blokkeren verandert
h1: Google-GeminiNotebook: wat het doet en wat blokkeren verandert
description: Google-GeminiNotebook (Google): door de gebruiker gestart ophalen. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert.
slug: google-gemininotebook
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over Google-GeminiNotebook: aanbieder Google, taak Door de gebruiker gestart ophalen, volgt robots.txt Niet altijd, adreslijst Reverse DNS
hero_sub: Google-GeminiNotebook, beheerd door Google
hero_boxes: Aanbieder|Google; Taak|Door de gebruiker gestart ophalen; Volgt robots.txt|Niet altijd; Adreslijst|Reverse DNS
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/chatgpt-user|ChatGPT-User; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: Google-GeminiNotebook is de user agent van de Gemini Notebook-fetcher. Hij vraagt losse URL's op die gebruikers als bron aan hun projecten hebben toegevoegd. Google rekent hem tot de door de gebruiker gestarte fetchers, die robots.txt meestal negeren omdat een gebruiker het ophalen vroeg. Op de pagina van Google staat Google-NotebookLM als vroegere agent.

## Wat Google-GeminiNotebook is

Google-GeminiNotebook is de user agent van de Gemini Notebook-fetcher, die Google tot zijn door de gebruiker gestarte fetchers rekent. Hij vraagt losse URL's op die gebruikers als bron voor hun projecten hebben opgegeven. Op de pagina van Google staat Google-NotebookLM als vroegere agent, ondersteund tot augustus 2026.

| Gegeven | Google-GeminiNotebook |
| --- | --- |
| Aanbieder | Google |
| Taak | Door de gebruiker gestart ophalen |
| robots.txt-token | `Google-GeminiNotebook` |
| Volgt robots.txt | Gedeeltelijk. Google zegt dat door de gebruiker gestarte fetchers robots.txt-regels meestal negeren, omdat een gebruiker het ophalen heeft gevraagd. |
| IP-adressen | Controle via reverse DNS |
| Pagina van de aanbieder gelezen op | 24 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “The Gemini Notebook fetcher requests individual URLs that Gemini Notebook users have provided as sources for their projects.”

Bron: [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers), gelezen op 24 oktober 2026.

## Wat gebeurt er als je Google-GeminiNotebook blokkeert

Google zegt dat door de gebruiker gestarte fetchers robots.txt-regels meestal negeren, omdat een gebruiker het ophalen heeft gevraagd. De pagina van Google beschrijft geen robots.txt-token voor deze fetcher.

## De robots.txt-regels

Om Google-GeminiNotebook toe te staan:

```
User-agent: Google-GeminiNotebook
Allow: /
```

Om Google-GeminiNotebook te blokkeren:

```
User-agent: Google-GeminiNotebook
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 (compatible; Google-GeminiNotebook; +https://developers.google.com/crawling/docs/crawlers-fetchers/google-gemininotebook)
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

Google zegt dat door de gebruiker gestarte fetchers IP-bereiken publiceren in user-triggered-fetchers.json, user-triggered-fetchers-google.json en user-triggered-agents.json, en dat het reverse DNS-masker overeenkomt met ***-***-***-***.gae.googleusercontent.com of google-proxy-***-***-***-***.google.com, afhankelijk van of de fetcher van Google is of van een gebruiker.

## Vergelijk met ChatGPT-User

[ChatGPT-User](/nl/bots/chatgpt-user): Beide halen losse URL's op omdat een gebruiker een assistentproduct vroeg ze te gebruiken, en beide aanbieders zeggen dat deze verzoeken robots.txt-regels mogelijk niet volgen.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). Google-GeminiNotebook is er niet bij: kijk in je robots.txt of er een groep `Google-GeminiNotebook` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt Google-GeminiNotebook robots.txt?

Niet altijd. Gedeeltelijk. Google zegt dat door de gebruiker gestarte fetchers robots.txt-regels meestal negeren, omdat een gebruiker het ophalen heeft gevraagd. Een regel voor Google-GeminiNotebook in robots.txt houdt het dus mogelijk niet tegen. Wil je het zeker weigeren, gebruik dan een firewall- of CDN-regel die user agent en gepubliceerde adressen combineert.

### Hoe weet ik dat Google-GeminiNotebook echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
