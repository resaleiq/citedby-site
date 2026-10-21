title: ChatGPT nennt meinen alten Preis: Quelle finden, korrigieren
h1: ChatGPT nennt meinen alten Preis. So finden Sie die Quelle und korrigieren sie
description: ChatGPT zitiert einen Preis, den Sie vor Monaten geändert haben. Die drei möglichen Quellen (Ihre Seite, Ihr Feed, fremde Seiten), Suche und erneuter Test.
slug: chatgpt-wrong-price
locale: de
cluster: Falsche Fakten
date: 2026-10-20
reviewed: 2026-10-20
widget: on
howto: on
related: /de/blog/check-what-ai-says-about-your-brand|Was sagt ChatGPT über Ihre Marke? 20 Prompts; /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen?; /de/ai-visibility-audit|KI-Sichtbarkeits-Audit für Ihre Website
hero: auto
hero_alt: Titelkarte: ChatGPT nennt meinen alten Preis, mit drei Kästen: Ihre eigene Seite, Ihr Produktfeed und fremde Websites
hero_sub: Falscher Preis? Die Quelle liegt außerhalb des Chats
hero_boxes: Ihre Seite|Text und JSON-LD;Ihr Produktfeed|zweite Kopie des Preises;Fremde Seiten|Vergleich und Verzeichnisse
steps_img: on
answer: ChatGPT nennt einen alten Preis, wenn es ihn aus einer veralteten Quelle gelesen hat: Ihrer eigenen Seite, einem Produktfeed oder einer fremden Website. Suchen Sie den alten Preis an jeder dieser Stellen, korrigieren Sie die Quelle und fragen Sie danach zweimal in einem neuen Chat nach. Aktualisieren Sie den Feed, sobald eine Aktion beginnt oder endet.

## Warum nennt ein Assistent einen Preis, den Sie längst geändert haben?

Ein Assistent antwortet mit dem, was er findet: Seiten, die er abgerufen hat, Feeds, die ein Händler eingereicht hat, und fremde Seiten, die Sie erwähnen. Trägt eine dieser Quellen noch den alten Betrag, kann die Antwort ihn auch tragen. Ein falscher Preis ist damit ein Datenproblem auf einer Seite, die Sie selbst pflegen oder bei der Sie nachfragen können. Deshalb lässt er sich beheben. Korrigiert wird an der Quelle, nicht im Chat.

Die folgenden fünf Schritte gehen die Quellen in dieser Reihenfolge durch: erst Ihre Seite, dann Ihr Feed, dann fremde Seiten.

## Wie gehen Sie vor?

1. Falsche Antwort festhalten: Öffnen Sie einen neuen Chat, mit aktivierter Websuche, falls der Assistent sie anbietet, und fragen Sie: "Was kostet [Produkt] von [Shop]?" Kopieren Sie Antwort, Datum, Assistent und jeden genannten Link. Ein genannter Link ist der beste Hinweis, denn er benennt die Seite, die die Antwort gespeist hat. Fragen Sie in einem zweiten neuen Chat noch einmal. Weichen die Antworten ab, notieren Sie beide.
2. Eigene Seite prüfen: Suchen Sie den alten Preis auf der Produktseite und im JSON-LD. Details stehen im nächsten Abschnitt.
3. Produktfeed prüfen: Gleichen Sie Feed und Seite ab, und aktualisieren Sie den Feed bei jeder Preisänderung.
4. Fremde Seiten suchen: Suchen Sie den alten Preis zusammen mit Marken- und Produktnamen auf anderen Websites.
5. Warten und erneut fragen: Stellen Sie die gleiche Frage einmal pro Woche zweimal in neuen Chats und notieren Sie jede Antwort.

## Wo steckt der alte Preis auf Ihrer eigenen Seite?

Öffnen Sie die Produktseite und den Seitenquelltext (Rechtsklick, "Seitenquelltext anzeigen"). Suchen Sie den alten Preis, zum Beispiel `49,00` und `49.00`, mit und ohne Währungszeichen. Im Quelltext steht der Preis oft mit Punkt, auf der Seite mit Komma.

