title: Meta-WebIndexer: qué hace y qué cambia si lo bloqueas
h1: Meta-WebIndexer: qué hace y qué cambia si lo bloqueas
description: Meta-WebIndexer (Meta): búsqueda. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: meta-webindexer
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre Meta-WebIndexer: operador Meta, función Búsqueda, respeta robots.txt Sí, lista de direcciones Ninguna
hero_sub: Meta-WebIndexer, de Meta
hero_boxes: Operador|Meta; Función|Búsqueda; Respeta robots.txt|Sí; Lista de direcciones|Ninguna
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/meta-externalagent|Meta-ExternalAgent; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: Meta-WebIndexer es un rastreador de Meta que navega por la web para mejorar los resultados de búsqueda de Meta AI. Meta dice que permitirlo en robots.txt le ayuda a citar y enlazar tu contenido en las respuestas de Meta AI. Meta dice que sus rastreadores se bloquean con un disallow y que un cambio puede tardar hasta 24 horas.

## Qué es Meta-WebIndexer

Meta-WebIndexer es un rastreador de Meta que navega por la web para mejorar la calidad de los resultados de búsqueda de Meta AI para los usuarios. Meta dice que permitirlo en robots.txt ayuda a Meta a citar y enlazar tu contenido en las respuestas de Meta AI. Meta lo documenta junto con Meta-ExternalAgent, Meta-ExternalFetcher, Meta-ExternalAds y FacebookExternalHit en una sola página.

| Dato | Meta-WebIndexer |
| --- | --- |
| Operador | Meta |
| Función | Búsqueda |
| Token de robots.txt | `Meta-WebIndexer` |
| Respeta robots.txt | Sí, los cambios pueden tardar hasta 24 horas |
| Direcciones IP | Ninguna publicada |
| Página del proveedor leída el | 24 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “The Meta-WebIndexer crawler navigates the web to improve Meta AI search result quality for users. In doing so, Meta analyzes online content to enhance the relevance and accuracy of Meta AI.”

Fuente: [Meta: Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers), leído el 24 de octubre de 2026.

## Qué pasa si bloqueas Meta-WebIndexer

Meta dice que puedes bloquear sus rastreadores añadiendo a robots.txt un disallow para el rastreador correspondiente, y que los cambios en robots.txt pueden tardar hasta 24 horas en surtir efecto. Meta dice que permitir Meta-WebIndexer le ayuda a citar y enlazar tu contenido en las respuestas de Meta AI. La página de Meta no dice si un disallow para Meta-WebIndexer afecta a sus otros rastreadores.

## Las líneas de robots.txt

Para permitir Meta-WebIndexer:

```
User-agent: Meta-WebIndexer
Allow: /
```

Para bloquear Meta-WebIndexer:

```
User-agent: Meta-WebIndexer
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
meta-webindexer/1.1
```

## Cómo distinguir una petición real de una falsa

La página de rastreadores de Meta no enumera direcciones IP ni un método de verificación para este rastreador; lo identifica por su cadena de user-agent.

## Compara con Meta-ExternalAgent

[Meta-ExternalAgent](/es/bots/meta-externalagent): Meta-WebIndexer es para los resultados de búsqueda y las citas de Meta AI, mientras que Meta describe a Meta-ExternalAgent como un rastreador para usos como entrenar modelos fundacionales de IA o indexar contenido directamente.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). Meta-WebIndexer no es uno de ellos: lee tu robots.txt buscando un grupo `Meta-WebIndexer` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿Meta-WebIndexer respeta robots.txt?

Sí, los cambios pueden tardar hasta 24 horas. Dale a Meta-WebIndexer su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que Meta-WebIndexer está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Meta: Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers)
