title: ¿Está bloqueado GPTBot en tu web? 4 formas de comprobarlo
h1: ¿Está bloqueado GPTBot en mi web? Cuatro sitios donde mirar y una prueba para cada uno
description: A GPTBot lo puede frenar robots.txt, tu CDN, un cortafuegos o tu servidor. Cómo saber cuál en minutos y qué cambia (y qué no) al bloquearlo.
slug: is-gptbot-blocked
locale: es
cluster: Rastreo
date: 2026-10-20
reviewed: 2026-10-20
hero: auto
hero_alt: Cuatro cuadros numerados del 1 al 4: robots.txt, CDN, cortafuegos y servidor, los sitios donde se puede frenar a GPTBot
hero_sub: Cuatro capas, una prueba para cada una
hero_boxes: robots.txt|El archivo público; CDN|Por ejemplo Cloudflare; Cortafuegos|Plugins y reglas WAF; Servidor|Reglas y registros
widget: on
howto: on
steps_img: on
related: /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web?; /es/ai-visibility-audit|Auditoría de visibilidad en IA; /es/guides/technical-seo-checklist|Lista de comprobación técnica
answer: GPTBot está bloqueado en tu web si robots.txt tiene una regla Disallow que le afecta, o si una regla de tu CDN, cortafuegos o servidor rechaza sus peticiones. Abre tutienda.es/robots.txt, lanza una auditoría y compara dos peticiones a tu servidor. Bloquear GPTBot no bloquea por sí solo la búsqueda de ChatGPT.

## ¿En qué cuatro sitios puede frenarse a GPTBot?

GPTBot es el rastreador que, según OpenAI, usa para recopilar contenido que puede servir para entrenar sus modelos. Una petición suya puede rechazarse en cuatro capas, y cada una necesita su propia prueba: el archivo `robots.txt`, tu CDN, un plugin de seguridad o regla de cortafuegos (WAF) y una regla del servidor web.

La auditoría de CitedBy, desde 9 €, cubre la primera. Las otras tres pueden devolver un código de error aunque robots.txt diga que sí.

## ¿Cómo comprobarlo, paso a paso?

