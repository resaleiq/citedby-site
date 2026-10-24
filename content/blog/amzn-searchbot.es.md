title: Amzn-SearchBot: qué hace y qué cambia si lo bloqueas
h1: Amzn-SearchBot: qué hace y qué cambia si lo bloqueas
description: Amzn-SearchBot (Amazon): búsqueda. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: amzn-searchbot
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre Amzn-SearchBot: operador Amazon, función Búsqueda, respeta robots.txt Sí, lista de direcciones Lista en su página
hero_sub: Amzn-SearchBot, de Amazon
hero_boxes: Operador|Amazon; Función|Búsqueda; Respeta robots.txt|Sí; Lista de direcciones|Lista en su página
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/amazonbot|Amazonbot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: Amzn-SearchBot es un rastreador de Amazon que se usa para mejorar experiencias de búsqueda como Alexa. Amazon dice que, si lo permites, tu contenido es apto para aparecer ahí y que no rastrea para entrenar modelos de IA generativa. Su ajuste es independiente de Amazonbot y Amzn-User, y un cambio puede tardar unas 24 horas.

## Qué es Amzn-SearchBot

Amzn-SearchBot es un rastreador de Amazon que se usa para mejorar las experiencias de búsqueda en los productos y servicios de Amazon. Amazon dice que, si lo permites, tu contenido es apto para aparecer en experiencias de búsqueda como Alexa y que no rastrea contenido para entrenar modelos de IA generativa. Es uno de los tres agentes de usuario de Amazon (Amazonbot, Amzn-SearchBot, Amzn-User) que Amazon documenta en una sola página.

| Dato | Amzn-SearchBot |
| --- | --- |
| Operador | Amazon |
| Función | Búsqueda |
| Token de robots.txt | `Amzn-SearchBot` |
| Respeta robots.txt | Sí, los cambios pueden tardar unas 24 horas |
| Direcciones IP | Lista en la página del proveedor (developer.amazon.com/amazonbot/searchbot-ip-addresses) |
| Página del proveedor leída el | 24 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “If robots.txt files don’t mention Amzn-SearchBot but allow other search bots, Amzn-SearchBot will crawl in accordance with the robots.txt directives given to other search bots.”

Fuente: [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot), leído el 24 de octubre de 2026.

## Qué pasa si bloqueas Amzn-SearchBot

Amazon dice que el rastreo automatizado de sus agentes de usuario listados respeta el Protocolo de exclusión de robots y atiende las directivas user-agent y allow/disallow. Amazon dice que el ajuste de cada agente de usuario es independiente de los demás y que puede tardar unas 24 horas en aplicarse. Si robots.txt no menciona Amzn-SearchBot pero permite a otros bots de búsqueda, sigue las directivas dadas a esos otros bots de búsqueda.

## Las líneas de robots.txt

Para permitir Amzn-SearchBot:

```
User-agent: Amzn-SearchBot
Allow: /
```

Para bloquear Amzn-SearchBot:

```
User-agent: Amzn-SearchBot
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Amzn-SearchBot/0.1) Chrome/W.X.Y.Z Safari/537.36
```

## Cómo distinguir una petición real de una falsa

Amazon publica las direcciones IP de Amzn-SearchBot en una página web que muestra la lista como JSON, y la enlaza desde la página de documentación de Amazonbot.

## Compara con Amazonbot

[Amazonbot](/es/bots/amazonbot): Amazonbot se usa para mejorar productos y servicios de Amazon y puede usarse para entrenar modelos de IA de Amazon, mientras que Amzn-SearchBot es para experiencias de búsqueda y Amazon dice que no rastrea para entrenar modelos de IA generativa.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). Amzn-SearchBot no es uno de ellos: lee tu robots.txt buscando un grupo `Amzn-SearchBot` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿Amzn-SearchBot respeta robots.txt?

Sí, los cambios pueden tardar unas 24 horas. Dale a Amzn-SearchBot su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que Amzn-SearchBot está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot)
- [Amazon: Amzn-SearchBot IP addresses (read 2026-10-24)](https://developer.amazon.com/amazonbot/searchbot-ip-addresses/)
