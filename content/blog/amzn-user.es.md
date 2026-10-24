title: Amzn-User: qué hace y qué cambia si lo bloqueas
h1: Amzn-User: qué hace y qué cambia si lo bloqueas
description: Amzn-User (Amazon): consulta iniciada por el usuario. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición.
slug: amzn-user
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre Amzn-User: operador Amazon, función Consulta iniciada por el usuario, respeta robots.txt No siempre, lista de direcciones Lista en su página
hero_sub: Amzn-User, de Amazon
hero_boxes: Operador|Amazon; Función|Consulta iniciada por el usuario; Respeta robots.txt|No siempre; Lista de direcciones|Lista en su página
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/amzn-searchbot|Amzn-SearchBot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: Amzn-User es el agente de usuario de Amazon que obtiene páginas en directo cuando un cliente le pregunta a Alexa algo que necesita información actual. Amazon dice que no rastrea para entrenar IA generativa y que puede no seguir todas las directivas de robots.txt, porque la acción la inicia el usuario. Amazonbot y Amzn-SearchBot son ajustes aparte.

## Qué es Amzn-User

Amzn-User es un agente de usuario de Amazon que da soporte a acciones del usuario, como responder a consultas de Alexa que requieren información actualizada. Amazon dice que, cuando un cliente hace una pregunta, Amzn-User puede obtener información en directo de la web para dar respuestas precisas en nombre del usuario. Amazon dice que no rastrea contenido para entrenar modelos de IA generativa.

| Dato | Amzn-User |
| --- | --- |
| Operador | Amazon |
| Función | Consulta iniciada por el usuario |
| Token de robots.txt | `Amzn-User` |
| Respeta robots.txt | Parcial, puede no seguir todas las directivas de robots.txt porque las acciones pueden ser iniciadas por el usuario |
| Direcciones IP | Lista en la página del proveedor (developer.amazon.com/amazonbot/live-ip-addresses) |
| Página del proveedor leída el | 24 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “Because actions taken by Amzn-User can be initiated by a user, it may not follow all robots.txt directives.”

Fuente: [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot), leído el 24 de octubre de 2026.

## Qué pasa si bloqueas Amzn-User

Amazon dice que Amzn-User puede no seguir todas las directivas de robots.txt porque sus acciones pueden ser iniciadas por un usuario. Amazon dice también que el ajuste de cada uno de sus agentes de usuario (Amazonbot, Amzn-SearchBot, Amzn-User) es independiente de los demás y que puede tardar unas 24 horas en reflejar los cambios.

## Las líneas de robots.txt

Para permitir Amzn-User:

```
User-agent: Amzn-User
Allow: /
```

Para bloquear Amzn-User:

```
User-agent: Amzn-User
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Amzn-User/0.1) Chrome/W.X.Y.Z Safari/537.36
```

## Cómo distinguir una petición real de una falsa

Amazon publica las direcciones IP de Amzn-User en una página web que muestra la lista como JSON, y la enlaza desde la página de documentación de Amazonbot.

## Compara con Amzn-SearchBot

[Amzn-SearchBot](/es/bots/amzn-searchbot): Amzn-SearchBot es un rastreador automatizado para las experiencias de búsqueda de Amazon que, según Amazon, respeta robots.txt, mientras que Amzn-User obtiene información en directo cuando un cliente lo pide y puede no seguir todas las directivas.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). Amzn-User no es uno de ellos: lee tu robots.txt buscando un grupo `Amzn-User` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿Amzn-User respeta robots.txt?

No siempre. Parcial, puede no seguir todas las directivas de robots.txt porque las acciones pueden ser iniciadas por el usuario. Por eso una regla para Amzn-User en robots.txt puede no detenerlo. Para rechazarlo con seguridad, usa una regla de cortafuegos o de CDN que combine el user agent y las direcciones publicadas.

### ¿Cómo sé que Amzn-User está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot)
- [Amazon: Amzn-User IP addresses (read 2026-10-24)](https://developer.amazon.com/amazonbot/live-ip-addresses/)
