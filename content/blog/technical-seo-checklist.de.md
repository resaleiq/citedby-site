title: Technische SEO-Checkliste für KI-Sichtbarkeit im Onlineshop
h1: Technische SEO-Checkliste für KI-Sichtbarkeit: 9 Prüfungen für Ihren Onlineshop
description: Neun technische Prüfungen, mit denen Sie selbst testen, ob KI-Crawler Ihren Onlineshop lesen können: robots.txt, Statuscodes, Sitemap, JSON-LD und mehr.
slug: technical-seo-checklist
locale: de
section: guides
cluster: Technische Grundlagen
date: 2026-10-20
reviewed: 2026-10-20
widget: on
howto: on
related: /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen?; /de/blog/is-gptbot-blocked|Ist GPTBot auf meiner Website blockiert?; /de/guides/cms|KI-Sichtbarkeit für Shopify, WooCommerce und Co.
hero: auto
hero_alt: Titelkarte: Technische SEO-Checkliste für KI-Sichtbarkeit mit vier der neun Prüfungen: robots.txt, Statuscodes, Sitemap und Text im HTML
hero_sub: Neun Prüfungen, die Sie ohne Tool selbst machen
hero_boxes: robots.txt|KI-Crawler erlaubt?;Statuscodes|200 auf wichtigen Seiten;Sitemap|listet die richtigen URLs;Text im HTML|ohne JavaScript lesbar
answer: Technisch sichtbar für KI ist ein Onlineshop, wenn neun Dinge stimmen: robots.txt, Statuscodes, Sitemap, Canonical, hreflang, Titel und H1, JSON-LD, Text im rohen HTML und funktionierende interne Links. Jede Prüfung können Sie mit Browser und Quelltext selbst machen. llms.txt ist optional, weil kein großer Assistent bestätigt hat, sie zu lesen.
steps_img: on

## Was gehört in eine technische Checkliste für KI-Sichtbarkeit?

Ein Assistent kann Ihren Shop nur nennen, wenn er ihn lesen kann. Die folgenden neun Prüfungen betreffen genau das: Zugang, Auslieferung, Struktur und Lesbarkeit. Sie brauchen dafür nur einen Browser. Wer lieber nicht jede Seite einzeln öffnet, lässt das [Audit](/de/ai-visibility-audit) (ab 9 €) alle Seiten crawlen. Ob ein Assistent Sie danach tatsächlich nennt, ist eine zweite Frage, die Sie mit [20 Prompts](/de/blog/check-what-ai-says-about-your-brand) messen.

## Die neun Prüfungen

