title: WordPress.com: AI-opt-out via privacyinstelling, geen robots.txt
slug: wordpress-com
description: WordPress.com ziet AI-opt-out als 'Prevent third-party sharing' in de privacyinstellingen. Wat de zichtbaarheidsgids zegt, beoordeeld op 5 oktober 2026.
section: platforms
locale: nl
cluster: AI-crawlers per platform
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Vier feiten over WordPress.com: Waar Privacyinstellingen, Niet Een robots.txt-bewerking, Gids beoordeeld 5 okt. 2026, Ook MCP-agenttoegang
hero_sub: Instellingen voor AI-crawlers op WordPress.com
hero_boxes: Waar|Privacyinstellingen; Niet|Een robots.txt-bewerking; Gids beoordeeld|5 okt. 2026; Ook|MCP-agenttoegang
widget: on
related: /nl/platforms|Alle platforms vergeleken; /nl/platforms/cloudflare|Cloudflare; /nl/bots|AI-crawlers vergeleken; /nl/guides/cms|Checklist AI-zichtbaarheid voor Shopify, WooCommerce en meer
answer: Bij WordPress.com is de AI-opt-out een privacyinstelling en geen robots.txt-bewerking. In de zichtbaarheidsgids, voor het laatst beoordeeld op 5 oktober 2026, staat dat je voor een opt-out van het delen van je openbare content met derden, waaronder AI-modellen, de gids Prevent third-party sharing volgt.

## Waar de instelling staat in WordPress.com

De zichtbaarheidsgids van WordPress.com verwijst je naar Settings, dan Reading, voor Site Visibility (Public, Coming Soon of Private), en naar een aparte gids Prevent third-party sharing voor de AI-opt-out.

## Een AI-opt-out is hier een instelling voor delen

De gids van WordPress.com over het beheren van de zichtbaarheid van je site zegt: om je af te melden voor het delen van de openbare content van je site met derden (waaronder AI-modellen), bezoek je de gids Prevent third-party sharing. Dat is een platforminstelling, los van de robots.txt die zoek- en AI-crawlers lezen. Dezelfde pagina, voor het laatst beoordeeld op 5 oktober 2026, beschrijft ook de andere richting: je kunt externe AI-agents zoals ChatGPT of Claude verbinden om de zichtbaarheidsinstellingen van je site te lezen en te bewerken door MCP tool access in te schakelen. De inhoud van de gids Prevent third-party sharing konden we op 21 oktober niet lezen: de pagina laadde met zijn titel en een beoordelingsdatum van 1 augustus 2024, maar zonder stappen, zowel met een gewone fetch als in een browser. Deze pagina beschrijft dus niet hoe die instelling werkt; open de gids vanuit je eigen dashboard. Draai je zelfgehost WordPress in plaats van WordPress.com, dan kun je het bestand zelf bewerken, zoals bij elke host.

In de woorden van de leverancier (origineel in het Engels): “To opt out of sharing your site's public content with third parties (including AI models), visit the Prevent third-party sharing guide.”

Bron: [WordPress.com Support: Control your site's visibility](https://wordpress.com/support/privacy-settings/), gelezen op 21 oktober 2026.

## De stappen

1. Open Settings, dan Reading, en controleer of Site Visibility op Public staat als je wilt dat crawlers de site überhaupt zien.
2. Open de gids Prevent third-party sharing van WordPress.com via de help bij de privacyinstellingen en volg die als je je wilt afmelden voor het delen van content met derden, waaronder AI-modellen.
3. Open yourdomain.com/robots.txt en lees wat je site daadwerkelijk aan crawlers levert.

## De regels om te gebruiken

Toestaan:

```
# No edit to make on WordPress.com for the sharing opt-out.
# Check what your site serves:
# https://yourdomain.com/robots.txt
```

Blokkeren:

```
# On a self-hosted WordPress site, you add lines like these through your SEO plugin or the file:
User-agent: GPTBot
Disallow: /
```

## Aandachtspunten

Een site met Coming Soon of Private is niet hetzelfde als een AI-opt-out: hij verbergt de site voor iedereen, zoekmachines inbegrepen, en dat is het tegenovergestelde van wat een winkel nodig heeft die geciteerd wil worden.

## Vergelijk met Cloudflare

[Cloudflare](/nl/platforms/cloudflare): Een schakelaar op netwerkniveau die werkt op elk siteplatform.

## Controleer je eigen site

De gratis check in het vak hierboven leest robots.txt voor de AI-crawlers en stuurt per crawler één live verzoek. Zo zie je ook een regel die de instellingen van je platform toestaan maar een firewall weigert. De volledige lijst met crawlers staat op [de AI-crawlerhub](/nl/bots).

## FAQ

### Is de AI-opt-out van WordPress.com hetzelfde als GPTBot blokkeren?

WordPress.com beschrijft het als je afmelden voor het delen van je openbare content met derden, waaronder AI-modellen. Het beschrijft het niet als een robots.txt-regel, dus controleer je live robots.txt om te zien wat crawlers wordt verteld.

### Kan ik robots.txt bewerken op WordPress.com?

We vonden geen robots.txt-editor in de zichtbaarheidsgids die we hebben gelezen, dus we zeggen er niets over, noch ja noch nee. Kijk in de instellingen van je site wat er bij jouw abonnement beschikbaar is.

### Wat is MCP tool access?

De gids zegt dat externe AI-agents daarmee de zichtbaarheidsinstellingen van je site kunnen lezen en bewerken. Het gaat om het beheren van de site, niet om crawlers.

## Sources

- [WordPress.com Support: Control your site's visibility](https://wordpress.com/support/privacy-settings/), gelezen op 21 oktober 2026
- [WordPress.com Support: Prevent third-party sharing](https://wordpress.com/support/privacy-settings/prevent-third-party-sharing/), gelezen op 21 oktober 2026
