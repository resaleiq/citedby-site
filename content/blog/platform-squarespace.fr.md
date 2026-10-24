title: Squarespace : la case des robots IA bloque 26 bots, pas ChatGPT
slug: squarespace
description: Le panneau Crawlers de Squarespace a une case qui bloque les robots IA connus. Les 26 noms omettent les bots de recherche et utilisateur de ChatGPT.
section: platforms
locale: fr
cluster: Robots d'exploration IA par plateforme
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Quatre faits sur Squarespace : Où Settings, Crawlers, Noms bloqués 26, Modifier robots.txt Non, Entraînement passé Non retiré
hero_sub: Réglages des robots d'exploration IA sur Squarespace
hero_boxes: Où|Settings, Crawlers; Noms bloqués|26; Modifier robots.txt|Non; Entraînement passé|Non retiré
widget: on
related: /fr/platforms|Toutes les plateformes comparées; /fr/platforms/wix|Wix; /fr/bots|Robots d'exploration IA comparés; /fr/guides/cms|Checklist de visibilité IA pour Shopify, WooCommerce et plus
answer: Squarespace a une seule case à cocher : Settings, puis Crawlers, puis Block known artificial intelligence crawlers. Elle ajoute 26 bots nommés à votre robots.txt. La liste comprend GPTBot, ClaudeBot et DuckAssistBot, mais pas OAI-SearchBot, ChatGPT-User ni PerplexityBot, et vous ne pouvez pas modifier robots.txt vous-même.

## Où se trouve le réglage sur Squarespace

Ouvrez le panneau Settings, cliquez sur Crawlers et cochez Block known artificial intelligence crawlers. La page de Squarespace dit que cocher la case met à jour votre fichier robots.txt pour les bots listés ci-dessous, et qu'il peut en ajouter d'autres avec le temps.

## Les 26 noms, et ceux qui manquent

La page d'aide de Squarespace liste exactement 26 noms : AI2Bot, Ai2Bot-Dolma, aiHitBot, Amazonbot, anthropic-ai, Applebot-Extended, Bytespider, CCBot, ClaudeBot, cohere-ai, cohere-training-data-crawler, DuckAssistBot, FacebookBot, Google-Extended, GoogleOther, GoogleOther-Image, GoogleOther-Video, GPTBot, img2dataset, Meta-ExternalAgent, MyCentralAIScraperBot, omgili, omgilibot, Quora-Bot, TikTokSpider et YouBot. Rapprochée de nos propres pages sur les robots, la case couvre les robots d'entraînement et de jeux de données d'OpenAI, d'Anthropic, de Google, d'Apple, de Meta et de Common Crawl. Elle ne nomme pas [OAI-SearchBot](/fr/bots/oai-searchbot), [ChatGPT-User](/fr/bots/chatgpt-user), [PerplexityBot](/fr/bots/perplexitybot), [Claude-SearchBot](/fr/bots/claude-searchbot) ni [Claude-User](/fr/bots/claude-user) : la cocher ne vous retire donc pas de la recherche de ChatGPT. Elle nomme en revanche [DuckAssistBot](/fr/bots/duckassistbot) et [Amazonbot](/fr/bots/amazonbot), qui sont des robots d'exploration pour les réponses IA et pour les produits : la cocher peut donc aussi vous faire perdre les réponses IA de DuckDuckGo.

Dans les mots du fournisseur (original en anglais) : “Checking the box updates your robots.txt file to tell the following bots not to crawl your site.”

Source : [Squarespace Help: Request that AI models exclude your site](https://support.squarespace.com/hc/en-us/articles/360022347072-Request-that-AI-models-exclude-your-site), lu le 21 octobre 2026.

## Les étapes

1. Ouvrez le panneau Settings de votre site Squarespace.
2. Cliquez sur Crawlers.
3. Cochez Block known artificial intelligence crawlers pour bloquer les 26 noms, ou laissez la case décochée pour les laisser tous autorisés.
4. Pour demander l'ajout d'un autre bot, contactez Squarespace : le texte de la page dit que vous pouvez en faire la demande.

## Les lignes à utiliser

Pour autoriser :

```
# Squarespace sites are open to these crawlers while the box is unticked.
# You cannot add lines yourself, so there is nothing to paste.
```

Pour bloquer :

```
# Written by Squarespace when the box is ticked (excerpt):
User-agent: GPTBot
User-agent: ClaudeBot
User-agent: CCBot
Disallow: /
```

## Pièges à éviter

Squarespace indique que cocher la case ne retire pas rétroactivement des données d'entraînement des modèles d'IA le contenu déjà récupéré sur votre site. Il dit aussi que robots.txt n'est qu'une demande que les robots bien intentionnés ont proposé de respecter. L'extrait ci-dessus est notre illustration abrégée du type de lignes que produit la case ; le fichier exact est celui que votre site sert à /robots.txt : ouvrez-le et lisez-le.

## Comparer avec Wix

[Wix](/fr/platforms/wix) : un vrai éditeur de robots.txt, et une liste d'exemples de quatre noms.

## Vérifier votre propre site

Le contrôle gratuit dans l'encadré ci-dessus lit robots.txt pour les robots d'exploration IA et envoie une requête réelle par robot. Une règle que les réglages de votre plateforme autorisent mais qu'un pare-feu refuse apparaît donc. La liste complète des robots se trouve sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Puis-je autoriser la recherche de ChatGPT mais bloquer l'entraînement sur Squarespace ?

En partie. Cocher la case écrit une règle pour GPTBot, et OAI-SearchBot ne figure pas parmi les 26 noms. Vous ne pouvez pas ajouter de lignes vous-même : ouvrez donc votre /robots.txt en ligne pour confirmer ce qu'il dit.

### Puis-je modifier robots.txt sur Squarespace ?

La page de Squarespace traite le panneau Crawlers comme le moyen de contrôle et ne propose pas d'éditeur robots.txt. Wix et Webflow en proposent un.

### La case empêche-t-elle Google d'indexer mon site ?

Non. Elle est distincte de l'option sur les robots des moteurs de recherche, dans le même panneau. La case IA nomme Google-Extended et GoogleOther, pas Googlebot.

## Sources

- [Squarespace Help: Request that AI models exclude your site](https://support.squarespace.com/hc/en-us/articles/360022347072-Request-that-AI-models-exclude-your-site), lu le 21 octobre 2026
