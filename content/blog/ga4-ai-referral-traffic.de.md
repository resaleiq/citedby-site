title: GA4: Traffic von ChatGPT und KI-Assistenten messen
h1: GA4: So messen Sie Besucher von ChatGPT und anderen KI-Assistenten
description: Eigener Kanal für KI-Assistenten in Google Analytics 4: Regex, Reihenfolge der Kanäle und was GA4 nicht sehen kann. Schritt für Schritt erklärt.
slug: ga4-ai-referral-traffic
locale: de
cluster: Messung
date: 2026-10-20
reviewed: 2026-10-20
widget: on
howto: on
related: /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen?; /de/blog/check-what-ai-says-about-your-brand|Was sagt ChatGPT über Ihre Marke? 20 Prompts; /de/ai-visibility-audit|KI-Sichtbarkeits-Audit für Ihre Website
hero: auto
hero_alt: Titelkarte: GA4 und KI-Traffic, mit drei Schritten: Quellen im Bericht finden, Kanal mit Regex anlegen, Kanal über Referral schieben
hero_sub: Eigener Kanal, richtige Reihenfolge, ehrliche Zahl
hero_boxes: Quellen finden|im Akquisitionsbericht;Kanal anlegen|Quelle per Regex;Reihenfolge|über Referral schieben
steps_img: on
answer: Legen Sie in GA4 eine eigene Channelgruppe mit einem Kanal "KI-Assistenten" an, dessen Quelle zu einem Regex der Assistenten passt, die Sie im Bericht Traffic-Akquisition sehen. Schieben Sie ihn über Referral, denn GA4 nutzt den ersten passenden Kanal. Vergleichen Sie dann Conversions pro Kanal. Besuche ohne Referrer bleiben unter Direct.

## Warum sieht man KI-Besuche in GA4 nicht sofort?

GA4 ordnet jede Sitzung einem Kanal zu. Besuche aus einem Assistenten landen womöglich im Kanal Referral, vermischt mit Links aus Blogs und Verzeichnissen, oder in einem anderen Kanal. Als Gruppe sehen Sie sie so nicht. Ein eigener Kanal gibt ihnen eine eigene Zeile.

