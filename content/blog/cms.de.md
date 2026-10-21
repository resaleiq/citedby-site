title: KI-Sichtbarkeit für Shopify, WooCommerce und Co.
h1: KI-Sichtbarkeit für Shopify, WooCommerce und Co.: die Checkliste
description: Wo Sie bei Shopify und WooCommerce robots.txt und Sitemap finden, wie Sie Produkt-JSON-LD prüfen und woran Sie JavaScript-only-Texte im Theme erkennen.
slug: cms
locale: de
section: guides
cluster: Shopsysteme
date: 2026-10-20
reviewed: 2026-10-20
widget: on
howto: on
related: /de/guides/technical-seo-checklist|Technische SEO-Checkliste für KI-Sichtbarkeit; /de/blog/is-gptbot-blocked|Ist GPTBot auf meiner Website blockiert?; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen?
hero: auto
hero_alt: Titelkarte: KI-Sichtbarkeit für Shopify, WooCommerce und Co., mit fünf Prüfpunkten von robots.txt bis Theme-Text
hero_sub: Fünf Prüfpunkte, die in jedem Shopsystem gelten
hero_boxes: robots.txt|wo Sie sie ändern;Sitemap|wo Sie sie finden;Product-JSON-LD|im Quelltext prüfen;Theme-Text|ohne JavaScript lesbar
steps_img: on
answer: Bei Shopify bearbeiten Sie die robots.txt über die Vorlage robots.txt.liquid im Theme, und die Sitemap liegt automatisch unter ihr-shop.de/sitemap.xml. Bei WordPress und WooCommerce steuern Seitensichtbarkeit und Sitemap Einstellungen und Plugins. Welches System Sie auch haben: Prüfen Sie robots.txt, Sitemap, Product-JSON-LD und Theme-Text im Quelltext.

## Welche fünf Punkte prüfen Sie in jedem Shopsystem?

Shopsysteme nehmen Ihnen viel Technik ab, und genau deshalb lohnt der Blick in die Einstellungen. Diese Punkte gelten für Shopify, WooCommerce und jedes andere System:

1. robots.txt öffnen: Rufen Sie `ihr-shop.de/robots.txt` auf und suchen Sie nach `Disallow`-Regeln für KI-Crawler wie `OAI-SearchBot` und `GPTBot` sowie nach `User-agent: *` mit `Disallow: /`.
2. Sitemap finden: Rufen Sie `ihr-shop.de/sitemap.xml` auf. Fehlt sie, suchen Sie in den Einstellungen Ihres Systems.
3. Sichtbarkeit prüfen: Stellen Sie sicher, dass Ihr Shop nicht passwortgeschützt ist und keine Einstellung Suchmaschinen aussperrt.
4. Product-JSON-LD ansehen: Öffnen Sie eine Produktseite, wählen Sie "Seitenquelltext anzeigen" und suchen Sie `application/ld+json`. Name, Preis und Verfügbarkeit sollten zur sichtbaren Seite passen.
5. Theme-Text testen: Suchen Sie im Quelltext nach Produktname, Preis und Lieferzeit. Was dort fehlt, wird erst per JavaScript nachgeladen.

Die Hintergründe zu jedem Punkt stehen in der [technischen SEO-Checkliste](/de/guides/technical-seo-checklist).

## Wie gehen Sie bei Shopify vor?

