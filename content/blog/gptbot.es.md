title: GPTBot: qué hace y qué cambia si lo bloqueas
h1: GPTBot: qué hace y qué cambia si lo bloqueas
description: GPTBot (OpenAI): entrenamiento. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: gptbot
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Cuatro datos sobre GPTBot: operador OpenAI, función Entrenamiento, respeta robots.txt Sí, lista de direcciones 18 rangos
hero_sub: GPTBot, de OpenAI
hero_boxes: Operador|OpenAI; Función|Entrenamiento; Respeta robots.txt|Sí; Lista de direcciones|18 rangos
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/oai-searchbot|OAI-SearchBot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: GPTBot es el rastreador de entrenamiento de OpenAI. Bloquearlo con Disallow en robots.txt le indica a OpenAI que el contenido del sitio no debe usarse para entrenar sus modelos fundacionales de IA generativa. No controla la búsqueda de ChatGPT, que usa OAI-SearchBot. OpenAI publica 18 rangos de IP para GPTBot.

## Qué es GPTBot

GPTBot es el rastreador al que se refiere la gente cuando dice «bloquear a OpenAI». La página de OpenAI dice que se usa para rastrear contenido que puede emplearse en el entrenamiento de sus modelos. Es uno de los tres rastreadores que nombra la documentación de OpenAI para la familia de productos de ChatGPT, junto a [OAI-SearchBot](/es/bots/oai-searchbot) y [ChatGPT-User](/es/bots/chatgpt-user).

| Dato | GPTBot |
| --- | --- |
| Operador | OpenAI |
| Función | Entrenamiento |
| Token de robots.txt | `GPTBot` |
| Respeta robots.txt | Sí, sigue robots.txt |
| Direcciones IP | 18 rangos (openai.com/gptbot.json, archivo del 2026-09-22) |
| Página del proveedor leída el | 21 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “GPTBot is used to make our generative AI foundation models more useful and safe. It is used to crawl content that may be used in training our generative AI foundation models. Disallowing GPTBot indicates a site's content should not be used in training generative AI foundation models.”

Fuente: [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots), leído el 21 de octubre de 2026.

## Qué pasa si bloqueas GPTBot

OpenAI presenta un Disallow para GPTBot como una señal sobre el entrenamiento: el contenido no debe usarse para entrenar modelos fundacionales de IA generativa. La misma página da el ejemplo de un sitio que permite a OAI-SearchBot aparecer en los resultados de búsqueda mientras bloquea a GPTBot, así que un bloqueo aquí no te saca por sí solo de las respuestas de búsqueda de ChatGPT. Bloquear o no es una decisión de negocio; ambas son legítimas.

## Las líneas de robots.txt

Para permitir GPTBot:

```
User-agent: GPTBot
Allow: /
```

Para bloquear GPTBot:

```
User-agent: GPTBot
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.4; +https://openai.com/gptbot
```

## Cómo distinguir una petición real de una falsa

La lista de GPTBot en openai.com/gptbot.json es la más corta de los tres archivos de OpenAI que contamos: 18 prefijos el 21 de octubre de 2026, con hora de creación 2026-09-22. Cuando una solicitud nombra a GPTBot pero llega desde una dirección que no está en esa lista, el nombre por sí solo no prueba nada.

## Compara con OAI-SearchBot

[OAI-SearchBot](/es/bots/oai-searchbot): Permítelo y bloquea GPTBot para seguir en la búsqueda de ChatGPT y excluirte del entrenamiento.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba GPTBot con una petición real y lee robots.txt para él. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿GPTBot respeta robots.txt?

Sí, sigue robots.txt. Dale a GPTBot su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que GPTBot está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots)
- [openai.com/gptbot.json](https://openai.com/gptbot.json)
