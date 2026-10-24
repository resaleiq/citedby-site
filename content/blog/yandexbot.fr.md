title: YandexBot : ce qu'il fait et ce que change son blocage
h1: YandexBot : ce qu'il fait et ce que change son blocage
description: YandexBot (Yandex) : recherche. Jeton robots.txt, effet d'un Disallow et vérification d'une requête, lus sur la page de l'opérateur.
slug: yandexbot
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur YandexBot : opérateur Yandex, rôle Recherche, respecte robots.txt Oui, liste d'adresses DNS inversé
hero_sub: YandexBot, géré par Yandex
hero_boxes: Opérateur|Yandex; Rôle|Recherche; Respecte robots.txt|Oui; Liste d'adresses|DNS inversé
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/googlebot|Googlebot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: YandexBot est présenté par Yandex comme son principal robot d’indexation, l’un des nombreux robots de Yandex ayant leurs propres user agents. Yandex indique que certains téléchargent des pages à des fins autres que l’indexation et peuvent ignorer les règles restrictives écrites pour tous les robots (User-agent: *). Yandex ne publie pas de liste d’IP.

## Ce qu'est YandexBot

YandexBot est présenté par Yandex comme le principal robot d’indexation. Yandex exploite de nombreux autres robots avec leurs propres user agents (pour les images, la vidéo, la publicité, les pages mobiles, les favicons et plus), listés sur la même page. Yandex ne publie pas de liste d’IP pour ses robots.

| Fait | YandexBot |
| --- | --- |
| Opérateur | Yandex |
| Rôle | Recherche (principal robot d’indexation) |
| Jeton robots.txt | `Yandex` |
| Respecte robots.txt | Oui, tient compte des règles générales de robots.txt (User-agent: *) |
| Adresses IP | Vérification par DNS inversé |
| Page de l'opérateur lue le | 24 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “Some robots can disguise themselves as Yandex robots by indicating the relevant User Agent. You can check the authenticity of a robot using a reverse DNS lookup.”

Source : [Yandex Webmaster: How to check that a robot belongs to Yandex](https://yandex.com/support/webmaster/en/robot-workings/check-yandex-robots), lu le 24 octobre 2026.

## Que se passe-t-il si vous bloquez YandexBot

Yandex indique qu’un certain nombre de ses robots téléchargent des pages à des fins autres que l’indexation et peuvent ignorer les règles restrictives écrites pour tous les robots (User-agent: *). Pour restreindre ces robots, il faut des directives écrites spécifiquement pour eux, par exemple User-agent: YandexCalendar. Yandex ajoute qu’un document auquel le principal robot de Yandex ne peut pas accéder ne sera jamais indexé ni trouvé dans les résultats de recherche.

## Les lignes robots.txt

Pour autoriser YandexBot :

```
User-agent: Yandex
Allow: /
```

Pour bloquer YandexBot :

```
User-agent: Yandex
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)
```

## Comment distinguer une vraie requête d'une fausse

Yandex indique d’effectuer une recherche DNS inverse sur l’IP, de vérifier que le nom d’hôte se termine par yandex.ru, yandex.net ou yandex.com, puis de confirmer par une recherche directe ; il propose aussi un outil de vérification d’adresse IP.

## À comparer avec Googlebot

[Googlebot](/fr/bots/googlebot) : Les deux sont le principal robot d’indexation de recherche de leur opérateur ; Yandex liste de nombreux robots distincts, dont certains ignorent les règles robots.txt générales, et indique qu’il ne publie pas de liste d’IP.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). YandexBot n'en fait pas partie : lisez votre robots.txt pour un groupe `Yandex` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### YandexBot respecte-t-il robots.txt ?

Oui, tient compte des règles générales de robots.txt (User-agent: *). Donnez à Yandex son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si YandexBot est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Yandex Webmaster: How to check that a robot belongs to Yandex](https://yandex.com/support/webmaster/en/robot-workings/check-yandex-robots)
- [Yandex Webmaster: Using robots.txt](https://yandex.com/support/webmaster/en/controlling-robot/robots-txt)
