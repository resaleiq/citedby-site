title: ¿Puede ChatGPT leer mi web? Qué lo decide
h1: ¿Puede ChatGPT leer mi web?
description: Tres cosas deciden si ChatGPT y otros asistentes de IA leen tu tienda online: robots.txt, el texto del HTML y los datos estructurados. Cómo revisarlas.
slug: can-chatgpt-read-my-website
locale: es
cluster: Rastreo
date: 2026-10-20
reviewed: 2026-10-20
hero: auto
hero_alt: Tres puertas entre la página de una tienda y un asistente de IA: robots.txt, texto de la página y datos estructurados
hero_sub: Tres puertas entre tu tienda y la IA
hero_boxes: robots.txt|Quién puede entrar; Respuesta|Qué devuelve el servidor; Contenido|Texto en el HTML
widget: on
howto: on
steps_img: on
related: /es/ai-visibility-audit|Auditoría de visibilidad en IA; /es/blog/is-gptbot-blocked|¿Está bloqueado GPTBot en tu web?; /es/blog/check-what-ai-says-about-your-brand|Qué dice la IA de tu marca
answer: ChatGPT puede leer tu web si se cumplen tres cosas: robots.txt no bloquea a OAI-SearchBot, el texto de la página está en el HTML que envía tu servidor y no lo añade JavaScript, y tu servidor o cortafuegos no rechaza al rastreador. La auditoría de CitedBy comprueba las dos primeras en cada página.

## ¿Cuáles son las tres puertas?

La búsqueda de ChatGPT usa un rastreador llamado OAI-SearchBot para encontrar páginas. OpenAI también tiene GPTBot, que recopila datos de entrenamiento, y ChatGPT-User, que visita una página cuando una persona pregunta por ella. Según OpenAI, cada uno se controla por separado en robots.txt, de modo que puedes permitir uno y bloquear otro ([documentación de OpenAI](https://developers.openai.com/docs/bots)).

Las tres puertas son: lo que dice robots.txt, lo que responde tu servidor y lo que contiene la página que llega. Si una falla, las otras dos dan igual: un asistente no puede nombrar lo que no ha podido leer.

## ¿Cómo comprobarlo, paso a paso?

1. Abre el archivo de robots: escribe `tutienda.es/robots.txt` en el navegador y busca `User-agent: OAI-SearchBot`, `GPTBot` o `*` seguido de `Disallow: /`. Un `Disallow: /` general bajo `User-agent: *` bloquea a todos los rastreadores que no tengan una regla propia.
2. Audita tu web: la auditoría de CitedBy, desde 9 €, lee robots.txt para OAI-SearchBot, GPTBot, PerplexityBot, Google-Extended y Bingbot y te dice cuáles están bloqueados.
3. Mira el recuento de palabras: la auditoría informa del texto que hay en el HTML de la página. Tu página de inicio debería tener cientos de palabras ahí, con el nombre de tu marca y lo que vendes.
4. Busca tu producto en el código fuente: abre la página, elige "Ver código fuente de la página" y busca el nombre de un producto. Si no aparece, la página construye su texto con JavaScript y un rastreador que no ejecuta scripts no ve nada.
5. Comprueba los datos de Organization: confirma que hay JSON-LD de Organization, para que los asistentes obtengan tu nombre, tu logotipo y tus datos de contacto en un solo sitio.

## ¿Cómo ve una página un rastreador que no ejecuta JavaScript?

Algunos temas de tienda y creadores de webs envían una página casi vacía y la rellenan con JavaScript. Un visitante ve una ficha de producto completa. Un rastreador que no ejecuta JavaScript recibe un cascarón.

Algunos asistentes ejecutan JavaScript y otros no, así que lo más seguro es tener el nombre de tu marca y el texto de tus productos en el propio HTML.

## ¿Qué puerta no puede ver la auditoría?

robots.txt es una petición, y el que lo hace cumplir es tu hosting. Un ajuste del cortafuegos o del CDN puede responder con un error a un rastreador aunque robots.txt lo permita. La auditoría no prueba esto.

Mira en los registros de tu servidor o de tu CDN las peticiones de `OAI-SearchBot` y los códigos de estado que recibieron. Una serie de respuestas 403 es la señal. En [¿Está bloqueado GPTBot en tu web?](/es/blog/is-gptbot-blocked) tienes una prueba con dos peticiones para detectarlo.

## ¿Qué hacer con el resultado?

| Resultado | Qué hacer |
| --- | --- |
| robots.txt bloquea un rastreador que quieres | Quita la regla `Disallow` correspondiente. OpenAI dice que los cambios pueden tardar un día en aplicarse |
| Pocas palabras en el HTML | Haz que el servidor genere el texto de la página de inicio y de los productos |
| Faltan los datos de Organization | Añádelos como JSON-LD en la página de inicio |
| Todo en orden | Poder leerte es la entrada, no el resultado. Que un asistente nombre tu tienda es otra cuestión, que la auditoría mide con preguntas reales de compradores |

## FAQ

### ¿Es GPTBot lo mismo que la búsqueda de ChatGPT?
No. GPTBot recopila datos que pueden servir para entrenar modelos. OAI-SearchBot es el rastreador de los resultados de búsqueda de ChatGPT. Puedes bloquear GPTBot y permitir OAI-SearchBot.

### Si bloqueo GPTBot, ¿dejará ChatGPT de mencionar mi tienda?
No por sí solo. Los resultados de búsqueda dependen de OAI-SearchBot. Bloquear únicamente GPTBot es una elección habitual en tiendas que no quieren que se use su contenido para entrenar.

### ¿Arregla esto añadir llms.txt?
Es opcional. No esperamos que cambie lo que responden los asistentes y la auditoría lo marca como opcional. Tienes el detalle en [¿Sirve llms.txt?](/es/blog/does-llms-txt-work).

### ¿Cuánto tarda en notarse un cambio?
OpenAI indica que sus sistemas pueden tardar unas 24 horas en ajustarse tras cambiar robots.txt.

## Sources

- [OpenAI: rastreadores y agentes de usuario](https://developers.openai.com/docs/bots)
- [CitedBy: auditoría de tu web](https://citedby.eu/)
