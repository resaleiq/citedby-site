title: ICC-Crawler : ce qu'il fait et ce que change son blocage
h1: ICC-Crawler : ce qu'il fait et ce que change son blocage
description: ICC-Crawler (NICT (Universal Communication Research Institute)) : entraînement. Jeton robots.txt, effet d'un Disallow et vérification d'une requête.
slug: icc-crawler
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur ICC-Crawler : opérateur NICT (Universal Communication Research Institute), rôle Entraînement, respecte robots.txt Oui, liste d'adresses Liste sur sa page
hero_sub: ICC-Crawler, géré par NICT (Universal Communication Research Institute)
hero_boxes: Opérateur|NICT (Universal Communication Research Institute); Rôle|Entraînement; Respecte robots.txt|Oui; Liste d'adresses|Liste sur sa page
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/gptbot|GPTBot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: ICC-Crawler est exploité par l’Universal Communication Research Institute du NICT au Japon. Le NICT indique qu’il utilise les pages collectées pour la recherche sur le traitement de l’information, notamment la traduction multilingue, l’analyse de l’information et l’intelligence artificielle. Il prend en charge le Robots Exclusion Protocol : User-agent: ICC-Crawler avec Disallow: / pourrait désactiver la collecte sur toutes les pages.

## Ce qu'est ICC-Crawler

ICC-Crawler est un robot d’exploration exploité par l’Universal Communication Research Institute du National Institute of Information and Communications Technology (NICT) du Japon. Le NICT indique qu’il utilise les pages collectées pour la recherche et le développement de technologies de traitement de l’information, notamment la traduction multilingue, l’analyse de l’information et l’intelligence artificielle. Le NICT peut aussi fournir les informations collectées ou les produits de recherche à des tiers, dans la mesure permise par la loi.

| Fait | ICC-Crawler |
| --- | --- |
| Opérateur | NICT (Universal Communication Research Institute) |
| Rôle | Collecte de données pour la recherche (inclut la recherche et le développement en IA) |
| Jeton robots.txt | `ICC-Crawler` |
| Respecte robots.txt | Oui, et avec un Crawl-Delay il utilise la plus grande valeur entre cet intervalle et son propre minimum |
| Adresses IP | Liste sur la page de l'opérateur (ucri.nict.go.jp/en/icccrawler.html) |
| Page de l'opérateur lue le | 24 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “NICT uses the information it collects for research and development of advanced information processing technologies including multilingual translation, information analysis, and artificial intelligence technologies.”

Source : [NICT Universal Communication Research Institute: ICC-Crawler](https://ucri.nict.go.jp/en/icccrawler.html), lu le 24 octobre 2026.

## Que se passe-t-il si vous bloquez ICC-Crawler

Le NICT indique qu’ICC-Crawler prend en charge le Robots Exclusion Protocol et qu’ajouter User-agent: ICC-Crawler avec Disallow: / à robots.txt pourrait désactiver la collecte sur toutes les pages. Il permet aussi aux propriétaires de sites de bloquer un chemin ou un type de fichier, ou d’autoriser certains chemins sous un Disallow complet. Si l’accès continue ensuite, le NICT demande aux propriétaires de sites de le contacter afin qu’il cesse de collecter sur cet hôte.

## Les lignes robots.txt

Pour autoriser ICC-Crawler :

```
User-agent: ICC-Crawler
Allow: /
```

Pour bloquer ICC-Crawler :

```
User-agent: ICC-Crawler
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La page de l'opérateur n'indique pas de chaîne user-agent complète pour ICC-Crawler.

## Comment distinguer une vraie requête d'une fausse

La page de l’opérateur liste les adresses IP du robot en texte brut ; elle ne publie pas de liste lisible par machine.

## À comparer avec GPTBot

[GPTBot](/fr/bots/gptbot) : Les deux collectent des pages qui alimentent le développement de l’IA, mais ICC-Crawler est exploité par un institut public de recherche japonais pour ses propres recherches et publie deux adresses IP de robot sur sa page, tandis que GPTBot est exploité par une société commerciale.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). ICC-Crawler n'en fait pas partie : lisez votre robots.txt pour un groupe `ICC-Crawler` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### ICC-Crawler respecte-t-il robots.txt ?

Oui, et avec un Crawl-Delay il utilise la plus grande valeur entre cet intervalle et son propre minimum. Donnez à ICC-Crawler son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si ICC-Crawler est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [NICT Universal Communication Research Institute: ICC-Crawler](https://ucri.nict.go.jp/en/icccrawler.html)
