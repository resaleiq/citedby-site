title: Cloudflare: AI-botbeleid voor Search, Agent en Training
slug: cloudflare
description: Cloudflare deelt AI-bots in als Search, Agent en Training, met Block, Block on pages with ads en Allow. Nieuwe standaardinstellingen vanaf 15 sept. 2026.
section: platforms
locale: nl
cluster: AI-crawlers per platform
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Vier feiten over Cloudflare: Waar Security Settings, Gedragstypen Search, Agent, Training, Keuzes 3 per gedragstype, Pagina bijgewerkt 1 juli 2026
hero_sub: Instellingen voor AI-crawlers op Cloudflare
hero_boxes: Waar|Security Settings; Gedragstypen|Search, Agent, Training; Keuzes|3 per gedragstype; Pagina bijgewerkt|1 juli 2026
widget: on
related: /nl/platforms|Alle platforms vergeleken; /nl/platforms/shopify|Shopify; /nl/bots|AI-crawlers vergeleken; /nl/guides/cms|Checklist AI-zichtbaarheid voor Shopify, WooCommerce en meer
answer: Cloudflare deelt AI-bots in drie typen in: Search, Agent en Training. Per type kies je Block on all pages, Block on pages with ads of Allow, onder Security Settings en dan Configure AI bot policies. De pagina, voor het laatst bijgewerkt op 1 juli 2026, zegt dat nieuwe standaardinstellingen voor nieuwe domeinen op 15 september 2026 ingaan.

## Waar de instelling staat in Cloudflare

Ga in het Cloudflare-dashboard naar Security Settings en dan naar Configure AI bot policies. Elk van de drie typen heeft een eigen instelling. Dit werkt op netwerkniveau, dus het geldt voor elk platform waarop de site draait.

## Drie typen, drie keuzes en een datum die al voorbij is

De presets van Cloudflare zijn: Search, crawlers die je content verzamelen of indexeren om er later vragen over te beantwoorden; Agent, geautomatiseerde activiteit die in realtime namens een persoon handelt, zoals chat-fetchbots en browser-use-agents; Training, crawlers die je content gebruiken om een model te trainen of te finetunen, inclusief crawlers met gemengd doel die voor zowel Training als Search worden gebruikt. Elke preset blokkeert geverifieerde bots die zo zijn ingedeeld, plus enkele niet-geverifieerde bots die zich op dezelfde manier gedragen. De pagina, voor het laatst bijgewerkt op 1 juli 2026, kondigt nieuwe standaardinstellingen voor nieuwe domeinen aan vanaf 15 september 2026: Training- en Agent-bots geblokkeerd op pagina's die advertenties tonen, Search blijft toegestaan, en crawlers met gemengd doel geblokkeerd door elke configuratie die AI-training blokkeert, inclusief de oudere optie Block AI bots, die Cloudflare op die datum als uitfaserend markeert. De pagina gebruikte nog de toekomende tijd toen wij haar op 21 oktober lazen, vijf weken na die datum. Open dus je eigen dashboard en kijk wat er aanstaat, in plaats van een van beide teksten te vertrouwen.

In de woorden van de leverancier (origineel in het Engels): “Search: crawlers that collect or index your content to answer questions about it later.”

Bron: [Cloudflare Docs: Block AI Bots](https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/), gelezen op 21 oktober 2026.

## De stappen

1. Open je zone in het Cloudflare-dashboard en ga naar Security Settings.
2. Open Configure AI bot policies.
3. Kies voor Search, Agent en Training Block on all pages, Block on pages with ads of Allow.
4. Gebruik je de oudere optie Block AI bots, controleer dan welke crawlers met gemengd doel die nu dekt, want Cloudflare zegt dat die wordt uitgefaseerd.
5. Test met de gratis [AI-crawler-toegangscheck](/nl/tools/ai-crawler-check): een bot die robots.txt toestaat, kan hier toch geweigerd worden.

## De regels om te gebruiken

Toestaan:

```
# Cloudflare settings are not robots.txt lines.
# Choose Allow (do not block) for Search so answer engines can fetch pages.
```

Blokkeren:

```
# Cloudflare settings are not robots.txt lines.
# Choose Block (on all pages) for Training; leave Search on Allow.
```

## Aandachtspunten

Het risico voor een winkel die geciteerd wil worden zit in de middelste preset: Cloudflare definieert Agent als chat-fetchbots die namens een persoon handelen, en dat is het werk van fetchers zoals [ChatGPT-User](/nl/bots/chatgpt-user). Agent blokkeren kan voorkomen dat een assistent je pagina opent als iemand ernaar vraagt, ook als je robots.txt dat toestaat. Let er ook op dat Shopify zegt dat het een proxyconfiguratie voor een Shopify-winkel niet aanraadt.

## Vergelijk met Shopify

[Shopify](/nl/platforms/shopify): Zegt dat het bot management zelf afhandelt en raadt een proxy af.

## Controleer je eigen site

De gratis check in het vak hierboven leest robots.txt voor de AI-crawlers en stuurt per crawler één live verzoek. Zo zie je ook een regel die de instellingen van je platform toestaan maar een firewall weigert. De volledige lijst met crawlers staat op [de AI-crawlerhub](/nl/bots).

## FAQ

### Gaat de AI-blokkade van Cloudflare boven robots.txt?

De pagina van Cloudflare beschrijft blokkeren op gedrag in het eigen netwerk, dus een bot kan daar geweigerd worden, ook als je robots.txt hem toestaat. Daarom is een test met een live verzoek belangrijk.

### Wat is het verschil tussen Search en Training bij Cloudflare?

Search-crawlers indexeren content om later vragen te beantwoorden; Training-crawlers gebruiken content om een model te trainen of te finetunen. Crawlers met gemengd doel vallen onder Training.

### Is Block AI bots nog beschikbaar?

Cloudflare markeert de optie als uitfaserend op 15 september 2026. De pagina stond nog in de toekomende tijd toen we haar op 21 oktober 2026 lazen.

## Sources

- [Cloudflare Docs: Block AI Bots](https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/), gelezen op 21 oktober 2026
