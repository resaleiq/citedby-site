title: YandexBot: qué hace y qué cambia si lo bloqueas
h1: YandexBot: qué hace y qué cambia si lo bloqueas
description: YandexBot (Yandex): búsqueda. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: yandexbot
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre YandexBot: operador Yandex, función Búsqueda, respeta robots.txt Sí, lista de direcciones DNS inverso
hero_sub: YandexBot, de Yandex
hero_boxes: Operador|Yandex; Función|Búsqueda; Respeta robots.txt|Sí; Lista de direcciones|DNS inverso
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/googlebot|Googlebot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: Yandex enumera YandexBot como su robot de indexación principal, uno de los muchos robots de Yandex con sus propios agentes de usuario. Yandex dice que algunos descargan páginas con fines distintos de la indexación y pueden ignorar reglas restrictivas escritas para todos los robots (User-agent: *). Yandex no publica una lista de IP.

## Qué es YandexBot

Yandex enumera YandexBot como el robot de indexación principal. Yandex tiene otros muchos robots con sus propios agentes de usuario (para imágenes, vídeo, publicidad, páginas móviles, favicons y más), enumerados en la misma página. Yandex no publica una lista de IP de sus bots.

| Dato | YandexBot |
| --- | --- |
| Operador | Yandex |
| Función | Búsqueda (robot de indexación principal) |
| Token de robots.txt | `Yandex` |
| Respeta robots.txt | Sí, tiene en cuenta las reglas generales de robots.txt (User-agent: *) |
| Direcciones IP | Comprobación por DNS inverso |
| Página del proveedor leída el | 24 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “Some robots can disguise themselves as Yandex robots by indicating the relevant User Agent. You can check the authenticity of a robot using a reverse DNS lookup.”

Fuente: [Yandex Webmaster: How to check that a robot belongs to Yandex](https://yandex.com/support/webmaster/en/robot-workings/check-yandex-robots), leído el 24 de octubre de 2026.

## Qué pasa si bloqueas YandexBot

Yandex dice que varios de sus robots descargan páginas con fines distintos de la indexación y pueden ignorar reglas restrictivas escritas para todos los robots (User-agent: *). Para restringir esos robots necesitas directivas escritas expresamente para ellos, por ejemplo User-agent: YandexCalendar. Yandex añade que un documento al que el robot principal de Yandex no puede acceder nunca se indexará ni se encontrará en los resultados de búsqueda.

## Las líneas de robots.txt

Para permitir YandexBot:

```
User-agent: Yandex
Allow: /
```

Para bloquear YandexBot:

```
User-agent: Yandex
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)
```

## Cómo distinguir una petición real de una falsa

Yandex dice que hay que hacer una consulta de DNS inverso sobre la IP, comprobar que el nombre de host termina en yandex.ru, yandex.net o yandex.com y confirmarlo después con una consulta directa; ofrece además una herramienta para comprobar direcciones IP.

## Compara con Googlebot

[Googlebot](/es/bots/googlebot): Ambos son el rastreador de indexación de búsqueda principal de su operador; Yandex enumera muchos robots distintos, algunos de los cuales ignoran las reglas generales de robots.txt, y dice que no publica una lista de IP.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). YandexBot no es uno de ellos: lee tu robots.txt buscando un grupo `Yandex` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿YandexBot respeta robots.txt?

Sí, tiene en cuenta las reglas generales de robots.txt (User-agent: *). Dale a Yandex su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que YandexBot está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Yandex Webmaster: How to check that a robot belongs to Yandex](https://yandex.com/support/webmaster/en/robot-workings/check-yandex-robots)
- [Yandex Webmaster: Using robots.txt](https://yandex.com/support/webmaster/en/controlling-robot/robots-txt)
