title: Wix : bloquez les robots IA dans Robots.txt Editor (quatre noms)
slug: wix
description: La page d'aide de Wix dit de coller quatre user agents dans le Robots.txt Editor. Où se trouve l'éditeur, ce que l'exemple omet et l'option nosnippet.
section: platforms
locale: fr
cluster: Robots d'exploration IA par plateforme
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Quatre faits sur Wix : Où Robots.txt Editor, Noms d'exemple 4, Au niveau de la page balise nosnippet, Support Pas pour les modifications
hero_sub: Réglages des robots d'exploration IA sur Wix
hero_boxes: Où|Robots.txt Editor; Noms d'exemple|4; Au niveau de la page|balise nosnippet; Support|Pas pour les modifications
widget: on
related: /fr/platforms|Toutes les plateformes comparées; /fr/platforms/webflow|Webflow; /fr/bots|Robots d'exploration IA comparés; /fr/guides/cms|Checklist de visibilité IA pour Shopify, WooCommerce et plus
answer: Wix vous laisse modifier robots.txt : SEO & GEO dans le tableau de bord, puis Tools and settings, puis Robots.txt Editor. Sa page d'aide propose de coller quatre noms à bloquer : CCBot, GPTBot, ChatGPT-User et BingAI. ClaudeBot, PerplexityBot et Google-Extended ne figurent pas dans cet exemple : ajoutez-les vous-même si vous voulez les bloquer.

## Où se trouve le réglage sur Wix

Dans le tableau de bord de votre site, allez dans SEO & GEO, faites défiler jusqu'à Tools and settings, cliquez sur Robots.txt Editor, puis sur View File. Le guide d'édition distinct de Wix appelle cela une fonction avancée et dit que le Wix Customer Care ne peut pas aider pour les changements que vous apportez au fichier.

## L'exemple bloque quatre noms, et l'un d'eux ne figure pas sur la liste de Bing

La page d'aide de Wix dit que sa liste « comprend quelques robots d'exploration IA connus, mais vous pouvez toujours en ajouter d'autres ». Les quatre qu'elle affiche sont CCBot, GPTBot, ChatGPT-User et BingAI. Elle omet les jetons d'Anthropic, de Perplexity, de Google et de Meta qui apparaissent sur nos autres pages. « BingAI » est l'intrus : la page de Microsoft sur les robots que Bing utilise, lue le même jour, liste Bingbot, AdIdxBot, BingPreview, MicrosoftPreview et BingVideoPreview, et pas BingAI. Une règle pour un nom qu'aucun robot n'utilise ne fait rien : considérez donc la liste de Wix comme un point de départ et vérifiez-la sur la page de chaque opérateur. Notez aussi que [ChatGPT-User](/fr/bots/chatgpt-user) est le robot qui ouvre une page pour une personne qui interroge ChatGPT : le bloquer supprime donc cette voie d'accès à vos pages.

Dans les mots du fournisseur (original en anglais) : “This list includes some known AI crawlers, but you can always add more as needed.”

Source : [Wix Help Center: Blocking AI Crawlers from Your Site](https://support.wix.com/en/article/blocking-ai-crawlers-from-your-site), lu le 21 octobre 2026.

## Les étapes

1. Allez dans SEO & GEO dans le tableau de bord de votre site.
2. Faites défiler jusqu'à Tools and settings et cliquez sur Robots.txt Editor.
3. Cliquez sur View File, puis cliquez sur le champ sous Your robots.txt file.
4. Ajoutez les directives sous This is your current file, puis Save Changes et Save.
5. Pour une seule page, ouvrez SEO basics, Advanced SEO, Robots meta tag de la page, et cochez nosnippet. Wix dit que cela empêche l'utilisation du contenu comme entrée directe pour les aperçus IA.

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
User-agent: CCBot
Disallow: /

User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /
```

## Pièges à éviter

La FAQ de Wix dit que bloquer les robots d'exploration IA dans robots.txt peut limiter les fonctions de NLWeb, car les agents IA ont besoin d'accéder à votre contenu structuré. Elle dit aussi que certains robots ignorent robots.txt : un blocage n'est donc pas étanche.

## Comparer avec Webflow

[Webflow](/fr/platforms/webflow) : lui aussi un éditeur robots.txt, plus un en-tête Content-Signal.

## Vérifier votre propre site

Le contrôle gratuit dans l'encadré ci-dessus lit robots.txt pour les robots d'exploration IA et envoie une requête réelle par robot. Une règle que les réglages de votre plateforme autorisent mais qu'un pare-feu refuse apparaît donc. La liste complète des robots se trouve sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Bloquer les robots d'exploration IA nuira-t-il au SEO de mon site Wix ?

Wix dit que bloquer des robots d'exploration IA précis ne devrait pas affecter sensiblement le SEO, et recommande de vérifier ensuite vos statistiques.

### BingAI est-il un vrai robot d'exploration ?

Il ne figure pas sur la liste actuelle de Microsoft pour les robots de Bing, qui nomme Bingbot, AdIdxBot, BingPreview, MicrosoftPreview et BingVideoPreview. Voir la [page Bingbot](/fr/bots/bingbot).

### nosnippet bloque-t-il les robots d'exploration IA ?

Wix le décrit comme un moyen d'empêcher que votre contenu soit utilisé comme entrée directe pour les aperçus IA. C'est une balise au niveau de la page, pas un blocage de robot.

## Sources

- [Wix Help Center: Blocking AI Crawlers from Your Site](https://support.wix.com/en/article/blocking-ai-crawlers-from-your-site), lu le 21 octobre 2026
- [Wix Help Center: Editing Your Site's Robots.txt File](https://support.wix.com/en/article/editing-your-sites-robotstxt-file), lu le 21 octobre 2026
- [Microsoft Bing Webmaster help: Which Crawlers Does Bing Use?](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0), lu le 21 octobre 2026
