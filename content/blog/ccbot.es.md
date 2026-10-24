title: CCBot: qué hace y qué cambia si lo bloqueas
h1: CCBot: qué hace y qué cambia si lo bloqueas
description: CCBot (Common Crawl): varias funciones. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: ccbot
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre CCBot: operador Common Crawl, función Varias funciones, respeta robots.txt Sí, lista de direcciones DNS inverso
hero_sub: CCBot, de Common Crawl
hero_boxes: Operador|Common Crawl; Función|Varias funciones; Respeta robots.txt|Sí; Lista de direcciones|DNS inverso
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/gptbot|GPTBot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: CCBot es el rastreador de Common Crawl, una organización sin ánimo de lucro que mantiene un repositorio abierto de datos de rastreo web que cualquiera puede consultar y analizar. Common Crawl dice que User-agent: CCBot con Disallow: / impide que rastree un sitio. Avisa también de que otros rastreadores se hacen pasar por CCBot, así que verifica las solicitudes.

## Qué es CCBot

CCBot es el rastreador de Common Crawl, una fundación sin ánimo de lucro que produce y mantiene un repositorio abierto de datos de rastreo web al que cualquiera puede acceder y que cualquiera puede analizar. La página del proveedor dice que los datos de rastreo están pensados para estar disponibles gratuitamente para organizaciones, el mundo académico y entidades sin ánimo de lucro.

| Dato | CCBot |
| --- | --- |
| Operador | Common Crawl |
| Función | Archivo abierto de rastreo web |
| Token de robots.txt | `CCBot` |
| Respeta robots.txt | Sí, mediante una regla de robots.txt para CCBot |
| Direcciones IP | Comprobación por DNS inverso |
| Página del proveedor leída el | 24 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “To prevent Common Crawl from crawling your website, include the following in your robots.txt”

Fuente: [Common Crawl: CCBot](https://commoncrawl.org/ccbot), leído el 24 de octubre de 2026.

## Qué pasa si bloqueas CCBot

Common Crawl dice que añadir User-agent: CCBot con Disallow: / a robots.txt impide que Common Crawl rastree el sitio. La página dice también que sabe que hay rastreadores que se identifican falsamente como CCBot y recomienda verificar las cadenas de agente de usuario.

## Las líneas de robots.txt

Para permitir CCBot:

```
User-agent: CCBot
Allow: /
```

Para bloquear CCBot:

```
User-agent: CCBot
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
CCBot/2.0 (https://commoncrawl.org/faq/)
```

## Cómo distinguir una petición real de una falsa

Common Crawl dice que CCBot funciona desde rangos de direcciones IP dedicados con DNS inverso (no para IPv6), así que una solicitud registrada se puede comprobar con una búsqueda inversa que resuelva a un nombre de host crawl.commoncrawl.org; los rangos también se publican como JSON en https://index.commoncrawl.org/ccbot.json.

## Compara con GPTBot

[GPTBot](/es/bots/gptbot): CCBot construye un archivo público de rastreo que otros pueden usar, mientras que GPTBot recoge contenido para los fines propios de OpenAI.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). CCBot no es uno de ellos: lee tu robots.txt buscando un grupo `CCBot` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿CCBot respeta robots.txt?

Sí, mediante una regla de robots.txt para CCBot. Dale a CCBot su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que CCBot está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Common Crawl: CCBot (read 2026-10-24)](https://commoncrawl.org/ccbot)
