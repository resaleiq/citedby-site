title: WP Engine: robots.txt, Standard-Crawl-Delay 10 s und Web Rules
slug: wp-engine
description: Laut WP Engine hat eine physische robots.txt Vorrang vor Plugin-Dateien, der Standard-Crawl-Delay beträgt 10 Sekunden. Web Rules sperren Bots per User-Agent.
section: platforms
locale: de
cluster: KI-Crawler nach Plattform
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu WP Engine: Wo SFTP, Yoast oder Web Rules, Standard-Crawl-Delay 10 Sekunden, wpengine.com-Adresse Disallow all, Sperre per User-Agent Web Rules Engine
hero_sub: Einstellungen für KI-Crawler bei WP Engine
hero_boxes: Wo|SFTP, Yoast oder Web Rules; Crawl-Delay|Standard 10 Sekunden; wpengine.com|Disallow all; Sperre per User-Agent|Web Rules Engine
widget: on
related: /de/platforms|Alle Plattformen im Vergleich; /de/platforms/wordpress-com|WordPress.com; /de/bots|KI-Crawler im Vergleich; /de/guides/cms|Checkliste für KI-Sichtbarkeit bei Shopify, WooCommerce und mehr
answer: Laut WP Engines Seite zur robots.txt überschreibt eine physische robots.txt im Stammverzeichnis Ihrer Site jede Datei, die ein Plugin oder Theme erzeugt. Die Standarddatei setzt einen Crawl-Delay von 10 Sekunden, und Sites auf einer wpengine.com-Adresse bekommen eine Datei, die alles sperrt. Um einen Bot per User-Agent abzuweisen, verweist WP Engine auf seine Web Rules Engine.

## Wo die Einstellung bei WP Engine liegt

WP Engines Seite nennt zwei Wege, die Datei zu erstellen. Wenn das Plugin Yoast SEO installiert ist, gehen Sie zu SEO, dann Tools, wählen den Datei-Editor und dann Create robots.txt file. Oder Sie erstellen selbst eine robots.txt und laden sie per SFTP oder SSH Gateway in das Stammverzeichnis Ihrer Site hoch. Zum Sperren per User-Agent verweist die Seite auf die Access rules in der Web Rules Engine im User Portal.

## Was nur WP Engines Seite sagt und die anderer Plattformen nicht

WP Engine liefert eine Standard-robots.txt aus, und die Seite sagt, was darin steht. Laut ihrem Hinweis beträgt der Standard-Crawl-Delay für alle Sites 10 Sekunden, und jede Umgebung auf einer wpengine.com-Adresse bekommt eine Datei, die alles sperrt, damit eine Site vor dem Launch nicht auf der falschen Domain indexiert wird. Nur Umgebungen mit einer eigenen Domain sehen Änderungen an der robots.txt. Eine physische Datei, die Sie hochladen, hat außerdem Vorrang vor einer Datei, die ein Plugin oder Theme erzeugt.

Mit den Worten des Anbieters (englisches Original): “This is what’s in the server’s default robots.txt file and can be overridden when you add a custom robots.txt file with one of the methods outlined in this article.”

Quelle: [WP Engine Support: Robots.txt and WordPress](https://wpengine.com/support/read-use-robots-txt/), gelesen am 24. Oktober 2026.

## Die Schritte

1. Erstellen Sie eine Datei mit dem Namen robots.txt. Der Name muss kleingeschrieben sein und die Endung .txt lauten, nicht .html.
2. Fügen Sie Ihre Anweisungen hinzu und speichern Sie. Für den Weg über ein Plugin nutzen Sie stattdessen Yoast SEO, Tools, dann Create robots.txt file.
3. Laden Sie die Datei per SFTP oder SSH Gateway in das Stammverzeichnis Ihrer Site hoch.
4. Öffnen Sie /robots.txt auf Ihrer aktiven eigenen Domain, um sie zu prüfen. Eine Kopie auf einer wpengine.com-Adresse zeigt Ihre Änderungen nicht.
5. Um einen Bot stattdessen auf dem Server abzuweisen, öffnen Sie im User Portal die Seite Sites, wählen die Umgebung aus, klicken im sekundären linken Menü auf Web Rules (möglicherweise müssen Sie Advanced aufklappen), wählen Access rules und klicken auf Add Rule.
6. Setzen Sie Action auf Deny, IP auf All und fügen Sie eine Bedingung hinzu mit Type Header, Name User-Agent, Operator Regex matches (~) und dem Namen des User-Agents als Value. Klicken Sie auf Add Rule, um zu speichern.

## Die passenden Zeilen

Zum Erlauben:

```
User-agent: OAI-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /
```

Zum Sperren:

```
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /
```

WP Engines Seite sagt, Werte von Anweisungen seien groß- und kleinschreibungsabhängig, und Globbing und reguläre Ausdrücke würden in der robots.txt nicht vollständig unterstützt.

## Stolperfallen

Die Seite nennt keine KI-Crawler: Ihre Beispiele verwenden BadBotName, Googlebot, bingbot und SEMrush. Sie sagt auch, Roboter müssten die robots.txt nicht befolgen, und empfiehlt eine Firewall wie Sucuri WAF oder Cloudflare oder die Kontaktaufnahme mit dem Support, um böswillige Akteure zu stoppen, bevor sie die Site erreichen. Laut der Seite zur Web Rules Engine erhält eine Anfrage, die eine Access rule der Web Rules abweist, die Antwort 403 Forbidden und zählt nicht zu den abrechenbaren Besuchen. Ihre eigene robots.txt überschreibt die Standarddatei, auch deren Crawl-Delay-Zeile mit 10 Sekunden. Fügen Sie also selbst eine Zeile Crawl-delay hinzu, wenn Sie eine behalten möchten.

## Vergleich mit WordPress.com

[WordPress.com](/de/platforms/wordpress-com): Ein KI-Opt-out in den Datenschutzeinstellungen statt einer robots.txt, die Sie selbst schreiben.

## Prüfen Sie Ihre eigene Website

Die kostenlose Prüfung im Feld oben liest die robots.txt für die KI-Crawler und sendet pro Crawler eine Live-Anfrage. So fällt eine Regel auf, die die Einstellungen Ihrer Plattform erlauben, eine Firewall aber ablehnt. Die vollständige Liste der Crawler finden Sie im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Warum ignoriert meine Staging-Site bei WP Engine meine robots.txt?

WP Engine sagt, Sites auf einer Adresse environment.wpengine.com bekämen automatisch eine robots.txt, die alles sperrt, und nur Umgebungen mit einer eigenen Domain sähen Änderungen an der Datei. Geteilte Konten können nur Production eine eigene Domain hinzufügen, deshalb zeigen Staging und Development Ihre Änderungen in der Regel nicht.

### Überschreibt ein robots.txt-Plugin eine Datei, die ich bei WP Engine hochlade?

Nein, es ist umgekehrt. WP Engine sagt, eine physische robots.txt im Stammverzeichnis Ihrer Site überschreibe jede dynamisch erzeugte Datei, die ein Plugin oder Theme erstellt.

## Sources

- [WP Engine Support: Robots.txt and WordPress](https://wpengine.com/support/read-use-robots-txt/), gelesen am 24. Oktober 2026
- [WP Engine Support: Web Rules Engine](https://wpengine.com/support/web-rules-engine/), gelesen am 24. Oktober 2026
