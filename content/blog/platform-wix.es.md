title: Wix: bloquea rastreadores de IA en Robots.txt Editor (4 nombres)
slug: wix
description: La ayuda de Wix dice que pegues cuatro agentes de usuario en el Robots.txt Editor. Dónde está el editor, qué omite el ejemplo y la opción nosnippet.
section: platforms
locale: es
cluster: Rastreadores de IA por plataforma
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Cuatro datos sobre Wix: Dónde Robots.txt Editor, Nombres de ejemplo 4, A nivel de página etiqueta nosnippet, Soporte No para ediciones
hero_sub: Ajustes de rastreadores de IA en Wix
hero_boxes: Dónde|Robots.txt Editor; Nombres de ejemplo|4; A nivel de página|Etiqueta nosnippet; Soporte|No para ediciones
widget: on
related: /es/platforms|Todas las plataformas comparadas; /es/platforms/webflow|Webflow; /es/bots|Rastreadores de IA comparados; /es/guides/cms|Lista de comprobación de visibilidad en IA para Shopify, WooCommerce y más
answer: Wix te deja editar robots.txt: SEO & GEO en el panel, luego Tools and settings y después Robots.txt Editor. Su página de ayuda pega cuatro nombres para bloquear: CCBot, GPTBot, ChatGPT-User y BingAI. ClaudeBot, PerplexityBot y Google-Extended no están en ese ejemplo, así que añádelos tú si quieres bloquearlos.

## Dónde está el ajuste en Wix

En el panel de tu sitio ve a SEO & GEO, baja hasta Tools and settings, haz clic en Robots.txt Editor y luego en View File. La guía de edición aparte de Wix lo llama una función avanzada y dice que Wix Customer Care no puede ayudar con los cambios que hagas en el archivo.

## El ejemplo bloquea cuatro nombres, y uno de ellos no está en la lista de Bing

La página de ayuda de Wix dice que su lista «incluye algunos rastreadores de IA conocidos, pero siempre puedes añadir más». Los cuatro que imprime son CCBot, GPTBot, ChatGPT-User y BingAI. Deja fuera los tokens de Anthropic, Perplexity, Google y Meta que aparecen en nuestras otras páginas. «BingAI» es el raro: la página de Microsoft sobre qué rastreadores usa Bing, leída el mismo día, enumera Bingbot, AdIdxBot, BingPreview, MicrosoftPreview y BingVideoPreview, y no BingAI. Una regla para un nombre que ningún rastreador usa no hace nada, así que toma la lista de Wix como punto de partida y contrástala con la página de cada proveedor. Ten en cuenta también que [ChatGPT-User](/es/bots/chatgpt-user) es el rastreador que abre una página cuando una persona se lo pide a ChatGPT, así que bloquearlo elimina esa vía de acceso a tus páginas.

En palabras del proveedor (original en inglés): “This list includes some known AI crawlers, but you can always add more as needed.”

Fuente: [Wix Help Center: Blocking AI Crawlers from Your Site](https://support.wix.com/en/article/blocking-ai-crawlers-from-your-site), leído el 21 de octubre de 2026.

## Los pasos

1. Ve a SEO & GEO en el panel de tu sitio.
2. Baja hasta Tools and settings y haz clic en Robots.txt Editor.
3. Haz clic en View File y luego en el campo que hay bajo Your robots.txt file.
4. Añade las directivas bajo This is your current file, y después Save Changes y Save.
5. Para una sola página, abre SEO basics de la página, Advanced SEO, Robots meta tag, y marca nosnippet. Wix dice que esto impide que el contenido se use como entrada directa para los resúmenes de IA.

## Las líneas que debes usar

Para permitir:

```
User-agent: OAI-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /
```

Para bloquear:

```
User-agent: CCBot
Disallow: /

User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /
```

## Cosas a tener en cuenta

Las preguntas frecuentes de Wix dicen que bloquear rastreadores de IA en robots.txt puede limitar la funcionalidad de NLWeb, porque los agentes de IA necesitan acceso a tu contenido estructurado. También dicen que algunos rastreadores ignoran robots.txt, así que un bloqueo no es hermético.

## Compara con Webflow

[Webflow](/es/platforms/webflow): también un editor de robots.txt, más una cabecera Content-Signal.

## Comprueba tu propio sitio

La comprobación gratuita del cuadro de arriba lee robots.txt para los rastreadores de IA y envía una petición real por rastreador, así que aparece cualquier regla que los ajustes de tu plataforma permiten pero que un cortafuegos rechaza. La lista completa de rastreadores está en [el centro de rastreadores de IA](/es/bots).

## FAQ

### ¿Bloquear rastreadores de IA perjudicará el SEO de mi sitio en Wix?

Wix dice que bloquear rastreadores de IA concretos no debería afectar de forma significativa al SEO, y recomienda revisar tus analíticas después.

### ¿BingAI es un rastreador real?

No está en la lista actual de rastreadores de Bing de Microsoft, que nombra Bingbot, AdIdxBot, BingPreview, MicrosoftPreview y BingVideoPreview. Consulta la [página de Bingbot](/es/bots/bingbot).

### ¿nosnippet bloquea los rastreadores de IA?

Wix lo describe como algo que impide que tu contenido se use como entrada directa para los resúmenes de IA. Es una etiqueta a nivel de página, no un bloqueo de rastreadores.

## Sources

- [Wix Help Center: Blocking AI Crawlers from Your Site](https://support.wix.com/en/article/blocking-ai-crawlers-from-your-site), leído el 21 de octubre de 2026
- [Wix Help Center: Editing Your Site's Robots.txt File](https://support.wix.com/en/article/editing-your-sites-robotstxt-file), leído el 21 de octubre de 2026
- [Microsoft Bing Webmaster help: Which Crawlers Does Bing Use?](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0), leído el 21 de octubre de 2026
