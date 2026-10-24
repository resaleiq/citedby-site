title: WordPress.com: KI-Opt-out per Datenschutz, nicht per robots.txt
slug: wordpress-com
description: WordPress.com behandelt das KI-Opt-out als „Prevent third-party sharing“ in den Datenschutzeinstellungen. Was der Leitfaden sagt, geprüft am 5. Oktober 2026.
section: platforms
locale: de
cluster: KI-Crawler nach Plattform
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Vier Fakten zu WordPress.com: Wo Privacy settings, Nicht Eine Änderung der robots.txt, Leitfaden geprüft 5. Okt. 2026, Außerdem MCP-Zugriff für Agenten
hero_sub: Einstellungen für KI-Crawler bei WordPress.com
hero_boxes: Wo|Privacy settings; Nicht|Eine Änderung der robots.txt; Leitfaden geprüft|5. Okt. 2026; Außerdem|MCP-Zugriff für Agenten
widget: on
related: /de/platforms|Alle Plattformen im Vergleich; /de/platforms/cloudflare|Cloudflare; /de/bots|KI-Crawler im Vergleich; /de/guides/cms|Checkliste für KI-Sichtbarkeit bei Shopify, WooCommerce und mehr
answer: Bei WordPress.com ist das KI-Opt-out eine Datenschutzeinstellung und keine Änderung der robots.txt. Der Leitfaden zur Sichtbarkeit der Site, zuletzt am 5. Oktober 2026 geprüft, sagt: Um das Teilen Ihrer öffentlichen Inhalte mit Dritten, auch KI-Modellen, abzulehnen, folgen Sie dem Leitfaden Prevent third-party sharing.

## Wo die Einstellung bei WordPress.com liegt

WordPress.coms Leitfaden zur Sichtbarkeit führt Sie für Site Visibility (Public, Coming Soon oder Private) zu Settings, dann Reading, und für das KI-Opt-out zu einem separaten Leitfaden Prevent third-party sharing.

## Das KI-Opt-out ist hier eine Freigabe-Einstellung

WordPress.coms Leitfaden zur Steuerung der Sichtbarkeit Ihrer Site sagt: Um das Teilen der öffentlichen Inhalte Ihrer Site mit Dritten (auch KI-Modellen) abzulehnen, rufen Sie den Leitfaden Prevent third-party sharing auf. Das ist eine Plattform-Einstellung, getrennt von der robots.txt, die Such- und KI-Crawler lesen. Dieselbe Seite, zuletzt am 5. Oktober 2026 geprüft, beschreibt auch die Gegenrichtung: Sie können externe KI-Agenten wie ChatGPT oder Claude anbinden, damit sie die Einstellungen zur Sichtbarkeit Ihrer Site lesen und bearbeiten, indem Sie den MCP-Tool-Zugriff aktivieren. Den Inhalt des Leitfadens Prevent third-party sharing konnten wir am 21. Oktober nicht lesen: Die Seite lud mit ihrem Titel und einem Prüfdatum vom 1. August 2024, aber ohne Schritte, sowohl per einfachem Abruf als auch im Browser. Diese Seite beschreibt also nicht, wie diese Einstellung funktioniert; öffnen Sie den Leitfaden aus Ihrem eigenen Dashboard. Wenn Sie selbst gehostetes WordPress statt WordPress.com betreiben, können Sie die Datei wie bei jedem Host selbst bearbeiten.

Mit den Worten des Anbieters (englisches Original): “To opt out of sharing your site's public content with third parties (including AI models), visit the Prevent third-party sharing guide.”

Quelle: [WordPress.com Support: Control your site's visibility](https://wordpress.com/support/privacy-settings/), gelesen am 21. Oktober 2026.

## Die Schritte

1. Öffnen Sie Settings, dann Reading, und prüfen Sie, ob Site Visibility auf Public steht, wenn Crawler die Site überhaupt sehen sollen.
2. Öffnen Sie WordPress.coms Leitfaden Prevent third-party sharing aus der Hilfe zu den Datenschutzeinstellungen und folgen Sie ihm, wenn Sie das Teilen von Inhalten mit Dritten, auch KI-Modellen, ablehnen möchten.
3. Öffnen Sie yourdomain.com/robots.txt und lesen Sie, was Ihre Site Crawlern tatsächlich ausliefert.

## Die passenden Zeilen

Zum Erlauben:

```
# No edit to make on WordPress.com for the sharing opt-out.
# Check what your site serves:
# https://yourdomain.com/robots.txt
```

Zum Sperren:

```
# On a self-hosted WordPress site, you add lines like these through your SEO plugin or the file:
User-agent: GPTBot
Disallow: /
```

## Stolperfallen

Eine Site im Modus Coming Soon oder Private ist nicht dasselbe wie ein KI-Opt-out: Sie verbirgt die Site vor allen, auch vor Suchmaschinen. Das ist das Gegenteil dessen, was ein Shop braucht, der zitiert werden will.

## Vergleich mit Cloudflare

[Cloudflare](/de/platforms/cloudflare): Ein Schalter auf Netzwerkebene, der unabhängig von der Plattform der Site funktioniert.

## Prüfen Sie Ihre eigene Website

Die kostenlose Prüfung im Feld oben liest die robots.txt für die KI-Crawler und sendet pro Crawler eine Live-Anfrage. So fällt eine Regel auf, die die Einstellungen Ihrer Plattform erlauben, eine Firewall aber ablehnt. Die vollständige Liste der Crawler finden Sie im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Ist das KI-Opt-out von WordPress.com dasselbe wie das Sperren von GPTBot?

WordPress.com beschreibt es als Ablehnung des Teilens Ihrer öffentlichen Inhalte mit Dritten, auch KI-Modellen. Es beschreibt es nicht als robots.txt-Regel. Prüfen Sie daher Ihre aktuelle robots.txt, um zu sehen, was Crawlern gesagt wird.

### Kann ich die robots.txt bei WordPress.com bearbeiten?

Im Leitfaden zur Sichtbarkeit, den wir gelesen haben, fanden wir keinen robots.txt-Editor, deshalb sagen wir dazu weder Ja noch Nein. Sehen Sie in den Einstellungen Ihrer Site für Ihren Tarif nach.

### Was ist MCP-Tool-Zugriff?

Laut Leitfaden können externe KI-Agenten damit die Einstellungen zur Sichtbarkeit Ihrer Site lesen und bearbeiten. Es geht um die Verwaltung der Site, nicht um Crawler.

## Sources

- [WordPress.com Support: Control your site's visibility](https://wordpress.com/support/privacy-settings/), gelesen am 21. Oktober 2026
- [WordPress.com Support: Prevent third-party sharing](https://wordpress.com/support/privacy-settings/prevent-third-party-sharing/), gelesen am 21. Oktober 2026
