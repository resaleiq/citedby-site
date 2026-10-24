title: Cloudflare: políticas para bots de IA de Search, Agent y Training
slug: cloudflare
description: Block AI Bots de Cloudflare divide los bots de IA en Search, Agent y Training, con tres opciones. Nuevos valores por defecto desde el 15 sept. 2026.
section: platforms
locale: es
cluster: Rastreadores de IA por plataforma
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Cuatro datos sobre Cloudflare: Dónde Security Settings, Comportamientos Search, Agent, Training, Opciones 3 por comportamiento, Página actualizada 1 jul 2026
hero_sub: Ajustes de rastreadores de IA en Cloudflare
hero_boxes: Dónde|Security Settings; Comportamientos|Search, Agent, Training; Opciones|3 por comportamiento; Página actualizada|1 jul 2026
widget: on
related: /es/platforms|Todas las plataformas comparadas; /es/platforms/shopify|Shopify; /es/bots|Rastreadores de IA comparados; /es/guides/cms|Lista de comprobación de visibilidad en IA para Shopify, WooCommerce y más
answer: Cloudflare clasifica los bots de IA en tres comportamientos: Search, Agent y Training. Para cada uno eliges Block on all pages, Block on pages with ads o Allow, en Security Settings, Configure AI bot policies. Su página, actualizada el 1 de julio de 2026, dice que los nuevos valores para dominios nuevos empiezan el 15 de septiembre de 2026.

## Dónde está el ajuste en Cloudflare

En el panel de Cloudflare ve a Security Settings y luego a Configure AI bot policies. Cada uno de los tres comportamientos tiene su propio ajuste. Funciona a nivel de red, así que se aplica sea cual sea la plataforma en la que funcione el sitio.

## Tres comportamientos, tres opciones y una fecha que ya ha pasado

Los ajustes preestablecidos de Cloudflare son estos: Search, rastreadores que recogen o indexan tu contenido para responder preguntas sobre él más adelante; Agent, actividad automatizada que actúa en tiempo real en nombre de una persona, como los bots de chat que obtienen páginas y los agentes que usan el navegador; Training, rastreadores que toman tu contenido para entrenar o ajustar un modelo, incluidos los rastreadores de uso mixto que sirven tanto para Training como para Search. Cada ajuste bloquea los bots verificados clasificados así, además de algunos bots no verificados que se comportan de forma parecida. La página, actualizada por última vez el 1 de julio de 2026, anuncia nuevos valores por defecto para dominios nuevos desde el 15 de septiembre de 2026: bots de Training y Agent bloqueados en las páginas que muestran anuncios, Search sigue permitido, y los rastreadores de uso mixto bloqueados por toda configuración que bloquee el entrenamiento de IA, incluida la opción heredada Block AI bots, que marca como obsoleta en esa fecha. La página seguía en futuro cuando la leímos el 21 de octubre, cinco semanas después de esa fecha, así que abre tu propio panel y mira qué está activado en lugar de fiarte de uno u otro texto.

En palabras del proveedor (original en inglés): “Search: crawlers that collect or index your content to answer questions about it later.”

Fuente: [Cloudflare Docs: Block AI Bots](https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/), leído el 21 de octubre de 2026.

## Los pasos

1. Abre tu zona en el panel de Cloudflare y ve a Security Settings.
2. Abre Configure AI bot policies.
3. Para Search, Agent y Training elige Block on all pages, Block on pages with ads o Allow.
4. Si usas la opción heredada Block AI bots, comprueba qué rastreadores de uso mixto cubre ahora, porque Cloudflare dice que quedará obsoleta.
5. Haz la prueba con el [comprobador gratuito de acceso de rastreadores de IA](/es/tools/ai-crawler-check): un bot que robots.txt permite puede ser rechazado aquí.

## Las líneas que debes usar

Para permitir:

```
# Cloudflare settings are not robots.txt lines.
# Choose Allow (do not block) for Search so answer engines can fetch pages.
```

Para bloquear:

```
# Cloudflare settings are not robots.txt lines.
# Choose Block (on all pages) for Training; leave Search on Allow.
```

## Cosas a tener en cuenta

El riesgo para una tienda que quiere citas está en el ajuste intermedio: Cloudflare define Agent como bots de chat que obtienen páginas en nombre de una persona, que es el trabajo de herramientas como [ChatGPT-User](/es/bots/chatgpt-user). Bloquear Agent puede impedir que un asistente abra tu página cuando alguien pregunta por ella, aunque tu robots.txt lo permita. Ten en cuenta también que Shopify dice que no recomienda una configuración de proxy delante de una tienda Shopify.

## Compara con Shopify

[Shopify](/es/platforms/shopify): dice que gestiona él mismo la administración de bots y desaconseja usar un proxy.

## Comprueba tu propio sitio

La comprobación gratuita del cuadro de arriba lee robots.txt para los rastreadores de IA y envía una petición real por rastreador, así que aparece cualquier regla que los ajustes de tu plataforma permiten pero que un cortafuegos rechaza. La lista completa de rastreadores está en [el centro de rastreadores de IA](/es/bots).

## FAQ

### ¿El bloqueo de IA de Cloudflare anula robots.txt?

La página de Cloudflare describe un bloqueo por comportamiento en su red, así que un bot puede ser rechazado ahí aunque tu robots.txt lo permita. Por eso importa una prueba con una petición real.

### ¿Qué diferencia hay entre Search y Training en Cloudflare?

Los rastreadores de Search indexan contenido para responder preguntas más adelante; los de Training toman contenido para entrenar o ajustar un modelo. Los rastreadores de uso mixto se clasifican como Training.

### ¿Block AI bots sigue disponible?

Cloudflare lo marca como obsoleto el 15 de septiembre de 2026. Su página seguía escrita en futuro cuando la leímos el 21 de octubre de 2026.

## Sources

- [Cloudflare Docs: Block AI Bots](https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/), leído el 21 de octubre de 2026
