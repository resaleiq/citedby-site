title: Perplexity-User: qué hace y qué cambia si lo bloqueas
h1: Perplexity-User: qué hace y qué cambia si lo bloqueas
description: Perplexity-User (Perplexity): consulta iniciada por el usuario. Token de robots.txt, qué cambia un Disallow y cómo verificar una petición.
slug: perplexity-user
section: bots
locale: es
cluster: Rastreadores de IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Cuatro datos sobre Perplexity-User: operador Perplexity, función Consulta iniciada por el usuario, respeta robots.txt No siempre, lista de direcciones 4 rangos
hero_sub: Perplexity-User, de Perplexity
hero_boxes: Operador|Perplexity; Función|Consulta iniciada por el usuario; Respeta robots.txt|No siempre; Lista de direcciones|4 rangos
widget: on
related: /es/bots|Todos los rastreadores de IA comparados; /es/bots/perplexitybot|PerplexityBot; /es/platforms|Ajustes de rastreadores de IA por plataforma; /es/blog/can-chatgpt-read-my-website|¿Puede ChatGPT leer mi web? Qué lo decide
answer: Perplexity-User es el agente de Perplexity para acciones del usuario: cuando un usuario hace una pregunta, puede visitar una página para responder con precisión y enlazarla. Perplexity dice que no se usa para rastrear la web ni para entrenar modelos de IA, y que por lo general ignora las reglas de robots.txt porque la consulta la pidió un usuario.

## Qué es Perplexity-User

Perplexity-User es el agente de Perplexity para acciones del usuario. Cuando un usuario le hace una pregunta a Perplexity, puede visitar una página web para ayudar a dar una respuesta precisa e incluir un enlace a la página en su respuesta. Perplexity dice que no se usa para rastrear la web ni para recoger contenido con el que entrenar modelos fundacionales de IA, y que es independiente de PerplexityBot, que muestra y enlaza sitios web en los resultados de búsqueda de Perplexity.

| Dato | Perplexity-User |
| --- | --- |
| Operador | Perplexity |
| Función | Consulta iniciada por el usuario |
| Token de robots.txt | `Perplexity-User` |
| Respeta robots.txt | Por lo general ignora las reglas de robots.txt, porque la consulta la pidió un usuario |
| Direcciones IP | 4 rangos (www.perplexity.com/perplexity-user.json, archivo del 2025-10-17) |
| Página del proveedor leída el | 24 de octubre de 2026 |

## Qué dice el proveedor

En palabras del proveedor (original en inglés): “Since a user requested the fetch, this fetcher generally ignores robots.txt rules.”

Fuente: [Perplexity: Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers), leído el 24 de octubre de 2026.

## Qué pasa si bloqueas Perplexity-User

Perplexity incluye Perplexity-User como token de robots.txt y dice que controla a qué sitios pueden acceder estas solicitudes de usuario. Perplexity dice también que este agente por lo general ignora las reglas de robots.txt porque la consulta la pidió un usuario. Perplexity dice que cada uno de sus ajustes de robots.txt funciona de forma independiente y que los cambios pueden tardar hasta 24 horas en surtir efecto.

## Las líneas de robots.txt

Para permitir Perplexity-User:

```
User-agent: Perplexity-User
Allow: /
```

Para bloquear Perplexity-User:

```
User-agent: Perplexity-User
Disallow: /
```

Pega un bloque en el robots.txt de la raíz de tu host, por ejemplo https://example.com/robots.txt. Un grupo para un token no cubre los demás rastreadores del mismo operador.

La cadena user-agent que muestra el proveedor:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Perplexity-User/1.0; +https://perplexity.ai/perplexity-user)
```

## Cómo distinguir una petición real de una falsa

El archivo www.perplexity.com/perplexity-user.json tenía 4 rangos el 24 de octubre de 2026, archivo del 2025-10-17.

Perplexity publica las direcciones IP de Perplexity-User como un archivo JSON y dice que se use como fuente de verdad para las reglas de permiso, combinado con la cadena de user-agent.

## Compara con PerplexityBot

[PerplexityBot](/es/bots/perplexitybot): PerplexityBot muestra y enlaza sitios en los resultados de búsqueda de Perplexity, mientras que Perplexity-User obtiene una página cuando la pregunta de un usuario lo necesita y por lo general ignora robots.txt.

## Tu propio sitio

La comprobación gratuita del recuadro de arriba prueba ocho rastreadores (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot y Googlebot). Perplexity-User no es uno de ellos: lee tu robots.txt buscando un grupo `Perplexity-User` y busca el user agent en el registro de tu servidor. La lista completa de rastreadores está en [el directorio de rastreadores de IA](/es/bots).

## FAQ

### ¿Perplexity-User respeta robots.txt?

No siempre. Por lo general ignora las reglas de robots.txt, porque la consulta la pidió un usuario. Por eso una regla para Perplexity-User en robots.txt puede no detenerlo. Para rechazarlo con seguridad, usa una regla de cortafuegos o de CDN que combine el user agent y las direcciones publicadas.

### ¿Cómo sé que Perplexity-User está realmente bloqueado?

robots.txt es solo una capa: una regla de CDN o de cortafuegos también puede rechazar a un rastreador, y un rastreador puede ignorar el archivo. Busca el user agent en el registro de tu servidor y prueba la dirección desde fuera de tu red.

## Sources

- [Perplexity: Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers)
- [Perplexity: Perplexity-User IP addresses JSON (read 2026-10-24)](https://www.perplexity.com/perplexity-user.json)
