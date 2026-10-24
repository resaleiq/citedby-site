title: Amazonbot: qué hace y qué cambia si lo bloqueas
h1: Amazonbot: qué hace y qué cambia si lo bloqueas
description: Amazonbot (Amazon): varias funciones. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: amazonbot
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Cuatro datos sobre Amazonbot: operador Amazon, función Varias funciones, respeta robots.txt Sí, lista de direcciones Lista en su página
hero_sub: Amazonbot, de Amazon
hero_boxes: Operador|Amazon; Función|Varias funciones; Respeta robots.txt|Sí; Lista de direcciones|Lista en su página
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/duckassistbot|DuckAssistBot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: Amazonbot sirve para mejorar los productos y servicios de Amazon y puede usarse para entrenar modelos de IA de Amazon. La página de Amazon también recoge Amzn-SearchBot, que hace el contenido apto para experiencias de búsqueda como Alexa, y Amzn-User, que puede no seguir todas las directivas de robots.txt. Cada ajuste es independiente.

## Qué es Amazonbot

La página de Amazon recoge tres agentes de usuario y dice que cada ajuste es independiente de los demás y que puede tardar unas 24 horas en aplicarse: Amazonbot, Amzn-SearchBot y Amzn-User. Solo del primero se dice que puede entrenar modelos de IA de Amazon.

| Dato | Amazonbot |
| --- | --- |
| Operador | Amazon |
| Función | Mejora de productos, puede entrenar modelos de IA de Amazon |
| Token de robots.txt | `Amazonbot` |
| Respeta robots.txt | Sí, los cambios tardan unas 24 horas |
| Direcciones IP | Lista en la página del proveedor (developer.amazon.com/amazonbot/ip-addresses) |
| Página del proveedor leída el | 21 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “Amazonbot is used to improve our products and services. This helps us provide more accurate information to customers and may be used to train Amazon AI models.”

Fuente: [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot), leído el 21 de octubre de 2026.

## Qué pasa si bloqueas Amazonbot

Amzn-SearchBot es para experiencias de búsqueda como Alexa: si lo permites, el contenido es apto para aparecer ahí. Amzn-User responde a consultas en directo de Alexa que necesitan información actualizada. Amazon dice que puede no seguir todas las directivas de robots.txt y que no rastrea para entrenar IA generativa. Por eso, un robots.txt que solo menciona Amazonbot no recoge tu política para los otros dos.

## Las líneas de robots.txt

Para permitir Amazonbot:

```
User-agent: Amazonbot
Allow: /
```

Para bloquear Amazonbot:

```
User-agent: Amazonbot
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Amazonbot/0.1) Chrome/W.X.Y.Z Safari/537.36
```

## Cómo distinguir una petición real de una falsa

Amazon publica las direcciones de Amazonbot y, en páginas aparte, las de Amzn-SearchBot y las de las consultas en directo. Las listas son páginas HTML, no un archivo JSON, así que no indicamos ningún número. Amazon dice además que, si robots.txt no menciona Amzn-SearchBot pero permite a otros bots de búsqueda, Amzn-SearchBot rastrea de acuerdo con ese archivo.

## Compara con DuckAssistBot

[DuckAssistBot](/es/bots/duckassistbot): Otro rastreador de contenido para respuestas, con exclusión declarada y un retraso de 72 horas.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). Amazonbot no es uno de ellos: lee tu robots.txt buscando un grupo `Amazonbot` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿Amazonbot respeta robots.txt?

Sí, los cambios tardan unas 24 horas. Dale a Amazonbot su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que Amazonbot está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot)
- [developer.amazon.com/amazonbot/ip-addresses](https://developer.amazon.com/amazonbot/ip-addresses)