Laut Google-Dokumentation lässt sich eine benutzerdefinierte Channelgruppe rückwirkend auf Ihre Berichte anwenden. Ihr Verlauf wird also umbenannt, sobald Sie speichern ([Google Analytics-Hilfe](https://support.google.com/analytics/answer/13051316)). Um sie anzulegen, brauchen Sie mindestens die Rolle Editor in der Property. Standard-Properties können laut derselben Seite 2 benutzerdefinierte Channelgruppen mit bis zu 50 Kanälen enthalten.

## Wie legen Sie den Kanal "KI-Assistenten" an?

Die Menübezeichnungen können je nach Spracheinstellung von GA4 abweichen. Die englischen Namen stehen in Klammern.

1. Quellen finden: Öffnen Sie unter Berichte den Bereich Akquisition und dort Traffic-Akquisition (Traffic acquisition). Stellen Sie die Dimension auf Sitzung: Quelle/Medium (Session source / medium) um.
2. Namen notieren: Suchen Sie in der Liste nach Assistenten wie chatgpt, perplexity, gemini oder copilot und schreiben Sie die genauen Quellen auf, die Sie sehen.
3. Channelgruppe erstellen: Öffnen Sie Verwaltung, Datenanzeige, Channelgruppen (Channel groups) und wählen Sie, eine neue Channelgruppe zu erstellen.
4. Kanal mit Regex definieren: Fügen Sie einen neuen Kanal mit dem Namen "KI-Assistenten" hinzu. Als Bedingung wählen Sie Quelle (Source), entspricht regulärem Ausdruck (matches regex), und tragen Ihre Liste ein.
5. Reihenfolge anpassen: Speichern Sie den Kanal, wählen Sie Neu anordnen (Reorder), ziehen Sie "KI-Assistenten" über Referral und klicken Sie auf Anwenden.

Öffnen Sie danach Traffic-Akquisition mit Ihrer neuen Channelgruppe als Dimension und vergleichen Sie Sitzungen, engagierte Sitzungen und Conversions.

Die Reihenfolge ist der Schritt, den die meisten übersehen. Laut Google fließt Traffic in den ersten Kanal, dessen Definition bei der aktuellen Reihenfolge passt. Steht Referral über Ihrem neuen Kanal, erreichen Assistenten ihn nie.

## Welchen Regex nehmen Sie als Ausgangspunkt?

Als Ausgangspunkt taugt eine Liste der bekannten Assistenten:

```
(chatgpt|openai|perplexity|gemini|copilot)
```

Verstehen Sie das als Startvermutung, nicht als geprüfte Liste. Hostnamen ändern sich, neue Assistenten kommen dazu. Entscheidend ist, was in Ihrem eigenen Bericht steht. Ergänzen Sie die Quellen, die Sie wirklich sehen, und streichen Sie alles, was auf etwas anderes als einen Assistenten passt. Prüfen Sie den Regex mindestens einmal pro Quartal.

## Was kann GA4 nicht erkennen?

Nur Besuche mit Referrer lassen sich zuordnen. Wer Ihre Adresse aus einer Antwort kopiert und in den Browser einfügt, kommt als Direct an. Der GA4-Kanal zeigt deshalb eine Untergrenze der KI-getriebenen Besuche, nicht die Gesamtzahl. Sagen Sie das dazu, wenn Sie die Zahl jemandem nennen, der danach handelt.

Kleine Zahlen können Zufall sein. Vergleichen Sie Conversion-Rate und Umsatz pro Sitzung mit Organic Search, bevor Sie Schlüsse ziehen, und rechnen Sie nicht von einer Woche Daten hoch.

## Welche Kennzahlen vergleichen Sie?

Legen Sie den neuen Kanal neben Organic Search und Direct und schauen Sie auf drei Werte: die Zahl der Sitzungen, den Anteil engagierter Sitzungen und die Conversions. Hat der Kanal nur wenige Sitzungen, lesen Sie die Prozentwerte vorsichtig. Drei Bestellungen aus zehn Sitzungen sind ein anderer Befund als dreißig aus hundert.

Halten Sie den Zeitraum fest, wenn Sie vergleichen, und nehmen Sie bei Zahlen für Entscheidungen mehrere Wochen. Notieren Sie außerdem, wann Sie den Kanal angelegt haben, damit spätere Änderungen am Regex nachvollziehbar bleiben.

## Wie geht es nach der Messung weiter?

Der Kanal zeigt, ob Assistenten Besucher schicken. Er zeigt nicht, ob sie Ihren Shop nennen. Ob KI-Crawler Ihre Seiten lesen können, prüft das Audit, und mit echten Käuferfragen sehen Sie, wer genannt wird. Eine Anleitung dazu finden Sie in [Was sagt ChatGPT über Ihre Marke? 20 Prompts](/de/blog/check-what-ai-says-about-your-brand).

## FAQ

### Wie sehe ich ChatGPT-Traffic in GA4?
Öffnen Sie Traffic-Akquisition mit Sitzung: Quelle/Medium und suchen Sie in der Spalte Quelle nach chatgpt. Für eine dauerhafte Ansicht legen Sie wie oben einen Kanal "KI-Assistenten" an.

### Warum erscheint mein KI-Traffic als Direct?
Sendet der Browser des Besuchers keinen Referrer, hat GA4 nichts, was es zuordnen könnte. Das passiert, wenn ein Link eingefügt oder aus einer App ohne Referrer-Angabe geöffnet wird.

### Ändert eine benutzerdefinierte Channelgruppe meine alten Daten?
Laut Google lassen sich benutzerdefinierte Channelgruppen rückwirkend auf Ihre Berichte anwenden. Ihr Verlauf wird also in den Berichten, die die Gruppe nutzen, neu zugeordnet.

### Muss ich Administrator sein, um den Kanal anzulegen?
Nein, aber Sie brauchen mindestens die Rolle Editor in der Property.

## Sources

- [Google Analytics-Hilfe: benutzerdefinierte Channelgruppen](https://support.google.com/analytics/answer/13051316)
