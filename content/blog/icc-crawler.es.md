title: ICC-Crawler: qué hace y qué cambia si lo bloqueas
h1: ICC-Crawler: qué hace y qué cambia si lo bloqueas
description: ICC-Crawler (NICT (Universal Communication Research Institute)): entrenamiento. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición.
slug: icc-crawler
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre ICC-Crawler: operador NICT (Universal Communication Research Institute), función Entrenamiento, respeta robots.txt Sí, lista de direcciones Lista en su página
hero_sub: ICC-Crawler, de NICT (Universal Communication Research Institute)
hero_boxes: Operador|NICT (Universal Communication Research Institute); Función|Entrenamiento; Respeta robots.txt|Sí; Lista de direcciones|Lista en su página
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/gptbot|GPTBot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: ICC-Crawler lo gestiona el Universal Communication Research Institute del NICT de Japón. El NICT dice que usa las páginas recogidas para investigar el procesamiento de la información, incluidas la traducción multilingüe, el análisis de información y la inteligencia artificial. Admite el Protocolo de exclusión de robots: User-agent: ICC-Crawler con Disallow: / podría desactivar la recogida en todas las páginas.

## Qué es ICC-Crawler

ICC-Crawler es un rastreador que gestiona el Universal Communication Research Institute del National Institute of Information and Communications Technology (NICT) de Japón. El NICT dice que usa las páginas recogidas para la investigación y el desarrollo de tecnologías de procesamiento de la información, incluidas la traducción multilingüe, el análisis de información y la inteligencia artificial. El NICT también puede facilitar a terceros la información recogida o los productos de la investigación, en la medida en que lo permita la ley.

| Dato | ICC-Crawler |
| --- | --- |
| Operador | NICT (Universal Communication Research Institute) |
| Función | Recogida de datos para investigación (incluye investigación y desarrollo de IA) |
| Token de robots.txt | `ICC-Crawler` |
| Respeta robots.txt | Sí, y con un Crawl-Delay usa el mayor entre ese intervalo y su propio mínimo |
| Direcciones IP | Lista en la página del proveedor (ucri.nict.go.jp/en/icccrawler.html) |
| Página del proveedor leída el | 24 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “NICT uses the information it collects for research and development of advanced information processing technologies including multilingual translation, information analysis, and artificial intelligence technologies.”

Fuente: [NICT Universal Communication Research Institute: ICC-Crawler](https://ucri.nict.go.jp/en/icccrawler.html), leído el 24 de octubre de 2026.

## Qué pasa si bloqueas ICC-Crawler

El NICT dice que ICC-Crawler admite el Protocolo de exclusión de robots y que añadir User-agent: ICC-Crawler con Disallow: / a robots.txt podría desactivar la recogida en todas las páginas. También permite a los propietarios de sitios bloquear una ruta o un tipo de archivo, o permitir rutas concretas bajo un Disallow total. Si el acceso continúa después de eso, el NICT pide a los propietarios de sitios que se pongan en contacto con él para que pueda dejar de recoger contenido del host.

## Las líneas de robots.txt

Para permitir ICC-Crawler:

```
User-agent: ICC-Crawler
Allow: /
```

Para bloquear ICC-Crawler:

```
User-agent: ICC-Crawler
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La página del proveedor no muestra una cadena user-agent completa para ICC-Crawler.

## Cómo distinguir una petición real de una falsa

La página del proveedor enumera las direcciones IP del rastreador en texto plano; no publica una lista legible por máquina.

## Compara con GPTBot

[GPTBot](/es/bots/gptbot): Ambos recogen páginas que alimentan el desarrollo de IA, pero ICC-Crawler lo gestiona un instituto público de investigación japonés para su propia investigación y publica dos direcciones IP del rastreador en su página, mientras que GPTBot lo gestiona una empresa comercial.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). ICC-Crawler no es uno de ellos: lee tu robots.txt buscando un grupo `ICC-Crawler` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿ICC-Crawler respeta robots.txt?

Sí, y con un Crawl-Delay usa el mayor entre ese intervalo y su propio mínimo. Dale a ICC-Crawler su propio grupo User-agent en robots.txt: los demás rastreadores del mismo operador tienen cada uno su ajuste.

### ¿Cómo sé que ICC-Crawler está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [NICT Universal Communication Research Institute: ICC-Crawler](https://ucri.nict.go.jp/en/icccrawler.html)
