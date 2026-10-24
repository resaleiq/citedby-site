title: Google-GeminiNotebook: qué hace y qué cambia si lo bloqueas
h1: Google-GeminiNotebook: qué hace y qué cambia si lo bloqueas
description: Google-GeminiNotebook (Google): consulta iniciada por el usuario. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición.
slug: google-gemininotebook
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre Google-GeminiNotebook: operador Google, función Consulta iniciada por el usuario, respeta robots.txt No siempre, lista de direcciones DNS inverso
hero_sub: Google-GeminiNotebook, de Google
hero_boxes: Operador|Google; Función|Consulta iniciada por el usuario; Respeta robots.txt|No siempre; Lista de direcciones|DNS inverso
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/chatgpt-user|ChatGPT-User; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: Google-GeminiNotebook es el agente de usuario del recuperador de Gemini Notebook. Solicita URL concretas que los usuarios han añadido como fuentes de sus proyectos. Google lo incluye entre los agentes de consultas iniciadas por el usuario, que por lo general ignoran robots.txt porque la consulta la pidió un usuario. La página de Google nombra a Google-NotebookLM como el agente anterior.

## Qué es Google-GeminiNotebook

Google-GeminiNotebook es el agente de usuario del recuperador de Gemini Notebook, que Google incluye entre sus agentes de consultas iniciadas por el usuario. Solicita URL concretas que los usuarios han aportado como fuentes de sus proyectos. La página de Google nombra a Google-NotebookLM como el agente anterior, con soporte hasta agosto de 2026.

| Dato | Google-GeminiNotebook |
| --- | --- |
| Operador | Google |
| Función | Consulta iniciada por el usuario |
| Token de robots.txt | `Google-GeminiNotebook` |
| Respeta robots.txt | Parcial. Google dice que los agentes de consultas iniciadas por el usuario por lo general ignoran las reglas de robots.txt porque la consulta la pidió un usuario. |
| Direcciones IP | Comprobación por DNS inverso |
| Página del proveedor leída el | 24 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “The Gemini Notebook fetcher requests individual URLs that Gemini Notebook users have provided as sources for their projects.”

Fuente: [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers), leído el 24 de octubre de 2026.

## Qué pasa si bloqueas Google-GeminiNotebook

Google dice que, como la consulta la pidió un usuario, los agentes de consultas iniciadas por el usuario por lo general ignoran las reglas de robots.txt. La página de Google no documenta ningún token de robots.txt para este agente.

## Las líneas de robots.txt

Para permitir Google-GeminiNotebook:

```
User-agent: Google-GeminiNotebook
Allow: /
```

Para bloquear Google-GeminiNotebook:

```
User-agent: Google-GeminiNotebook
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 (compatible; Google-GeminiNotebook; +https://developers.google.com/crawling/docs/crawlers-fetchers/google-gemininotebook)
```

## Cómo distinguir una petición real de una falsa

Google dice que los agentes de consultas iniciadas por el usuario publican rangos de IP en user-triggered-fetchers.json, user-triggered-fetchers-google.json y user-triggered-agents.json, y que la máscara de DNS inverso coincide con ***-***-***-***.gae.googleusercontent.com o google-proxy-***-***-***-***.google.com, según si el agente es de Google o del usuario.

## Compara con ChatGPT-User

[ChatGPT-User](/es/bots/chatgpt-user): Ambos obtienen URL concretas porque un usuario le pidió a un producto de asistente que las usara, y ambos proveedores dicen que estas consultas pueden no seguir las reglas de robots.txt.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). Google-GeminiNotebook no es uno de ellos: lee tu robots.txt buscando un grupo `Google-GeminiNotebook` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿Google-GeminiNotebook respeta robots.txt?

No siempre. Parcial. Google dice que los agentes de consultas iniciadas por el usuario por lo general ignoran las reglas de robots.txt porque la consulta la pidió un usuario. Por eso una regla para Google-GeminiNotebook en robots.txt puede no detenerlo. Para rechazarlo con seguridad, usa una regla de cortafuegos o de CDN que combine el user agent y las direcciones publicadas.

### ¿Cómo sé que Google-GeminiNotebook está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
