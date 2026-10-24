title: LinkupBot: qué hace y qué cambia si lo bloqueas
h1: LinkupBot: qué hace y qué cambia si lo bloqueas
description: LinkupBot (Linkup): búsqueda. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: linkupbot
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre LinkupBot: operador Linkup, función Búsqueda, respeta robots.txt Sí, lista de direcciones Lista en su página
hero_sub: LinkupBot, de Linkup
hero_boxes: Operador|Linkup; Función|Búsqueda; Respeta robots.txt|Sí; Lista de direcciones|Lista en su página
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/perplexitybot|PerplexityBot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: LinkupBot es el rastreador web de Linkup. Obtiene páginas de acceso público para construir el índice de búsqueda de Linkup, que según Linkup alimenta la búsqueda y el anclaje web de aplicaciones de IA. Linkup dice que User-agent: LinkupBot con Disallow: / bloquea todo el sitio y que robots.txt no es un mecanismo de control de acceso.

## Qué es LinkupBot

LinkupBot es el rastreador web de Linkup. Obtiene páginas de acceso público para construir y mantener el índice de búsqueda de Linkup, que según Linkup alimenta la búsqueda y el anclaje web de aplicaciones de IA.

| Dato | LinkupBot |
| --- | --- |
| Operador | Linkup |
| Función | Índice de búsqueda para la búsqueda web de IA |
| Token de robots.txt | `LinkupBot` |
| Respeta robots.txt | Sí, el proveedor dice que respeta las reglas de robots.txt aplicables |
| Direcciones IP | Lista en la página del proveedor (www.linkup.so/linkupbot-ips.txt) |
| Página del proveedor leída el | 24 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “LinkupBot is Linkup’s web crawler. It discovers and retrieves publicly accessible webpages to build and maintain the Linkup web search index, which powers search and web grounding for AI applications.”

Fuente: [Linkup: LinkupBot](https://www.linkup.so/bot), leído el 24 de octubre de 2026.

## Qué pasa si bloqueas LinkupBot

Según el proveedor, añadir User-agent: LinkupBot con Disallow: / a robots.txt bloquea todo el sitio. El proveedor dice también que las reglas de robots se aplican por host, que permitir a LinkupBot en un cortafuegos no anula robots.txt y que robots.txt no es un mecanismo de control de acceso.

## Las líneas de robots.txt

Para permitir LinkupBot:

```
User-agent: LinkupBot
Allow: /
```

Para bloquear LinkupBot:

```
User-agent: LinkupBot
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
LinkupBot/1.0 (LinkupBot for web indexing; https://www.linkup.so/bot; bot@linkup.so)
```

## Cómo distinguir una petición real de una falsa

El proveedor dice que las solicitudes llegan desde los rangos CIDR de su lista publicada y que se verifique con una IP de origen de esa lista y con un user-agent que contenga el token LinkupBot, las dos cosas a la vez.

## Compara con PerplexityBot

[PerplexityBot](/es/bots/perplexitybot): Ambos construyen un índice de búsqueda que alimenta respuestas de IA; el índice de LinkupBot sirve a aplicaciones de IA mediante el servicio de búsqueda y anclaje de Linkup, y su lista de IP es un archivo de texto plano y no JSON.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). LinkupBot no es uno de ellos: lee tu robots.txt buscando un grupo `LinkupBot` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿LinkupBot respeta robots.txt?

Sí, el proveedor dice que respeta las reglas de robots.txt aplicables. Dale a LinkupBot su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que LinkupBot está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Linkup: LinkupBot](https://www.linkup.so/bot)
- [Linkup: linkupbot-ips.txt (plain text, read 2026-10-24)](https://www.linkup.so/linkupbot-ips.txt)
