title: ChatGPT-User: qué hace y qué cambia si lo bloqueas
h1: ChatGPT-User: qué hace y qué cambia si lo bloqueas
description: ChatGPT-User (OpenAI): consulta iniciada por el usuario. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición.
slug: chatgpt-user
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Cuatro datos sobre ChatGPT-User: operador OpenAI, función Consulta iniciada por el usuario, respeta robots.txt No siempre, lista de direcciones 234 rangos
hero_sub: ChatGPT-User, de OpenAI
hero_boxes: Operador|OpenAI; Función|Consulta iniciada por el usuario; Respeta robots.txt|No siempre; Lista de direcciones|234 rangos
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/oai-searchbot|OAI-SearchBot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: ChatGPT-User visita una página web cuando una persona le hace a ChatGPT o a un GPT personalizado una pregunta que la necesita. OpenAI dice que no se usa para rastrear de forma automática y que, como la solicitud la inicia un usuario, es posible que las reglas de robots.txt no se apliquen. OpenAI enumera 234 rangos de IP para él.

## Qué es ChatGPT-User

A diferencia de los demás robots de OpenAI, ChatGPT-User no recorre la web por su cuenta. OpenAI lo describe como el agente que se usa para ciertas acciones del usuario en ChatGPT y en los GPT personalizados, incluidas las páginas a las que llega un GPT personalizado mediante GPT Actions. Una persona escribió algo y después llegó una solicitud a tu servidor.

| Dato | ChatGPT-User |
| --- | --- |
| Operador | OpenAI |
| Función | Consulta iniciada por el usuario |
| Token de robots.txt | `ChatGPT-User` |
| Respeta robots.txt | Es posible que las reglas de robots.txt no se apliquen |
| Direcciones IP | 234 rangos (openai.com/chatgpt-user.json, archivo del 2026-10-20) |
| Página del proveedor leída el | 21 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “ChatGPT-User is not used for crawling the web in an automatic fashion. Because these actions are initiated by a user, robots.txt rules may not apply.”

Fuente: [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots), leído el 21 de octubre de 2026.

## Qué pasa si bloqueas ChatGPT-User

Como la visita la inicia el usuario, OpenAI avisa de que es posible que las reglas de robots.txt no se apliquen, así que una línea `Disallow` para ChatGPT-User no garantiza que se detenga. OpenAI dice también que ChatGPT-User no se usa para decidir si el contenido aparece en la búsqueda y remite las exclusiones de búsqueda a OAI-SearchBot. Si necesitas detener estas solicitudes, el control está en tu servidor o en tu CDN, no solo en robots.txt.

## Las líneas de robots.txt

Para permitir ChatGPT-User:

```
User-agent: ChatGPT-User
Allow: /
```

Para bloquear ChatGPT-User:

```
User-agent: ChatGPT-User
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ChatGPT-User/1.0; +https://openai.com/bot
```

## Cómo distinguir una petición real de una falsa

Su lista de direcciones es la más larga de los tres archivos de OpenAI que contamos: openai.com/chatgpt-user.json tenía 234 prefijos el 21 de octubre de 2026, con hora de creación 2026-10-20, el día antes de esta página. Una lista tan larga es motivo para volver a descargarla cuando compruebes una línea de registro, no para copiarla una sola vez en un cortafuegos.

## Compara con OAI-SearchBot

[OAI-SearchBot](/es/bots/oai-searchbot): OAI-SearchBot es el rastreador de búsqueda y sí obedece robots.txt.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ChatGPT-User con una petición real y lee robots.txt para él. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿ChatGPT-User respeta robots.txt?

No siempre. Es posible que las reglas de robots.txt no se apliquen. Por eso una regla para ChatGPT-User en robots.txt puede no detenerlo. Para rechazarlo con seguridad, usa una regla de cortafuegos o de CDN que combine el user agent y las direcciones publicadas.

### ¿Cómo sé que ChatGPT-User está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots)
- [openai.com/chatgpt-user.json](https://openai.com/chatgpt-user.json)
