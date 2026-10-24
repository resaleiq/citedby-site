title: Wix: blokkeer AI-crawlers in de Robots.txt Editor (vier namen)
slug: wix
description: De helppagina van Wix zegt dat je vier user agents in de Robots.txt Editor plakt. Waar de editor staat, wat het voorbeeld weglaat en de optie nosnippet.
section: platforms
locale: nl
cluster: AI-crawlers per platform
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Vier feiten over Wix: Waar Robots.txt Editor, Voorbeeldnamen 4, Paginaniveau nosnippet-tag, Support Niet voor bewerkingen
hero_sub: Instellingen voor AI-crawlers op Wix
hero_boxes: Waar|Robots.txt Editor; Voorbeeldnamen|4; Paginaniveau|nosnippet-tag; Support|Niet voor bewerkingen
widget: on
related: /nl/platforms|Alle platforms vergeleken; /nl/platforms/webflow|Webflow; /nl/bots|AI-crawlers vergeleken; /nl/guides/cms|Checklist AI-zichtbaarheid voor Shopify, WooCommerce en meer
answer: Wix laat je robots.txt bewerken: SEO & GEO in het dashboard, dan Tools and settings, dan Robots.txt Editor. De helppagina plakt vier namen om te blokkeren: CCBot, GPTBot, ChatGPT-User en BingAI. ClaudeBot, PerplexityBot en Google-Extended staan niet in dat voorbeeld, dus voeg ze zelf toe als je ze geblokkeerd wilt hebben.

## Waar de instelling staat in Wix

Ga in het dashboard van je site naar SEO & GEO, scroll naar Tools and settings, klik op Robots.txt Editor en dan op View File. De aparte bewerkgids van Wix noemt dit een geavanceerde functie en zegt dat Wix Customer Care niet kan helpen met wijzigingen die je in het bestand maakt.

## Het voorbeeld blokkeert vier namen, en een daarvan staat niet op de lijst van Bing

Op de helppagina van Wix staat dat de lijst "includes some known AI crawlers, but you can always add more". De vier die erin staan zijn CCBot, GPTBot, ChatGPT-User en BingAI. De tokens van Anthropic, Perplexity, Google en Meta die op onze andere pagina's staan, ontbreken. "BingAI" is de vreemde eend: de pagina van Microsoft over welke crawlers Bing gebruikt, dezelfde dag gelezen, noemt Bingbot, AdIdxBot, BingPreview, MicrosoftPreview en BingVideoPreview en geen BingAI. Een regel voor een naam die geen enkele crawler gebruikt doet niets, dus beschouw de lijst van Wix als startpunt en controleer hem aan de hand van de eigen pagina van elke leverancier. Let er ook op dat [ChatGPT-User](/nl/bots/chatgpt-user) de fetcher is die een pagina opent voor iemand die ChatGPT iets vraagt, dus door die te blokkeren verdwijnt die route naar je pagina's.

In de woorden van de leverancier (origineel in het Engels): “This list includes some known AI crawlers, but you can always add more as needed.”

Bron: [Wix Help Center: Blocking AI Crawlers from Your Site](https://support.wix.com/en/article/blocking-ai-crawlers-from-your-site), gelezen op 21 oktober 2026.

## De stappen

1. Ga in het dashboard van je site naar SEO & GEO.
2. Scroll naar Tools and settings en klik op Robots.txt Editor.
3. Klik op View File en klik dan op het veld onder Your robots.txt file.
4. Voeg de regels toe onder This is your current file, en klik dan op Save Changes en Save.
5. Voor één pagina alleen: open bij die pagina SEO basics, Advanced SEO, Robots meta tag, en vink nosnippet aan. Wix zegt dat dit voorkomt dat de content wordt gebruikt als directe input voor AI overviews.

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
User-agent: CCBot
Disallow: /

User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /
```

## Aandachtspunten

In de FAQ van Wix staat dat het blokkeren van AI-crawlers in robots.txt de NLWeb-functionaliteit kan beperken, omdat AI-agents toegang nodig hebben tot je gestructureerde content. Ook staat er dat sommige crawlers robots.txt negeren, dus een blokkade is niet waterdicht.

## Vergelijk met Webflow

[Webflow](/nl/platforms/webflow): Ook een robots.txt-editor, plus een Content-Signal-header.

## Controleer je eigen site

De gratis check in het vak hierboven leest robots.txt voor de AI-crawlers en stuurt per crawler één live verzoek. Zo zie je ook een regel die de instellingen van je platform toestaan maar een firewall weigert. De volledige lijst met crawlers staat op [de AI-crawlerhub](/nl/bots).

## FAQ

### Schaadt het blokkeren van AI-crawlers mijn SEO op Wix?

Wix zegt dat het blokkeren van specifieke AI-crawlers SEO niet significant zou moeten beïnvloeden, en raadt aan daarna je analytics te controleren.

### Is BingAI een echte crawler?

Hij staat niet op de huidige lijst van Bing-crawlers van Microsoft, waarop Bingbot, AdIdxBot, BingPreview, MicrosoftPreview en BingVideoPreview staan. Zie de [Bingbot-pagina](/nl/bots/bingbot).

### Blokkeert nosnippet AI-crawlers?

Wix beschrijft het als voorkomen dat je content wordt gebruikt als directe input voor AI overviews. Het is een tag op paginaniveau, geen crawlerblokkade.

## Sources

- [Wix Help Center: Blocking AI Crawlers from Your Site](https://support.wix.com/en/article/blocking-ai-crawlers-from-your-site), gelezen op 21 oktober 2026
- [Wix Help Center: Editing Your Site's Robots.txt File](https://support.wix.com/en/article/editing-your-sites-robotstxt-file), gelezen op 21 oktober 2026
- [Microsoft Bing Webmaster help: Which Crawlers Does Bing Use?](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0), gelezen op 21 oktober 2026
