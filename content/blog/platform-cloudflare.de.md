title: Cloudflare: KI-Bot-Richtlinien für Search, Agent und Training
slug: cloudflare
description: Cloudflares Seite Block AI Bots teilt KI-Bots in Search, Agent und Training ein, mit Block, Block on pages with ads und Allow. Neue Standards ab 15. Sept. 2026.
section: platforms
locale: de
cluster: KI-Crawler nach Plattform
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Vier Fakten zu Cloudflare: Wo Security Settings, Verhalten Search, Agent, Training, Auswahl 3 pro Verhalten, Seite aktualisiert 1. Juli 2026
hero_sub: Einstellungen für KI-Crawler bei Cloudflare
hero_boxes: Wo|Security Settings; Verhalten|Search, Agent, Training; Auswahl|3 pro Verhalten; Seite aktualisiert|1. Juli 2026
widget: on
related: /de/platforms|Alle Plattformen im Vergleich; /de/platforms/shopify|Shopify; /de/bots|KI-Crawler im Vergleich; /de/guides/cms|Checkliste für KI-Sichtbarkeit bei Shopify, WooCommerce und mehr
answer: Cloudflare ordnet KI-Bots drei Verhaltensweisen zu: Search, Agent und Training. Für jede wählen Sie unter Security Settings und Configure AI bot policies zwischen Block on all pages, Block on pages with ads oder Allow. Laut der Seite, zuletzt am 1. Juli 2026 aktualisiert, gelten aktualisierte Standards für neue Domains ab dem 15. September 2026.

## Wo die Einstellung bei Cloudflare liegt

Gehen Sie im Cloudflare-Dashboard zu Security Settings und dann zu Configure AI bot policies. Jedes der drei Verhalten hat eine eigene Einstellung. Das funktioniert auf Netzwerkebene und gilt daher für jede Plattform, auf der die Website läuft.

## Drei Verhalten, drei Auswahlmöglichkeiten und ein Datum, das schon vorbei ist

Cloudflares Voreinstellungen sind: Search, Crawler, die Ihre Inhalte sammeln oder indexieren, um später Fragen dazu zu beantworten; Agent, automatisierte Aktivität, die in Echtzeit im Auftrag einer Person handelt, etwa Chat-Fetch-Bots und Browser-Use-Agenten; Training, Crawler, die Ihre Inhalte nehmen, um ein Modell zu trainieren oder feinzujustieren, einschließlich Crawler mit gemischtem Zweck, die sowohl für Training als auch für Search genutzt werden. Jede Voreinstellung blockiert verifizierte Bots, die so eingestuft sind, sowie einige nicht verifizierte Bots mit ähnlichem Verhalten. Die Seite, zuletzt am 1. Juli 2026 aktualisiert, kündigt neue Standards für neue Domains ab dem 15. September 2026 an: Training- und Agent-Bots werden auf Seiten mit Werbung blockiert, Search bleibt erlaubt, und Crawler mit gemischtem Zweck werden von jeder Konfiguration blockiert, die KI-Training sperrt. Das gilt auch für die ältere Option Block AI bots, die Cloudflare zu diesem Datum als auslaufend kennzeichnet. Die Seite verwendete noch das Futur, als wir sie am 21. Oktober lasen, fünf Wochen nach diesem Datum. Öffnen Sie daher Ihr eigenes Dashboard und sehen Sie nach, was eingeschaltet ist, statt sich auf einen der beiden Texte zu verlassen.

Mit den Worten des Anbieters (englisches Original): “Search: crawlers that collect or index your content to answer questions about it later.”

Quelle: [Cloudflare Docs: Block AI Bots](https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/), gelesen am 21. Oktober 2026.

## Die Schritte

1. Öffnen Sie Ihre Zone im Cloudflare-Dashboard und gehen Sie zu Security Settings.
2. Öffnen Sie Configure AI bot policies.
3. Wählen Sie für Search, Agent und Training jeweils Block on all pages, Block on pages with ads oder Allow.
4. Wenn Sie die ältere Option Block AI bots nutzen, prüfen Sie, welche Crawler mit gemischtem Zweck sie jetzt abdeckt, denn Cloudflare sagt, dass sie ausläuft.
5. Testen Sie mit dem kostenlosen [AI-crawler access checker](/de/tools/ai-crawler-check): Ein Bot, den die robots.txt erlaubt, kann hier trotzdem abgewiesen werden.

## Die passenden Zeilen

Zum Erlauben:

```
# Cloudflare settings are not robots.txt lines.
# Choose Allow (do not block) for Search so answer engines can fetch pages.
```

Zum Sperren:

```
# Cloudflare settings are not robots.txt lines.
# Choose Block (on all pages) for Training; leave Search on Allow.
```

## Stolperfallen

Das Risiko für einen Shop, der Zitierungen will, liegt in der mittleren Voreinstellung: Cloudflare definiert Agent als Chat-Fetch-Bots, die im Auftrag einer Person handeln. Das ist die Aufgabe von Fetchern wie [ChatGPT-User](/de/bots/chatgpt-user). Wenn Sie Agent blockieren, kann ein Assistent Ihre Seite womöglich nicht öffnen, wenn eine Person danach fragt, selbst wenn Ihre robots.txt ihn erlaubt. Beachten Sie auch, dass Shopify sagt, es empfehle keine Proxy-Konfiguration vor einem Shopify-Shop.

## Vergleich mit Shopify

[Shopify](/de/platforms/shopify): Sagt, es übernehme das Bot-Management selbst, und rät von einem Proxy ab.

## Prüfen Sie Ihre eigene Website

Die kostenlose Prüfung im Feld oben liest die robots.txt für die KI-Crawler und sendet pro Crawler eine Live-Anfrage. So fällt eine Regel auf, die die Einstellungen Ihrer Plattform erlauben, eine Firewall aber ablehnt. Die vollständige Liste der Crawler finden Sie im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Hat Cloudflares KI-Sperre Vorrang vor der robots.txt?

Cloudflares Seite beschreibt das Blockieren nach Verhalten an seinem Netzwerk. Ein Bot kann dort also abgewiesen werden, auch wenn Ihre robots.txt ihn erlaubt. Deshalb ist ein Test mit einer Live-Anfrage wichtig.

### Was ist bei Cloudflare der Unterschied zwischen Search und Training?

Search-Crawler indexieren Inhalte, um später Fragen zu beantworten; Training-Crawler nehmen Inhalte, um ein Modell zu trainieren oder feinzujustieren. Crawler mit gemischtem Zweck werden als Training eingestuft.

### Ist Block AI bots noch verfügbar?

Cloudflare kennzeichnet die Option zum 15. September 2026 als auslaufend. Die Seite war noch im Futur geschrieben, als wir sie am 21. Oktober 2026 lasen.

## Sources

- [Cloudflare Docs: Block AI Bots](https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/), gelesen am 21. Oktober 2026
