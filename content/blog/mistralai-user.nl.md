title: MistralAI-User: wat het doet en wat blokkeren verandert
h1: MistralAI-User: wat het doet en wat blokkeren verandert
description: MistralAI-User (Mistral): door de gebruiker gestart ophalen. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert.
slug: mistralai-user
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Vier feiten over MistralAI-User: aanbieder Mistral, taak Door de gebruiker gestart ophalen, volgt robots.txt Ja, adreslijst 4 bereiken
hero_sub: MistralAI-User, beheerd door Mistral
hero_boxes: Aanbieder|Mistral; Taak|Door de gebruiker gestart ophalen; Volgt robots.txt|Ja; Adreslijst|4 bereiken
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/chatgpt-user|ChatGPT-User; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: MistralAI-User is de Mistral-agent die een pagina kan bezoeken als een gebruiker Vibe een vraag stelt en in het antwoord naar de bron linkt. Mistral zegt dat hij niet wordt gebruikt om automatisch te crawlen of voor het trainen van generatieve AI. Op de pagina van Mistral staan ook MistralAI-Index en MistralAI-Training, elk met een eigen token.

## Wat MistralAI-User is

Op de crawlerpagina van Mistral staan drie agents: MistralAI-User voor gebruikersacties in Vibe, MistralAI-Index voor het indexeren van content voor het zoeken van Mistral, en MistralAI-Training, dat webcontent crawlt om datasets op te bouwen voor het trainen van generatieve AI-modellen van Mistral. Webmasters kunnen elk daarvan in robots.txt uitsluiten met Disallow.

| Gegeven | MistralAI-User |
| --- | --- |
| Aanbieder | Mistral |
| Taak | Door de gebruiker gestart ophalen |
| robots.txt-token | `MistralAI-User` |
| Volgt robots.txt | Opt-out via robots.txt |
| IP-adressen | 4 bereiken (mistral.ai/mistralai-user-ips.json, bestand van 2025-02-19) |
| Pagina van de aanbieder gelezen op | 21 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “MistralAI-User is for user actions in Vibe. When users ask Vibe a question, it may visit a web page to help answer and include a link to the source in its response.”

Bron: [Mistral Docs: Mistral crawlers](https://docs.mistral.ai/robots), gelezen op 21 oktober 2026.

## Wat gebeurt er als je MistralAI-User blokkeert

Als je MistralAI-User uitsluit, opent die agent je pagina niet meer voor de vraag van een Vibe-gebruiker. De index- en trainingsagents blijven buiten schot, want die hebben eigen tokens. Mistral zegt dat de user agent niet wordt gebruikt om het web automatisch te crawlen, ook niet om content te crawlen voor het trainen van generatieve AI, en dat content die de indexagent crawlt niet wordt gebruikt voor generatieve AI-training van welke aard dan ook.

## De robots.txt-regels

Om MistralAI-User toe te staan:

```
User-agent: MistralAI-User
Allow: /
```

Om MistralAI-User te blokkeren:

```
User-agent: MistralAI-User
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; MistralAI-User/1.0; +https://docs.mistral.ai/robots)
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

Mistral publiceert aparte adresbestanden voor de agents. mistral.ai/mistralai-user-ips.json bevatte op 21 oktober 2026 4 prefixen (aanmaaktijd 2025-02-19) en het indexbestand 2 prefixen (aanmaaktijd 2026-04-19). Twee vermeldingen voor een indexcrawler is een lijst die een firewallregel precies kan bevatten.

## Vergelijk met ChatGPT-User

[ChatGPT-User](/nl/bots/chatgpt-user): Dezelfde taak als bij OpenAI, met een andere robots.txt-belofte.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). MistralAI-User is er niet bij: kijk in je robots.txt of er een groep `MistralAI-User` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt MistralAI-User robots.txt?

Opt-out via robots.txt. Geef MistralAI-User in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat MistralAI-User echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Mistral Docs: Mistral crawlers](https://docs.mistral.ai/robots)
- [mistral.ai/mistralai-user-ips.json](https://mistral.ai/mistralai-user-ips.json)