1. robots.txt und KI-Crawler: Öffnen Sie `ihr-shop.de/robots.txt`. Suchen Sie nach `OAI-SearchBot`, `GPTBot`, `PerplexityBot`, `Google-Extended` und `*`. Ein pauschales `Disallow: /` unter `User-agent: *` sperrt jeden Crawler ohne eigene Regel. Die robots.txt ist eine Bitte. Ob Ihr Server oder CDN trotzdem sperrt, prüfen Sie wie in [Ist GPTBot auf meiner Website blockiert?](/de/blog/is-gptbot-blocked).
2. HTTP-Status wichtiger Seiten: Rufen Sie Startseite, eine Kategorie, ein Produkt sowie die Seiten zu Versand und Rückgabe auf. Jede sollte 200 liefern. Mit `curl -s -o /dev/null -w "%{http_code}\n" https://ihr-shop.de/` sehen Sie den Code. Fehler wie 403, 404, 429 oder 503 sind ein Problem, 302-Umleitungen auf eine Login-Seite ebenso.
3. sitemap.xml: Öffnen Sie `ihr-shop.de/sitemap.xml`. Sie sollte die Seiten nennen, die gelesen werden sollen, und nichts, was Fehler liefert oder per `noindex` ausgeschlossen ist. Eine Sitemap hilft Suchmaschinen, Ihre Seiten effizienter zu crawlen ([Google: Sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview)).
4. Canonical: Suchen Sie im Quelltext nach `rel="canonical"`. Auf einer Produktseite sollte die Adresse auf sich selbst zeigen. Bei Filter- und Sortierseiten zeigt sie auf die Hauptseite. Google nennt Canonical-Angaben ein starkes Signal für die bevorzugte URL ([Google: Canonical](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)).
5. hreflang: Verkaufen Sie in mehreren Ländern oder Sprachen, etwa für Deutschland, Österreich und die Schweiz, suchen Sie `hreflang` im Quelltext. Jede Sprachversion sollte die anderen nennen. Google beschreibt drei Wege: HTML, HTTP-Header oder Sitemap ([Google: lokalisierte Versionen](https://developers.google.com/search/docs/specialty/international/localized-versions)).
6. Titel und H1: Prüfen Sie im Quelltext `<title>` und `<h1>`. Jede Seite braucht einen eigenen, beschreibenden Titel und genau eine H1. Google rät von vagen Titeln wie "Home" ab ([Google: Titellinks](https://developers.google.com/search/docs/appearance/title-link)).
7. JSON-LD für Product und Organization: Suchen Sie im Quelltext nach `application/ld+json`. Auf der Startseite sollten Name, Logo und Kontakt als Organization stehen. Auf Produktseiten gehören Name, Preis und Verfügbarkeit in einen Product-Block ([Google: Product-Markup](https://developers.google.com/search/docs/appearance/structured-data/product)). Der Preis dort sollte zum sichtbaren Preis passen.
8. Text im rohen HTML: Wählen Sie "Seitenquelltext anzeigen" (nicht die Entwicklertools, die zeigen die fertige Seite) und suchen Sie Produktnamen, Preis, Versandkosten und Lieferzeit. Steht dort nur ein leeres Gerüst, fehlt der Text für jeden Crawler, der kein JavaScript ausführt. Google führt zwar JavaScript aus, beschreibt dafür aber eigene Phasen und Grenzen ([Google: JavaScript-SEO](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)). Manche Assistenten führen kein JavaScript aus, deshalb gehört der Text ins HTML.
9. Defekte interne Links: Klicken Sie sich durch Menü, Kategorien und die Links in Ihren Produktbeschreibungen. Jeder Link auf eine 404-Seite ist eine Sackgasse für Crawler. Bei großen Shops ist das von Hand mühsam, hier spart ein Crawl Zeit.

## Was ist mit llms.txt?

llms.txt ist optional. Kein großer Assistent hat bestätigt, sie zu lesen, und die Studien von Ahrefs und SE Ranking zeigen bisher keinen messbaren Nutzen. Legen Sie sie erst an, wenn die neun Punkte oben erledigt sind. Die Belege stehen in [Bringt llms.txt etwas?](/de/blog/does-llms-txt-work).

## In welcher Reihenfolge arbeiten Sie die Punkte ab?

| Wenn Sie sehen | Zuerst beheben |
| --- | --- |
| Ein Crawler ist in der robots.txt gesperrt | Prüfung 1, dann 2 |
| Wichtige Seiten liefern keinen Status 200 | Prüfung 2 |
| Der Text fehlt im Quelltext | Prüfung 8 |
| Alles sauber, aber Mitbewerber werden genannt | Prüfungen 6 und 7, dann Antworten und FAQ auf den Hauptseiten ergänzen |

Prüfung 1, 2 und 8 entscheiden, ob eine Seite überhaupt gelesen wird. Die übrigen verbessern, wie gut sie verstanden wird.

## Was ist, wenn Sie ein Shopsystem wie Shopify oder WooCommerce nutzen?

Dann setzen Sie viele Punkte nicht im Code um, sondern in den Einstellungen Ihres Systems. Wo das geht und wo nicht, steht im Ratgeber [KI-Sichtbarkeit für Shopify, WooCommerce und Co.](/de/guides/cms).

## FAQ

### Wie lange dauert die Checkliste?
Für die Startseite, eine Kategorie und ein Produkt rechnen Sie mit etwa einer Stunde. Je mehr Seitentypen Ihr Shop hat, desto länger dauert es. Ein Crawl nimmt Ihnen den Teil ab, der von Hand mühsam ist.

### Brauche ich für KI-Sichtbarkeit etwas anderes als für SEO?
Die technische Basis ist weitgehend dieselbe. Google schreibt, dass für seine KI-Funktionen keine zusätzlichen Anforderungen gelten. Für andere Assistenten ist vor allem wichtig, dass ihr Crawler Zugang hat und Text im HTML findet.

### Muss ich JSON-LD selbst schreiben?
Meist nicht. Viele Shopsysteme und Themes geben Product-Daten aus. Prüfen Sie im Quelltext, ob Preis und Verfügbarkeit zur sichtbaren Seite passen.

### Reicht eine Sitemap, damit KI meine Seiten findet?
Nein. Die Sitemap zeigt, welche Seiten Sie wichtig finden. Ob ein Crawler sie abrufen darf und lesen kann, hängt von robots.txt, Server und Seiteninhalt ab.

## Sources

- [Google Search Central: Sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview)
- [Google Search Central: Canonical-URLs festlegen](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- [Google Search Central: lokalisierte Versionen und hreflang](https://developers.google.com/search/docs/specialty/international/localized-versions)
- [Google Search Central: Titellinks beeinflussen](https://developers.google.com/search/docs/appearance/title-link)
- [Google Search Central: Product-Markup](https://developers.google.com/search/docs/appearance/structured-data/product)
- [Google Search Central: Grundlagen JavaScript-SEO](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- [OpenAI: Crawler und User-Agents](https://developers.openai.com/api/docs/bots)
- [CitedBy Website-Audit](https://citedby.eu/)
