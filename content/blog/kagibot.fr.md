title: Kagibot : ce qu'il fait et ce que change son blocage
h1: Kagibot : ce qu'il fait et ce que change son blocage
description: Kagibot (Kagi) : recherche. Jeton robots.txt, effet d'un Disallow et vérification d'une requête, lus sur la page de l'opérateur.
slug: kagibot
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur Kagibot : opérateur Kagi, rôle Recherche, respecte robots.txt Oui, liste d'adresses Liste sur sa page
hero_sub: Kagibot, géré par Kagi
hero_boxes: Opérateur|Kagi; Rôle|Recherche; Respecte robots.txt|Oui; Liste d'adresses|Liste sur sa page
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/googlebot|Googlebot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: Kagibot est le robot d’exploration du moteur de recherche Kagi. Kagi indique que les directives robots.txt standard qui visent Kagibot sont respectées, et que lorsqu’aucune règle ne vise Kagibot mais qu’une vise Googlebot, Kagibot suit les directives de Googlebot. Kagi publie sa chaîne de user agent et les adresses IP d’où viennent ses requêtes.

## Ce qu'est Kagibot

Kagibot est le robot d’exploration du moteur de recherche Kagi. Kagi publie sa chaîne de user agent et les adresses IP d’où proviennent les requêtes de Kagibot.

| Fait | Kagibot |
| --- | --- |
| Opérateur | Kagi |
| Rôle | Recherche |
| Jeton robots.txt | `Kagibot` |
| Respecte robots.txt | Oui, les directives robots.txt standard qui visent Kagibot sont respectées |
| Adresses IP | Liste sur la page de l'opérateur (kagi.com/bot) |
| Page de l'opérateur lue le | 24 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “Standard directives in robots.txt that target Kagibot are respected.”

Source : [Kagi: About KagiBot](https://kagi.com/bot), lu le 24 octobre 2026.

## Que se passe-t-il si vous bloquez Kagibot

Kagi indique que les directives robots.txt standard qui visent Kagibot sont respectées, par exemple des règles Disallow pour un chemin. S’il n’y a pas de règle pour Kagibot mais qu’il y en a une pour Googlebot, Kagibot suit les directives de Googlebot.

## Les lignes robots.txt

Pour autoriser Kagibot :

```
User-agent: Kagibot
Allow: /
```

Pour bloquer Kagibot :

```
User-agent: Kagibot
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
Mozilla/5.0 (compatible; Kagibot/1.0; +https://kagi.com/bot)
```

## Comment distinguer une vraie requête d'une fausse

Kagi liste sur sa page du robot les adresses IP (avec des noms d’hôte kagibot.org) d’où proviennent les requêtes de Kagibot.

## À comparer avec Googlebot

[Googlebot](/fr/bots/googlebot) : Kagibot suit ses propres règles robots.txt, et se rabat sur celles de Googlebot quand aucune ne le vise.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). Kagibot n'en fait pas partie : lisez votre robots.txt pour un groupe `Kagibot` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Kagibot respecte-t-il robots.txt ?

Oui, les directives robots.txt standard qui visent Kagibot sont respectées. Donnez à Kagibot son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si Kagibot est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Kagi: About KagiBot (read 2026-10-24)](https://kagi.com/bot)
