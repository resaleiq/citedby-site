title: PerplexityBot: qué hace y qué cambia si lo bloqueas
h1: PerplexityBot: qué hace y qué cambia si lo bloqueas
description: PerplexityBot (Perplexity): búsqueda. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: perplexitybot
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Cuatro datos sobre PerplexityBot: operador Perplexity, función Búsqueda, respeta robots.txt Sí, lista de direcciones 8 rangos
hero_sub: PerplexityBot, de Perplexity
hero_boxes: Operador|Perplexity; Función|Búsqueda; Respeta robots.txt|Sí; Lista de direcciones|8 rangos
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/perplexity-user|Perplexity-User; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: PerplexityBot es el rastreador de Perplexity para mostrar y enlazar sitios web en sus resultados de búsqueda. Perplexity dice que no se usa para rastrear contenido para modelos fundacionales de IA. Sigue robots.txt, los cambios pueden tardar hasta 24 horas en aplicarse y Perplexity publica 8 rangos de IP para él.

## Qué es PerplexityBot

Perplexity nombra dos agentes. PerplexityBot construye el índice de búsqueda; Perplexity-User visita una página cuando una persona pregunta. La página de Perplexity contiene pautas de configuración para proveedores de WAF populares, porque un cortafuegos puede detener al rastreador antes de que robots.txt importe.

| Dato | PerplexityBot |
| --- | --- |
| Operador | Perplexity |
| Función | Búsqueda |
| Token de robots.txt | `PerplexityBot` |
| Respeta robots.txt | Sí, sigue robots.txt |
| Direcciones IP | 8 rangos (perplexity.com/perplexitybot.json, archivo del 2025-02-07) |
| Página del proveedor leída el | 21 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “PerplexityBot is designed to surface and link websites in search results on Perplexity. It is not used to crawl content for AI foundation models.”

Fuente: [Perplexity: Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers), leído el 21 de octubre de 2026.

## Qué pasa si bloqueas PerplexityBot

Perplexity recomienda permitir a PerplexityBot en robots.txt y permitir las solicitudes desde sus rangos de IP publicados si quieres aparecer en sus resultados de búsqueda. Dice también que los cambios en tu robots.txt pueden tardar hasta 24 horas en reflejarse en sus sistemas, así que una comprobación hecha una hora después de editar demuestra poco.

## Las líneas de robots.txt

Para permitir PerplexityBot:

```
User-agent: PerplexityBot
Allow: /
```

Para bloquear PerplexityBot:

```
User-agent: PerplexityBot
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)
```

## Cómo distinguir una petición real de una falsa

El archivo de Perplexity en perplexity.com/perplexitybot.json tenía 8 prefijos el 21 de octubre de 2026, con hora de creación 2025-02-07. Su sección sobre WAF sugiere una regla que combine el user-agent con la condición de IP, de modo que una solicitud que afirme el nombre desde otra dirección no pase.

## Compara con Perplexity-User

[Perplexity-User](/es/bots/perplexity-user): El agente de consultas iniciadas por el usuario; Perplexity dice que por lo general ignora robots.txt.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba PerplexityBot con una petición real y lee robots.txt para él. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿PerplexityBot respeta robots.txt?

Sí, sigue robots.txt. Dale a PerplexityBot su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que PerplexityBot está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Perplexity: Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers)
- [perplexity.com/perplexitybot.json](https://www.perplexity.ai/perplexitybot.json)
