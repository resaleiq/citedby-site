title: ChatGPT peut-il lire mon site ? Ce qui décide
h1: ChatGPT peut-il lire mon site ? Les trois points qui décident
description: Trois points décident si ChatGPT lit votre boutique en ligne : robots.txt, le texte dans le HTML et la réponse du serveur. Comment les vérifier.
slug: can-chatgpt-read-my-website
locale: fr
cluster: Exploration par les robots
date: 2026-10-20
reviewed: 2026-10-20
hero: auto
hero_alt: Trois portes entre une page de boutique et un assistant IA : robots.txt, texte de la page et données structurées
hero_sub: Trois portes entre votre page et l'assistant
hero_boxes: robots.txt|OAI-SearchBot autorisé ?; Réponse du serveur|pas de refus 403; Texte de la page|présent dans le HTML
widget: on
steps_img: on
howto: on
related: /fr/ai-visibility-audit|Audit de visibilité IA : que vérifier ?; /fr/blog/is-gptbot-blocked|GPTBot est-il bloqué sur votre site ?; /data|Qui ChatGPT cite, par niche
answer: ChatGPT peut lire votre site si trois conditions sont réunies : robots.txt ne bloque pas OAI-SearchBot, le texte de la page se trouve dans le HTML envoyé par votre serveur plutôt que ajouté par JavaScript, et votre serveur ou pare-feu ne refuse pas le robot. L'audit CitedBy teste les deux premières sur chaque page.

## Quelles sont les trois portes entre ChatGPT et votre page ?

La recherche de ChatGPT utilise un robot nommé OAI-SearchBot pour trouver des pages. OpenAI exploite aussi GPTBot, qui collecte des données d'entraînement, et ChatGPT-User, qui récupère une page quand une personne pose une question à son sujet. OpenAI précise que chacun se règle séparément dans robots.txt : vous pouvez en autoriser un et en bloquer un autre ([documentation OpenAI](https://developers.openai.com/docs/bots)).

Trois portes doivent donc rester ouvertes : robots.txt, la réponse de votre serveur et le contenu de la page. L'audit teste la première et la troisième. La deuxième se lit dans vos journaux de serveur.

## Comment vérifier, étape par étape ?

1. Ouvrez robots.txt : tapez `votre-boutique.fr/robots.txt` dans un navigateur et cherchez `User-agent: OAI-SearchBot`, `GPTBot` ou `*` suivi de `Disallow: /`. Un `Disallow: /` sous `User-agent: *` bloque tous les robots qui n'ont pas de règle propre.
2. Lancez l'audit : il lit robots.txt pour OAI-SearchBot, GPTBot, PerplexityBot, Google-Extended et Bingbot et vous dit lesquels sont bloqués (dès 9 €).
3. Regardez le nombre de mots : l'audit indique combien de mots contient le HTML de la page. Votre accueil doit en compter plusieurs centaines, avec le nom de votre boutique et ce que vous vendez.
4. Cherchez votre produit dans le code source : ouvrez la page, choisissez Afficher le code source de la page et cherchez le nom d'un produit. S'il manque, la page construit son texte avec JavaScript, et un robot qui n'exécute pas les scripts ne voit rien.
5. Vérifiez les données Organization : le bloc JSON-LD doit être présent pour que les assistants trouvent votre nom, votre logo et vos coordonnées au même endroit.

![Un contrôle CitedBy sur bbc.com le 18 octobre 2026 : robots.txt bloque OAI-SearchBot, GPTBot, PerplexityBot et Google-Extended ; 2 547 mots sont lisibles dans le HTML](/blog/img/check-result-bbc.webp "Un vrai contrôle sur bbc.com, le 18 oct. 2026. La BBC bloque ces robots volontairement ; pour une boutique qui veut être nommée, ce résultat serait le problème à corriger."){972x559}

## À quoi ressemble une page bloquée pour un robot ?

Certains thèmes de boutique en ligne et certains créateurs de sites envoient une page presque vide et la remplissent avec JavaScript. Le visiteur voit une fiche produit complète. Un robot qui n'exécute pas JavaScript reçoit une coquille.

Certains assistants exécutent JavaScript, d'autres non. La position la plus sûre consiste à mettre le nom de votre marque et le texte de vos produits dans le HTML lui-même.

## Quelle porte l'audit ne peut-il pas voir ?

robots.txt est une demande, et c'est votre hébergement qui décide en pratique. Un réglage de pare-feu ou de CDN peut répondre à un robot par une erreur même quand robots.txt l'autorise. L'audit ne teste pas ce point. Cherchez dans les journaux de votre serveur ou de votre CDN les requêtes de `OAI-SearchBot` et regardez les codes de réponse : une série de 403 est le signe d'un refus.

## Que faire du résultat ?

- robots.txt bloque un robot que vous voulez : supprimez la règle `Disallow` correspondante. OpenAI indique que la prise en compte peut demander environ une journée.
- Peu de mots dans le HTML : faites générer l'accueil et les textes produit côté serveur.
- Pas de données Organization : ajoutez-les en JSON-LD sur la page d'accueil.
- Tout est en règle : être lisible est le ticket d'entrée, pas le résultat. Savoir si un assistant nomme votre boutique est une autre question, que l'audit mesure en posant de vraies questions d'acheteurs.

Pour la liste complète des vérifications d'une boutique, voyez [l'audit de visibilité IA](/fr/ai-visibility-audit).

## FAQ

### GPTBot et la recherche ChatGPT, est-ce la même chose ?
Non. GPTBot collecte des données qui peuvent servir à entraîner des modèles. OAI-SearchBot est le robot des résultats de recherche de ChatGPT. Vous pouvez bloquer GPTBot et autoriser OAI-SearchBot.

### Si je bloque GPTBot, ChatGPT arrêtera-t-il de citer ma boutique ?
Pas à lui seul. Les résultats de recherche dépendent d'OAI-SearchBot. Ne bloquer que GPTBot est un choix courant des boutiques qui ne veulent pas que leur contenu serve à l'entraînement.

### Ajouter un fichier llms.txt règle-t-il le problème ?
C'est facultatif. Nous ne nous attendons pas à ce qu'il change les réponses des assistants, et l'audit le marque comme facultatif.

### Combien de temps avant qu'une modification soit prise en compte ?
OpenAI indique qu'il faut compter environ 24 heures pour que ses systèmes s'adaptent après une modification de robots.txt.

## Sources

- [OpenAI : robots d'exploration et user agents](https://developers.openai.com/docs/bots)
- [CitedBy : audit de site](https://citedby.eu/)
