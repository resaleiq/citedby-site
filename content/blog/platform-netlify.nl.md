title: Netlify: blokkeer AI-crawlers met robots.txt + User Agent Blocker
slug: netlify
description: Netlify heeft geen robots.txt-instelling: lever een bestand vanuit je siteroot of installeer User Agent Blocker. De gids van Netlify zegt: gebruik beide.
section: platforms
locale: nl
cluster: AI-crawlers per platform
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over Netlify: Waar robots.txt in de siteroot, Edge-blokkade User Agent Blocker, Activering Eén project tegelijk, Terugval Edge Function
hero_sub: Instellingen voor AI-crawlers op Netlify
hero_boxes: Waar|robots.txt in de siteroot; Edge-blokkade|User Agent Blocker; Activering|Eén project tegelijk; Terugval|Edge Function
widget: on
related: /nl/platforms|Alle platforms vergeleken; /nl/platforms/cloudflare|Cloudflare; /nl/bots|AI-crawlers vergeleken; /nl/guides/cms|Checklist AI-zichtbaarheid voor Shopify, WooCommerce en meer
answer: Netlify biedt twee routes. De eerste is een robots.txt-bestand dat vanuit de root van je site wordt geleverd. De tweede is de extensie User Agent Blocker, die met een Netlify Edge Function verzoeken blokkeert op user agent. De developergids van Netlify zegt dat robots.txt alleen niet genoeg is, omdat sommige AI-producten het negeren.

## Waar de instelling staat in Netlify

In de dashboardpagina's die we hebben gelezen is er geen robots.txt-editor. De developergids van Netlify zegt dat je je regels in een robots.txt-bestand zet dat "served from the root of your site" is. De aparte docs-pagina over het blokkeren van AI-crawlers behandelt de extensie User Agent Blocker, die je na installatie vindt onder Extensions in de linkernavigatie van je project.

## Het enige wat de pagina's van Netlify zeggen en die van andere platforms niet

De eigen gids van Netlify behandelt robots.txt als de eerste van twee lagen, niet als het hele antwoord. Hij toont een robots.txt met per bot één blok User-agent en Disallow, gegenereerd uit een JSON-lijst met namen, en voegt daar een Edge Function aan toe die de User-Agent-header van elk verzoek met dezelfde lijst vergelijkt en bij een treffer HTTP 401 teruggeeft. De gids zegt dat sommige AI-producten robots.txt niet respecteren, en voegt dan toe dat de controle op user agent zelf ook een gat heeft.

In de woorden van de leverancier (origineel in het Engels): “Sadly, some bots have been found to mis-report their names in their User Agent strings, so we can’t rely on that technique alone either.”

Bron: [Netlify Developers: Blocking AI bots and controlling crawlers](https://developers.netlify.com/guides/blocking-ai-bots-and-controlling-crawlers/), gelezen op 24 oktober 2026.

## De stappen

1. Schrijf een robots.txt met een regel User-agent en Disallow: / voor elke bot die je wilt blokkeren, en lever het bestand vanuit de root van je site. De gids genereert het bestand met een klein buildscript uit een lijst met namen, om typefouten te voorkomen.
2. Deploy de site. De gids merkt op dat AI-crawlers het bestand zouden moeten respecteren ("should"), en daarom voegt hij een tweede laag toe.
3. Voor de extensie: selecteer in het dashboard van je Netlify-project Extensions in de linkerzijbalk, zoek naar User Agent Blocker, selecteer hem en selecteer Install. Daarmee is hij beschikbaar voor alle projecten in je Netlify-team.
4. Ga naar het project waar je hem actief wilt hebben. Je kunt de extensie maar voor één project tegelijk activeren. Selecteer onder Extensions in de linkernavigatie User Agent Blocker.
5. Selecteer onder Block User Agents het verkeer dat je wilt blokkeren. Om AI-crawlers en bots te blokkeren selecteer je alle AI-crawleropties.
6. Selecteer Redeploy site en bevestig met Save, en selecteer daarna Enable analytics and deploy site. Netlify zegt dat blokkeren direct werkt zodra de deploy slaagt.

## De regels om te gebruiken

Toestaan:

```
User-agent: OAI-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /
```

Blokkeren:

```
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /
```

De pagina's van Netlify tonen alleen Disallow-regels. De Allow-regels hierboven zijn standaard robots.txt, niet iets wat Netlify documenteert.

## Aandachtspunten

Netlify zegt dat de vooraf ingestelde lijst van de extensie "does not include all possible AI crawlers and AI bots", dus een crawler die niet op de lijst staat wordt niet geblokkeerd. Dezelfde pagina noemt naast de AI-crawlers ook SEO- en zoekcrawlers, dus selecteer alleen de AI-opties als je nog zoekverkeer wilt. De voorbeeld-Edge Function van de gids antwoordt met een 401 op elk overeenkomend verzoek, op de hele site.

## Vergelijk met Cloudflare

[Cloudflare](/nl/platforms/cloudflare): Een schakelaar op netwerkniveau die werkt op elk siteplatform, terwijl de extensie van Netlify per project geldt.

## Controleer je eigen site

De gratis check in het vak hierboven leest robots.txt voor de AI-crawlers en stuurt per crawler één live verzoek. Zo zie je ook een regel die de instellingen van je platform toestaan maar een firewall weigert. De volledige lijst met crawlers staat op [de AI-crawlerhub](/nl/bots).

## FAQ

### Is robots.txt genoeg om AI-bots op Netlify te blokkeren?

Volgens de gids van Netlify niet. Die zegt dat niet alle AI-producten robots.txt respecteren en raadt aan een Edge Function of de extensie User Agent Blocker toe te voegen die op user agent blokkeert. Ook zegt de gids dat sommige bots hun user agent verkeerd opgeven, dus de twee lagen samen vormen het antwoord van Netlify.

### Kan ik de User Agent Blocker voor alle projecten tegelijk aanzetten?

Niet volgens de docs van Netlify. Door hem te installeren wordt de extensie beschikbaar voor alle projecten in je team, maar je kunt hem maar voor één project tegelijk activeren.

## Sources

- [Netlify Developers: Blocking AI bots and controlling crawlers](https://developers.netlify.com/guides/blocking-ai-bots-and-controlling-crawlers/), gelezen op 24 oktober 2026
- [Netlify Docs: Block AI crawlers and bots](https://docs.netlify.com/build/build-with-ai/block-ai-crawlers), gelezen op 24 oktober 2026
