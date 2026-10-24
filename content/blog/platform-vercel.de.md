title: Vercel: Das AI Bots Ruleset in der Firewall (Log oder Deny)
slug: vercel
description: Vercel blockt KI-Bots mit einem Firewall-Ruleset, nicht per robots.txt. Wo das AI Bots Ruleset liegt, was Log und Deny tun und wie Vercel die Bot-Liste pflegt.
section: platforms
locale: de
cluster: KI-Crawler nach Plattform
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu Vercel: Wo Firewall, Rules, Tarife Alle Tarife, Standard Allow (inaktiv), Aktionen Log oder Deny
hero_sub: Einstellungen für KI-Crawler bei Vercel
hero_boxes: Wo|Firewall, Rules; Tarife|Alle Tarife; Standard|Allow (inaktiv); Aktionen|Log oder Deny
widget: on
related: /de/platforms|Alle Plattformen im Vergleich; /de/platforms/cloudflare|Cloudflare; /de/bots|KI-Crawler im Vergleich; /de/guides/cms|Checkliste für KI-Sichtbarkeit bei Shopify, WooCommerce und mehr
answer: Vercel behandelt KI-Bots mit einem Firewall-Ruleset, nicht mit einer robots.txt-Zeile. Öffnen Sie in Ihrem Projekt Firewall, dann Rules, und stellen Sie das AI Bots Ruleset auf Log oder Deny. Es ist in allen Tarifen verfügbar und startet inaktiv, angezeigt als Allow. Bis Sie das ändern, wird also nichts blockiert.

## Wo die Einstellung bei Vercel liegt

Öffnen Sie im Dashboard Ihres Projekts in der Seitenleiste Firewall, dann Rules. Im Bereich Bot Management finden Sie die Regel AI Bots Ruleset. Vercels Docs sagen, das Ruleset sei in allen Tarifen verfügbar.

## Was nur Vercels Seite sagt und die anderer Plattformen nicht

Vercels Liste der KI-Bots müssen nicht Sie pflegen. Das Ruleset deckt KI-Bots ab, die für Trainingsdaten, für Suchzwecke oder für nutzergesteuerte Abrufe crawlen, und Vercel hält die Liste aktuell. Dieselbe Seite sagt, das Ruleset sei standardmäßig inaktiv und im Dashboard mit Allow beschriftet. Passender Traffic wird dann nicht ausgewertet und erreicht Ihre Anwendung. Die Steuerung ist eine einzige Aktion für das ganze Ruleset, Log oder Deny, angewendet an der Firewall.

Mit den Worten des Anbieters (englisches Original): “When new AI bots emerge, Vercel automatically adds them to its managed list and handles them according to your existing configured action without requiring any changes on your part.”

Quelle: [Vercel Docs: Bot Management](https://vercel.com/docs/bot-management), gelesen am 24. Oktober 2026.

## Die Schritte

1. Öffnen Sie im Dashboard Ihres Projekts in der Seitenleiste Firewall.
2. Öffnen Sie in der Seitenleiste Rules.
3. Wählen Sie im Bereich Bot Management bei der Regel AI Bots Ruleset Log oder Deny. Log zeichnet den Traffic von KI-Bots auf, ohne ihn zu blockieren, und eignet sich zur Beobachtung. Deny blockiert den gesamten Traffic, der als von KI-Bots stammend erkannt wird.
4. Wenn Sie etwas ändern, erscheint eine Schaltfläche Review Changes mit der Anzahl der Änderungen. Wählen Sie Review Changes, prüfen Sie die Änderungen und wählen Sie dann Publish, um sie auf Ihr Produktions-Deployment anzuwenden.

## Die passenden Zeilen

Vercels Seiten beschreiben das als Firewall-Einstellung, es gibt also keine robots.txt-Zeile zum Hinzufügen. Die beiden Zustände sind:

Zum Erlauben:

```
AI Bots Ruleset: Allow (the default, ruleset inactive)
```

Zum Sperren:

```
AI Bots Ruleset: Deny
```

## Stolperfallen

Deny blockiert den gesamten Traffic, der als von KI-Bots stammend erkannt wird, und der Geltungsbereich des Rulesets umfasst Training, Suche und nutzergesteuerte Abrufe zusammen. Damit lassen sich Trainings-Bots nicht blockieren, während Such-Bots erhalten bleiben. Log ist der sicherere erste Schritt. Vercels Seite sagt nicht, wie das Ruleset zu Ihrer robots.txt steht. Prüfen Sie daher gesondert, was Ihre eigene Datei sagt. Für einzelne Bots sagt dieselbe Seite, dass Sie manche oder alle Bots aus ihrem Verzeichnis verifizierter Bots mit benutzerdefinierten WAF-Regeln blockieren können, die die Match-Bedingung User Agent oder den Header Signature-Agent verwenden.

## Vergleich mit Cloudflare

[Cloudflare](/de/platforms/cloudflare): Ebenfalls ein Schalter auf Netzwerkebene, mit drei Aktionen für jedes von Search, Agent und Training.

## Prüfen Sie Ihre eigene Website

Die kostenlose Prüfung im Feld oben liest die robots.txt für die KI-Crawler und sendet pro Crawler eine Live-Anfrage. So fällt eine Regel auf, die die Einstellungen Ihrer Plattform erlauben, eine Firewall aber ablehnt. Die vollständige Liste der Crawler finden Sie im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Blockiert Vercel KI-Bots standardmäßig?

Nein. Vercels Docs sagen, das AI Bots Ruleset sei standardmäßig inaktiv, im Dashboard mit Allow beschriftet, und passender Traffic werde nicht ausgewertet und erreiche Ihre Anwendung.

### Muss ich Vercels Liste der KI-Bots selbst aktuell halten?

Nein. Vercel sagt, die Liste bekannter KI-Bots werde von Vercel automatisch gepflegt und aktualisiert, und neue Bots würden nach der Aktion behandelt, die Sie bereits festgelegt haben.

## Sources

- [Vercel Docs: Bot Management](https://vercel.com/docs/bot-management), gelesen am 24. Oktober 2026
- [Vercel Docs: WAF Managed Rulesets](https://vercel.com/docs/vercel-firewall/vercel-waf/managed-rulesets), gelesen am 24. Oktober 2026
