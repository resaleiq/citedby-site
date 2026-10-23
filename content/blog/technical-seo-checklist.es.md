title: Lista de comprobación de SEO técnico para visibilidad en IA
h1: SEO técnico para visibilidad en IA: 10 comprobaciones para tu tienda online
description: Diez comprobaciones técnicas que puedes hacer a mano para que los rastreadores de IA lleguen a las páginas de tu tienda online y las lean.
slug: technical-seo-checklist
section: guides
locale: es
cluster: Guías
date: 2026-10-20
reviewed: 2026-10-20
hero: auto
hero_alt: Tarjeta con el título SEO técnico para visibilidad en IA y cuatro cuadros: rastreadores, estado HTTP, HTML legible y datos estructurados
hero_sub: Diez comprobaciones, cada una con su prueba
hero_boxes: Rastreadores|robots.txt y bloqueos; Estado HTTP|Páginas clave; HTML legible|Texto sin JavaScript; Datos|JSON-LD de producto
widget: on
howto: on
steps_img: on
related: /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web?; /es/blog/does-llms-txt-work|¿Sirve llms.txt?; /es/guides/cms|Guía para Shopify, WooCommerce y otras plataformas
answer: Para que una IA lea tu tienda online, comprueba diez cosas: robots.txt y los rastreadores de IA, el código de estado de tus páginas clave, el sitemap, el canonical, hreflang, título y H1, datos JSON-LD, texto presente en el HTML sin JavaScript, enlaces rotos y, como opcional, llms.txt. Todas se verifican a mano.

## ¿Qué comprobaciones técnicas importan para la IA?

Un asistente solo puede nombrar tu tienda online si antes ha podido llegar a tus páginas y leerlas. Esta lista ordena diez comprobaciones técnicas, de las que más bloquean a las que menos, y dice cómo verificar cada una sin herramientas especiales. Ninguna garantiza que te nombren: son la condición para que sea posible.

## Las diez comprobaciones, una a una

1. Revisa los rastreadores de IA en robots: abre `tutienda.es/robots.txt` y busca reglas para `OAI-SearchBot`, `GPTBot`, `PerplexityBot`, `Google-Extended` y `Bingbot`. Un `Disallow: /` bajo `User-agent: *` afecta a los rastreadores sin regla propia ([RFC 9309](https://www.rfc-editor.org/info/rfc9309/)). OpenAI indica que cada uno de sus rastreadores se controla por separado ([OpenAI](https://developers.openai.com/api/docs/bots)).
2. Comprueba el código de estado: abre la portada, una categoría y un producto, y mira el código HTTP de cada una (las herramientas para desarrolladores del navegador lo muestran en la pestaña Red). Debe ser 200. Un 403, un 429 o un 503 tampoco ayudan a un rastreador. Para el caso de un bloqueo en el servidor, mira [¿Está bloqueado GPTBot en tu web?](/es/blog/is-gptbot-blocked).
3. Localiza el sitemap: abre `tutienda.es/sitemap.xml`, comprueba que lista tus productos y categorías y que no incluye páginas que quieras ocultar. Google explica qué es y cómo se construye en su [guía de sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview).
4. Mira el canonical: en el código fuente de una ficha, busca `rel="canonical"`. Debe apuntar a la dirección que quieres que se lea, y no a otra variante con parámetros. Google lo explica en [consolidar URL duplicadas](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls).
5. Revisa hreflang si vendes en varios idiomas: por ejemplo, una versión para España y otra para Portugal. Según Google, cada versión debe listarse a sí misma y a todas las demás, con direcciones completas ([versiones localizadas](https://developers.google.com/search/docs/specialty/international/localized-versions)).
6. Comprueba el título y el H1: cada página debe tener un título propio y un solo H1 que diga qué es. Busca duplicados en tus fichas de producto ([Google: títulos](https://developers.google.com/search/docs/appearance/title-link)).
7. Busca los datos JSON-LD: en el código fuente, localiza el bloque `application/ld+json` con `Product` (nombre, precio, disponibilidad) en las fichas y `Organization` en la portada ([Google: datos de producto](https://developers.google.com/search/docs/appearance/structured-data/product)). El precio del marcado debe coincidir con el de la página.
8. Verifica que el texto está en el HTML: abre "Ver código fuente de la página" y busca el nombre y el precio de un producto. Si no aparecen, la página los construye con JavaScript y un rastreador que no lo ejecuta verá una página vacía ([Google: JavaScript y SEO](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)).
9. Busca enlaces internos rotos: recorre el menú, las categorías y los enlaces de las fichas. Un enlace que devuelve 404 corta el camino a lo que hay detrás.
10. Valora el archivo opcional para IA: llms.txt es opcional. Ningún asistente importante ha confirmado que lo lea; el detalle está en [¿Sirve llms.txt?](/es/blog/does-llms-txt-work).

## ¿Qué prioridad tiene cada comprobación?

| Comprobación | Si falla | Prioridad |
| --- | --- | --- |
| robots.txt y rastreadores | Los asistentes no pueden entrar | Alta |
| Código de estado | La página no se lee | Alta |
| Texto en el HTML | El rastreador ve una página vacía | Alta |
| Datos JSON-LD | Precio y nombre menos claros para las máquinas | Media |
| Sitemap, canonical, hreflang | Páginas que faltan o se duplican | Media |
| Título, H1, enlaces rotos | Menos claridad y caminos cortados | Media |
| llms.txt | Sin efecto demostrado | Baja |

## ¿Se puede hacer todo esto a la vez?

Las diez comprobaciones llevan una tarde en una tienda pequeña. La auditoría de CitedBy, desde 9 €, rastrea tu web hasta el límite de páginas de tu plan y revisa estos puntos en cada página rastreada, con la corrección exacta para cada problema. Puedes ver el formato en el [informe de muestra](/es/sample) o leer qué revisa en [Auditoría de visibilidad en IA](/es/ai-visibility-audit).

Para las instrucciones por plataforma (Shopify, WooCommerce y otras) tienes la [guía por plataformas](/es/guides/cms).

## FAQ

### ¿Qué compruebo primero?
Los rastreadores de IA en robots.txt y el código de estado de tus páginas clave. Si un rastreador no puede entrar, el resto de comprobaciones no sirve de nada.

### ¿Hace falta un sitemap para que la IA me lea?
No es un requisito demostrado para los asistentes de IA, pero ayuda a los buscadores a descubrir tus páginas y es una comprobación de higiene sencilla.

### ¿Los datos JSON-LD hacen que me citen?
No hay garantía. Indican a las máquinas qué número es el precio y qué texto es la respuesta, así que reducen errores, pero no deciden si te nombran.

### ¿Debo crear un archivo llms.txt?
Es opcional y, con los datos actuales, no mueve las citas. Hazlo después de lo básico, si te apetece.

## Sources

- [IETF RFC 9309: protocolo de exclusión de robots](https://www.rfc-editor.org/info/rfc9309/)
- [OpenAI: rastreadores y agentes de usuario](https://developers.openai.com/api/docs/bots)
- [Google Search Central: sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview)
- [Google Search Central: consolidar URL duplicadas](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- [Google Search Central: versiones localizadas (hreflang)](https://developers.google.com/search/docs/specialty/international/localized-versions)
- [Google Search Central: títulos](https://developers.google.com/search/docs/appearance/title-link)
- [Google Search Central: datos estructurados de producto](https://developers.google.com/search/docs/appearance/structured-data/product)
- [Google Search Central: fundamentos de JavaScript y SEO](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
