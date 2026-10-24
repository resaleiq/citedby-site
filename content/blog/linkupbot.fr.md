title: LinkupBot : ce qu'il fait et ce que change son blocage
h1: LinkupBot : ce qu'il fait et ce que change son blocage
description: LinkupBot (Linkup) : recherche. Jeton robots.txt, effet d'un Disallow et vérification d'une requête, lus sur la page de l'opérateur.
slug: linkupbot
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur LinkupBot : opérateur Linkup, rôle Recherche, respecte robots.txt Oui, liste d'adresses Liste sur sa page
hero_sub: LinkupBot, géré par Linkup
hero_boxes: Opérateur|Linkup; Rôle|Recherche; Respecte robots.txt|Oui; Liste d'adresses|Liste sur sa page
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/perplexitybot|PerplexityBot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: LinkupBot est le robot d’exploration de Linkup. Il récupère des pages accessibles publiquement pour construire l’index de recherche de Linkup, qui, selon Linkup, alimente la recherche et l’ancrage web des applications d’IA. Linkup indique que User-agent: LinkupBot avec Disallow: / bloque tout le site, et que robots.txt n’est pas un mécanisme de contrôle d’accès.

## Ce qu'est LinkupBot

LinkupBot est le robot d’exploration de Linkup. Il récupère des pages accessibles publiquement pour construire et tenir à jour l’index de recherche de Linkup, qui, selon Linkup, alimente la recherche et l’ancrage web des applications d’IA.

| Fait | LinkupBot |
| --- | --- |
| Opérateur | Linkup |
| Rôle | Index de recherche pour la recherche web par IA |
| Jeton robots.txt | `LinkupBot` |
| Respecte robots.txt | Oui, l’opérateur indique qu’il respecte les règles robots.txt applicables |
| Adresses IP | Liste sur la page de l'opérateur (www.linkup.so/linkupbot-ips.txt) |
| Page de l'opérateur lue le | 24 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “LinkupBot is Linkup’s web crawler. It discovers and retrieves publicly accessible webpages to build and maintain the Linkup web search index, which powers search and web grounding for AI applications.”

Source : [Linkup: LinkupBot](https://www.linkup.so/bot), lu le 24 octobre 2026.

## Que se passe-t-il si vous bloquez LinkupBot

Ajouter User-agent: LinkupBot avec Disallow: / à robots.txt bloque tout le site, selon l’opérateur. L’opérateur indique aussi que les règles robots s’appliquent par hôte, qu’autoriser LinkupBot dans un pare-feu ne prime pas sur robots.txt, et que robots.txt n’est pas un mécanisme de contrôle d’accès.

## Les lignes robots.txt

Pour autoriser LinkupBot :

```
User-agent: LinkupBot
Allow: /
```

Pour bloquer LinkupBot :

```
User-agent: LinkupBot
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
LinkupBot/1.0 (LinkupBot for web indexing; https://www.linkup.so/bot; bot@linkup.so)
```

## Comment distinguer une vraie requête d'une fausse

L’opérateur indique que les requêtes viennent des plages CIDR de sa liste publiée, et recommande de vérifier à la fois l’IP source dans cette liste et un user agent contenant le jeton LinkupBot.

## À comparer avec PerplexityBot

[PerplexityBot](/fr/bots/perplexitybot) : Les deux construisent un index de recherche qui alimente des réponses IA ; l’index de LinkupBot sert des applications d’IA via le service de recherche et d’ancrage de Linkup, et sa liste d’IP est un fichier texte brut plutôt que du JSON.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). LinkupBot n'en fait pas partie : lisez votre robots.txt pour un groupe `LinkupBot` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### LinkupBot respecte-t-il robots.txt ?

Oui, l’opérateur indique qu’il respecte les règles robots.txt applicables. Donnez à LinkupBot son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si LinkupBot est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Linkup: LinkupBot](https://www.linkup.so/bot)
- [Linkup: linkupbot-ips.txt (plain text, read 2026-10-24)](https://www.linkup.so/linkupbot-ips.txt)
