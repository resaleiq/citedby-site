title: Amzn-User : ce qu'il fait et ce que change son blocage
h1: Amzn-User : ce qu'il fait et ce que change son blocage
description: Amzn-User (Amazon) : récupération déclenchée par l'utilisateur. Jeton robots.txt, effet d'un Disallow et vérification d'une requête.
slug: amzn-user
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur Amzn-User : opérateur Amazon, rôle Récupération déclenchée par l'utilisateur, respecte robots.txt Pas toujours, liste d'adresses Liste sur sa page
hero_sub: Amzn-User, géré par Amazon
hero_boxes: Opérateur|Amazon; Rôle|Récupération déclenchée par l'utilisateur; Respecte robots.txt|Pas toujours; Liste d'adresses|Liste sur sa page
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/amzn-searchbot|Amzn-SearchBot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: Amzn-User est le user agent d’Amazon qui récupère des pages en direct lorsqu’un client pose à Alexa une question qui demande des informations à jour. Amazon indique qu’il n’explore pas pour l’entraînement de l’IA générative et qu’il peut ne pas suivre toutes les directives robots.txt, car l’action est lancée par l’utilisateur. Amazonbot et Amzn-SearchBot sont des réglages distincts.

## Ce qu'est Amzn-User

Amzn-User est un user agent d’Amazon qui prend en charge des actions de l’utilisateur, par exemple répondre à des requêtes Alexa qui demandent des informations à jour. Amazon indique que lorsqu’un client pose une question, Amzn-User peut récupérer des informations en direct sur le web pour fournir des réponses exactes au nom de l’utilisateur. Amazon indique qu’il n’explore pas de contenu pour l’entraînement de modèles d’IA générative.

| Fait | Amzn-User |
| --- | --- |
| Opérateur | Amazon |
| Rôle | Récupération déclenchée par l’utilisateur |
| Jeton robots.txt | `Amzn-User` |
| Respecte robots.txt | Partiel, peut ne pas suivre toutes les directives robots.txt car les actions peuvent être lancées par l’utilisateur |
| Adresses IP | Liste sur la page de l'opérateur (developer.amazon.com/amazonbot/live-ip-addresses) |
| Page de l'opérateur lue le | 24 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “Because actions taken by Amzn-User can be initiated by a user, it may not follow all robots.txt directives.”

Source : [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot), lu le 24 octobre 2026.

## Que se passe-t-il si vous bloquez Amzn-User

Amazon indique qu’Amzn-User peut ne pas suivre toutes les directives robots.txt, parce que ses actions peuvent être lancées par un utilisateur. Amazon précise aussi que chacun de ses réglages de user agent (Amazonbot, Amzn-SearchBot, Amzn-User) est indépendant des autres et peut prendre environ 24 heures à refléter les changements.

## Les lignes robots.txt

Pour autoriser Amzn-User :

```
User-agent: Amzn-User
Allow: /
```

Pour bloquer Amzn-User :

```
User-agent: Amzn-User
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Amzn-User/0.1) Chrome/W.X.Y.Z Safari/537.36
```

## Comment distinguer une vraie requête d'une fausse

Amazon publie les adresses IP d’Amzn-User sur une page web qui affiche la liste au format JSON, et renvoie vers elle depuis la page de documentation d’Amazonbot.

## À comparer avec Amzn-SearchBot

[Amzn-SearchBot](/fr/bots/amzn-searchbot) : Amzn-SearchBot est un robot d’exploration automatisé pour les expériences de recherche d’Amazon, qui, selon Amazon, respecte robots.txt, alors qu’Amzn-User récupère des informations en direct quand un client pose une question et peut ne pas suivre toutes les directives.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). Amzn-User n'en fait pas partie : lisez votre robots.txt pour un groupe `Amzn-User` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Amzn-User respecte-t-il robots.txt ?

Pas toujours : peut ne pas suivre toutes les directives robots.txt car les actions peuvent être lancées par l’utilisateur. Une règle pour Amzn-User dans robots.txt peut donc ne pas l'arrêter. Pour le refuser à coup sûr, utilisez une règle de pare-feu ou de CDN qui combine le user agent et les adresses publiées.

### Comment savoir si Amzn-User est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot)
- [Amazon: Amzn-User IP addresses (read 2026-10-24)](https://developer.amazon.com/amazonbot/live-ip-addresses/)
