title: AI-zichtbaarheid op Shopify, WooCommerce en andere platforms
h1: AI-zichtbaarheid op Shopify, WooCommerce en andere webshopplatforms: een checklist
description: Waar u op Shopify, WooCommerce en andere platforms robots.txt aanpast, uw sitemap vindt en product-JSON-LD en JavaScript-only tekst controleert.
slug: cms
section: guides
locale: nl
cluster: Platforms
date: 2026-10-20
reviewed: 2026-10-20
answer: Op Shopify past u robots.txt aan via het bestand robots.txt.liquid in uw thema, en uw sitemap staat vanzelf op /sitemap.xml. WooCommerce draait op WordPress, dat een sitemap op /wp-sitemap.xml aanmaakt en in WooCommerce Product-JSON-LD plaatst. Voor andere platforms zoekt u de instellingen voor robots.txt en sitemap in het beheerpaneel.
widget: on
howto: on
related: /nl/guides/technical-seo-checklist|Technische SEO-checklist; /nl/blog/is-gptbot-blocked|Is GPTBot geblokkeerd op uw site?; /nl/ai-visibility-audit|AI-zichtbaarheidsaudit
hero: auto
hero_alt: Titelkaart: AI-zichtbaarheid op Shopify en WooCommerce, met drie vakken: robots.txt, sitemap, productdata
hero_sub: Per platform waar u wat instelt
hero_boxes: Shopify|robots.txt.liquid; WooCommerce|WordPress en Product-JSON-LD; Ander platform|zoek in het beheerpaneel
steps_img: on

## Waarom hangt AI-zichtbaarheid af van uw platform?

Of een crawler uw webshop leest, hangt af van vier dingen: robots.txt, uw sitemap, uw productdata en de vraag of de tekst in de HTML staat. Op een eigen maatwerksite past u dat in code aan. Op een platform zoals Shopify of WooCommerce zit het meeste in thema, plugins en instellingen. Dit stuk zegt per platform waar u moet kijken. Alleen wat in de officiële documentatie staat, noemen we als feit. De rest is algemeen advies.

## Welke vijf stappen doorloopt u op elk platform?

1. Open robots.txt. Ga naar `uwwebshop.nl/robots.txt` en kijk welke crawlers geblokkeerd zijn.
2. Zoek uw sitemap. Open `uwwebshop.nl/sitemap.xml` of de variant van uw platform.
3. Controleer product-JSON-LD. Bekijk de paginabron van een product en zoek `application/ld+json`.
4. Zoek tekst die alleen met JavaScript verschijnt. Kijk in de paginabron of productnaam en prijs er staan.
5. Test opnieuw na elke thema- of pluginwijziging. Een update kan eerdere instellingen overschrijven.

## Hoe pakt u het aan op Shopify?

