title: DuckDuckBot: qué hace y qué cambia si lo bloqueas
h1: DuckDuckBot: qué hace y qué cambia si lo bloqueas
description: DuckDuckBot (DuckDuckGo): búsqueda. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: duckduckbot
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre DuckDuckBot: operador DuckDuckGo, función Búsqueda, respeta robots.txt Sí, lista de direcciones 486 direcciones
hero_sub: DuckDuckBot, de DuckDuckGo
hero_boxes: Operador|DuckDuckGo; Función|Búsqueda; Respeta robots.txt|Sí; Lista de direcciones|486 direcciones
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/duckassistbot|DuckAssistBot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: DuckDuckBot es el rastreador web de DuckDuckGo y, según dice DuckDuckGo, su función es mejorar los resultados de búsqueda de DuckDuckGo. DuckDuckGo dice que respeta WWW::RobotRules y que publica sus direcciones IP como una lista en formato JSON. DuckAssistBot, que obtiene páginas para las respuestas asistidas por IA, está documentado en otra página de ayuda de DuckDuckGo.

## Qué es DuckDuckBot

DuckDuckBot es el rastreador web de DuckDuckGo. DuckDuckGo dice que su función es mejorar los resultados de búsqueda de DuckDuckGo. Las páginas de ayuda de DuckDuckGo enumeran DuckAssistBot en una página aparte.

| Dato | DuckDuckBot |
| --- | --- |
| Operador | DuckDuckGo |
| Función | Búsqueda |
| Token de robots.txt | `DuckDuckBot` |
| Respeta robots.txt | Sí, respeta WWW::RobotRules (no publica ninguna nota sobre plazos) |
| Direcciones IP | 486 direcciones (duckduckgo.com/duckduckbot.json, archivo del 2026-09-01) |
| Página del proveedor leída el | 24 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “DuckDuckBot’s job is to constantly improve our search results and offer users the best and most secure search experience possible.”

Fuente: [DuckDuckGo Help Pages: Is DuckDuckBot related to DuckDuckGo?](https://duckduckgo.com/duckduckgo-help-pages/results/duckduckbot), leído el 24 de octubre de 2026.

## Qué pasa si bloqueas DuckDuckBot

DuckDuckGo dice que DuckDuckBot respeta WWW::RobotRules, así que una regla Disallow dirigida a DuckDuckBot en robots.txt se aplica a este rastreador. La página no dice nada sobre qué cambia en los resultados de DuckDuckGo si lo bloqueas, ni nada sobre DuckAssistBot.

## Las líneas de robots.txt

Para permitir DuckDuckBot:

```
User-agent: DuckDuckBot
Allow: /
```

Para bloquear DuckDuckBot:

```
User-agent: DuckDuckBot
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
DuckDuckBot/1.1; (+http://duckduckgo.com/duckduckbot.html)
```

## Cómo distinguir una petición real de una falsa

El archivo duckduckgo.com/duckduckbot.json tenía 486 direcciones el 24 de octubre de 2026, archivo del 2026-09-01.

DuckDuckGo dice que el rastreador procede de las direcciones IP que figuran en su página de ayuda, disponibles también como JSON en duckduckgo.com/duckduckbot.json.

## Compara con DuckAssistBot

[DuckAssistBot](/es/bots/duckassistbot): DuckDuckBot es el rastreador de los resultados de búsqueda de DuckDuckGo, mientras que DuckDuckGo documenta DuckAssistBot en su propia página de ayuda.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). DuckDuckBot no es uno de ellos: lee tu robots.txt buscando un grupo `DuckDuckBot` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿DuckDuckBot respeta robots.txt?

Sí, respeta WWW::RobotRules (no publica ninguna nota sobre plazos). Dale a DuckDuckBot su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que DuckDuckBot está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [DuckDuckGo Help Pages: Is DuckDuckBot related to DuckDuckGo?](https://duckduckgo.com/duckduckgo-help-pages/results/duckduckbot)
- [DuckDuckBot IP list (JSON, creationTime 2026-09-01, read 2026-10-24)](https://duckduckgo.com/duckduckbot.json)
