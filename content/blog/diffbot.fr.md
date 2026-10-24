title: Diffbot : ce qu'il fait et ce que change son blocage
h1: Diffbot : ce qu'il fait et ce que change son blocage
description: Diffbot (Diffbot) : recherche. Jeton robots.txt, effet d'un Disallow et vérification d'une requête, lus sur la page de l'opérateur.
slug: diffbot
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur Diffbot : opérateur Diffbot, rôle Recherche, respecte robots.txt Oui, liste d'adresses Aucune
hero_sub: Diffbot, géré par Diffbot
hero_boxes: Opérateur|Diffbot; Rôle|Recherche; Respecte robots.txt|Oui; Liste d'adresses|Aucune
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/bingbot|Bingbot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: Diffbot documente deux user agents. Diffbot explore le web de façon proactive pour un moteur de recherche généraliste, afin que les sites puissent être découverts et cités depuis son Knowledge Graph. Diffbot-User récupère une URL pour une personne qui utilise son logiciel. Diffbot indique que ses explorations suivent robots.txt par défaut, y compris disallow et crawl-delay.

## Ce qu'est Diffbot

Diffbot documente deux user agents. Diffbot sert à l’exploration générale et proactive du web pour construire un moteur de recherche généraliste, afin que les sites puissent être découverts et cités depuis le Knowledge Graph de Diffbot et ses services de recherche web. Diffbot-User sert aux requêtes faites au nom d’un utilisateur humain qui consulte une URL avec le logiciel de Diffbot.

| Fait | Diffbot |
| --- | --- |
| Opérateur | Diffbot |
| Rôle | Recherche (exploration générale du web) |
| Jeton robots.txt | `Diffbot` |
| Respecte robots.txt | Oui, par défaut (directives disallow et crawl-delay) |
| Adresses IP | Aucune publiée |
| Page de l'opérateur lue le | 24 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “By default Diffbot's web crawls adhere to a site’s robots.txt instructions, including the disallow and crawl-delay directives.”

Source : [Diffbot: Does Diffbot respect robots.txt?](https://www.diffbot.com/docs/crawl/faq/robots-txt), lu le 24 octobre 2026.

## Que se passe-t-il si vous bloquez Diffbot

Diffbot indique que ses explorations web suivent robots.txt par défaut, y compris disallow et crawl-delay, et qu’une règle peut être levée dans des cas précis, comme un partenariat ou un accord avec le site. Il liste Diffbot et Diffbot-User comme des user agents distincts, et précise que les utilisateurs de ses API Extract et Crawlbot définissent leurs propres paramètres d’exploration et peuvent définir leur propre User-Agent.

## Les lignes robots.txt

Pour autoriser Diffbot :

```
User-agent: Diffbot
Allow: /
```

Pour bloquer Diffbot :

```
User-agent: Diffbot
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
Diffbot
```

## Comment distinguer une vraie requête d'une fausse

La page de l’opérateur ne décrit ni liste d’IP ni méthode de vérification.

## À comparer avec Bingbot

[Bingbot](/fr/bots/bingbot) : L’opérateur décrit Diffbot comme semblable à Googlebot et à Bing, un robot généraliste pour un index de recherche, et indique qu’il n’est pas utilisé pour l’entraînement d’IA.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). Diffbot n'en fait pas partie : lisez votre robots.txt pour un groupe `Diffbot` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Diffbot respecte-t-il robots.txt ?

Oui, par défaut (directives disallow et crawl-delay). Donnez à Diffbot son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si Diffbot est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Diffbot: Does Diffbot respect robots.txt? (read 2026-10-24)](https://www.diffbot.com/docs/crawl/faq/robots-txt)
