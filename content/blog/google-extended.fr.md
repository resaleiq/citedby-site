title: Google-Extended : ce qu'il fait et ce que change son blocage
h1: Google-Extended : ce qu'il fait et ce que change son blocage
description: Google-Extended (Google) : jeton de contrôle. Jeton robots.txt, effet d'un Disallow et vérification d'une requête, lus sur la page de l'opérateur.
slug: google-extended
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Quatre faits sur Google-Extended : opérateur Google, rôle Jeton de contrôle, respecte robots.txt Lu dans robots.txt seulement, liste d'adresses Aucune
hero_sub: Google-Extended, géré par Google
hero_boxes: Opérateur|Google; Rôle|Jeton de contrôle; Respecte robots.txt|Lu dans robots.txt seulement; Liste d'adresses|Aucune
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/googlebot|Googlebot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: Google-Extended est un jeton de produit robots.txt qui permet aux éditeurs de gérer si le contenu exploré par Google peut servir à entraîner les futurs modèles Gemini. Il n’a pas de user agent HTTP propre, donc il n’apparaît jamais dans votre journal de serveur. Google indique qu’il n’affecte ni l’inclusion dans Search ni le classement.

## Ce qu'est Google-Extended

La plupart des pages de cet ensemble décrivent un robot que l’on retrouve dans un journal de serveur. Celui-ci, non. Google indique que Google-Extended « n’a pas de chaîne de user agent de requête HTTP distincte » : l’exploration se fait avec les user agents Google existants, et le jeton robots.txt sert de contrôle.

| Fait | Google-Extended |
| --- | --- |
| Opérateur | Google |
| Rôle | Jeton de contrôle (aucune requête propre) |
| Jeton robots.txt | `Google-Extended` |
| Respecte robots.txt | Lu dans robots.txt seulement ; il n’existe pas de user agent distinct |
| Adresses IP | Aucune : il ne récupère jamais de page |
| Page de l'opérateur lue le | 21 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “Google-Extended is a standalone product token that web publishers can use to manage whether content Google crawls from their sites may be used for training future generations of Gemini models that power Gemini Apps and Vertex AI API for Gemini and for grounding (providing content from the Google Search index to the model at prompt time to improve factuality and relevancy) in Gemini Apps and Grounding with Google Search on Vertex AI. Google-Extended does not impact a site's inclusion in Google Search nor is it used as a ranking signal in Google Search.”

Source : [Google Search Central: Google's common crawlers (last updated 2026-10-15)](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers), lu le 21 octobre 2026.

## Que se passe-t-il si vous bloquez Google-Extended

Ajouter `Disallow: /` sous Google-Extended indique à Google qu’il ne peut pas utiliser le contenu pour entraîner les futurs modèles Gemini qui sous-tendent Gemini Apps et l’API Vertex AI pour Gemini. Google précise aussi que cela n’a pas d’incidence sur l’inclusion dans Google Search et n’est pas un signal de classement. Notre audit lit ce jeton dans robots.txt comme l’un de ses contrôles ; c’est le seul signal qui existe. La page de Google indique aussi que ce jeton gère le grounding (l’ancrage), c’est-à-dire le contenu de l’index Google Search fourni au modèle au moment de la requête.

## Les lignes robots.txt

Pour autoriser Google-Extended :

```
User-agent: Google-Extended
Allow: /
```

Pour bloquer Google-Extended :

```
User-agent: Google-Extended
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

## Comment distinguer une vraie requête d'une fausse

Il n’y a rien à vérifier au niveau du réseau : pas de user agent, pas de liste d’adresses. Vérifiez robots.txt lui-même, sur chaque hôte, et rappelez-vous qu’une recherche de Google-Extended dans le journal de serveur ne trouve rien, que vous le bloquiez ou non. L’exemple de groupe de Google montre le jeton avec un chemin autorisé et un chemin interdit comme n’importe quel autre.

Google-Extended n'envoie aucune requête lui-même : il n'apparaît donc jamais dans votre journal de serveur. Il est seulement lu dans robots.txt.

## À comparer avec Googlebot

[Googlebot](/fr/bots/googlebot) : Le robot qui récupère réellement vos pages pour Search.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste Google-Extended avec une requête réelle et lit robots.txt pour lui. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Google-Extended respecte-t-il robots.txt ?

Lu dans robots.txt seulement ; il n’existe pas de user agent distinct. Il n'envoie aucune requête lui-même : il n'y a rien à bloquer au pare-feu, la règle dans robots.txt est le seul moyen de contrôle.

### Comment savoir si Google-Extended est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Google Search Central: Google's common crawlers (last updated 2026-10-15)](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers)
