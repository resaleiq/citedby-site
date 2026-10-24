title: Webflow: robots.txt-regels en de Content-Signal-header voor AI
slug: webflow
description: Waar de robots.txt-editor van Webflow staat, welk abonnement je nodig hebt en hoe de Content-Signal-header AI-training, zoeken en AI-input van elkaar scheidt.
section: platforms
locale: nl
cluster: AI-crawlers per platform
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Vier feiten over Webflow: Waar Site settings, SEO, Vereist Site- of betaald Workspace-abonnement, Extra Content-Signal, Status Voorgestelde extensie
hero_sub: Instellingen voor AI-crawlers op Webflow
hero_boxes: Waar|Site settings, SEO; Vereist|Site- of betaald Workspace-abonnement; Extra|Content-Signal; Status|Voorgestelde extensie
widget: on
related: /nl/platforms|Alle platforms vergeleken; /nl/platforms/wix|Wix; /nl/bots|AI-crawlers vergeleken; /nl/guides/cms|Checklist AI-zichtbaarheid voor Shopify, WooCommerce en meer
answer: Webflow zet robots.txt onder Site settings, dan SEO, dan Indexing, en een van de helppagina's zegt dat je een Site-abonnement of een betaald Workspace-abonnement nodig hebt. Het kan ook een Content-Signal-header sturen die ai-train, search en ai-input apart instelt. Webflow noemt dat een voorgestelde extensie, geen geaccepteerde standaard.

## Waar de instelling staat in Webflow

Ga naar Site settings, dan SEO, dan Indexing, voeg de robots.txt-regel of -regels toe die je wilt, klik op Save en publiceer je site. Webflow voegt standaard een sitemapregel toe; met een schakelaar haal je die weg.

## Een header die training, zoeken en AI-antwoorden scheidt

Naast robots.txt zegt de pagina van Webflow dat een site een HTTP-header Content-Signal kan leveren, in te stellen in hetzelfde gebied Indexing, om AI-crawlers gedetailleerdere instructies te geven. Het voorbeeld is `Content-Signal: ai-train=no, search=yes, ai-input=no`. Webflow legt de splitsing uit: robots.txt bepaalt of bots toegang hebben tot je pagina's, terwijl Content-Signal apart zegt of content mag worden gebruikt voor AI-training, zoekindexering of door AI gegenereerde antwoorden. Webflow plaatst zelf de kanttekening: dit is gebaseerd op een voorgestelde extensie van RFC 9309 en is nog geen geaccepteerde standaard. Het geeft dus een voorkeur aan; het stopt geen crawler, en de pagina van Webflow zegt niet welke crawlers het lezen.

In de woorden van de leverancier (origineel in het Engels): “This is based on a proposed extension to RFC 9309 and is not yet an accepted standard.”

Bron: [Webflow Help: Set robots.txt rules](https://help.webflow.com/hc/en-us/articles/41954080897683-Set-robots-txt-rules), gelezen op 21 oktober 2026.

## De stappen

1. Open Site settings en ga naar SEO, dan Indexing.
2. Typ de gewenste robots.txt-regels in het regelveld.
3. Stel eventueel de Content-Signal-header in hetzelfde gebied in.
4. Klik op Save en publiceer je site, en open daarna yourdomain.com/robots.txt om het live bestand te controleren.

## De regels om te gebruiken

Toestaan:

```
User-agent: OAI-SearchBot
Allow: /

User-agent: *
Allow: /
```

Blokkeren:

```
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

Content-Signal: ai-train=no, search=yes, ai-input=no
```

## Aandachtspunten

Op de pagina van Webflow staat dat je robots.txt openbaar zichtbaar is, dus vertrouw er niet op om privépagina's te verbergen, en dat niet alle bots het volgen.

## Vergelijk met Wix

[Wix](/nl/platforms/wix): Een langer bewerkingspad en een voorbeeld met vier namen.

## Controleer je eigen site

De gratis check in het vak hierboven leest robots.txt voor de AI-crawlers en stuurt per crawler één live verzoek. Zo zie je ook een regel die de instellingen van je platform toestaan maar een firewall weigert. De volledige lijst met crawlers staat op [de AI-crawlerhub](/nl/bots).

## FAQ

### Heb ik een betaald abonnement nodig voor robots.txt op Webflow?

Een helppagina van Webflow zegt dat je een Site-abonnement of een betaald Workspace-abonnement nodig hebt om een robots.txt-bestand aan je site toe te voegen.

### Wat is Content-Signal?

Een voorgestelde extensie van RFC 9309 die Webflow als header kan sturen: ai-train, search en ai-input, elk ingesteld op yes of no.

### Blokkeert Webflow slechte bots voor mij?

De helppagina laat zien hoe je een regel voor een benoemde bot schrijft. Er staat dat sommige bots, vooral kwaadaardige, robots.txt niet volgen.

## Sources

- [Webflow Help: Set robots.txt rules](https://help.webflow.com/hc/en-us/articles/41954080897683-Set-robots-txt-rules), gelezen op 21 oktober 2026
- [Webflow Help: Request to block specific bots from visiting your site](https://help.webflow.com/hc/en-us/articles/41954183592851-Request-to-block-specific-bots-from-visiting-your-site), gelezen op 21 oktober 2026
