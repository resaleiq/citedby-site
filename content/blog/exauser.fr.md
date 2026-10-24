title: ExaUser : ce qu'il fait et ce que change son blocage
h1: ExaUser : ce qu'il fait et ce que change son blocage
description: ExaUser (Exa) : récupération déclenchée par l'utilisateur. Jeton robots.txt, effet d'un Disallow et vérification d'une requête.
slug: exauser
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur ExaUser : opérateur Exa, rôle Récupération déclenchée par l'utilisateur, respecte robots.txt Pas toujours, liste d'adresses Outil de vérification
hero_sub: ExaUser, géré par Exa
hero_boxes: Opérateur|Exa; Rôle|Récupération déclenchée par l'utilisateur; Respecte robots.txt|Pas toujours; Liste d'adresses|Outil de vérification
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/exasearchbot|ExaSearchBot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: ExaUser est l’agent qu’Exa utilise pour récupérer une page en direct lorsqu’un utilisateur, ou une application construite sur l’API Exa, demande son contenu actuel. Exa indique que les règles robots.txt peuvent ne pas s’appliquer à ces récupérations lancées par l’utilisateur. Les refus de recherche et l’exploration automatique se contrôlent plutôt avec le jeton ExaSearchBot.

## Ce qu'est ExaUser

ExaUser est l’agent qu’Exa utilise pour récupérer une page en direct lorsqu’un utilisateur, ou une application construite sur l’API Exa, demande son contenu actuel. Exa indique qu’il n’est pas utilisé pour explorer le web automatiquement ; c’est le rôle d’ExaSearchBot. Il ne cherche pas à contourner les connexions, les paywalls ni les CAPTCHA, et ne soumet aucun formulaire.

| Fait | ExaUser |
| --- | --- |
| Opérateur | Exa |
| Rôle | Récupération déclenchée par l’utilisateur |
| Jeton robots.txt | `ExaUser` |
| Respecte robots.txt | Partiel, l’opérateur indique que les règles robots.txt peuvent ne pas s’appliquer aux récupérations lancées par l’utilisateur |
| Adresses IP | Outil de vérification |
| Page de l'opérateur lue le | 24 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “Exa uses ExaUser to fetch a page live when a user, or an application built on the Exa API, asks for its current content.”

Source : [Exa: ExaUser](https://crawler.exa.ai/exauser), lu le 24 octobre 2026.

## Que se passe-t-il si vous bloquez ExaUser

Exa indique que, comme les récupérations sont lancées par un utilisateur, les règles robots.txt peuvent ne pas s’appliquer à ExaUser. Exa précise aussi qu’ExaUser n’est pas utilisé pour décider si un contenu apparaît dans la recherche Exa, et que les refus de recherche et l’exploration automatique se gèrent avec le jeton ExaSearchBot dans robots.txt.

## Les lignes robots.txt

Pour autoriser ExaUser :

```
User-agent: ExaUser
Allow: /
```

Pour bloquer ExaUser :

```
User-agent: ExaUser
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
Mozilla/5.0 (compatible; ExaUser/1.0; +https://crawler.exa.ai/exauser)
```

## Comment distinguer une vraie requête d'une fausse

L’opérateur indique que chaque requête est signée avec Web Bot Auth (RFC 9421) et publie ses clés dans un répertoire public ; il ne publie pas de liste d’IP.

## À comparer avec ExaSearchBot

[ExaSearchBot](/fr/bots/exasearchbot) : ExaSearchBot explore automatiquement pour construire l’index de recherche d’Exa et suit robots.txt, tandis qu’ExaUser ne récupère une page que lorsqu’un utilisateur ou une application le demande, et l’opérateur indique que robots.txt peut ne pas s’appliquer.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). ExaUser n'en fait pas partie : lisez votre robots.txt pour un groupe `ExaUser` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### ExaUser respecte-t-il robots.txt ?

Pas toujours. Partiel, l’opérateur indique que les règles robots.txt peuvent ne pas s’appliquer aux récupérations lancées par l’utilisateur. Une règle pour ExaUser dans robots.txt peut donc ne pas l'arrêter. Pour le refuser à coup sûr, utilisez une règle de pare-feu ou de CDN qui combine le user agent et les adresses publiées.

### Comment savoir si ExaUser est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Exa: ExaUser](https://crawler.exa.ai/exauser)
- [Exa: Exa Search Crawler](https://crawler.exa.ai/)
