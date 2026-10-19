title: Visibilité IA sur Shopify, WooCommerce et autres : checklist
h1: Visibilité IA sur Shopify, WooCommerce et les autres plateformes : la checklist par plateforme
description: Où modifier robots.txt, où trouver le sitemap, comment vérifier le JSON-LD produit et repérer le texte en JavaScript, sur Shopify, WordPress et WooCommerce.
slug: cms
section: guides
locale: fr
cluster: Exploration par les robots
date: 2026-10-20
reviewed: 2026-10-20
hero: auto
hero_alt: Carte de titre : checklist de visibilité IA pour Shopify, WooCommerce et autres plateformes, avec quatre contrôles
hero_sub: robots.txt, sitemap, JSON-LD, texte lisible
hero_boxes: robots.txt|où le modifier; Sitemap|où le trouver; JSON-LD produit|prix et stock; Texte en JavaScript|à repérer
widget: on
steps_img: on
howto: on
related: /fr/guides/technical-seo-checklist|Checklist SEO technique pour la visibilité IA; /fr/blog/is-gptbot-blocked|GPTBot est-il bloqué sur votre site ?; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ?
answer: Sur Shopify, robots.txt se modifie avec le modèle robots.txt.liquid du thème et le sitemap existe déjà à /sitemap.xml. Sur WordPress, le sitemap natif est /wp-sitemap.xml. Pour toutes les plateformes, contrôlez le prix dans le JSON-LD et le texte dans le code source de la fiche produit. Les réglages exacts dépendent de votre version.

## Pourquoi vérifier sa plateforme avant son contenu ?

Votre plateforme décide à votre place d'une partie de ce que les robots voient : le fichier robots.txt, le sitemap, le balisage produit et la façon dont le texte arrive dans la page. Un thème ou un plugin peut changer ces réglages sans que vous le remarquiez. Les contrôles ci-dessous sont les mêmes pour toutes les boutiques en ligne, la différence tient à l'endroit où l'on clique.

Pour les neuf contrôles techniques en général, voyez la [checklist SEO technique](/fr/guides/technical-seo-checklist).

## Comment vérifier sa boutique, quelle que soit la plateforme ?

1. Ouvrez robots.txt : tapez `votre-boutique.fr/robots.txt` et cherchez un `Disallow: /` général ou une règle qui nomme `OAI-SearchBot`, `GPTBot` ou `PerplexityBot`.
2. Trouvez le sitemap : essayez `/sitemap.xml`, puis regardez la dernière ligne de robots.txt, qui l'indique souvent.
3. Lisez le JSON-LD d'une fiche produit : affichez le code source (clic droit, Afficher le code source de la page), cherchez `application/ld+json` et relisez le prix, la devise et la disponibilité.
4. Cherchez le texte dans le code source : le nom du produit et sa description doivent y figurer. Dans l'inspecteur du navigateur, ils apparaissent même quand un script les ajoute, ce qui masque le problème.
5. Contrôlez les extensions : désactivez un à un les modules d'avis, de variantes ou de description en onglets, et vérifiez si le texte disparaît du code source.

## Que faire sur Shopify ?

