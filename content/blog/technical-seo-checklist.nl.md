title: Technische SEO-checklist voor AI-zichtbaarheid van webshops
h1: Technische SEO-checklist voor AI-zichtbaarheid: 9 controles voor je webshop
description: Negen technische controles die bepalen of AI-assistenten je webshop kunnen lezen, elk met een manier om het zelf na te kijken. Van robots.txt tot JSON-LD.
slug: technical-seo-checklist
section: guides
locale: nl
cluster: Technische basis
date: 2026-10-20
reviewed: 2026-10-20
answer: Voor AI-zichtbaarheid controleert je negen technische punten: robots.txt en AI-crawlers, statuscodes, sitemap.xml, canonical, hreflang, titel en H1, JSON-LD voor Product en Organization, tekst in de ruwe HTML, kapotte interne links. llms.txt is optioneel. Elk punt kun je in enkele minuten zelf nakijken.
widget: on
howto: on
related: /nl/blog/is-gptbot-blocked|Is GPTBot geblokkeerd op je site?; /nl/blog/does-llms-txt-work|Werkt llms.txt?; /nl/guides/cms|AI-zichtbaarheid op Shopify en WooCommerce
hero: auto
hero_alt: Titelkaart: technische SEO-checklist voor AI-zichtbaarheid, met drie vakken: toegang, structuur, leesbare tekst
hero_sub: Negen controles die je zelf kunt doen
hero_boxes: Toegang|robots.txt en statuscodes; Structuur|sitemap canonical hreflang; Leesbare tekst|HTML zonder JavaScript; Data|JSON-LD voor product
steps_img: on

## Wat moet technisch kloppen voordat AI-assistenten je webshop kunnen lezen?

Een assistent kan alleen noemen wat hij kan ophalen en lezen. Dat is de technische basis: de crawler komt binnen, krijgt een goede pagina terug en begrijpt wat erop staat. Hieronder staan negen controles, elk met een manier om het met de hand na te kijken. Gebruik je eigen domein, bijvoorbeeld `jouwwebshop.nl`.

## De checklist in negen punten

