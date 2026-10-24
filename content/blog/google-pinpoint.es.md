title: Google-Pinpoint: qué hace y qué cambia si lo bloqueas
h1: Google-Pinpoint: qué hace y qué cambia si lo bloqueas
description: Google-Pinpoint (Google): consulta iniciada por el usuario. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición.
slug: google-pinpoint
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre Google-Pinpoint: operador Google, función Consulta iniciada por el usuario, respeta robots.txt No siempre, lista de direcciones DNS inverso
hero_sub: Google-Pinpoint, de Google
hero_boxes: Operador|Google; Función|Consulta iniciada por el usuario; Respeta robots.txt|No siempre; Lista de direcciones|DNS inverso
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/google-gemininotebook|Google-GeminiNotebook; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: Google-Pinpoint es un agente de consultas iniciadas por el usuario que Google incluye en su lista. Solicita URL concretas que los usuarios de Pinpoint indicaron como fuentes de sus colecciones personales de documentos. Google dice que estos agentes por lo general ignoran robots.txt porque la consulta la pidió un usuario, y no documenta ningún token para él.

## Qué es Google-Pinpoint

Google-Pinpoint es un agente de consultas iniciadas por el usuario que Google incluye en su lista. Solicita URL concretas que los usuarios de Pinpoint indicaron como fuentes de sus colecciones personales de documentos. Google lo enumera con el agente de usuario Google-Pinpoint.

| Dato | Google-Pinpoint |
| --- | --- |
| Operador | Google |
| Función | Consulta iniciada por el usuario |
| Token de robots.txt | `Google-Pinpoint` |
| Respeta robots.txt | Parcial. Google dice que los agentes de consultas iniciadas por el usuario por lo general ignoran las reglas de robots.txt porque la consulta la pidió un usuario. |
| Direcciones IP | Comprobación por DNS inverso |
| Página del proveedor leída el | 24 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “The Google-Pinpoint fetcher requests individual URLs that Pinpoint users specified as sources for their personal collections of documents.”

Fuente: [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers), leído el 24 de octubre de 2026.

## Qué pasa si bloqueas Google-Pinpoint

Google dice que, como la consulta la pidió un usuario, los agentes de consultas iniciadas por el usuario por lo general ignoran las reglas de robots.txt. La página de Google no documenta ningún token de robots.txt para Google-Pinpoint.

## Las líneas de robots.txt

Para permitir Google-Pinpoint:

```
User-agent: Google-Pinpoint
Allow: /
```

Para bloquear Google-Pinpoint:

```
User-agent: Google-Pinpoint
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
Google-Pinpoint
```

## Cómo distinguir una petición real de una falsa

Google dice que los agentes de consultas iniciadas por el usuario publican rangos de IP en user-triggered-fetchers.json, user-triggered-fetchers-google.json y user-triggered-agents.json, y que la máscara de DNS inverso coincide con ***-***-***-***.gae.googleusercontent.com o google-proxy-***-***-***-***.google.com, según si el agente es de Google o del usuario.

## Compara con Google-GeminiNotebook

[Google-GeminiNotebook](/es/bots/google-gemininotebook): Ambos obtienen URL que los usuarios aportaron como fuentes en un producto de Google, y ambos entran en las reglas de Google para los agentes de consultas iniciadas por el usuario.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). Google-Pinpoint no es uno de ellos: lee tu robots.txt buscando un grupo `Google-Pinpoint` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿Google-Pinpoint respeta robots.txt?

No siempre. Parcial. Google dice que los agentes de consultas iniciadas por el usuario por lo general ignoran las reglas de robots.txt porque la consulta la pidió un usuario. Por eso una regla para Google-Pinpoint en robots.txt puede no detenerlo. Para rechazarlo con seguridad, usa una regla de cortafuegos o de CDN que combine el user agent y las direcciones publicadas.

### ¿Cómo sé que Google-Pinpoint está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
