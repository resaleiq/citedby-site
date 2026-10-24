title: Bingbot : ce qu'il fait et ce que change son blocage
h1: Bingbot : ce qu'il fait et ce que change son blocage
description: Bingbot (Microsoft) : recherche. Jeton robots.txt, effet d'un Disallow et vérification d'une requête, lus sur la page de l'opérateur.
slug: bingbot
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Quatre faits sur Bingbot : opérateur Microsoft, rôle Recherche, respecte robots.txt Oui, liste d'adresses Outil de vérification
hero_sub: Bingbot, géré par Microsoft
hero_boxes: Opérateur|Microsoft; Rôle|Recherche; Respecte robots.txt|Oui; Liste d'adresses|Outil de vérification
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/googlebot|Googlebot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: Bingbot est le robot d’exploration standard de Microsoft et assure l’essentiel de l’exploration de Bing. La page d’aide de Bing liste cinq robots : Bingbot, AdIdxBot, BingPreview, MicrosoftPreview et BingVideoPreview. Vous les contrôlez via robots.txt, et la vitesse d’exploration via l’outil Crawl control de Bing Webmaster Tools, pas via robots.txt.

## Ce qu'est Bingbot

La page de Bing s’intitule « Overview of Bing crawlers (user agents) » et indique que Bing exploite aujourd’hui ces principaux robots : Bingbot (le robot standard), AdIdxBot (utilisé par Bing Ads, qui explore les annonces et suit leurs sites web pour le contrôle qualité), BingPreview (captures de pages pour Bing), MicrosoftPreview (captures pour les produits Microsoft) et BingVideoPreview (aperçus vidéo, dans Bing uniquement). Bingbot, AdIdxBot, BingPreview et BingVideoPreview existent en variantes ordinateur et mobile. La page ne nomme pas de robot d’exploration IA distinct. La même section d’aide contient « How To Permanently Remove a URL or Page from Bing or Copilot », la page à lire si l’objectif est la suppression plutôt que l’accès.

| Fait | Bingbot |
| --- | --- |
| Opérateur | Microsoft |
| Rôle | Robot d’exploration de recherche |
| Jeton robots.txt | `bingbot` |
| Respecte robots.txt | Oui |
| Adresses IP | Outil de vérification |
| Page de l'opérateur lue le | 21 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “Bingbot is our standard crawler and handles most of our crawling needs each day.”

Source : [Microsoft Bing Webmaster help: Which Crawlers Does Bing Use?](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0), lu le 21 octobre 2026.

## Que se passe-t-il si vous bloquez Bingbot

La page de Bing ne dit pas ce que coûte un blocage ; il s’agit de notre lecture, pas de celle de Bing. Bingbot est le robot qui alimente Bing : l’interdire dans robots.txt empêche Bing d’explorer ces pages, et tout ce qui s’appuie sur l’index de Bing les perd aussi. Bing vous donne deux contrôles : robots.txt indique à ses robots comment interagir avec votre site, et Bing Webmaster Tools propose un outil Crawl control qui règle la vitesse d’exploration heure par heure.

## Les lignes robots.txt

Pour autoriser Bingbot :

```
User-agent: bingbot
Allow: /
```

Pour bloquer Bingbot :

```
User-agent: bingbot
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm) Chrome/W.X.Y.Z Safari/537.36
```

## Comment distinguer une vraie requête d'une fausse

Bing indique que les chaînes de user agent sont faciles à usurper, donc toutes les requêtes qui les portent ne viennent pas d’un vrai robot Bing. Pour vérifier l’adresse, utilisez l’outil Verify Bingbot ou l’une des autres méthodes de vérification que décrit Bing. Dans la chaîne de user agent, W.X.Y.Z représente la version de Microsoft Edge avec laquelle Bing effectue le rendu, que Bing dit mettre à jour régulièrement. Nous n’avons pas lu de liste d’IP sur cette page, donc nous n’indiquons aucun nombre.

## À comparer avec Googlebot

[Googlebot](/fr/bots/googlebot) : L’autre grand robot de recherche : un jeton différent et une vérification différente.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste Bingbot avec une requête réelle et lit robots.txt pour lui. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Bingbot respecte-t-il robots.txt ?

Oui. Donnez à bingbot son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si Bingbot est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Microsoft Bing Webmaster help: Which Crawlers Does Bing Use?](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0)
