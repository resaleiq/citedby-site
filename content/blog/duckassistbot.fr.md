title: DuckAssistBot : ce qu'il fait et ce que change son blocage
h1: DuckAssistBot : ce qu'il fait et ce que change son blocage
description: DuckAssistBot (DuckDuckGo) : récupération déclenchée par l'utilisateur. Jeton robots.txt, effet d'un Disallow et vérification d'une requête.
slug: duckassistbot
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Quatre faits sur DuckAssistBot : opérateur DuckDuckGo, rôle Récupération déclenchée par l'utilisateur, respecte robots.txt Oui, liste d'adresses 486 adresses
hero_sub: DuckAssistBot, géré par DuckDuckGo
hero_boxes: Opérateur|DuckDuckGo; Rôle|Récupération déclenchée par l'utilisateur; Respecte robots.txt|Oui; Liste d'adresses|486 adresses
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/amazonbot|Amazonbot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: DuckAssistBot explore des pages en temps réel pour les réponses assistées par IA de DuckDuckGo, qui citent leurs sources. DuckDuckGo indique que ces données ne servent pas à entraîner des modèles d’IA. Un Disallow dans robots.txt prend effet après 72 heures et n’affecte pas le classement dans la recherche organique. Il liste 486 adresses IP.

## Ce qu'est DuckAssistBot

DuckDuckGo exploite deux robots que l’on confond. DuckDuckBot est le robot de recherche ; DuckAssistBot est celui qui se trouve derrière les réponses assistées par IA. La page d’aide de DuckDuckGo indique que les réponses citent leurs sources de façon bien visible et que les données explorées ne servent pas à entraîner des modèles d’IA.

| Fait | DuckAssistBot |
| --- | --- |
| Opérateur | DuckDuckGo |
| Rôle | Récupération en temps réel pour les réponses assistées par IA |
| Jeton robots.txt | `DuckAssistBot` |
| Respecte robots.txt | Oui, un changement prend effet après 72 heures |
| Adresses IP | 486 adresses (duckduckgo.com/duckassistbot.json, fichier daté du 2026-09-01) |
| Page de l'opérateur lue le | 21 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “DuckAssistBot is a web crawler for DuckDuckGo Search that crawls pages in real-time for our AI-assisted answers, which prominently cite their sources. This data is not used in any way to train AI models.”

Source : [DuckDuckGo Help Pages: About DuckAssistBot](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot), lu le 21 octobre 2026.

## Que se passe-t-il si vous bloquez DuckAssistBot

DuckDuckGo indique qu’une fois DuckAssistBot interdit, le changement prend effet après 72 heures, et que le refus n’a pas d’incidence sur le classement dans la recherche organique et n’affecte pas l’apparition des sites dans ses résultats de recherche. Le coût d’un blocage se limite donc aux réponses assistées et à leurs citations. Les problèmes de refus se signalent à l’adresse indiquée par la page, crawling@duckduckgo.com.

## Les lignes robots.txt

Pour autoriser DuckAssistBot :

```
User-agent: DuckAssistBot
Allow: /
```

Pour bloquer DuckAssistBot :

```
User-agent: DuckAssistBot
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
DuckAssistBot/1.2; (+http://duckduckgo.com/duckassistbot.html)
```

## Comment distinguer une vraie requête d'une fausse

DuckDuckGo liste les adresses dans l’article d’aide et en JSON sur duckduckgo.com/duckassistbot.json. Le fichier contenait 486 entrées le 21 octobre 2026, avec une date de création au 2026-09-01, soit plus que toute autre liste d’adresses que nous avons comptée pour cet ensemble, et il contient des adresses uniques là où les autres publient des plages CIDR. Le user agent apparaît sous la forme `DuckAssistBot/1.2`.

## À comparer avec Amazonbot

[Amazonbot](/fr/bots/amazonbot) : La famille de trois agents d’Amazon, dont l’un peut ignorer robots.txt.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). DuckAssistBot n'en fait pas partie : lisez votre robots.txt pour un groupe `DuckAssistBot` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### DuckAssistBot respecte-t-il robots.txt ?

Oui, un changement prend effet après 72 heures. Donnez à DuckAssistBot son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si DuckAssistBot est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [DuckDuckGo Help Pages: About DuckAssistBot](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot)
- [duckduckgo.com/duckassistbot.json](https://duckduckgo.com/duckassistbot.json)
