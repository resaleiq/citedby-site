title: Meta-WebIndexer : ce qu'il fait et ce que change son blocage
h1: Meta-WebIndexer : ce qu'il fait et ce que change son blocage
description: Meta-WebIndexer (Meta) : recherche. Jeton robots.txt, effet d'un Disallow et vérification d'une requête, lus sur la page de l'opérateur.
slug: meta-webindexer
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur Meta-WebIndexer : opérateur Meta, rôle Recherche, respecte robots.txt Oui, liste d'adresses Aucune
hero_sub: Meta-WebIndexer, géré par Meta
hero_boxes: Opérateur|Meta; Rôle|Recherche; Respecte robots.txt|Oui; Liste d'adresses|Aucune
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/meta-externalagent|Meta-ExternalAgent; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: Meta-WebIndexer est un robot de Meta qui parcourt le web pour améliorer la qualité des résultats de recherche de Meta AI. Meta indique que l’autoriser dans robots.txt l’aide à citer et à lier votre contenu dans les réponses de Meta AI. Meta indique qu’on le bloque par un disallow pour ce robot, et qu’un changement peut prendre jusqu’à 24 heures.

## Ce qu'est Meta-WebIndexer

Meta-WebIndexer est un robot de Meta qui parcourt le web pour améliorer la qualité des résultats de recherche de Meta AI pour les utilisateurs. Meta indique que l’autoriser dans robots.txt l’aide à citer et à lier votre contenu dans les réponses de Meta AI. Meta le documente avec Meta-ExternalAgent, Meta-ExternalFetcher, Meta-ExternalAds et FacebookExternalHit sur une seule page.

| Fait | Meta-WebIndexer |
| --- | --- |
| Opérateur | Meta |
| Rôle | Recherche |
| Jeton robots.txt | `Meta-WebIndexer` |
| Respecte robots.txt | Oui, les changements peuvent prendre jusqu’à 24 heures |
| Adresses IP | Aucune publiée |
| Page de l'opérateur lue le | 24 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “The Meta-WebIndexer crawler navigates the web to improve Meta AI search result quality for users. In doing so, Meta analyzes online content to enhance the relevance and accuracy of Meta AI.”

Source : [Meta: Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers), lu le 24 octobre 2026.

## Que se passe-t-il si vous bloquez Meta-WebIndexer

Meta indique que vous pouvez bloquer ses robots en ajoutant à robots.txt un disallow pour le robot concerné, et que les changements de robots.txt peuvent prendre jusqu’à 24 heures. Meta indique qu’autoriser Meta-WebIndexer l’aide à citer et à lier votre contenu dans les réponses de Meta AI. La page de Meta ne dit pas si un disallow pour Meta-WebIndexer affecte ses autres robots.

## Les lignes robots.txt

Pour autoriser Meta-WebIndexer :

```
User-agent: Meta-WebIndexer
Allow: /
```

Pour bloquer Meta-WebIndexer :

```
User-agent: Meta-WebIndexer
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
meta-webindexer/1.1
```

## Comment distinguer une vraie requête d'une fausse

La page des robots de Meta ne liste ni adresses IP ni méthode de vérification pour ce robot ; elle l’identifie par sa chaîne de user agent.

## À comparer avec Meta-ExternalAgent

[Meta-ExternalAgent](/fr/bots/meta-externalagent) : Meta-WebIndexer sert aux résultats de recherche et aux citations de Meta AI, tandis que Meta décrit Meta-ExternalAgent comme explorant pour des usages comme l’entraînement de modèles d’IA de fondation ou l’indexation directe de contenu.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). Meta-WebIndexer n'en fait pas partie : lisez votre robots.txt pour un groupe `Meta-WebIndexer` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Meta-WebIndexer respecte-t-il robots.txt ?

Oui, les changements peuvent prendre jusqu’à 24 heures. Donnez à Meta-WebIndexer son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si Meta-WebIndexer est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Meta: Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers)
