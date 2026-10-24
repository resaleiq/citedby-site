title: WordPress.com: la IA se excluye en privacidad, no en robots.txt
slug: wordpress-com
description: WordPress.com trata la exclusión de la IA como «Prevent third-party sharing» en privacidad. Qué dice su guía de visibilidad, revisada el 5 de octubre de 2026.
section: platforms
locale: es
cluster: Rastreadores de IA por plataforma
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Cuatro datos sobre WordPress.com: Dónde Privacy settings, No es Una edición de robots.txt, Guía revisada 5 oct 2026, También Acceso de agentes por MCP
hero_sub: Ajustes de rastreadores de IA en WordPress.com
hero_boxes: Dónde|Privacy settings; No es|Una edición de robots.txt; Guía revisada|5 oct 2026; También|Acceso de agentes por MCP
widget: on
related: /es/platforms|Todas las plataformas comparadas; /es/platforms/cloudflare|Cloudflare; /es/bots|Rastreadores de IA comparados; /es/guides/cms|Lista de comprobación de visibilidad en IA para Shopify, WooCommerce y más
answer: En WordPress.com, la exclusión de la IA es un ajuste de privacidad y no una edición de robots.txt. Su guía de visibilidad del sitio, revisada por última vez el 5 de octubre de 2026, dice que, para excluirte de compartir tu contenido público con terceros, incluidos los modelos de IA, sigas su guía Prevent third-party sharing.

## Dónde está el ajuste en WordPress.com

La guía de visibilidad de WordPress.com te envía a Settings, luego a Reading, para Site Visibility (Public, Coming Soon o Private), y a una guía aparte, Prevent third-party sharing, para la exclusión de la IA.

## Aquí, excluirse de la IA es un ajuste de uso compartido

La guía de WordPress.com sobre cómo controlar la visibilidad de tu sitio dice: para excluirte de compartir el contenido público de tu sitio con terceros (incluidos los modelos de IA), visita la guía Prevent third-party sharing. Es un ajuste de la plataforma, independiente del robots.txt que leen los rastreadores de búsqueda y de IA. La misma página, revisada por última vez el 5 de octubre de 2026, describe también el sentido contrario: puedes conectar agentes de IA externos, como ChatGPT o Claude, para que lean y editen los ajustes de visibilidad de tu sitio activando el acceso a herramientas por MCP. El 21 de octubre no pudimos leer el cuerpo de la guía Prevent third-party sharing: la página cargaba con su título y una fecha de revisión del 1 de agosto de 2024, pero sin pasos, tanto con una petición simple como en un navegador. Por eso esta página no describe cómo funciona ese ajuste; abre la guía desde tu propio panel. Si usas WordPress autoalojado en lugar de WordPress.com, el archivo lo editas tú, como en cualquier alojamiento.

En palabras del proveedor (original en inglés): “To opt out of sharing your site's public content with third parties (including AI models), visit the Prevent third-party sharing guide.”

Fuente: [WordPress.com Support: Control your site's visibility](https://wordpress.com/support/privacy-settings/), leído el 21 de octubre de 2026.

## Los pasos

1. Abre Settings, luego Reading, y comprueba que Site Visibility esté en Public si quieres que los rastreadores vean el sitio.
2. Abre la guía Prevent third-party sharing de WordPress.com desde la ayuda de ajustes de privacidad y síguela si quieres excluirte de compartir contenido con terceros, incluidos los modelos de IA.
3. Abre tudominio.com/robots.txt y lee lo que tu sitio sirve realmente a los rastreadores.

## Las líneas que debes usar

Para permitir:

```
# No edit to make on WordPress.com for the sharing opt-out.
# Check what your site serves:
# https://yourdomain.com/robots.txt
```

Para bloquear:

```
# On a self-hosted WordPress site, you add lines like these through your SEO plugin or the file:
User-agent: GPTBot
Disallow: /
```

## Cosas a tener en cuenta

Un sitio en Coming Soon o Private no es lo mismo que excluirse de la IA: lo oculta a todo el mundo, buscadores incluidos, que es lo contrario de lo que necesita una tienda que quiere ser citada.

## Compara con Cloudflare

[Cloudflare](/es/platforms/cloudflare): un interruptor a nivel de red que funciona sea cual sea la plataforma del sitio.

## Comprueba tu propio sitio

La comprobación gratuita del cuadro de arriba lee robots.txt para los rastreadores de IA y envía una petición real por rastreador, así que aparece cualquier regla que los ajustes de tu plataforma permiten pero que un cortafuegos rechaza. La lista completa de rastreadores está en [el centro de rastreadores de IA](/es/bots).

## FAQ

### ¿La exclusión de la IA de WordPress.com es lo mismo que bloquear GPTBot?

WordPress.com la describe como excluirte de compartir tu contenido público con terceros, incluidos los modelos de IA. No la describe como una regla de robots.txt, así que revisa tu robots.txt activo para ver qué se les dice a los rastreadores.

### ¿Puedo editar robots.txt en WordPress.com?

No encontramos un editor de robots.txt en la guía de visibilidad que leímos, así que no afirmamos ni una cosa ni la otra. Busca en los ajustes de tu sitio según tu plan.

### ¿Qué es el acceso a herramientas por MCP?

La guía dice que permite a agentes de IA externos leer y editar los ajustes de visibilidad de tu sitio. Trata de gestionar el sitio, no de los rastreadores.

## Sources

- [WordPress.com Support: Control your site's visibility](https://wordpress.com/support/privacy-settings/), leído el 21 de octubre de 2026
- [WordPress.com Support: Prevent third-party sharing](https://wordpress.com/support/privacy-settings/prevent-third-party-sharing/), leído el 21 de octubre de 2026
