title: Squarespace: la casilla de IA bloquea 26 bots, pero no ChatGPT
slug: squarespace
description: La casilla de rastreadores de IA de Squarespace escribe 26 nombres en robots.txt y deja fuera los bots de búsqueda y de usuario de ChatGPT.
section: platforms
locale: es
cluster: Rastreadores de IA por plataforma
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Cuatro datos sobre Squarespace: Dónde Settings, Crawlers, Nombres bloqueados 26, Editar robots.txt No, Entrenamiento pasado No se elimina
hero_sub: Ajustes de rastreadores de IA en Squarespace
hero_boxes: Dónde|Settings, Crawlers; Nombres bloqueados|26; Editar robots.txt|No; Entrenamiento pasado|No se elimina
widget: on
related: /es/platforms|Todas las plataformas comparadas; /es/platforms/wix|Wix; /es/bots|Rastreadores de IA comparados; /es/guides/cms|Lista de comprobación de visibilidad en IA para Shopify, WooCommerce y más
answer: Squarespace tiene una sola casilla: Settings, luego Crawlers y luego Block known artificial intelligence crawlers. Añade 26 bots con nombre a tu robots.txt. La lista incluye GPTBot, ClaudeBot y DuckAssistBot, pero no OAI-SearchBot, ChatGPT-User ni PerplexityBot, y no puedes editar robots.txt tú mismo.

## Dónde está el ajuste en Squarespace

Abre el panel Settings, haz clic en Crawlers y marca Block known artificial intelligence crawlers. La página de Squarespace dice que al marcar la casilla se actualiza tu archivo robots.txt para los bots que se enumeran más abajo, y que puede añadir más con el tiempo.

## Los 26 nombres, y cuáles faltan

La página de ayuda de Squarespace enumera exactamente 26 nombres: AI2Bot, Ai2Bot-Dolma, aiHitBot, Amazonbot, anthropic-ai, Applebot-Extended, Bytespider, CCBot, ClaudeBot, cohere-ai, cohere-training-data-crawler, DuckAssistBot, FacebookBot, Google-Extended, GoogleOther, GoogleOther-Image, GoogleOther-Video, GPTBot, img2dataset, Meta-ExternalAgent, MyCentralAIScraperBot, omgili, omgilibot, Quora-Bot, TikTokSpider y YouBot. Si lo comparamos con nuestras propias páginas de rastreadores, la casilla cubre los rastreadores de entrenamiento y de conjuntos de datos de OpenAI, Anthropic, Google, Apple, Meta y Common Crawl. No nombra a [OAI-SearchBot](/es/bots/oai-searchbot), [ChatGPT-User](/es/bots/chatgpt-user), [PerplexityBot](/es/bots/perplexitybot), [Claude-SearchBot](/es/bots/claude-searchbot) ni [Claude-User](/es/bots/claude-user), así que marcarla no te saca de la búsqueda de ChatGPT. Sí nombra a [DuckAssistBot](/es/bots/duckassistbot) y [Amazonbot](/es/bots/amazonbot), que son rastreadores de respuestas y de productos, así que marcarla también puede costarte las respuestas de IA de DuckDuckGo.

En palabras del proveedor (original en inglés): “Checking the box updates your robots.txt file to tell the following bots not to crawl your site.”

Fuente: [Squarespace Help: Request that AI models exclude your site](https://support.squarespace.com/hc/en-us/articles/360022347072-Request-that-AI-models-exclude-your-site), leído el 21 de octubre de 2026.

## Los pasos

1. Abre el panel Settings de tu sitio de Squarespace.
2. Haz clic en Crawlers.
3. Marca Block known artificial intelligence crawlers para bloquear los 26 nombres, o déjala sin marcar para dejarlos todos permitidos.
4. Para pedir que se añada otro bot, contacta con Squarespace: el propio texto de su página dice que puedes solicitarlo.

## Las líneas que debes usar

Para permitir:

```
# Squarespace sites are open to these crawlers while the box is unticked.
# You cannot add lines yourself, so there is nothing to paste.
```

Para bloquear:

```
# Written by Squarespace when the box is ticked (excerpt):
User-agent: GPTBot
User-agent: ClaudeBot
User-agent: CCBot
Disallow: /
```

## Cosas a tener en cuenta

Squarespace afirma que marcar la casilla no elimina con efecto retroactivo de los datos de entrenamiento de los modelos de IA el contenido que ya se haya extraído de tu sitio. También dice que robots.txt es solo una petición que los rastreadores amistosos se han ofrecido a respetar. El fragmento de arriba es una ilustración abreviada nuestra del tipo de líneas que genera la casilla; el archivo exacto es el que tu sitio sirva en /robots.txt, así que ábrelo y léelo.

## Compara con Wix

[Wix](/es/platforms/wix): un editor de robots.txt de verdad y una lista de ejemplo con cuatro nombres.

## Comprueba tu propio sitio

La comprobación gratuita del cuadro de arriba lee robots.txt para los rastreadores de IA y envía una petición real por rastreador, así que aparece cualquier regla que los ajustes de tu plataforma permiten pero que un cortafuegos rechaza. La lista completa de rastreadores está en [el centro de rastreadores de IA](/es/bots).

## FAQ

### ¿Puedo permitir la búsqueda de ChatGPT pero bloquear el entrenamiento en Squarespace?

En parte. Al marcar la casilla se escribe una regla para GPTBot, y OAI-SearchBot no está entre los 26 nombres. No puedes añadir líneas propias, así que abre tu /robots.txt activo para confirmar qué dice.

### ¿Puedo editar robots.txt en Squarespace?

La propia página de Squarespace trata el panel Crawlers como el control y no ofrece un editor de robots.txt. Wix y Webflow sí lo ofrecen.

### ¿La casilla impide que Google indexe mi sitio?

No. Es independiente de la opción de rastreadores de motores de búsqueda del mismo panel. La casilla de IA nombra Google-Extended y GoogleOther, no Googlebot.

## Sources

- [Squarespace Help: Request that AI models exclude your site](https://support.squarespace.com/hc/en-us/articles/360022347072-Request-that-AI-models-exclude-your-site), leído el 21 de octubre de 2026
