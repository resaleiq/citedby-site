title: DuckAssistBot: wat het doet en wat blokkeren verandert
h1: DuckAssistBot: wat het doet en wat blokkeren verandert
description: DuckAssistBot (DuckDuckGo): door de gebruiker gestart ophalen. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert.
slug: duckassistbot
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Vier feiten over DuckAssistBot: aanbieder DuckDuckGo, taak Door de gebruiker gestart ophalen, volgt robots.txt Ja, adreslijst 486 adressen
hero_sub: DuckAssistBot, beheerd door DuckDuckGo
hero_boxes: Aanbieder|DuckDuckGo; Taak|Door de gebruiker gestart ophalen; Volgt robots.txt|Ja; Adreslijst|486 adressen
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/amazonbot|Amazonbot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: DuckAssistBot crawlt pagina's in realtime voor de AI-ondersteunde antwoorden van DuckDuckGo, die hun bronnen vermelden. DuckDuckGo zegt dat de data niet wordt gebruikt om AI-modellen te trainen. Een Disallow in robots.txt werkt na 72 uur en heeft geen invloed op organische zoekrangschikking. DuckDuckGo vermeldt 486 IP-adressen.

## Wat DuckAssistBot is

DuckDuckGo heeft twee bots die mensen door elkaar halen. DuckDuckBot is de zoekcrawler en DuckAssistBot hoort bij de AI-ondersteunde antwoorden. Op de helppagina van DuckDuckGo staat dat de antwoorden duidelijk hun bronnen vermelden en dat de gecrawlde data niet wordt gebruikt om AI-modellen te trainen.

| Gegeven | DuckAssistBot |
| --- | --- |
| Aanbieder | DuckDuckGo |
| Taak | Realtime ophalen voor AI-ondersteunde antwoorden |
| robots.txt-token | `DuckAssistBot` |
| Volgt robots.txt | Ja, een wijziging werkt na 72 uur |
| IP-adressen | 486 adressen (duckduckgo.com/duckassistbot.json, bestand van 2026-09-01) |
| Pagina van de aanbieder gelezen op | 21 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “DuckAssistBot is a web crawler for DuckDuckGo Search that crawls pages in real-time for our AI-assisted answers, which prominently cite their sources. This data is not used in any way to train AI models.”

Bron: [DuckDuckGo Help Pages: About DuckAssistBot](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot), gelezen op 21 oktober 2026.

## Wat gebeurt er als je DuckAssistBot blokkeert

DuckDuckGo zegt dat een wijziging na 72 uur ingaat zodra je DuckAssistBot met Disallow uitsluit, en dat een opt-out geen invloed heeft op de organische zoekrangschikking en niet bepaalt of sites in de zoekresultaten verschijnen. De kosten van blokkeren beperken zich dus tot de ondersteunde antwoorden en hun bronvermeldingen. Problemen met opt-outs gaan naar het adres dat de pagina noemt: crawling@duckduckgo.com.

## De robots.txt-regels

Om DuckAssistBot toe te staan:

```
User-agent: DuckAssistBot
Allow: /
```

Om DuckAssistBot te blokkeren:

```
User-agent: DuckAssistBot
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
DuckAssistBot/1.2; (+http://duckduckgo.com/duckassistbot.html)
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

DuckDuckGo vermeldt de adressen in het helpartikel en als JSON op duckduckgo.com/duckassistbot.json. Het bestand bevatte op 21 oktober 2026 486 vermeldingen, met aanmaaktijd 2026-09-01. Dat is langer dan elke andere adreslijst die we voor deze set hebben geteld. Het bevat losse adressen, waar de andere CIDR-bereiken publiceren. De user agent verschijnt als `DuckAssistBot/1.2`.

## Vergelijk met Amazonbot

[Amazonbot](/nl/bots/amazonbot): Amazons familie van drie agents, waarvan er één robots.txt mogelijk negeert.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). DuckAssistBot is er niet bij: kijk in je robots.txt of er een groep `DuckAssistBot` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt DuckAssistBot robots.txt?

Ja, een wijziging werkt na 72 uur. Geef DuckAssistBot in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat DuckAssistBot echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [DuckDuckGo Help Pages: About DuckAssistBot](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot)
- [duckduckgo.com/duckassistbot.json](https://duckduckgo.com/duckassistbot.json)
