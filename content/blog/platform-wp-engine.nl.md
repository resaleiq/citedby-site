title: WP Engine: robots.txt, standaard crawl-delay van 10 s, Web Rules
slug: wp-engine
description: Volgens WP Engine gaat een fysiek robots.txt boven pluginbestanden en geldt standaard een crawl-delay van 10 seconden. Web Rules weigert bots op user agent.
section: platforms
locale: nl
cluster: AI-crawlers per platform
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over WP Engine: Waar SFTP, Yoast of Web Rules, Standaard crawl-delay 10 seconden, wpengine.com-adres Disallow all, Blokkeren op agent Web Rules Engine
hero_sub: Instellingen voor AI-crawlers op WP Engine
hero_boxes: Waar|SFTP, Yoast of Web Rules; Crawl-delay|Standaard 10 seconden; wpengine.com|Disallow all; Blokkeren op agent|Web Rules Engine
widget: on
related: /nl/platforms|Alle platforms vergeleken; /nl/platforms/wordpress-com|WordPress.com; /nl/bots|AI-crawlers vergeleken; /nl/guides/cms|Checklist AI-zichtbaarheid voor Shopify, WooCommerce en meer
answer: Volgens de robots.txt-pagina van WP Engine overschrijft een fysiek robots.txt in de root van je site elk bestand dat een plugin of thema genereert. Het standaardbestand stelt een crawl-delay van 10 seconden in, en sites op een wpengine.com-adres krijgen een disallow-all-bestand. Voor het weigeren van een bot op user agent verwijst WP Engine naar de Web Rules Engine.

## Waar de instelling staat in WP Engine

De pagina van WP Engine geeft twee manieren om het bestand te maken. Met de plugin Yoast SEO geïnstalleerd ga je naar SEO, dan Tools, kies je de bestandseditor en selecteer je Create robots.txt file. Of je maakt zelf een robots.txt-bestand en uploadt het met SFTP of de SSH Gateway naar de rootmap van je site. Voor blokkeren op user agent verwijst de pagina je naar access rules in de Web Rules Engine in de User Portal.

## Het enige wat de pagina van WP Engine zegt en die van andere platforms niet

WP Engine levert een standaard robots.txt, en de pagina zegt wat erin staat. In de opmerking staat dat de standaard crawl-delay voor alle sites 10 seconden is, en dat elke omgeving op een wpengine.com-adres een bestand krijgt dat alles weigert, om te voorkomen dat een site vóór de lancering op het verkeerde domein wordt geïndexeerd. Alleen omgevingen met een eigen domein zien wijzigingen in robots.txt. Een fysiek bestand dat je uploadt gaat ook voor op een bestand dat door een plugin of thema is gemaakt.

In de woorden van de leverancier (origineel in het Engels): “This is what’s in the server’s default robots.txt file and can be overridden when you add a custom robots.txt file with one of the methods outlined in this article.”

Bron: [WP Engine Support: Robots.txt and WordPress](https://wpengine.com/support/read-use-robots-txt/), gelezen op 24 oktober 2026.

## De stappen

1. Maak een bestand met de naam robots.txt. De naam moet in kleine letters zijn en de extensie .txt, niet .html.
2. Voeg je regels toe en sla op. Voor de pluginroute gebruik je in plaats daarvan Yoast SEO, Tools, dan Create robots.txt file.
3. Upload het bestand met SFTP of de SSH Gateway naar de rootmap van je site.
4. Open /robots.txt op je live eigen domein om het te controleren. Een kopie op een wpengine.com-adres toont je wijzigingen niet.
5. Om een bot op de server te weigeren open je de pagina Sites in de User Portal, selecteer je de omgeving, klik je in het secundaire linkermenu op Web Rules (misschien moet je Advanced uitklappen), kies je Access rules en klik je op Add Rule.
6. Stel Action in op Deny, IP op All, en voeg een voorwaarde toe met Type Header, Name User-Agent, Operator Regex matches (~) en de naam van de user agent als Value. Klik op Add Rule om op te slaan.

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

De pagina van WP Engine zegt dat waarden van directives hoofdlettergevoelig zijn en dat globbing en reguliere expressies in robots.txt niet volledig worden ondersteund.

## Aandachtspunten

De pagina noemt geen AI-crawlers: de voorbeelden gebruiken BadBotName, Googlebot, bingbot en SEMrush. Ook staat er dat robots robots.txt niet hoeven te volgen, en de pagina raadt een firewall zoals Sucuri WAF of Cloudflare aan, of contact met Support, om kwaadwillenden te stoppen voordat ze de site bereiken. Een verzoek dat door een access rule van Web Rules wordt geweigerd, krijgt volgens de pagina over de Web Rules Engine een antwoord 403 Forbidden en telt niet mee voor factureerbare bezoeken. Je eigen robots.txt overschrijft het standaardbestand, inclusief de regel met de crawl-delay van 10 seconden, dus voeg zelf een regel Crawl-delay toe als je er een wilt houden.

## Vergelijk met WordPress.com

[WordPress.com](/nl/platforms/wordpress-com): Een AI-opt-out in de privacyinstellingen in plaats van een robots.txt-bestand dat je zelf schrijft.

## Controleer je eigen site

De gratis check in het vak hierboven leest robots.txt voor de AI-crawlers en stuurt per crawler één live verzoek. Zo zie je ook een regel die de instellingen van je platform toestaan maar een firewall weigert. De volledige lijst met crawlers staat op [de AI-crawlerhub](/nl/bots).

## FAQ

### Waarom negeert mijn staging-site op WP Engine mijn robots.txt?

WP Engine zegt dat sites op een adres environment.wpengine.com automatisch een disallow-all-robots.txt krijgen en dat alleen omgevingen met een eigen domein wijzigingen in het bestand zien. Gedeelde accounts kunnen alleen aan Production een eigen domein toevoegen, dus Staging en Development tonen je bewerkingen meestal niet.

### Overschrijft een robots.txt-plugin een bestand dat ik naar WP Engine upload?

Nee, het is andersom. WP Engine zegt dat een fysiek robots.txt in de root van je site elk dynamisch gegenereerd bestand overschrijft dat door een plugin of thema is gemaakt.

## Sources

- [WP Engine Support: Robots.txt and WordPress](https://wpengine.com/support/read-use-robots-txt/), gelezen op 24 oktober 2026
- [WP Engine Support: Web Rules Engine](https://wpengine.com/support/web-rules-engine/), gelezen op 24 oktober 2026
