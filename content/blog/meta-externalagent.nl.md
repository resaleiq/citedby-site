title: Meta-ExternalAgent: wat het doet en wat blokkeren verandert
h1: Meta-ExternalAgent: wat het doet en wat blokkeren verandert
description: Meta-ExternalAgent (Meta): meerdere taken. robots.txt-token, wat een Disallow verandert en hoe je een verzoek controleert.
slug: meta-externalagent
section: bots
locale: nl
cluster: AI-crawlers
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Vier feiten over Meta-ExternalAgent: aanbieder Meta, taak Meerdere taken, volgt robots.txt Ja, adreslijst Geen
hero_sub: Meta-ExternalAgent, beheerd door Meta
hero_boxes: Aanbieder|Meta; Taak|Meerdere taken; Volgt robots.txt|Ja; Adreslijst|Geen
widget: on
related: /nl/bots|Alle AI-crawlers vergeleken; /nl/bots/gptbot|GPTBot; /nl/platforms|AI-crawlerinstellingen per platform; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen? Wat daarover beslist
answer: Meta-ExternalAgent is de crawler van Meta voor toepassingen zoals het trainen van AI-foundation-modellen of het verbeteren van producten door content rechtstreeks te indexeren. Op de pagina van Meta, bijgewerkt op 21 mei 2026, staan vijf agents. Meta zegt dat Meta-ExternalFetcher en FacebookExternalHit robots.txt kunnen omzeilen en dat wijzigingen tot 24 uur kunnen duren.

## Wat Meta-ExternalAgent is

Op de pagina van Meta staan vijf crawlers. FacebookExternalHit haalt een pagina op als iemand een link deelt op Facebook, Instagram of Messenger, om titel, beschrijving en thumbnail te cachen. Meta-WebIndexer verbetert de zoekresultaten van Meta AI. Meta zegt dat het toestaan ervan Meta helpt je content te citeren en ernaar te linken in de antwoorden van Meta AI. Meta-ExternalAds crawlt voor advertentie- en zakelijke producten. Meta-ExternalAgent is die voor het trainen van AI-foundation-modellen of indexeren. Meta-ExternalFetcher haalt losse links op verzoek van een gebruiker op, ook om AI te helpen websites te doorlopen en taken voor gebruikers af te ronden.

| Gegeven | Meta-ExternalAgent |
| --- | --- |
| Aanbieder | Meta |
| Taak | AI-modeltraining en contentindexering |
| robots.txt-token | `meta-externalagent` |
| Volgt robots.txt | Ja |
| IP-adressen | Niet gepubliceerd |
| Pagina van de aanbieder gelezen op | 21 oktober 2026 |

## Wat de aanbieder zegt

De woorden van de aanbieder (Engels origineel): “The Meta-ExternalAgent crawler crawls the web for use cases such as training foundation AI models or improving products by indexing content directly.”

Bron: [Meta for Developers: Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers), gelezen op 21 oktober 2026.

## Wat gebeurt er als je Meta-ExternalAgent blokkeert

Als je meta-externalagent met Disallow uitsluit, geldt dat alleen voor die agent. In de voorbeelden van Meta heeft elk token een eigen groep, en de andere vier hebben er ook een. Het duurste om per ongeluk te blokkeren is FacebookExternalHit, want die bouwt het linkvoorbeeld als iemand je pagina deelt. Twee van de vijf negeren je robots.txt mogelijk: Meta zegt dat Meta-ExternalFetcher robots.txt kan omzeilen omdat hij ophaalacties uitvoert die de gebruiker vraagt, en dat FacebookExternalHit het kan omzeilen voor veiligheids- of integriteitscontroles, zoals malwarecontroles.

## De robots.txt-regels

Om Meta-ExternalAgent toe te staan:

```
User-agent: meta-externalagent
Allow: /
```

Om Meta-ExternalAgent te blokkeren:

```
User-agent: meta-externalagent
Disallow: /
```

Plak een blok in de robots.txt in de root van je host, bijvoorbeeld https://example.com/robots.txt. Een groep voor één token geldt niet voor de andere crawlers van dezelfde aanbieder.

De user-agent-string volgens de aanbieder:

```
meta-externalagent/1.1
```

## Hoe je een echt verzoek van een nep-verzoek onderscheidt

De pagina van Meta geeft de user-agent-strings (meta-externalagent/1.1 en de versie met een link) en publiceert in de tekst die we lazen geen IP-lijst, dus we noemen geen aantal. Voor FacebookExternalHit zegt Meta dat je óf de user-agent-strings óf de IP-adressen op de allowlist moet zetten, en noemt de adressen de veiligere optie. Meta zegt dat crawlers robots.txt tot 24 uur kunnen cachen. Wacht dus zo lang voordat je een wijziging beoordeelt. Vragen gaan naar webmasters@meta.com.

## Vergelijk met GPTBot

[GPTBot](/nl/bots/gptbot): De trainingscrawler van OpenAI, die robots.txt respecteert zonder de omzeilgevallen van Meta.

## Je eigen site

De gratis check in het kader hierboven test acht crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot en Googlebot). Meta-ExternalAgent is er niet bij: kijk in je robots.txt of er een groep `meta-externalagent` staat en zoek de user agent in je serverlog. De volledige lijst met crawlers staat in [de gids met AI-crawlers](/nl/bots).

## FAQ

### Volgt Meta-ExternalAgent robots.txt?

Ja. Geef meta-externalagent in robots.txt een eigen User-agent-groep: de andere crawlers van dezelfde aanbieder hebben elk hun eigen instelling.

### Hoe weet ik dat Meta-ExternalAgent echt geblokkeerd is?

robots.txt is maar één laag: ook een CDN- of firewallregel kan een crawler weigeren, en een crawler kan het bestand negeren. Zoek de user agent in je serverlog en test het adres van buiten je netwerk.

## Sources

- [Meta for Developers: Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers)
