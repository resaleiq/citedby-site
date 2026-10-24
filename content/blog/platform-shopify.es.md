title: Shopify: gestiona rastreadores de IA y lo que robots.txt no cubre
slug: shopify
description: Edita robots.txt.liquid para permitir o bloquear rastreadores de IA en Shopify. Un bloqueo solo afecta a la web abierta, no a los datos enviados a ChatGPT.
section: platforms
locale: es
cluster: Rastreadores de IA por plataforma
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Cuatro datos sobre Shopify: Dónde robots.txt.liquid, Soporte Sin soporte de Shopify, Feed del catálogo No cubierto, Efecto Instantáneo
hero_sub: Ajustes de rastreadores de IA en Shopify
hero_boxes: Dónde|robots.txt.liquid; Soporte|Sin soporte de Shopify; Feed del catálogo|No cubierto; Efecto|Instantáneo
widget: on
related: /es/platforms|Todas las plataformas comparadas; /es/platforms/squarespace|Squarespace; /es/bots|Rastreadores de IA comparados; /es/guides/cms|Lista de comprobación de visibilidad en IA para Shopify, WooCommerce y más
answer: En Shopify controlas los rastreadores de IA añadiendo una plantilla robots.txt.liquid a tu tema. La página de ayuda de Shopify dice que un bloqueo ahí solo afecta a la visibilidad en la web abierta: los datos de producto siguen llegando a escaparates agénticos como ChatGPT o Microsoft Copilot a través de Shopify Catalog, con independencia de /robots.txt.

## Dónde está el ajuste en Shopify

Online Store, luego Edit code del tema, después Add a new template y elige robots. Shopify dice que es una personalización sin soporte: su Support no puede ayudar con las ediciones, y un uso incorrecto «puede provocar la pérdida de todo el tráfico».

## Lo que solo dice la página de Shopify y no las de otras plataformas

Shopify describe dos capas de control. La capa de red la gestiona Shopify para las tiendas que están en Shopify, y no tienes que hacer nada. La capa de /robots.txt es tuya mediante robots.txt.liquid. Su página traza entonces la línea que importa para una tienda: si vendes a través de escaparates agénticos como ChatGPT o Microsoft Copilot, tus datos de producto se sindican a través de Shopify Catalog «con independencia de /robots.txt», y bloquear los rastreadores de IA en cualquiera de las dos capas «solo afecta a la visibilidad en la web abierta». Para cambiar lo que comparte Catalog usas los ajustes de escaparates agénticos, no robots.txt.

En palabras del proveedor (original en inglés): “Blocking AI crawlers at the /robots.txt or network layer affects only open-web discoverability. It doesn't stop your product data from being sent by Shopify Catalog to the agentic storefronts that you've activated.”

Fuente: [Shopify Help Center: Editing robots.txt.liquid](https://help.shopify.com/en/manual/promoting-marketing/seo/editing-robots-txt), leído el 21 de octubre de 2026.

## Los pasos

1. Desde tu admin de Shopify ve a Online Store.
2. En el tema que tienes publicado, abre el menú y elige Edit code.
3. Haz clic en Add a new template, elige robots y luego Create template.
4. Conserva el Liquid que genera los grupos de reglas por defecto y añade tus propias reglas debajo. Shopify recomienda esto en lugar de sustituir el archivo por texto sin formato, porque el texto sin formato se queda obsoleto.
5. Guarda en el tema publicado. Shopify dice que los cambios son instantáneos, pero los rastreadores no siempre reaccionan de inmediato.

## Las líneas que debes usar

Para permitir:

```
# Nothing to add: Shopify's default robots.txt allows crawlers that are not named.
# To name one explicitly, add under the default Liquid block:
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

Dos detalles de la misma página. Un tema subido desde la sección Themes del admin no importa robots.txt.liquid; los cambios hechos con ThemeKit o por línea de comandos sí lo conservan. Y si tu plantilla genera los grupos por defecto, bórrala para obtener el valor por defecto actual de Shopify, que puede incluir reglas que tu copia antigua no tiene, como Disallow: /search.

## Compara con Squarespace

[Squarespace](/es/platforms/squarespace): una casilla en lugar de una plantilla, y una lista fija de 26 nombres.

## Comprueba tu propio sitio

La comprobación gratuita del cuadro de arriba lee robots.txt para los rastreadores de IA y envía una petición real por rastreador, así que aparece cualquier regla que los ajustes de tu plataforma permiten pero que un cortafuegos rechaza. La lista completa de rastreadores está en [el centro de rastreadores de IA](/es/bots).

## FAQ

### ¿Bloquear GPTBot en Shopify impide que ChatGPT muestre mis productos?

No por sí solo. Shopify dice que robots.txt y los bloqueos de red solo afectan a la visibilidad en la web abierta, y que Shopify Catalog envía los datos de producto a los escaparates agénticos que has activado con independencia de /robots.txt. Para controlar ese feed, usa los ajustes de escaparates agénticos de Shopify.

### ¿Puede el Support de Shopify arreglar mi robots.txt.liquid?

No. La página de Shopify dice que Support no puede ayudar con las ediciones del archivo y sugiere contratar a un Shopify Partner.

### ¿Necesito un proxy de Cloudflare delante de Shopify?

Shopify dice que la gestión de bots en la capa de red se hace desde Shopify para las tiendas que están en Shopify, y que no recomienda una configuración de proxy delante de Shopify ni la admite.

## Sources

- [Shopify Help Center: Editing robots.txt.liquid](https://help.shopify.com/en/manual/promoting-marketing/seo/editing-robots-txt), leído el 21 de octubre de 2026
- [Shopify.dev: Customize robots.txt.liquid](https://shopify.dev/docs/storefronts/themes/seo/robots-txt), leído el 21 de octubre de 2026
