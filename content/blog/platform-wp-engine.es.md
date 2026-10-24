title: WP Engine: robots.txt, crawl-delay por defecto 10 s y Web Rules
slug: wp-engine
description: Según WP Engine, un robots.txt físico anula los de plugins y el crawl-delay por defecto es de 10 segundos. Web Rules Engine deniega bots por agente de usuario.
section: platforms
locale: es
cluster: Rastreadores de IA por plataforma
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre WP Engine: Dónde SFTP, Yoast o Web Rules, Crawl-delay por defecto 10 segundos, Dirección wpengine.com Disallow all, Bloqueo por agente Web Rules Engine
hero_sub: Ajustes de rastreadores de IA en WP Engine
hero_boxes: Dónde|SFTP, Yoast o Web Rules; Crawl-delay|10 segundos por defecto; wpengine.com|Disallow all; Bloqueo por agente|Web Rules Engine
widget: on
related: /es/platforms|Todas las plataformas comparadas; /es/platforms/wordpress-com|WordPress.com; /es/bots|Rastreadores de IA comparados; /es/guides/cms|Lista de comprobación de visibilidad en IA para Shopify, WooCommerce y más
answer: WP Engine dice que un robots.txt físico en la raíz de tu sitio anula cualquier archivo generado por un plugin o un tema. Su archivo por defecto fija un crawl-delay de 10 segundos, y las direcciones wpengine.com reciben un archivo que lo deniega todo. Para denegar un bot por agente de usuario, remite a su Web Rules Engine.

## Dónde está el ajuste en WP Engine

La página de WP Engine ofrece dos formas de crear el archivo. Con el plugin Yoast SEO instalado, ve a SEO, luego a Tools, elige el editor de archivos y selecciona Create robots.txt file. O crea tú mismo un archivo robots.txt y súbelo por SFTP o por SSH Gateway al directorio raíz de tu sitio. Para bloquear por agente de usuario, la página te remite a las reglas de acceso del Web Rules Engine en el User Portal.

## Lo que solo dice la página de WP Engine y no las de otras plataformas

WP Engine incluye un robots.txt por defecto, y la página dice qué contiene. Su nota indica que el crawl-delay por defecto para todos los sitios es de 10 segundos, y que cualquier entorno con una dirección wpengine.com recibe un archivo que lo deniega todo, para evitar que un sitio se indexe en el dominio equivocado antes del lanzamiento. Solo los entornos que usan un dominio propio verán los cambios hechos en robots.txt. Además, un archivo físico que subas tiene prioridad sobre un archivo creado por un plugin o un tema.

En palabras del proveedor (original en inglés): “This is what’s in the server’s default robots.txt file and can be overridden when you add a custom robots.txt file with one of the methods outlined in this article.”

Fuente: [WP Engine Support: Robots.txt and WordPress](https://wpengine.com/support/read-use-robots-txt/), leído el 24 de octubre de 2026.

## Los pasos

1. Crea un archivo llamado robots.txt. El nombre debe ir en minúsculas y la extensión ser .txt, no .html.
2. Añade tus directivas y guarda. Si prefieres la vía del plugin, usa Yoast SEO, Tools y luego Create robots.txt file.
3. Sube el archivo por SFTP o por SSH Gateway al directorio raíz de tu sitio.
4. Abre /robots.txt en tu dominio propio activo para comprobarlo. Una copia en una dirección wpengine.com no mostrará tus cambios.
5. Para denegar un bot en el servidor, abre la página Sites del User Portal, selecciona el entorno, haz clic en Web Rules en el menú secundario de la izquierda (puede que tengas que desplegar Advanced), elige Access rules y haz clic en Add Rule.
6. Pon Action en Deny, IP en All y añade una condición con Type Header, Name User-Agent, Operator Regex matches (~) y el nombre del agente de usuario como Value. Haz clic en Add Rule para guardar.

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

La página de WP Engine dice que los valores de las directivas distinguen mayúsculas de minúsculas y que robots.txt no admite del todo los comodines ni las expresiones regulares.

## Cosas a tener en cuenta

La página no nombra ningún rastreador de IA: sus ejemplos usan BadBotName, Googlebot, bingbot y SEMrush. También dice que los robots no tienen por qué seguir robots.txt, y recomienda un cortafuegos como Sucuri WAF o Cloudflare, o contactar con Support, para frenar a los malos actores antes de que lleguen al sitio. Según la página del Web Rules Engine, una petición denegada por una regla de acceso de Web Rules recibe una respuesta 403 Forbidden y no cuenta para las visitas facturables. Tu robots.txt personalizado anula el archivo por defecto, incluida su línea de crawl-delay de 10 segundos, así que añade tú mismo una línea Crawl-delay si quieres conservar una.

## Compara con WordPress.com

[WordPress.com](/es/platforms/wordpress-com): una exclusión de la IA en los ajustes de privacidad en lugar de un archivo robots.txt que escribas tú.

## Comprueba tu propio sitio

La comprobación gratuita del cuadro de arriba lee robots.txt para los rastreadores de IA y envía una petición real por rastreador, así que aparece cualquier regla que los ajustes de tu plataforma permiten pero que un cortafuegos rechaza. La lista completa de rastreadores está en [el centro de rastreadores de IA](/es/bots).

## FAQ

### ¿Por qué mi sitio de staging en WP Engine ignora mi robots.txt?

WP Engine dice que los sitios en una dirección environment.wpengine.com reciben automáticamente un robots.txt que lo deniega todo, y que solo los entornos con un dominio propio ven los cambios del archivo. Las cuentas compartidas solo pueden añadir un dominio propio a Production, así que Staging y Development normalmente no mostrarán tus ediciones.

### ¿Un plugin de robots.txt anula un archivo que subo a WP Engine?

No, es al revés. WP Engine dice que un robots.txt físico en la raíz de tu sitio sobrescribe cualquier archivo generado dinámicamente por un plugin o un tema.

## Sources

- [WP Engine Support: Robots.txt and WordPress](https://wpengine.com/support/read-use-robots-txt/), leído el 24 de octubre de 2026
- [WP Engine Support: Web Rules Engine](https://wpengine.com/support/web-rules-engine/), leído el 24 de octubre de 2026
