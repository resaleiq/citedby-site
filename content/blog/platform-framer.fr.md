title: Framer : importez votre propre robots.txt avec Static Files
slug: framer
description: Framer génère un robots.txt pour chaque site publié. Pour le changer, importez le vôtre via Static Files sur Pro ou Enterprise : il remplace le fichier généré.
section: platforms
locale: fr
cluster: Robots d'exploration IA par plateforme
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur Framer : Où Static Files, Offres Pro et Enterprise, Par défaut Généré automatiquement, Fichier personnalisé Remplace le fichier par défaut
hero_sub: Réglages des robots d'exploration IA sur Framer
hero_boxes: Où|Static Files; Offres|Pro et Enterprise; Par défaut|Généré automatiquement; Fichier personnalisé|Remplace le fichier par défaut
widget: on
related: /fr/platforms|Toutes les plateformes comparées; /fr/platforms/webflow|Webflow; /fr/bots|Robots d'exploration IA comparés; /fr/guides/cms|Checklist de visibilité IA pour Shopify, WooCommerce et plus
answer: Framer génère un robots.txt pour chaque site publié. Pour autoriser ou bloquer des robots d'exploration IA, vous importez votre propre fichier via Static Files, avec le chemin réglé sur /. Framer indique que c'est disponible avec les offres Pro et Enterprise, et que votre fichier remplace le fichier généré au lieu de s'y ajouter.

## Où se trouve le réglage sur Framer

Dans le tableau de bord de votre projet, sélectionnez votre domaine, ouvrez l'onglet Files et importez votre fichier avec le chemin réglé sur /. La page d'aide de Framer appelle cela Static Files. Pour voir d'abord le fichier en ligne, ajoutez /robots.txt au domaine de votre site dans un navigateur.

## Ce que dit la page de Framer et que les autres plateformes ne disent pas

Framer ne propose aucun éditeur de robots.txt. Le fichier est généré pour vous, et la seule façon de le changer est d'importer un fichier de remplacement, ce qui dépend de l'offre. La page de Framer dit que si vous avez besoin d'un robots.txt personnalisé, vous pouvez en importer un avec Static Files, et que le nouveau fichier remplace celui qui est généré automatiquement. La limite liée à l'offre vient juste après.

Dans les mots du fournisseur (original en anglais) : “This is available on Pro and Enterprise plans.”

Source : [Framer Help: Access your robots.txt file](https://www.framer.com/help/articles/how-can-i-access-the-robots-txt-file/), lu le 24 octobre 2026.

## Les étapes

1. Écrivez votre robots.txt dans un fichier texte brut sur votre ordinateur.
2. Allez dans le tableau de bord de votre projet et sélectionnez votre domaine.
3. Ouvrez l'onglet Files.
4. Importez votre fichier avec le chemin réglé sur /.
5. Ouvrez yourdomain.com/robots.txt dans un navigateur pour vérifier que le fichier en ligne est bien le vôtre.

## Les lignes à utiliser

Pour autoriser :

```
User-agent: OAI-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /
```

Pour bloquer :

```
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /
```

## Pièges à éviter

Comme votre fichier importé remplace le fichier généré, tout ce que contenait ce dernier disparaît, sauf si vous le copiez d'abord. La page de Framer ne dit pas ce que contient le fichier généré : lisez donc yourdomain.com/robots.txt avant d'importer le vôtre et conservez les lignes que vous voulez garder, comme une ligne Sitemap. La page parle de robots.txt en général et ne mentionne aucun robot d'exploration IA par son nom : les user agents ci-dessus sont donc des exemples à vérifier sur la page de chaque opérateur. Elle a été mise à jour pour la dernière fois le 15 septembre 2026.

## Comparer avec Webflow

[Webflow](/fr/platforms/webflow) : les règles se saisissent dans un champ de réglages au lieu d'être importées sous forme de fichier, avec en plus un en-tête Content-Signal.

## Vérifier votre propre site

Le contrôle gratuit dans l'encadré ci-dessus lit robots.txt pour les robots d'exploration IA et envoie une requête réelle par robot. Une règle que les réglages de votre plateforme autorisent mais qu'un pare-feu refuse apparaît donc. La liste complète des robots se trouve sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Puis-je modifier le fichier robots.txt dans Framer ?

Oui, par importation. La page de Framer indique d'ouvrir l'onglet Files de votre domaine dans le tableau de bord du projet et d'importer votre fichier avec le chemin réglé sur /. Elle dit que c'est disponible avec les offres Pro et Enterprise.

### Framer crée-t-il un robots.txt automatiquement ?

Oui. La page de Framer dit qu'il génère un fichier robots.txt pour chaque site publié, et qu'un fichier personnalisé importé via Static Files remplace celui par défaut.

## Sources

- [Framer Help: Access your robots.txt file](https://www.framer.com/help/articles/how-can-i-access-the-robots-txt-file/), lu le 24 octobre 2026
