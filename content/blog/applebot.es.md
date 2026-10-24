title: Applebot: qué hace y qué cambia si lo bloqueas
h1: Applebot: qué hace y qué cambia si lo bloqueas
description: Applebot (Apple): varias funciones. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: applebot
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre Applebot: operador Apple, función Varias funciones, respeta robots.txt Sí, lista de direcciones 24 rangos
hero_sub: Applebot, de Apple
hero_boxes: Operador|Apple; Función|Varias funciones; Respeta robots.txt|Sí; Lista de direcciones|24 rangos
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/applebot-extended|Applebot-Extended; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: Applebot es el rastreador web de Apple. Apple dice que sus datos alimentan la búsqueda en Spotlight, Siri y Safari y que también pueden ayudar a entrenar los modelos fundacionales de Apple. Bloquear Applebot-Extended excluye el contenido solo del entrenamiento. Si robots.txt no menciona Applebot pero sí Googlebot, Applebot sigue las reglas de Googlebot.

## Qué es Applebot

Applebot es el rastreador web de Apple. Apple dice que sus datos alimentan la tecnología de búsqueda de Spotlight, Siri y Safari, y que también pueden usarse para ayudar a entrenar los modelos fundacionales de Apple y para dar contexto cuando los modelos de IA generan respuestas en los productos de Apple. Apple documenta además un token aparte, Applebot-Extended, y un agente de usuario iTMS para Apple Podcasts.

| Dato | Applebot |
| --- | --- |
| Operador | Apple |
| Función | Búsqueda (los datos rastreados también pueden ayudar a entrenar modelos de Apple) |
| Token de robots.txt | `Applebot` |
| Respeta robots.txt | Sí, en los rastreos generales de búsqueda dirigidos a Applebot |
| Direcciones IP | 24 rangos (search.developer.apple.com/applebot.json, archivo del 2026-09-15) |
| Página del proveedor leída el | 24 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “Applebot respects standard robots.txt directives in general search crawls that are targeted at Applebot.”

Fuente: [Apple: About Applebot](https://support.apple.com/en-us/119829), leído el 24 de octubre de 2026.

## Qué pasa si bloqueas Applebot

Apple dice que bloquear Applebot-Extended excluye el contenido del entrenamiento de los modelos fundacionales generativos de Apple, pero Applebot aún puede rastrear el sitio y este sigue apareciendo en Spotlight, Siri y Safari. Un Disallow para el propio Applebot se aplica a los rastreos generales de búsqueda dirigidos a Applebot, y Apple dice que, si robots.txt no menciona Applebot pero sí Googlebot, Applebot sigue las instrucciones de Googlebot. Apple dice que la metaetiqueta nosnippet excluye el contenido de las respuestas de conocimiento general.

## Las líneas de robots.txt

Para permitir Applebot:

```
User-agent: Applebot
Allow: /
```

Para bloquear Applebot:

```
User-agent: Applebot
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15 (Applebot/0.1; +http://www.apple.com/go/applebot)
```

## Cómo distinguir una petición real de una falsa

El archivo search.developer.apple.com/applebot.json tenía 24 rangos el 24 de octubre de 2026, archivo del 2026-09-15.

Apple dice que el tráfico de Applebot se identifica por lo general mediante DNS inverso en el dominio *.applebot.apple.com, o comparando la dirección IP con un prefijo CIDR de su archivo JSON publicado.

## Compara con Applebot-Extended

[Applebot-Extended](/es/bots/applebot-extended): Applebot es el rastreador que obtiene páginas para las funciones de búsqueda de Apple, mientras que Applebot-Extended es el token de robots.txt que controla si el contenido rastreado se usa para entrenar modelos generativos de Apple.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). Applebot no es uno de ellos: lee tu robots.txt buscando un grupo `Applebot` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿Applebot respeta robots.txt?

Sí, en los rastreos generales de búsqueda dirigidos a Applebot. Dale a Applebot su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que Applebot está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Apple: About Applebot](https://support.apple.com/en-us/119829)
- [Apple: Applebot IP CIDRs JSON (read 2026-10-24)](https://search.developer.apple.com/applebot.json)
