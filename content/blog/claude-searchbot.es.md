title: Claude-SearchBot: qué hace y qué cambia si lo bloqueas
h1: Claude-SearchBot: qué hace y qué cambia si lo bloqueas
description: Claude-SearchBot (Anthropic): búsqueda. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: claude-searchbot
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Cuatro datos sobre Claude-SearchBot: operador Anthropic, función Búsqueda, respeta robots.txt Sí, lista de direcciones Lista, no para bloquear
hero_sub: Claude-SearchBot, de Anthropic
hero_boxes: Operador|Anthropic; Función|Búsqueda; Respeta robots.txt|Sí; Lista de direcciones|Lista, no para bloquear
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/claudebot|ClaudeBot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: Claude-SearchBot es el robot de Anthropic que navega por la web para mejorar la calidad de los resultados de búsqueda. Anthropic dice que desactivarlo impide indexar tu contenido para la optimización de la búsqueda, lo que puede reducir tu visibilidad y precisión en los resultados de búsqueda de los usuarios. Su token de robots.txt es Claude-SearchBot.

## Qué es Claude-SearchBot

Claude-SearchBot es la parte de indexación de la búsqueda de Anthropic. Anthropic lo describe como un robot que analiza contenido en línea para mejorar la relevancia y la precisión de las respuestas de búsqueda. [ClaudeBot](/es/bots/claudebot) recoge contenido para el entrenamiento y [Claude-User](/es/bots/claude-user) responde a una pregunta en directo.

| Dato | Claude-SearchBot |
| --- | --- |
| Operador | Anthropic |
| Función | Búsqueda |
| Token de robots.txt | `Claude-SearchBot` |
| Respeta robots.txt | Sí, Anthropic dice que sus robots respetan robots.txt |
| Direcciones IP | El proveedor remite a una lista pero desaconseja bloquear por IP |
| Página del proveedor leída el | 21 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “Claude-SearchBot navigates the web to improve search result quality for users. It analyzes online content specifically to enhance the relevance and accuracy of search responses. Disabling Claude-SearchBot on your site prevents our system from indexing your content for search optimization, which may reduce your site's visibility and accuracy in user search results.”

Fuente: [Anthropic Help Center: Does Anthropic crawl data from the web, and how can site owners block the crawler? (7 April 2026)](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler), leído el 21 de octubre de 2026.

## Qué pasa si bloqueas Claude-SearchBot

Anthropic nombra dos efectos de desactivarlo: tu contenido no se indexa para la optimización de la búsqueda, y la visibilidad y la precisión de tu sitio en los resultados de búsqueda de los usuarios pueden bajar.

## Las líneas de robots.txt

Para permitir Claude-SearchBot:

```
User-agent: Claude-SearchBot
Allow: /
```

Para bloquear Claude-SearchBot:

```
User-agent: Claude-SearchBot
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La página del proveedor no muestra una cadena user-agent completa para Claude-SearchBot.

## Cómo distinguir una petición real de una falsa

El artículo de ayuda tiene fecha de 7 de abril de 2026. No incluye ninguna cadena de user-agent, así que una línea de registro que nombre Claude-SearchBot es una afirmación que no puedes confirmar solo con el artículo. Anthropic dice que el tráfico de una dirección de su lista enlazada es de Anthropic, y pide a los propietarios de sitios que crean que un robot se comporta mal que escriban desde un correo electrónico del dominio afectado.

## Compara con ClaudeBot

[ClaudeBot](/es/bots/claudebot): Bloquear ClaudeBot excluye solo del entrenamiento; no te quita del índice de búsqueda de Claude.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). Claude-SearchBot no es uno de ellos: lee tu robots.txt buscando un grupo `Claude-SearchBot` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿Claude-SearchBot respeta robots.txt?

Sí, Anthropic dice que sus robots respetan robots.txt. Dale a Claude-SearchBot su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que Claude-SearchBot está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Anthropic Help Center: Does Anthropic crawl data from the web, and how can site owners block the crawler? (7 April 2026)](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)
