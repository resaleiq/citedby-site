title: OAI-SearchBot : ce qu'il fait et ce que change son blocage
h1: OAI-SearchBot : ce qu'il fait et ce que change son blocage
description: OAI-SearchBot (OpenAI) : recherche. Jeton robots.txt, effet d'un Disallow et vérification d'une requête, lus sur la page de l'opérateur.
slug: oai-searchbot
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Quatre faits sur OAI-SearchBot : opérateur OpenAI, rôle Recherche, respecte robots.txt Oui, liste d'adresses 39 plages
hero_sub: OAI-SearchBot, géré par OpenAI
hero_boxes: Opérateur|OpenAI; Rôle|Recherche; Respecte robots.txt|Oui; Liste d'adresses|39 plages
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/gptbot|GPTBot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: OAI-SearchBot est le robot d’exploration d’OpenAI pour la recherche de ChatGPT. Les sites qui le refusent ne seront pas montrés dans les réponses de recherche de ChatGPT, mais peuvent encore apparaître sous forme de liens de navigation. Il respecte robots.txt avec le jeton OAI-SearchBot, et OpenAI publie 39 plages d’IP pour lui.

## Ce qu'est OAI-SearchBot

OpenAI exploite plusieurs robots et indique que chaque réglage est indépendant des autres. OAI-SearchBot est celui qui décide si vos pages peuvent apparaître dans les fonctions de recherche de ChatGPT. Ce n’est pas le robot d’entraînement (c’est [GPTBot](/fr/bots/gptbot)) et ce n’est pas l’agent qui ouvre une page quand une personne pose une question à son sujet (c’est [ChatGPT-User](/fr/bots/chatgpt-user)).

| Fait | OAI-SearchBot |
| --- | --- |
| Opérateur | OpenAI |
| Rôle | Recherche |
| Jeton robots.txt | `OAI-SearchBot` |
| Respecte robots.txt | Oui, il suit robots.txt |
| Adresses IP | 39 plages (openai.com/searchbot.json, fichier daté du 2026-01-02) |
| Page de l'opérateur lue le | 21 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “OAI-SearchBot is used to surface websites in search results in ChatGPT's search features. Sites that are opted out of OAI-SearchBot will not be shown in ChatGPT search answers, though can still appear as navigational links.”

Source : [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots), lu le 21 octobre 2026.

## Que se passe-t-il si vous bloquez OAI-SearchBot

La formulation d’OpenAI est que les sites qui refusent « ne seront pas montrés dans les réponses de recherche de ChatGPT ». C’est là le coût : une boutique qui bloque OAI-SearchBot renonce à la partie de ChatGPT qui renvoie vers des sources. OpenAI recommande l’inverse aux sites qui veulent apparaître : autoriser OAI-SearchBot dans robots.txt et autoriser les requêtes provenant de ses plages d’IP publiées.

## Les lignes robots.txt

Pour autoriser OAI-SearchBot :

```
User-agent: OAI-SearchBot
Allow: /
```

Pour bloquer OAI-SearchBot :

```
User-agent: OAI-SearchBot
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36; compatible; OAI-SearchBot/1.4; +https://openai.com/searchbot
```

## Comment distinguer une vraie requête d'une fausse

OpenAI publie les adresses qu’utilise OAI-SearchBot sur openai.com/searchbot.json. Le 21 octobre 2026, ce fichier contenait 39 préfixes et portait la date de création 2026-01-02. Comparez l’adresse de votre journal de serveur à ces préfixes avant de faire confiance à une requête qui ne fait que revendiquer le nom dans son user agent. OpenAI indique aussi que lorsqu’il récupère robots.txt, il peut ajouter un marqueur `robots.txt` à la chaîne de user agent : ces requêtes se distinguent donc facilement dans des journaux sans chemins.

## À comparer avec GPTBot

[GPTBot](/fr/bots/gptbot) : GPTBot sert à l’entraînement ; le bloquer ne vous retire pas de la recherche de ChatGPT, car les réglages sont indépendants.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste OAI-SearchBot avec une requête réelle et lit robots.txt pour lui. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### OAI-SearchBot respecte-t-il robots.txt ?

Oui, il suit robots.txt. Donnez à OAI-SearchBot son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si OAI-SearchBot est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots)
- [openai.com/searchbot.json](https://openai.com/searchbot.json)