Shopify heeft een standaard robots.txt voor elke winkel. Volgens de Shopify-documentatie werkt die voor de meeste winkels. Wilt u hem aanpassen, dan voegt u een `robots.txt.liquid` toe aan de map `templates` van uw thema in de code-editor. Daarmee kunt u URL's toestaan of weigeren, crawl-delay-regels toevoegen, sitemap-URL's toevoegen en bepaalde crawlers blokkeren ([Shopify: robots.txt.liquid bewerken](https://help.shopify.com/en/manual/promoting-marketing/seo/editing-robots-txt)).

Let op twee dingen die Shopify zelf noemt. Het is een niet-ondersteunde aanpassing: Shopify Support helpt er niet bij en onjuist gebruik kan al uw verkeer kosten. Daarnaast bepaalt robots.txt alleen de open web-vindbaarheid. Verkoopt u via agentische storefronts zoals ChatGPT of Microsoft Copilot, dan wordt uw productdata via Shopify Catalog los van robots.txt aangeleverd.

De sitemap maakt Shopify automatisch aan op `/sitemap.xml`. Hij verwijst naar aparte sitemaps voor producten, collecties, blogs en pagina's en wordt bijgewerkt als u iets toevoegt ([Shopify: sitemap vinden en indienen](https://help.shopify.com/en/manual/promoting-marketing/seo/find-site-map)). Staat uw winkel in privémodus, dan kan een crawler hem niet lezen.

Shopify geeft ook advies voor productpagina's voor AI: uitgebreide specificaties, een volledige beschrijving en gestructureerde data en productattributen ([Shopify: uw winkel optimaliseren voor AI](https://help.shopify.com/en/manual/promoting-marketing/seo/optimizing-store-for-ai)). Of uw thema product-JSON-LD plaatst en met welke prijs, controleert u in de paginabron. Dat verschilt per thema en app, dus ga niet op aannames af.

## Hoe pakt u het aan op WooCommerce?

WooCommerce draait op WordPress. Sinds WordPress 5.5 maakt WordPress zelf een sitemapindex aan op `/wp-sitemap.xml`, en de robots.txt van WordPress verwijst ernaar ([WordPress: XML-sitemaps in 5.5](https://make.wordpress.org/core/2020/07/22/new-xml-sitemaps-functionality-in-wordpress-5-5/)). Gebruikt u een SEO-plugin, dan kan die een eigen sitemap-URL gebruiken, dus open beide en kijk welke gevuld is.

Eén instelling die vaak wordt vergeten: onder Instellingen, Lezen, bestaat het vakje "Zoekmachines ontmoedigen deze site te indexeren". Staat dat aan, dan krijgt elke pagina een `noindex,nofollow`-tag ([WordPress: scherm Lezen](https://wordpress.org/documentation/article/settings-reading-screen/)). Op een testomgeving is dat handig, op een live webshop houdt het uw pagina's uit de zoekresultaten.

WooCommerce zelf voegt Product-gegevens toe als JSON-LD. In de broncode van WooCommerce is te zien dat het `Product` met `Offer` of `AggregateOffer` genereert op de productpagina ([WooCommerce: class-wc-structured-data.php](https://github.com/woocommerce/woocommerce/blob/trunk/plugins/woocommerce/includes/class-wc-structured-data.php)). Een SEO- of feedplugin kan een tweede blok toevoegen. Zoek in de paginabron dus op het aantal `application/ld+json`-blokken en vergelijk de prijzen.

## En op andere platforms?

Voor Lightspeed, Magento, Wix, Squarespace, Shopware, een eigen maatwerksite of een ander platform hebben wij hier geen officiële documentatie geopend, dus we doen geen platformspecifieke beweringen. Het algemene advies is voor elk platform gelijk:

| Wat | Waar u kijkt |
| --- | --- |
| robots.txt | Zoek in de instellingen van uw platform naar SEO of robots. Kan het niet, vraag uw leverancier |
| Sitemap | Open `/sitemap.xml` en zoek in de helpdocumentatie van uw platform |
| Product-JSON-LD | Paginabron van een product, zoek `application/ld+json` |
| Tekst met JavaScript | Paginabron, zoek uw productnaam en prijs |

## Hoe vindt u tekst die alleen met JavaScript verschijnt?

Dit is de fout die op elk platform kan voorkomen. Thema's en plugins voor reviews, prijsblokken, tabbladen met specificaties of "laad meer"-lijsten bouwen hun tekst vaak met JavaScript op. Een bezoeker ziet alles, een crawler die geen scripts draait niet.

Test het zo: kies "Paginabron weergeven" (niet "Element inspecteren") en zoek op een zin uit uw productbeschrijving en op de prijs. Staat de zin er niet, dan ontbreekt de tekst voor die crawler. Schakel de plugin of het thema-onderdeel uit om te zien of de tekst terugkomt in de bron, en vraag zo nodig uw leverancier om server-side rendering.

Wilt u alle pagina's laten nakijken, gebruik dan de [AI-zichtbaarheidsaudit](/nl/ai-visibility-audit): die crawlt elke pagina en geeft de exacte oplossing. De volledige reeks controles staat in de [technische SEO-checklist](/nl/guides/technical-seo-checklist).

## FAQ

### Kan ik robots.txt op Shopify aanpassen?
Ja, via een `robots.txt.liquid` in uw thema. Shopify noemt het wel een niet-ondersteunde aanpassing en raadt aan het met een Shopify Partner of met kennis van code en SEO te doen.

### Waar vind ik mijn sitemap op WooCommerce?
Meestal op `/wp-sitemap.xml`, de sitemap die WordPress sinds versie 5.5 zelf maakt. Een SEO-plugin kan een andere URL gebruiken, dus controleer beide.

### Blokkeert robots.txt AI-crawlers voor mijn Shopify-producten in ChatGPT?
Volgens Shopify bepaalt robots.txt alleen de open web-vindbaarheid. Als u via agentische storefronts verkoopt, wordt uw productdata via Shopify Catalog apart aangeleverd.

### Moet ik een plugin installeren om zichtbaar te zijn voor AI?
Nee, een plugin is geen vereiste. Controleer eerst robots.txt, uw sitemap, uw JSON-LD en de tekst in de HTML.

## Sources

- [Shopify: robots.txt.liquid bewerken](https://help.shopify.com/en/manual/promoting-marketing/seo/editing-robots-txt)
- [Shopify: sitemap vinden en indienen](https://help.shopify.com/en/manual/promoting-marketing/seo/find-site-map)
- [Shopify: uw winkel optimaliseren voor AI](https://help.shopify.com/en/manual/promoting-marketing/seo/optimizing-store-for-ai)
- [WordPress: XML-sitemaps in WordPress 5.5](https://make.wordpress.org/core/2020/07/22/new-xml-sitemaps-functionality-in-wordpress-5-5/)
- [WordPress: instellingenscherm Lezen](https://wordpress.org/documentation/article/settings-reading-screen/)
- [WooCommerce: broncode voor gestructureerde data](https://github.com/woocommerce/woocommerce/blob/trunk/plugins/woocommerce/includes/class-wc-structured-data.php)
- [Google Search Central: basis van JavaScript-SEO](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
