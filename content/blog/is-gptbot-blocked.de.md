title: Ist GPTBot auf meiner Website blockiert? So prüfen Sie es
h1: Ist GPTBot auf Ihrer Website blockiert? So finden Sie es heraus
description: GPTBot kann an vier Stellen gestoppt werden, nicht nur in der robots.txt. Prüfen Sie jede Ebene mit dem Zwei-Anfragen-Test, Logs und Ihrem CDN.
slug: is-gptbot-blocked
locale: de
cluster: Crawler-Zugang
date: 2026-10-20
reviewed: 2026-10-20
widget: on
howto: on
related: /de/tools/ai-crawler-check|KI-Crawler-Zugriffscheck (free); /de/blog/can-chatgpt-read-my-website|Kann ChatGPT meine Website lesen?; /de/guides/technical-seo-checklist|Technische SEO-Checkliste für KI-Sichtbarkeit; /de/blog/does-llms-txt-work|Bringt llms.txt etwas?
hero: auto
hero_alt: Titelkarte zu GPTBot mit vier Ebenen, auf denen der Crawler gestoppt werden kann: robots.txt, CDN, Sicherheits-Plugin oder Firewall und Servereinstellung
hero_sub: Vier Ebenen, vier Tests
hero_boxes: robots.txt|Disallow-Regel;CDN|zum Beispiel Cloudflare;Firewall|Plugin oder WAF-Regel;Server|Regel im Webserver
steps_img: on
answer: GPTBot ist auf Ihrer Website blockiert, wenn die robots.txt eine passende Disallow-Regel enthält oder ein CDN, eine Firewall oder eine Serverregel seine Anfragen abweist. Öffnen Sie ihre-domain.de/robots.txt, starten Sie ein Audit und vergleichen Sie zwei Anfragen an Ihren Server. Ein gesperrter GPTBot sperrt nicht automatisch die ChatGPT-Suche.

## An welchen vier Stellen kann GPTBot gestoppt werden?

GPTBot ist der Crawler, mit dem OpenAI nach eigener Angabe Inhalte sammelt, die zum Training seiner Modelle dienen können. Eine Anfrage von ihm kann auf vier Ebenen abgewiesen werden, und jede braucht einen eigenen Test. Das CitedBy-Audit im Kasten oben deckt die erste ab. Die anderen drei antworten mit einem Fehlercode, auch wenn die robots.txt alles erlaubt.

- robots.txt: eine Disallow-Regel für GPTBot oder für alle Crawler.
- CDN: eine Bot-Einstellung bei Ihrem Content-Delivery-Anbieter, zum Beispiel Cloudflare.
- Sicherheits-Plugin oder Firewall: eine WAF-Regel, die Bots nach Namen oder Verhalten sperrt.
- Webserver: eine Regel in der Server-Konfiguration, die bestimmte User-Agents abweist.

Die Ebenen 2 bis 4 sieht man in der robots.txt nicht. Prüfen Sie sie getrennt.

## Wie prüfen Sie das Schritt für Schritt?

