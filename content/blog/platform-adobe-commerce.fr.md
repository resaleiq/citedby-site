title: Adobe Commerce : robots.txt dans Content, Design, Configuration
slug: adobe-commerce
description: Adobe Commerce modifie robots.txt dans l'Admin, sous Search Engine Robots. Les projets Cloud ajoutent des étapes pub/media, et Adobe ne nomme aucun robot IA.
section: platforms
locale: fr
cluster: Robots d'exploration IA par plateforme
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur Adobe Commerce : Où Content, Design, Configuration, Section Search Engine Robots, Cloud Étapes en plus, Noms d'IA Non cités
hero_sub: Réglages des robots d'exploration IA sur Adobe Commerce
hero_boxes: Où|Content > Design > Configuration; Section|Search Engine Robots; Cloud|Étapes en plus; Noms d'IA|Non cités
widget: on
related: /fr/platforms|Toutes les plateformes comparées; /fr/platforms/shopify|Shopify; /fr/bots|Robots d'exploration IA comparés; /fr/guides/cms|Checklist de visibilité IA pour Shopify, WooCommerce et plus
answer: Sur Adobe Commerce, vous modifiez robots.txt dans l'Admin : Content, Design, Configuration, ligne Global, puis Search Engine Robots et la zone d'instruction personnalisée. Les pages d'Adobe parlent des robots et bots en général, sans nommer de robot IA : c'est à vous d'ajouter les user agents IA. Les projets Cloud ont des étapes de chemin de fichier en plus.

## Où se trouve le réglage sur Adobe Commerce

Dans la barre latérale de l'Admin, allez dans Content, puis Design, puis Configuration. La présentation SEO d'Adobe indique de repérer la configuration Global dans la première ligne de la grille, de cliquer sur Edit, puis de déplier la section Search Engine Robots. La zone Edit Custom instruction of robots.txt file s'y trouve, avec un bouton Reset to Default.

## Ce que disent les pages d'Adobe Commerce et que les autres plateformes ne disent pas

Sur Adobe Commerce en infrastructure cloud, le fichier robots.txt pose un problème d'emplacement que les autres plateformes n'ont pas. Le playbook de mise en œuvre d'Adobe indique d'ajouter le contenu dans l'Admin. Mais le système de fichiers est en lecture seule : le fichier doit donc se trouver sous pub/media, et un extrait VCL Fastly personnalisé redirige /robots.txt vers cet emplacement. Pour plusieurs sites dans un même projet, le playbook nomme les fichiers site par site, par exemple domainone_robots.txt. Pour les installations sur site, il indique d'écrire les fichiers dans /path/to/commerce/pub/media/ ou /path/to/commerce/media, selon ce qui convient à votre installation.

Dans les mots du fournisseur (original en anglais) : “Due to the read-only file system on Adobe Commerce on cloud infrastructure projects, you must specify the pub/media path before generating the file.”

Source : [Adobe Commerce Implementation Playbook: Best practices for configuring web crawlers](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/launch/robots-txt), lu le 24 octobre 2026.

## Les étapes

1. Dans la barre latérale de l'Admin, allez dans Content, puis Design, puis Configuration.
2. Repérez la configuration Global dans la première ligne de la grille et cliquez sur Edit.
3. Faites défiler la page et dépliez Search Engine Robots.
4. Réglez Default Robots sur INDEX, FOLLOW, NOINDEX, FOLLOW, INDEX, NOFOLLOW ou NOINDEX, NOFOLLOW. Adobe décrit ces valeurs comme des instructions données aux robots sur l'indexation et le suivi des liens.
5. Si besoin, saisissez vos propres règles dans la zone Edit Custom instruction of robots.txt file. Reset to Default rétablit les instructions d'Adobe.
6. Cliquez sur Save Configuration, puis ouvrez le /robots.txt de votre boutique pour voir le résultat. Le playbook d'Adobe donne en astuce que vous pouvez y consulter le fichier généré automatiquement.

## Les lignes à utiliser

Les exemples d'Adobe utilisent User-agent: * pour tous les robots. Pour autoriser ou bloquer un robot précis, ajoutez un groupe à son nom :

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

Les pages d'Adobe ne disent pas si le texte que vous saisissez s'ajoute à ses instructions par défaut ou les remplace. Enregistrez, puis lisez /robots.txt pour confirmer ce qui est servi.

## Pièges à éviter

Le playbook d'Adobe dit de ne pas exposer le chemin de votre Admin dans robots.txt, car c'est une vulnérabilité qui expose le site au piratage et à une perte de données potentielle, et de le supprimer. Les instructions par défaut d'Adobe commencent par User-agent: * et une liste de lignes Disallow comme /checkout/ et /catalog/ : vérifiez donc ce que vous conservez. Sur le cloud, un article de la base de connaissances daté du 18 août 2026 indique que le contenu de robots.txt est généré à partir de la configuration de l'Admin et stocké dans la base de données, sans fichier physique nécessaire dans ce scénario, alors que le playbook décrit la redirection vers pub/media. Les deux pages ne disent pas la même chose : confirmez auprès du support Adobe Commerce laquelle s'applique à votre projet. Le playbook précise aussi que ses conseils ne concernent que la vitrine native d'Adobe Commerce, pas les vitrines headless ni celles d'Adobe Experience Manager.

## Comparer avec Shopify

[Shopify](/fr/platforms/shopify) : un modèle de thème à la place d'une zone dans l'Admin, et le support ne corrigera pas les modifications qu'on y apporte.

## Vérifier votre propre site

Le contrôle gratuit dans l'encadré ci-dessus lit robots.txt pour les robots d'exploration IA et envoie une requête réelle par robot. Une règle que les réglages de votre plateforme autorisent mais qu'un pare-feu refuse apparaît donc. La liste complète des robots se trouve sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Pourquoi mon robots.txt personnalisé ne change-t-il pas sur Adobe Commerce cloud ?

La base de connaissances d'Adobe indique que la cause habituelle est la désactivation de l'indexation par les moteurs de recherche, ce qui empêche d'appliquer le contenu personnalisé de robots.txt. Corrigez-le dans la Cloud Console ou avec le réglage restrict_robots de la CLI magento-cloud. L'article ajoute que les environnements Staging ont l'indexation désactivée par défaut et qu'on ne peut pas l'y activer.

### Adobe Commerce liste-t-il des robots d'exploration IA pour robots.txt ?

Pas dans les pages que nous avons lues. Elles parlent de robots d'exploration et de bots, et leurs exemples n'utilisent que User-agent: *. Ajoutez chaque user agent IA que vous voulez autoriser ou bloquer sous la forme d'un groupe distinct.

## Sources

- [Adobe Commerce Implementation Playbook: Best practices for configuring web crawlers](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/launch/robots-txt), lu le 24 octobre 2026
- [Adobe Commerce Admin guide: SEO overview](https://experienceleague.adobe.com/en/docs/commerce-admin/marketing/seo/seo-overview), lu le 24 octobre 2026
- [Adobe Commerce knowledge base: Resolve robots.txt not updating or displaying default settings](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/robots-txt-not-updated-or-displaying-default-settings), lu le 24 octobre 2026
