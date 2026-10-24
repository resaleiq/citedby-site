title: Webflow: robots.txt-Regeln und der Content-Signal-Header für KI
slug: webflow
description: Wo Webflows robots.txt-Editor liegt, welchen Tarif er braucht und wie der Content-Signal-Header KI-Training, Suche und KI-Eingabe trennt.
section: platforms
locale: de
cluster: KI-Crawler nach Plattform
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Vier Fakten zu Webflow: Wo Site settings, SEO, Voraussetzung Site- oder bezahlter Workspace-Tarif, Zusatz Content-Signal, Status Vorgeschlagene Erweiterung
hero_sub: Einstellungen für KI-Crawler bei Webflow
hero_boxes: Wo|Site settings, SEO; Voraussetzung|Site- oder bezahlter Workspace-Tarif; Zusatz|Content-Signal; Status|Vorgeschlagene Erweiterung
widget: on
related: /de/platforms|Alle Plattformen im Vergleich; /de/platforms/wix|Wix; /de/bots|KI-Crawler im Vergleich; /de/guides/cms|Checkliste für KI-Sichtbarkeit bei Shopify, WooCommerce und mehr
answer: Webflow legt die robots.txt unter Site settings, dann SEO, dann Indexing ab, und eine seiner Hilfeseiten sagt, Sie brauchen einen Site-Tarif oder einen bezahlten Workspace-Tarif. Es kann außerdem einen Content-Signal-Header senden, der ai-train, search und ai-input getrennt festlegt. Webflow nennt das eine vorgeschlagene Erweiterung, keinen anerkannten Standard.

## Wo die Einstellung bei Webflow liegt

Gehen Sie zu Site settings, dann SEO, dann Indexing, fügen Sie die gewünschte(n) robots.txt-Regel(n) hinzu und klicken Sie dann auf Save und veröffentlichen Sie Ihre Site. Webflow fügt standardmäßig eine Sitemap-Zeile hinzu; ein Schalter entfernt sie.

## Ein Header, der Training, Suche und KI-Antworten trennt

Neben der robots.txt kann eine Site laut Webflows Seite einen HTTP-Header Content-Signal ausliefern, der im selben Bereich Indexing gesetzt wird, um KI-Crawlern genauere Anweisungen zu geben. Das Beispiel der Seite lautet `Content-Signal: ai-train=no, search=yes, ai-input=no`. Webflow erklärt die Trennung: Die robots.txt steuert, ob Bots auf Ihre Seiten zugreifen können, während Content-Signal getrennt angibt, ob Inhalte für KI-Training, für die Suchindexierung oder für KI-generierte Antworten verwendet werden dürfen. Webflow nennt die Einschränkung selbst: Das beruht auf einer vorgeschlagenen Erweiterung von RFC 9309 und ist noch kein anerkannter Standard. Es drückt also eine Präferenz aus, hält aber keinen Crawler auf, und Webflows Seite sagt nicht, welche Crawler es lesen.

Mit den Worten des Anbieters (englisches Original): “This is based on a proposed extension to RFC 9309 and is not yet an accepted standard.”

Quelle: [Webflow Help: Set robots.txt rules](https://help.webflow.com/hc/en-us/articles/41954080897683-Set-robots-txt-rules), gelesen am 21. Oktober 2026.

## Die Schritte

1. Öffnen Sie Site settings und gehen Sie zu SEO, dann Indexing.
2. Tippen Sie die gewünschten robots.txt-Regeln in das Regelfeld.
3. Setzen Sie optional im selben Bereich den Content-Signal-Header.
4. Klicken Sie auf Save und veröffentlichen Sie Ihre Site. Öffnen Sie dann yourdomain.com/robots.txt, um die aktuelle Datei zu prüfen.

## Die passenden Zeilen

Zum Erlauben:

```
User-agent: OAI-SearchBot
Allow: /

User-agent: *
Allow: /
```

Zum Sperren:

```
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

Content-Signal: ai-train=no, search=yes, ai-input=no
```

## Stolperfallen

Webflows Seite sagt, Ihre robots.txt sei öffentlich sichtbar und nicht alle Bots befolgten sie. Verlassen Sie sich daher nicht darauf, private Seiten zu verbergen.

## Vergleich mit Wix

[Wix](/de/platforms/wix): Ein längerer Bearbeitungsweg und ein Beispiel mit vier Namen.

## Prüfen Sie Ihre eigene Website

Die kostenlose Prüfung im Feld oben liest die robots.txt für die KI-Crawler und sendet pro Crawler eine Live-Anfrage. So fällt eine Regel auf, die die Einstellungen Ihrer Plattform erlauben, eine Firewall aber ablehnt. Die vollständige Liste der Crawler finden Sie im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Brauche ich bei Webflow einen bezahlten Tarif für die robots.txt?

Eine Webflow-Hilfeseite sagt, Sie brauchen einen Site-Tarif oder einen bezahlten Workspace-Tarif, um Ihrer Site eine robots.txt hinzuzufügen.

### Was ist Content-Signal?

Eine vorgeschlagene Erweiterung von RFC 9309, die Webflow als Header senden kann: ai-train, search und ai-input, jeweils auf yes oder no gesetzt.

### Blockt Webflow schlechte Bots für mich?

Die Hilfeseite zeigt, wie Sie eine Regel für einen benannten Bot schreiben. Sie sagt, dass manche Bots, vor allem bösartige, die robots.txt nicht befolgen.

## Sources

- [Webflow Help: Set robots.txt rules](https://help.webflow.com/hc/en-us/articles/41954080897683-Set-robots-txt-rules), gelesen am 21. Oktober 2026
- [Webflow Help: Request to block specific bots from visiting your site](https://help.webflow.com/hc/en-us/articles/41954183592851-Request-to-block-specific-bots-from-visiting-your-site), gelesen am 21. Oktober 2026
