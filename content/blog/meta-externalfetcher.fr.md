title: Meta-ExternalFetcher : ce qu'il fait et ce que change son blocage
h1: Meta-ExternalFetcher : ce qu'il fait et ce que change son blocage
description: Meta-ExternalFetcher (Meta) : récupération déclenchée par l'utilisateur. Jeton robots.txt, effet d'un Disallow et vérification d'une requête.
slug: meta-externalfetcher
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur Meta-ExternalFetcher : opérateur Meta, rôle Récupération déclenchée par l'utilisateur, respecte robots.txt Pas toujours, liste d'adresses Aucune
hero_sub: Meta-ExternalFetcher, géré par Meta
hero_boxes: Opérateur|Meta; Rôle|Récupération déclenchée par l'utilisateur; Respecte robots.txt|Pas toujours; Liste d'adresses|Aucune
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/meta-externalagent|Meta-ExternalAgent; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: Meta-ExternalFetcher est un robot de Meta qui récupère des liens individuels à la demande d’un utilisateur. Meta indique qu’il prend en charge des fonctions comme aider l’IA à naviguer sur des sites pour accomplir des tâches d’utilisateurs, et qu’il peut contourner robots.txt, car ces récupérations sont demandées par un utilisateur. Les changements de robots.txt peuvent prendre jusqu’à 24 heures.

## Ce qu'est Meta-ExternalFetcher

Meta-ExternalFetcher est un robot de Meta qui récupère des liens individuels à la demande d’un utilisateur. Meta indique qu’il prend en charge des fonctions de produits comme l’évaluation et l’amélioration des capacités d’IA agentique, y compris aider l’IA à naviguer sur des sites web pour accomplir des tâches pour les utilisateurs. Meta le documente avec Meta-ExternalAgent, Meta-WebIndexer, Meta-ExternalAds et FacebookExternalHit sur une seule page.

| Fait | Meta-ExternalFetcher |
| --- | --- |
| Opérateur | Meta |
| Rôle | Récupération déclenchée par l’utilisateur |
| Jeton robots.txt | `Meta-ExternalFetcher` |
| Respecte robots.txt | Partiel, peut contourner robots.txt car les récupérations sont demandées par un utilisateur |
| Adresses IP | Aucune publiée |
| Page de l'opérateur lue le | 24 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “The Meta-ExternalFetcher crawler fetches individual links at a user's request and supports product functions such as evaluating and improving agentic AI capabilities—including helping AI navigate websites to complete tasks for users. Accordingly, this crawler may bypass robots.txt rules.”

Source : [Meta: Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers), lu le 24 octobre 2026.

## Que se passe-t-il si vous bloquez Meta-ExternalFetcher

Meta indique que vous pouvez bloquer ses robots en ajoutant à robots.txt un disallow pour le robot concerné. Meta indique aussi que Meta-ExternalFetcher peut contourner robots.txt parce qu’il effectue des récupérations demandées par l’utilisateur. Meta précise que les changements de robots.txt peuvent prendre jusqu’à 24 heures, car les robots peuvent mettre le fichier en cache jusqu’à 24 heures.

## Les lignes robots.txt

Pour autoriser Meta-ExternalFetcher :

```
User-agent: Meta-ExternalFetcher
Allow: /
```

Pour bloquer Meta-ExternalFetcher :

```
User-agent: Meta-ExternalFetcher
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
meta-externalfetcher/1.1
```

## Comment distinguer une vraie requête d'une fausse

La page des robots de Meta ne liste ni adresses IP ni méthode de vérification pour ce robot ; elle l’identifie par sa chaîne de user agent.

## À comparer avec Meta-ExternalAgent

[Meta-ExternalAgent](/fr/bots/meta-externalagent) : Meta-ExternalAgent explore le web en arrière-plan, notamment pour entraîner des modèles d’IA de fondation, tandis que Meta-ExternalFetcher récupère les liens uniques qu’un utilisateur a demandés et peut contourner robots.txt.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). Meta-ExternalFetcher n'en fait pas partie : lisez votre robots.txt pour un groupe `Meta-ExternalFetcher` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Meta-ExternalFetcher respecte-t-il robots.txt ?

Pas toujours : peut contourner robots.txt car les récupérations sont demandées par un utilisateur. Une règle pour Meta-ExternalFetcher dans robots.txt peut donc ne pas l'arrêter. Pour le refuser à coup sûr, utilisez une règle de pare-feu ou de CDN qui combine le user agent et les adresses publiées.

### Comment savoir si Meta-ExternalFetcher est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Meta: Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers)
