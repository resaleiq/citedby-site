title: Applebot-Extended: qué hace y qué cambia si lo bloqueas
h1: Applebot-Extended: qué hace y qué cambia si lo bloqueas
description: Applebot-Extended (Apple): token de control. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición, leído en la página del operador.
slug: applebot-extended
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Cuatro datos sobre Applebot-Extended: operador Apple, función Token de control, respeta robots.txt Solo se lee en robots.txt, lista de direcciones Ninguna
hero_sub: Applebot-Extended, de Apple
hero_boxes: Operador|Apple; Función|Token de control; Respeta robots.txt|Solo se lee en robots.txt; Lista de direcciones|Ninguna
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/applebot|Applebot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: Applebot-Extended es un token de robots.txt. Apple dice que los editores pueden excluir su contenido del entrenamiento de modelos fundacionales generativos si lo bloquean con Disallow. Applebot aún puede rastrear la página, así que el contenido sigue apareciendo en Spotlight, Siri y Safari. No hace ninguna solicitud por su cuenta.

## Qué es Applebot-Extended

La página de Apple describe Applebot-Extended como la forma de mantener el contenido fuera del entrenamiento de los modelos fundacionales que hay detrás de Apple Intelligence, los servicios y las herramientas para desarrolladores. Igual que [Google-Extended](/es/bots/google-extended), es un token de control: no lo encontrarás en un registro.

| Dato | Applebot-Extended |
| --- | --- |
| Operador | Apple |
| Función | Token de control (sin solicitudes propias) |
| Token de robots.txt | `Applebot-Extended` |
| Respeta robots.txt | Solo se lee en robots.txt |
| Direcciones IP | Ninguna: nunca descarga páginas |
| Página del proveedor leída el | 21 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “Web publishers can opt-out from having their content used to train generative foundation models by disallowing Applebot-Extended in the robots.txt file.”

Fuente: [Apple Support: About Applebot](https://support.apple.com/en-us/119829), leído el 21 de octubre de 2026.

## Qué pasa si bloqueas Applebot-Extended

Apple explica el límite: si bloqueas Applebot-Extended y además marcas el contenido con la metaetiqueta nosnippet, tus instrucciones aún pueden permitir que Applebot rastree la página, y el contenido sigue apareciendo en Spotlight, Siri y Safari. La misma página dice que los editores pueden excluirse del uso en respuestas de conocimiento general aplicando este control de robots.txt.

## Las líneas de robots.txt

Para permitir Applebot-Extended:

```
User-agent: Applebot-Extended
Allow: /
```

Para bloquear Applebot-Extended:

```
User-agent: Applebot-Extended
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

## Cómo distinguir una petición real de una falsa

No existe una comprobación de red para un token que no envía solicitudes. Lee robots.txt, en cada host, y revisa Applebot por separado, porque los dos tokens son independientes y un único grupo `User-agent: Applebot-Extended` no dice nada sobre Applebot.

Applebot-Extended no envía peticiones por sí mismo, así que nunca aparece en el registro de tu servidor. Solo se lee en robots.txt.

## Compara con Applebot

[Applebot](/es/bots/applebot): El propio rastreador: si lo permites, sigues en la búsqueda de Spotlight, Siri y Safari.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). Applebot-Extended no es uno de ellos: lee tu robots.txt buscando un grupo `Applebot-Extended` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿Applebot-Extended respeta robots.txt?

Solo se lee en robots.txt. No envía peticiones por sí mismo, así que no hay nada que bloquear en el cortafuegos: la regla de robots.txt es todo el control.

### ¿Cómo sé que Applebot-Extended está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Apple Support: About Applebot](https://support.apple.com/en-us/119829)
