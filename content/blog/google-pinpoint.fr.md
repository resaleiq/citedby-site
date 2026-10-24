title: Google-Pinpoint : ce qu'il fait et ce que change son blocage
h1: Google-Pinpoint : ce qu'il fait et ce que change son blocage
description: Google-Pinpoint (Google) : récupération déclenchée par l'utilisateur. Jeton robots.txt, effet d'un Disallow et vérification d'une requête.
slug: google-pinpoint
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur Google-Pinpoint : opérateur Google, rôle Récupération déclenchée par l'utilisateur, respecte robots.txt Pas toujours, liste d'adresses DNS inversé
hero_sub: Google-Pinpoint, géré par Google
hero_boxes: Opérateur|Google; Rôle|Récupération déclenchée par l'utilisateur; Respecte robots.txt|Pas toujours; Liste d'adresses|DNS inversé
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/google-gemininotebook|Google-GeminiNotebook; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: Google-Pinpoint est un agent de récupération déclenchée par l’utilisateur listé par Google. Il demande des URL individuelles que les utilisateurs de Pinpoint ont indiquées comme sources de leurs collections personnelles de documents. Google indique que ces agents ignorent généralement les règles robots.txt car l’utilisateur a demandé la récupération, et ne documente aucun jeton robots.txt pour lui.

## Ce qu'est Google-Pinpoint

Google-Pinpoint est un agent de récupération déclenchée par l’utilisateur listé par Google. Il demande des URL individuelles que les utilisateurs de Pinpoint ont indiquées comme sources de leurs collections personnelles de documents. Google le liste avec le user agent Google-Pinpoint.

| Fait | Google-Pinpoint |
| --- | --- |
| Opérateur | Google |
| Rôle | Récupération déclenchée par l’utilisateur |
| Jeton robots.txt | `Google-Pinpoint` |
| Respecte robots.txt | Partiel. Google indique que les agents de récupération déclenchée par l’utilisateur ignorent généralement les règles robots.txt, car un utilisateur a demandé la récupération. |
| Adresses IP | Vérification par DNS inversé |
| Page de l'opérateur lue le | 24 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “The Google-Pinpoint fetcher requests individual URLs that Pinpoint users specified as sources for their personal collections of documents.”

Source : [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers), lu le 24 octobre 2026.

## Que se passe-t-il si vous bloquez Google-Pinpoint

Google indique que, la récupération ayant été demandée par un utilisateur, les agents de récupération déclenchée par l’utilisateur ignorent généralement les règles robots.txt. La page de Google ne documente aucun jeton robots.txt pour Google-Pinpoint.

## Les lignes robots.txt

Pour autoriser Google-Pinpoint :

```
User-agent: Google-Pinpoint
Allow: /
```

Pour bloquer Google-Pinpoint :

```
User-agent: Google-Pinpoint
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
Google-Pinpoint
```

## Comment distinguer une vraie requête d'une fausse

Google indique que les agents de récupération déclenchée par l’utilisateur publient leurs plages d’IP dans user-triggered-fetchers.json, user-triggered-fetchers-google.json et user-triggered-agents.json, et que le masque DNS inverse correspond à ***-***-***-***.gae.googleusercontent.com ou google-proxy-***-***-***-***.google.com selon que l’agent appartient à Google ou à l’utilisateur.

## À comparer avec Google-GeminiNotebook

[Google-GeminiNotebook](/fr/bots/google-gemininotebook) : Les deux récupèrent des URL que des utilisateurs ont fournies comme sources dans un produit Google, et les deux relèvent des règles de Google pour les agents de récupération déclenchée par l’utilisateur.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). Google-Pinpoint n'en fait pas partie : lisez votre robots.txt pour un groupe `Google-Pinpoint` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Google-Pinpoint respecte-t-il robots.txt ?

Pas toujours. Partiel. Google indique que les agents de récupération déclenchée par l’utilisateur ignorent généralement les règles robots.txt, car un utilisateur a demandé la récupération. Une règle pour Google-Pinpoint dans robots.txt peut donc ne pas l'arrêter. Pour le refuser à coup sûr, utilisez une règle de pare-feu ou de CDN qui combine le user agent et les adresses publiées.

### Comment savoir si Google-Pinpoint est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
