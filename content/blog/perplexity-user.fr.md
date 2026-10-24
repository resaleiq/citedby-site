title: Perplexity-User : ce qu'il fait et ce que change son blocage
h1: Perplexity-User : ce qu'il fait et ce que change son blocage
description: Perplexity-User (Perplexity) : récupération déclenchée par l'utilisateur. Jeton robots.txt, effet d'un Disallow et vérification d'une requête.
slug: perplexity-user
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur Perplexity-User : opérateur Perplexity, rôle Récupération déclenchée par l'utilisateur, respecte robots.txt Pas toujours, liste d'adresses 4 plages
hero_sub: Perplexity-User, géré par Perplexity
hero_boxes: Opérateur|Perplexity; Rôle|Récupération déclenchée par l'utilisateur; Respecte robots.txt|Pas toujours; Liste d'adresses|4 plages
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/perplexitybot|PerplexityBot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: Perplexity-User est l’agent d’actions utilisateur de Perplexity : quand un utilisateur pose une question, il peut visiter une page pour répondre avec exactitude et renvoyer vers elle. Perplexity indique qu’il ne sert ni à explorer le web ni à entraîner des modèles d’IA, et qu’il ignore généralement les règles robots.txt car un utilisateur a demandé la récupération.

## Ce qu'est Perplexity-User

Perplexity-User est l’agent de récupération de Perplexity pour les actions d’utilisateur. Lorsqu’un utilisateur pose une question à Perplexity, il peut visiter une page web pour aider à fournir une réponse exacte et inclure un lien vers la page dans sa réponse. Perplexity indique qu’il n’est pas utilisé pour l’exploration du web ni pour collecter du contenu afin d’entraîner des modèles d’IA de fondation, et qu’il est distinct de PerplexityBot, qui fait apparaître des sites web et renvoie vers eux dans les résultats de recherche de Perplexity.

| Fait | Perplexity-User |
| --- | --- |
| Opérateur | Perplexity |
| Rôle | Récupération déclenchée par l’utilisateur |
| Jeton robots.txt | `Perplexity-User` |
| Respecte robots.txt | Ignore généralement les règles robots.txt, car un utilisateur a demandé la récupération |
| Adresses IP | 4 plages (www.perplexity.com/perplexity-user.json, fichier daté du 2025-10-17) |
| Page de l'opérateur lue le | 24 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “Since a user requested the fetch, this fetcher generally ignores robots.txt rules.”

Source : [Perplexity: Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers), lu le 24 octobre 2026.

## Que se passe-t-il si vous bloquez Perplexity-User

Perplexity liste Perplexity-User comme jeton robots.txt et indique qu’il contrôle les sites auxquels ces requêtes d’utilisateurs peuvent accéder. Perplexity indique aussi que cet agent ignore généralement les règles robots.txt car un utilisateur a demandé la récupération. Perplexity précise que chacun de ses réglages robots.txt fonctionne indépendamment et que les changements peuvent prendre jusqu’à 24 heures.

## Les lignes robots.txt

Pour autoriser Perplexity-User :

```
User-agent: Perplexity-User
Allow: /
```

Pour bloquer Perplexity-User :

```
User-agent: Perplexity-User
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Perplexity-User/1.0; +https://perplexity.ai/perplexity-user)
```

## Comment distinguer une vraie requête d'une fausse

Le fichier www.perplexity.com/perplexity-user.json contenait 4 plages le 24 octobre 2026, fichier daté du 2025-10-17.

Perplexity publie les adresses IP de Perplexity-User sous forme de fichier JSON et indique de l’utiliser comme source de référence pour les règles d’autorisation, en combinaison avec la chaîne de user agent.

## À comparer avec PerplexityBot

[PerplexityBot](/fr/bots/perplexitybot) : PerplexityBot fait apparaître les sites et renvoie vers eux dans les résultats de recherche de Perplexity, tandis que Perplexity-User récupère une page quand la question d’un utilisateur l’exige et ignore généralement robots.txt.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). Perplexity-User n'en fait pas partie : lisez votre robots.txt pour un groupe `Perplexity-User` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Perplexity-User respecte-t-il robots.txt ?

Ignore généralement les règles robots.txt, car un utilisateur a demandé la récupération. Une règle pour Perplexity-User dans robots.txt peut donc ne pas l'arrêter. Pour le refuser à coup sûr, utilisez une règle de pare-feu ou de CDN qui combine le user agent et les adresses publiées.

### Comment savoir si Perplexity-User est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Perplexity: Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers)
- [Perplexity: Perplexity-User IP addresses JSON (read 2026-10-24)](https://www.perplexity.com/perplexity-user.json)
