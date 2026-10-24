title: Diffbot: qué hace y qué cambia si lo bloqueas
h1: Diffbot: qué hace y qué cambia si lo bloqueas
description: Diffbot (Diffbot): búsqueda. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: diffbot
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre Diffbot: operador Diffbot, función Búsqueda, respeta robots.txt Sí, lista de direcciones Ninguna
hero_sub: Diffbot, de Diffbot
hero_boxes: Operador|Diffbot; Función|Búsqueda; Respeta robots.txt|Sí; Lista de direcciones|Ninguna
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/bingbot|Bingbot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: Diffbot documenta dos agentes de usuario. Diffbot rastrea la web de forma proactiva para un motor de búsqueda general, de modo que los sitios puedan descubrirse y citarse desde su Knowledge Graph. Diffbot-User obtiene una URL para una persona que usa su software. Diffbot dice que sus rastreos siguen robots.txt por defecto, incluidos disallow y crawl-delay.

## Qué es Diffbot

Diffbot documenta dos agentes de usuario. Diffbot se usa para el rastreo web general y proactivo con el fin de construir un motor de búsqueda general, de modo que los sitios puedan descubrirse y citarse desde el Diffbot Knowledge Graph y los servicios de búsqueda web. Diffbot-User se usa para solicitudes hechas en nombre de un usuario humano que navega a una URL con el software de Diffbot.

| Dato | Diffbot |
| --- | --- |
| Operador | Diffbot |
| Función | Búsqueda (rastreo web general) |
| Token de robots.txt | `Diffbot` |
| Respeta robots.txt | Sí, por defecto (directivas disallow y crawl-delay) |
| Direcciones IP | Ninguna publicada |
| Página del proveedor leída el | 24 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “By default Diffbot's web crawls adhere to a site’s robots.txt instructions, including the disallow and crawl-delay directives.”

Fuente: [Diffbot: Does Diffbot respect robots.txt?](https://www.diffbot.com/docs/crawl/faq/robots-txt), leído el 24 de octubre de 2026.

## Qué pasa si bloqueas Diffbot

Diffbot dice que sus rastreos web siguen robots.txt por defecto, incluidos disallow y crawl-delay, y que una regla puede anularse en casos concretos, como una alianza o un acuerdo con el sitio. Enumera Diffbot y Diffbot-User como agentes de usuario independientes y dice que quienes usan sus API Extract y Crawlbot definen sus propios parámetros de rastreo y pueden fijar su propio User-Agent.

## Las líneas de robots.txt

Para permitir Diffbot:

```
User-agent: Diffbot
Allow: /
```

Para bloquear Diffbot:

```
User-agent: Diffbot
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
Diffbot
```

## Cómo distinguir una petición real de una falsa

La página del proveedor no describe ninguna lista de IP ni método de verificación.

## Compara con Bingbot

[Bingbot](/es/bots/bingbot): Su operador describe Diffbot como similar a Googlebot y Bing, un rastreador general para un índice de búsqueda, y el proveedor dice que no se usa para entrenar IA.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). Diffbot no es uno de ellos: lee tu robots.txt buscando un grupo `Diffbot` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿Diffbot respeta robots.txt?

Sí, por defecto (directivas disallow y crawl-delay). Dale a Diffbot su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que Diffbot está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Diffbot: Does Diffbot respect robots.txt? (read 2026-10-24)](https://www.diffbot.com/docs/crawl/faq/robots-txt)
