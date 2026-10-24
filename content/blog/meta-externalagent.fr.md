title: Meta-ExternalAgent : ce qu'il fait et ce que change son blocage
h1: Meta-ExternalAgent : ce qu'il fait et ce que change son blocage
description: Meta-ExternalAgent (Meta) : plusieurs rôles. Jeton robots.txt, effet d'un Disallow et vérification d'une requête, lus sur la page de l'opérateur.
slug: meta-externalagent
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Quatre faits sur Meta-ExternalAgent : opérateur Meta, rôle Plusieurs rôles, respecte robots.txt Oui, liste d'adresses Aucune
hero_sub: Meta-ExternalAgent, géré par Meta
hero_boxes: Opérateur|Meta; Rôle|Plusieurs rôles; Respecte robots.txt|Oui; Liste d'adresses|Aucune
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/gptbot|GPTBot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: Meta-ExternalAgent est le robot d’exploration de Meta pour des usages comme l’entraînement de modèles d’IA de fondation ou l’amélioration de produits par l’indexation directe de contenu. La page de Meta, mise à jour le 21 mai 2026, liste cinq agents. Meta indique que Meta-ExternalFetcher et FacebookExternalHit peuvent contourner robots.txt, et que les changements peuvent prendre jusqu’à 24 heures.

## Ce qu'est Meta-ExternalAgent

La page de Meta liste cinq robots. FacebookExternalHit récupère une page quand quelqu’un partage un lien sur Facebook, Instagram ou Messenger, pour mettre en cache son titre, sa description et sa vignette. Meta-WebIndexer améliore les résultats de recherche de Meta AI, et Meta indique que l’autoriser l’aide à citer et à lier votre contenu dans les réponses de Meta AI. Meta-ExternalAds explore pour les produits publicitaires et professionnels. Meta-ExternalAgent est celui de l’entraînement de modèles d’IA de fondation ou de l’indexation. Meta-ExternalFetcher récupère des liens individuels à la demande d’un utilisateur, y compris pour aider l’IA à naviguer sur des sites web afin d’accomplir des tâches pour les utilisateurs.

| Fait | Meta-ExternalAgent |
| --- | --- |
| Opérateur | Meta |
| Rôle | Entraînement de modèles d’IA et indexation de contenu |
| Jeton robots.txt | `meta-externalagent` |
| Respecte robots.txt | Oui |
| Adresses IP | Aucune publiée |
| Page de l'opérateur lue le | 21 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “The Meta-ExternalAgent crawler crawls the web for use cases such as training foundation AI models or improving products by indexing content directly.”

Source : [Meta for Developers: Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers), lu le 21 octobre 2026.

## Que se passe-t-il si vous bloquez Meta-ExternalAgent

Interdire meta-externalagent n’affecte que cet agent : les exemples de Meta donnent un groupe distinct pour chaque jeton, et les quatre autres ont les leurs. Le plus coûteux à bloquer par erreur est FacebookExternalHit, car il construit l’aperçu du lien quand quelqu’un partage votre page. Deux des cinq peuvent ignorer votre robots.txt : Meta indique que Meta-ExternalFetcher peut contourner robots.txt parce qu’il effectue des récupérations demandées par l’utilisateur, et que FacebookExternalHit peut le contourner pour des contrôles de sécurité ou d’intégrité, comme les contrôles de logiciels malveillants.

## Les lignes robots.txt

Pour autoriser Meta-ExternalAgent :

```
User-agent: meta-externalagent
Allow: /
```

Pour bloquer Meta-ExternalAgent :

```
User-agent: meta-externalagent
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
meta-externalagent/1.1
```

## Comment distinguer une vraie requête d'une fausse

La page de Meta donne les chaînes de user agent (meta-externalagent/1.1 et la version avec un lien) et ne publie pas de liste d’IP dans le texte que nous avons lu : nous n’indiquons donc aucun nombre. Pour FacebookExternalHit, Meta indique d’autoriser soit les chaînes de user agent, soit les adresses IP, et qualifie les adresses d’option la plus sûre. Meta indique que les robots peuvent mettre robots.txt en cache jusqu’à 24 heures : comptez donc ce délai avant de juger un changement. Les questions vont à webmasters@meta.com.

## À comparer avec GPTBot

[GPTBot](/fr/bots/gptbot) : Le robot d’entraînement d’OpenAI, qui respecte robots.txt sans les cas de contournement de Meta.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). Meta-ExternalAgent n'en fait pas partie : lisez votre robots.txt pour un groupe `meta-externalagent` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Meta-ExternalAgent respecte-t-il robots.txt ?

Oui. Donnez à meta-externalagent son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si Meta-ExternalAgent est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Meta for Developers: Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers)
