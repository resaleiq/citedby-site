title: Storebot-Google: qué hace y qué cambia si lo bloqueas
h1: Storebot-Google: qué hace y qué cambia si lo bloqueas
description: Storebot-Google (Google): búsqueda. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: storebot-google
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre Storebot-Google: operador Google, función Búsqueda, respeta robots.txt Sí, lista de direcciones 317 rangos
hero_sub: Storebot-Google, de Google
hero_boxes: Operador|Google; Función|Búsqueda; Respeta robots.txt|Sí; Lista de direcciones|317 rangos
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/googlebot|Googlebot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: Storebot-Google es el rastreador que Google documenta como Google StoreBot entre sus rastreadores comunes. Google dice que un Disallow dirigido a su token afecta a todas las superficies de Google Shopping, como la pestaña Shopping de Google Search y Google Shopping. Googlebot es un token aparte con sus propios productos afectados.

## Qué es Storebot-Google

Storebot-Google es el rastreador de Google documentado como Google StoreBot entre sus rastreadores comunes. Google dice que las reglas dirigidas a él afectan a todas las superficies de Google Shopping. Google enumera cadenas de agente de usuario distintas para escritorio y móvil.

| Dato | Storebot-Google |
| --- | --- |
| Operador | Google |
| Función | Búsqueda (superficies de Google Shopping) |
| Token de robots.txt | `Storebot-Google` |
| Respeta robots.txt | Sí. Google dice que los rastreadores comunes siempre obedecen las reglas de robots.txt cuando rastrean de forma automática. |
| Direcciones IP | 317 rangos (developers.google.com/static/crawling/ipranges/common-crawlers.json, archivo del 2026-10-23) |
| Página del proveedor leída el | 24 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “Crawling preferences addressed to the Storebot-Google user agent affect all surfaces of Google Shopping”

Fuente: [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers), leído el 24 de octubre de 2026.

## Qué pasa si bloqueas Storebot-Google

Google dice que un Disallow dirigido al token Storebot-Google afecta a todas las superficies de Google Shopping, como la pestaña Shopping de Google Search y Google Shopping. La página incluye a Googlebot como un token aparte con sus propios productos afectados.

## Las líneas de robots.txt

Para permitir Storebot-Google:

```
User-agent: Storebot-Google
Allow: /
```

Para bloquear Storebot-Google:

```
User-agent: Storebot-Google
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
Mozilla/5.0 (X11; Linux x86_64; Storebot-Google/1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z Safari/537.36
```

## Cómo distinguir una petición real de una falsa

El archivo developers.google.com/static/crawling/ipranges/common-crawlers.json tenía 317 rangos el 24 de octubre de 2026, archivo del 2026-10-23.

Google dice que los rastreadores comunes por lo general rastrean desde los rangos de common-crawlers.json y que el nombre de DNS inverso coincide con crawl-***-***-***-***.googlebot.com o geo-crawl-***-***-***-***.geo.googlebot.com.

## Compara con Googlebot

[Googlebot](/es/bots/googlebot): Las reglas de Googlebot afectan a Google Search y productos relacionados, mientras que las de Storebot-Google afectan a las superficies de Google Shopping.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). Storebot-Google no es uno de ellos: lee tu robots.txt buscando un grupo `Storebot-Google` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿Storebot-Google respeta robots.txt?

Sí. Google dice que los rastreadores comunes siempre obedecen las reglas de robots.txt cuando rastrean de forma automática. Dale a Storebot-Google su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que Storebot-Google está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers)
- [Google: common-crawlers.json (read 2026-10-24, creationTime 2026-10-23)](https://developers.google.com/static/crawling/ipranges/common-crawlers.json)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
