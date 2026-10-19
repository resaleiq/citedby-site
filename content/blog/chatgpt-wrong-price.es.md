title: ChatGPT muestra un precio antiguo de mi producto: cómo corregirlo
h1: ChatGPT muestra mi precio antiguo. Cómo encontrar de dónde lo lee y corregirlo
description: ChatGPT cita un precio que cambiaste hace meses. Las tres fuentes posibles (tu página, tu feed y otras webs), cómo rastrearlas y cómo volver a comprobarlo.
slug: chatgpt-wrong-price
locale: es
cluster: Datos erróneos
date: 2026-10-20
reviewed: 2026-10-20
hero: auto
hero_alt: Tarjeta con el título ChatGPT muestra mi precio antiguo y tres cuadros: tu propia página, tu feed de productos y otras webs
hero_sub: Tres fuentes posibles del precio viejo
hero_boxes: Tu página|Texto y JSON-LD; Tu feed|Catálogo de productos; Otras webs|Listados y reseñas
widget: on
howto: on
steps_img: on
related: /es/blog/check-what-ai-says-about-your-brand|Qué dice la IA de tu marca; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web?; /es/ai-visibility-audit|Auditoría de visibilidad en IA
answer: ChatGPT muestra un precio antiguo cuando lo leyó de una fuente desactualizada: tu propia página, un feed de productos u otra web. Busca el precio viejo en cada sitio, corrige la fuente y vuelve a preguntar dos veces en un chat nuevo. Actualiza tu feed cada vez que empiece o termine una oferta.

## ¿Por qué un asistente cita un precio que ya cambiaste?

Un asistente responde con lo que encuentra: páginas que visitó, feeds que envió un comerciante y páginas de terceros que te mencionan. Si una de esas fuentes conserva la cifra antigua, la respuesta puede llevarla también.

Eso convierte un precio erróneo en un problema de datos en una página que controlas o a cuyo dueño puedes escribir, y por eso tiene arreglo. La corrección se hace en la fuente, no en el chat.

## Paso 1: ¿cómo anoto la respuesta equivocada?

Abre un chat nuevo, con la búsqueda web activada si el asistente la ofrece, y pregunta: "¿Cuánto cuesta [producto] de [tienda]?". Copia la respuesta, la fecha, el asistente y cualquier enlace que cite.

Un enlace citado es la mejor pista, porque señala la página que alimentó la respuesta. Pregunta una segunda vez en otro chat nuevo. Si las dos respuestas difieren, apunta ambas: las respuestas varían de una ejecución a otra.

## Paso 2: ¿cómo busco el precio antiguo en mi propia página?

1. Abre el código fuente: entra en la ficha del producto y elige "Ver código fuente de la página" con el botón derecho.
2. Busca el precio viejo: por ejemplo `49,00` o `49.00`, con y sin el símbolo del euro.
3. Lee el bloque de datos estructurados: localiza el bloque `application/ld+json` y mira el precio dentro de `offers`. Un marcado de producto que nunca se actualizó es un motivo frecuente de cifras antiguas.
4. Busca un segundo precio: mira si la página tiene un precio "antes", un precio de pack o una variante que carga otro importe.
5. Pide la página como un rastreador: sin JavaScript. Si el precio solo aparece cuando se ejecutan los scripts, un rastreador puede no ver la cifra final.

## Paso 3: ¿cómo reviso mi feed de productos?

Si vendes por Google Shopping, un marketplace o el feed de compras de ChatGPT, el feed es una segunda copia de tu precio. La especificación de feed de producto de OpenAI pide un precio con el formato `79.99 USD`, una fila por artículo o variante comprable, y dice que hay que actualizar el feed cuando empieza o termina una oferta ([especificación de OpenAI](https://developers.openai.com/commerce/specs/feed)).

Una oferta que ya terminó en tu web pero sigue en el feed es el desajuste clásico. Si usas una plataforma de tienda, mira en sus ajustes cómo se genera y cada cuánto se reenvía el feed.

La página de OpenAI no describe un modo de impugnar datos que ya se han recogido, así que no prometemos ninguno.

## Paso 4: ¿cómo busco el precio antiguo en otras webs?

Busca el precio viejo junto con el nombre de tu marca y el del producto. Mira webs de opiniones, listas de precios, comparadores, entradas antiguas de blogs y tus propias notas de prensa. Pide al dueño de cada página que lo actualice.

Donde no puedas, publica en tu web una página actual que indique el precio con su fecha, para que la fuente más reciente sea también la más clara.

## Paso 5: ¿cuánto hay que esperar y cómo vuelvo a preguntar?

OpenAI dice que un cambio en robots.txt puede tardar unas 24 horas en llegar a su rastreador de búsqueda ([documentación de OpenAI](https://developers.openai.com/api/docs/bots)). No publica un calendario para refrescar una página que ya leyó, así que nadie puede prometerte una fecha.

Repite la misma pregunta dos veces, en chats nuevos, una vez por semana, y apunta cada respuesta en una tabla como esta.

| Fecha | Asistente | Pregunta | Precio mostrado | Enlace citado | ¿Coincide con tu página? |
| --- | --- | --- | --- | --- | --- |
| 2026-10-20 | ChatGPT, con búsqueda | ¿Cuánto cuesta [producto] de [tienda]? | | | |

## ¿Puede la auditoría encontrar este problema?

La auditoría de CitedBy rastrea tus páginas y prueba si los rastreadores de IA pueden llegar a ellas y leer tus datos de producto, desde 9 €. Si tu página de precio está bloqueada o vacía para un rastreador, ninguna corrección del precio servirá, así que prueba eso primero.

## FAQ

### ¿Por qué ChatGPT muestra un precio antiguo de mi producto?
Probablemente leyó la cifra antigua en tu página, en tu feed de productos o en otra web que todavía la conserva. Busca el precio viejo en cada sitio y mira el enlace que cita, si lo hay.

### ¿Cuánto tarda ChatGPT en mostrar el precio nuevo?
Nadie puede prometer una fecha. OpenAI dice que los cambios en robots.txt tardan unas 24 horas en llegar a su rastreador de búsqueda y no da un calendario de refresco para páginas ya leídas. Vuelve a preguntar cada semana y apunta las respuestas.

### ¿Puedo pedirle a OpenAI que corrija un precio erróneo?
La especificación de feed de OpenAI no describe un modo de corregir datos ya recogidos, así que corrige las fuentes y vuelve a comprobar. Mira en el centro de ayuda de OpenAI si existe alguna opción de reporte cuando leas esto.

### ¿Importa el precio en el marcado de datos estructurados?
Sí, cuando está desactualizado. Un bloque de marcado que nunca se actualizó es un desajuste habitual que conviene buscar.

## Sources

- [OpenAI: especificación del feed de productos](https://developers.openai.com/commerce/specs/feed)
- [OpenAI: rastreadores y agentes de usuario](https://developers.openai.com/api/docs/bots)
- [CitedBy: auditoría de tu web](https://citedby.eu/)
