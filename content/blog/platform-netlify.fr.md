title: Netlify : robots.txt et User Agent Blocker contre les robots IA
slug: netlify
description: Netlify n'a pas de réglage robots.txt : servez un fichier depuis la racine du site, ou installez User Agent Blocker. Son guide dit d'utiliser les deux.
section: platforms
locale: fr
cluster: Robots d'exploration IA par plateforme
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur Netlify : Où robots.txt à la racine du site, Blocage en périphérie User Agent Blocker, Activation Un projet à la fois, Solution de repli Edge Function
hero_sub: Réglages des robots d'exploration IA sur Netlify
hero_boxes: Où|robots.txt à la racine du site; Blocage en périphérie|User Agent Blocker; Activation|Un projet à la fois; Solution de repli|Edge Function
widget: on
related: /fr/platforms|Toutes les plateformes comparées; /fr/platforms/cloudflare|Cloudflare; /fr/bots|Robots d'exploration IA comparés; /fr/guides/cms|Checklist de visibilité IA pour Shopify, WooCommerce et plus
answer: Netlify vous donne deux voies. La première est un fichier robots.txt servi depuis la racine de votre site. La seconde est l'extension User Agent Blocker, qui utilise une Netlify Edge Function pour bloquer les requêtes selon le user agent. Le guide pour développeurs de Netlify dit que robots.txt seul ne suffit pas, car certains produits d'IA l'ignorent.

## Où se trouve le réglage sur Netlify

Il n'y a aucun éditeur robots.txt dans les pages du tableau de bord que nous avons lues. Le guide pour développeurs de Netlify dit d'énoncer vos règles dans un fichier robots.txt « servi depuis la racine de votre site ». La page distincte de la documentation sur le blocage des robots d'exploration IA traite de l'extension User Agent Blocker, que vous trouvez sous Extensions dans la navigation de gauche de votre projet, une fois l'extension installée.

## Ce que disent les pages de Netlify et que les autres plateformes ne disent pas

Le guide de Netlify traite robots.txt comme la première de deux couches, et non comme la réponse complète. Il montre un robots.txt avec un bloc User-agent et Disallow par bot, généré à partir d'une liste JSON de noms. Il ajoute ensuite une Edge Function qui compare l'en-tête User-Agent de chaque requête à la même liste et renvoie un code HTTP 401 en cas de correspondance. Il dit que certains produits d'IA ne respectent pas robots.txt, puis ajoute que la vérification du user agent a elle aussi une faille.

Dans les mots du fournisseur (original en anglais) : “Sadly, some bots have been found to mis-report their names in their User Agent strings, so we can’t rely on that technique alone either.”

Source : [Netlify Developers: Blocking AI bots and controlling crawlers](https://developers.netlify.com/guides/blocking-ai-bots-and-controlling-crawlers/), lu le 24 octobre 2026.

## Les étapes

1. Écrivez un robots.txt avec une ligne User-agent et Disallow: / pour chaque bot que vous voulez bloquer, et servez-le depuis la racine de votre site. Le guide génère le fichier à partir d'une liste de noms avec un petit script de build, pour éviter les fautes de frappe.
2. Déployez le site. Le guide note que les robots d'exploration IA « devraient » respecter le fichier, ce qui explique qu'il ajoute une seconde couche.
3. Pour l'extension : dans le tableau de bord de votre projet Netlify, sélectionnez Extensions dans la barre latérale de gauche, cherchez User Agent Blocker, sélectionnez-la, puis sélectionnez Install. L'extension devient alors disponible pour tous les projets de votre équipe Netlify.
4. Allez dans le projet où vous voulez l'activer. Vous ne pouvez activer l'extension que pour un seul projet à la fois. Sous Extensions dans la navigation de gauche, sélectionnez User Agent Blocker.
5. Sous Block User Agents, sélectionnez le trafic à bloquer. Pour cibler les robots d'exploration et les bots IA, sélectionnez toutes les options de robots d'exploration IA.
6. Sélectionnez Redeploy site et confirmez avec Save, puis sélectionnez Enable analytics and deploy site. Netlify dit que le blocage commence à fonctionner immédiatement une fois le déploiement réussi.

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

Les pages de Netlify ne montrent que des règles Disallow. Les lignes Allow ci-dessus relèvent du robots.txt standard, et non de quelque chose que Netlify documente.

## Pièges à éviter

Netlify dit que la liste prédéfinie de l'extension « ne comprend pas tous les robots d'exploration et bots IA possibles » : un robot absent de la liste n'est donc pas bloqué. La même page liste les robots d'exploration SEO et de recherche à côté de ceux de l'IA : sélectionnez donc uniquement les options IA si vous voulez conserver le trafic de recherche. L'exemple d'Edge Function du guide répond par un 401 à chaque requête correspondante, sur l'ensemble du site.

## Comparer avec Cloudflare

[Cloudflare](/fr/platforms/cloudflare) : un interrupteur au niveau du réseau qui fonctionne quelle que soit la plateforme du site, alors que l'extension de Netlify agit projet par projet.

## Vérifier votre propre site

Le contrôle gratuit dans l'encadré ci-dessus lit robots.txt pour les robots d'exploration IA et envoie une requête réelle par robot. Une règle que les réglages de votre plateforme autorisent mais qu'un pare-feu refuse apparaît donc. La liste complète des robots se trouve sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### robots.txt suffit-il pour bloquer les bots IA sur Netlify ?

Le guide de Netlify dit que non. Il dit que tous les produits d'IA ne respectent pas robots.txt et recommande d'ajouter une Edge Function, ou l'extension User Agent Blocker, qui bloque selon le user agent. Il dit aussi que certains bots déclarent un faux user agent : les deux couches ensemble sont donc sa réponse.

### Puis-je activer User Agent Blocker pour tous les projets à la fois ?

Pas selon la documentation de Netlify. L'installer rend l'extension disponible pour tous les projets de votre équipe, mais vous ne pouvez l'activer que pour un projet à la fois.

## Sources

- [Netlify Developers: Blocking AI bots and controlling crawlers](https://developers.netlify.com/guides/blocking-ai-bots-and-controlling-crawlers/), lu le 24 octobre 2026
- [Netlify Docs: Block AI crawlers and bots](https://docs.netlify.com/build/build-with-ai/block-ai-crawlers), lu le 24 octobre 2026
