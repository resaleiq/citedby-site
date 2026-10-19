title: GPTBot est-il bloqué sur votre site ? 4 vérifications (2026)
h1: GPTBot est-il bloqué sur mon site ? Quatre endroits à vérifier, avec un test pour chacun
description: robots.txt, CDN, pare-feu ou serveur peuvent bloquer GPTBot. Comment savoir lequel en quelques minutes, et ce que le blocage change ou non pour ChatGPT.
slug: is-gptbot-blocked
locale: fr
cluster: Exploration par les robots
date: 2026-10-20
reviewed: 2026-10-20
hero: auto
hero_alt: Quatre cases numérotées de 1 à 4 : robots.txt, CDN, pare-feu, serveur, les endroits où GPTBot peut être arrêté
hero_sub: Les quatre endroits où GPTBot peut être arrêté
hero_boxes: robots.txt|la règle Disallow; CDN|réglages anti-robots; Pare-feu ou plugin|règles de sécurité; Serveur|règles et journaux
widget: on
steps_img: on
howto: on
related: /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ?; /fr/ai-visibility-audit|Audit de visibilité IA : que vérifier ?; /sample-audit|Un exemple de mini-audit
answer: GPTBot est bloqué sur votre site si votre fichier robots.txt contient une règle Disallow qui le concerne, ou si un CDN, un pare-feu ou le serveur refuse ses requêtes. Ouvrez votre-boutique.fr/robots.txt, lancez un audit, puis comparez deux requêtes envoyées à votre serveur. Bloquer GPTBot ne bloque pas à lui seul la recherche ChatGPT.

## Où GPTBot peut-il être arrêté ?

GPTBot est le robot qu'OpenAI utilise pour collecter des contenus susceptibles d'entraîner ses modèles. Une de ses requêtes peut être refusée à quatre niveaux, et chacun demande son propre test : le fichier robots.txt, le CDN, un plugin de sécurité ou un pare-feu applicatif (WAF), et la configuration du serveur web.

Le premier niveau se lit dans robots.txt, et notre audit le contrôle. Les trois autres répondent par un code d'erreur même quand robots.txt dit oui, ce qui les rend invisibles dans ce fichier.

## Comment vérifier, étape par étape ?

