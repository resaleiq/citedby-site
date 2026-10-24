title: Googlebot : ce qu'il fait et ce que change son blocage
h1: Googlebot : ce qu'il fait et ce que change son blocage
description: Googlebot (Google) : recherche. Jeton robots.txt, effet d'un Disallow et vérification d'une requête, lus sur la page de l'opérateur.
slug: googlebot
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Quatre faits sur Googlebot : opérateur Google, rôle Recherche, respecte robots.txt Oui, liste d'adresses 317 plages
hero_sub: Googlebot, géré par Google
hero_boxes: Opérateur|Google; Rôle|Recherche; Respecte robots.txt|Oui; Liste d'adresses|317 plages
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/google-extended|Google-Extended; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: Googlebot est le principal robot d’exploration de Google pour Search. Google indique que ses robots d’exploration courants respectent toujours les règles robots.txt lors d’une exploration automatique. Les préférences d’exploration pour le jeton Googlebot concernent Google Search, y compris Discover, et des produits comme Images, Video et News. Google publie 317 plages d’IP pour lui.

## Ce qu'est Googlebot

Googlebot est le robot d’où part chaque contrôle de Search. La page de Google liste plusieurs robots, et le seul jeton Googlebot régit Search, Discover et les produits qui s’appuient sur la même exploration, comme Images, le mode Video et News.

| Fait | Googlebot |
| --- | --- |
| Opérateur | Google |
| Rôle | Recherche (aussi Images, Video, News, Discover) |
| Jeton robots.txt | `Googlebot` |
| Respecte robots.txt | Oui, toujours lors d’une exploration automatique |
| Adresses IP | 317 plages (developers.google.com/static/search/apis/ipranges/googlebot.json, fichier daté du 2026-10-20) |
| Page de l'opérateur lue le | 21 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “Google's common crawlers are used to find information for building Google's search indexes, perform other product specific crawls, and for analysis. They always obey robots.txt rules when crawling automatically.”

Source : [Google Search Central: Google's common crawlers (last updated 2026-10-15)](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers), lu le 21 octobre 2026.

## Que se passe-t-il si vous bloquez Googlebot

Un Disallow pour Googlebot n’est pas un refus d’IA ciblé ; il affecte Google Search lui-même, y compris Discover et les fonctions qui s’appuient dessus, selon la liste des produits concernés de Google. Le contrôle plus ciblé pour l’entraînement de Gemini est le jeton distinct [Google-Extended](/fr/bots/google-extended).

## Les lignes robots.txt

Pour autoriser Googlebot :

```
User-agent: Googlebot
Allow: /
```

Pour bloquer Googlebot :

```
User-agent: Googlebot
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)
```

## Comment distinguer une vraie requête d'une fausse

Google publie les plages que ses robots d’exploration courants utilisent. Le fichier de Googlebot contenait 317 préfixes le 21 octobre 2026, avec une date de création au 2026-10-20 14:46 UTC. Google documente aussi un masque DNS inverse pour confirmer un nom d’hôte : une requête se vérifie donc de deux façons, l’adresse contre le fichier et la recherche inverse contre le masque. La page elle-même a été mise à jour pour la dernière fois le 2026-10-15.

## À comparer avec Google-Extended

[Google-Extended](/fr/bots/google-extended) : Un jeton de contrôle pour l’entraînement de Gemini ; il ne récupère jamais de page.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste Googlebot avec une requête réelle et lit robots.txt pour lui. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Googlebot respecte-t-il robots.txt ?

Oui, toujours lors d’une exploration automatique. Donnez à Googlebot son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si Googlebot est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Google Search Central: Google's common crawlers (last updated 2026-10-15)](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers)
- [developers.google.com/static/search/apis/ipranges/googlebot.json](https://developers.google.com/static/crawling/ipranges/common-crawlers.json)
