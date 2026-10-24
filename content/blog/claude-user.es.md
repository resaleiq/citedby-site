title: Claude-User: qué hace y qué cambia si lo bloqueas
h1: Claude-User: qué hace y qué cambia si lo bloqueas
description: Claude-User (Anthropic): consulta iniciada por el usuario. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición.
slug: claude-user
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Cuatro datos sobre Claude-User: operador Anthropic, función Consulta iniciada por el usuario, respeta robots.txt Sí, lista de direcciones Lista, no para bloquear
hero_sub: Claude-User, de Anthropic
hero_boxes: Operador|Anthropic; Función|Consulta iniciada por el usuario; Respeta robots.txt|Sí; Lista de direcciones|Lista, no para bloquear
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/claude-searchbot|Claude-SearchBot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: Claude-User es el agente que Claude puede usar para acceder a un sitio web cuando una persona le hace una pregunta. Anthropic dice que desactivarlo impide recuperar tu contenido en respuesta a una consulta del usuario, lo que puede reducir tu visibilidad en la búsqueda web dirigida por el usuario. Es independiente de ClaudeBot y Claude-SearchBot.

## Qué es Claude-User

De los tres robots de Anthropic, Claude-User es el que va ligado a la pregunta de una persona. No recoge datos de entrenamiento (eso lo hace [ClaudeBot](/es/bots/claudebot)) y no construye el índice de búsqueda (eso lo hace [Claude-SearchBot](/es/bots/claude-searchbot)).

| Dato | Claude-User |
| --- | --- |
| Operador | Anthropic |
| Función | Consulta iniciada por el usuario |
| Token de robots.txt | `Claude-User` |
| Respeta robots.txt | Sí, Anthropic dice que sus robots respetan robots.txt |
| Direcciones IP | El proveedor remite a una lista pero desaconseja bloquear por IP |
| Página del proveedor leída el | 21 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “Claude-User supports Claude AI users. When individuals ask questions to Claude, it may access websites using a Claude-User agent. Claude-User allows site owners to control which sites can be accessed through these user-initiated requests. Disabling Claude-User on your site prevents our system from retrieving your content in response to a user query, which may reduce your site's visibility for user-directed web search.”

Fuente: [Anthropic Help Center: Does Anthropic crawl data from the web, and how can site owners block the crawler? (7 April 2026)](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler), leído el 21 de octubre de 2026.

## Qué pasa si bloqueas Claude-User

Aquí es donde la redacción de Anthropic sobre el coste es más directa: desactivar Claude-User impide la recuperación «en respuesta a una consulta del usuario» y «puede reducir la visibilidad de tu sitio en la búsqueda web dirigida por el usuario». Una tienda que lo bloquea puede seguir siendo conocida por el modelo a través de otras fuentes, pero Claude no puede abrir la página cuando se le pide.

## Las líneas de robots.txt

Para permitir Claude-User:

```
User-agent: Claude-User
Allow: /
```

Para bloquear Claude-User:

```
User-agent: Claude-User
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La página del proveedor no muestra una cadena user-agent completa para Claude-User.

## Cómo distinguir una petición real de una falsa

El artículo de ayuda de Anthropic no incluye una cadena de user-agent para los tres robots y dice que sus direcciones IP de origen están en una lista que enlaza. Como Anthropic dice también que bloquear esas direcciones puede impedir que sus robots lean robots.txt, el consejo del artículo es controlar el acceso en robots.txt y no en la capa de IP.

## Compara con Claude-SearchBot

[Claude-SearchBot](/es/bots/claude-searchbot): Robot de calidad de búsqueda; su bloqueo afecta a la indexación para la búsqueda, no a la pregunta en directo de un usuario.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). Claude-User no es uno de ellos: lee tu robots.txt buscando un grupo `Claude-User` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿Claude-User respeta robots.txt?

Sí, Anthropic dice que sus robots respetan robots.txt. Dale a Claude-User su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que Claude-User está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Anthropic Help Center: Does Anthropic crawl data from the web, and how can site owners block the crawler? (7 April 2026)](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)
