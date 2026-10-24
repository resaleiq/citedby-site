title: Squarespace: AI-crawlervakje blokkeert 26 bots, maar ChatGPT niet
slug: squarespace
description: Het paneel Crawlers van Squarespace heeft één vakje dat bekende AI-crawlers blokkeert. De 26 namen in robots.txt missen de zoek- en gebruikersbots van ChatGPT.
section: platforms
locale: nl
cluster: AI-crawlers per platform
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Vier feiten over Squarespace: Waar Settings, Crawlers, Geblokkeerde namen 26, robots.txt bewerken Nee, Eerdere training Niet verwijderd
hero_sub: Instellingen voor AI-crawlers op Squarespace
hero_boxes: Waar|Settings, Crawlers; Geblokkeerde namen|26; robots.txt bewerken|Nee; Eerdere training|Niet verwijderd
widget: on
related: /nl/platforms|Alle platforms vergeleken; /nl/platforms/wix|Wix; /nl/bots|AI-crawlers vergeleken; /nl/guides/cms|Checklist AI-zichtbaarheid voor Shopify, WooCommerce en meer
answer: Squarespace heeft één selectievakje: Settings, dan Crawlers, dan Block known artificial intelligence crawlers. Dat zet 26 benoemde bots in je robots.txt. De lijst bevat GPTBot, ClaudeBot en DuckAssistBot, maar niet OAI-SearchBot, ChatGPT-User of PerplexityBot, en je kunt robots.txt zelf niet bewerken.

## Waar de instelling staat in Squarespace

Open het paneel Settings, klik op Crawlers en vink Block known artificial intelligence crawlers aan. Op de pagina van Squarespace staat dat het aanvinken van het vakje je robots.txt-bestand bijwerkt voor de hieronder genoemde bots, en dat er na verloop van tijd meer bij kunnen komen.

## De 26 namen, en welke ontbreken

De helppagina van Squarespace noemt precies 26 namen: AI2Bot, Ai2Bot-Dolma, aiHitBot, Amazonbot, anthropic-ai, Applebot-Extended, Bytespider, CCBot, ClaudeBot, cohere-ai, cohere-training-data-crawler, DuckAssistBot, FacebookBot, Google-Extended, GoogleOther, GoogleOther-Image, GoogleOther-Video, GPTBot, img2dataset, Meta-ExternalAgent, MyCentralAIScraperBot, omgili, omgilibot, Quora-Bot, TikTokSpider en YouBot. Naast onze eigen crawlerpagina's gelegd dekt het vakje de training- en datasetcrawlers van OpenAI, Anthropic, Google, Apple, Meta en Common Crawl. Het noemt [OAI-SearchBot](/nl/bots/oai-searchbot), [ChatGPT-User](/nl/bots/chatgpt-user), [PerplexityBot](/nl/bots/perplexitybot), [Claude-SearchBot](/nl/bots/claude-searchbot) en [Claude-User](/nl/bots/claude-user) niet, dus aanvinken haalt je niet uit ChatGPT-zoeken. Het noemt wel [DuckAssistBot](/nl/bots/duckassistbot) en [Amazonbot](/nl/bots/amazonbot), crawlers voor AI-antwoorden en producten, dus aanvinken kan je ook de AI-antwoorden van DuckDuckGo kosten.

In de woorden van de leverancier (origineel in het Engels): “Checking the box updates your robots.txt file to tell the following bots not to crawl your site.”

Bron: [Squarespace Help: Request that AI models exclude your site](https://support.squarespace.com/hc/en-us/articles/360022347072-Request-that-AI-models-exclude-your-site), gelezen op 21 oktober 2026.

## De stappen

1. Open het paneel Settings van je Squarespace-site.
2. Klik op Crawlers.
3. Vink Block known artificial intelligence crawlers aan om de 26 namen te blokkeren, of laat het uitgevinkt om ze allemaal toe te staan.
4. Wil je dat er een andere bot wordt toegevoegd, neem dan contact op met Squarespace: de tekst op de pagina zelf zegt dat je dat kunt aanvragen.

## De regels om te gebruiken

Toestaan:

```
# Squarespace sites are open to these crawlers while the box is unticked.
# You cannot add lines yourself, so there is nothing to paste.
```

Blokkeren:

```
# Written by Squarespace when the box is ticked (excerpt):
User-agent: GPTBot
User-agent: ClaudeBot
User-agent: CCBot
Disallow: /
```

## Aandachtspunten

Squarespace stelt dat het aanvinken van het vakje inhoud die al van je site is gescrapet niet met terugwerkende kracht uit de trainingsdata van AI-modellen verwijdert. Het zegt ook dat robots.txt slechts een verzoek is dat vriendelijke crawlers hebben aangeboden te volgen. Het fragment hierboven is onze ingekorte illustratie van het soort regels dat het vakje oplevert; het exacte bestand is wat je site op /robots.txt levert, dus open het en lees het.

## Vergelijk met Wix

[Wix](/nl/platforms/wix): Een echte robots.txt-editor, en een voorbeeldlijst van vier namen.

## Controleer je eigen site

De gratis check in het vak hierboven leest robots.txt voor de AI-crawlers en stuurt per crawler één live verzoek. Zo zie je ook een regel die de instellingen van je platform toestaan maar een firewall weigert. De volledige lijst met crawlers staat op [de AI-crawlerhub](/nl/bots).

## FAQ

### Kan ik ChatGPT-zoeken toestaan maar training blokkeren op Squarespace?

Gedeeltelijk. Het aanvinken van het vakje schrijft een regel voor GPTBot, en OAI-SearchBot staat niet bij de 26 namen. Je kunt geen eigen regels toevoegen, dus open je live /robots.txt om te controleren wat erin staat.

### Kan ik robots.txt bewerken op Squarespace?

De eigen pagina van Squarespace behandelt het paneel Crawlers als de plek waar je dit regelt en biedt geen robots.txt-editor. Wix en Webflow wel.

### Stopt het vakje dat Google mijn site indexeert?

Nee. Het staat los van de optie voor crawlers van zoekmachines in hetzelfde paneel. Het AI-vakje noemt Google-Extended en GoogleOther, niet Googlebot.

## Sources

- [Squarespace Help: Request that AI models exclude your site](https://support.squarespace.com/hc/en-us/articles/360022347072-Request-that-AI-models-exclude-your-site), gelezen op 21 oktober 2026
