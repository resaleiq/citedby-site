title: Amazonbot : ce qu'il fait et ce que change son blocage
h1: Amazonbot : ce qu'il fait et ce que change son blocage
description: Amazonbot (Amazon) : plusieurs rôles. Jeton robots.txt, effet d'un Disallow et vérification d'une requête, lus sur la page de l'opérateur.
slug: amazonbot
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Quatre faits sur Amazonbot : opérateur Amazon, rôle Plusieurs rôles, respecte robots.txt Oui, liste d'adresses Liste sur sa page
hero_sub: Amazonbot, géré par Amazon
hero_boxes: Opérateur|Amazon; Rôle|Plusieurs rôles; Respecte robots.txt|Oui; Liste d'adresses|Liste sur sa page
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/duckassistbot|DuckAssistBot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: Amazonbot sert à améliorer les produits et services d’Amazon et peut servir à entraîner des modèles d’IA d’Amazon. La page d’Amazon couvre aussi Amzn-SearchBot, qui rend le contenu éligible aux expériences de recherche comme Alexa, et Amzn-User, qui peut ne pas suivre toutes les directives robots.txt. Chaque réglage est indépendant.

## Ce qu'est Amazonbot

La page d’Amazon couvre trois user agents et indique que chaque réglage est indépendant des autres et peut prendre environ 24 heures à s’appliquer : Amazonbot, Amzn-SearchBot et Amzn-User. Seul le premier est décrit comme pouvant entraîner des modèles d’IA d’Amazon.

| Fait | Amazonbot |
| --- | --- |
| Opérateur | Amazon |
| Rôle | Amélioration des produits, peut entraîner des modèles d’IA d’Amazon |
| Jeton robots.txt | `Amazonbot` |
| Respecte robots.txt | Oui, les changements prennent environ 24 heures |
| Adresses IP | Liste sur la page de l'opérateur (developer.amazon.com/amazonbot/ip-addresses) |
| Page de l'opérateur lue le | 21 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “Amazonbot is used to improve our products and services. This helps us provide more accurate information to customers and may be used to train Amazon AI models.”

Source : [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot), lu le 21 octobre 2026.

## Que se passe-t-il si vous bloquez Amazonbot

Amzn-SearchBot sert aux expériences de recherche comme Alexa : si vous l’autorisez, le contenu est éligible pour y apparaître. Amzn-User répond aux requêtes Alexa en direct qui demandent des informations à jour ; Amazon indique qu’il peut ne pas suivre toutes les directives robots.txt et qu’il n’explore pas pour l’entraînement de l’IA générative. Un fichier robots.txt qui ne cite qu’Amazonbot ne décrit donc pas votre politique pour les deux autres.

## Les lignes robots.txt

Pour autoriser Amazonbot :

```
User-agent: Amazonbot
Allow: /
```

Pour bloquer Amazonbot :

```
User-agent: Amazonbot
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Amazonbot/0.1) Chrome/W.X.Y.Z Safari/537.36
```

## Comment distinguer une vraie requête d'une fausse

Amazon publie les adresses d’Amazonbot et, sur des pages distinctes, celles d’Amzn-SearchBot et des récupérations en direct. Ces listes sont des pages HTML, pas un fichier JSON : nous n’indiquons donc pas de nombre. Amazon précise aussi que si robots.txt ne mentionne pas Amzn-SearchBot mais autorise d’autres robots de recherche, Amzn-SearchBot explore selon ce fichier.

## À comparer avec DuckAssistBot

[DuckAssistBot](/fr/bots/duckassistbot) : Autre robot de récupération pour réponses IA, avec un refus déclaré et un délai de 72 heures.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). Amazonbot n'en fait pas partie : lisez votre robots.txt pour un groupe `Amazonbot` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Amazonbot respecte-t-il robots.txt ?

Oui, les changements prennent environ 24 heures. Donnez à Amazonbot son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si Amazonbot est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot)
- [developer.amazon.com/amazonbot/ip-addresses](https://developer.amazon.com/amazonbot/ip-addresses)
