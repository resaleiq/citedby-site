title: Framer: upload je eigen robots.txt met Static Files
slug: framer
description: Framer genereert een robots.txt voor elke gepubliceerde site. Je wijzigt hem door via Static Files je eigen bestand te uploaden (Pro of Enterprise).
section: platforms
locale: nl
cluster: AI-crawlers per platform
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over Framer: Waar Static Files, Abonnementen Pro en Enterprise, Standaard Automatisch gegenereerd, Eigen bestand Vervangt standaard
hero_sub: Instellingen voor AI-crawlers op Framer
hero_boxes: Waar|Static Files; Abonnementen|Pro en Enterprise; Standaard|Automatisch gegenereerd; Eigen bestand|Vervangt standaard
widget: on
related: /nl/platforms|Alle platforms vergeleken; /nl/platforms/webflow|Webflow; /nl/bots|AI-crawlers vergeleken; /nl/guides/cms|Checklist AI-zichtbaarheid voor Shopify, WooCommerce en meer
answer: Framer genereert een robots.txt voor elke gepubliceerde site. Om AI-crawlers toe te staan of te blokkeren upload je je eigen bestand via Static Files, met het pad ingesteld op /. Framer zegt dat dit beschikbaar is bij de abonnementen Pro en Enterprise en dat je upload het gegenereerde bestand vervangt in plaats van eraan toe te voegen.

## Waar de instelling staat in Framer

Ga in je projectdashboard naar je domein, open het tabblad Files en upload je bestand met het pad ingesteld op /. Op de helppagina van Framer heet dit Static Files. Wil je eerst het live bestand zien, voeg dan /robots.txt toe aan het domein van je site in een browser.

## Het enige wat de pagina van Framer zegt en die van andere platforms niet

Framer geeft je geen robots.txt-editor. Het bestand wordt voor je gegenereerd en je kunt het alleen wijzigen door een vervanger te uploaden, en dat hangt af van je abonnement. Op de pagina van Framer staat dat je met Static Files een eigen robots.txt kunt uploaden en dat het nieuwe bestand het automatisch gegenereerde bestand vervangt. De beperking per abonnement volgt direct daarna.

In de woorden van de leverancier (origineel in het Engels): “This is available on Pro and Enterprise plans.”

Bron: [Framer Help: Access your robots.txt file](https://www.framer.com/help/articles/how-can-i-access-the-robots-txt-file/), gelezen op 24 oktober 2026.

## De stappen

1. Schrijf je robots.txt als gewoon tekstbestand op je computer.
2. Ga naar je projectdashboard en selecteer je domein.
3. Open het tabblad Files.
4. Upload je bestand met het pad ingesteld op /.
5. Open yourdomain.com/robots.txt in een browser om te controleren of het live bestand van jou is.

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

## Aandachtspunten

Omdat je upload het gegenereerde bestand vervangt, is alles wat daarin stond weg, tenzij je het eerst kopieert. De pagina van Framer zegt niet wat het gegenereerde bestand bevat, dus lees yourdomain.com/robots.txt voordat je uploadt en bewaar de regels die je wilt houden, zoals een sitemapregel. De pagina gaat over robots.txt in het algemeen en noemt geen AI-crawlers bij naam, dus de user agents hierboven zijn voorbeelden die je moet controleren op de eigen pagina van elke leverancier. De pagina is voor het laatst bijgewerkt op 15 september 2026.

## Vergelijk met Webflow

[Webflow](/nl/platforms/webflow): Regels typ je in een instellingenveld in plaats van een bestand te uploaden, plus een Content-Signal-header.

## Controleer je eigen site

De gratis check in het vak hierboven leest robots.txt voor de AI-crawlers en stuurt per crawler één live verzoek. Zo zie je ook een regel die de instellingen van je platform toestaan maar een firewall weigert. De volledige lijst met crawlers staat op [de AI-crawlerhub](/nl/bots).

## FAQ

### Kan ik het robots.txt-bestand in Framer bewerken?

Ja, via upload. Op de pagina van Framer staat dat je in het projectdashboard het tabblad Files voor je domein opent en je bestand uploadt met het pad ingesteld op /. Framer zegt dat dit beschikbaar is bij de abonnementen Pro en Enterprise.

### Maakt Framer automatisch een robots.txt aan?

Ja. Framer zegt dat het voor elke gepubliceerde site een robots.txt genereert en dat een eigen bestand dat via Static Files is geüpload het standaardbestand vervangt.

## Sources

- [Framer Help: Access your robots.txt file](https://www.framer.com/help/articles/how-can-i-access-the-robots-txt-file/), gelezen op 24 oktober 2026
