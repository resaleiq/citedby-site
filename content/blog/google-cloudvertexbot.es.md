title: Google-CloudVertexBot: qué hace y qué cambia si lo bloqueas
h1: Google-CloudVertexBot: qué hace y qué cambia si lo bloqueas
description: Google-CloudVertexBot (Google): varias funciones. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: google-cloudvertexbot
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre Google-CloudVertexBot: operador Google, función Varias funciones, respeta robots.txt Sí, lista de direcciones 317 rangos
hero_sub: Google-CloudVertexBot, de Google
hero_boxes: Operador|Google; Función|Varias funciones; Respeta robots.txt|Sí; Lista de direcciones|317 rangos
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/googlebot|Googlebot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: Google-CloudVertexBot es un rastreador de Google que hace los rastreos que piden los propietarios de sitios para crear Vertex AI Agents. Google lo incluye entre sus rastreadores comunes, que siempre obedecen robots.txt cuando rastrean de forma automática. Google dice que las reglas dirigidas a él no afectan a Google Search ni a otros productos de Google.

## Qué es Google-CloudVertexBot

Google-CloudVertexBot es un rastreador de Google incluido entre sus rastreadores comunes. Google dice que hace los rastreos que piden los propietarios de sitios para crear Vertex AI Agents. Google lo muestra como una subcadena de agente de usuario, no como una cadena de agente de usuario completa.

| Dato | Google-CloudVertexBot |
| --- | --- |
| Operador | Google |
| Función | Rastreo pedido por propietarios de sitios para Vertex AI Agents |
| Token de robots.txt | `Google-CloudVertexBot` |
| Respeta robots.txt | Sí. Google dice que los rastreadores comunes siempre obedecen las reglas de robots.txt cuando rastrean de forma automática. |
| Direcciones IP | 317 rangos (developers.google.com/static/crawling/ipranges/common-crawlers.json, archivo del 2026-10-23) |
| Página del proveedor leída el | 24 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “Crawling preferences addressed to the Google-CloudVertexBot user agent affect crawls requested by the site owners' for building Vertex AI Agents”

Fuente: [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers), leído el 24 de octubre de 2026.

## Qué pasa si bloqueas Google-CloudVertexBot

Google dice que las preferencias dirigidas al agente de usuario Google-CloudVertexBot afectan a los rastreos que piden los propietarios de sitios para crear Vertex AI Agents. Dice que esto no afecta a Google Search ni a otros productos.

## Las líneas de robots.txt

Para permitir Google-CloudVertexBot:

```
User-agent: Google-CloudVertexBot
Allow: /
```

Para bloquear Google-CloudVertexBot:

```
User-agent: Google-CloudVertexBot
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
Google-CloudVertexBot
```

## Cómo distinguir una petición real de una falsa

El archivo developers.google.com/static/crawling/ipranges/common-crawlers.json tenía 317 rangos el 24 de octubre de 2026, archivo del 2026-10-23.

Google dice que los rastreadores comunes por lo general rastrean desde los rangos de common-crawlers.json y que el nombre de DNS inverso coincide con crawl-***-***-***-***.googlebot.com o geo-crawl-***-***-***-***.geo.googlebot.com.

## Compara con Googlebot

[Googlebot](/es/bots/googlebot): Googlebot rastrea para Google Search, mientras que Google-CloudVertexBot solo rastrea cuando un propietario de sitio ha pedido un rastreo para crear Vertex AI Agents.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). Google-CloudVertexBot no es uno de ellos: lee tu robots.txt buscando un grupo `Google-CloudVertexBot` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿Google-CloudVertexBot respeta robots.txt?

Sí. Google dice que los rastreadores comunes siempre obedecen las reglas de robots.txt cuando rastrean de forma automática. Dale a Google-CloudVertexBot su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que Google-CloudVertexBot está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers)
- [Google: common-crawlers.json (read 2026-10-24, creationTime 2026-10-23)](https://developers.google.com/static/crawling/ipranges/common-crawlers.json)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
