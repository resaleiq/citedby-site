title: YouBot: qué hace y qué cambia si lo bloqueas
h1: YouBot: qué hace y qué cambia si lo bloqueas
description: YouBot (You.com): búsqueda. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: youbot
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre YouBot: operador You.com, función Búsqueda, respeta robots.txt Sí, lista de direcciones Lista en su página
hero_sub: YouBot, de You.com
hero_boxes: Operador|You.com; Función|Búsqueda; Respeta robots.txt|Sí; Lista de direcciones|Lista en su página
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/mojeekbot|MojeekBot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: YouBot es el rastreador web que alimenta el motor de búsqueda You.com: descubre e indexa páginas para sus resultados. You.com dice que respeta robots.txt, atiende Crawl-delay y guarda robots.txt en caché durante 30 minutos. User-agent: YouBot con Disallow: / lo bloquea en todo el sitio.

## Qué es YouBot

YouBot es el rastreador web que alimenta el motor de búsqueda You.com. Descubre e indexa páginas web para los resultados de búsqueda de You.com. You.com dice que X.X.X.X en el agente de usuario representa el número de versión de Google Chrome.

| Dato | YouBot |
| --- | --- |
| Operador | You.com |
| Función | Búsqueda |
| Token de robots.txt | `YouBot` |
| Respeta robots.txt | Sí, robots.txt se guarda en caché 30 minutos, así que los cambios pueden tardar hasta 30 minutos |
| Direcciones IP | Lista en la página del proveedor (you.com/docs/youbot) |
| Página del proveedor leída el | 24 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “YouBot is the web crawler that powers the You.com search engine.”

Fuente: [You.com Docs: YouBot: You.com's Web Crawler](https://docs.you.com/youbot), leído el 24 de octubre de 2026.

## Qué pasa si bloqueas YouBot

You.com dice que YouBot respeta robots.txt y muestra User-agent: YouBot con Disallow: / como la forma de bloquearlo en todo el sitio. También atiende Crawl-delay y guarda robots.txt en caché durante 30 minutos. La página no describe ningún otro agente de You.com.

## Las líneas de robots.txt

Para permitir YouBot:

```
User-agent: YouBot
Allow: /
```

Para bloquear YouBot:

```
User-agent: YouBot
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; YouBot/1.0; +https://docs.you.com/youbot; env:prod) Chrome/X.X.X.X Safari/537.36
```

## Cómo distinguir una petición real de una falsa

You.com dice que las solicitudes proceden de 68.67.112.0/24, que los hosts se resuelven como youbot-{octets-with-hyphens}.search.you.com y que las solicitudes llevan firmas Web Bot Auth de Cloudflare con claves públicas en you.com/.well-known/http-message-signatures-directory.

## Compara con MojeekBot

[MojeekBot](/es/bots/mojeekbot): Ambos son rastreadores de motores de búsqueda que siguen robots.txt; You.com admite Crawl-delay y firma las solicitudes con Web Bot Auth, mientras que Mojeek no admite Crawl-delay.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). YouBot no es uno de ellos: lee tu robots.txt buscando un grupo `YouBot` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿YouBot respeta robots.txt?

Sí, robots.txt se guarda en caché 30 minutos, así que los cambios pueden tardar hasta 30 minutos. Dale a YouBot su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que YouBot está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [You.com Docs: YouBot: You.com's Web Crawler](https://docs.you.com/youbot)
