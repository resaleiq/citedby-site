title: GoogleOther: qué hace y qué cambia si lo bloqueas
h1: GoogleOther: qué hace y qué cambia si lo bloqueas
description: GoogleOther (Google): varias funciones. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: googleother
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre GoogleOther: operador Google, función Varias funciones, respeta robots.txt Sí, lista de direcciones 317 rangos
hero_sub: GoogleOther, de Google
hero_boxes: Operador|Google; Función|Varias funciones; Respeta robots.txt|Sí; Lista de direcciones|317 rangos
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/googlebot|Googlebot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: GoogleOther es el rastreador genérico de Google. Varios equipos de producto de Google lo usan para obtener contenido de acceso público, por ejemplo en rastreos puntuales para investigación y desarrollo internos. Google dice que las reglas dirigidas a GoogleOther no afectan a ningún producto concreto. GoogleOther-Image y GoogleOther-Video se documentan como tokens aparte.

## Qué es GoogleOther

GoogleOther es el rastreador genérico de Google, que usan varios equipos de producto de Google para obtener contenido de acceso público, por ejemplo en rastreos puntuales para investigación y desarrollo internos. Google lo incluye entre sus rastreadores comunes, junto a Googlebot, y documenta también GoogleOther-Image y GoogleOther-Video como versiones optimizadas para URL de imágenes y de vídeo. La página de Google no dice que se use para entrenar IA.

| Dato | GoogleOther |
| --- | --- |
| Operador | Google |
| Función | Rastreo genérico para varios equipos de producto de Google |
| Token de robots.txt | `GoogleOther` |
| Respeta robots.txt | Sí. Google dice que los rastreadores comunes siempre obedecen las reglas de robots.txt cuando rastrean de forma automática. |
| Direcciones IP | 317 rangos (developers.google.com/static/crawling/ipranges/common-crawlers.json, archivo del 2026-10-23) |
| Página del proveedor leída el | 24 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “GoogleOther is the generic crawler that may be used by various product teams for fetching publicly accessible content from sites. For example, it may be used for one-off crawls for internal research and development.”

Fuente: [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers), leído el 24 de octubre de 2026.

## Qué pasa si bloqueas GoogleOther

Google dice que las preferencias de rastreo dirigidas al agente de usuario GoogleOther no afectan a ningún producto concreto. Google documenta GoogleOther-Image y GoogleOther-Video como tokens de robots.txt aparte, así que no se dice que una regla para GoogleOther los cubra, y el token Googlebot es otro token distinto.

## Las líneas de robots.txt

Para permitir GoogleOther:

```
User-agent: GoogleOther
Allow: /
```

Para bloquear GoogleOther:

```
User-agent: GoogleOther
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GoogleOther) Chrome/W.X.Y.Z Safari/537.36
```

## Cómo distinguir una petición real de una falsa

El archivo developers.google.com/static/crawling/ipranges/common-crawlers.json tenía 317 rangos el 24 de octubre de 2026, archivo del 2026-10-23.

Google dice que los rastreadores comunes por lo general rastrean desde los rangos de common-crawlers.json y que el nombre de DNS inverso coincide con crawl-***-***-***-***.googlebot.com o geo-crawl-***-***-***-***.geo.googlebot.com.

## Compara con Googlebot

[Googlebot](/es/bots/googlebot): Googlebot rastrea para Google Search y productos relacionados, mientras que GoogleOther es un rastreador genérico cuyas reglas de robots.txt no afectan a ningún producto concreto de Google.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). GoogleOther no es uno de ellos: lee tu robots.txt buscando un grupo `GoogleOther` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿GoogleOther respeta robots.txt?

Sí. Google dice que los rastreadores comunes siempre obedecen las reglas de robots.txt cuando rastrean de forma automática. Dale a GoogleOther su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que GoogleOther está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers)
- [Google: common-crawlers.json (read 2026-10-24, creationTime 2026-10-23)](https://developers.google.com/static/crawling/ipranges/common-crawlers.json)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
