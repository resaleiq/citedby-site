title: Adobe Commerce: robots.txt está en Content, Design, Configuration
slug: adobe-commerce
description: Adobe Commerce edita robots.txt en el Admin, en Search Engine Robots. En Cloud hay pasos extra con pub/media y Adobe no nombra ningún rastreador de IA.
section: platforms
locale: es
cluster: Rastreadores de IA por plataforma
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre Adobe Commerce: Dónde Content, Design, Configuration, Sección Search Engine Robots, Cloud Pasos extra, Nombres de IA No aparecen
hero_sub: Ajustes de rastreadores de IA en Adobe Commerce
hero_boxes: Dónde|Content > Design > Configuration; Sección|Search Engine Robots; Cloud|Pasos extra; Nombres de IA|No aparecen
widget: on
related: /es/platforms|Todas las plataformas comparadas; /es/platforms/shopify|Shopify; /es/bots|Rastreadores de IA comparados; /es/guides/cms|Lista de comprobación de visibilidad en IA para Shopify, WooCommerce y más
answer: En Adobe Commerce editas robots.txt en el Admin: Content, Design, Configuration, la fila Global, luego Search Engine Robots y el cuadro de instrucciones personalizadas. Las páginas de Adobe hablan de rastreadores y bots en general, sin nombrar ninguno de IA, así que esos agentes de usuario los añades tú. Cloud tiene pasos extra con rutas de archivo.

## Dónde está el ajuste en Adobe Commerce

En la barra lateral del Admin ve a Content, luego a Design y después a Configuration. La descripción general de SEO de Adobe indica que busques la configuración Global en la primera fila de la cuadrícula, hagas clic en Edit y despliegues la sección Search Engine Robots. Ahí está el cuadro Edit Custom instruction of robots.txt file, con un botón Reset to Default.

## Lo que solo dicen las páginas de Adobe Commerce y no las de otras plataformas

En Adobe Commerce sobre infraestructura en la nube, el archivo robots.txt tiene un problema de ubicación que las otras plataformas no tienen. El manual de implementación de Adobe dice que añadas el contenido en el Admin, pero el sistema de archivos es de solo lectura, así que el archivo tiene que estar en pub/media y un fragmento VCL personalizado de Fastly redirige /robots.txt hasta allí. Si hay varios sitios en un mismo proyecto, el manual nombra los archivos por sitio, por ejemplo domainone_robots.txt. Para las instalaciones locales dice que escribas los archivos en /path/to/commerce/pub/media/ o en /path/to/commerce/media, la ruta que corresponda a tu instalación.

En palabras del proveedor (original en inglés): “Due to the read-only file system on Adobe Commerce on cloud infrastructure projects, you must specify the pub/media path before generating the file.”

Fuente: [Adobe Commerce Implementation Playbook: Best practices for configuring web crawlers](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/launch/robots-txt), leído el 24 de octubre de 2026.

## Los pasos

1. En la barra lateral del Admin ve a Content, luego a Design y después a Configuration.
2. Busca la configuración Global en la primera fila de la cuadrícula y haz clic en Edit.
3. Baja y despliega Search Engine Robots.
4. Elige para Default Robots INDEX, FOLLOW, NOINDEX, FOLLOW, INDEX, NOFOLLOW o NOINDEX, NOFOLLOW. Adobe las describe como instrucciones para los rastreadores sobre la indexación y el seguimiento de enlaces.
5. Si lo necesitas, escribe tus propias reglas en el cuadro Edit Custom instruction of robots.txt file. Reset to Default restaura las instrucciones de Adobe.
6. Haz clic en Save Configuration y abre el /robots.txt de tu tienda para ver el resultado. El manual de Adobe indica que ahí puedes ver el archivo generado automáticamente.

## Las líneas que debes usar

Los ejemplos de Adobe usan User-agent: * para todos los rastreadores. Para permitir o bloquear un rastreador concreto, añade un grupo con su nombre:

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

Las páginas de Adobe no dicen si el texto que escribes se suma a sus instrucciones por defecto o las sustituye. Guarda y lee /robots.txt para confirmar qué se sirve.

## Cosas a tener en cuenta

El manual de Adobe dice que no expongas la ruta de tu Admin en robots.txt, porque es una vulnerabilidad para el hackeo del sitio y una posible pérdida de datos, y que la elimines. Las instrucciones por defecto de Adobe empiezan con User-agent: * y una lista de líneas Disallow como /checkout/ y /catalog/, así que revisa lo que conservas. En cloud, un artículo de la base de conocimiento con fecha del 18 de agosto de 2026 dice que el contenido de robots.txt se genera a partir de la configuración del Admin y se guarda en la base de datos, sin que haga falta un archivo físico en ese caso, mientras que el manual describe la redirección a pub/media. Las dos páginas dicen cosas distintas, así que confirma con el soporte de Adobe Commerce cuál se aplica a tu proyecto. El manual también dice que su consejo cubre solo el escaparate nativo de Adobe Commerce, no los escaparates headless ni los de Adobe Experience Manager.

## Compara con Shopify

[Shopify](/es/platforms/shopify): una plantilla del tema en lugar de un cuadro en el Admin, y el soporte no arreglará las ediciones que hagas en ella.

## Comprueba tu propio sitio

La comprobación gratuita del cuadro de arriba lee robots.txt para los rastreadores de IA y envía una petición real por rastreador, así que aparece cualquier regla que los ajustes de tu plataforma permiten pero que un cortafuegos rechaza. La lista completa de rastreadores está en [el centro de rastreadores de IA](/es/bots).

## FAQ

### ¿Por qué no cambia mi robots.txt personalizado en Adobe Commerce cloud?

La base de conocimiento de Adobe dice que la causa habitual es que la indexación por los motores de búsqueda está desactivada, lo que impide aplicar el contenido personalizado de robots.txt. Se arregla en la Cloud Console o con el ajuste restrict_robots de la CLI magento-cloud. El artículo añade que los entornos de Staging tienen la indexación desactivada por defecto y que no se puede activar ahí.

### ¿Adobe Commerce menciona rastreadores de IA para robots.txt?

No en las páginas que hemos leído. Hablan de rastreadores web y bots, y sus ejemplos usan solo User-agent: *. Añade cada agente de usuario de IA que quieras permitir o bloquear como un grupo propio.

## Sources

- [Adobe Commerce Implementation Playbook: Best practices for configuring web crawlers](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/launch/robots-txt), leído el 24 de octubre de 2026
- [Adobe Commerce Admin guide: SEO overview](https://experienceleague.adobe.com/en/docs/commerce-admin/marketing/seo/seo-overview), leído el 24 de octubre de 2026
- [Adobe Commerce knowledge base: Resolve robots.txt not updating or displaying default settings](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/robots-txt-not-updated-or-displaying-default-settings), leído el 24 de octubre de 2026