1. Ouvrez robots.txt : tapez `votre-boutique.fr/robots.txt` dans un navigateur et cherchez un groupe qui nomme `GPTBot`. S'il n'y en a pas, GPTBot suit le groupe `User-agent: *`, et un `Disallow: /` général le bloque aussi ([RFC 9309](https://www.rfc-editor.org/rfc/rfc9309)).
2. Lancez l'audit : il lit robots.txt pour GPTBot, OAI-SearchBot, PerplexityBot, Google-Extended et Bingbot et nomme ceux qui sont bloqués (dès 9 €).
3. Comparez deux requêtes : envoyez deux requêtes vers votre page d'accueil, l'une normale, l'autre avec le user-agent de GPTBot, et comparez les codes de réponse (commandes plus bas).
4. Regardez votre CDN : ouvrez votre compte et cherchez les réglages sur les robots IA. Les étapes pour Cloudflare sont plus bas.
5. Passez en revue vos règles de sécurité : parcourez la liste de votre plugin de sécurité ou de votre pare-feu et cherchez `GPTBot`, `bot`, `AI` et `crawler`.
6. Fouillez les journaux : cherchez `GPTBot` dans les journaux de votre serveur. Une série de réponses 403 trahit un blocage que robots.txt ne montre pas.

## Comment faire le test des deux requêtes ?

Remplacez `votre-boutique.fr` par votre adresse. La première commande envoie une requête normale, la seconde envoie la chaîne user-agent de GPTBot publiée par OpenAI. Chacune n'affiche que le code de réponse.

```
curl -s -o /dev/null -w "%{http_code}\n" https://votre-boutique.fr/
curl -s -o /dev/null -w "%{http_code}\n" -A "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.4; +https://openai.com/gptbot" https://votre-boutique.fr/
```

Un 403 sur la seconde requête seulement indique qu'une règle cible le nom du robot. Gardez une limite en tête : ce test part de votre ordinateur. Si votre hébergeur juge aussi les robots d'après leur adresse IP, le vrai GPTBot peut recevoir une réponse différente de la vôtre. OpenAI publie les plages d'IP de GPTBot à l'adresse `openai.com/gptbot.json`, ce qui permet de vérifier dans vos journaux si les requêtes venues de ces plages sont passées ([documentation OpenAI](https://developers.openai.com/api/docs/bots)).

## Où se trouve le réglage dans Cloudflare ?

D'après la documentation de Cloudflare : ouvrez votre domaine, allez dans AI Crawl Control, onglet Security, puis onglet Crawlers. La colonne Actions permet d'autoriser (Allow) ou de bloquer (Block) chaque robot. Choisir Block crée ou met à jour une règle personnalisée du WAF, et vous pouvez continuer à appliquer robots.txt si vous choisissez Allow ([Cloudflare : gérer les robots IA](https://developers.cloudflare.com/ai-crawl-control/features/manage-ai-crawlers/)).

Les réglages par défaut de Cloudflare évoluent. Selon Help Net Security, à partir du 15 septembre 2026, les nouveaux domaines bloquent par défaut les robots d'entraînement et les agents sur les pages qui affichent de la publicité, tandis que les robots de recherche restent autorisés ([Help Net Security](https://www.helpnetsecurity.com/2026/07/02/cloudflare-ai-crawler-controls/)). Regardez votre propre tableau de bord plutôt que de supposer quel réglage votre domaine a reçu.

## Que faire quand le contrôle indique que votre site a refusé la requête ?

Une requête simple de notre contrôle peut elle-même être refusée. Quand la réponse est un code HTTP 403, 429 ou 503, le contrôle le signale et précise qu'il ne peut pas savoir, de l'extérieur, si les robots IA sont refusés eux aussi. Un 403 signifie en général qu'une règle a bloqué la requête. Un 429 ou un 503 peut aussi venir d'une limitation de débit ou d'une panne, qui touche tous vos visiteurs. Corrigez la cause dans votre CDN, votre pare-feu ou votre espace d'hébergement, puis relancez le contrôle.

## Faut-il débloquer GPTBot ?

C'est votre décision, et le bloquer est un choix légitime. OpenAI distingue GPTBot, OAI-SearchBot et ChatGPT-User, trois robots aux rôles séparés. GPTBot sert aux données d'entraînement. OAI-SearchBot fait apparaître les sites dans les fonctions de recherche de ChatGPT. ChatGPT-User récupère une page quand une personne pose une question à son sujet.

| Votre objectif | Ce qu'il faut faire |
| --- | --- |
| Apparaître dans la recherche ChatGPT sans servir à l'entraînement | Autoriser `OAI-SearchBot`, interdire `GPTBot` |
| Apparaître dans la recherche ChatGPT et autoriser l'entraînement | Autoriser les deux |
| Rester hors des deux | Interdire les deux et vérifier vos journaux pour ChatGPT-User |

Selon OpenAI, une modification de robots.txt peut mettre environ 24 heures à atteindre OAI-SearchBot.

## FAQ

### Bloquer GPTBot retire-t-il ma boutique de ChatGPT ?
Pas à lui seul. OpenAI décrit OAI-SearchBot comme le robot des fonctions de recherche de ChatGPT et GPTBot comme le robot d'entraînement, chacun réglé séparément dans robots.txt.

### Mon robots.txt est correct, pourquoi GPTBot reçoit-il quand même un 403 ?
robots.txt est une demande adressée au robot. Un CDN, un pare-feu ou une règle du serveur peut refuser la requête malgré tout. Vérifiez ces niveaux avec le test des deux requêtes et vos journaux.

### ChatGPT-User respecte-t-il robots.txt ?
OpenAI indique que les règles de robots.txt peuvent ne pas s'appliquer à ChatGPT-User, parce que ces requêtes sont déclenchées par une personne.

### Débloquer GPTBot fera-t-il recommander ma boutique ?
Non. Être lisible est le ticket d'entrée. Que l'assistant nomme votre boutique dépend de ce qu'il trouve sur votre catégorie, ce que l'audit CitedBy mesure avec de vraies questions d'acheteurs.

## Sources

- [OpenAI : robots d'exploration, user agents et plages d'IP](https://developers.openai.com/api/docs/bots)
- [Cloudflare : gérer les robots IA](https://developers.cloudflare.com/ai-crawl-control/features/manage-ai-crawlers/)
- [Help Net Security : Cloudflare modifie l'accès des robots IA, 2 juillet 2026](https://www.helpnetsecurity.com/2026/07/02/cloudflare-ai-crawler-controls/)
- [IETF RFC 9309 : protocole d'exclusion des robots](https://www.rfc-editor.org/rfc/rfc9309)
