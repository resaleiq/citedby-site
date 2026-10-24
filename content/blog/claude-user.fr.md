title: Claude-User : ce qu'il fait et ce que change son blocage
h1: Claude-User : ce qu'il fait et ce que change son blocage
description: Claude-User (Anthropic) : récupération déclenchée par l'utilisateur. Jeton robots.txt, effet d'un Disallow et vérification d'une requête.
slug: claude-user
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Quatre faits sur Claude-User : opérateur Anthropic, rôle Récupération déclenchée par l'utilisateur, respecte robots.txt Oui, liste d'adresses Liste, pas pour bloquer
hero_sub: Claude-User, géré par Anthropic
hero_boxes: Opérateur|Anthropic; Rôle|Récupération déclenchée par l'utilisateur; Respecte robots.txt|Oui; Liste d'adresses|Liste, pas pour bloquer
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/claude-searchbot|Claude-SearchBot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: Claude-User est l’agent que Claude peut utiliser pour accéder à un site web lorsqu’une personne lui pose une question. Anthropic indique que le désactiver empêche la récupération de votre contenu en réponse à une requête d’utilisateur, ce qui peut réduire votre visibilité dans la recherche web dirigée par l’utilisateur. Il est distinct de ClaudeBot et de Claude-SearchBot.

## Ce qu'est Claude-User

Parmi les trois robots d’Anthropic, Claude-User est celui lié à la question d’une personne. Il ne collecte pas de données d’entraînement ([ClaudeBot](/fr/bots/claudebot) le fait) et ne construit pas l’index de recherche ([Claude-SearchBot](/fr/bots/claude-searchbot) le fait).

| Fait | Claude-User |
| --- | --- |
| Opérateur | Anthropic |
| Rôle | Récupération déclenchée par l’utilisateur |
| Jeton robots.txt | `Claude-User` |
| Respecte robots.txt | Oui, Anthropic indique que ses robots respectent robots.txt |
| Adresses IP | L'opérateur renvoie à une liste mais déconseille le blocage par IP |
| Page de l'opérateur lue le | 21 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “Claude-User supports Claude AI users. When individuals ask questions to Claude, it may access websites using a Claude-User agent. Disabling Claude-User on your site prevents our system from retrieving your content in response to a user query, which may reduce your site's visibility for user-directed web search.”

Source : [Anthropic Help Center: Does Anthropic crawl data from the web, and how can site owners block the crawler? (7 April 2026)](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler), lu le 21 octobre 2026.

## Que se passe-t-il si vous bloquez Claude-User

C’est ici que la formulation d’Anthropic sur le coût est la plus directe : désactiver Claude-User empêche la récupération « en réponse à une requête d’utilisateur » et « peut réduire la visibilité de votre site pour la recherche web dirigée par l’utilisateur ». Une boutique qui le bloque peut rester connue du modèle par d’autres sources, mais Claude ne peut pas ouvrir la page quand on le lui demande.

## Les lignes robots.txt

Pour autoriser Claude-User :

```
User-agent: Claude-User
Allow: /
```

Pour bloquer Claude-User :

```
User-agent: Claude-User
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La page de l'opérateur n'indique pas de chaîne user-agent complète pour Claude-User.

## Comment distinguer une vraie requête d'une fausse

L’article d’aide d’Anthropic n’indique pas de chaîne de user agent pour les trois robots, et précise que ses adresses IP sources figurent sur une liste vers laquelle il renvoie. Comme Anthropic indique aussi que bloquer ces adresses peut empêcher ses robots de lire robots.txt, l’article conseille de contrôler l’accès dans robots.txt plutôt qu’au niveau IP.

## À comparer avec Claude-SearchBot

[Claude-SearchBot](/fr/bots/claude-searchbot) : Robot de qualité de la recherche ; son blocage affecte l’indexation pour la recherche, pas la question en direct d’un utilisateur.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). Claude-User n'en fait pas partie : lisez votre robots.txt pour un groupe `Claude-User` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Claude-User respecte-t-il robots.txt ?

Oui, Anthropic indique que ses robots respectent robots.txt. Donnez à Claude-User son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si Claude-User est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Anthropic Help Center: Does Anthropic crawl data from the web, and how can site owners block the crawler? (7 April 2026)](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)