1. Revisa el archivo de robots: abre `tutienda.es/robots.txt` en el navegador y busca un grupo que nombre `GPTBot`. Si no hay ninguno, GPTBot sigue el grupo `User-agent: *`, así que un `Disallow: /` general también le afecta ([RFC 9309](https://www.rfc-editor.org/rfc/rfc9309)).
2. Lanza una auditoría: la de CitedBy lee robots.txt para GPTBot, OAI-SearchBot, PerplexityBot, Google-Extended y Bingbot y te dice cuáles están bloqueados.
3. Compara dos peticiones: envía dos peticiones a tu página de inicio, una normal y otra con el agente de usuario de GPTBot, y compara los códigos de estado. Los comandos están abajo.
4. Mira tu CDN y tu cortafuegos: entra en el panel de tu CDN y busca los ajustes de rastreadores de IA; en el plugin de seguridad o en la lista de reglas, busca `GPTBot`, `bot`, `AI` y `crawler`.
5. Busca en los registros: filtra los logs de tu servidor por `GPTBot`. Una serie de respuestas 403 es la señal de un bloqueo que robots.txt no muestra.

## ¿Cómo funciona la prueba de las dos peticiones?

Sustituye `tutienda.es` por tu dirección. El primer comando envía una petición normal; el segundo, el agente de usuario de GPTBot que publica OpenAI. Cada uno imprime solo el código de estado.

```
curl -s -o /dev/null -w "%{http_code}\n" https://tutienda.es/
curl -s -o /dev/null -w "%{http_code}\n" -A "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.4; +https://openai.com/gptbot" https://tutienda.es/
```

Un 403 solo en la segunda petición indica que una regla apunta al nombre del rastreador.

Hay un límite. La prueba sale de tu ordenador. Si tu hosting también juzga a los rastreadores por su dirección IP, el GPTBot real puede recibir otra respuesta distinta a la que has visto. OpenAI publica los rangos de IP de GPTBot en `openai.com/gptbot.json`, así que tus registros pueden mostrar si las peticiones desde esos rangos pasaron ([documentación de OpenAI](https://developers.openai.com/api/docs/bots)).

## ¿Dónde se ajusta en Cloudflare?

La documentación de Cloudflare indica los pasos: entra en tu dominio, abre AI Crawl Control y ve a la pestaña Security. La pestaña Crawlers muestra los rastreadores de IA que piden tu contenido. En la columna Actions eliges Allow o Block para cada uno, y con Allow puedes seguir aplicando robots.txt ([Cloudflare: gestionar rastreadores de IA](https://developers.cloudflare.com/ai-crawl-control/features/manage-ai-crawlers/)).

Los valores por defecto también cambian. Help Net Security informa de que, desde el 15 de septiembre de 2026, los dominios nuevos bloquean por defecto los rastreadores de entrenamiento y de agentes en las páginas que muestran anuncios, y los de búsqueda siguen permitidos ([Help Net Security](https://www.helpnetsecurity.com/2026/07/02/cloudflare-ai-crawler-controls/)). Mira tu propio panel en lugar de dar por hecho qué valor recibió tu dominio.

## ¿Qué hacer si la web rechaza la petición?

Una petición normal de nuestra comprobación también puede ser rechazada. Si la respuesta es HTTP 403, 429 o 503, la comprobación lo indica y avisa de que desde fuera no puede saber si también se rechaza a los rastreadores de IA. Un 403 suele significar que una regla bloqueó la petición. Un 429 o un 503 pueden indicar también límite de peticiones o una caída, que afecta a todos los visitantes. Corrige la causa en el CDN, el cortafuegos o el panel del hosting y vuelve a comprobar.

## ¿Debes desbloquear GPTBot?

Es decisión tuya, y bloquearlo es una opción legítima. OpenAI lista GPTBot, OAI-SearchBot y ChatGPT-User como rastreadores distintos con funciones distintas. GPTBot es para datos de entrenamiento. OAI-SearchBot muestra webs en las funciones de búsqueda de ChatGPT. ChatGPT-User visita páginas cuando una persona pregunta por ellas.

| Tu objetivo | Qué hacer |
| --- | --- |
| Salir en la búsqueda de ChatGPT sin que se entrene con tu contenido | Permite `OAI-SearchBot` y bloquea `GPTBot` |
| Salir en la búsqueda de ChatGPT y permitir el entrenamiento | Permite ambos |
| Quedarte fuera de los dos | Bloquea ambos y revisa tus registros por ChatGPT-User |

Según OpenAI, un cambio en robots.txt puede tardar unas 24 horas en llegar a OAI-SearchBot.

## FAQ

### ¿Bloquear GPTBot saca mi tienda online de ChatGPT?
No por sí solo. OpenAI describe OAI-SearchBot como el rastreador de las funciones de búsqueda de ChatGPT y GPTBot como el de entrenamiento, cada uno configurado por separado en robots.txt.

### ¿Por qué robots.txt parece correcto pero GPTBot recibe un 403?
robots.txt es una petición al rastreador. Un CDN, un cortafuegos o una regla del servidor pueden rechazar la petición igualmente, así que revisa esas capas con la prueba de las dos peticiones y con tus registros.

### ¿Respeta ChatGPT-User el archivo robots.txt?
OpenAI indica que las reglas de robots.txt pueden no aplicarse a ChatGPT-User, porque las peticiones las inicia una persona.

### ¿Me recomendará ChatGPT si desbloqueo GPTBot?
No. Que te puedan leer es la entrada, no el resultado. Que un asistente nombre tu tienda depende de lo que encuentre sobre tu categoría, y eso lo mide la auditoría de CitedBy con preguntas reales de compradores.

## Sources

- [OpenAI: rastreadores y agentes de usuario, rangos de IP](https://developers.openai.com/api/docs/bots)
- [Cloudflare: gestionar rastreadores de IA](https://developers.cloudflare.com/ai-crawl-control/features/manage-ai-crawlers/)
- [Help Net Security: Cloudflare cambia las reglas de acceso de rastreadores de IA, 2 de julio de 2026](https://www.helpnetsecurity.com/2026/07/02/cloudflare-ai-crawler-controls/)
- [IETF RFC 9309: protocolo de exclusión de robots](https://www.rfc-editor.org/rfc/rfc9309)
