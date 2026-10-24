title: ExaUser: qué hace y qué cambia si lo bloqueas
h1: ExaUser: qué hace y qué cambia si lo bloqueas
description: ExaUser (Exa): consulta iniciada por el usuario. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: exauser
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre ExaUser: operador Exa, función Consulta iniciada por el usuario, respeta robots.txt No siempre, lista de direcciones Herramienta de verificación
hero_sub: ExaUser, de Exa
hero_boxes: Operador|Exa; Función|Consulta iniciada por el usuario; Respeta robots.txt|No siempre; Lista de direcciones|Herramienta de verificación
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/exasearchbot|ExaSearchBot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: ExaUser es el agente que Exa usa para obtener una página en directo cuando un usuario, o una aplicación creada con la API de Exa, pide su contenido actual. Exa dice que es posible que robots.txt no se aplique a estas consultas iniciadas por el usuario. Las exclusiones de búsqueda y el rastreo automático se controlan con el token ExaSearchBot.

## Qué es ExaUser

ExaUser es el agente que Exa usa para obtener una página en directo cuando un usuario, o una aplicación creada con la API de Exa, pide su contenido actual. Exa dice que no se usa para rastrear la web de forma automática; eso lo hace ExaSearchBot. No intenta saltarse inicios de sesión, muros de pago ni CAPTCHA, y no envía formularios.

| Dato | ExaUser |
| --- | --- |
| Operador | Exa |
| Función | Consulta iniciada por el usuario |
| Token de robots.txt | `ExaUser` |
| Respeta robots.txt | Parcial, el proveedor dice que es posible que las reglas de robots.txt no se apliquen a las consultas iniciadas por el usuario |
| Direcciones IP | Herramienta de verificación |
| Página del proveedor leída el | 24 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “Exa uses ExaUser to fetch a page live when a user, or an application built on the Exa API, asks for its current content.”

Fuente: [Exa: ExaUser](https://crawler.exa.ai/exauser), leído el 24 de octubre de 2026.

## Qué pasa si bloqueas ExaUser

Exa dice que, como las consultas las inicia un usuario, es posible que las reglas de robots.txt no se apliquen a ExaUser. Dice también que ExaUser no se usa para decidir si el contenido aparece en la búsqueda de Exa y que las exclusiones de búsqueda y el rastreo automático se gestionan con el token ExaSearchBot en robots.txt.

## Las líneas de robots.txt

Para permitir ExaUser:

```
User-agent: ExaUser
Allow: /
```

Para bloquear ExaUser:

```
User-agent: ExaUser
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
Mozilla/5.0 (compatible; ExaUser/1.0; +https://crawler.exa.ai/exauser)
```

## Cómo distinguir una petición real de una falsa

El proveedor dice que cada solicitud va firmada con Web Bot Auth (RFC 9421) y publica sus claves en un directorio público; no publica una lista de IP.

## Compara con ExaSearchBot

[ExaSearchBot](/es/bots/exasearchbot): ExaSearchBot rastrea de forma automática para construir el índice de búsqueda de Exa y sigue robots.txt, mientras que ExaUser obtiene una página solo cuando un usuario o una aplicación lo pide y el proveedor dice que es posible que robots.txt no se aplique.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). ExaUser no es uno de ellos: lee tu robots.txt buscando un grupo `ExaUser` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿ExaUser respeta robots.txt?

No siempre: el proveedor dice que es posible que las reglas de robots.txt no se apliquen a las consultas iniciadas por el usuario. Por eso una regla para ExaUser en robots.txt puede no detenerlo. Para rechazarlo con seguridad, usa una regla de cortafuegos o de CDN que combine el user agent y las direcciones publicadas.

### ¿Cómo sé que ExaUser está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Exa: ExaUser](https://crawler.exa.ai/exauser)
- [Exa: Exa Search Crawler](https://crawler.exa.ai/)