1. robots.txt lesen: Öffnen Sie `ihr-shop.de/robots.txt` im Browser und suchen Sie eine Gruppe mit `GPTBot`. Gibt es keine, folgt GPTBot der Gruppe `User-agent: *`. Ein pauschales `Disallow: /` darunter sperrt ihn also mit ([RFC 9309](https://www.rfc-editor.org/rfc/rfc9309)).
2. Audit starten: Das Audit (ab 9 €) liest die robots.txt für GPTBot, OAI-SearchBot, PerplexityBot, Google-Extended und Bingbot und nennt die gesperrten.
3. Zwei Anfragen vergleichen: Senden Sie zwei Anfragen an Ihre Startseite, eine normale und eine mit dem GPTBot-User-Agent, und vergleichen Sie die Statuscodes. Die Befehle stehen unten.
4. CDN und Firewall prüfen: Schauen Sie in den KI-Crawler-Einstellungen Ihres CDN nach, und suchen Sie in der Regelliste Ihres Sicherheits-Plugins nach `GPTBot`, `bot`, `AI` und `crawler`.
5. Server-Logs durchsuchen: Suchen Sie nach `GPTBot`. Viele 403-Antworten auf seine Anfragen sind das Zeichen für eine Sperre, die die robots.txt nicht zeigt.

## Wie funktioniert der Zwei-Anfragen-Test?

Ersetzen Sie `ihr-shop.de` durch Ihre Adresse. Der erste Befehl sendet eine normale Anfrage, der zweite den GPTBot-User-Agent, den OpenAI veröffentlicht. Beide geben nur den Statuscode aus.

```
curl -s -o /dev/null -w "%{http_code}\n" https://ihr-shop.de/
curl -s -o /dev/null -w "%{http_code}\n" -A "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.4; +https://openai.com/gptbot" https://ihr-shop.de/
```

Liefert nur die zweite Anfrage einen 403-Fehler, zielt eine Regel auf den Namen des Crawlers.

Der Test läuft von Ihrem eigenen Rechner aus. Beurteilt Ihr Hoster Crawler zusätzlich nach IP-Adresse, kann der echte GPTBot eine andere Antwort bekommen als Sie. OpenAI veröffentlicht die IP-Bereiche unter `openai.com/gptbot.json`. In Ihren Logs sehen Sie, ob Anfragen aus diesen Bereichen durchkamen ([OpenAI-Dokumentation zu Crawlern](https://developers.openai.com/api/docs/bots)).

## Wo stellen Sie das bei Cloudflare ein?

Laut Cloudflare-Dokumentation öffnen Sie Ihre Domain, gehen zu AI Crawl Control, dann zum Tab Security und dort zu Crawlers. In der Spalte Actions legen Sie pro Crawler Allow oder Block fest. Block erstellt oder aktualisiert eine WAF-Regel, und bei Allow können Sie die robots.txt weiterhin durchsetzen ([Cloudflare: AI-Crawler verwalten](https://developers.cloudflare.com/ai-crawl-control/features/manage-ai-crawlers/)).

Auch die Standardwerte ändern sich. Laut Help Net Security blockieren neue Domains ab dem 15. September 2026 standardmäßig Training- und Agent-Crawler auf Seiten mit Werbung, Suchcrawler bleiben erlaubt ([Help Net Security](https://www.helpnetsecurity.com/2026/07/02/cloudflare-ai-crawler-controls/)). Schauen Sie in Ihr eigenes Dashboard, statt den Standard anzunehmen.

## Was bedeutet es, wenn die Prüfung eine Abweisung meldet?

Auch eine einfache Anfrage unserer Prüfung kann abgewiesen werden. Bei HTTP 403, 429 oder 503 sagt die Prüfung das und weist darauf hin, dass sie von außen nicht erkennen kann, ob KI-Crawler ebenfalls abgewiesen werden. Ein 403 bedeutet meist, dass eine Regel die Anfrage sperrt. Ein 429 oder 503 kann auch auf Rate-Limiting oder einen Ausfall hindeuten, der jeden Besucher trifft. Beheben Sie die Ursache in CDN, Firewall oder Hosting-Oberfläche und prüfen Sie erneut.

## Sollten Sie GPTBot freigeben?

Das entscheiden Sie, und eine Sperre ist eine legitime Wahl. OpenAI führt GPTBot, OAI-SearchBot und ChatGPT-User als getrennte Crawler mit getrennten Aufgaben. GPTBot sammelt Trainingsdaten. OAI-SearchBot bringt Websites in die Suchfunktionen von ChatGPT. ChatGPT-User ruft Seiten ab, wenn eine Person danach fragt.

| Ihr Ziel | Was Sie tun |
| --- | --- |
| In ChatGPT-Suchergebnissen erscheinen, Inhalte aus dem Training heraushalten | `OAI-SearchBot` erlauben, `GPTBot` sperren |
| In der Suche erscheinen und Training erlauben | Beide erlauben |
| Aus beidem heraushalten | Beide sperren und in den Logs auf ChatGPT-User achten |

Eine Änderung der robots.txt kann laut OpenAI etwa 24 Stunden brauchen, bis sie bei OAI-SearchBot ankommt.

## FAQ

### Entfernt die GPTBot-Sperre meinen Shop aus ChatGPT?
Nicht von allein. OpenAI beschreibt OAI-SearchBot als Crawler für die Suchfunktionen von ChatGPT und GPTBot als Trainings-Crawler. Beide werden in der robots.txt getrennt gesteuert.

### Warum sieht die robots.txt gut aus, und GPTBot bekommt trotzdem einen 403?
Die robots.txt ist eine Bitte an den Crawler. Ein CDN, eine Firewall oder eine Serverregel kann die Anfrage trotzdem abweisen. Prüfen Sie diese Ebenen mit dem Zwei-Anfragen-Test und Ihren Logs.

### Befolgt ChatGPT-User die robots.txt?
OpenAI schreibt, dass robots.txt-Regeln für ChatGPT-User eventuell nicht gelten, weil eine Person die Anfrage auslöst.

### Wird mein Shop empfohlen, wenn ich GPTBot freigebe?
Nein. Lesbar zu sein ist die Eintrittskarte. Ob ein Assistent Ihren Shop nennt, hängt davon ab, was er zu Ihrer Kategorie findet. Das misst das CitedBy-Audit mit echten Käuferfragen.

## Sources

- [OpenAI: Crawler und User-Agents, IP-Bereiche](https://developers.openai.com/api/docs/bots)
- [Cloudflare: AI-Crawler verwalten](https://developers.cloudflare.com/ai-crawl-control/features/manage-ai-crawlers/)
- [Help Net Security: Cloudflare ändert Zugriffsregeln für KI-Crawler, 2. Juli 2026](https://www.helpnetsecurity.com/2026/07/02/cloudflare-ai-crawler-controls/)
- [IETF RFC 9309: Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309)
- [CitedBy Website-Audit](https://citedby.eu/de)
