title: Ghost: robots.txt in je thema, AI-crawlers toestaan of blokkeren
slug: ghost
description: Ghost heeft geen robots.txt-instelling in de admin. Volgens de helppagina sla je een robots.txt op in de root van je thema. Ghost(Pro): abonnement nodig.
section: platforms
locale: nl
cluster: AI-crawlers per platform
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over Ghost: Waar Thema-root, Bestand robots.txt, Effect Vervangt standaard, Ghost(Pro) Creator-abonnement of hoger
hero_sub: Instellingen voor AI-crawlers op Ghost
hero_boxes: Waar|Thema-root; Bestand|robots.txt; Effect|Vervangt standaard; Ghost(Pro)|Creator of hoger
widget: on
related: /nl/platforms|Alle platforms vergeleken; /nl/platforms/wordpress-com|WordPress.com; /nl/bots|AI-crawlers vergeleken; /nl/guides/cms|Checklist AI-zichtbaarheid voor Shopify, WooCommerce en meer
answer: Ghost levert een standaard robots.txt. Om die te wijzigen sla je je eigen robots.txt op in de root van je thema en installeer en activeer je daarna de nieuwe themaversie. Op de helppagina van Ghost staat dat eigen thema's op Ghost(Pro) het Creator-abonnement of hoger vereisen, dus je abonnement bepaalt of je het bestand kunt bewerken.

## Waar de instelling staat in Ghost

Er is geen robots.txt-veld in de admin. Op de helppagina van Ghost staat dat het bestand in het thema van je site staat: schrijf je robots.txt en sla hem op in de root van het thema. De themadocumentatie van Ghost zegt hetzelfde in één regel: thema's kunnen een robots.txt bevatten die de standaard-robots.txt van Ghost overschrijft.

## Het enige wat de pagina van Ghost zegt en die van andere platforms niet

Bij Ghost reist het bestand mee met het thema, dus je abonnement bepaalt of je het kunt wijzigen. Op de helppagina van Ghost staat dat je er vertrouwd mee moet zijn om zelf een robots.txt te schrijven en een nieuwe versie van je thema te installeren. Daarna volgt een beperking voor Ghost(Pro), de gehoste dienst van Ghost: een eigen thema installeren vereist het Creator-abonnement of hoger. De pagina beschrijft in deze bewoordingen wat er dan gebeurt.

In de woorden van de leverancier (origineel in het Engels): “Once the new version of the theme is installed and activated, the theme's robots.txt will be used in place of Ghost's default robots.txt.”

Bron: [Ghost Help: Modifying robots.txt](https://ghost.org/help/modifying-robots-txt/), gelezen op 24 oktober 2026.

## De stappen

1. Schrijf je robots.txt-bestand.
2. Sla het op in de root van je thema.
3. Installeer de nieuwe versie van het thema en activeer die. Ghost zegt dat de robots.txt van het thema wordt gebruikt in plaats van de standaard zodra de nieuwe versie is geïnstalleerd en geactiveerd.
4. Controleer op Ghost(Pro) eerst je abonnement: Ghost zegt dat een eigen thema installeren het Creator-abonnement of hoger vereist.

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

Het bestand van het thema wordt gebruikt in plaats van de standaard van Ghost, niet erbovenop. De pagina's van Ghost zeggen niet wat de standaard bevat, dus open yoursite.com/robots.txt voordat je hem vervangt en kopieer de regels die je wilt houden, zoals een sitemapregel. De pagina waarschuwt ook dat je er voor deze route vertrouwd mee moet zijn om het bestand zelf te schrijven, en dat AI-crawlers er niet bij naam in worden behandeld.

## Vergelijk met WordPress.com

[WordPress.com](/nl/platforms/wordpress-com): De AI-opt-out is een instelling voor delen, geen bestand dat je zelf schrijft.

## Controleer je eigen site

De gratis check in het vak hierboven leest robots.txt voor de AI-crawlers en stuurt per crawler één live verzoek. Zo zie je ook een regel die de instellingen van je platform toestaan maar een firewall weigert. De volledige lijst met crawlers staat op [de AI-crawlerhub](/nl/bots).

## FAQ

### Waar zet ik een eigen robots.txt in Ghost?

In de root van je thema. Op de helppagina van Ghost staat dat zodra de nieuwe themaversie is geïnstalleerd en geactiveerd, de robots.txt van het thema wordt gebruikt in plaats van de standaard van Ghost.

### Heb ik een betaald abonnement nodig om robots.txt te bewerken op Ghost(Pro)?

Op de pagina van Ghost staat dat een eigen thema installeren op Ghost(Pro) het Creator-abonnement of hoger vereist. Omdat het bestand deel van het thema is, geldt dat ook voor een eigen robots.txt.

## Sources

- [Ghost Help: Modifying robots.txt](https://ghost.org/help/modifying-robots-txt/), gelezen op 24 oktober 2026
- [Ghost Docs: Theme structure](https://docs.ghost.org/themes/structure), gelezen op 24 oktober 2026
