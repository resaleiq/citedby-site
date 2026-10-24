title: GPTBot : ce qu'il fait et ce que change son blocage
h1: GPTBot : ce qu'il fait et ce que change son blocage
description: GPTBot (OpenAI) : entraînement. Jeton robots.txt, effet d'un Disallow et vérification d'une requête, lus sur la page de l'opérateur.
slug: gptbot
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Quatre faits sur GPTBot : opérateur OpenAI, rôle Entraînement, respecte robots.txt Oui, liste d'adresses 18 plages
hero_sub: GPTBot, géré par OpenAI
hero_boxes: Opérateur|OpenAI; Rôle|Entraînement; Respecte robots.txt|Oui; Liste d'adresses|18 plages
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/oai-searchbot|OAI-SearchBot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: GPTBot est le robot d’exploration d’OpenAI pour l’entraînement. L’interdire dans robots.txt indique à OpenAI que le contenu du site ne doit pas servir à entraîner ses modèles de fondation d’IA générative. Il ne contrôle pas la recherche de ChatGPT, qui utilise OAI-SearchBot. OpenAI publie 18 plages d’IP pour GPTBot.

## Ce qu'est GPTBot

GPTBot est le robot auquel on pense en général quand on dit « bloquer OpenAI ». La page d’OpenAI indique qu’il sert à explorer du contenu pouvant être utilisé pour entraîner ses modèles. C’est l’un des trois robots nommés dans la documentation d’OpenAI pour la famille de produits ChatGPT, avec [OAI-SearchBot](/fr/bots/oai-searchbot) et [ChatGPT-User](/fr/bots/chatgpt-user).

| Fait | GPTBot |
| --- | --- |
| Opérateur | OpenAI |
| Rôle | Entraînement |
| Jeton robots.txt | `GPTBot` |
| Respecte robots.txt | Oui, il suit robots.txt |
| Adresses IP | 18 plages (openai.com/gptbot.json, fichier daté du 2026-09-22) |
| Page de l'opérateur lue le | 21 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “GPTBot is used to make our generative AI foundation models more useful and safe. It is used to crawl content that may be used in training our generative AI foundation models. Disallowing GPTBot indicates a site's content should not be used in training generative AI foundation models.”

Source : [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots), lu le 21 octobre 2026.

## Que se passe-t-il si vous bloquez GPTBot

OpenAI présente un Disallow pour GPTBot comme un signal sur l’entraînement : le contenu ne doit pas servir à entraîner des modèles de fondation d’IA générative. La même page donne l’exemple d’un site qui autorise OAI-SearchBot pour apparaître dans les résultats de recherche tout en interdisant GPTBot : un blocage ici ne vous retire donc pas, à lui seul, des réponses de recherche de ChatGPT. Bloquer ou non est un choix d’entreprise ; les deux sont légitimes.

## Les lignes robots.txt

Pour autoriser GPTBot :

```
User-agent: GPTBot
Allow: /
```

Pour bloquer GPTBot :

```
User-agent: GPTBot
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.4; +https://openai.com/gptbot
```

## Comment distinguer une vraie requête d'une fausse

La liste de GPTBot sur openai.com/gptbot.json est la plus courte des trois fichiers OpenAI que nous avons comptés : 18 préfixes le 21 octobre 2026, avec une date de création au 2026-09-22. Lorsqu’une requête nomme GPTBot mais vient d’une adresse hors de cette liste, le nom seul ne prouve rien.

## À comparer avec OAI-SearchBot

[OAI-SearchBot](/fr/bots/oai-searchbot) : Autorisez-le et interdisez GPTBot pour rester dans la recherche de ChatGPT tout en refusant l’entraînement.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste GPTBot avec une requête réelle et lit robots.txt pour lui. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### GPTBot respecte-t-il robots.txt ?

Oui, il suit robots.txt. Donnez à GPTBot son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si GPTBot est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots)
- [openai.com/gptbot.json](https://openai.com/gptbot.json)
