title: Framer: sube tu propio robots.txt con Static Files
slug: framer
description: Framer genera un robots.txt para cada sitio publicado. Para cambiarlo subes el tuyo con Static Files en los planes Pro o Enterprise, y sustituye al generado.
section: platforms
locale: es
cluster: Rastreadores de IA por plataforma
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre Framer: Dónde Static Files, Planes Pro y Enterprise, Por defecto Autogenerado, Archivo propio Sustituye al predeterminado
hero_sub: Ajustes de rastreadores de IA en Framer
hero_boxes: Dónde|Static Files; Planes|Pro y Enterprise; Por defecto|Autogenerado; Archivo propio|Sustituye al predeterminado
widget: on
related: /es/platforms|Todas las plataformas comparadas; /es/platforms/webflow|Webflow; /es/bots|Rastreadores de IA comparados; /es/guides/cms|Lista de comprobación de visibilidad en IA para Shopify, WooCommerce y más
answer: Framer genera un robots.txt para cada sitio publicado. Para permitir o bloquear rastreadores de IA subes tu propio archivo con Static Files, con la ruta establecida en /. Framer dice que está disponible en los planes Pro y Enterprise, y que tu archivo sustituye al generado en lugar de añadirse a él.

## Dónde está el ajuste en Framer

En el panel de tu proyecto, selecciona tu dominio, abre la pestaña Files y sube tu archivo con la ruta establecida en /. La página de ayuda de Framer lo llama Static Files. Para ver antes el archivo activo, añade /robots.txt al dominio de tu sitio en un navegador.

## Lo que solo dice la página de Framer y no las de otras plataformas

Framer no te da ningún editor de robots.txt. El archivo se genera por ti y la única forma de cambiarlo es subir uno que lo sustituya, algo que depende del plan. La página de Framer dice que, si necesitas un robots.txt personalizado, puedes subir uno con Static Files, y que el archivo nuevo sustituye al generado automáticamente. El límite por plan viene justo después.

En palabras del proveedor (original en inglés): “This is available on Pro and Enterprise plans.”

Fuente: [Framer Help: Access your robots.txt file](https://www.framer.com/help/articles/how-can-i-access-the-robots-txt-file/), leído el 24 de octubre de 2026.

## Los pasos

1. Escribe tu robots.txt como un archivo de texto sin formato en tu ordenador.
2. Ve al panel de tu proyecto y selecciona tu dominio.
3. Abre la pestaña Files.
4. Sube tu archivo con la ruta establecida en /.
5. Abre tudominio.com/robots.txt en un navegador para confirmar que el archivo activo es el tuyo.

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

## Cosas a tener en cuenta

Como tu archivo sustituye al generado, todo lo que contenía el archivo generado desaparece a menos que lo copies antes. La página de Framer no dice qué contiene el archivo generado, así que lee tudominio.com/robots.txt antes de subir el tuyo y conserva las líneas que quieras, como una línea de sitemap. La página trata de robots.txt en general y no menciona rastreadores de IA por su nombre, así que los agentes de usuario de arriba son ejemplos que debes contrastar con la página de cada proveedor. Se actualizó por última vez el 15 de septiembre de 2026.

## Compara con Webflow

[Webflow](/es/platforms/webflow): las reglas se escriben en un campo de ajustes en lugar de subirse como archivo, y además hay una cabecera Content-Signal.

## Comprueba tu propio sitio

La comprobación gratuita del cuadro de arriba lee robots.txt para los rastreadores de IA y envía una petición real por rastreador, así que aparece cualquier regla que los ajustes de tu plataforma permiten pero que un cortafuegos rechaza. La lista completa de rastreadores está en [el centro de rastreadores de IA](/es/bots).

## FAQ

### ¿Puedo editar el archivo robots.txt en Framer?

Sí, subiéndolo. La página de Framer dice que abras la pestaña Files de tu dominio en el panel del proyecto y subas tu archivo con la ruta establecida en /. Dice que está disponible en los planes Pro y Enterprise.

### ¿Framer crea un robots.txt automáticamente?

Sí. La página de Framer dice que genera un archivo robots.txt para cada sitio publicado, y que un archivo personalizado subido con Static Files sustituye al predeterminado.

## Sources

- [Framer Help: Access your robots.txt file](https://www.framer.com/help/articles/how-can-i-access-the-robots-txt-file/), leído el 24 de octubre de 2026
