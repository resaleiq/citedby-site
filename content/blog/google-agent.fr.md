title: Google-Agent : ce qu'il fait et ce que change son blocage
h1: Google-Agent : ce qu'il fait et ce que change son blocage
description: Google-Agent (Google) : récupération déclenchée par l'utilisateur. Jeton robots.txt, effet d'un Disallow et vérification d'une requête.
slug: google-agent
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur Google-Agent : opérateur Google, rôle Récupération déclenchée par l'utilisateur, respecte robots.txt Pas toujours, liste d'adresses 20 plages
hero_sub: Google-Agent, géré par Google
hero_boxes: Opérateur|Google; Rôle|Récupération déclenchée par l'utilisateur; Respecte robots.txt|Pas toujours; Liste d'adresses|20 plages
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/chatgpt-user|ChatGPT-User; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: Google-Agent est un agent de récupération déclenchée par l’utilisateur que, selon Google, des agents hébergés sur l’infrastructure de Google utilisent pour naviguer sur le web et agir à la demande d’un utilisateur. Google indique que ces agents ignorent généralement robots.txt, car l’utilisateur a demandé la récupération. Google publie ses plages d’IP dans user-triggered-agents.json.

## Ce qu'est Google-Agent

Google-Agent est un agent de récupération déclenchée par l’utilisateur que, selon Google, des agents hébergés sur l’infrastructure de Google utilisent pour naviguer sur le web et effectuer des actions à la demande de l’utilisateur. Google liste des chaînes de user agent distinctes pour mobile et ordinateur. Google indique aussi qu’elle expérimente le protocole Web Bot Auth avec l’identité https://agent.bot.goog.

| Fait | Google-Agent |
| --- | --- |
| Opérateur | Google |
| Rôle | Récupération déclenchée par l’utilisateur (agents agissant pour un utilisateur) |
| Jeton robots.txt | `Google-Agent` |
| Respecte robots.txt | Partiel. Google indique que les agents de récupération déclenchée par l’utilisateur ignorent généralement les règles robots.txt, car un utilisateur a demandé la récupération. |
| Adresses IP | 20 plages (developers.google.com/static/crawling/ipranges/user-triggered-agents.json, fichier daté du 2026-10-23) |
| Page de l'opérateur lue le | 24 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “Google-Agent is used by agents hosted on Google infrastructure to navigate the web and perform actions upon user request.”

Source : [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers), lu le 24 octobre 2026.

## Que se passe-t-il si vous bloquez Google-Agent

Google indique que, la récupération ayant été demandée par un utilisateur, les agents de récupération déclenchée par l’utilisateur ignorent généralement les règles robots.txt. La page de Google ne documente aucun jeton robots.txt pour Google-Agent.

## Les lignes robots.txt

Pour autoriser Google-Agent :

```
User-agent: Google-Agent
Allow: /
```

Pour bloquer Google-Agent :

```
User-agent: Google-Agent
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko; compatible; Google-Agent; +https://developers.google.com/crawling/docs/crawlers-fetchers/google-agent) Chrome/W.X.Y.Z Safari/537.36
```

## Comment distinguer une vraie requête d'une fausse

Le fichier developers.google.com/static/crawling/ipranges/user-triggered-agents.json contenait 20 plages le 24 octobre 2026, fichier daté du 2026-10-23.

Google indique que Google-Agent utilise les plages d’IP de user-triggered-agents.json, et que le masque DNS inverse des agents de récupération déclenchée par l’utilisateur correspond à ***-***-***-***.gae.googleusercontent.com ou google-proxy-***-***-***-***.google.com selon que l’agent appartient à Google ou à l’utilisateur.

## À comparer avec ChatGPT-User

[ChatGPT-User](/fr/bots/chatgpt-user) : Les deux agissent à la demande d’un utilisateur plutôt que d’explorer d’eux-mêmes, et Google-Agent est décrit comme naviguant sur le web et effectuant des actions pour l’utilisateur.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). Google-Agent n'en fait pas partie : lisez votre robots.txt pour un groupe `Google-Agent` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Google-Agent respecte-t-il robots.txt ?

Pas toujours. Google indique que les agents de récupération déclenchée par l’utilisateur ignorent généralement les règles robots.txt, car un utilisateur a demandé la récupération. Une règle pour Google-Agent dans robots.txt peut donc ne pas l'arrêter. Pour le refuser à coup sûr, utilisez une règle de pare-feu ou de CDN qui combine le user agent et les adresses publiées.

### Comment savoir si Google-Agent est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers)
- [Google: user-triggered-agents.json (read 2026-10-24, creationTime 2026-10-23)](https://developers.google.com/static/crawling/ipranges/user-triggered-agents.json)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
