title: Google-Agent: qué hace y qué cambia si lo bloqueas
h1: Google-Agent: qué hace y qué cambia si lo bloqueas
description: Google-Agent (Google): consulta iniciada por el usuario. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición.
slug: google-agent
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre Google-Agent: operador Google, función Consulta iniciada por el usuario, respeta robots.txt No siempre, lista de direcciones 20 rangos
hero_sub: Google-Agent, de Google
hero_boxes: Operador|Google; Función|Consulta iniciada por el usuario; Respeta robots.txt|No siempre; Lista de direcciones|20 rangos
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/chatgpt-user|ChatGPT-User; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: Google-Agent es un agente de consultas iniciadas por el usuario que, según Google, usan los agentes alojados en la infraestructura de Google para navegar por la web y actuar a petición de un usuario. Google dice que estos agentes por lo general ignoran robots.txt, porque la consulta la pidió un usuario. Google publica sus rangos de IP en user-triggered-agents.json.

## Qué es Google-Agent

Google-Agent es un agente de consultas iniciadas por el usuario que, según Google, usan los agentes alojados en la infraestructura de Google para navegar por la web y realizar acciones a petición del usuario. Google enumera cadenas de agente de usuario distintas para móvil y escritorio. Google dice también que está experimentando con el protocolo Web Bot Auth con la identidad https://agent.bot.goog.

| Dato | Google-Agent |
| --- | --- |
| Operador | Google |
| Función | Consulta iniciada por el usuario (agentes que actúan por un usuario) |
| Token de robots.txt | `Google-Agent` |
| Respeta robots.txt | Parcial. Google dice que los agentes de consultas iniciadas por el usuario por lo general ignoran las reglas de robots.txt porque la consulta la pidió un usuario. |
| Direcciones IP | 20 rangos (developers.google.com/static/crawling/ipranges/user-triggered-agents.json, archivo del 2026-10-23) |
| Página del proveedor leída el | 24 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “Google-Agent is used by agents hosted on Google infrastructure to navigate the web and perform actions upon user request.”

Fuente: [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers), leído el 24 de octubre de 2026.

## Qué pasa si bloqueas Google-Agent

Google dice que, como la consulta la pidió un usuario, los agentes de consultas iniciadas por el usuario por lo general ignoran las reglas de robots.txt. La página de Google no documenta ningún token de robots.txt para Google-Agent.

## Las líneas de robots.txt

Para permitir Google-Agent:

```
User-agent: Google-Agent
Allow: /
```

Para bloquear Google-Agent:

```
User-agent: Google-Agent
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko; compatible; Google-Agent; +https://developers.google.com/crawling/docs/crawlers-fetchers/google-agent) Chrome/W.X.Y.Z Safari/537.36
```

## Cómo distinguir una petición real de una falsa

El archivo developers.google.com/static/crawling/ipranges/user-triggered-agents.json tenía 20 rangos el 24 de octubre de 2026, archivo del 2026-10-23.

Google dice que Google-Agent usa rangos de IP de user-triggered-agents.json y que la máscara de DNS inverso de estos agentes coincide con ***-***-***-***.gae.googleusercontent.com o google-proxy-***-***-***-***.google.com, según si el agente es de Google o del usuario.

## Compara con ChatGPT-User

[ChatGPT-User](/es/bots/chatgpt-user): Ambos actúan a petición de un usuario en lugar de rastrear por su cuenta, y Google-Agent se describe como un agente que navega por la web y realiza acciones para el usuario.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). Google-Agent no es uno de ellos: lee tu robots.txt buscando un grupo `Google-Agent` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿Google-Agent respeta robots.txt?

No siempre. Google dice que los agentes de consultas iniciadas por el usuario por lo general ignoran las reglas de robots.txt porque la consulta la pidió un usuario. Por eso una regla para Google-Agent en robots.txt puede no detenerlo. Para rechazarlo con seguridad, usa una regla de cortafuegos o de CDN que combine el user agent y las direcciones publicadas.

### ¿Cómo sé que Google-Agent está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers)
- [Google: user-triggered-agents.json (read 2026-10-24, creationTime 2026-10-23)](https://developers.google.com/static/crawling/ipranges/user-triggered-agents.json)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
