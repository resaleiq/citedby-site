title: ImagesiftBot: qué hace y qué cambia si lo bloqueas
h1: ImagesiftBot: qué hace y qué cambia si lo bloqueas
description: ImagesiftBot (Hive (ImageSift)): búsqueda. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: imagesiftbot
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre ImagesiftBot: operador Hive (ImageSift), función Búsqueda, respeta robots.txt Sí, lista de direcciones Ninguna
hero_sub: ImagesiftBot, de Hive (ImageSift)
hero_boxes: Operador|Hive (ImageSift); Función|Búsqueda; Respeta robots.txt|Sí; Lista de direcciones|Ninguna
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/googlebot|Googlebot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: ImagesiftBot es el rastreador de ImageSift, un producto de Hive. Recoge imágenes de acceso público junto con la URL del host, el texto de la página y el texto alternativo de la imagen para un índice de imágenes similares. El proveedor dice que respeta robots.txt y Crawl-delay, y que sigue las reglas de Googlebot si ninguna se dirige a él.

## Qué es ImagesiftBot

ImageSiftBot es el rastreador de ImageSift, un producto de Hive. Recoge imágenes de acceso público, junto con la URL del host, el texto de la página y el texto alternativo de la imagen. ImageSift guarda los datos en un índice que sus productos usan para buscar y recuperar imágenes similares.

| Dato | ImagesiftBot |
| --- | --- |
| Operador | Hive (ImageSift) |
| Función | Índice de imágenes para búsqueda de imágenes similares |
| Token de robots.txt | `ImagesiftBot` |
| Respeta robots.txt | Sí, y admite Crawl-delay |
| Direcciones IP | Ninguna publicada |
| Página del proveedor leída el | 24 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “ImageSiftBot is a web crawler that scrapes the internet for publicly available images to support our suite of web intelligence products”

Fuente: [Imagesift by Hive: ImageSift Bot](https://imagesift.com/about), leído el 24 de octubre de 2026.

## Qué pasa si bloqueas ImagesiftBot

El proveedor dice que se respetan las directivas estándar de robots.txt dirigidas a ImagesiftBot y que admite Crawl-delay. Si ninguna regla se dirige a ImagesiftBot pero sí una a Googlebot, sigue las reglas de Googlebot. La página indica también support@imagesift.com para las solicitudes de exclusión.

## Las líneas de robots.txt

Para permitir ImagesiftBot:

```
User-agent: ImagesiftBot
Allow: /
```

Para bloquear ImagesiftBot:

```
User-agent: ImagesiftBot
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
Mozilla/5.0 (compatible; ImagesiftBot; +imagesift.com)
```

## Cómo distinguir una petición real de una falsa

La página del proveedor no publica una lista de IP ni un método de verificación.

## Compara con Googlebot

[Googlebot](/es/bots/googlebot): ImagesiftBot recurre a las reglas de robots.txt de Googlebot cuando no tiene las suyas, y recoge imágenes para un índice de imágenes similares y no para una búsqueda web general.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). ImagesiftBot no es uno de ellos: lee tu robots.txt buscando un grupo `ImagesiftBot` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿ImagesiftBot respeta robots.txt?

Sí, y admite Crawl-delay. Dale a ImagesiftBot su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que ImagesiftBot está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Imagesift by Hive: ImageSift Bot](https://imagesift.com/about)
