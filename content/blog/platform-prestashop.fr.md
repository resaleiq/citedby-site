title: PrestaShop : un seul jeu de règles robots.txt pour tous les bots
slug: prestashop
description: Le guide de PrestaShop décrit un bouton Generate robots.txt qui remplace votre fichier et n'utilise que User-agent: *. Ajoutez les règles IA ensuite.
section: platforms
locale: fr
cluster: Robots d'exploration IA par plateforme
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur PrestaShop : Où Traffic, SEO and URLs, Bouton Generate robots.txt, User-agent étoile seulement, Régénération Remplace le fichier
hero_sub: Réglages des robots d'exploration IA sur PrestaShop
hero_boxes: Où|Traffic > SEO and URLs; Bouton|Generate robots.txt; User-agent|* seulement; Régénération|Remplace le fichier
widget: on
related: /fr/platforms|Toutes les plateformes comparées; /fr/platforms/shopify|Shopify; /fr/bots|Robots d'exploration IA comparés; /fr/guides/cms|Checklist de visibilité IA pour Shopify, WooCommerce et plus
answer: Le guide utilisateur de PrestaShop décrit un outil Robots file generation sous Shop Parameters, Traffic, SEO and URLs. Il écrit des directives d'exclusion pour les fichiers non publics avec User-agent: *, donc il ne nomme aucun robot d'exploration IA. Cliquer sur Generate robots.txt remplace tout fichier existant : ajoutez vos propres règles IA seulement après la génération.

## Où se trouve le réglage sur PrestaShop

Le guide utilisateur de PrestaShop 8 le place sous Configuring your Shop Parameters, puis Traffic, puis SEO and URLs. La section s'appelle Robots file generation. La page ne nomme pas d'autre chemin de menu dans le back-office, et elle affiche « Last updated 4 years ago » en bas.

## Ce que dit la page de PrestaShop et que les autres plateformes ne disent pas

PrestaShop ne vous donne pas de zone où saisir des règles. Il vous donne un bouton qui écrit tout le fichier. Le guide dit que le générateur « crée simplement un fichier avec des directives d'exclusion pour les fichiers et répertoires qui ne sont pas destinés à être publics », appliquées à tous les bots par la chaîne « User-agent: * ». Il dit aussi que les pires bots ignorent le fichier, car il est « purement consultatif ». La conséquence pour les robots d'exploration IA se trouve dans les deux dernières phrases de la section : régénérer efface tout ce que vous avez ajouté.

Dans les mots du fournisseur (original en anglais) : “Clicking on the "Generate robots.txt" button replaces any existing robots.txt file with a new one. Therefore, if you want to add your own rules, do it after PrestaShop has generated its version of the file.”

Source : [PrestaShop 8 User Guide: SEO and URLs](https://docs.prestashop-project.org/v.8-documentation/user-guide/configuring-shop/shop-parameters/traffic/seo-and-urls), lu le 24 octobre 2026.

## Les étapes

1. Ouvrez SEO and URLs dans la section Traffic de Shop Parameters.
2. Allez dans Robots file generation.
3. Cliquez sur Generate robots.txt. Cela remplace tout fichier robots.txt existant.
4. Ajoutez vos propres règles après que PrestaShop a généré sa version. La page ne dit pas comment modifier le fichier généré : utilisez donc l'accès aux fichiers que vous donne votre hébergement.
5. Ouvrez /robots.txt sur votre boutique pour vérifier que vos règles y sont toujours. Répétez l'étape 4 chaque fois que vous cliquez de nouveau sur le bouton.

## Les lignes à utiliser

Pour autoriser :

```
# Nothing to add: the generated file only lists files and directories that are not public.
# To name one explicitly, add after the generated block:
User-agent: OAI-SearchBot
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

Le fichier généré s'adresse de la même façon à tous les bots, car il utilise User-agent: * et rien d'autre : l'outil de PrestaShop ne vous laisse donc aucun choix par robot. Le guide dit que vous voulez donner un accès complet à certains bots, comme ceux de Google, et pas à d'autres, comme les bots de spam et les voleurs de contenu : c'est une décision que vous prenez dans les groupes que vous ajoutez vous-même. Le guide ne mentionne aucun robot d'exploration IA par son nom, et il ne renvoie à aucun réglage ni module pour eux.

## Comparer avec Shopify

[Shopify](/fr/platforms/shopify) : un modèle robots.txt.liquid qui conserve vos ajouts, là où le bouton de PrestaShop les écrase.

## Vérifier votre propre site

Le contrôle gratuit dans l'encadré ci-dessus lit robots.txt pour les robots d'exploration IA et envoie une requête réelle par robot. Une règle que les réglages de votre plateforme autorisent mais qu'un pare-feu refuse apparaît donc. La liste complète des robots se trouve sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Régénérer robots.txt dans PrestaShop supprimera-t-il mes règles pour les robots d'exploration IA ?

Oui, si vous les avez ajoutées au fichier généré. Le guide de PrestaShop dit que le bouton remplace tout robots.txt existant par un nouveau, et que vous devez ajouter vos propres règles après qu'il a généré sa version.

### PrestaShop bloque-t-il les robots d'exploration IA par défaut ?

Le guide ne le dit pas. Il décrit un fichier généré avec des directives d'exclusion pour les fichiers et répertoires non publics sous User-agent: *, et il ne nomme aucun robot d'exploration IA.

## Sources

- [PrestaShop 8 User Guide: SEO and URLs](https://docs.prestashop-project.org/v.8-documentation/user-guide/configuring-shop/shop-parameters/traffic/seo-and-urls), lu le 24 octobre 2026