Finden Sie den Block `application/ld+json` und lesen Sie den Preis unter `offers`. Produkt-Markup, das nie aktualisiert wurde, ist ein häufiger Grund für veraltete Zahlen. Google schreibt, dass Preis in Markup und Feed zum Preis auf der Zielseite passen müssen ([Google Merchant Center-Hilfe](https://support.google.com/merchants/answer/9773429)).

Achten Sie auch auf einen zweiten Preis auf der Seite: einen durchgestrichenen Preis, einen Bundle-Preis oder eine Variante, die einen anderen Betrag nachlädt. Rufen Sie die Seite außerdem so ab, wie ein Crawler es tut, ohne JavaScript. Erscheint der Preis erst nach dem Ausführen von Skripten, sieht ein Crawler eventuell nicht den endgültigen Betrag. Die Google-Hilfeseite warnt zudem, dass langsame Seiten dazu führen können, dass Crawler den endgültigen Preis verpassen.

## Stimmt Ihr Produktfeed noch?

Wer über Google Shopping, einen Marktplatz oder den Shopping-Feed von ChatGPT verkauft, hat im Feed eine zweite Kopie des Preises. Die Produktfeed-Spezifikation von OpenAI verlangt den Preis in der Form `79.99 USD`, eine Zeile pro kaufbarem Artikel oder Variante, und sie sagt, dass der Feed aktualisiert werden soll, wenn eine Aktion beginnt oder endet ([OpenAI-Produktfeed-Spezifikation](https://developers.openai.com/commerce/specs/feed)). Eine Aktion, die im Shop schon beendet ist, aber im Feed stehen blieb, ist die klassische Abweichung.

Google beschreibt dieselbe Falle für den eigenen Feed. Weichen Feed und Zielseite ab, gleichen Sie sie an, reichen den Feed erneut ein (Feed-Upload, Content API oder Ihr Shopsystem) und beantragen dann eine Prüfung. Die dauert laut Google 7 Werktage ([Google Merchant Center-Hilfe](https://support.google.com/merchants/answer/9773429)). Einen Weg, bereits eingelesene Daten bei OpenAI anzufechten, beschreibt die Seite nicht. Deshalb versprechen wir auch keinen.

## Wo steht der alte Preis auf fremden Seiten?

Suchen Sie den alten Preis zusammen mit Markenname und Produktname. Schauen Sie in Bewertungsportale, Preisvergleiche, Verzeichnisse, alte Blogbeiträge und Ihre eigenen Pressemitteilungen. Bitten Sie die jeweiligen Betreiber um eine Korrektur. Wo das nicht geht, veröffentlichen Sie auf Ihrer eigenen Seite eine aktuelle Seite mit Preis und Datum, damit die neueste Quelle auch die deutlichste ist.

## Wie lange dauert es, bis der neue Preis auftaucht?

OpenAI schreibt, dass eine Änderung der robots.txt etwa 24 Stunden braucht, bis sie beim Suchcrawler ankommt ([OpenAI-Dokumentation zu Crawlern](https://developers.openai.com/api/docs/bots)). Einen Zeitplan dafür, wann eine bereits gelesene Seite erneut abgerufen wird, nennt OpenAI nicht. Einen Termin kann Ihnen also niemand zusagen. Fragen Sie wöchentlich zweimal in neuen Chats nach und führen Sie eine Tabelle.

| Datum | Assistent | Frage | Genannter Preis | Genannter Link | Stimmt mit Ihrer Seite überein? |
| --- | --- | --- | --- | --- | --- |
| 20.10.2026 | ChatGPT, Suche an | Was kostet [Produkt] von [Shop]? | | | |

## Kann das Audit das finden?

Das CitedBy-Audit crawlt Ihre Seiten und testet, ob KI-Crawler sie erreichen und Ihre Produktdaten lesen können. Ist die Preisseite für einen Crawler gesperrt oder leer, hilft auch die beste Preiskorrektur nicht. Testen Sie das deshalb zuerst. Mehr dazu auf der Seite [KI-Sichtbarkeits-Audit](/de/ai-visibility-audit).

## FAQ

### Warum zeigt ChatGPT einen alten Preis für mein Produkt?
Vermutlich hat es den alten Betrag auf Ihrer Seite, in Ihrem Produktfeed oder auf einer fremden Website gelesen, die ihn noch trägt. Suchen Sie den alten Preis an jeder Stelle und sehen Sie sich den genannten Link an, falls es einen gibt.

### Wie lange dauert es, bis ChatGPT den neuen Preis zeigt?
Ein Datum kann niemand versprechen. OpenAI nennt etwa 24 Stunden, bis robots.txt-Änderungen beim Suchcrawler ankommen, und keinen Zeitplan für bereits gelesene Seiten. Fragen Sie wöchentlich nach und protokollieren Sie die Antworten.

### Kann ich OpenAI bitten, einen falschen Preis zu ändern?
Die Feed-Spezifikation von OpenAI beschreibt keinen Weg, bereits eingelesene Daten zu korrigieren. Beheben Sie deshalb die Quellen und testen Sie erneut. Schauen Sie ins Hilfecenter von OpenAI, ob es zum Zeitpunkt Ihres Besuchs eine Meldefunktion gibt.

### Spielt ein Preis im Schema-Markup eine Rolle?
Ja, wenn er veraltet ist. Google schreibt, dass Preis in Markup und Feed zur Zielseite passen soll. Ein nie aktualisierter Markup-Block ist eine häufige Abweichung.

## Sources

- [OpenAI: Produktfeed-Spezifikation](https://developers.openai.com/commerce/specs/feed)
- [OpenAI: Crawler und User-Agents](https://developers.openai.com/api/docs/bots)
- [Google Merchant Center-Hilfe: falscher Preis durch Abweichung zwischen Feed und Zielseite](https://support.google.com/merchants/answer/9773429)
- [CitedBy Website-Audit](https://citedby.eu/de)
