title: Kagibot: qué hace y qué cambia si lo bloqueas
h1: Kagibot: qué hace y qué cambia si lo bloqueas
description: Kagibot (Kagi): búsqueda. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: kagibot
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre Kagibot: operador Kagi, función Búsqueda, respeta robots.txt Sí, lista de direcciones Lista en su página
hero_sub: Kagibot, de Kagi
hero_boxes: Operador|Kagi; Función|Búsqueda; Respeta robots.txt|Sí; Lista de direcciones|Lista en su página
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/googlebot|Googlebot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: Kagibot es el rastreador web del motor de búsqueda Kagi. Kagi dice que se respetan las directivas estándar de robots.txt dirigidas a Kagibot y que, cuando ninguna regla se dirige a Kagibot pero una sí a Googlebot, Kagibot sigue las directivas de Googlebot. Kagi publica su cadena de user-agent y las direcciones IP desde las que llegan sus solicitudes.

## Qué es Kagibot

Kagibot es el rastreador web del motor de búsqueda Kagi. Kagi publica su cadena de user-agent y las direcciones IP desde las que se originan las solicitudes de Kagibot.

| Dato | Kagibot |
| --- | --- |
| Operador | Kagi |
| Función | Búsqueda |
| Token de robots.txt | `Kagibot` |
| Respeta robots.txt | Sí, se respetan las directivas estándar de robots.txt dirigidas a Kagibot |
| Direcciones IP | Lista en la página del proveedor (kagi.com/bot) |
| Página del proveedor leída el | 24 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “Standard directives in robots.txt that target Kagibot are respected.”

Fuente: [Kagi: About KagiBot](https://kagi.com/bot), leído el 24 de octubre de 2026.

## Qué pasa si bloqueas Kagibot

Kagi dice que se respetan las directivas estándar de robots.txt dirigidas a Kagibot, por ejemplo las reglas Disallow para una ruta. Si no hay ninguna regla para Kagibot pero sí una para Googlebot, Kagibot sigue las directivas de Googlebot.

## Las líneas de robots.txt

Para permitir Kagibot:

```
User-agent: Kagibot
Allow: /
```

Para bloquear Kagibot:

```
User-agent: Kagibot
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
Mozilla/5.0 (compatible; Kagibot/1.0; +https://kagi.com/bot)
```

## Cómo distinguir una petición real de una falsa

Kagi enumera en su página del bot las direcciones IP (con nombres de host de kagibot.org) desde las que se originan las solicitudes de Kagibot.

## Compara con Googlebot

[Googlebot](/es/bots/googlebot): Kagibot sigue sus propias reglas de robots.txt y recurre a las de Googlebot cuando ninguna se dirige a Kagibot.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). Kagibot no es uno de ellos: lee tu robots.txt buscando un grupo `Kagibot` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿Kagibot respeta robots.txt?

Sí, se respetan las directivas estándar de robots.txt dirigidas a Kagibot. Dale a Kagibot su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que Kagibot está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Kagi: About KagiBot (read 2026-10-24)](https://kagi.com/bot)
