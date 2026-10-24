title: Meta-ExternalAgent: qué hace y qué cambia si lo bloqueas
h1: Meta-ExternalAgent: qué hace y qué cambia si lo bloqueas
description: Meta-ExternalAgent (Meta): varias funciones. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: meta-externalagent
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Cuatro datos sobre Meta-ExternalAgent: operador Meta, función Varias funciones, respeta robots.txt Sí, lista de direcciones Ninguna
hero_sub: Meta-ExternalAgent, de Meta
hero_boxes: Operador|Meta; Función|Varias funciones; Respeta robots.txt|Sí; Lista de direcciones|Ninguna
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/gptbot|GPTBot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: Meta-ExternalAgent es el rastreador de Meta para usos como entrenar modelos fundacionales de IA o mejorar productos indexando contenido directamente. La página de Meta, actualizada el 21 de mayo de 2026, enumera cinco agentes. Dice que Meta-ExternalFetcher y FacebookExternalHit pueden saltarse robots.txt y que los cambios pueden tardar hasta 24 horas.

## Qué es Meta-ExternalAgent

La página de Meta enumera cinco rastreadores. FacebookExternalHit obtiene una página cuando alguien comparte un enlace en Facebook, Instagram o Messenger, para guardar en caché su título, su descripción y su miniatura. Meta-WebIndexer mejora los resultados de búsqueda de Meta AI, y Meta dice que permitirlo ayuda a Meta a citar y enlazar tu contenido en las respuestas de Meta AI. Meta-ExternalAds rastrea para productos de publicidad y de empresa. Meta-ExternalAgent es el que se usa para entrenar modelos fundacionales de IA o para indexar. Meta-ExternalFetcher obtiene enlaces concretos a petición de un usuario, incluido ayudar a la IA a navegar por sitios web para completar tareas de los usuarios.

| Dato | Meta-ExternalAgent |
| --- | --- |
| Operador | Meta |
| Función | Entrenamiento de modelos de IA e indexación de contenido |
| Token de robots.txt | `meta-externalagent` |
| Respeta robots.txt | Sí |
| Direcciones IP | Ninguna publicada |
| Página del proveedor leída el | 21 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “The Meta-ExternalAgent crawler crawls the web for use cases such as training foundation AI models or improving products by indexing content directly.”

Fuente: [Meta for Developers: Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers), leído el 21 de octubre de 2026.

## Qué pasa si bloqueas Meta-ExternalAgent

Bloquear meta-externalagent afecta solo a ese agente: los ejemplos de Meta dan un grupo aparte para cada token, y los otros cuatro tienen el suyo. El que más cuesta bloquear por error es FacebookExternalHit, porque genera la vista previa del enlace cuando alguien comparte tu página. Dos de los cinco pueden ignorar tu robots.txt: Meta dice que Meta-ExternalFetcher puede saltarse robots.txt porque hace consultas que pide el usuario, y que FacebookExternalHit puede saltárselo por comprobaciones de seguridad o de integridad, como las de malware.

## Las líneas de robots.txt

Para permitir Meta-ExternalAgent:

```
User-agent: meta-externalagent
Allow: /
```

Para bloquear Meta-ExternalAgent:

```
User-agent: meta-externalagent
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
meta-externalagent/1.1
```

## Cómo distinguir una petición real de una falsa

La página de Meta da las cadenas de user-agent (meta-externalagent/1.1 y la versión con un enlace) y no publica una lista de IP en el texto que leímos, así que no indicamos ningún número. Para FacebookExternalHit, Meta dice que se permitan en una lista blanca las cadenas de user-agent o las direcciones IP, y califica las direcciones como la opción más segura. Meta dice que los rastreadores pueden guardar robots.txt en caché hasta 24 horas, así que espera ese tiempo antes de valorar un cambio. Las preguntas van a webmasters@meta.com.

## Compara con GPTBot

[GPTBot](/es/bots/gptbot): El rastreador de entrenamiento de OpenAI, que respeta robots.txt sin los casos en que Meta puede saltarse robots.txt.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). Meta-ExternalAgent no es uno de ellos: lee tu robots.txt buscando un grupo `meta-externalagent` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿Meta-ExternalAgent respeta robots.txt?

Sí. Dale a meta-externalagent su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que Meta-ExternalAgent está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Meta for Developers: Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers)