D'après le centre d'aide de Shopify, chaque boutique a un fichier robots.txt par défaut, optimisé pour le référencement. Pour le personnaliser, il faut ajouter un modèle `robots.txt.liquid` au dossier des modèles du thème : depuis l'administration, ouvrez les thèmes de la boutique en ligne, puis l'éditeur de code, et ajoutez un nouveau modèle de type robots. Shopify précise que c'est une personnalisation non prise en charge par son support et qu'une erreur peut faire perdre tout le trafic ([Shopify : modifier robots.txt.liquid](https://help.shopify.com/en/manual/promoting-marketing/seo/editing-robots-txt)).

Le sitemap est généré automatiquement et se trouve à la racine du domaine, par exemple `votre-boutique.fr/sitemap.xml`. Il renvoie vers des sitemaps séparés pour produits, collections, blogs et pages, et se met à jour tout seul ([Shopify : trouver et soumettre votre sitemap](https://help.shopify.com/en/manual/promoting-marketing/seo/find-site-map)).

Pour les assistants, Shopify distingue deux couches. Les règles de robots.txt agissent sur la découverte par le web ouvert. Les données produit envoyées vers les vitrines d'agents, comme ChatGPT ou Microsoft Copilot, passent par Shopify Catalog, indépendamment de robots.txt. Bloquer un robot dans robots.txt ne coupe donc pas ce canal, selon la même page d'aide.

Shopify propose aussi une page sur l'optimisation d'une boutique pour l'IA, qui recommande des fiches produit détaillées avec données structurées et attributs produit ([Shopify : optimiser votre boutique pour l'IA](https://help.shopify.com/en/manual/promoting-marketing/seo/optimizing-store-for-ai)).

## Que faire sur WordPress et WooCommerce ?

Depuis la version 5.5, WordPress expose un index de sitemaps à l'adresse `/wp-sitemap.xml`, et le robots.txt qu'il génère le référence ([WordPress : sitemaps XML dans le noyau](https://make.wordpress.org/core/2020/07/22/new-xml-sitemaps-functionality-in-wordpress-5-5/)). Si vous utilisez une extension de référencement, elle peut proposer son propre sitemap : regardez lequel est annoncé dans votre robots.txt.

WooCommerce fonctionne sur WordPress, donc les mêmes adresses s'appliquent. Pour robots.txt, les réglages de votre extension de référencement ou de sécurité sont le premier endroit à regarder. Pour le JSON-LD, comparez le bloc présent dans le code source avec le prix affiché : si une extension ajoute un second bloc Product, les deux doivent dire la même chose.

## Et sur PrestaShop, Wix ou une autre plateforme ?

Nous n'avons pas vérifié leurs pages d'aide publiques pour ce guide, nous ne détaillons donc pas leurs menus. La démarche reste celle des cinq contrôles ci-dessus : lisez robots.txt, trouvez le sitemap, relisez le JSON-LD et le texte du code source, puis cherchez dans les paramètres de votre plateforme, ou dans l'aide de votre éditeur, comment modifier ce qui ne va pas.

## Que dit Google du balisage produit ?

Google explique qu'avec des données structurées sur vos fiches produit, les internautes peuvent voir prix, disponibilité, avis, informations de livraison directement dans les résultats. Il distingue les extraits de produit (pages où l'on ne peut pas acheter) et les fiches marchands (pages d'achat), qui acceptent plus de détails comme la livraison et la politique de retour ([Google : données structurées Product](https://developers.google.com/search/docs/appearance/structured-data/product)). Pour une boutique, c'est la seconde catégorie qui vous concerne.

## FAQ

### Dois-je modifier robots.txt sur Shopify pour apparaître dans ChatGPT ?
Pas forcément. Shopify indique que son robots.txt par défaut convient à la plupart des boutiques. Modifiez-le seulement si vous voulez autoriser ou bloquer un robot précis.

### Où trouve-t-on le sitemap d'une boutique WooCommerce ?
Essayez `/wp-sitemap.xml`, le sitemap natif de WordPress. Si vous avez une extension de référencement, regardez l'adresse annoncée dans robots.txt.

### Le prix du JSON-LD doit-il être identique à celui de la page ?
Oui. Une valeur périmée dans le balisage peut conduire un assistant à citer l'ancien prix. Nous détaillons ce cas dans [ChatGPT affiche un ancien prix](/fr/blog/chatgpt-wrong-price).

### Un plugin peut-il rendre ma page vide pour les robots ?
Oui, si le texte est ajouté par un script. Regardez le code source de la page, pas l'inspecteur, pour voir ce que reçoit un robot qui n'exécute pas JavaScript.

## Sources

- [Shopify : modifier robots.txt.liquid](https://help.shopify.com/en/manual/promoting-marketing/seo/editing-robots-txt)
- [Shopify : trouver et soumettre votre sitemap](https://help.shopify.com/en/manual/promoting-marketing/seo/find-site-map)
- [Shopify : optimiser votre boutique pour l'IA](https://help.shopify.com/en/manual/promoting-marketing/seo/optimizing-store-for-ai)
- [WordPress : sitemaps XML dans le noyau, version 5.5](https://make.wordpress.org/core/2020/07/22/new-xml-sitemaps-functionality-in-wordpress-5-5/)
- [Google Search Central : données structurées Product](https://developers.google.com/search/docs/appearance/structured-data/product)
