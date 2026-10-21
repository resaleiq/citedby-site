title: Kann ChatGPT meine Website lesen? Was darüber entscheidet
h1: Kann ChatGPT meine Website lesen? Drei Bedingungen und wie Sie sie prüfen
description: ChatGPT liest Ihren Onlineshop nur, wenn robots.txt, Server und Seiteninhalt mitspielen. So prüfen Sie die drei Bedingungen in einer Stunde selbst.
slug: can-chatgpt-read-my-website
locale: de
cluster: Crawler-Zugang
date: 2026-10-20
reviewed: 2026-10-20
widget: on
howto: on
related: /de/blog/is-gptbot-blocked|Ist GPTBot auf meiner Website blockiert?; /de/guides/technical-seo-checklist|Technische SEO-Checkliste für KI-Sichtbarkeit; /de/blog/check-what-ai-says-about-your-brand|Was sagt ChatGPT über Ihre Marke? 20 Prompts
hero: auto
hero_alt: Titelkarte: Kann ChatGPT meine Website lesen? Drei Tore: robots.txt, Antwort des Servers und Inhalt der Seite
hero_sub: Drei Tore, die offen sein müssen
hero_boxes: robots.txt|erlaubt OAI-SearchBot?;Server|antwortet ohne Fehler?;Seiteninhalt|Text steht im HTML
steps_img: on
answer: ChatGPT kann Ihre Website lesen, wenn drei Dinge zutreffen: Die robots.txt sperrt OAI-SearchBot nicht, der Seitentext steckt im HTML, das Ihr Server ausliefert, und nicht erst in nachgeladenem JavaScript, und Ihr Server oder Ihre Firewall weist den Crawler nicht ab. Das CitedBy-Audit prüft die ersten beiden auf jeder Seite.

## Welche drei Tore müssen offen sein?

