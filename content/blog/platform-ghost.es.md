title: Ghost: robots.txt en tu tema: permite o bloquea bots de IA
slug: ghost
description: Ghost no tiene ajuste de robots.txt en el admin. Su ayuda indica guardar uno en la raíz del tema, que sustituye al predeterminado. Ghost(Pro) exige plan.
section: platforms
locale: es
cluster: Rastreadores de IA por plataforma
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre Ghost: Dónde Raíz del tema, Archivo robots.txt, Efecto Sustituye al predeterminado, Ghost(Pro) Plan Creator o superior
hero_sub: Ajustes de rastreadores de IA en Ghost
hero_boxes: Dónde|Raíz del tema; Archivo|robots.txt; Efecto|Sustituye al predeterminado; Ghost(Pro)|Creator o superior
widget: on
related: /es/platforms|Todas las plataformas comparadas; /es/platforms/wordpress-com|WordPress.com; /es/bots|Rastreadores de IA comparados; /es/guides/cms|Lista de comprobación de visibilidad en IA para Shopify, WooCommerce y más
answer: Ghost sirve un robots.txt por defecto. Para cambiarlo, guarda tu propio robots.txt en la raíz de tu tema y luego instala y activa la nueva versión del tema. La página de ayuda de Ghost dice que los temas personalizados en Ghost(Pro) requieren el plan Creator o uno superior, así que tu plan decide si puedes editarlo.

## Dónde está el ajuste en Ghost

No hay ningún campo de robots.txt en el admin. La página de ayuda de Ghost dice que el archivo vive dentro del tema de tu sitio: escribe tu robots.txt y guárdalo en la raíz del tema. La documentación de temas de Ghost lo dice en una línea: los temas pueden incluir un robots.txt que anula el robots.txt predeterminado que ofrece Ghost.

## Lo que solo dice la página de Ghost y no las de otras plataformas

En Ghost el archivo viaja con el tema, así que el plan que tengas decide si puedes cambiarlo. La página de ayuda de Ghost dice que necesitas sentirte cómodo escribiendo tu propio robots.txt e instalando una nueva versión de tu tema. Después añade un límite de plan para Ghost(Pro), el servicio alojado de Ghost: instalar un tema personalizado requiere el plan Creator o uno superior. La página describe lo que ocurre a continuación en estos términos.

En palabras del proveedor (original en inglés): “Once the new version of the theme is installed and activated, the theme's robots.txt will be used in place of Ghost's default robots.txt.”

Fuente: [Ghost Help: Modifying robots.txt](https://ghost.org/help/modifying-robots-txt/), leído el 24 de octubre de 2026.

## Los pasos

1. Escribe tu archivo robots.txt.
2. Guárdalo en la raíz de tu tema.
3. Instala la nueva versión del tema y actívala. Ghost dice que el robots.txt del tema se usa en lugar del predeterminado una vez que la nueva versión está instalada y activada.
4. En Ghost(Pro), comprueba antes tu plan: Ghost dice que instalar un tema personalizado requiere el plan Creator o uno superior.

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

El archivo del tema se usa en lugar del predeterminado de Ghost, no se suma a él. Las páginas de Ghost no dicen qué contiene el predeterminado, así que abre tusitio.com/robots.txt antes de sustituirlo y copia las líneas que quieras conservar, como una línea de sitemap. La página también avisa de que esta vía exige que te sientas cómodo escribiendo el archivo tú mismo, y no trata los rastreadores de IA por su nombre.

## Compara con WordPress.com

[WordPress.com](/es/platforms/wordpress-com): su exclusión de la IA es un ajuste de uso compartido, no un archivo que escribas tú.

## Comprueba tu propio sitio

La comprobación gratuita del cuadro de arriba lee robots.txt para los rastreadores de IA y envía una petición real por rastreador, así que aparece cualquier regla que los ajustes de tu plataforma permiten pero que un cortafuegos rechaza. La lista completa de rastreadores está en [el centro de rastreadores de IA](/es/bots).

## FAQ

### ¿Dónde pongo un robots.txt personalizado en Ghost?

En la raíz de tu tema. La página de ayuda de Ghost dice que, una vez que la nueva versión del tema está instalada y activada, el robots.txt del tema se usa en lugar del predeterminado de Ghost.

### ¿Necesito un plan de pago para editar robots.txt en Ghost(Pro)?

La página de Ghost dice que instalar un tema personalizado en Ghost(Pro) requiere una suscripción al plan Creator o a uno superior. Como el archivo forma parte del tema, eso vale también para un robots.txt personalizado.

## Sources

- [Ghost Help: Modifying robots.txt](https://ghost.org/help/modifying-robots-txt/), leído el 24 de octubre de 2026
- [Ghost Docs: Theme structure](https://docs.ghost.org/themes/structure), leído el 24 de octubre de 2026
