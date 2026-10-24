title: Google-CloudVertexBot : rôle et effet d'un blocage
h1: Google-CloudVertexBot : rôle et effet d'un blocage
description: Google-CloudVertexBot (Google) : plusieurs rôles. Jeton robots.txt, effet d'un Disallow et vérification d'une requête, lus sur la page de l'opérateur.
slug: google-cloudvertexbot
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur Google-CloudVertexBot : opérateur Google, rôle Plusieurs rôles, respecte robots.txt Oui, liste d'adresses 317 plages
hero_sub: Google-CloudVertexBot, géré par Google
hero_boxes: Opérateur|Google; Rôle|Plusieurs rôles; Respecte robots.txt|Oui; Liste d'adresses|317 plages
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/googlebot|Googlebot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: Google-CloudVertexBot est un robot d’exploration de Google qui effectue des explorations demandées par les propriétaires de sites pour construire des Vertex AI Agents. Google le range parmi ses robots d’exploration courants, qui respectent toujours robots.txt lors d’une exploration automatique. Google indique que les règles qui lui sont adressées n’ont aucun effet sur Google Search ni sur les autres produits Google.

## Ce qu'est Google-CloudVertexBot

Google-CloudVertexBot est un robot d’exploration de Google listé parmi ses robots d’exploration courants. Google indique qu’il effectue des explorations demandées par les propriétaires de sites pour construire des Vertex AI Agents. Google le présente comme une sous-chaîne de user agent, pas comme une chaîne de user agent complète.

| Fait | Google-CloudVertexBot |
| --- | --- |
| Opérateur | Google |
| Rôle | Exploration demandée par les propriétaires de sites pour Vertex AI Agents |
| Jeton robots.txt | `Google-CloudVertexBot` |
| Respecte robots.txt | Oui. Google indique que les robots d’exploration courants respectent toujours les règles robots.txt lors d’une exploration automatique. |
| Adresses IP | 317 plages (developers.google.com/static/crawling/ipranges/common-crawlers.json, fichier daté du 2026-10-23) |
| Page de l'opérateur lue le | 24 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “Crawling preferences addressed to the Google-CloudVertexBot user agent affect crawls requested by the site owners' for building Vertex AI Agents”

Source : [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers), lu le 24 octobre 2026.

## Que se passe-t-il si vous bloquez Google-CloudVertexBot

Google indique que les préférences adressées au user agent Google-CloudVertexBot concernent les explorations demandées par les propriétaires de sites pour construire des Vertex AI Agents. Elle précise que cela n’a aucun effet sur Google Search ni sur les autres produits.

## Les lignes robots.txt

Pour autoriser Google-CloudVertexBot :

```
User-agent: Google-CloudVertexBot
Allow: /
```

Pour bloquer Google-CloudVertexBot :

```
User-agent: Google-CloudVertexBot
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
Google-CloudVertexBot
```

## Comment distinguer une vraie requête d'une fausse

Le fichier developers.google.com/static/crawling/ipranges/common-crawlers.json contenait 317 plages le 24 octobre 2026, fichier daté du 2026-10-23.

Google indique que les robots d’exploration courants explorent généralement depuis les plages de common-crawlers.json, et que le nom DNS inverse correspond à crawl-***-***-***-***.googlebot.com ou geo-crawl-***-***-***-***.geo.googlebot.com.

## À comparer avec Googlebot

[Googlebot](/fr/bots/googlebot) : Googlebot explore pour Google Search, tandis que Google-CloudVertexBot n’explore que lorsqu’un propriétaire de site a demandé une exploration pour construire des Vertex AI Agents.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). Google-CloudVertexBot n'en fait pas partie : lisez votre robots.txt pour un groupe `Google-CloudVertexBot` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Google-CloudVertexBot respecte-t-il robots.txt ?

Oui. Google indique que les robots d’exploration courants respectent toujours les règles robots.txt lors d’une exploration automatique. Donnez à Google-CloudVertexBot son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si Google-CloudVertexBot est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers)
- [Google: common-crawlers.json (read 2026-10-24, creationTime 2026-10-23)](https://developers.google.com/static/crawling/ipranges/common-crawlers.json)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