Alle Shopify-Shops haben standardmäßig eine robots.txt, die laut Shopify für SEO ausgelegt ist. Wollen Sie sie anpassen, legen Sie im Code-Editor Ihres Themes die Vorlage `robots.txt.liquid` an: Onlineshop, beim gewünschten Theme "Code bearbeiten", "Neue Vorlage hinzufügen", "robots" wählen. Shopify weist darauf hin, dass dies eine nicht unterstützte Anpassung ist, bei der der Support nicht hilft, und dass falsche Eingaben den gesamten Traffic kosten können. Holen Sie sich dafür Hilfe von jemandem mit Erfahrung ([Shopify-Hilfe: robots.txt.liquid](https://help.shopify.com/en/manual/promoting-marketing/seo/editing-robots-txt)).

Für KI-Crawler beschreibt Shopify zwei Ebenen. Das Bot-Management auf Netzwerkebene übernimmt Shopify bei Shops, die dort laufen. Die robots.txt-Ebene steuern Sie selbst. Ihre Regeln dort sind laut Shopify richtungsweisend und unverbindlich, nicht jeder Crawler hält sich daran. Verkaufen Sie über Agentic Storefronts wie ChatGPT oder Copilot, laufen Ihre Produktdaten außerdem über Shopify Catalog, unabhängig von der robots.txt.

Die Sitemap erzeugt Shopify automatisch. Sie liegt im Hauptverzeichnis Ihrer Domain als `sitemap.xml` und verweist auf getrennte Sitemaps für Produkte, Kollektionen, Blogs und Seiten. Ist Ihr Shop im privaten Modus, kann kein Sitemap-Leser darauf zugreifen ([Shopify-Hilfe: Sitemap finden und einreichen](https://help.shopify.com/en/manual/promoting-marketing/seo/find-site-map)).

Ob Ihr Theme Product-Daten als JSON-LD ausgibt und ob Ihr Preis dort aktuell ist, prüfen Sie wie oben im Quelltext einer Produktseite. Was Ihr Theme genau ausgibt, steht in seiner Dokumentation.

## Wie gehen Sie bei WooCommerce und WordPress vor?

Bei WordPress finden Sie unter Einstellungen, Lesen, die Option "Suchmaschinen davon abhalten, diese Website zu indexieren". Ist sie aktiviert, bittet WordPress Suchmaschinen, die Website nicht zu indexieren. Die Dokumentation betont, dass sie den Zugriff nicht verhindert und es Sache der Suchmaschine ist, sich daran zu halten ([WordPress-Dokumentation: Einstellungen Lesen](https://wordpress.org/documentation/article/settings-reading-screen/)). Prüfen Sie diesen Haken zuerst, besonders nach einem Relaunch oder Umzug aus einer Testumgebung.

Seit WordPress 5.5 bringt der Kern eine einfache XML-Sitemap mit, die unter `wp-sitemap.xml` liegt ([Make WordPress Core](https://make.wordpress.org/core/2020/07/22/new-xml-sitemaps-functionality-in-wordpress-5-5/)). Viele Shops nutzen stattdessen die Sitemap eines SEO-Plugins. Öffnen Sie beide Adressen und prüfen Sie, welche Ihr Shop ausliefert.

Wie Sie die robots.txt bearbeiten, hängt bei WordPress von Ihrer Installation und Ihren Plugins ab. Schauen Sie in den Einstellungen Ihres SEO-Plugins oder fragen Sie Ihren Hoster. Ob und wie Ihr Theme oder Plugin Product-JSON-LD ausgibt, prüfen Sie im Quelltext einer Produktseite.

## Und bei anderen Shopsystemen?

Google weist darauf hin, dass Sie bei einem CMS wie Wix oder Blogger die robots.txt womöglich nicht direkt bearbeiten können oder müssen. Stattdessen biete das System eine Einstellungsseite für die Sichtbarkeit in Suchmaschinen ([Google: Einführung in robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro)). Ebenso erzeugen CMS wie WordPress oder Wix laut Google häufig schon eine Sitemap ([Google: Sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview)).

Für Shopware, JTL, Wix, IONOS, Jimdo und andere gilt deshalb: Prüfen Sie in den Einstellungen Ihres Systems, ob und wie sich robots.txt und Sitemap ändern lassen. Ob eine Funktion in Ihrem Tarif möglich ist, steht in der Hilfe Ihres Anbieters, nicht in diesem Ratgeber.

## Woran erkennen Sie Theme-Text, der nur mit JavaScript erscheint?

Vergleichen Sie, was Sie auf der Seite sehen, mit dem Seitenquelltext. Steht der Produktname, aber nicht der Preis im Quelltext, lädt Ihr Theme den Preis nach. Dasselbe gilt für Lieferzeit, Varianten und Bewertungen. Manche Assistenten führen kein JavaScript aus. Fragen Sie Ihren Theme-Anbieter, ob sich Preis und Verfügbarkeit serverseitig ausgeben lassen, oder wechseln Sie das Theme, wenn nicht.

## FAQ

### Kann ich bei Shopify KI-Crawler sperren?
Ja, über die Vorlage `robots.txt.liquid`. Shopify nennt die Regeln dort richtungsweisend und unverbindlich, und ein Eingriff gilt als nicht unterstützte Anpassung.

### Verschwinden meine Produkte aus ChatGPT, wenn ich einen Crawler in der robots.txt sperre?
Bei Shopify sagt die Hilfe, dass eine Sperre nur die Auffindbarkeit im offenen Web betrifft. Produktdaten, die Shopify Catalog an aktivierte Agentic Storefronts sendet, bleiben davon unberührt.

### Wo finde ich die Sitemap meines Shops?
Bei Shopify unter `ihr-shop.de/sitemap.xml`, bei WordPress ab Version 5.5 unter `wp-sitemap.xml`, sofern kein Plugin eine eigene ausliefert.

### Muss ich Product-JSON-LD selbst einbauen?
Prüfen Sie zuerst, was Ihr Theme oder Plugin ausgibt, im Quelltext einer Produktseite. Nur wenn Angaben fehlen oder veraltet sind, lohnt sich ein Eingriff.

## Sources

- [Shopify-Hilfe: robots.txt.liquid bearbeiten](https://help.shopify.com/en/manual/promoting-marketing/seo/editing-robots-txt)
- [Shopify-Hilfe: Sitemap finden und einreichen](https://help.shopify.com/en/manual/promoting-marketing/seo/find-site-map)
- [WordPress-Dokumentation: Einstellungen Lesen](https://wordpress.org/documentation/article/settings-reading-screen/)
- [Make WordPress Core: XML-Sitemaps in WordPress 5.5](https://make.wordpress.org/core/2020/07/22/new-xml-sitemaps-functionality-in-wordpress-5-5/)
- [Google Search Central: Einführung in robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro)
- [Google Search Central: Sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview)
- [CitedBy Website-Audit](https://citedby.eu/de)
