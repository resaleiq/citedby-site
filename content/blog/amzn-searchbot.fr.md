title: Amzn-SearchBot : ce qu'il fait et ce que change son blocage
h1: Amzn-SearchBot : ce qu'il fait et ce que change son blocage
description: Amzn-SearchBot (Amazon) : recherche. Jeton robots.txt, effet d'un Disallow et vérification d'une requête, lus sur la page de l'opérateur.
slug: amzn-searchbot
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur Amzn-SearchBot : opérateur Amazon, rôle Recherche, respecte robots.txt Oui, liste d'adresses Liste sur sa page
hero_sub: Amzn-SearchBot, géré par Amazon
hero_boxes: Opérateur|Amazon; Rôle|Recherche; Respecte robots.txt|Oui; Liste d'adresses|Liste sur sa page
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/amazonbot|Amazonbot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: Amzn-SearchBot est un robot d’exploration d’Amazon qui sert à améliorer les expériences de recherche comme Alexa. Amazon indique qu’en l’autorisant, votre contenu devient éligible pour y apparaître, et qu’il n’explore pas de contenu pour entraîner des modèles d’IA générative. Son réglage est indépendant d’Amazonbot et d’Amzn-User, et un changement peut prendre environ 24 heures.

## Ce qu'est Amzn-SearchBot

Amzn-SearchBot est un robot d’exploration d’Amazon qui sert à améliorer les expériences de recherche dans les produits et services d’Amazon. Amazon indique qu’en l’autorisant, votre contenu devient éligible pour apparaître dans des expériences de recherche comme Alexa, et qu’il n’explore pas de contenu pour l’entraînement de modèles d’IA générative. C’est l’un des trois user agents d’Amazon (Amazonbot, Amzn-SearchBot, Amzn-User) que la société documente sur une seule page.

| Fait | Amzn-SearchBot |
| --- | --- |
| Opérateur | Amazon |
| Rôle | Recherche |
| Jeton robots.txt | `Amzn-SearchBot` |
| Respecte robots.txt | Oui, les changements peuvent prendre environ 24 heures |
| Adresses IP | Liste sur la page de l'opérateur (developer.amazon.com/amazonbot/searchbot-ip-addresses) |
| Page de l'opérateur lue le | 24 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “If robots.txt files don’t mention Amzn-SearchBot but allow other search bots, Amzn-SearchBot will crawl in accordance with the robots.txt directives given to other search bots.”

Source : [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot), lu le 24 octobre 2026.

## Que se passe-t-il si vous bloquez Amzn-SearchBot

Amazon indique que l’exploration automatisée par ses user agents listés respecte le Robots Exclusion Protocol, en honorant les directives user-agent et allow/disallow. Amazon précise que le réglage de chaque user agent est indépendant des autres et peut prendre environ 24 heures à s’appliquer. Si robots.txt ne mentionne pas Amzn-SearchBot mais autorise d’autres robots de recherche, il suit les directives données à ces autres robots de recherche.

## Les lignes robots.txt

Pour autoriser Amzn-SearchBot :

```
User-agent: Amzn-SearchBot
Allow: /
```

Pour bloquer Amzn-SearchBot :

```
User-agent: Amzn-SearchBot
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Amzn-SearchBot/0.1) Chrome/W.X.Y.Z Safari/537.36
```

## Comment distinguer une vraie requête d'une fausse

Amazon publie les adresses IP d’Amzn-SearchBot sur une page web qui affiche la liste au format JSON, et renvoie vers elle depuis la page de documentation d’Amazonbot.

## À comparer avec Amazonbot

[Amazonbot](/fr/bots/amazonbot) : Amazonbot sert à améliorer les produits et services d’Amazon et peut servir à entraîner des modèles d’IA d’Amazon, alors qu’Amzn-SearchBot est destiné aux expériences de recherche et qu’Amazon indique qu’il n’explore pas pour l’entraînement de modèles d’IA générative.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). Amzn-SearchBot n'en fait pas partie : lisez votre robots.txt pour un groupe `Amzn-SearchBot` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Amzn-SearchBot respecte-t-il robots.txt ?

Oui, les changements peuvent prendre environ 24 heures. Donnez à Amzn-SearchBot son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si Amzn-SearchBot est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot)
- [Amazon: Amzn-SearchBot IP addresses (read 2026-10-24)](https://developer.amazon.com/amazonbot/searchbot-ip-addresses/)
