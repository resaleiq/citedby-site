title: ExaSearchBot: qué hace y qué cambia si lo bloqueas
h1: ExaSearchBot: qué hace y qué cambia si lo bloqueas
description: ExaSearchBot (Exa): búsqueda. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: exasearchbot
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre ExaSearchBot: operador Exa, función Búsqueda, respeta robots.txt Sí, lista de direcciones Herramienta de verificación
hero_sub: ExaSearchBot, de Exa
hero_boxes: Operador|Exa; Función|Búsqueda; Respeta robots.txt|Sí; Lista de direcciones|Herramienta de verificación
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/perplexitybot|PerplexityBot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: ExaSearchBot es el rastreador de Exa, un motor de búsqueda creado para la búsqueda y la recuperación, de modo que las páginas puedan descubrirse y citarse. Exa dice que consulta robots.txt antes de obtener una página y que User-agent: ExaSearchBot con Disallow: / bloquea todo el sitio. Cada solicitud va firmada criptográficamente, así que verificarla no depende de la IP.

## Qué es ExaSearchBot

ExaSearchBot es el rastreador de Exa, un motor de búsqueda. Exa dice que su finalidad es la búsqueda y la recuperación, de modo que las páginas se vuelven descubribles y pueden citarse. Las páginas que Exa obtiene a petición de un usuario, y no por rastreo, salen con el nombre ExaUser.

| Dato | ExaSearchBot |
| --- | --- |
| Operador | Exa |
| Función | Índice de búsqueda y recuperación |
| Token de robots.txt | `ExaSearchBot` |
| Respeta robots.txt | Sí, el proveedor dice que consulta robots.txt antes de obtener una página |
| Direcciones IP | Herramienta de verificación |
| Página del proveedor leída el | 24 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “Exa is a search engine. Similar to other search engines, Exa uses a robot (ExaSearchBot) to discover and index pages on the public web.”

Fuente: [Exa: Exa Search Crawler](https://crawler.exa.ai/), leído el 24 de octubre de 2026.

## Qué pasa si bloqueas ExaSearchBot

Exa dice que User-agent: ExaSearchBot con Disallow: / bloquea a ExaSearchBot en todo el sitio. Si no hay un grupo para ExaSearchBot, sigue las reglas fijadas para los principales motores de búsqueda y, si no, el grupo *. El proveedor dice que robots.txt controla el rastreo, no la indexación, así que las páginas ya indexadas se eliminan con una metaetiqueta noindex o una cabecera X-Robots-Tag.

## Las líneas de robots.txt

Para permitir ExaSearchBot:

```
User-agent: ExaSearchBot
Allow: /
```

Para bloquear ExaSearchBot:

```
User-agent: ExaSearchBot
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
Mozilla/5.0 (compatible; ExaSearchBot/1.0; +https://crawler.exa.ai/)
```

## Cómo distinguir una petición real de una falsa

El proveedor dice que cada solicitud está firmada criptográficamente con HTTP Message Signatures (Web Bot Auth) y ofrece un directorio de claves públicas para verificarla, y que la verificación vale con independencia de la dirección IP.

## Compara con PerplexityBot

[PerplexityBot](/es/bots/perplexitybot): Ambos son rastreadores de índice de búsqueda que alimentan respuestas de IA con fuentes citadas; ExaSearchBot firma sus solicitudes con Web Bot Auth y recurre a las reglas de los principales motores de búsqueda cuando no tiene un grupo propio.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). ExaSearchBot no es uno de ellos: lee tu robots.txt buscando un grupo `ExaSearchBot` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿ExaSearchBot respeta robots.txt?

Sí, el proveedor dice que consulta robots.txt antes de obtener una página. Dale a ExaSearchBot su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que ExaSearchBot está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Exa: Exa Search Crawler](https://crawler.exa.ai/)
- [Exa: FAQs](https://exa.ai/docs/admin/faqs)
