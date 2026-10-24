title: MistralAI-User: qué hace y qué cambia si lo bloqueas
h1: MistralAI-User: qué hace y qué cambia si lo bloqueas
description: MistralAI-User (Mistral): consulta iniciada por el usuario. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición.
slug: mistralai-user
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Cuatro datos sobre MistralAI-User: operador Mistral, función Consulta iniciada por el usuario, respeta robots.txt Sí, lista de direcciones 4 rangos
hero_sub: MistralAI-User, de Mistral
hero_boxes: Operador|Mistral; Función|Consulta iniciada por el usuario; Respeta robots.txt|Sí; Lista de direcciones|4 rangos
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/chatgpt-user|ChatGPT-User; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: MistralAI-User es el agente de Mistral que puede visitar una página cuando un usuario le hace una pregunta a Vibe y enlazar la fuente en su respuesta. Mistral dice que no se usa para rastrear de forma automática ni para entrenar IA generativa. La página de Mistral enumera también MistralAI-Index y MistralAI-Training, cada uno con su propio token.

## Qué es MistralAI-User

La página de rastreadores de Mistral enumera tres agentes: MistralAI-User para acciones del usuario en Vibe, MistralAI-Index para indexar contenido para la búsqueda de Mistral y MistralAI-Training, que rastrea contenido web para ayudar a construir conjuntos de datos con los que entrenar los modelos de IA generativa de Mistral. Los administradores web pueden bloquear cada uno en robots.txt.

| Dato | MistralAI-User |
| --- | --- |
| Operador | Mistral |
| Función | Consulta iniciada por el usuario |
| Token de robots.txt | `MistralAI-User` |
| Respeta robots.txt | Exclusión mediante robots.txt |
| Direcciones IP | 4 rangos (mistral.ai/mistralai-user-ips.json, archivo del 2025-02-19) |
| Página del proveedor leída el | 21 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “MistralAI-User is for user actions in Vibe. When users ask Vibe a question, it may visit a web page to help answer and include a link to the source in its response.”

Fuente: [Mistral Docs: Mistral crawlers](https://docs.mistral.ai/robots), leído el 21 de octubre de 2026.

## Qué pasa si bloqueas MistralAI-User

Bloquear MistralAI-User impide que ese agente abra tu página para la pregunta de un usuario de Vibe; no afecta a los agentes de índice y de entrenamiento, que tienen sus propios tokens. Mistral dice que el agente de usuario no se usa para rastrear la web de ninguna forma automática ni para rastrear contenido para entrenar IA generativa, y que el contenido que rastrea el agente de índice no se usa para entrenar IA generativa de ningún tipo.

## Las líneas de robots.txt

Para permitir MistralAI-User:

```
User-agent: MistralAI-User
Allow: /
```

Para bloquear MistralAI-User:

```
User-agent: MistralAI-User
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; MistralAI-User/1.0; +https://docs.mistral.ai/robots)
```

## Cómo distinguir una petición real de una falsa

Mistral publica archivos de direcciones distintos para cada agente. El 21 de octubre de 2026, mistral.ai/mistralai-user-ips.json tenía 4 prefijos (hora de creación 2025-02-19) y el archivo del índice 2 prefijos (hora de creación 2026-04-19). Dos entradas para un rastreador de índice es una lista que una regla de cortafuegos puede cubrir con exactitud.

## Compara con ChatGPT-User

[ChatGPT-User](/es/bots/chatgpt-user): La misma función en OpenAI, con otra promesa sobre robots.txt.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). MistralAI-User no es uno de ellos: lee tu robots.txt buscando un grupo `MistralAI-User` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿MistralAI-User respeta robots.txt?

Exclusión mediante robots.txt. Dale a MistralAI-User su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que MistralAI-User está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Mistral Docs: Mistral crawlers](https://docs.mistral.ai/robots)
- [mistral.ai/mistralai-user-ips.json](https://mistral.ai/mistralai-user-ips.json)
