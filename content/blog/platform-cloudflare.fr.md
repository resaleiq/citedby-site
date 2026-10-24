title: Cloudflare : politiques des bots IA Search, Agent et Training
slug: cloudflare
description: Cloudflare classe les bots IA en Search, Agent et Training, avec Block, Block on pages with ads et Allow. Nouvelles valeurs par défaut dès le 15 sept. 2026.
section: platforms
locale: fr
cluster: Robots d'exploration IA par plateforme
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Quatre faits sur Cloudflare : Où Security Settings, Comportements Search, Agent, Training, Choix 3 par comportement, Page mise à jour 1 juil. 2026
hero_sub: Réglages des robots d'exploration IA sur Cloudflare
hero_boxes: Où|Security Settings; Comportements|Search, Agent, Training; Choix|3 par comportement; Page mise à jour|1 juil. 2026
widget: on
related: /fr/platforms|Toutes les plateformes comparées; /fr/platforms/shopify|Shopify; /fr/bots|Robots d'exploration IA comparés; /fr/guides/cms|Checklist de visibilité IA pour Shopify, WooCommerce et plus
answer: Cloudflare range les bots IA en trois comportements : Search, Agent et Training. Pour chacun, vous choisissez Block on all pages, Block on pages with ads ou Allow, dans Security Settings, puis Configure AI bot policies. Sa page, mise à jour le 1er juillet 2026, indique que les nouvelles valeurs par défaut des nouveaux domaines démarrent le 15 septembre 2026.

## Où se trouve le réglage sur Cloudflare

Dans le tableau de bord Cloudflare, allez dans Security Settings, puis Configure AI bot policies. Chacun des trois comportements a son propre réglage. Cela fonctionne au niveau du réseau : le réglage s'applique donc quelle que soit la plateforme sur laquelle tourne le site.

## Trois comportements, trois choix et une date déjà passée

Les préréglages de Cloudflare sont les suivants. Search : les robots qui collectent ou indexent votre contenu pour répondre ensuite à des questions à son sujet. Agent : l'activité automatisée qui agit en temps réel pour le compte d'une personne, comme les bots de récupération de chat et les agents qui utilisent un navigateur. Training : les robots qui prennent votre contenu pour entraîner ou affiner un modèle, y compris les robots à usage mixte employés à la fois pour Training et pour Search. Chaque préréglage bloque les bots vérifiés classés ainsi, plus certains bots non vérifiés au comportement similaire. La page, mise à jour pour la dernière fois le 1er juillet 2026, annonce de nouvelles valeurs par défaut pour les nouveaux domaines à partir du 15 septembre 2026 : les bots Training et Agent bloqués sur les pages qui affichent des publicités, Search qui reste autorisé, et les robots à usage mixte bloqués par toute configuration qui bloque l'entraînement d'IA, y compris l'ancienne option Block AI bots, que la page signale comme obsolète à cette date. La page employait encore le futur quand nous l'avons lue le 21 octobre, cinq semaines après cette date : ouvrez donc votre propre tableau de bord et regardez ce qui est activé, plutôt que de vous fier à l'un ou l'autre texte.

Dans les mots du fournisseur (original en anglais) : “Search: crawlers that collect or index your content to answer questions about it later.”

Source : [Cloudflare Docs: Block AI Bots](https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/), lu le 21 octobre 2026.

## Les étapes

1. Ouvrez votre zone dans le tableau de bord Cloudflare et allez dans Security Settings.
2. Ouvrez Configure AI bot policies.
3. Pour Search, Agent et Training, choisissez Block on all pages, Block on pages with ads ou Allow.
4. Si vous utilisez l'ancienne option Block AI bots, vérifiez quels robots à usage mixte elle couvre désormais, car Cloudflare indique qu'elle devient obsolète.
5. Testez avec le [testeur gratuit d'accès des robots d'exploration IA](/fr/tools/ai-crawler-check) : un bot que robots.txt autorise peut quand même être refusé ici.

## Les lignes à utiliser

Pour autoriser :

```
# Cloudflare settings are not robots.txt lines.
# Choose Allow (do not block) for Search so answer engines can fetch pages.
```

Pour bloquer :

```
# Cloudflare settings are not robots.txt lines.
# Choose Block (on all pages) for Training; leave Search on Allow.
```

## Pièges à éviter

Pour une boutique qui veut être citée, le risque se trouve dans le préréglage du milieu : Cloudflare définit Agent comme les bots de récupération de chat qui agissent pour le compte d'une personne, ce qui est le rôle de robots comme [ChatGPT-User](/fr/bots/chatgpt-user). Bloquer Agent peut empêcher un assistant d'ouvrir votre page quand une personne l'interroge à son sujet, même si votre robots.txt l'autorise. Notez aussi que Shopify dit ne pas recommander de configuration proxy devant une boutique Shopify.

## Comparer avec Shopify

[Shopify](/fr/platforms/shopify) : dit assurer lui-même la gestion des bots et déconseille un proxy.

## Vérifier votre propre site

Le contrôle gratuit dans l'encadré ci-dessus lit robots.txt pour les robots d'exploration IA et envoie une requête réelle par robot. Une règle que les réglages de votre plateforme autorisent mais qu'un pare-feu refuse apparaît donc. La liste complète des robots se trouve sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Le blocage IA de Cloudflare l'emporte-t-il sur robots.txt ?

La page de Cloudflare décrit un blocage par comportement au niveau de son réseau : un bot peut donc y être refusé même quand votre robots.txt l'autorise. C'est pourquoi un test par requête réelle est utile.

### Quelle est la différence entre Search et Training sur Cloudflare ?

Les robots Search indexent le contenu pour répondre ensuite à des questions ; les robots Training prennent le contenu pour entraîner ou affiner un modèle. Les robots à usage mixte sont classés dans Training.

### Block AI bots est-il toujours disponible ?

Cloudflare le signale comme obsolète à la date du 15 septembre 2026. Sa page était encore rédigée au futur quand nous l'avons lue le 21 octobre 2026.

## Sources

- [Cloudflare Docs: Block AI Bots](https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/), lu le 21 octobre 2026
