title: Applebot-Extended : ce qu'il fait et ce que change son blocage
h1: Applebot-Extended : ce qu'il fait et ce que change son blocage
description: Applebot-Extended (Apple) : jeton de contrôle. Jeton robots.txt, effet d'un Disallow et vérification d'une requête, lus sur la page de l'opérateur.
slug: applebot-extended
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Quatre faits sur Applebot-Extended : opérateur Apple, rôle Jeton de contrôle, respecte robots.txt Lu dans robots.txt seulement, liste d'adresses Aucune
hero_sub: Applebot-Extended, géré par Apple
hero_boxes: Opérateur|Apple; Rôle|Jeton de contrôle; Respecte robots.txt|Lu dans robots.txt seulement; Liste d'adresses|Aucune
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/applebot|Applebot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: Applebot-Extended est un jeton robots.txt. Apple indique que les éditeurs peuvent refuser que leur contenu serve à entraîner ses modèles de fondation génératifs en l’interdisant. Applebot peut tout de même explorer la page, de sorte que le contenu reste repérable dans Spotlight, Siri et Safari. Il n’envoie aucune requête de lui-même.

## Ce qu'est Applebot-Extended

La page d’Apple décrit Applebot-Extended comme le moyen d’exclure du contenu de l’entraînement des modèles de fondation qui sous-tendent Apple Intelligence, les services et les outils pour développeurs. Comme [Google-Extended](/fr/bots/google-extended), c’est un jeton de contrôle : vous ne le trouverez pas dans votre journal de serveur.

| Fait | Applebot-Extended |
| --- | --- |
| Opérateur | Apple |
| Rôle | Jeton de contrôle (aucune requête propre) |
| Jeton robots.txt | `Applebot-Extended` |
| Respecte robots.txt | Lu dans robots.txt seulement |
| Adresses IP | Aucune : il ne récupère jamais de page |
| Page de l'opérateur lue le | 21 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “Web publishers can opt-out from having their content used to train generative foundation models by disallowing Applebot-Extended in the robots.txt file.”

Source : [Apple Support: About Applebot](https://support.apple.com/en-us/119829), lu le 21 octobre 2026.

## Que se passe-t-il si vous bloquez Applebot-Extended

Apple précise la limite : si vous interdisez Applebot-Extended et marquez aussi le contenu avec la balise meta nosnippet, vos instructions peuvent quand même permettre à Applebot d’explorer la page, et le contenu reste repérable via Spotlight, Siri et Safari. La même page indique que les éditeurs peuvent refuser l’utilisation de leur contenu dans les réponses de connaissance générale du monde en appliquant ce contrôle robots.txt.

## Les lignes robots.txt

Pour autoriser Applebot-Extended :

```
User-agent: Applebot-Extended
Allow: /
```

Pour bloquer Applebot-Extended :

```
User-agent: Applebot-Extended
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

## Comment distinguer une vraie requête d'une fausse

Aucun contrôle réseau n’existe pour un jeton qui n’envoie aucune requête. Lisez robots.txt, sur chaque hôte, et vérifiez Applebot séparément, car les deux jetons sont indépendants et un simple groupe `User-agent: Applebot-Extended` ne dit rien d’Applebot.

Applebot-Extended n'envoie aucune requête lui-même : il n'apparaît donc jamais dans votre journal de serveur. Il est seulement lu dans robots.txt.

## À comparer avec Applebot

[Applebot](/fr/bots/applebot) : Le robot d’exploration lui-même : l’autoriser vous garde dans la recherche Spotlight, Siri et Safari.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). Applebot-Extended n'en fait pas partie : lisez votre robots.txt pour un groupe `Applebot-Extended` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Applebot-Extended respecte-t-il robots.txt ?

Lu dans robots.txt seulement. Il n'envoie aucune requête lui-même : il n'y a rien à bloquer au pare-feu, la règle dans robots.txt est le seul moyen de contrôle.

### Comment savoir si Applebot-Extended est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Apple Support: About Applebot](https://support.apple.com/en-us/119829)
