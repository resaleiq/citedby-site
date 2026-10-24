title: Ghost : ajoutez robots.txt à votre thème pour gérer les robots IA
slug: ghost
description: Ghost n'a pas de réglage robots.txt dans l'admin. Selon son aide, un robots.txt à la racine du thème remplace celui par défaut. Offre requise sur Ghost(Pro).
section: platforms
locale: fr
cluster: Robots d'exploration IA par plateforme
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur Ghost : Où Racine du thème, Fichier robots.txt, Effet Remplace le fichier par défaut, Ghost(Pro) Offre Creator ou supérieure
hero_sub: Réglages des robots d'exploration IA sur Ghost
hero_boxes: Où|Racine du thème; Fichier|robots.txt; Effet|Remplace le fichier par défaut; Ghost(Pro)|Creator ou supérieure
widget: on
related: /fr/platforms|Toutes les plateformes comparées; /fr/platforms/wordpress-com|WordPress.com; /fr/bots|Robots d'exploration IA comparés; /fr/guides/cms|Checklist de visibilité IA pour Shopify, WooCommerce et plus
answer: Ghost sert un robots.txt par défaut. Pour le changer, enregistrez votre propre robots.txt à la racine de votre thème, puis installez et activez la nouvelle version du thème. La page d'aide de Ghost dit que les thèmes personnalisés sur Ghost(Pro) demandent l'offre Creator ou supérieure : votre offre décide donc si vous pouvez le modifier.

## Où se trouve le réglage sur Ghost

Il n'y a aucun champ robots.txt dans l'admin. La page d'aide de Ghost dit que le fichier se trouve dans le thème de votre site : écrivez votre robots.txt et enregistrez-le à la racine du thème. La documentation des thèmes de Ghost le dit en une ligne : les thèmes peuvent inclure un robots.txt qui remplace le robots.txt par défaut fourni par Ghost.

## Ce que dit la page de Ghost et que les autres plateformes ne disent pas

Sur Ghost, le fichier voyage avec le thème : l'offre que vous avez décide donc si vous pouvez le changer. La page d'aide de Ghost dit qu'il faut être à l'aise pour écrire son propre robots.txt et installer une nouvelle version de son thème. Elle ajoute ensuite une limite d'offre pour Ghost(Pro), le service hébergé de Ghost : installer un thème personnalisé demande l'offre Creator ou supérieure. La page décrit ce qui se passe ensuite en ces termes.

Dans les mots du fournisseur (original en anglais) : “Once the new version of the theme is installed and activated, the theme's robots.txt will be used in place of Ghost's default robots.txt.”

Source : [Ghost Help: Modifying robots.txt](https://ghost.org/help/modifying-robots-txt/), lu le 24 octobre 2026.

## Les étapes

1. Écrivez votre fichier robots.txt.
2. Enregistrez-le à la racine de votre thème.
3. Installez la nouvelle version du thème, puis activez-la. Ghost dit que le robots.txt du thème est utilisé à la place de celui par défaut une fois la nouvelle version installée et activée.
4. Sur Ghost(Pro), vérifiez d'abord votre offre : Ghost dit qu'installer un thème personnalisé demande l'offre Creator ou supérieure.

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

Le fichier du thème est utilisé à la place de celui par défaut de Ghost, et non en plus. Les pages de Ghost ne disent pas ce que contient le fichier par défaut : ouvrez donc yoursite.com/robots.txt avant de le remplacer et recopiez les lignes que vous voulez garder, comme une ligne Sitemap. La page avertit aussi que cette voie demande d'être à l'aise pour écrire le fichier soi-même, et elle ne couvre aucun robot d'exploration IA par son nom.

## Comparer avec WordPress.com

[WordPress.com](/fr/platforms/wordpress-com) : son refus de l'IA est un réglage de partage, et non un fichier que vous écrivez.

## Vérifier votre propre site

Le contrôle gratuit dans l'encadré ci-dessus lit robots.txt pour les robots d'exploration IA et envoie une requête réelle par robot. Une règle que les réglages de votre plateforme autorisent mais qu'un pare-feu refuse apparaît donc. La liste complète des robots se trouve sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Où mettre un robots.txt personnalisé sur Ghost ?

À la racine de votre thème. La page d'aide de Ghost dit qu'une fois la nouvelle version du thème installée et activée, le robots.txt du thème est utilisé à la place de celui par défaut de Ghost.

### Faut-il une offre payante pour modifier robots.txt sur Ghost(Pro) ?

La page de Ghost dit qu'installer un thème personnalisé sur Ghost(Pro) demande un abonnement à l'offre Creator ou supérieure. Comme le fichier fait partie du thème, cela vaut aussi pour un robots.txt personnalisé.

## Sources

- [Ghost Help: Modifying robots.txt](https://ghost.org/help/modifying-robots-txt/), lu le 24 octobre 2026
- [Ghost Docs: Theme structure](https://docs.ghost.org/themes/structure), lu le 24 octobre 2026
