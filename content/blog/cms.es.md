title: Visibilidad en IA en Shopify, WooCommerce y similares
h1: Lista de comprobación de visibilidad en IA para Shopify, WooCommerce y otras plataformas de tienda online
description: Cómo editar robots.txt, hallar el sitemap, revisar el JSON-LD de producto y detectar texto que solo carga JavaScript en Shopify y WooCommerce.
slug: cms
section: guides
locale: es
cluster: Guías
date: 2026-10-20
reviewed: 2026-10-20
hero: auto
hero_alt: Tarjeta con el título visibilidad en IA en Shopify, WooCommerce y otras plataformas y cuatro cuadros: robots.txt, sitemap, JSON-LD y texto en HTML
hero_sub: Qué revisar en cada plataforma
hero_boxes: robots.txt|Dónde se edita; Sitemap|Dónde está; JSON-LD|Datos de producto; Texto en HTML|Sin depender de scripts
widget: on
howto: on
steps_img: on
related: /es/guides/technical-seo-checklist|Lista de comprobación de SEO técnico; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web?; /es/blog/is-gptbot-blocked|¿Está bloqueado GPTBot en tu web?
answer: En cualquier plataforma de tienda online haces las mismas cuatro comprobaciones: dónde se edita robots.txt, dónde está el sitemap, si el código fuente trae JSON-LD de producto y si el texto del producto está en el HTML sin JavaScript. En Shopify y WordPress con WooCommerce los pasos concretos están en su documentación oficial.

## ¿Qué cuatro cosas debes revisar en tu plataforma?

Los asistentes de IA no saben qué plataforma usas: solo ven lo que sirve tu web. Por eso la lista es la misma en todas, y lo que cambia es dónde se toca cada cosa. Las cuatro comprobaciones son robots.txt, el sitemap, los datos de producto en JSON-LD y el texto en el HTML.

1. Mira robots: abre `tutienda.es/robots.txt` y busca reglas para `OAI-SearchBot`, `GPTBot` y `PerplexityBot`, y un `Disallow: /` general.
2. Abre el sitemap: prueba `tutienda.es/sitemap.xml` y comprueba que lista productos y categorías.
3. Busca el JSON-LD: en el código fuente de una ficha, busca `application/ld+json` y lee nombre, precio y disponibilidad.
4. Comprueba el texto sin scripts: busca en el código fuente el nombre y la descripción de un producto. Si no están, los añade JavaScript.

## ¿Cómo se hace en Shopify?

