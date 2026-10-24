title: ImagesiftBot : ce qu'il fait et ce que change son blocage
h1: ImagesiftBot : ce qu'il fait et ce que change son blocage
description: ImagesiftBot (Hive (ImageSift)) : recherche. Jeton robots.txt, effet d'un Disallow et vérification d'une requête, lus sur la page de l'opérateur.
slug: imagesiftbot
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur ImagesiftBot : opérateur Hive (ImageSift), rôle Recherche, respecte robots.txt Oui, liste d'adresses Aucune
hero_sub: ImagesiftBot, géré par Hive (ImageSift)
hero_boxes: Opérateur|Hive (ImageSift); Rôle|Recherche; Respecte robots.txt|Oui; Liste d'adresses|Aucune
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/googlebot|Googlebot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: ImagesiftBot est le robot d’exploration d’ImageSift, un produit de Hive. Il collecte des images publiquement disponibles avec l’URL de l’hôte, le texte de la page et le texte alternatif de l’image, pour un index servant à chercher des images similaires. L’opérateur indique qu’il respecte robots.txt et Crawl-delay, et suit les règles de Googlebot quand aucune ne le vise.

## Ce qu'est ImagesiftBot

ImageSiftBot est le robot d’exploration d’ImageSift, un produit de Hive. Il collecte des images publiquement disponibles, avec l’URL de l’hôte, le texte de la page et le texte alternatif de l’image. ImageSift stocke ces données dans un index que ses produits utilisent pour la recherche et la récupération d’images similaires.

| Fait | ImagesiftBot |
| --- | --- |
| Opérateur | Hive (ImageSift) |
| Rôle | Index d’images pour la recherche d’images similaires |
| Jeton robots.txt | `ImagesiftBot` |
| Respecte robots.txt | Oui, et il prend en charge Crawl-delay |
| Adresses IP | Aucune publiée |
| Page de l'opérateur lue le | 24 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “ImageSiftBot is a web crawler that scrapes the internet for publicly available images to support our suite of web intelligence products”

Source : [Imagesift by Hive: ImageSift Bot](https://imagesift.com/about), lu le 24 octobre 2026.

## Que se passe-t-il si vous bloquez ImagesiftBot

L’opérateur indique que les directives robots.txt standard qui visent ImagesiftBot sont respectées, et qu’il prend en charge Crawl-delay. Si aucune règle ne vise ImagesiftBot mais qu’une règle vise Googlebot, il suit les règles de Googlebot. La page donne aussi support@imagesift.com pour les demandes de refus.

## Les lignes robots.txt

Pour autoriser ImagesiftBot :

```
User-agent: ImagesiftBot
Allow: /
```

Pour bloquer ImagesiftBot :

```
User-agent: ImagesiftBot
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
Mozilla/5.0 (compatible; ImagesiftBot; +imagesift.com)
```

## Comment distinguer une vraie requête d'une fausse

La page de l’opérateur ne publie ni liste d’IP ni méthode de vérification.

## À comparer avec Googlebot

[Googlebot](/fr/bots/googlebot) : ImagesiftBot se rabat sur les règles robots.txt de Googlebot quand il n’en a pas de propres, et il collecte des images pour un index d’images similaires plutôt que pour une recherche web générale.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). ImagesiftBot n'en fait pas partie : lisez votre robots.txt pour un groupe `ImagesiftBot` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### ImagesiftBot respecte-t-il robots.txt ?

Oui, et il prend en charge Crawl-delay. Donnez à ImagesiftBot son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si ImagesiftBot est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Imagesift by Hive: ImageSift Bot](https://imagesift.com/about)
