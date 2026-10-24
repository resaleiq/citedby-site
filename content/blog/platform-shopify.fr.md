title: Shopify : gérez les robots IA et ce que robots.txt ne couvre pas
slug: shopify
description: Modifiez robots.txt.liquid pour gérer les robots IA sur Shopify. Shopify dit qu'un blocage n'affecte que le web ouvert, pas les données produit pour ChatGPT.
section: platforms
locale: fr
cluster: Robots d'exploration IA par plateforme
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Quatre faits sur Shopify : Où robots.txt.liquid, Support Non pris en charge par Shopify, Flux du catalogue Non couvert, Effet Immédiat
hero_sub: Réglages des robots d'exploration IA sur Shopify
hero_boxes: Où|robots.txt.liquid; Support|Non pris en charge par Shopify; Flux du catalogue|Non couvert; Effet|Immédiat
widget: on
related: /fr/platforms|Toutes les plateformes comparées; /fr/platforms/squarespace|Squarespace; /fr/bots|Robots d'exploration IA comparés; /fr/guides/cms|Checklist de visibilité IA pour Shopify, WooCommerce et plus
answer: Sur Shopify, vous contrôlez les robots d'exploration IA en ajoutant un modèle robots.txt.liquid à votre thème. La page d'aide de Shopify dit qu'un blocage à cet endroit n'affecte que la découvrabilité sur le web ouvert : les données produit continuent d'aller vers les vitrines agentiques comme ChatGPT ou Microsoft Copilot via Shopify Catalog, indépendamment de /robots.txt.

## Où se trouve le réglage sur Shopify

Online Store, puis Edit code du thème, puis Add a new template et choisissez robots. Shopify dit qu'il s'agit d'une personnalisation non prise en charge : son support ne peut pas aider pour les modifications, et un usage incorrect « peut entraîner la perte de tout le trafic ».

## Ce que dit la page de Shopify et que les autres plateformes ne disent pas

Shopify décrit deux couches de contrôle. La couche réseau est gérée par Shopify pour les boutiques hébergées sur Shopify, et vous n'avez rien à faire. La couche /robots.txt est la vôtre, via robots.txt.liquid. Sa page trace ensuite la ligne qui compte pour une boutique : si vous vendez via des vitrines agentiques comme ChatGPT ou Microsoft Copilot, vos données produit sont diffusées via Shopify Catalog « indépendamment de /robots.txt », et bloquer les robots d'exploration IA à l'une ou l'autre couche « n'affecte que la découvrabilité sur le web ouvert ». Pour changer ce que Catalog partage, vous utilisez les réglages des vitrines agentiques, et non robots.txt.

Dans les mots du fournisseur (original en anglais) : “Blocking AI crawlers at the /robots.txt or network layer affects only open-web discoverability. It doesn't stop your product data from being sent by Shopify Catalog to the agentic storefronts that you've activated.”

Source : [Shopify Help Center: Editing robots.txt.liquid](https://help.shopify.com/en/manual/promoting-marketing/seo/editing-robots-txt), lu le 21 octobre 2026.

## Les étapes

1. Depuis votre admin Shopify, allez dans Online Store.
2. Pour le thème que vous publiez, ouvrez le menu et choisissez Edit code.
3. Cliquez sur Add a new template, choisissez robots, puis Create template.
4. Conservez le Liquid qui produit les groupes de règles par défaut et ajoutez vos propres règles en dessous. Shopify recommande cette méthode plutôt que de remplacer le fichier par du texte brut, car le texte brut devient obsolète.
5. Enregistrez dans le thème publié. Shopify dit que les changements sont instantanés, mais que les robots ne réagissent pas toujours immédiatement.

## Les lignes à utiliser

Pour autoriser :

```
# Nothing to add: Shopify's default robots.txt allows crawlers that are not named.
# To name one explicitly, add under the default Liquid block:
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

Deux précisions tirées de la même page. Un thème importé depuis la section Themes de l'admin n'importe pas robots.txt.liquid ; les modifications faites avec ThemeKit ou en ligne de commande le conservent. Et si votre modèle produit les groupes par défaut, supprimez-le pour récupérer la version par défaut actuelle de Shopify, qui peut comporter des règles absentes de votre ancienne copie, comme Disallow: /search.

## Comparer avec Squarespace

[Squarespace](/fr/platforms/squarespace) : une case à cocher au lieu d'un modèle, et une liste figée de 26 noms.

## Vérifier votre propre site

Le contrôle gratuit dans l'encadré ci-dessus lit robots.txt pour les robots d'exploration IA et envoie une requête réelle par robot. Une règle que les réglages de votre plateforme autorisent mais qu'un pare-feu refuse apparaît donc. La liste complète des robots se trouve sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Bloquer GPTBot sur Shopify empêche-t-il ChatGPT d'afficher mes produits ?

Pas à lui seul. Shopify dit que robots.txt et les blocages réseau n'affectent que la découvrabilité sur le web ouvert, et que Shopify Catalog envoie les données produit aux vitrines agentiques que vous avez activées, indépendamment de /robots.txt. Pour contrôler ce flux, utilisez les réglages des vitrines agentiques de Shopify.

### Le support Shopify peut-il corriger mon robots.txt.liquid ?

Non. La page de Shopify dit que le support ne peut pas aider pour les modifications du fichier et suggère de faire appel à un Shopify Partner.

### Me faut-il un proxy Cloudflare devant Shopify ?

Shopify dit que la gestion des bots au niveau du réseau est assurée pour les boutiques hébergées sur Shopify, qu'il ne recommande pas de configuration proxy devant Shopify et qu'il n'en prend pas en charge.

## Sources

- [Shopify Help Center: Editing robots.txt.liquid](https://help.shopify.com/en/manual/promoting-marketing/seo/editing-robots-txt), lu le 21 octobre 2026
- [Shopify.dev: Customize robots.txt.liquid](https://shopify.dev/docs/storefronts/themes/seo/robots-txt), lu le 21 octobre 2026