ChatGPT nutzt für seine Suche einen Crawler namens OAI-SearchBot. Daneben betreibt OpenAI den GPTBot, der Trainingsdaten sammelt, und ChatGPT-User, der eine Seite abruft, wenn eine Person danach fragt. Laut OpenAI lässt sich jeder davon in der robots.txt einzeln steuern. Sie können also einen erlauben und einen anderen sperren ([OpenAI-Dokumentation zu Crawlern](https://developers.openai.com/docs/bots)).

Daraus ergeben sich drei Tore: Die robots.txt muss den Crawler zulassen, der Server muss ihm antworten, und auf der Seite muss lesbarer Text stehen. Das Audit testet das erste und das dritte Tor. Das zweite sehen nur Ihre Server-Logs.

## Wie prüfen Sie das Schritt für Schritt?

1. robots.txt ansehen: Öffnen Sie `ihr-shop.de/robots.txt` im Browser. Suchen Sie nach `User-agent: OAI-SearchBot`, `GPTBot` oder `*`, gefolgt von `Disallow: /`. Ein pauschales `Disallow: /` unter `User-agent: *` sperrt jeden Crawler, der keine eigene Regel hat.
2. Audit starten: Das Audit (ab 9 €) liest die robots.txt für OAI-SearchBot, GPTBot, PerplexityBot, Google-Extended und Bingbot und nennt die gesperrten.
3. Wortzahl lesen: Achten Sie auf die gemeldete Wortzahl im HTML. Ihre Startseite sollte dort mehrere hundert Wörter haben, darunter Ihren Shopnamen und was Sie verkaufen.
4. Quelltext durchsuchen: Öffnen Sie die Seite, wählen Sie "Seitenquelltext anzeigen" und suchen Sie nach Ihrem Produktnamen. Fehlt er, baut die Seite ihren Text per JavaScript auf. Ein Crawler ohne Skriptausführung sieht dann nichts.
5. Organisationsdaten prüfen: Stellen Sie sicher, dass Organization-Daten (JSON-LD) vorhanden sind. So finden Assistenten Name, Logo und Kontaktdaten an einer Stelle.

## Wie sieht eine leere Seite für einen Crawler aus?

Manche Shop-Themes und Baukästen liefern eine fast leere Seite aus und füllen sie erst per JavaScript. Ein Kunde sieht eine vollständige Produktseite. Ein Crawler, der kein JavaScript ausführt, bekommt nur ein leeres Gerüst: ein leeres `div` und ein Skript-Tag.

Manche Assistenten führen JavaScript aus, andere nicht. Sicher ist nur, wenn Ihr Markenname und Ihre Produkttexte im HTML selbst stehen. Das gilt besonders für Preis, Versandkosten und Lieferzeit, die in vielen Shop-Themes erst nachgeladen werden.

## Was heißt das für Shops mit Baukasten oder Theme?

Wer einen Baukasten oder ein fertiges Theme nutzt, sieht den Quelltext selten und verlässt sich darauf, dass die Standardeinstellungen passen. Das ist meist in Ordnung, aber nicht garantiert. Prüfen Sie deshalb einmal selbst, was Ihr Shop ausliefert: die robots.txt, den Text im Quelltext einer Produktseite und die Organization-Daten. Wie das in einzelnen Shopsystemen aussieht, steht im Ratgeber [KI-Sichtbarkeit für Shopify, WooCommerce und Co.](/de/guides/cms).

Wiederholen Sie die Prüfung nach jedem Theme-Wechsel und nach größeren Plugin-Updates, denn dabei ändern sich Einstellungen und Ausgaben gern unbemerkt.

## Welches Tor kann das Audit nicht sehen?

Die robots.txt ist eine Bitte, durchgesetzt wird auf Ihrem Hosting. Eine Firewall- oder CDN-Einstellung kann einem Crawler mit einem Fehler antworten, obwohl die robots.txt ihn erlaubt. Das testet das Audit nicht. Suchen Sie in Ihren Server- oder CDN-Logs nach Anfragen von `OAI-SearchBot` und sehen Sie nach, welche Statuscodes zurückkamen. Viele 403-Antworten sind das Zeichen. Wie Sie das genau prüfen, steht im Beitrag [Ist GPTBot auf meiner Website blockiert?](/de/blog/is-gptbot-blocked).

## Was machen Sie mit dem Ergebnis?

| Ergebnis | Maßnahme |
| --- | --- |
| robots.txt sperrt einen Crawler, den Sie wollen | Die passende `Disallow`-Regel entfernen. Laut OpenAI dauert es etwa einen Tag, bis die Änderung wirkt. |
| Wenig Wörter im HTML | Startseite und Produkttexte auf dem Server rendern lassen |
| Keine Organization-Daten | Als JSON-LD auf der Startseite ergänzen |
| Alles in Ordnung | Lesbarkeit ist die Eintrittskarte, nicht das Ergebnis. Ob ein Assistent Ihren Shop nennt, ist eine eigene Frage. |

Für die zweite Frage hilft die Methode aus [Was sagt ChatGPT über Ihre Marke? 20 Prompts](/de/blog/check-what-ai-says-about-your-brand).

## FAQ

### Ist GPTBot dasselbe wie die ChatGPT-Suche?
Nein. GPTBot sammelt Daten, die zum Training von Modellen verwendet werden können. OAI-SearchBot ist der Crawler für die ChatGPT-Suchergebnisse. Sie können GPTBot sperren und OAI-SearchBot trotzdem erlauben.

### Erwähnt ChatGPT meinen Shop nicht mehr, wenn ich GPTBot sperre?
Nicht von allein. Die Suchergebnisse hängen an OAI-SearchBot. Nur GPTBot zu sperren ist eine verbreitete Entscheidung bei Shops, die nicht wollen, dass ihre Inhalte für das Training genutzt werden.

### Behebt eine llms.txt das Problem?
Sie ist optional. Wir erwarten nicht, dass sie ändert, was Assistenten antworten, und das Audit führt sie als optional. Mehr dazu in [Bringt llms.txt etwas?](/de/blog/does-llms-txt-work).

### Wie lange dauert es, bis eine Änderung sichtbar wird?
OpenAI nennt etwa 24 Stunden, bis sich seine Systeme nach einer Änderung der robots.txt angepasst haben.

## Sources

- [OpenAI: Crawler und User-Agents](https://developers.openai.com/docs/bots)
- [CitedBy Website-Audit](https://citedby.eu/)
