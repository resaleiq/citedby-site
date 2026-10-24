title: PrestaShop: robots.txt-generator: één set regels voor alle bots
slug: prestashop
description: De gids van PrestaShop beschrijft een knop Generate robots.txt die je bestand vervangt en alleen User-agent: * gebruikt. Voeg AI-regels toe na het genereren.
section: platforms
locale: nl
cluster: AI-crawlers per platform
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over PrestaShop: Waar Traffic, SEO and URLs, Knop Generate robots.txt, User-agent Alleen asterisk, Opnieuw genereren Vervangt het bestand
hero_sub: Instellingen voor AI-crawlers op PrestaShop
hero_boxes: Waar|Traffic > SEO and URLs; Knop|Generate robots.txt; User-agent|Alleen *; Opnieuw genereren|Vervangt het bestand
widget: on
related: /nl/platforms|Alle platforms vergeleken; /nl/platforms/shopify|Shopify; /nl/bots|AI-crawlers vergeleken; /nl/guides/cms|Checklist AI-zichtbaarheid voor Shopify, WooCommerce en meer
answer: De gebruikershandleiding van PrestaShop beschrijft een tool voor Robots file generation onder Shop Parameters, Traffic, SEO and URLs. Die schrijft met User-agent: * uitsluitingsregels voor niet-openbare bestanden en noemt dus geen AI-crawler. Een klik op Generate robots.txt vervangt elk bestaand bestand, dus voeg je eigen AI-crawlerregels pas toe na het genereren.

## Waar de instelling staat in PrestaShop

De gebruikershandleiding van PrestaShop 8 plaatst het onder Configuring your Shop Parameters, dan Traffic, dan SEO and URLs. De sectie heet Robots file generation. De pagina noemt daarbinnen geen verder menupad in de back office, en onderaan staat "Last updated 4 years ago".

## Het enige wat de pagina van PrestaShop zegt en die van andere platforms niet

PrestaShop geeft je geen vak om regels in te typen. Het geeft je een knop die het hele bestand schrijft. De handleiding zegt dat de generator "simply creates a file with exclusion directives for files and directories that are not meant to be public", toegepast op alle bots via de string "User-agent: *". Ook zegt de handleiding dat de slechtste bots het bestand negeren, omdat het "purely advisory" is. Het gevolg voor AI-crawlers staat in de laatste twee zinnen van de sectie: opnieuw genereren wist alles wat je hebt toegevoegd.

In de woorden van de leverancier (origineel in het Engels): “Clicking on the "Generate robots.txt" button replaces any existing robots.txt file with a new one. Therefore, if you want to add your own rules, do it after PrestaShop has generated its version of the file.”

Bron: [PrestaShop 8 User Guide: SEO and URLs](https://docs.prestashop-project.org/v.8-documentation/user-guide/configuring-shop/shop-parameters/traffic/seo-and-urls), gelezen op 24 oktober 2026.

## De stappen

1. Open SEO and URLs in de sectie Traffic van Shop Parameters.
2. Ga naar Robots file generation.
3. Klik op Generate robots.txt. Dit vervangt elk bestaand robots.txt-bestand.
4. Voeg je eigen regels toe nadat PrestaShop zijn versie heeft gegenereerd. De pagina zegt niet hoe je het gegenereerde bestand bewerkt, dus gebruik de bestandstoegang die je hosting biedt.
5. Open /robots.txt op je winkel om te controleren of je regels er nog staan. Herhaal stap 4 elke keer dat je opnieuw op de knop klikt.

## De regels om te gebruiken

Toestaan:

```
# Nothing to add: the generated file only lists files and directories that are not public.
# To name one explicitly, add after the generated block:
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

Het gegenereerde bestand spreekt elke bot op dezelfde manier aan, omdat het User-agent: * gebruikt en niets anders, dus de tool van PrestaShop geeft je geen keuze per crawler. De handleiding zegt dat je sommige bots volledige toegang wilt geven, zoals die van Google, en andere niet, zoals spambots en contentdieven, en dat is een beslissing die je neemt in je eigen toegevoegde groepen. De handleiding noemt AI-crawlers helemaal niet bij naam en wijst voor hen geen instelling of module aan.

## Vergelijk met Shopify

[Shopify](/nl/platforms/shopify): Een sjabloon robots.txt.liquid dat je toevoegingen behoudt, waar de knop van PrestaShop ze overschrijft.

## Controleer je eigen site

De gratis check in het vak hierboven leest robots.txt voor de AI-crawlers en stuurt per crawler één live verzoek. Zo zie je ook een regel die de instellingen van je platform toestaan maar een firewall weigert. De volledige lijst met crawlers staat op [de AI-crawlerhub](/nl/bots).

## FAQ

### Verwijdert opnieuw genereren van robots.txt in PrestaShop mijn AI-crawlerregels?

Ja, als je ze aan het gegenereerde bestand hebt toegevoegd. Volgens de handleiding van PrestaShop vervangt de knop elk bestaand robots.txt door een nieuw bestand en voeg je je eigen regels toe nadat het zijn versie heeft gegenereerd.

### Blokkeert PrestaShop standaard AI-crawlers?

De handleiding zegt dat niet. Die beschrijft een gegenereerd bestand met uitsluitingsregels voor niet-openbare bestanden en mappen onder User-agent: *, en noemt geen AI-crawler.

## Sources

- [PrestaShop 8 User Guide: SEO and URLs](https://docs.prestashop-project.org/v.8-documentation/user-guide/configuring-shop/shop-parameters/traffic/seo-and-urls), gelezen op 24 oktober 2026
