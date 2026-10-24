title: Googlebot: qué hace y qué cambia si lo bloqueas
h1: Googlebot: qué hace y qué cambia si lo bloqueas
description: Googlebot (Google): búsqueda. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: googlebot
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Cuatro datos sobre Googlebot: operador Google, función Búsqueda, respeta robots.txt Sí, lista de direcciones 317 rangos
hero_sub: Googlebot, de Google
hero_boxes: Operador|Google; Función|Búsqueda; Respeta robots.txt|Sí; Lista de direcciones|317 rangos
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/google-extended|Google-Extended; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: Googlebot es el rastreador principal de Google para Search. Google dice que sus rastreadores comunes siempre obedecen las reglas de robots.txt cuando rastrean de forma automática. Las preferencias de rastreo para el token Googlebot afectan a Google Search, incluido Discover, y a productos como Imágenes, Vídeo y Noticias. Google publica 317 rangos de IP para él.

## Qué es Googlebot

Googlebot es el rastreador del que parte toda comprobación de Search. La página de Google enumera varios rastreadores, y el único token Googlebot gobierna Search, Discover y los productos que se nutren del mismo rastreo, como Imágenes, el modo Vídeo y Noticias.

| Dato | Googlebot |
| --- | --- |
| Operador | Google |
| Función | Búsqueda (también Imágenes, Vídeo, Noticias, Discover) |
| Token de robots.txt | `Googlebot` |
| Respeta robots.txt | Sí, siempre que rastrea de forma automática |
| Direcciones IP | 317 rangos (developers.google.com/static/search/apis/ipranges/googlebot.json, archivo del 2026-10-20) |
| Página del proveedor leída el | 21 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “Google's common crawlers are used to find information for building Google's search indexes, perform other product specific crawls, and for analysis. They always obey robots.txt rules when crawling automatically.”

Fuente: [Google Search Central: Google's common crawlers (last updated 2026-10-15)](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers), leído el 21 de octubre de 2026.

## Qué pasa si bloqueas Googlebot

Un Disallow para Googlebot no es una exclusión específica de la IA; afecta a la propia Google Search, incluido Discover y las funciones que se apoyan en ella, según la lista de productos afectados de Google. El control más acotado para el entrenamiento de Gemini es el token aparte [Google-Extended](/es/bots/google-extended).

## Las líneas de robots.txt

Para permitir Googlebot:

```
User-agent: Googlebot
Allow: /
```

Para bloquear Googlebot:

```
User-agent: Googlebot
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)
```

## Cómo distinguir una petición real de una falsa

Google publica los rangos que usan sus rastreadores comunes. El archivo de Googlebot tenía 317 prefijos el 21 de octubre de 2026, con hora de creación 2026-10-20 14:46 UTC. Google documenta también una máscara de DNS inverso para confirmar un nombre de host, así que una solicitud se comprueba de dos maneras: la dirección contra el archivo, y la búsqueda inversa contra la máscara. La propia página se actualizó por última vez el 2026-10-15.

## Compara con Google-Extended

[Google-Extended](/es/bots/google-extended): Un token de control para el entrenamiento de Gemini; nunca obtiene una página.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba Googlebot con una petición real y lee robots.txt para él. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿Googlebot respeta robots.txt?

Sí, siempre que rastrea de forma automática. Dale a Googlebot su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que Googlebot está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Google Search Central: Google's common crawlers (last updated 2026-10-15)](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers)
- [developers.google.com/static/search/apis/ipranges/googlebot.json](https://developers.google.com/static/crawling/ipranges/common-crawlers.json)
