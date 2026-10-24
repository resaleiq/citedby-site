title: PerplexityBot : ce qu'il fait et ce que change son blocage
h1: PerplexityBot : ce qu'il fait et ce que change son blocage
description: PerplexityBot (Perplexity) : recherche. Jeton robots.txt, effet d'un Disallow et vérification d'une requête, lus sur la page de l'opérateur.
slug: perplexitybot
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Quatre faits sur PerplexityBot : opérateur Perplexity, rôle Recherche, respecte robots.txt Oui, liste d'adresses 8 plages
hero_sub: PerplexityBot, géré par Perplexity
hero_boxes: Opérateur|Perplexity; Rôle|Recherche; Respecte robots.txt|Oui; Liste d'adresses|8 plages
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/perplexity-user|Perplexity-User; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: PerplexityBot est le robot d’exploration de Perplexity pour faire apparaître des sites web dans ses résultats de recherche et renvoyer vers eux. Perplexity indique qu’il n’est pas utilisé pour explorer du contenu destiné à des modèles d’IA de fondation. Il suit robots.txt, les changements peuvent prendre jusqu’à 24 heures, et Perplexity publie 8 plages d’IP pour lui.

## Ce qu'est PerplexityBot

Perplexity nomme deux agents. PerplexityBot construit l’index de recherche ; Perplexity-User visite une page quand une personne le demande. La page de Perplexity contient des consignes de configuration pour les fournisseurs de WAF courants, parce qu’un pare-feu peut arrêter le robot avant que robots.txt n’entre en jeu.

| Fait | PerplexityBot |
| --- | --- |
| Opérateur | Perplexity |
| Rôle | Recherche |
| Jeton robots.txt | `PerplexityBot` |
| Respecte robots.txt | Oui, il suit robots.txt |
| Adresses IP | 8 plages (perplexity.com/perplexitybot.json, fichier daté du 2025-02-07) |
| Page de l'opérateur lue le | 21 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “PerplexityBot is designed to surface and link websites in search results on Perplexity. It is not used to crawl content for AI foundation models.”

Source : [Perplexity: Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers), lu le 21 octobre 2026.

## Que se passe-t-il si vous bloquez PerplexityBot

Perplexity recommande d’autoriser PerplexityBot dans robots.txt et d’autoriser les requêtes provenant de ses plages d’IP publiées si vous voulez apparaître dans ses résultats de recherche. Elle précise aussi que les changements apportés à votre robots.txt peuvent prendre jusqu’à 24 heures pour être pris en compte dans ses systèmes : un contrôle fait une heure après une modification ne prouve donc pas grand-chose.

## Les lignes robots.txt

Pour autoriser PerplexityBot :

```
User-agent: PerplexityBot
Allow: /
```

Pour bloquer PerplexityBot :

```
User-agent: PerplexityBot
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)
```

## Comment distinguer une vraie requête d'une fausse

Le fichier de Perplexity à perplexity.com/perplexitybot.json contenait 8 préfixes le 21 octobre 2026, avec une date de création au 2025-02-07. Sa section WAF suggère une règle qui combine le user agent et la condition d’IP, afin qu’une requête qui revendique le nom depuis une autre adresse ne passe pas.

## À comparer avec Perplexity-User

[Perplexity-User](/fr/bots/perplexity-user) : L’agent de récupération déclenchée par l’utilisateur ; Perplexity indique qu’il ignore généralement robots.txt.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste PerplexityBot avec une requête réelle et lit robots.txt pour lui. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### PerplexityBot respecte-t-il robots.txt ?

Oui, il suit robots.txt. Donnez à PerplexityBot son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si PerplexityBot est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Perplexity: Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers)
- [perplexity.com/perplexitybot.json](https://www.perplexity.ai/perplexitybot.json)
