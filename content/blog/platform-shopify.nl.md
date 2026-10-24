title: Shopify: AI-crawlers toestaan of blokkeren en wat robots.txt mist
slug: shopify
description: Bewerk robots.txt.liquid om AI-crawlers op Shopify toe te staan of te blokkeren. Dat raakt volgens Shopify alleen het open web, niet de productdata.
section: platforms
locale: nl
cluster: AI-crawlers per platform
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Vier feiten over Shopify: Waar robots.txt.liquid, Support Niet ondersteund door Shopify, Catalog-feed Niet gedekt, Effect Direct
hero_sub: Instellingen voor AI-crawlers op Shopify
hero_boxes: Waar|robots.txt.liquid; Support|Niet ondersteund door Shopify; Catalog-feed|Niet gedekt; Effect|Direct
widget: on
related: /nl/platforms|Alle platforms vergeleken; /nl/platforms/squarespace|Squarespace; /nl/bots|AI-crawlers vergeleken; /nl/guides/cms|Checklist AI-zichtbaarheid voor Shopify, WooCommerce en meer
answer: Op Shopify beheer je AI-crawlers door een sjabloon robots.txt.liquid aan je thema toe te voegen. Op de helppagina van Shopify staat dat een blokkade daar alleen de vindbaarheid op het open web raakt: productdata gaat via Shopify Catalog, los van /robots.txt, nog steeds naar agentic storefronts zoals ChatGPT of Microsoft Copilot.

## Waar de instelling staat in Shopify

Online Store, dan Edit code van het thema, dan Add a new template en kies robots. Shopify zegt dat dit een niet-ondersteunde aanpassing is: Support kan niet helpen met bewerkingen, en verkeerd gebruik "can result in loss of all traffic".

## Het enige wat de pagina van Shopify zegt en die van andere platforms niet

Shopify beschrijft twee lagen van controle. De netwerklaag wordt door Shopify afgehandeld voor winkels op Shopify, en daar hoef je niets te doen. De laag /robots.txt is van jou via robots.txt.liquid. De pagina trekt daarna de lijn die voor een winkel telt: als je verkoopt via agentic storefronts zoals ChatGPT of Microsoft Copilot, wordt je productdata via Shopify Catalog verspreid "independently of /robots.txt", en het blokkeren van AI-crawlers op een van beide lagen "affects only open-web discoverability". Om te wijzigen wat Catalog deelt gebruik je de instellingen voor agentic storefronts, niet robots.txt.

In de woorden van de leverancier (origineel in het Engels): “Blocking AI crawlers at the /robots.txt or network layer affects only open-web discoverability. It doesn't stop your product data from being sent by Shopify Catalog to the agentic storefronts that you've activated.”

Bron: [Shopify Help Center: Editing robots.txt.liquid](https://help.shopify.com/en/manual/promoting-marketing/seo/editing-robots-txt), gelezen op 21 oktober 2026.

## De stappen

1. Ga vanuit je Shopify-admin naar Online Store.
2. Open voor het thema dat je publiceert het menu en kies Edit code.
3. Klik op Add a new template, kies robots en dan Create template.
4. Houd de Liquid die de standaardregelgroepen uitvoert en voeg je eigen regels eronder toe. Shopify raadt dit aan boven het vervangen van het bestand door gewone tekst, omdat gewone tekst verouderd raakt.
5. Sla op in het gepubliceerde thema. Shopify zegt dat wijzigingen direct gelden, maar crawlers reageren niet altijd meteen.

## De regels om te gebruiken

Toestaan:

```
# Nothing to add: Shopify's default robots.txt allows crawlers that are not named.
# To name one explicitly, add under the default Liquid block:
User-agent: OAI-SearchBot
Allow: /
```

Blokkeren:

```
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /
```

## Aandachtspunten

Twee details van dezelfde pagina. Een thema dat je uploadt vanuit de sectie Themes van de admin importeert robots.txt.liquid niet; wijzigingen via ThemeKit of de opdrachtregel behouden het wel. En als je sjabloon de standaardgroepen uitvoert, verwijder het dan om de huidige standaard van Shopify op te pikken, die regels kan bevatten die je oudere kopie mist, zoals Disallow: /search.

## Vergelijk met Squarespace

[Squarespace](/nl/platforms/squarespace): Eén selectievakje in plaats van een sjabloon, en een vaste lijst van 26 namen.

## Controleer je eigen site

De gratis check in het vak hierboven leest robots.txt voor de AI-crawlers en stuurt per crawler één live verzoek. Zo zie je ook een regel die de instellingen van je platform toestaan maar een firewall weigert. De volledige lijst met crawlers staat op [de AI-crawlerhub](/nl/bots).

## FAQ

### Stopt het blokkeren van GPTBot op Shopify dat ChatGPT mijn producten toont?

Niet op zichzelf. Shopify zegt dat robots.txt en netwerkblokkades alleen de vindbaarheid op het open web raken, en dat Shopify Catalog productdata los van /robots.txt naar de agentic storefronts stuurt die je hebt geactiveerd. Gebruik de instellingen voor agentic storefronts van Shopify om die feed te beheren.

### Kan Shopify Support mijn robots.txt.liquid repareren?

Nee. Op de pagina van Shopify staat dat Support niet kan helpen met bewerkingen aan het bestand, en dat je een Shopify Partner kunt inhuren.

### Heb ik een Cloudflare-proxy voor Shopify nodig?

Shopify zegt dat bot management op netwerkniveau wordt afgehandeld voor winkels op Shopify, en dat het een proxyconfiguratie voor Shopify niet aanraadt en niet ondersteunt.

## Sources

- [Shopify Help Center: Editing robots.txt.liquid](https://help.shopify.com/en/manual/promoting-marketing/seo/editing-robots-txt), gelezen op 21 oktober 2026
- [Shopify.dev: Customize robots.txt.liquid](https://shopify.dev/docs/storefronts/themes/seo/robots-txt), gelezen op 21 oktober 2026
