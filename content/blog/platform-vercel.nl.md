title: Vercel: de AI Bots-regelset in de Firewall (Log of Deny)
slug: vercel
description: Vercel blokkeert AI-bots met een Firewall-regelset, niet met een robots.txt-regel. Waar de AI Bots Ruleset staat, de acties Log en Deny en de botlijst.
section: platforms
locale: nl
cluster: AI-crawlers per platform
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier feiten over Vercel: Waar Firewall, Rules, Abonnementen Alle abonnementen, Standaard Allow (inactief), Acties Log of Deny
hero_sub: Instellingen voor AI-crawlers op Vercel
hero_boxes: Waar|Firewall, Rules; Abonnementen|Alle abonnementen; Standaard|Allow (inactief); Acties|Log of Deny
widget: on
related: /nl/platforms|Alle platforms vergeleken; /nl/platforms/cloudflare|Cloudflare; /nl/bots|AI-crawlers vergeleken; /nl/guides/cms|Checklist AI-zichtbaarheid voor Shopify, WooCommerce en meer
answer: Vercel behandelt AI-bots met een Firewall-regelset, niet met een robots.txt-regel. Open in je project Firewall, dan Rules, en zet de AI Bots Ruleset op Log of Deny. Hij is beschikbaar op alle abonnementen en begint inactief, weergegeven als Allow, dus er wordt niets geblokkeerd tot je dat verandert.

## Waar de instelling staat in Vercel

Open in het dashboard van je project Firewall in de zijbalk en dan Rules. In de sectie Bot Management vind je de regel AI Bots Ruleset. In de docs van Vercel staat dat de regelset op alle abonnementen beschikbaar is.

## Het enige wat de pagina van Vercel zegt en die van andere platforms niet

De lijst met AI-bots van Vercel hoef je niet zelf bij te houden. De regelset dekt AI-bots die crawlen voor trainingsdata, voor zoekdoeleinden of voor door gebruikers gestarte fetches, en Vercel houdt de lijst actueel. Dezelfde pagina zegt dat de regelset standaard inactief is en in het dashboard als Allow staat, dus overeenkomend verkeer wordt niet beoordeeld en bereikt je applicatie. Je bedient het met één actie voor de hele regelset, Log of Deny, toegepast op de Firewall.

In de woorden van de leverancier (origineel in het Engels): “When new AI bots emerge, Vercel automatically adds them to its managed list and handles them according to your existing configured action without requiring any changes on your part.”

Bron: [Vercel Docs: Bot Management](https://vercel.com/docs/bot-management), gelezen op 24 oktober 2026.

## De stappen

1. Open in het dashboard van je project Firewall in de zijbalk.
2. Open Rules in de zijbalk.
3. Selecteer in de sectie Bot Management Log of Deny bij de regel AI Bots Ruleset. Log legt AI-botverkeer vast zonder het te blokkeren en is nuttig om te monitoren. Deny blokkeert al het verkeer dat als afkomstig van AI-bots is geïdentificeerd.
4. Als je een wijziging maakt, verschijnt een knop Review Changes met het aantal wijzigingen. Selecteer Review Changes, controleer ze en selecteer dan Publish om de wijzigingen toe te passen op je productie-deployment.

## De regels om te gebruiken

De pagina's van Vercel beschrijven dit als een Firewall-instelling, dus er is geen robots.txt-regel om toe te voegen. De twee toestanden zijn:

Toestaan:

```
AI Bots Ruleset: Allow (the default, ruleset inactive)
```

Blokkeren:

```
AI Bots Ruleset: Deny
```

## Aandachtspunten

Deny blokkeert al het verkeer dat als afkomstig van AI-bots is geïdentificeerd, en de regelset omvat training, zoeken en door gebruikers gestarte fetches samen, dus het is geen manier om trainingsbots te blokkeren en zoekbots te behouden. Log is de veiligere eerste stap. De pagina van Vercel zegt niet hoe de regelset zich verhoudt tot je robots.txt, dus controleer apart wat je eigen bestand zegt. Voor afzonderlijke bots zegt dezelfde pagina dat je sommige of alle bots uit de directory met geverifieerde bots kunt blokkeren met WAF custom rules die de matchvoorwaarde User Agent of de header Signature-Agent gebruiken.

## Vergelijk met Cloudflare

[Cloudflare](/nl/platforms/cloudflare): Ook een schakelaar op netwerkniveau, met drie acties voor elk van Search, Agent en Training.

## Controleer je eigen site

De gratis check in het vak hierboven leest robots.txt voor de AI-crawlers en stuurt per crawler één live verzoek. Zo zie je ook een regel die de instellingen van je platform toestaan maar een firewall weigert. De volledige lijst met crawlers staat op [de AI-crawlerhub](/nl/bots).

## FAQ

### Blokkeert Vercel standaard AI-bots?

Nee. In de docs van Vercel staat dat de AI Bots Ruleset standaard inactief is, in het dashboard als Allow weergegeven, en dat overeenkomend verkeer niet wordt beoordeeld en je applicatie bereikt.

### Moet ik de AI-botlijst van Vercel zelf bijhouden?

Nee. Vercel zegt dat de lijst met bekende AI-bots automatisch door Vercel wordt onderhouden en bijgewerkt, en dat nieuwe bots worden behandeld volgens de actie die je al hebt ingesteld.

## Sources

- [Vercel Docs: Bot Management](https://vercel.com/docs/bot-management), gelezen op 24 oktober 2026
- [Vercel Docs: WAF Managed Rulesets](https://vercel.com/docs/vercel-firewall/vercel-waf/managed-rulesets), gelezen op 24 oktober 2026
