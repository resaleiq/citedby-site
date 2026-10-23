title: ChatGPT toont mijn oude prijs: zoek de bron en herstel het
h1: ChatGPT toont mijn oude prijs. Zo vind je waar het die las en herstelt je het
description: ChatGPT noemt een prijs die je maanden geleden aanpaste. De drie plekken waar die vandaan kan komen (je pagina, je feed, andere sites) en hoe je het naloopt.
slug: chatgpt-wrong-price
locale: nl
cluster: Foute feiten
date: 2026-10-20
reviewed: 2026-10-20
answer: ChatGPT toont een oude prijs als die prijs uit een verouderde bron komt: je eigen pagina, een productfeed of een andere website. Zoek de oude prijs op elke plek, herstel de bron en vraag het daarna twee keer opnieuw in een nieuwe chat. Werk je feed bij zodra een actie begint of eindigt.
widget: on
howto: on
related: /nl/blog/check-what-ai-says-about-your-brand|Wat zegt ChatGPT over je merk? 20 prompts; /nl/blog/can-chatgpt-read-my-website|Kan ChatGPT mijn website lezen?; /nl/ai-visibility-audit|AI-zichtbaarheidsaudit
hero: auto
hero_alt: Titelkaart: ChatGPT toont mijn oude prijs, met drie vakken: je eigen pagina, je productfeed, andere websites
hero_sub: Herstel de bron, niet de chat
hero_boxes: Je eigen pagina|tekst en JSON-LD; Je productfeed|prijs en actieprijs; Andere websites|vergelijkers en reviews
steps_img: on

## Waarom noemt een assistent een prijs die je al hebt aangepast?

Een assistent antwoordt op basis van wat hij kan vinden: pagina's die hij heeft opgehaald, feeds die een winkelier heeft aangeleverd en pagina's van derden die je noemen. Staat in één daarvan nog het oude bedrag, dan kan het antwoord dat ook bevatten.

Een verkeerde prijs is dus een dataprobleem op een pagina die je beheert of kunt aanspreken. Daarom is het op te lossen. Het herstel gebeurt bij de bron, niet in de chat.

## Welke stappen volg je?

1. Noteer het foute antwoord. Open een nieuwe chat en stel dezelfde vraag nog eens.
2. Zoek de oude prijs op je eigen pagina, in de paginabron en in de JSON-LD.
3. Controleer je productfeed. Een actieprijs die op je site is afgelopen, kan in de feed zijn blijven staan.
4. Zoek de oude prijs op andere websites, samen met je merk- en productnaam.
5. Wacht en vraag het daarna twee keer opnieuw, in nieuwe chats.

## Stap 1: hoe noteert je het foute antwoord?

Open een nieuwe chat, met webzoeken aan als de assistent dat biedt, en vraag: "Wat kost [product] van [webshop]?" Kopieer het antwoord, de datum, de assistent en elke link die wordt genoemd. Een genoemde link is de beste aanwijzing, want die noemt de pagina die het antwoord voedde.

Vraag het een tweede keer in een andere nieuwe chat. Verschillen de twee antwoorden, noteer dan beide, want antwoorden wisselen per run.

## Stap 2: hoe vind je de oude prijs op je eigen pagina?

1. Open de productpagina en bekijk de paginabron (rechtsklik, Paginabron weergeven).
2. Zoek op de oude prijs, bijvoorbeeld `49,00` en `49.00`. Probeer met en zonder euroteken.
3. Zoek het blok `application/ld+json` en lees de `price` onder `offers`. Productmarkup die nooit is bijgewerkt, is een veelvoorkomende reden voor een verouderd bedrag.
4. Kijk of er een tweede prijs op de pagina staat: een "van"-prijs, een bundelprijs of een variant die een ander bedrag laadt.
5. Haal de pagina op zoals een crawler dat doet, zonder JavaScript. Verschijnt de prijs pas nadat scripts draaien, dan ziet een crawler het eindbedrag mogelijk niet.

