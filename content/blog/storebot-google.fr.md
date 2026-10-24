title: Storebot-Google : ce qu'il fait et ce que change son blocage
h1: Storebot-Google : ce qu'il fait et ce que change son blocage
description: Storebot-Google (Google) : recherche. Jeton robots.txt, effet d'un Disallow et vérification d'une requête, lus sur la page de l'opérateur.
slug: storebot-google
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur Storebot-Google : opérateur Google, rôle Recherche, respecte robots.txt Oui, liste d'adresses 317 plages
hero_sub: Storebot-Google, géré par Google
hero_boxes: Opérateur|Google; Rôle|Recherche; Respecte robots.txt|Oui; Liste d'adresses|317 plages
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/googlebot|Googlebot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: Storebot-Google est le robot d’exploration que Google documente sous le nom Google StoreBot parmi ses robots d’exploration courants. Google indique qu’un Disallow adressé à son jeton affecte toutes les surfaces de Google Shopping, comme l’onglet Shopping de Google Search et Google Shopping. Googlebot est un jeton distinct, avec ses propres produits concernés.

## Ce qu'est Storebot-Google

Storebot-Google est le robot d’exploration de Google documenté sous le nom Google StoreBot parmi ses robots d’exploration courants. Google indique que les règles qui lui sont adressées affectent toutes les surfaces de Google Shopping. Google liste pour lui des chaînes de user agent distinctes pour ordinateur et mobile.

| Fait | Storebot-Google |
| --- | --- |
| Opérateur | Google |
| Rôle | Recherche (surfaces de Google Shopping) |
| Jeton robots.txt | `Storebot-Google` |
| Respecte robots.txt | Oui. Google indique que les robots d’exploration courants respectent toujours les règles robots.txt lors d’une exploration automatique. |
| Adresses IP | 317 plages (developers.google.com/static/crawling/ipranges/common-crawlers.json, fichier daté du 2026-10-23) |
| Page de l'opérateur lue le | 24 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “Crawling preferences addressed to the Storebot-Google user agent affect all surfaces of Google Shopping”

Source : [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers), lu le 24 octobre 2026.

## Que se passe-t-il si vous bloquez Storebot-Google

Google indique qu’un Disallow adressé au jeton Storebot-Google affecte toutes les surfaces de Google Shopping, comme l’onglet Shopping de Google Search et Google Shopping. La page liste Googlebot comme un jeton distinct, avec ses propres produits concernés.

## Les lignes robots.txt

Pour autoriser Storebot-Google :

```
User-agent: Storebot-Google
Allow: /
```

Pour bloquer Storebot-Google :

```
User-agent: Storebot-Google
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
Mozilla/5.0 (X11; Linux x86_64; Storebot-Google/1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z Safari/537.36
```

## Comment distinguer une vraie requête d'une fausse

Le fichier developers.google.com/static/crawling/ipranges/common-crawlers.json contenait 317 plages le 24 octobre 2026, fichier daté du 2026-10-23.

Google indique que les robots d’exploration courants explorent généralement depuis les plages de common-crawlers.json, et que le nom DNS inverse correspond à crawl-***-***-***-***.googlebot.com ou geo-crawl-***-***-***-***.geo.googlebot.com.

## À comparer avec Googlebot

[Googlebot](/fr/bots/googlebot) : Les règles de Googlebot affectent Google Search et les produits associés, tandis que celles de Storebot-Google affectent les surfaces de Google Shopping.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). Storebot-Google n'en fait pas partie : lisez votre robots.txt pour un groupe `Storebot-Google` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Storebot-Google respecte-t-il robots.txt ?

Oui. Google indique que les robots d’exploration courants respectent toujours les règles robots.txt lors d’une exploration automatique. Donnez à Storebot-Google son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si Storebot-Google est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers)
- [Google: common-crawlers.json (read 2026-10-24, creationTime 2026-10-23)](https://developers.google.com/static/crawling/ipranges/common-crawlers.json)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
