title: DuckDuckBot : ce qu'il fait et ce que change son blocage
h1: DuckDuckBot : ce qu'il fait et ce que change son blocage
description: DuckDuckBot (DuckDuckGo) : recherche. Jeton robots.txt, effet d'un Disallow et vérification d'une requête, lus sur la page de l'opérateur.
slug: duckduckbot
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur DuckDuckBot : opérateur DuckDuckGo, rôle Recherche, respecte robots.txt Oui, liste d'adresses 486 adresses
hero_sub: DuckDuckBot, géré par DuckDuckGo
hero_boxes: Opérateur|DuckDuckGo; Rôle|Recherche; Respecte robots.txt|Oui; Liste d'adresses|486 adresses
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/duckassistbot|DuckAssistBot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: DuckDuckBot est le robot d’exploration de DuckDuckGo, dont la mission déclarée est d’améliorer les résultats de recherche de DuckDuckGo. DuckDuckGo indique qu’il respecte WWW::RobotRules et publie ses adresses IP sous forme de liste JSON. DuckAssistBot, qui récupère les pages pour les réponses assistées par IA, est documenté sur une autre page d’aide de DuckDuckGo.

## Ce qu'est DuckDuckBot

DuckDuckBot est le robot d’exploration de DuckDuckGo. DuckDuckGo indique que sa mission est d’améliorer les résultats de recherche de DuckDuckGo. Les pages d’aide de DuckDuckGo présentent DuckAssistBot sur une page distincte.

| Fait | DuckDuckBot |
| --- | --- |
| Opérateur | DuckDuckGo |
| Rôle | Recherche |
| Jeton robots.txt | `DuckDuckBot` |
| Respecte robots.txt | Oui, respecte WWW::RobotRules (aucune indication de délai publiée) |
| Adresses IP | 486 adresses (duckduckgo.com/duckduckbot.json, fichier daté du 2026-09-01) |
| Page de l'opérateur lue le | 24 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “DuckDuckBot’s job is to constantly improve our search results and offer users the best and most secure search experience possible.”

Source : [DuckDuckGo Help Pages: Is DuckDuckBot related to DuckDuckGo?](https://duckduckgo.com/duckduckgo-help-pages/results/duckduckbot), lu le 24 octobre 2026.

## Que se passe-t-il si vous bloquez DuckDuckBot

DuckDuckGo indique que DuckDuckBot respecte WWW::RobotRules : une règle Disallow adressée à DuckDuckBot dans robots.txt s’applique donc à ce robot. La page ne dit rien de ce que change son blocage dans les résultats de DuckDuckGo, ni rien sur DuckAssistBot.

## Les lignes robots.txt

Pour autoriser DuckDuckBot :

```
User-agent: DuckDuckBot
Allow: /
```

Pour bloquer DuckDuckBot :

```
User-agent: DuckDuckBot
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
DuckDuckBot/1.1; (+http://duckduckgo.com/duckduckbot.html)
```

## Comment distinguer une vraie requête d'une fausse

Le fichier duckduckgo.com/duckduckbot.json contenait 486 adresses le 24 octobre 2026, fichier daté du 2026-09-01.

DuckDuckGo indique que le robot provient des adresses IP listées sur sa page d’aide, aussi disponibles en JSON sur duckduckgo.com/duckduckbot.json.

## À comparer avec DuckAssistBot

[DuckAssistBot](/fr/bots/duckassistbot) : DuckDuckBot est le robot d’exploration des résultats de recherche de DuckDuckGo, tandis que DuckAssistBot est documenté par DuckDuckGo sur sa propre page d’aide.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). DuckDuckBot n'en fait pas partie : lisez votre robots.txt pour un groupe `DuckDuckBot` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### DuckDuckBot respecte-t-il robots.txt ?

Oui, respecte WWW::RobotRules (aucune indication de délai publiée). Donnez à DuckDuckBot son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si DuckDuckBot est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [DuckDuckGo Help Pages: Is DuckDuckBot related to DuckDuckGo?](https://duckduckgo.com/duckduckgo-help-pages/results/duckduckbot)
- [DuckDuckBot IP list (JSON, creationTime 2026-09-01, read 2026-10-24)](https://duckduckgo.com/duckduckbot.json)
