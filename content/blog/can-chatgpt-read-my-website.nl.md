title: Kan ChatGPT mijn website lezen? Wat daarover beslist
h1: Kan ChatGPT mijn webshop lezen? Drie dingen die het bepalen
description: Drie dingen bepalen of ChatGPT en andere AI-assistenten uw webshop kunnen lezen: robots.txt, de tekst in uw HTML en gestructureerde data. Zo checkt u ze.
slug: can-chatgpt-read-my-website
locale: nl
cluster: Crawlbaarheid
date: 2026-10-20
reviewed: 2026-10-20
answer: ChatGPT kan uw website lezen als drie dingen kloppen: robots.txt blokkeert OAI-SearchBot niet, de paginatekst staat in de HTML die uw server verstuurt in plaats van door JavaScript te worden toegevoegd, en uw server of firewall weigert de crawler niet. De CitedBy-audit test de eerste twee op elke pagina.
widget: on
howto: on
related: /nl/blog/is-gptbot-blocked|Is GPTBot geblokkeerd op uw site?; /nl/ai-visibility-audit|AI-zichtbaarheidsaudit; /nl/blog/check-what-ai-says-about-your-brand|Wat zegt ChatGPT over uw merk?
hero: auto
hero_alt: Drie poorten tussen een webshoppagina en een AI-assistent: robots.txt, paginarespons en paginatekst
hero_sub: Drie poorten tussen uw pagina en ChatGPT
hero_boxes: robots.txt|mag de crawler binnen; Serverantwoord|geen 403 of 429; Paginatekst|staat in de HTML
steps_img: on

## Welke drie poorten staan er tussen uw pagina en ChatGPT?

ChatGPT-zoeken gebruikt een crawler met de naam OAI-SearchBot om pagina's te vinden. OpenAI draait daarnaast GPTBot, die trainingsdata verzamelt, en ChatGPT-User, die een pagina ophaalt wanneer iemand ernaar vraagt. Volgens OpenAI stuurt u elk van die drie apart aan in robots.txt, dus u kunt de ene toestaan en de andere blokkeren ([OpenAI-documentatie](https://developers.openai.com/api/docs/bots)).

De drie poorten zijn: robots.txt, het antwoord van uw server en de inhoud van de pagina zelf. De audit test poort 1 en 3. Voor poort 2 hebt u uw serverlogs nodig.

Een webshop kan dus op alle drie de punten onderuit gaan zonder dat u het in uw browser merkt. Uw eigen pagina ziet er prima uit. Het gaat erom wat een crawler terugkrijgt.

## Hoe controleert u dat stap voor stap?

1. Open `uwwebshop.nl/robots.txt` in een browser. Zoek `User-agent: OAI-SearchBot`, `GPTBot` of `*`, gevolgd door `Disallow: /`. Een algemene `Disallow: /` onder `User-agent: *` blokkeert elke crawler die geen eigen regel heeft.
2. Laat uw site auditen met het vak hierboven (vanaf €9). De audit leest robots.txt voor OAI-SearchBot, GPTBot, PerplexityBot, Google-Extended en Bingbot en meldt welke geblokkeerd zijn.
3. Bekijk het aantal woorden dat de audit voor de HTML meldt. Uw homepage hoort daar honderden woorden te hebben, met uw merknaam en wat u verkoopt.
4. Kies op de pagina "Paginabron weergeven" en zoek op uw productnaam. Ontbreekt die, dan bouwt de pagina zijn tekst met JavaScript op en ziet een crawler die geen scripts draait niets.
5. Controleer of Organization-data (JSON-LD) aanwezig is, zodat assistenten uw naam, logo en contactgegevens op één plek vinden.

## Hoe ziet een geblokkeerde pagina eruit voor een crawler?

Sommige webshopthema's en sitebouwers sturen een bijna lege pagina en vullen die daarna met JavaScript. Een bezoeker ziet een complete productpagina. Een crawler die geen JavaScript draait, krijgt een lege huls: een `div` zonder inhoud en een scripttag.

Sommige assistenten draaien wel JavaScript en andere niet. De veilige keuze is dus uw merk- en producttekst in de HTML zelf te hebben, bijvoorbeeld met server-side rendering.

Een voorbeeld van een echte run: op 18 oktober 2026 draaide de check op bbc.com. De robots.txt blokkeert daar OAI-SearchBot, GPTBot, PerplexityBot en Google-Extended, en er staan 2.547 leesbare woorden in de HTML. De BBC doet dat bewust. Voor een webshop die genoemd wil worden, is zo'n uitkomst juist het probleem.

## Welke poort ziet de audit niet?

robots.txt is een verzoek. Uw hosting dwingt het af. Een firewall- of CDN-instelling kan een crawler met een foutcode beantwoorden, ook als robots.txt hem toelaat. De audit test dat niet.

Zoek in uw server- of CDN-logs naar verzoeken van `OAI-SearchBot` en kijk welke statuscodes terugkwamen. Een reeks 403-antwoorden is het teken. Hoe u dit verder uitzoekt, leest u in [Is GPTBot geblokkeerd op uw site?](/nl/blog/is-gptbot-blocked).

## Wat doet u met de uitkomst?

| Uitkomst | Wat u doet |
| --- | --- |
| robots.txt blokkeert een crawler die u wilt | Verwijder de bijbehorende `Disallow`-regel. OpenAI zegt dat een wijziging ongeveer een dag kan duren |
| Weinig woorden in de HTML | Laat de homepage en de producttekst op de server renderen |
| Geen Organization-data | Voeg die als JSON-LD toe op de homepage |
| Alles in orde | Leesbaar zijn is het toegangsbewijs, niet het resultaat. Of een assistent uw webshop noemt, meet de audit met echte koopvragen |

## FAQ

### Is GPTBot hetzelfde als ChatGPT-zoeken?
Nee. GPTBot verzamelt data die gebruikt kan worden om modellen te trainen. OAI-SearchBot is de crawler voor de zoekresultaten van ChatGPT. U kunt GPTBot blokkeren en OAI-SearchBot toch toestaan.

### Noemt ChatGPT mijn webshop niet meer als ik GPTBot blokkeer?
Niet vanzelf. Zoekresultaten hangen af van OAI-SearchBot. Alleen GPTBot blokkeren is een gangbare keuze voor webshops die niet willen dat hun content voor training wordt gebruikt.

### Lost een llms.txt dit op?
Het is optioneel. We verwachten niet dat het verandert wat assistenten antwoorden, en de audit markeert het als optioneel. Meer daarover leest u in [Werkt llms.txt?](/nl/blog/does-llms-txt-work).

### Hoe lang duurt het voordat een wijziging zichtbaar is?
OpenAI zegt dat het ongeveer 24 uur kan duren voordat zijn systemen zich aanpassen nadat u robots.txt hebt gewijzigd.

## Sources

- [OpenAI: crawlers en user agents](https://developers.openai.com/api/docs/bots)
- [CitedBy: site-audit](https://citedby.eu/nl)
