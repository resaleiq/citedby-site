title: ExaSearchBot : ce qu'il fait et ce que change son blocage
h1: ExaSearchBot : ce qu'il fait et ce que change son blocage
description: ExaSearchBot (Exa) : recherche. Jeton robots.txt, effet d'un Disallow et vérification d'une requête, lus sur la page de l'opérateur.
slug: exasearchbot
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur ExaSearchBot : opérateur Exa, rôle Recherche, respecte robots.txt Oui, liste d'adresses Outil de vérification
hero_sub: ExaSearchBot, géré par Exa
hero_boxes: Opérateur|Exa; Rôle|Recherche; Respecte robots.txt|Oui; Liste d'adresses|Outil de vérification
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/perplexitybot|PerplexityBot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: ExaSearchBot est le robot d’exploration d’Exa, un moteur de recherche conçu pour la recherche et la récupération, afin que les pages puissent être découvertes et citées. Exa indique qu’il vérifie robots.txt avant de récupérer et que User-agent: ExaSearchBot avec Disallow: / bloque tout le site. Chaque requête est signée cryptographiquement, donc la vérification ne dépend pas d’une adresse IP.

## Ce qu'est ExaSearchBot

ExaSearchBot est le robot d’exploration d’Exa, un moteur de recherche. Exa indique que son but est la recherche et la récupération, afin que les pages soient repérables et puissent être citées. Les pages qu’Exa récupère à la demande d’un utilisateur plutôt que par exploration partent sous le nom ExaUser.

| Fait | ExaSearchBot |
| --- | --- |
| Opérateur | Exa |
| Rôle | Index de recherche et de récupération |
| Jeton robots.txt | `ExaSearchBot` |
| Respecte robots.txt | Oui, l’opérateur indique qu’il vérifie robots.txt avant de récupérer une page |
| Adresses IP | Outil de vérification |
| Page de l'opérateur lue le | 24 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “Exa is a search engine. Similar to other search engines, Exa uses a robot (ExaSearchBot) to discover and index pages on the public web.”

Source : [Exa: Exa Search Crawler](https://crawler.exa.ai/), lu le 24 octobre 2026.

## Que se passe-t-il si vous bloquez ExaSearchBot

Exa indique que User-agent: ExaSearchBot avec Disallow: / bloque ExaSearchBot sur tout le site. S’il n’existe pas de groupe ExaSearchBot, il suit les règles définies pour les grands moteurs de recherche, sinon le groupe *. L’opérateur indique que robots.txt contrôle l’exploration, pas l’indexation : les pages déjà indexées se retirent donc avec une balise meta noindex ou un en-tête X-Robots-Tag.

## Les lignes robots.txt

Pour autoriser ExaSearchBot :

```
User-agent: ExaSearchBot
Allow: /
```

Pour bloquer ExaSearchBot :

```
User-agent: ExaSearchBot
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
Mozilla/5.0 (compatible; ExaSearchBot/1.0; +https://crawler.exa.ai/)
```

## Comment distinguer une vraie requête d'une fausse

L’opérateur indique que chaque requête est signée cryptographiquement avec HTTP Message Signatures (Web Bot Auth) et fournit un répertoire de clés publiques pour la vérification, et que la vérification vaut quelle que soit l’adresse IP.

## À comparer avec PerplexityBot

[PerplexityBot](/fr/bots/perplexitybot) : Les deux sont des robots d’index de recherche qui alimentent des réponses IA avec des sources citées ; ExaSearchBot signe ses requêtes avec Web Bot Auth et se rabat sur les règles des grands moteurs de recherche quand il n’a pas de groupe à lui.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). ExaSearchBot n'en fait pas partie : lisez votre robots.txt pour un groupe `ExaSearchBot` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### ExaSearchBot respecte-t-il robots.txt ?

Oui, l’opérateur indique qu’il vérifie robots.txt avant de récupérer une page. Donnez à ExaSearchBot son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si ExaSearchBot est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Exa: Exa Search Crawler](https://crawler.exa.ai/)
- [Exa: FAQs](https://exa.ai/docs/admin/faqs)
