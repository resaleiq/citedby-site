title: MojeekBot: qué hace y qué cambia si lo bloqueas
h1: MojeekBot: qué hace y qué cambia si lo bloqueas
description: MojeekBot (Mojeek): búsqueda. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: mojeekbot
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre MojeekBot: operador Mojeek, función Búsqueda, respeta robots.txt Sí, lista de direcciones 1 rangos
hero_sub: MojeekBot, de Mojeek
hero_boxes: Operador|Mojeek; Función|Búsqueda; Respeta robots.txt|Sí; Lista de direcciones|1 rangos
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/bingbot|Bingbot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: MojeekBot es el rastreador web del motor de búsqueda Mojeek. Mojeek dice que obedece el Estándar de exclusión de robots, usando el primer registro cuyo User-Agent contiene MojeekBot, y que no admite la directiva no estándar crawl-delay. No debería solicitar más de una página de un sitio en el mismo segundo.

## Qué es MojeekBot

MojeekBot es el rastreador web del motor de búsqueda Mojeek. Mojeek dice que no debería solicitar más de una página de un sitio en el mismo periodo de 1 segundo. Obedece las metaetiquetas noindex, nocache y nofollow.

| Dato | MojeekBot |
| --- | --- |
| Operador | Mojeek |
| Función | Búsqueda |
| Token de robots.txt | `MojeekBot` |
| Respeta robots.txt | Sí, obedece el Estándar de exclusión de robots; crawl-delay no se admite |
| Direcciones IP | 1 rangos (www.mojeek.com/mojeekbot.json, archivo del 2025-05-14) |
| Página del proveedor leída el | 24 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “MojeekBot is the web crawler for the Mojeek search engine.”

Fuente: [Mojeek: MojeekBot](https://www.mojeek.com/bot.html), leído el 24 de octubre de 2026.

## Qué pasa si bloqueas MojeekBot

Mojeek dice que MojeekBot obedece el primer registro de robots.txt cuyo User-Agent contiene MojeekBot y, si no hay ninguno, el primer registro para User-Agent *. No recuperará URL que contengan una cadena bloqueada. No admite la directiva no estándar crawl-delay.

## Las líneas de robots.txt

Para permitir MojeekBot:

```
User-agent: MojeekBot
Allow: /
```

Para bloquear MojeekBot:

```
User-agent: MojeekBot
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
MojeekBot
```

## Cómo distinguir una petición real de una falsa

El archivo www.mojeek.com/mojeekbot.json tenía 1 rangos el 24 de octubre de 2026, archivo del 2025-05-14.

Mojeek dice que hay que resolver la IP visitante en inverso hasta un nombre del dominio mojeek.com y resolverlo de nuevo en directo hasta la misma IP, o comparar la IP con su lista publicada de direcciones IP de MojeekBot.

## Compara con Bingbot

[Bingbot](/es/bots/bingbot): Ambos rastrean para un motor de búsqueda; Mojeek publica una lista de IP de un solo rango y una comprobación de DNS inverso, y no admite crawl-delay.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). MojeekBot no es uno de ellos: lee tu robots.txt buscando un grupo `MojeekBot` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿MojeekBot respeta robots.txt?

Sí, obedece el Estándar de exclusión de robots; crawl-delay no se admite. Dale a MojeekBot su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que MojeekBot está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Mojeek: MojeekBot](https://www.mojeek.com/bot.html)
- [MojeekBot IP list (JSON, creationTime 2025-05-14, read 2026-10-24)](https://www.mojeek.com/mojeekbot.json)
