title: YouBot : ce qu'il fait et ce que change son blocage
h1: YouBot : ce qu'il fait et ce que change son blocage
description: YouBot (You.com) : recherche. Jeton robots.txt, effet d'un Disallow et vérification d'une requête, lus sur la page de l'opérateur.
slug: youbot
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur YouBot : opérateur You.com, rôle Recherche, respecte robots.txt Oui, liste d'adresses Liste sur sa page
hero_sub: YouBot, géré par You.com
hero_boxes: Opérateur|You.com; Rôle|Recherche; Respecte robots.txt|Oui; Liste d'adresses|Liste sur sa page
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/mojeekbot|MojeekBot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: YouBot est le robot d’exploration qui alimente le moteur de recherche You.com, en découvrant et en indexant des pages pour ses résultats. You.com indique qu’il respecte robots.txt, honore Crawl-delay et met robots.txt en cache pendant 30 minutes. User-agent: YouBot avec Disallow: / le bloque sur tout le site.

## Ce qu'est YouBot

YouBot est le robot d’exploration qui alimente le moteur de recherche You.com. Il découvre et indexe des pages web pour les résultats de recherche de You.com. You.com indique que X.X.X.X dans le user agent représente le numéro de version de Google Chrome.

| Fait | YouBot |
| --- | --- |
| Opérateur | You.com |
| Rôle | Recherche |
| Jeton robots.txt | `YouBot` |
| Respecte robots.txt | Oui, robots.txt est mis en cache pendant 30 minutes, donc les changements peuvent prendre jusqu’à 30 minutes |
| Adresses IP | Liste sur la page de l'opérateur (you.com/docs/youbot) |
| Page de l'opérateur lue le | 24 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “YouBot is the web crawler that powers the You.com search engine.”

Source : [You.com Docs: YouBot: You.com's Web Crawler](https://docs.you.com/youbot), lu le 24 octobre 2026.

## Que se passe-t-il si vous bloquez YouBot

You.com indique que YouBot respecte robots.txt et présente User-agent: YouBot avec Disallow: / comme moyen de le bloquer sur tout le site. Il honore aussi Crawl-delay et met robots.txt en cache pendant 30 minutes. La page ne décrit aucun autre agent de You.com.

## Les lignes robots.txt

Pour autoriser YouBot :

```
User-agent: YouBot
Allow: /
```

Pour bloquer YouBot :

```
User-agent: YouBot
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; YouBot/1.0; +https://docs.you.com/youbot; env:prod) Chrome/X.X.X.X Safari/537.36
```

## Comment distinguer une vraie requête d'une fausse

You.com indique que les requêtes proviennent de 68.67.112.0/24, que les hôtes se résolvent en youbot-{octets-avec-tirets}.search.you.com, et que les requêtes portent des signatures Cloudflare Web Bot Auth dont les clés publiques se trouvent à you.com/.well-known/http-message-signatures-directory.

## À comparer avec MojeekBot

[MojeekBot](/fr/bots/mojeekbot) : Les deux sont des robots de moteurs de recherche qui suivent robots.txt ; You.com prend en charge Crawl-delay et signe ses requêtes avec Web Bot Auth, alors que Mojeek ne prend pas en charge Crawl-delay.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). YouBot n'en fait pas partie : lisez votre robots.txt pour un groupe `YouBot` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### YouBot respecte-t-il robots.txt ?

Oui, robots.txt est mis en cache pendant 30 minutes, donc les changements peuvent prendre jusqu’à 30 minutes. Donnez à YouBot son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si YouBot est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [You.com Docs: YouBot: You.com's Web Crawler](https://docs.you.com/youbot)
