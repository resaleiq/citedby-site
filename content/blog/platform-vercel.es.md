title: Vercel: el conjunto de reglas AI Bots del Firewall (Log o Deny)
slug: vercel
description: Vercel bloquea los bots de IA con un conjunto de reglas del Firewall, no con robots.txt. Dónde está, las acciones Log y Deny y su lista autoactualizada.
section: platforms
locale: es
cluster: Rastreadores de IA por plataforma
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre Vercel: Dónde Firewall, Rules, Planes Todos los planes, Por defecto Allow (inactivo), Acciones Log o Deny
hero_sub: Ajustes de rastreadores de IA en Vercel
hero_boxes: Dónde|Firewall, Rules; Planes|Todos los planes; Por defecto|Allow (inactivo); Acciones|Log o Deny
widget: on
related: /es/platforms|Todas las plataformas comparadas; /es/platforms/cloudflare|Cloudflare; /es/bots|Rastreadores de IA comparados; /es/guides/cms|Lista de comprobación de visibilidad en IA para Shopify, WooCommerce y más
answer: Vercel gestiona los bots de IA con un conjunto de reglas del Firewall, no con una línea de robots.txt. En tu proyecto abre Firewall, luego Rules, y pon AI Bots Ruleset en Log o Deny. Está disponible en todos los planes y empieza inactivo, mostrado como Allow, así que no se bloquea nada hasta que lo cambies.

## Dónde está el ajuste en Vercel

Desde el panel de tu proyecto, abre Firewall en la barra lateral y luego Rules. En la sección Bot Management encontrarás la regla AI Bots Ruleset. La documentación de Vercel dice que el conjunto de reglas está disponible en todos los planes.

## Lo que solo dice la página de Vercel y no las de otras plataformas

La lista de bots de IA de Vercel no te toca mantenerla a ti. El conjunto de reglas cubre los bots de IA que rastrean para obtener datos de entrenamiento, para búsqueda o para obtener páginas a petición de usuarios, y Vercel mantiene la lista al día. La misma página dice que el conjunto de reglas está inactivo por defecto y etiquetado como Allow en el panel, así que el tráfico coincidente no se evalúa y llega a tu aplicación. El control es una única acción para todo el conjunto de reglas, Log o Deny, aplicada en el Firewall.

En palabras del proveedor (original en inglés): “When new AI bots emerge, Vercel automatically adds them to its managed list and handles them according to your existing configured action without requiring any changes on your part.”

Fuente: [Vercel Docs: Bot Management](https://vercel.com/docs/bot-management), leído el 24 de octubre de 2026.

## Los pasos

1. Desde el panel de tu proyecto, abre Firewall en la barra lateral.
2. Abre Rules en la barra lateral.
3. En la sección Bot Management, selecciona Log o Deny en la regla AI Bots Ruleset. Log registra el tráfico de bots de IA sin bloquearlo y sirve para monitorizar. Deny bloquea todo el tráfico identificado como procedente de bots de IA.
4. Cuando haces un cambio, aparece un botón Review Changes con el número de cambios. Selecciona Review Changes, revísalos y luego selecciona Publish para aplicar los cambios a tu despliegue de producción.

## Las líneas que debes usar

Las páginas de Vercel lo describen como un ajuste del Firewall, así que no hay ninguna línea de robots.txt que añadir. Los dos estados son:

Para permitir:

```
AI Bots Ruleset: Allow (the default, ruleset inactive)
```

Para bloquear:

```
AI Bots Ruleset: Deny
```

## Cosas a tener en cuenta

Deny bloquea todo el tráfico identificado como procedente de bots de IA, y el alcance del conjunto de reglas abarca juntos el entrenamiento, la búsqueda y la obtención de páginas a petición de usuarios, así que no sirve para bloquear los bots de entrenamiento y mantener los de búsqueda. Log es el primer paso más seguro. La página de Vercel no dice cómo se relaciona el conjunto de reglas con tu robots.txt, así que revisa por separado qué dice tu propio archivo. Para bots concretos, la misma página dice que puedes bloquear algunos o todos los bots de su directorio de bots verificados con reglas personalizadas de WAF que usen la condición de coincidencia User Agent o la cabecera Signature-Agent.

## Compara con Cloudflare

[Cloudflare](/es/platforms/cloudflare): también es un interruptor a nivel de red, con tres acciones para cada uno de Search, Agent y Training.

## Comprueba tu propio sitio

La comprobación gratuita del cuadro de arriba lee robots.txt para los rastreadores de IA y envía una petición real por rastreador, así que aparece cualquier regla que los ajustes de tu plataforma permiten pero que un cortafuegos rechaza. La lista completa de rastreadores está en [el centro de rastreadores de IA](/es/bots).

## FAQ

### ¿Vercel bloquea los bots de IA por defecto?

No. La documentación de Vercel dice que AI Bots Ruleset está inactivo por defecto, etiquetado como Allow en el panel, y que el tráfico coincidente no se evalúa y llega a tu aplicación.

### ¿Tengo que mantener al día la lista de bots de IA de Vercel?

No. Vercel dice que la lista de bots de IA conocidos la mantiene y actualiza automáticamente Vercel, y que los bots nuevos se tratan según la acción que ya hayas establecido.

## Sources

- [Vercel Docs: Bot Management](https://vercel.com/docs/bot-management), leído el 24 de octubre de 2026
- [Vercel Docs: WAF Managed Rulesets](https://vercel.com/docs/vercel-firewall/vercel-waf/managed-rulesets), leído el 24 de octubre de 2026