## Stap 3: hoe controleert je je productfeed?

Verkoopt je via Google Shopping, een marktplaats of de shoppingfeed van ChatGPT, dan is de feed een tweede kopie van je prijs. De productfeedspecificatie van OpenAI vraagt om een prijs in de vorm `79.99 USD`, één rij per koopbaar artikel of variant, en zegt dat je de feed moet bijwerken wanneer een actie begint of eindigt ([OpenAI-productfeed](https://developers.openai.com/commerce/specs/file-upload/products)).

Een actie die op je site is afgelopen maar in de feed bleef staan, is de klassieke afwijking. Controleer na elke actie of de feed opnieuw is aangeleverd.

De pagina van OpenAI beschrijft geen manier om al verwerkte data te betwisten, dus beloven wij die ook niet.

## Stap 4: hoe zoekt je de oude prijs op andere websites?

Zoek de oude prijs samen met je merknaam en productnaam. Kijk bij prijsvergelijkers, reviewsites, prijslijsten, oude blogberichten en je eigen persberichten. Vraag de eigenaar van elke pagina om bij te werken.

Lukt dat niet, publiceer dan op je eigen site een actuele pagina met de prijs en de datum, zodat de nieuwste bron ook de duidelijkste is.

## Stap 5: hoe lang wachten en hoe vraagt je opnieuw?

OpenAI zegt dat een wijziging in robots.txt ongeveer 24 uur kan duren voordat die bij de zoekcrawler is ([OpenAI-documentatie over crawlers](https://developers.openai.com/api/docs/bots)). Over het verversen van een pagina die al is gelezen publiceert OpenAI geen schema. Niemand kan je dus een datum beloven.

Stel dezelfde vraag eens per week twee keer, in nieuwe chats, en noteer elk antwoord in een tabel.

| Datum | Assistent | Vraag | Getoonde prijs | Link genoemd | Klopt met je pagina? |
| --- | --- | --- | --- | --- | --- |
| 20-10-2026 | ChatGPT, zoeken aan | Wat kost [product] van [webshop]? | | | |

## Kan de audit dit vinden?

De CitedBy-audit crawlt je pagina's en test of AI-crawlers ze kunnen bereiken en je productdata kunnen lezen. Is je prijspagina geblokkeerd of leeg voor een crawler, dan helpt geen enkele prijscorrectie. Test dat dus eerst.

## FAQ

### Waarom toont ChatGPT een oude prijs voor mijn product?
Waarschijnlijk las het het oude bedrag op je pagina, in je productfeed of op een andere website die het nog heeft. Zoek de oude prijs op elke plek en kijk naar de link die wordt genoemd, als die er is.

### Hoe lang duurt het voordat ChatGPT de nieuwe prijs toont?
Niemand kan een datum beloven. OpenAI zegt dat robots.txt-wijzigingen ongeveer 24 uur nodig hebben om de zoekcrawler te bereiken en geeft geen ververschema voor pagina's die al zijn gelezen. Vraag wekelijks opnieuw en noteer de antwoorden.

### Kan ik OpenAI vragen een foute prijs te wijzigen?
De feedspecificatie van OpenAI beschrijft geen manier om verwerkte data te corrigeren. Herstel dus de bronnen en test opnieuw. Kijk in het helpcentrum van OpenAI of er op het moment dat je dit leest een meldoptie bestaat.

### Telt een prijs in schema-markup mee?
Ja, als die verouderd is. Een JSON-LD-blok dat nooit is bijgewerkt, is een veelvoorkomende afwijking om op te letten.

## Sources

- [OpenAI: productfeedspecificatie](https://developers.openai.com/commerce/specs/file-upload/products)
- [OpenAI: crawlers en user agents](https://developers.openai.com/api/docs/bots)
- [CitedBy: site-audit](https://citedby.eu/nl)
