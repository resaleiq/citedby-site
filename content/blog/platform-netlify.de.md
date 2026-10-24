title: Netlify: KI-Crawler mit robots.txt und User Agent Blocker sperren
slug: netlify
description: Netlify hat keine robots.txt-Einstellung: Liefern Sie die Datei selbst aus oder nutzen Sie User Agent Blocker. Der Leitfaden rät zu beidem.
section: platforms
locale: de
cluster: KI-Crawler nach Plattform
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Vier Fakten zu Netlify: Wo robots.txt im Stammverzeichnis der Site, Sperre am Edge User Agent Blocker, Aktivierung Ein Projekt gleichzeitig, Zweite Stufe Edge Function
hero_sub: Einstellungen für KI-Crawler bei Netlify
hero_boxes: Wo|robots.txt im Stammverzeichnis der Site; Sperre am Edge|User Agent Blocker; Aktivierung|Ein Projekt gleichzeitig; Zweite Stufe|Edge Function
widget: on
related: /de/platforms|Alle Plattformen im Vergleich; /de/platforms/cloudflare|Cloudflare; /de/bots|KI-Crawler im Vergleich; /de/guides/cms|Checkliste für KI-Sichtbarkeit bei Shopify, WooCommerce und mehr
answer: Netlify bietet zwei Wege. Der eine ist eine robots.txt, die aus dem Stammverzeichnis Ihrer Site ausgeliefert wird. Der andere ist die Erweiterung User Agent Blocker, die mit einer Netlify Edge Function Anfragen nach User-Agent blockiert. Netlifys Entwicklerleitfaden sagt, die robots.txt allein genüge nicht, weil manche KI-Produkte sie ignorieren.

## Wo die Einstellung bei Netlify liegt

In den Dashboard-Seiten, die wir gelesen haben, gibt es keinen robots.txt-Editor. Netlifys Entwicklerleitfaden sagt, Sie sollen Ihre Regeln in einer robots.txt festlegen, die „aus dem Stammverzeichnis Ihrer Site ausgeliefert“ wird. Die separate Docs-Seite zum Blockieren von KI-Crawlern behandelt die Erweiterung User Agent Blocker. Nach der Installation finden Sie sie unter Extensions in der linken Navigation Ihres Projekts.

## Was nur Netlifys Seiten sagen und die anderer Plattformen nicht

Netlifys eigener Leitfaden behandelt die robots.txt als erste von zwei Schichten, nicht als die ganze Antwort. Er zeigt eine robots.txt mit je einem User-agent- und Disallow-Block pro Bot, erzeugt aus einer JSON-Liste von Namen. Dann fügt er eine Edge Function hinzu, die den User-Agent-Header jeder Anfrage mit derselben Liste vergleicht und bei einem Treffer HTTP 401 zurückgibt. Er sagt, manche KI-Produkte beachteten die robots.txt nicht, und ergänzt dann, dass auch die Prüfung des User-Agents eine eigene Lücke hat.

Mit den Worten des Anbieters (englisches Original): “Sadly, some bots have been found to mis-report their names in their User Agent strings, so we can’t rely on that technique alone either.”

Quelle: [Netlify Developers: Blocking AI bots and controlling crawlers](https://developers.netlify.com/guides/blocking-ai-bots-and-controlling-crawlers/), gelesen am 24. Oktober 2026.

## Die Schritte

1. Schreiben Sie eine robots.txt mit einer User-agent-Zeile und Disallow: / für jeden Bot, den Sie sperren möchten, und liefern Sie sie aus dem Stammverzeichnis Ihrer Site aus. Der Leitfaden erzeugt die Datei mit einem kleinen Build-Skript aus einer Liste von Namen, um Tippfehler zu vermeiden.
2. Deployen Sie die Site. Der Leitfaden merkt an, dass KI-Crawler die Datei beachten „sollten“. Deshalb fügt er eine zweite Schicht hinzu.
3. Für die Erweiterung: Wählen Sie im Netlify-Projekt-Dashboard in der linken Seitenleiste Extensions, suchen Sie nach User Agent Blocker, wählen Sie sie aus und wählen Sie Install. Damit steht sie für alle Projekte in Ihrem Netlify-Team zur Verfügung.
4. Gehen Sie zu dem Projekt, in dem sie aktiv sein soll. Sie können die Erweiterung nur für ein Projekt gleichzeitig aktivieren. Wählen Sie unter Extensions in der linken Navigation User Agent Blocker.
5. Wählen Sie unter Block User Agents den Traffic aus, der blockiert werden soll. Um KI-Crawler und Bots anzusprechen, wählen Sie alle KI-Crawler-Optionen.
6. Wählen Sie Redeploy site und bestätigen Sie mit Save. Wählen Sie dann Enable analytics and deploy site. Netlify sagt, dass das Blockieren sofort greift, sobald das Deployment erfolgreich ist.

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

Netlifys Seiten zeigen nur Disallow-Regeln. Die Allow-Zeilen oben sind Standard-robots.txt, nichts, was Netlify dokumentiert.

## Stolperfallen

Netlify sagt, die voreingestellte Liste der Erweiterung „enthält nicht alle möglichen KI-Crawler und KI-Bots“. Ein Crawler, der in der Liste fehlt, wird also nicht blockiert. Dieselbe Seite führt neben den KI-Crawlern auch SEO- und Suchmaschinen-Crawler auf. Wählen Sie daher nur die KI-Optionen aus, wenn Sie weiterhin Traffic aus der Suche wollen. Die Beispiel-Edge-Function des Leitfadens antwortet auf jede passende Anfrage mit einem 401, auf der gesamten Site.

## Vergleich mit Cloudflare

[Cloudflare](/de/platforms/cloudflare): Ein Schalter auf Netzwerkebene, der unabhängig von der Plattform der Site funktioniert, während Netlifys Erweiterung pro Projekt gilt.

## Prüfen Sie Ihre eigene Website

Die kostenlose Prüfung im Feld oben liest die robots.txt für die KI-Crawler und sendet pro Crawler eine Live-Anfrage. So fällt eine Regel auf, die die Einstellungen Ihrer Plattform erlauben, eine Firewall aber ablehnt. Die vollständige Liste der Crawler finden Sie im [KI-Crawler-Verzeichnis](/de/bots).

## FAQ

### Genügt die robots.txt, um KI-Bots bei Netlify zu sperren?

Netlifys Leitfaden sagt nein. Er sagt, nicht alle KI-Produkte beachteten die robots.txt, und empfiehlt, eine Edge Function oder die Erweiterung User Agent Blocker hinzuzufügen, die nach User-Agent blockiert. Er sagt auch, dass manche Bots ihren User-Agent falsch angeben. Seine Antwort sind also beide Schichten zusammen.

### Kann ich den User Agent Blocker für alle Projekte auf einmal einschalten?

Laut Netlifys Docs nicht. Die Installation macht die Erweiterung für alle Projekte in Ihrem Team verfügbar, aktivieren können Sie sie aber nur für ein Projekt gleichzeitig.

## Sources

- [Netlify Developers: Blocking AI bots and controlling crawlers](https://developers.netlify.com/guides/blocking-ai-bots-and-controlling-crawlers/), gelesen am 24. Oktober 2026
- [Netlify Docs: Block AI crawlers and bots](https://docs.netlify.com/build/build-with-ai/block-ai-crawlers), gelesen am 24. Oktober 2026
