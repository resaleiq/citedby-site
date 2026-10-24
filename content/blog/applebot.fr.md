title: Applebot : ce qu'il fait et ce que change son blocage
h1: Applebot : ce qu'il fait et ce que change son blocage
description: Applebot (Apple) : plusieurs rôles. Jeton robots.txt, effet d'un Disallow et vérification d'une requête, lus sur la page de l'opérateur.
slug: applebot
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur Applebot : opérateur Apple, rôle Plusieurs rôles, respecte robots.txt Oui, liste d'adresses 24 plages
hero_sub: Applebot, géré par Apple
hero_boxes: Opérateur|Apple; Rôle|Plusieurs rôles; Respecte robots.txt|Oui; Liste d'adresses|24 plages
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/applebot-extended|Applebot-Extended; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: Applebot est le robot d’exploration web d’Apple. Apple indique que ses données alimentent la recherche dans Spotlight, Siri et Safari et peuvent aussi aider à entraîner les modèles de fondation d’Apple. Interdire Applebot-Extended exclut le contenu de l’entraînement uniquement. Si robots.txt ne mentionne pas Applebot mais mentionne Googlebot, Applebot suit les règles de Googlebot.

## Ce qu'est Applebot

Applebot est le robot d’exploration web d’Apple. Apple indique que ses données alimentent la technologie de recherche de Spotlight, Siri et Safari, et peuvent aussi servir à entraîner les modèles de fondation d’Apple et à fournir du contexte lorsque des modèles d’IA génèrent des résultats dans les produits Apple. Apple documente aussi un jeton distinct, Applebot-Extended, et un user agent iTMS pour Apple Podcasts.

| Fait | Applebot |
| --- | --- |
| Opérateur | Apple |
| Rôle | Recherche (les données explorées peuvent aussi aider à entraîner des modèles d’Apple) |
| Jeton robots.txt | `Applebot` |
| Respecte robots.txt | Oui, pour les explorations de recherche générales destinées à Applebot |
| Adresses IP | 24 plages (search.developer.apple.com/applebot.json, fichier daté du 2026-09-15) |
| Page de l'opérateur lue le | 24 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “Applebot respects standard robots.txt directives in general search crawls that are targeted at Applebot.”

Source : [Apple: About Applebot](https://support.apple.com/en-us/119829), lu le 24 octobre 2026.

## Que se passe-t-il si vous bloquez Applebot

Apple indique qu’interdire Applebot-Extended exclut le contenu de l’entraînement des modèles de fondation génératifs d’Apple, mais que le site peut quand même être exploré par Applebot et rester repérable via Spotlight, Siri et Safari. Un Disallow pour Applebot lui-même s’applique aux explorations de recherche générales destinées à Applebot, et Apple indique que si robots.txt ne mentionne pas Applebot mais mentionne Googlebot, Applebot suit les instructions de Googlebot. Apple indique que la balise meta nosnippet exclut le contenu des réponses de connaissance générale du monde.

## Les lignes robots.txt

Pour autoriser Applebot :

```
User-agent: Applebot
Allow: /
```

Pour bloquer Applebot :

```
User-agent: Applebot
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15 (Applebot/0.1; +http://www.apple.com/go/applebot)
```

## Comment distinguer une vraie requête d'une fausse

Le fichier search.developer.apple.com/applebot.json contenait 24 plages le 24 octobre 2026, fichier daté du 2026-09-15.

Apple indique que le trafic d’Applebot est généralement identifié par DNS inverse dans le domaine *.applebot.apple.com, ou en faisant correspondre l’adresse IP à un préfixe CIDR de son fichier JSON publié.

## À comparer avec Applebot-Extended

[Applebot-Extended](/fr/bots/applebot-extended) : Applebot est le robot qui récupère les pages pour les fonctions de recherche d’Apple, tandis qu’Applebot-Extended est le jeton robots.txt qui détermine si le contenu exploré sert à entraîner les modèles génératifs d’Apple.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). Applebot n'en fait pas partie : lisez votre robots.txt pour un groupe `Applebot` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Applebot respecte-t-il robots.txt ?

Oui, pour les explorations de recherche générales destinées à Applebot. Donnez à Applebot son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si Applebot est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Apple: About Applebot](https://support.apple.com/en-us/119829)
- [Apple: Applebot IP CIDRs JSON (read 2026-10-24)](https://search.developer.apple.com/applebot.json)
