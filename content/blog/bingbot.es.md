title: Bingbot: qué hace y qué cambia si lo bloqueas
h1: Bingbot: qué hace y qué cambia si lo bloqueas
description: Bingbot (Microsoft): búsqueda. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: bingbot
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Cuatro datos sobre Bingbot: operador Microsoft, función Búsqueda, respeta robots.txt Sí, lista de direcciones Herramienta de verificación
hero_sub: Bingbot, de Microsoft
hero_boxes: Operador|Microsoft; Función|Búsqueda; Respeta robots.txt|Sí; Lista de direcciones|Herramienta de verificación
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/googlebot|Googlebot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: Bingbot es el rastreador estándar de Microsoft y se encarga de la mayor parte del rastreo de Bing. La página de ayuda de Bing enumera cinco rastreadores: Bingbot, AdIdxBot, BingPreview, MicrosoftPreview y BingVideoPreview. Los controlas con robots.txt, y la velocidad de rastreo con la herramienta Crawl control de Bing Webmaster Tools, no con robots.txt.

## Qué es Bingbot

La página de Bing se titula «Overview of Bing crawlers (user agents)» y dice que Bing opera hoy estos rastreadores principales: Bingbot (el rastreador estándar), AdIdxBot (lo usa Bing Ads, que rastrea anuncios y sigue sus sitios web para el control de calidad), BingPreview (instantáneas de páginas para Bing), MicrosoftPreview (instantáneas para productos de Microsoft) y BingVideoPreview (vistas previas de vídeo, solo en Bing). Bingbot, AdIdxBot, BingPreview y BingVideoPreview tienen variantes de escritorio y móvil. La página no nombra ningún rastreador de IA aparte. La misma sección de ayuda incluye «How To Permanently Remove a URL or Page from Bing or Copilot», que es la página que conviene leer si el objetivo es eliminar contenido y no dar acceso.

| Dato | Bingbot |
| --- | --- |
| Operador | Microsoft |
| Función | Rastreador de búsqueda |
| Token de robots.txt | `bingbot` |
| Respeta robots.txt | Sí |
| Direcciones IP | Herramienta de verificación |
| Página del proveedor leída el | 21 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “Bingbot is our standard crawler and handles most of our crawling needs each day.”

Fuente: [Microsoft Bing Webmaster help: Which Crawlers Does Bing Use?](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0), leído el 21 de octubre de 2026.

## Qué pasa si bloqueas Bingbot

La página de Bing no dice qué cuesta un bloqueo; esta es nuestra lectura, no la de Bing. Bingbot es el rastreador que alimenta Bing, así que bloquearlo en robots.txt hace que Bing deje de rastrear esas páginas, y todo lo que depende del índice de Bing también las pierde. Bing te da dos controles: robots.txt indica a sus rastreadores cómo interactuar con tu sitio, y Bing Webmaster Tools tiene una herramienta Crawl control que fija la velocidad de rastreo por horas.

## Las líneas de robots.txt

Para permitir Bingbot:

```
User-agent: bingbot
Allow: /
```

Para bloquear Bingbot:

```
User-agent: bingbot
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm) Chrome/W.X.Y.Z Safari/537.36
```

## Cómo distinguir una petición real de una falsa

Bing dice que las cadenas de agente de usuario son fáciles de falsificar, así que no toda solicitud que las lleva procede de un rastreador real de Bing. Para comprobar la dirección, usa la herramienta Verify Bingbot o alguno de los otros métodos de verificación que describe Bing. En la cadena de user-agent, W.X.Y.Z representa la versión de Microsoft Edge con la que Bing renderiza, que Bing dice que actualiza con regularidad. No leímos ninguna lista de IP en esa página, así que no indicamos ningún número.

## Compara con Googlebot

[Googlebot](/es/bots/googlebot): El otro rastreador de búsqueda principal: otro token y otra verificación.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba Bingbot con una petición real y lee robots.txt para él. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿Bingbot respeta robots.txt?

Sí. Dale a bingbot su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que Bingbot está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Microsoft Bing Webmaster help: Which Crawlers Does Bing Use?](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0)
