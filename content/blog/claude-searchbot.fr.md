title: Claude-SearchBot : ce qu'il fait et ce que change son blocage
h1: Claude-SearchBot : ce qu'il fait et ce que change son blocage
description: Claude-SearchBot (Anthropic) : recherche. Jeton robots.txt, effet d'un Disallow et vérification d'une requête, lus sur la page de l'opérateur.
slug: claude-searchbot
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Quatre faits sur Claude-SearchBot : opérateur Anthropic, rôle Recherche, respecte robots.txt Oui, liste d'adresses Liste, pas pour bloquer
hero_sub: Claude-SearchBot, géré par Anthropic
hero_boxes: Opérateur|Anthropic; Rôle|Recherche; Respecte robots.txt|Oui; Liste d'adresses|Liste, pas pour bloquer
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/claudebot|ClaudeBot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: Claude-SearchBot est le robot d’Anthropic qui parcourt le web pour améliorer la qualité des résultats de recherche. Anthropic indique que le désactiver empêche l’indexation de votre contenu pour l’optimisation de la recherche, ce qui peut réduire votre visibilité et la précision dans les résultats de recherche des utilisateurs. Son jeton robots.txt est Claude-SearchBot.

## Ce qu'est Claude-SearchBot

Claude-SearchBot est le volet d’indexation de la recherche d’Anthropic. Anthropic le décrit comme analysant le contenu en ligne pour améliorer la pertinence et la précision des réponses de recherche. [ClaudeBot](/fr/bots/claudebot) collecte pour l’entraînement et [Claude-User](/fr/bots/claude-user) répond à une question en direct.

| Fait | Claude-SearchBot |
| --- | --- |
| Opérateur | Anthropic |
| Rôle | Recherche |
| Jeton robots.txt | `Claude-SearchBot` |
| Respecte robots.txt | Oui, Anthropic indique que ses robots respectent robots.txt |
| Adresses IP | L'opérateur renvoie à une liste mais déconseille le blocage par IP |
| Page de l'opérateur lue le | 21 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “Claude-SearchBot navigates the web to improve search result quality for users. It analyzes online content specifically to enhance the relevance and accuracy of search responses. Disabling Claude-SearchBot on your site prevents our system from indexing your content for search optimization, which may reduce your site's visibility and accuracy in user search results.”

Source : [Anthropic Help Center: Does Anthropic crawl data from the web, and how can site owners block the crawler? (7 April 2026)](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler), lu le 21 octobre 2026.

## Que se passe-t-il si vous bloquez Claude-SearchBot

Anthropic nomme deux effets si vous le désactivez : votre contenu n’est pas indexé pour l’optimisation de la recherche, et la visibilité et la précision de votre site dans les résultats de recherche des utilisateurs peuvent baisser.

## Les lignes robots.txt

Pour autoriser Claude-SearchBot :

```
User-agent: Claude-SearchBot
Allow: /
```

Pour bloquer Claude-SearchBot :

```
User-agent: Claude-SearchBot
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La page de l'opérateur n'indique pas de chaîne user-agent complète pour Claude-SearchBot.

## Comment distinguer une vraie requête d'une fausse

L’article d’aide est daté du 7 avril 2026. Il ne donne aucune chaîne de user agent : une ligne du journal de serveur qui nomme Claude-SearchBot est donc une affirmation que l’article seul ne permet pas de confirmer. Anthropic indique que le trafic provenant d’une adresse de sa liste liée est celui d’Anthropic, et demande aux propriétaires de sites qui pensent qu’un robot se comporte mal d’écrire depuis une adresse e-mail du domaine concerné.

## À comparer avec ClaudeBot

[ClaudeBot](/fr/bots/claudebot) : Bloquer ClaudeBot exclut seulement de l’entraînement ; cela ne vous retire pas de l’index de recherche de Claude.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). Claude-SearchBot n'en fait pas partie : lisez votre robots.txt pour un groupe `Claude-SearchBot` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Claude-SearchBot respecte-t-il robots.txt ?

Oui, Anthropic indique que ses robots respectent robots.txt. Donnez à Claude-SearchBot son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si Claude-SearchBot est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Anthropic Help Center: Does Anthropic crawl data from the web, and how can site owners block the crawler? (7 April 2026)](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)
