title: OAI-SearchBot: qué hace y qué cambia si lo bloqueas
h1: OAI-SearchBot: qué hace y qué cambia si lo bloqueas
description: OAI-SearchBot (OpenAI): búsqueda. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: oai-searchbot
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Cuatro datos sobre OAI-SearchBot: operador OpenAI, función Búsqueda, respeta robots.txt Sí, lista de direcciones 39 rangos
hero_sub: OAI-SearchBot, de OpenAI
hero_boxes: Operador|OpenAI; Función|Búsqueda; Respeta robots.txt|Sí; Lista de direcciones|39 rangos
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/gptbot|GPTBot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: OAI-SearchBot es el rastreador de OpenAI para la búsqueda de ChatGPT. Los sitios que se excluyen no se mostrarán en las respuestas de búsqueda de ChatGPT, aunque pueden seguir apareciendo como enlaces de navegación. Obedece robots.txt con el token OAI-SearchBot, y OpenAI publica 39 rangos de IP para él.

## Qué es OAI-SearchBot

OpenAI tiene varios rastreadores y dice que el ajuste de cada uno es independiente de los demás. OAI-SearchBot es el que decide si tus páginas pueden aparecer en las funciones de búsqueda de ChatGPT. No es el rastreador de entrenamiento (ese es [GPTBot](/es/bots/gptbot)) ni el que abre una página cuando una persona pregunta por ella (ese es [ChatGPT-User](/es/bots/chatgpt-user)).

| Dato | OAI-SearchBot |
| --- | --- |
| Operador | OpenAI |
| Función | Búsqueda |
| Token de robots.txt | `OAI-SearchBot` |
| Respeta robots.txt | Sí, sigue robots.txt |
| Direcciones IP | 39 rangos (openai.com/searchbot.json, archivo del 2026-01-02) |
| Página del proveedor leída el | 21 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “OAI-SearchBot is used to surface websites in search results in ChatGPT's search features. Sites that are opted out of OAI-SearchBot will not be shown in ChatGPT search answers, though can still appear as navigational links.”

Fuente: [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots), leído el 21 de octubre de 2026.

## Qué pasa si bloqueas OAI-SearchBot

Según OpenAI, los sitios excluidos «no se mostrarán en las respuestas de búsqueda de ChatGPT». Ese es el coste: una tienda que bloquea OAI-SearchBot renuncia a la parte de ChatGPT que enlaza a las fuentes. OpenAI recomienda lo contrario a los sitios que quieren aparecer: permitir OAI-SearchBot en robots.txt y permitir las solicitudes desde sus rangos de IP publicados.

## Las líneas de robots.txt

Para permitir OAI-SearchBot:

```
User-agent: OAI-SearchBot
Allow: /
```

Para bloquear OAI-SearchBot:

```
User-agent: OAI-SearchBot
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36; compatible; OAI-SearchBot/1.4; +https://openai.com/searchbot
```

## Cómo distinguir una petición real de una falsa

OpenAI publica las direcciones que usa OAI-SearchBot en openai.com/searchbot.json. El 21 de octubre de 2026 ese archivo tenía 39 prefijos y llevaba la hora de creación 2026-01-02. Compara la dirección de tu registro del servidor con esos prefijos antes de fiarte de una solicitud que solo afirma el nombre en su user-agent. OpenAI dice también que, cuando obtiene robots.txt, puede añadir una marca `robots.txt` a la cadena de user-agent, de modo que esas solicitudes se distinguen fácilmente en los registros sin rutas.

## Compara con GPTBot

[GPTBot](/es/bots/gptbot): GPTBot es para el entrenamiento; bloquearlo no te quita de la búsqueda de ChatGPT, porque los ajustes son independientes.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba OAI-SearchBot con una petición real y lee robots.txt para él. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿OAI-SearchBot respeta robots.txt?

Sí, sigue robots.txt. Dale a OAI-SearchBot su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que OAI-SearchBot está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots)
- [openai.com/searchbot.json](https://openai.com/searchbot.json)
