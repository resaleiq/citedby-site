title: Baiduspider: qué hace y qué cambia si lo bloqueas
h1: Baiduspider: qué hace y qué cambia si lo bloqueas
description: Baiduspider (Baidu): búsqueda. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: baiduspider
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre Baiduspider: operador Baidu, función Búsqueda, respeta robots.txt Sí, lista de direcciones DNS inverso
hero_sub: Baiduspider, de Baidu
hero_boxes: Operador|Baidu; Función|Búsqueda; Respeta robots.txt|Sí; Lista de direcciones|DNS inverso
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/bingbot|Bingbot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: Baiduspider es el rastreador del motor de búsqueda de Baidu. Baidu dice que sigue el protocolo robots.txt y que bloquear Baiduspider bloquea todos los agentes de usuario de Baidu, por lo que tus páginas no aparecerán en los resultados de Baidu. Baiduspider-cpro y Baiduspider-ads funcionan según acuerdos con clientes y no siguen los registros de robots.txt.

## Qué es Baiduspider

Baiduspider es el rastreador del motor de búsqueda de Baidu: visita páginas y las incorpora al índice de Baidu. Baidu usa distintos agentes de usuario para distintos productos, por ejemplo Baiduspider para la búsqueda en PC y móvil, y Baiduspider-image, Baiduspider-video y Baiduspider-news para esas búsquedas.

| Dato | Baiduspider |
| --- | --- |
| Operador | Baidu |
| Función | Búsqueda |
| Token de robots.txt | `Baiduspider` |
| Respeta robots.txt | Sí en Baiduspider; Baiduspider-cpro y Baiduspider-ads no siguen los registros de robots.txt |
| Direcciones IP | Comprobación por DNS inverso |
| Página del proveedor leída el | 24 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “Baiduspider is Baidu search engine program which is used to visit pages on the internet and build information into Baidu index.”

Fuente: [Baidu Help Center: FAQs of Baiduspider](https://help.baidu.com/question?prod_id=99&class=0&id=3001), leído el 24 de octubre de 2026.

## Qué pasa si bloqueas Baiduspider

Baidu dice que Baiduspider funciona según el protocolo robots.txt y que, si lo bloqueas, tus páginas no se encontrarán en los resultados de búsqueda de Baidu ni en ningún otro resultado que ofrezca Baidu. Puedes fijar reglas distintas para distintos agentes de usuario de Baidu, y bloquear Baiduspider bloquea todos los agentes de usuario de Baidu. Baiduspider-cpro y Baiduspider-ads funcionan según acuerdos con clientes y no siguen los registros de robots.txt.

## Las líneas de robots.txt

Para permitir Baiduspider:

```
User-agent: Baiduspider
Allow: /
```

Para bloquear Baiduspider:

```
User-agent: Baiduspider
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
Baiduspider
```

## Cómo distinguir una petición real de una falsa

Baidu recomienda hacer una consulta de DNS inverso sobre la IP visitante; el nombre de host de Baiduspider es *.baidu.com o *.baidu.jp, y cualquier otro nombre de host es falso.

## Compara con Bingbot

[Bingbot](/es/bots/bingbot): Ambos rastrean para un motor de búsqueda; Baidu documenta varios agentes de usuario por producto (imagen, vídeo, noticias, anuncios) bajo el nombre Baiduspider y verifica por el nombre de host del DNS inverso.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). Baiduspider no es uno de ellos: lee tu robots.txt buscando un grupo `Baiduspider` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿Baiduspider respeta robots.txt?

Sí en Baiduspider; Baiduspider-cpro y Baiduspider-ads no siguen los registros de robots.txt. Dale a Baiduspider su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que Baiduspider está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Baidu Help Center: FAQs of Baiduspider](https://help.baidu.com/question?prod_id=99&class=0&id=3001)
- [Baidu Help Center: How to block the crawling (robots.txt)](https://www.baidu.com/search/robots_english.html)
