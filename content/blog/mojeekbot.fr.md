title: MojeekBot : ce qu'il fait et ce que change son blocage
h1: MojeekBot : ce qu'il fait et ce que change son blocage
description: MojeekBot (Mojeek) : recherche. Jeton robots.txt, effet d'un Disallow et vérification d'une requête, lus sur la page de l'opérateur.
slug: mojeekbot
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur MojeekBot : opérateur Mojeek, rôle Recherche, respecte robots.txt Oui, liste d'adresses 1 plages
hero_sub: MojeekBot, géré par Mojeek
hero_boxes: Opérateur|Mojeek; Rôle|Recherche; Respecte robots.txt|Oui; Liste d'adresses|1 plages
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/bingbot|Bingbot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: MojeekBot est le robot d’exploration du moteur de recherche Mojeek. Mojeek indique qu’il respecte le Robots Exclusion Standard, en utilisant le premier enregistrement dont le User-Agent contient MojeekBot, et qu’il ne prend pas en charge la directive non standard crawl-delay. Il ne devrait pas demander plus d’une page d’un site dans la même seconde.

## Ce qu'est MojeekBot

MojeekBot est le robot d’exploration du moteur de recherche Mojeek. Mojeek indique qu’il ne devrait pas demander plus d’une page d’un site dans la même période de 1 seconde. Il respecte les balises meta noindex, nocache et nofollow.

| Fait | MojeekBot |
| --- | --- |
| Opérateur | Mojeek |
| Rôle | Recherche |
| Jeton robots.txt | `MojeekBot` |
| Respecte robots.txt | Oui, respecte le Robots Exclusion Standard ; crawl-delay n’est pas pris en charge |
| Adresses IP | 1 plages (www.mojeek.com/mojeekbot.json, fichier daté du 2025-05-14) |
| Page de l'opérateur lue le | 24 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “MojeekBot is the web crawler for the Mojeek search engine.”

Source : [Mojeek: MojeekBot](https://www.mojeek.com/bot.html), lu le 24 octobre 2026.

## Que se passe-t-il si vous bloquez MojeekBot

Mojeek indique que MojeekBot respecte le premier enregistrement robots.txt dont le User-Agent contient MojeekBot, et sinon le premier enregistrement pour User-Agent *. Il ne récupérera pas les URL contenant une chaîne interdite. Il ne prend pas en charge la directive non standard crawl-delay.

## Les lignes robots.txt

Pour autoriser MojeekBot :

```
User-agent: MojeekBot
Allow: /
```

Pour bloquer MojeekBot :

```
User-agent: MojeekBot
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
MojeekBot
```

## Comment distinguer une vraie requête d'une fausse

Le fichier www.mojeek.com/mojeekbot.json contenait 1 plages le 24 octobre 2026, fichier daté du 2025-05-14.

Mojeek indique de résoudre l’IP visiteuse en nom dans le domaine mojeek.com puis de la résoudre en retour vers la même IP, ou de comparer l’IP à sa liste publiée d’adresses IP de MojeekBot.

## À comparer avec Bingbot

[Bingbot](/fr/bots/bingbot) : Les deux explorent pour un moteur de recherche ; Mojeek publie une liste d’IP d’une seule plage et une vérification par DNS inverse, et ne prend pas en charge crawl-delay.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). MojeekBot n'en fait pas partie : lisez votre robots.txt pour un groupe `MojeekBot` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### MojeekBot respecte-t-il robots.txt ?

Oui, respecte le Robots Exclusion Standard ; crawl-delay n’est pas pris en charge. Donnez à MojeekBot son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si MojeekBot est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Mojeek: MojeekBot](https://www.mojeek.com/bot.html)
- [MojeekBot IP list (JSON, creationTime 2025-05-14, read 2026-10-24)](https://www.mojeek.com/mojeekbot.json)
