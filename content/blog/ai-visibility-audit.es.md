title: Auditoría de visibilidad en IA para tu web (GEO y AEO)
h1: Auditoría de visibilidad en IA: qué revisa y qué recibes
description: Una auditoría de visibilidad en IA comprueba si los rastreadores de IA llegan a tus páginas y las leen. Qué revisa, qué entrega y cuánto cuesta, desde 9 €.
slug: ai-visibility-audit
section: root
locale: es
cluster: Auditoría
date: 2026-10-20
reviewed: 2026-10-20
hero: auto
hero_alt: Tarjeta con el título auditoría de visibilidad en IA y tres cuadros: acceso de rastreadores, HTML legible y datos estructurados
hero_sub: Qué revisamos página por página
hero_boxes: Acceso de rastreadores|robots.txt y firewall; HTML legible|Texto sin JavaScript; Datos estructurados|JSON-LD de producto; Calidad de respuesta|Precio, envío y FAQ
widget: on
howto: off
steps_img: on
related: /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web?; /es/blog/is-gptbot-blocked|¿Está bloqueado GPTBot en tu web?; /es/guides/technical-seo-checklist|Lista de comprobación técnica
answer: Una auditoría de visibilidad en IA, también llamada auditoría GEO o AEO, comprueba si los rastreadores de IA pueden llegar a tus páginas y leerlas, y si cada página responde con claridad a la pregunta de un comprador. CitedBy rastrea tu web hasta el límite de páginas de tu plan y te da la corrección exacta de cada problema.

## ¿Qué es una auditoría de visibilidad en IA?

Es una revisión técnica y de contenido de tu tienda online pensada para los asistentes que responden preguntas de compra, como ChatGPT, Perplexity o Gemini. Responde a dos cuestiones. La primera: ¿pueden sus rastreadores entrar en tus páginas y leer el texto? La segunda: ¿dice cada página, cerca del principio, lo que un comprador pregunta?

GEO (optimización para motores generativos) y AEO (optimización para motores de respuesta) describen en la práctica el mismo trabajo: que te lean y te nombren en las respuestas de la IA. Si lo que buscas son referencias académicas, CitedBy no sirve para eso: auditamos sitios web, no formateamos citas.

## ¿Qué revisa la auditoría, página por página?

1. Acceso de los rastreadores: comprobamos si tu `robots.txt` deja entrar a GPTBot, OAI-SearchBot y PerplexityBot, si tu firewall o tu CDN los bloquean y qué código de estado devuelve cada página.
2. HTML legible: una página que llega vacía hasta que se ejecuta JavaScript no muestra nada a la mayoría de los rastreadores. Comparamos el texto legible con el tamaño de la página y marcamos las vacías.
3. llms.txt y sitemap: miramos si existe `llms.txt` y si tu sitemap lista las páginas que quieres que se lean. Ningún asistente importante ha confirmado que lea llms.txt, así que lo marcamos como opcional.
4. Datos estructurados: el marcado JSON-LD de Organization, Product, FAQ y Article indica a las máquinas cuál es el precio y cuál es el texto de respuesta.
5. Títulos, encabezados y enlaces: revisamos títulos y descripciones que faltan o se repiten, H1, orden de los encabezados, canonicals, hreflang y enlaces internos rotos.
6. Calidad de la respuesta: miramos si la página responde a la pregunta del comprador al principio y si tienes las páginas que suelen citarse: FAQ, precios, comparativas y quiénes somos.

## ¿Qué recibes al terminar?

Una puntuación de salud de toda la web, los problemas agrupados por gravedad con las páginas que afecta cada uno, una vista página por página y una corrección lista para pegar en cada caso: la etiqueta, la línea de `robots.txt` o el bloque de datos estructurados.

Cuando cambies algo, puedes volver a rastrear y ver cómo se mueve la puntuación. Las agencias pueden añadir un PDF con marca blanca y gestionar muchas webs de clientes. Cada corrección indica la página a la que afecta, para que sepas dónde tocar.

Además, nuestras [páginas de datos](/data) muestran qué sitios enlazó ChatGPT, pregunta a pregunta, con el CSV completo. Y en el [informe de muestra](/es/sample) puedes ver cómo se presenta el resultado. ¿Quieres probar primero? La [revisión gratis de visibilidad en IA](/es/free-ai-visibility-check) lee hasta 10 páginas, sin cuenta.

## ¿Cuánto cuesta la auditoría?

Una auditoría suelta cuesta 9 €, con pago único antes del rastreo y garantía de devolución de 14 días. Los planes mensuales desde 19 € vuelven a rastrear tu web con la frecuencia que elijas. No hay plan gratuito.

## ¿Qué puedes comprobar a mano antes de pagar?

Tres cosas llevan un par de minutos y no cuestan nada. Abre `tutienda.es/robots.txt` y busca un `Disallow: /` bajo `User-agent: *`. Abre una página de producto, elige "Ver código fuente de la página" y busca el nombre del producto: si no aparece, el texto lo añade JavaScript. Y busca un bloque `application/ld+json` con el precio.

Si prefieres hacerlo por tu cuenta y con calma, tienes la [lista de comprobación técnica](/es/guides/technical-seo-checklist) y la explicación de [qué hace que ChatGPT pueda leer tu web](/es/blog/can-chatgpt-read-my-website).

## FAQ

### ¿Son lo mismo GEO, AEO y visibilidad en IA?
En la práctica sí. GEO, AEO y visibilidad en IA describen el trabajo de que te lean y te nombren en las respuestas de los asistentes.

### ¿Es CitedBy una herramienta de citas académicas?
No. CitedBy audita sitios web. No da formato ni comprueba referencias académicas.

### ¿Puedes prometerme que ChatGPT nombrará mi web?
No. Nadie controla lo que responde un asistente. La auditoría encuentra lo que bloquea o debilita tus páginas y te da la corrección.

### ¿Hay una versión gratuita?
No. La auditoría cuesta 9 € una vez, con garantía de devolución de 14 días.

## Sources

- [OpenAI: rastreadores y agentes de usuario](https://developers.openai.com/api/docs/bots)
- [Google Search Central: funciones de IA y tu sitio web](https://developers.google.com/search/docs/appearance/ai-features)
- [llmstxt.org: la propuesta llms.txt](https://llmstxt.org/)
- [CitedBy: informe de muestra](https://citedby.eu/sample-audit)
