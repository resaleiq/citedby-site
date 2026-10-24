title: DuckAssistBot: qué hace y qué cambia si lo bloqueas
h1: DuckAssistBot: qué hace y qué cambia si lo bloqueas
description: DuckAssistBot (DuckDuckGo): consulta iniciada por el usuario. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición.
slug: duckassistbot
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Cuatro datos sobre DuckAssistBot: operador DuckDuckGo, función Consulta iniciada por el usuario, respeta robots.txt Sí, lista de direcciones 486 direcciones
hero_sub: DuckAssistBot, de DuckDuckGo
hero_boxes: Operador|DuckDuckGo; Función|Consulta iniciada por el usuario; Respeta robots.txt|Sí; Lista de direcciones|486 direcciones
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/amazonbot|Amazonbot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: DuckAssistBot rastrea páginas en tiempo real para las respuestas asistidas por IA de DuckDuckGo, que citan sus fuentes. DuckDuckGo dice que los datos no se usan para entrenar modelos de IA. Un Disallow en robots.txt surte efecto a las 72 horas y no afecta al posicionamiento orgánico. Enumera 486 direcciones IP.

## Qué es DuckAssistBot

DuckDuckGo tiene dos bots que la gente confunde. DuckDuckBot es el rastreador de búsqueda; DuckAssistBot es el que está detrás de las respuestas asistidas por IA. La página de ayuda de DuckDuckGo dice que las respuestas citan sus fuentes de forma destacada y que los datos rastreados no se usan para entrenar modelos de IA.

| Dato | DuckAssistBot |
| --- | --- |
| Operador | DuckDuckGo |
| Función | Consulta en tiempo real para respuestas asistidas por IA |
| Token de robots.txt | `DuckAssistBot` |
| Respeta robots.txt | Sí, un cambio surte efecto a las 72 horas |
| Direcciones IP | 486 direcciones (duckduckgo.com/duckassistbot.json, archivo del 2026-09-01) |
| Página del proveedor leída el | 21 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “DuckAssistBot is a web crawler for DuckDuckGo Search that crawls pages in real-time for our AI-assisted answers, which prominently cite their sources. This data is not used in any way to train AI models.”

Fuente: [DuckDuckGo Help Pages: About DuckAssistBot](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot), leído el 21 de octubre de 2026.

## Qué pasa si bloqueas DuckAssistBot

DuckDuckGo dice que, una vez que bloqueas DuckAssistBot con Disallow, el cambio surte efecto a las 72 horas, y que excluirse no afecta al posicionamiento orgánico ni influye en que los sitios aparezcan en sus resultados de búsqueda. Por tanto, el coste de un bloqueo se limita a las respuestas asistidas y sus citas. Los problemas con la exclusión van a la dirección que indica la página, crawling@duckduckgo.com.

## Las líneas de robots.txt

Para permitir DuckAssistBot:

```
User-agent: DuckAssistBot
Allow: /
```

Para bloquear DuckAssistBot:

```
User-agent: DuckAssistBot
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
DuckAssistBot/1.2; (+http://duckduckgo.com/duckassistbot.html)
```

## Cómo distinguir una petición real de una falsa

DuckDuckGo enumera las direcciones en el artículo de ayuda y como JSON en duckduckgo.com/duckassistbot.json. El archivo tenía 486 entradas el 21 de octubre de 2026, con hora de creación 2026-09-01, más que cualquier otra lista de direcciones que contamos para este conjunto, y contiene direcciones sueltas donde las demás publican rangos CIDR. El agente de usuario aparece como `DuckAssistBot/1.2`.

## Compara con Amazonbot

[Amazonbot](/es/bots/amazonbot): La familia de tres agentes de Amazon, uno de los cuales puede ignorar robots.txt.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). DuckAssistBot no es uno de ellos: lee tu robots.txt buscando un grupo `DuckAssistBot` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿DuckAssistBot respeta robots.txt?

Sí, un cambio surte efecto a las 72 horas. Dale a DuckAssistBot su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que DuckAssistBot está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [DuckDuckGo Help Pages: About DuckAssistBot](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot)
- [duckduckgo.com/duckassistbot.json](https://duckduckgo.com/duckassistbot.json)
