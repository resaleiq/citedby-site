title: WordPress.com : refus de l'IA via confidentialité, pas robots.txt
slug: wordpress-com
description: WordPress.com traite le refus de l'IA comme « Prevent third-party sharing » dans la confidentialité. Ce que dit son guide, relu le 5 octobre 2026.
section: platforms
locale: fr
cluster: Robots d'exploration IA par plateforme
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Quatre faits sur WordPress.com : Où Privacy settings, Pas Une modification de robots.txt, Guide relu 5 oct. 2026, Aussi Accès MCP pour agents
hero_sub: Réglages des robots d'exploration IA sur WordPress.com
hero_boxes: Où|Privacy settings; Pas|Une modification de robots.txt; Guide relu|5 oct. 2026; Aussi|Accès MCP pour agents
widget: on
related: /fr/platforms|Toutes les plateformes comparées; /fr/platforms/cloudflare|Cloudflare; /fr/bots|Robots d'exploration IA comparés; /fr/guides/cms|Checklist de visibilité IA pour Shopify, WooCommerce et plus
answer: Sur WordPress.com, le refus de l'IA est un réglage de confidentialité et non une modification de robots.txt. Son guide de visibilité du site, relu pour la dernière fois le 5 octobre 2026, dit que pour refuser le partage de votre contenu public avec des tiers, modèles d'IA compris, vous suivez son guide Prevent third-party sharing.

## Où se trouve le réglage sur WordPress.com

Le guide de visibilité de WordPress.com vous envoie vers Settings, puis Reading, pour Site Visibility (Public, Coming Soon ou Private), et vers un guide distinct, Prevent third-party sharing, pour le refus de l'IA.

## Ici, refuser l'IA est un réglage de partage

Le guide de WordPress.com sur le contrôle de la visibilité de votre site dit : pour refuser le partage du contenu public de votre site avec des tiers (modèles d'IA compris), consultez le guide Prevent third-party sharing. C'est un réglage de la plateforme, distinct du fichier robots.txt que lisent les robots de recherche et d'IA. La même page, relue pour la dernière fois le 5 octobre 2026, décrit aussi le sens inverse : vous pouvez connecter des agents d'IA externes comme ChatGPT ou Claude pour lire et modifier les réglages de visibilité de votre site, en activant l'accès par outil MCP. Nous n'avons pas pu lire le contenu du guide Prevent third-party sharing le 21 octobre : la page s'est chargée avec son titre et une date de relecture du 1er août 2024, mais sans aucune étape, par une simple requête comme dans un navigateur. Cette page ne décrit donc pas le fonctionnement de ce réglage ; ouvrez le guide depuis votre propre tableau de bord. Si vous utilisez WordPress auto-hébergé plutôt que WordPress.com, le fichier vous appartient et vous pouvez le modifier, comme chez n'importe quel hébergeur.

Dans les mots du fournisseur (original en anglais) : “To opt out of sharing your site's public content with third parties (including AI models), visit the Prevent third-party sharing guide.”

Source : [WordPress.com Support: Control your site's visibility](https://wordpress.com/support/privacy-settings/), lu le 21 octobre 2026.

## Les étapes

1. Ouvrez Settings, puis Reading, et vérifiez que Site Visibility est sur Public si vous voulez que les robots voient le site.
2. Ouvrez le guide Prevent third-party sharing de WordPress.com depuis l'aide sur les réglages de confidentialité et suivez-le si vous voulez refuser le partage de contenu avec des tiers, modèles d'IA compris.
3. Ouvrez yourdomain.com/robots.txt et lisez ce que votre site sert réellement aux robots.

## Les lignes à utiliser

Pour autoriser :

```
# No edit to make on WordPress.com for the sharing opt-out.
# Check what your site serves:
# https://yourdomain.com/robots.txt
```

Pour bloquer :

```
# On a self-hosted WordPress site, you add lines like these through your SEO plugin or the file:
User-agent: GPTBot
Disallow: /
```

## Pièges à éviter

Un site Coming Soon ou Private n'est pas la même chose qu'un refus de l'IA : il cache le site à tout le monde, moteurs de recherche compris, ce qui est le contraire de ce dont a besoin une boutique qui veut être citée.

## Comparer avec Cloudflare

[Cloudflare](/fr/platforms/cloudflare) : un interrupteur au niveau du réseau qui fonctionne quelle que soit la plateforme du site.

## Vérifier votre propre site

Le contrôle gratuit dans l'encadré ci-dessus lit robots.txt pour les robots d'exploration IA et envoie une requête réelle par robot. Une règle que les réglages de votre plateforme autorisent mais qu'un pare-feu refuse apparaît donc. La liste complète des robots se trouve sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Le refus de l'IA sur WordPress.com revient-il à bloquer GPTBot ?

WordPress.com le décrit comme un refus de partager votre contenu public avec des tiers, modèles d'IA compris. Il ne le décrit pas comme une règle robots.txt : vérifiez donc votre robots.txt en ligne pour voir ce qui est dit aux robots.

### Puis-je modifier robots.txt sur WordPress.com ?

Nous n'avons pas trouvé d'éditeur robots.txt dans le guide de visibilité que nous avons lu, donc nous ne nous prononçons ni dans un sens ni dans l'autre. Cherchez dans les réglages de votre site, selon votre offre.

### Qu'est-ce que l'accès par outil MCP ?

Le guide dit qu'il permet à des agents d'IA externes de lire et de modifier les réglages de visibilité de votre site. Il s'agit de gérer le site, pas des robots d'exploration.

## Sources

- [WordPress.com Support: Control your site's visibility](https://wordpress.com/support/privacy-settings/), lu le 21 octobre 2026
- [WordPress.com Support: Prevent third-party sharing](https://wordpress.com/support/privacy-settings/prevent-third-party-sharing/), lu le 21 octobre 2026
