title: Adobe Commerce: robots.txt onder Content, Design, Configuration
slug: adobe-commerce
description: Adobe Commerce bewerkt robots.txt in de Admin onder Search Engine Robots. Cloud-projecten hebben extra pub/media-stappen en Adobe noemt geen AI-crawler.
section: platforms
locale: nl
cluster: AI-crawlers per platform
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over Adobe Commerce: Waar Content, Design, Configuration, Sectie Search Engine Robots, Cloud Extra stappen, AI-namen Niet vermeld
hero_sub: Instellingen voor AI-crawlers op Adobe Commerce
hero_boxes: Waar|Content > Design > Configuration; Sectie|Search Engine Robots; Cloud|Extra stappen; AI-namen|Niet vermeld
widget: on
related: /nl/platforms|Alle platforms vergeleken; /nl/platforms/shopify|Shopify; /nl/bots|AI-crawlers vergeleken; /nl/guides/cms|Checklist AI-zichtbaarheid voor Shopify, WooCommerce en meer
answer: In Adobe Commerce pas je robots.txt aan in de Admin: Content, Design, Configuration, de rij Global, dan Search Engine Robots en het vak voor eigen instructies. Adobe's pagina's hebben het over webcrawlers en bots in het algemeen en noemen geen AI-crawler, dus AI-user-agents voeg je zelf toe. Cloud-projecten hebben extra stappen met bestandspaden.

## Waar de instelling staat in Adobe Commerce

Ga in de zijbalk van de Admin naar Content, dan Design, dan Configuration. Volgens het SEO-overzicht van Adobe zoek je de Global-configuratie in de eerste rij van het raster, klik je op Edit en klap je de sectie Search Engine Robots open. Daar staat het vak Edit Custom instruction of robots.txt file, met een knop Reset to Default.

## Het enige wat de pagina's van Adobe Commerce zeggen en die van andere platforms niet

Bij Adobe Commerce op cloudinfrastructuur heeft het robots.txt-bestand een locatieprobleem dat andere platforms niet hebben. De Implementation Playbook van Adobe zegt dat je de inhoud in de Admin toevoegt, maar het bestandssysteem is alleen-lezen. Het bestand moet daarom onder pub/media staan en een eigen Fastly VCL-snippet stuurt /robots.txt daarnaartoe door. Voor meerdere sites in één project noemt de playbook de bestanden per site, bijvoorbeeld domainone_robots.txt. Voor on-premises installaties zegt hij dat je de bestanden schrijft naar /path/to/commerce/pub/media/ of /path/to/commerce/media, wat voor jouw installatie klopt.

In de woorden van de leverancier (origineel in het Engels): “Due to the read-only file system on Adobe Commerce on cloud infrastructure projects, you must specify the pub/media path before generating the file.”

Bron: [Adobe Commerce Implementation Playbook: Best practices for configuring web crawlers](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/launch/robots-txt), gelezen op 24 oktober 2026.

## De stappen

1. Ga in de zijbalk van de Admin naar Content, dan Design, dan Configuration.
2. Zoek de Global-configuratie in de eerste rij van het raster en klik op Edit.
3. Scroll omlaag en klap Search Engine Robots open.
4. Zet Default Robots op INDEX, FOLLOW, NOINDEX, FOLLOW, INDEX, NOFOLLOW of NOINDEX, NOFOLLOW. Adobe beschrijft dit als instructies aan crawlers over indexeren en het volgen van links.
5. Voer indien nodig je eigen regels in het vak Edit Custom instruction of robots.txt file in. Reset to Default herstelt de instructies van Adobe.
6. Klik op Save Configuration en open daarna de /robots.txt van je winkel om het resultaat te zien. Volgens een tip in de playbook van Adobe kun je het automatisch gegenereerde bestand daar bekijken.

## De regels om te gebruiken

De eigen voorbeelden van Adobe gebruiken User-agent: * voor alle crawlers. Wil je één crawler met naam toestaan of blokkeren, voeg dan een groep met zijn naam toe:

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

Adobe's pagina's zeggen niet of tekst die je zelf typt wordt toegevoegd aan de standaardinstructies of ze vervangt. Sla op en lees daarna /robots.txt om te controleren wat er wordt geleverd.

## Aandachtspunten

De playbook van Adobe zegt dat je je Admin-pad niet in robots.txt zet, omdat dat een kwetsbaarheid is voor het hacken van de site en mogelijk gegevensverlies, en dat je het moet verwijderen. De standaardinstructies van Adobe beginnen met User-agent: * en een lijst Disallow-regels zoals /checkout/ en /catalog/, dus controleer wat je laat staan. Over cloud zegt een knowledge base-artikel van 18 augustus 2026 dat de inhoud van robots.txt wordt gegenereerd vanuit de configuratie in de Admin en in de database wordt opgeslagen, zonder dat in dat scenario een fysiek bestand nodig is, terwijl de playbook de doorverwijzing naar pub/media beschrijft. De twee pagina's lezen verschillend, dus vraag Adobe Commerce Support welke voor jouw project geldt. De playbook zegt ook dat het advies alleen geldt voor de native Adobe Commerce-storefront, niet voor headless storefronts of storefronts op Adobe Experience Manager.

## Vergelijk met Shopify

[Shopify](/nl/platforms/shopify): Een themasjabloon in plaats van een vak in de Admin, en Support lost bewerkingen daarvan niet op.

## Controleer je eigen site

De gratis check in het vak hierboven leest robots.txt voor de AI-crawlers en stuurt per crawler één live verzoek. Zo zie je ook een regel die de instellingen van je platform toestaan maar een firewall weigert. De volledige lijst met crawlers staat op [de AI-crawlerhub](/nl/bots).

## FAQ

### Waarom verandert mijn eigen robots.txt niet op Adobe Commerce cloud?

Volgens de knowledge base van Adobe is de gewone oorzaak dat indexering door zoekmachines is uitgeschakeld, waardoor eigen robots.txt-inhoud niet wordt toegepast. Los het op in de Cloud Console of met de instelling restrict_robots van de magento-cloud CLI. Het artikel voegt toe dat Staging-omgevingen standaard indexering uit hebben en dat die daar niet kan worden ingeschakeld.

### Noemt Adobe Commerce AI-crawlers voor robots.txt?

Niet in de pagina's die we hebben gelezen. Die hebben het over webcrawlers en bots, en hun voorbeelden gebruiken alleen User-agent: *. Voeg elke AI-user-agent die je wilt toestaan of blokkeren als eigen groep toe.

## Sources

- [Adobe Commerce Implementation Playbook: Best practices for configuring web crawlers](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/launch/robots-txt), gelezen op 24 oktober 2026
- [Adobe Commerce Admin guide: SEO overview](https://experienceleague.adobe.com/en/docs/commerce-admin/marketing/seo/seo-overview), gelezen op 24 oktober 2026
- [Adobe Commerce knowledge base: Resolve robots.txt not updating or displaying default settings](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/robots-txt-not-updated-or-displaying-default-settings), gelezen op 24 oktober 2026