Todas las tiendas Shopify tienen un robots.txt por defecto. Para cambiarlo hay que añadir una plantilla `robots.txt.liquid` en la carpeta de plantillas de tu tema, desde Tienda online, Editar código, Añadir una plantilla nueva y elegir robots. Shopify avisa de que es una personalización no compatible con su soporte y de que un uso incorrecto puede hacer perder todo el tráfico ([Shopify: editar robots.txt.liquid](https://help.shopify.com/en/manual/promoting-marketing/seo/editing-robots-txt), en inglés).

La misma página explica que el acceso de los rastreadores de IA tiene dos capas. La de red la gestiona Shopify directamente. La de robots.txt la controlas tú con esa plantilla, y sus reglas son orientativas: no todos los rastreadores están obligados a seguirlas. Además, bloquear rastreadores en robots.txt solo afecta a la visibilidad en la web abierta, no a los datos de producto que Shopify Catalog envía a los canales de compra con agentes que hayas activado.

El sitemap se genera solo en `tuTienda.es/sitemap.xml` y enlaza a sitemaps separados de productos, colecciones, blogs y páginas. Se actualiza al añadir contenido nuevo, y no es accesible si la tienda está en modo privado ([Shopify: encontrar y enviar tu sitemap](https://help.shopify.com/en/manual/promoting-marketing/seo/find-site-map), en inglés).

Para las fichas de producto, Shopify recomienda incluir especificaciones detalladas, descripciones completas y datos estructurados con atributos del producto ([Shopify: optimizar tu tienda para la IA](https://help.shopify.com/en/manual/promoting-marketing/seo/optimizing-store-for-ai), en inglés). Comprueba en el código fuente qué bloque JSON-LD saca tu tema y si el precio coincide con el visible.

## ¿Cómo se hace en WordPress con WooCommerce?

WordPress genera un robots.txt por defecto, y un plugin puede modificarlo con el filtro `robots_txt` ([referencia del filtro](https://developer.wordpress.org/reference/hooks/robots_txt/)). Si subes un archivo robots.txt físico a la raíz, manda ese archivo. En Ajustes, Lectura, la casilla "Disuadir a los motores de búsqueda de indexar este sitio" añade una etiqueta `noindex` a la web ([WordPress: pantalla Lectura](https://wordpress.org/documentation/article/settings-reading-screen/)). Es habitual que se quede marcada desde la fase de pruebas: revísala.

Desde WordPress 5.5, el sitemap está en `tutienda.es/wp-sitemap.xml` ([WordPress Core](https://make.wordpress.org/core/2020/07/22/new-xml-sitemaps-functionality-in-wordpress-5-5/), en inglés). Si usas un plugin de SEO, puede publicar otro sitemap distinto: mira cuál lista tus productos.

WooCommerce incluye en su código una clase de datos estructurados que genera JSON-LD ([código en GitHub](https://github.com/woocommerce/woocommerce/blob/trunk/plugins/woocommerce/includes/class-wc-structured-data.php)). Comprueba en el código fuente de una ficha cuántos bloques `Product` salen: si tu tema o un plugin añade otro, pueden discrepar en el precio.

## ¿Y en PrestaShop, Wix, Squarespace u otras plataformas?

No citamos documentación oficial de estas plataformas porque no hemos podido verificarla, así que lo que sigue es consejo general. Busca en la ayuda de tu plataforma los términos "robots.txt", "sitemap" y "datos estructurados", o mira en los ajustes de SEO de tu panel.

Si la plataforma no deja editar robots.txt, anota lo que ves y pregunta a su soporte. Y haz siempre la prueba del código fuente: es válida en cualquier sitio.

## ¿Qué hacer con el texto que solo carga JavaScript?

Los temas y los plugins de reseñas, pestañas, variantes o "ver más" a veces cargan el texto después, con scripts. Un visitante lo ve. Un rastreador que no ejecuta JavaScript, no. Busca en el código fuente una frase de la descripción, del envío o de las devoluciones.

Si no está, desactiva el elemento o cambia a una versión que sirva el texto en el HTML. Si dudas de cuál es el culpable, desactiva los plugins de uno en uno y vuelve a mirar el código fuente.

## ¿Hay una forma de revisarlo todo de una vez?

La auditoría de CitedBy, desde 9 €, rastrea tu tienda hasta el límite de páginas de tu plan, revisa estos puntos y da la corrección exacta de cada problema. Mira [qué revisa](/es/ai-visibility-audit) y el [informe de muestra](/es/sample).

## FAQ

### ¿Puedo bloquear a los rastreadores de IA en Shopify?
Sí, editando la plantilla `robots.txt.liquid`. Shopify indica que bloquear en robots.txt solo afecta a la web abierta, no a los datos que Shopify Catalog comparte con los canales de compra con agentes que hayas activado.

### ¿Dónde está el sitemap de mi tienda en WooCommerce?
Desde WordPress 5.5, en `/wp-sitemap.xml`. Los plugins de SEO pueden publicar otro, así que mira cuál incluye tus productos.

### ¿Tengo que instalar un plugin para tener JSON-LD de producto?
WooCommerce incluye una clase que genera JSON-LD. Comprueba en el código fuente lo que sale en tu caso antes de instalar nada.

### ¿Y si mi plataforma no aparece en la lista?
Haz las cuatro comprobaciones del principio. Son independientes de la plataforma.

## Sources

- [Shopify: editar robots.txt.liquid](https://help.shopify.com/en/manual/promoting-marketing/seo/editing-robots-txt)
- [Shopify: encontrar y enviar tu sitemap](https://help.shopify.com/en/manual/promoting-marketing/seo/find-site-map)
- [Shopify: optimizar tu tienda para la IA](https://help.shopify.com/en/manual/promoting-marketing/seo/optimizing-store-for-ai)
- [WordPress: filtro robots_txt](https://developer.wordpress.org/reference/hooks/robots_txt/)
- [WordPress: pantalla Lectura](https://wordpress.org/documentation/article/settings-reading-screen/)
- [WordPress Core: sitemaps XML en WordPress 5.5](https://make.wordpress.org/core/2020/07/22/new-xml-sitemaps-functionality-in-wordpress-5-5/)
- [WooCommerce: clase WC_Structured_Data en GitHub](https://github.com/woocommerce/woocommerce/blob/trunk/plugins/woocommerce/includes/class-wc-structured-data.php)