1. robots.txt en AI-crawlers. Open `jouwwebshop.nl/robots.txt`. Zoek groepen voor `OAI-SearchBot`, `GPTBot`, `PerplexityBot` en `Google-Extended`, en kijk of onder `User-agent: *` een `Disallow: /` staat. Zo'n regel geldt voor elke crawler zonder eigen groep ([RFC 9309](https://www.rfc-editor.org/info/rfc9309/)). Uitleg per laag vind je in [Is GPTBot geblokkeerd op je site?](/nl/blog/is-gptbot-blocked).
2. HTTP-status van de belangrijkste pagina's. Controleer homepage, een categoriepagina, een productpagina en je verzend- en retourpagina. Ze horen 200 terug te geven. Met `curl -sI https://jouwwebshop.nl/` zie je de statuscode. Een 403, 429 of 503 wijst op een regel of storing die ook crawlers raakt ([Google: HTTP-statuscodes](https://developers.google.com/crawling/docs/troubleshooting/http-status-codes)).
3. sitemap.xml. Open `jouwwebshop.nl/sitemap.xml`. Staan je producten en categorieën erin, en alleen pagina's die 200 teruggeven? Verwijs er ook naar met een `Sitemap:`-regel in robots.txt ([Google: sitemap maken](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)).
4. Canonical. Bekijk de paginabron van een productpagina en zoek `rel="canonical"`. De URL hoort naar de schone productpagina te wijzen, niet naar een filter- of sorteerversie ([Google: dubbele URL's samenvoegen](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)).
5. hreflang. Verkoopt je in Nederland en België, of in meer talen, dan horen versies naar elkaar te verwijzen met `rel="alternate" hreflang="nl-NL"` en `hreflang="nl-BE"`. Elke versie noemt zichzelf en de andere ([Google: gelokaliseerde versies](https://developers.google.com/search/docs/specialty/international/localized-versions)). Verkoopt je maar in één taal, sla dit punt over.
6. Titel en H1. Elke pagina heeft een eigen, beschrijvende `<title>` en één H1 die zegt wat de pagina is. Zoek in de paginabron naar `<title>` en `<h1>`. Dubbele titels bij tientallen producten zijn een veelvoorkomend gebrek ([Google: titellinks](https://developers.google.com/search/docs/appearance/title-link)).
7. JSON-LD voor Product en Organization. Zoek in de paginabron naar `application/ld+json`. Op productpagina's lees je `Product` met `name`, `offers`, `price` en `priceCurrency`, op de homepage `Organization` met naam, logo en contactgegevens ([Google: Product-markup](https://developers.google.com/search/docs/appearance/structured-data/product)). Staat daar een oude prijs, dan citeert een assistent die misschien ook.
8. Tekst in de ruwe HTML. Kies "Paginabron weergeven" (niet "Element inspecteren", dat toont de pagina na JavaScript) en zoek op je productnaam, prijs en een zin uit de beschrijving. Staat die er niet, dan bouwt de pagina zijn tekst met JavaScript en kan een crawler zonder scripts niets lezen ([Google: JavaScript-SEO](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)).
9. Kapotte interne links. Klik door je hoofdmenu, categoriepagina's en de "gerelateerde producten" en let op 404's. Een crawler gebruikt interne links om pagina's te vinden. Een verouderd productlinkje dat naar een 404 leidt, is een doodlopende weg.

## Hoe zie je het resultaat in één overzicht?

| Controle | Handmatige test | Wat je zoekt |
| --- | --- | --- |
| robots.txt | `/robots.txt` openen | Geen `Disallow: /` voor crawlers die je wilt |
| Statuscode | `curl -sI` op vijf pagina's | 200 |
| sitemap.xml | `/sitemap.xml` openen | Producten en categorieën erin |
| Canonical | Paginabron | URL wijst naar zichzelf |
| hreflang | Paginabron | Wederzijdse verwijzingen |
| Titel en H1 | Paginabron | Uniek per pagina |
| JSON-LD | Paginabron | Juiste prijs en valuta |
| Ruwe HTML | Paginabron | Productnaam en prijs staan er |
| Interne links | Doorklikken | Geen 404's |

## En llms.txt?

llms.txt is optioneel. Geen enkele grote assistent heeft bevestigd dat hij het bestand leest, en Google zegt dat je geen AI-tekstbestand nodig hebt voor zijn AI-functies. Zet het onderaan je lijst, na de negen punten hierboven. De cijfers en bronnen staan in [Werkt llms.txt?](/nl/blog/does-llms-txt-work).

## Hoe gaat je verder met de uitkomst?

Loop de lijst een keer door en noteer per punt of het klopt. Sluit je een crawler buiten, begin dan bij punt 1 en 2. Zie je lege pagina's in punt 8, dan helpt geen enkele andere aanpassing totdat de tekst op de server wordt gerenderd.

Heb je honderden producten, dan is handmatig nakijken traag. De [AI-zichtbaarheidsaudit](/nl/ai-visibility-audit) crawlt je site tot de paginalimiet van je abonnement, controleert deze punten en geeft per probleem de exacte oplossing, vanaf €9 eenmalig. Op Shopify of WooCommerce past je dingen op een andere plek aan. Dat staat in [AI-zichtbaarheid op Shopify en WooCommerce](/nl/guides/cms).

## FAQ

### Hoe vaak moet ik deze checklist doorlopen?
Na elke grote wijziging aan je thema, je platform of je CDN, en daarnaast ongeveer eens per kwartaal. Een thema-update kan stilletjes je JSON-LD of robots.txt veranderen.

### Is technische SEO voor AI anders dan voor Google?
De basis is gelijk: toegang, statuscodes, sitemap, canonical en leesbare HTML. Voor AI-assistenten komt daar de keuze per crawler bij, omdat OpenAI GPTBot, OAI-SearchBot en ChatGPT-User apart aanstuurt.

### Moet ik JSON-LD zelf schrijven?
Meestal niet. Veel webshopplatforms voegen Product-markup toe. Controleer wel of prijs en valuta kloppen. Hoe dat per platform werkt, staat in de gids voor Shopify en WooCommerce.

### Wat als ik geen hreflang gebruik?
Verkoopt je in één taal en één land, dan is dat prima. Hreflang is bedoeld voor sites met meerdere taal- of landversies.

## Sources

- [IETF RFC 9309: Robots Exclusion Protocol](https://www.rfc-editor.org/info/rfc9309/)
- [Google Search Central: HTTP-statuscodes en netwerkfouten](https://developers.google.com/crawling/docs/troubleshooting/http-status-codes)
- [Google Search Central: een sitemap maken](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [Google Search Central: dubbele URL's samenvoegen (canonical)](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- [Google Search Central: gelokaliseerde versies (hreflang)](https://developers.google.com/search/docs/specialty/international/localized-versions)
- [Google Search Central: titellinks](https://developers.google.com/search/docs/appearance/title-link)
- [Google Search Central: Product-markup](https://developers.google.com/search/docs/appearance/structured-data/product)
- [Google Search Central: basis van JavaScript-SEO](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- [Google Search Central: AI-functies en je website](https://developers.google.com/search/docs/appearance/ai-features)
- [OpenAI: crawlers en user agents](https://developers.openai.com/api/docs/bots)
