title: Bingbot: wat het doet en wat blokkeren verandert
h1: Bingbot: wat het doet en wat blokkeren verandert
description: Bingbot (Microsoft): zoeken. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert, gelezen op de pagina van de aanbieder.
slug: bingbot
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Vier feiten over Bingbot: aanbieder Microsoft, taak Zoeken, volgt robots.txt Ja, adreslijst Controletool
hero_sub: Bingbot, beheerd door Microsoft
hero_boxes: Aanbieder|Microsoft; Taak|Zoeken; Volgt robots.txt|Ja; Adreslijst|Controletool
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/googlebot|Googlebot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: Bingbot is de standaardcrawler van Microsoft en doet het meeste crawlwerk voor Bing. Op de helppagina van Bing staan vijf crawlers: Bingbot, AdIdxBot, BingPreview, MicrosoftPreview en BingVideoPreview. Je stuurt ze aan via robots.txt. De crawlsnelheid stel je in met de tool Crawl control in Bing Webmaster Tools, niet in robots.txt.

## Wat Bingbot is

De pagina van Bing heet „Overview of Bing crawlers (user agents)“ en zegt dat Bing nu deze belangrijkste crawlers gebruikt: Bingbot (de standaardcrawler), AdIdxBot (gebruikt door Bing Ads, die advertenties crawlt en de bijbehorende websites volgt voor kwaliteitscontrole), BingPreview (paginasnapshots voor Bing), MicrosoftPreview (snapshots voor Microsoft-producten) en BingVideoPreview (videovoorbeelden, alleen in Bing). Bingbot, AdIdxBot, BingPreview en BingVideoPreview hebben desktop- en mobiele varianten. De pagina noemt geen aparte AI-crawler. Hetzelfde helpgedeelte bevat „How To Permanently Remove a URL or Page from Bing or Copilot“. Lees die pagina als je een pagina wilt laten verwijderen in plaats van de toegang te regelen.

| Gegeven | Bingbot |
| --- | --- |
| Aanbieder | Microsoft |
| Taak | Zoekcrawler |
| robots.txt-token | `bingbot` |
| Volgt robots.txt | Ja |
| IP-adressen | Controletool |
| Pagina van de aanbieder gelezen op | 21 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “Bingbot is our standard crawler and handles most of our crawling needs each day.”

Bron: [Microsoft Bing Webmaster help: Which Crawlers Does Bing Use?](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0), gelezen op 21 oktober 2026.

## Wat gebeurt er als je Bingbot blokkeert

De pagina van Bing zegt niet wat blokkeren kost. Dit is onze lezing, niet die van Bing. Bingbot is de crawler die Bing voedt. Sluit je hem in robots.txt uit met Disallow, dan stopt Bing met het crawlen van die pagina's en verliest alles wat op de index van Bing leunt ze ook. Bing geeft je twee instellingen: robots.txt vertelt zijn crawlers hoe ze met je site omgaan, en Bing Webmaster Tools heeft een tool Crawl control waarmee je de crawlsnelheid per uur instelt.

## De robots.txt-regels

Om Bingbot toe te staan:

```
User-agent: bingbot
Allow: /
```

Om Bingbot te blokkeren:

```
User-agent: bingbot
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm) Chrome/W.X.Y.Z Safari/537.36
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

Bing zegt dat user-agent-strings gemakkelijk te vervalsen zijn, dus niet elk verzoek met zo'n string komt van een echte Bing-crawler. Gebruik de tool Verify Bingbot om het adres te controleren, of een van de andere verificatiemethoden die Bing beschrijft. In de user-agent-string staat W.X.Y.Z voor de Microsoft Edge-versie waarmee Bing rendert en die Bing naar eigen zeggen regelmatig bijwerkt. Op die pagina hebben we geen IP-lijst gelezen, dus we noemen geen aantal.

## Vergelijk met Googlebot

[Googlebot](/nl/bots/googlebot): De andere belangrijke zoekcrawler: een ander token en een andere verificatie.

## Je eigen site

De gratis check in het kader hierboven test Bingbot met een echt verzoek en leest daarvoor robots.txt. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt Bingbot robots.txt?

Ja. Geef bingbot in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat Bingbot echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Microsoft Bing Webmaster help: Which Crawlers Does Bing Use?](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0)
