title: Google-GeminiNotebook : rôle et effet d'un blocage
h1: Google-GeminiNotebook : rôle et effet d'un blocage
description: Google-GeminiNotebook (Google) : récupération déclenchée par l'utilisateur. Jeton robots.txt, effet d'un Disallow et vérification d'une requête.
slug: google-gemininotebook
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur Google-GeminiNotebook : opérateur Google, rôle Récupération déclenchée par l'utilisateur, respecte robots.txt Pas toujours, liste d'adresses DNS inversé
hero_sub: Google-GeminiNotebook, géré par Google
hero_boxes: Opérateur|Google; Rôle|Récupération déclenchée par l'utilisateur; Respecte robots.txt|Pas toujours; Liste d'adresses|DNS inversé
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/chatgpt-user|ChatGPT-User; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: Google-GeminiNotebook est le user agent de l’agent de récupération de Gemini Notebook. Il demande des URL individuelles que les utilisateurs ont ajoutées comme sources de leurs projets. Google le range parmi les agents de récupération déclenchée par l’utilisateur, qui ignorent généralement robots.txt car l’utilisateur a demandé la récupération. La page de Google nomme Google-NotebookLM comme ancien agent.

## Ce qu'est Google-GeminiNotebook

Google-GeminiNotebook est le user agent de l’agent de récupération de Gemini Notebook, que Google range parmi ses agents de récupération déclenchée par l’utilisateur. Il demande des URL individuelles que les utilisateurs ont fournies comme sources de leurs projets. La page de Google nomme Google-NotebookLM comme ancien agent, pris en charge jusqu’en août 2026.

| Fait | Google-GeminiNotebook |
| --- | --- |
| Opérateur | Google |
| Rôle | Récupération déclenchée par l’utilisateur |
| Jeton robots.txt | `Google-GeminiNotebook` |
| Respecte robots.txt | Partiel. Google indique que les agents de récupération déclenchée par l’utilisateur ignorent généralement les règles robots.txt, car un utilisateur a demandé la récupération. |
| Adresses IP | Vérification par DNS inversé |
| Page de l'opérateur lue le | 24 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “The Gemini Notebook fetcher requests individual URLs that Gemini Notebook users have provided as sources for their projects.”

Source : [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers), lu le 24 octobre 2026.

## Que se passe-t-il si vous bloquez Google-GeminiNotebook

Google indique que, la récupération ayant été demandée par un utilisateur, les agents de récupération déclenchée par l’utilisateur ignorent généralement les règles robots.txt. La page de Google ne documente aucun jeton robots.txt pour cet agent.

## Les lignes robots.txt

Pour autoriser Google-GeminiNotebook :

```
User-agent: Google-GeminiNotebook
Allow: /
```

Pour bloquer Google-GeminiNotebook :

```
User-agent: Google-GeminiNotebook
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 (compatible; Google-GeminiNotebook; +https://developers.google.com/crawling/docs/crawlers-fetchers/google-gemininotebook)
```

## Comment distinguer une vraie requête d'une fausse

Google indique que les agents de récupération déclenchée par l’utilisateur publient leurs plages d’IP dans user-triggered-fetchers.json, user-triggered-fetchers-google.json et user-triggered-agents.json, et que le masque DNS inverse correspond à ***-***-***-***.gae.googleusercontent.com ou google-proxy-***-***-***-***.google.com selon que l’agent appartient à Google ou à l’utilisateur.

## À comparer avec ChatGPT-User

[ChatGPT-User](/fr/bots/chatgpt-user) : Les deux récupèrent des URL individuelles parce qu’un utilisateur a demandé à un produit d’assistant de les utiliser, et les deux opérateurs indiquent que ces récupérations peuvent ne pas suivre les règles robots.txt.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). Google-GeminiNotebook n'en fait pas partie : lisez votre robots.txt pour un groupe `Google-GeminiNotebook` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Google-GeminiNotebook respecte-t-il robots.txt ?

Pas toujours. Partiel. Google indique que les agents de récupération déclenchée par l’utilisateur ignorent généralement les règles robots.txt, car un utilisateur a demandé la récupération. Une règle pour Google-GeminiNotebook dans robots.txt peut donc ne pas l'arrêter. Pour le refuser à coup sûr, utilisez une règle de pare-feu ou de CDN qui combine le user agent et les adresses publiées.

### Comment savoir si Google-GeminiNotebook est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
