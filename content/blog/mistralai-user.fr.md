title: MistralAI-User : ce qu'il fait et ce que change son blocage
h1: MistralAI-User : ce qu'il fait et ce que change son blocage
description: MistralAI-User (Mistral) : récupération déclenchée par l'utilisateur. Jeton robots.txt, effet d'un Disallow et vérification d'une requête.
slug: mistralai-user
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Quatre faits sur MistralAI-User : opérateur Mistral, rôle Récupération déclenchée par l'utilisateur, respecte robots.txt Oui, liste d'adresses 4 plages
hero_sub: MistralAI-User, géré par Mistral
hero_boxes: Opérateur|Mistral; Rôle|Récupération déclenchée par l'utilisateur; Respecte robots.txt|Oui; Liste d'adresses|4 plages
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/chatgpt-user|ChatGPT-User; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: MistralAI-User est l’agent de Mistral qui peut visiter une page quand un utilisateur pose une question à Vibe, et lier la source dans sa réponse. Mistral indique qu’il n’est pas utilisé pour explorer automatiquement ni pour l’entraînement d’IA générative. La page de Mistral liste aussi MistralAI-Index et MistralAI-Training, chacun avec son propre jeton.

## Ce qu'est MistralAI-User

La page des robots de Mistral liste trois agents : MistralAI-User pour les actions d’utilisateurs dans Vibe, MistralAI-Index pour indexer du contenu pour la recherche de Mistral, et MistralAI-Training, qui explore du contenu web pour aider à constituer des jeux de données d’entraînement des modèles d’IA générative de Mistral. Les webmasters peuvent interdire chacun dans robots.txt.

| Fait | MistralAI-User |
| --- | --- |
| Opérateur | Mistral |
| Rôle | Récupération déclenchée par l’utilisateur |
| Jeton robots.txt | `MistralAI-User` |
| Respecte robots.txt | Refus possible via robots.txt |
| Adresses IP | 4 plages (mistral.ai/mistralai-user-ips.json, fichier daté du 2025-02-19) |
| Page de l'opérateur lue le | 21 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “MistralAI-User is for user actions in Vibe. When users ask Vibe a question, it may visit a web page to help answer and include a link to the source in its response.”

Source : [Mistral Docs: Mistral crawlers](https://docs.mistral.ai/robots), lu le 21 octobre 2026.

## Que se passe-t-il si vous bloquez MistralAI-User

Interdire MistralAI-User empêche cet agent d’ouvrir votre page pour la question d’un utilisateur de Vibe ; cela laisse tranquilles les agents d’index et d’entraînement, qui ont leurs propres jetons. Mistral indique que le user agent n’est pas utilisé pour explorer le web de façon automatique, ni pour explorer du contenu pour l’entraînement d’IA générative, et que le contenu exploré par l’agent d’index n’est utilisé pour aucun entraînement d’IA générative.

## Les lignes robots.txt

Pour autoriser MistralAI-User :

```
User-agent: MistralAI-User
Allow: /
```

Pour bloquer MistralAI-User :

```
User-agent: MistralAI-User
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; MistralAI-User/1.0; +https://docs.mistral.ai/robots)
```

## Comment distinguer une vraie requête d'une fausse

Mistral publie des fichiers d’adresses distincts pour les agents. mistral.ai/mistralai-user-ips.json contenait 4 préfixes (date de création 2025-02-19) et le fichier de l’index 2 préfixes (date de création 2026-04-19) le 21 octobre 2026. Deux entrées pour un robot d’index forment une liste qu’une règle de pare-feu peut reprendre exactement.

## À comparer avec ChatGPT-User

[ChatGPT-User](/fr/bots/chatgpt-user) : Le même rôle chez OpenAI, avec une promesse robots.txt différente.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). MistralAI-User n'en fait pas partie : lisez votre robots.txt pour un groupe `MistralAI-User` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### MistralAI-User respecte-t-il robots.txt ?

Refus possible via robots.txt. Donnez à MistralAI-User son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si MistralAI-User est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Mistral Docs: Mistral crawlers](https://docs.mistral.ai/robots)
- [mistral.ai/mistralai-user-ips.json](https://mistral.ai/mistralai-user-ips.json)
