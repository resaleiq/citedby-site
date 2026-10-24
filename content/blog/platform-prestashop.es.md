title: PrestaShop: generador de robots.txt: un solo conjunto de reglas
slug: prestashop
description: La guía de PrestaShop describe un botón Generate robots.txt que sustituye tu archivo y usa solo User-agent: *. Añade tus reglas de IA después de generarlo.
section: platforms
locale: es
cluster: Rastreadores de IA por plataforma
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre PrestaShop: Dónde Traffic, SEO and URLs, Botón Generate robots.txt, User-agent solo asterisco, Regenerar Sustituye el archivo
hero_sub: Ajustes de rastreadores de IA en PrestaShop
hero_boxes: Dónde|Traffic > SEO and URLs; Botón|Generate robots.txt; User-agent|Solo *; Regenerar|Sustituye el archivo
widget: on
related: /es/platforms|Todas las plataformas comparadas; /es/platforms/shopify|Shopify; /es/bots|Rastreadores de IA comparados; /es/guides/cms|Lista de comprobación de visibilidad en IA para Shopify, WooCommerce y más
answer: La guía de usuario de PrestaShop describe una herramienta Robots file generation en Shop Parameters, Traffic, SEO and URLs. Escribe directivas de exclusión para archivos no públicos con User-agent: *, sin nombrar ningún rastreador de IA. Generate robots.txt sustituye cualquier archivo existente, así que añade tus reglas de rastreadores de IA solo después de generarlo.

## Dónde está el ajuste en PrestaShop

La guía de usuario de PrestaShop 8 lo sitúa en Configuring your Shop Parameters, luego en Traffic y después en SEO and URLs. La sección se llama Robots file generation. La página no indica ninguna ruta de menú dentro del back office aparte de esa, y al pie muestra «Last updated 4 years ago».

## Lo que solo dice la página de PrestaShop y no las de otras plataformas

PrestaShop no te da un cuadro donde escribir reglas. Te da un botón que escribe el archivo entero. La guía dice que el generador «simplemente crea un archivo con directivas de exclusión para archivos y directorios que no están pensados para ser públicos», aplicadas a todos los bots mediante la cadena «User-agent: *». También dice que los peores bots ignoran el archivo, porque es «puramente orientativo». La consecuencia para los rastreadores de IA está en las dos últimas frases de la sección: al regenerar se borra todo lo que hayas añadido.

En palabras del proveedor (original en inglés): “Clicking on the "Generate robots.txt" button replaces any existing robots.txt file with a new one. Therefore, if you want to add your own rules, do it after PrestaShop has generated its version of the file.”

Fuente: [PrestaShop 8 User Guide: SEO and URLs](https://docs.prestashop-project.org/v.8-documentation/user-guide/configuring-shop/shop-parameters/traffic/seo-and-urls), leído el 24 de octubre de 2026.

## Los pasos

1. Abre SEO and URLs en la sección Traffic de Shop Parameters.
2. Ve a Robots file generation.
3. Haz clic en Generate robots.txt. Esto sustituye cualquier archivo robots.txt existente.
4. Añade tus propias reglas después de que PrestaShop haya generado su versión. La página no dice cómo editar el archivo generado, así que usa el acceso a archivos que te dé tu alojamiento.
5. Abre /robots.txt en tu tienda para comprobar que tus reglas siguen ahí. Repite el paso 4 cada vez que vuelvas a hacer clic en el botón.

## Las líneas que debes usar

Para permitir:

```
# Nothing to add: the generated file only lists files and directories that are not public.
# To name one explicitly, add after the generated block:
User-agent: OAI-SearchBot
Allow: /
```

Para bloquear:

```
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /
```

## Cosas a tener en cuenta

El archivo generado habla a todos los bots por igual, porque usa User-agent: * y nada más, así que la herramienta de PrestaShop no te deja elegir por rastreador. La guía dice que a algunos bots quieres darles acceso total, como los de Google, y a otros no, como los bots de spam y los ladrones de contenido, y esa es una decisión que tomas tú en los grupos que añadas. La guía no menciona los rastreadores de IA por su nombre y no apunta a ningún ajuste ni módulo para ellos.

## Compara con Shopify

[Shopify](/es/platforms/shopify): una plantilla robots.txt.liquid que conserva tus añadidos, mientras que el botón de PrestaShop los sobrescribe.

## Comprueba tu propio sitio

La comprobación gratuita del cuadro de arriba lee robots.txt para los rastreadores de IA y envía una petición real por rastreador, así que aparece cualquier regla que los ajustes de tu plataforma permiten pero que un cortafuegos rechaza. La lista completa de rastreadores está en [el centro de rastreadores de IA](/es/bots).

## FAQ

### ¿Regenerar robots.txt en PrestaShop borrará mis reglas para rastreadores de IA?

Sí, si las añadiste al archivo generado. La guía de PrestaShop dice que el botón sustituye cualquier robots.txt existente por uno nuevo, y que añadas tus propias reglas después de que haya generado su versión.

### ¿PrestaShop bloquea los rastreadores de IA por defecto?

La guía no lo dice. Describe un archivo generado con directivas de exclusión para archivos y directorios no públicos bajo User-agent: *, y no nombra ningún rastreador de IA.

## Sources

- [PrestaShop 8 User Guide: SEO and URLs](https://docs.prestashop-project.org/v.8-documentation/user-guide/configuring-shop/shop-parameters/traffic/seo-and-urls), leído el 24 de octubre de 2026
