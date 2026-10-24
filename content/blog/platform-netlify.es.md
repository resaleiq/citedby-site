title: Netlify: robots.txt y User Agent Blocker contra bots de IA
slug: netlify
description: Netlify no tiene ajuste de robots.txt: sirve un archivo desde la raíz del sitio o instala la extensión User Agent Blocker. Su guía dice que uses ambos.
section: platforms
locale: es
cluster: Rastreadores de IA por plataforma
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre Netlify: Dónde robots.txt en la raíz del sitio, Bloqueo en el edge User Agent Blocker, Activación Un proyecto a la vez, Respaldo Edge Function
hero_sub: Ajustes de rastreadores de IA en Netlify
hero_boxes: Dónde|robots.txt en la raíz del sitio; Bloqueo en el edge|User Agent Blocker; Activación|Un proyecto a la vez; Respaldo|Edge Function
widget: on
related: /es/platforms|Todas las plataformas comparadas; /es/platforms/cloudflare|Cloudflare; /es/bots|Rastreadores de IA comparados; /es/guides/cms|Lista de comprobación de visibilidad en IA para Shopify, WooCommerce y más
answer: Netlify te ofrece dos vías. Una es un archivo robots.txt servido desde la raíz de tu sitio. La otra es la extensión User Agent Blocker, que usa una Netlify Edge Function para bloquear peticiones según el agente de usuario. La guía para desarrolladores de Netlify dice que robots.txt no basta por sí solo, porque algunos productos de IA lo ignoran.

## Dónde está el ajuste en Netlify

En las páginas del panel que hemos leído no hay ningún editor de robots.txt. La guía para desarrolladores de Netlify dice que declares tus reglas en un archivo robots.txt «servido desde la raíz de tu sitio». La página de documentación aparte sobre cómo bloquear rastreadores de IA trata la extensión User Agent Blocker, que, una vez instalada, encuentras en Extensions en la navegación izquierda de tu proyecto.

## Lo que solo dicen las páginas de Netlify y no las de otras plataformas

La propia guía de Netlify trata robots.txt como la primera de dos capas, no como la respuesta completa. Muestra un robots.txt con un bloque User-agent y Disallow por bot, generado a partir de una lista de nombres en JSON, y luego añade una Edge Function que compara la cabecera User-Agent de cada petición con la misma lista y devuelve un HTTP 401 si coincide. Dice que algunos productos de IA no respetan robots.txt y después añade que la comprobación del agente de usuario tiene su propio fallo.

En palabras del proveedor (original en inglés): “Sadly, some bots have been found to mis-report their names in their User Agent strings, so we can’t rely on that technique alone either.”

Fuente: [Netlify Developers: Blocking AI bots and controlling crawlers](https://developers.netlify.com/guides/blocking-ai-bots-and-controlling-crawlers/), leído el 24 de octubre de 2026.

## Los pasos

1. Escribe un robots.txt con una línea User-agent y Disallow: / para cada bot que quieras bloquear, y sírvelo desde la raíz de tu sitio. La guía genera el archivo a partir de una lista de nombres con un pequeño script de compilación, para evitar erratas.
2. Despliega el sitio. La guía señala que los rastreadores de IA «deberían» respetar el archivo, y por eso añade una segunda capa.
3. Para la extensión: en el panel de tu proyecto de Netlify selecciona Extensions en la barra lateral izquierda, busca User Agent Blocker, selecciónala y selecciona Install. Así queda disponible para todos los proyectos de tu equipo de Netlify.
4. Ve al proyecto en el que quieras tenerla activa. Solo puedes activar la extensión para un proyecto a la vez. En Extensions, en la navegación izquierda, selecciona User Agent Blocker.
5. En Block User Agents, selecciona el tráfico que quieres bloquear. Para apuntar a los rastreadores y bots de IA, selecciona todas las opciones de rastreadores de IA.
6. Selecciona Redeploy site y confirma con Save, y después selecciona Enable analytics and deploy site. Netlify dice que el bloqueo empieza a funcionar de inmediato cuando el despliegue se completa con éxito.

## Las líneas que debes usar

Para permitir:

```
User-agent: OAI-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /
```

Para bloquear:

```
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /
```

Las páginas de Netlify solo muestran reglas Disallow. Las líneas Allow de arriba son robots.txt estándar, no algo que Netlify documente.

## Cosas a tener en cuenta

Netlify dice que la lista predefinida de la extensión «no incluye todos los posibles rastreadores y bots de IA», así que un rastreador que falte en la lista no queda bloqueado. La misma página enumera rastreadores de SEO y de búsqueda junto a los de IA, así que selecciona solo las opciones de IA si aún quieres tráfico de búsqueda. La Edge Function de ejemplo de la guía responde con un 401 a cada petición que coincide, en todo el sitio.

## Compara con Cloudflare

[Cloudflare](/es/platforms/cloudflare): un interruptor a nivel de red que funciona sea cual sea la plataforma del sitio, mientras que la extensión de Netlify es por proyecto.

## Comprueba tu propio sitio

La comprobación gratuita del cuadro de arriba lee robots.txt para los rastreadores de IA y envía una petición real por rastreador, así que aparece cualquier regla que los ajustes de tu plataforma permiten pero que un cortafuegos rechaza. La lista completa de rastreadores está en [el centro de rastreadores de IA](/es/bots).

## FAQ

### ¿Basta robots.txt para bloquear bots de IA en Netlify?

La guía de Netlify dice que no. Dice que no todos los productos de IA respetan robots.txt y recomienda añadir una Edge Function, o la extensión User Agent Blocker, que bloquee por agente de usuario. También dice que algunos bots informan mal de su agente de usuario, así que su respuesta son las dos capas juntas.

### ¿Puedo activar User Agent Blocker en todos los proyectos a la vez?

Según la documentación de Netlify, no. Al instalarla, la extensión queda disponible para todos los proyectos de tu equipo, pero solo puedes activarla en un proyecto a la vez.

## Sources

- [Netlify Developers: Blocking AI bots and controlling crawlers](https://developers.netlify.com/guides/blocking-ai-bots-and-controlling-crawlers/), leído el 24 de octubre de 2026
- [Netlify Docs: Block AI crawlers and bots](https://docs.netlify.com/build/build-with-ai/block-ai-crawlers), leído el 24 de octubre de 2026
