title: Webflow: robots.txt y la cabecera Content-Signal para la IA
slug: webflow
description: Dónde está el editor de robots.txt de Webflow, qué plan necesita y cómo su cabecera Content-Signal separa entrenamiento de IA, búsqueda y entrada de IA.
section: platforms
locale: es
cluster: Rastreadores de IA por plataforma
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Cuatro datos sobre Webflow: Dónde Site settings, SEO, Requiere Plan Site o Workspace de pago, Extra Content-Signal, Estado Extensión propuesta
hero_sub: Ajustes de rastreadores de IA en Webflow
hero_boxes: Dónde|Site settings, SEO; Requiere|Plan Site o Workspace de pago; Extra|Content-Signal; Estado|Extensión propuesta
widget: on
related: /es/platforms|Todas las plataformas comparadas; /es/platforms/wix|Wix; /es/bots|Rastreadores de IA comparados; /es/guides/cms|Lista de comprobación de visibilidad en IA para Shopify, WooCommerce y más
answer: Webflow pone robots.txt en Site settings, luego SEO y luego Indexing, y una de sus páginas de ayuda dice que necesitas un plan Site o un plan Workspace de pago. También puede enviar una cabecera Content-Signal que establece por separado ai-train, search y ai-input. Webflow la llama extensión propuesta, no un estándar aceptado.

## Dónde está el ajuste en Webflow

Ve a Site settings, luego a SEO y después a Indexing, añade la regla o reglas de robots.txt que quieras, haz clic en Save y publica tu sitio. Webflow añade por defecto una línea de sitemap; un interruptor la quita.

## Una cabecera que separa entrenamiento, búsqueda y respuestas de IA

Además de robots.txt, la página de Webflow dice que un sitio puede servir una cabecera HTTP Content-Signal, que se configura en la misma zona de Indexing, para dar instrucciones más detalladas a los rastreadores de IA. Su ejemplo es `Content-Signal: ai-train=no, search=yes, ai-input=no`. Webflow explica la separación: robots.txt controla si los bots pueden acceder a tus páginas, mientras que Content-Signal indica, por separado, si el contenido se puede usar para entrenar IA, para indexar en buscadores o para respuestas generadas por IA. Webflow añade él mismo la salvedad: se basa en una extensión propuesta de la RFC 9309 y todavía no es un estándar aceptado. Es decir, expresa una preferencia; no detiene a un rastreador, y la página de Webflow no dice qué rastreadores la leen.

En palabras del proveedor (original en inglés): “This is based on a proposed extension to RFC 9309 and is not yet an accepted standard.”

Fuente: [Webflow Help: Set robots.txt rules](https://help.webflow.com/hc/en-us/articles/41954080897683-Set-robots-txt-rules), leído el 21 de octubre de 2026.

## Los pasos

1. Abre Site settings y ve a SEO, luego a Indexing.
2. Escribe en el campo de reglas las reglas de robots.txt que quieras.
3. Si quieres, configura la cabecera Content-Signal en la misma zona.
4. Haz clic en Save y publica tu sitio, y luego abre tudominio.com/robots.txt para comprobar el archivo activo.

## Las líneas que debes usar

Para permitir:

```
User-agent: OAI-SearchBot
Allow: /

User-agent: *
Allow: /
```

Para bloquear:

```
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

Content-Signal: ai-train=no, search=yes, ai-input=no
```

## Cosas a tener en cuenta

La página de Webflow dice que tu robots.txt es visible públicamente, así que no cuentes con él para ocultar páginas privadas, y que no todos los bots lo siguen.

## Compara con Wix

[Wix](/es/platforms/wix): una ruta de edición más larga y un ejemplo con cuatro nombres.

## Comprueba tu propio sitio

La comprobación gratuita del cuadro de arriba lee robots.txt para los rastreadores de IA y envía una petición real por rastreador, así que aparece cualquier regla que los ajustes de tu plataforma permiten pero que un cortafuegos rechaza. La lista completa de rastreadores está en [el centro de rastreadores de IA](/es/bots).

## FAQ

### ¿Necesito un plan de pago para robots.txt en Webflow?

Una página de ayuda de Webflow dice que necesitas un plan Site o un plan Workspace de pago para añadir un archivo robots.txt a tu sitio.

### ¿Qué es Content-Signal?

Una extensión propuesta de la RFC 9309 que Webflow puede enviar como cabecera: ai-train, search y ai-input, cada uno establecido en yes o no.

### ¿Webflow bloquea por mí a los bots malos?

Su página de ayuda muestra cómo escribir una regla para un bot con nombre. Dice que algunos bots, sobre todo los maliciosos, no siguen robots.txt.

## Sources

- [Webflow Help: Set robots.txt rules](https://help.webflow.com/hc/en-us/articles/41954080897683-Set-robots-txt-rules), leído el 21 de octubre de 2026
- [Webflow Help: Request to block specific bots from visiting your site](https://help.webflow.com/hc/en-us/articles/41954183592851-Request-to-block-specific-bots-from-visiting-your-site), leído el 21 de octubre de 2026
