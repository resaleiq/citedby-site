title: Vercel : le jeu de règles AI Bots dans le Firewall (Log ou Deny)
slug: vercel
description: Vercel bloque les bots IA via un jeu de règles du Firewall, pas robots.txt : où est l'AI Bots Ruleset, les actions Log et Deny, et sa liste de bots à jour.
section: platforms
locale: fr
cluster: Robots d'exploration IA par plateforme
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur Vercel : Où Firewall, Rules, Offres Toutes les offres, Par défaut Allow (inactif), Actions Log ou Deny
hero_sub: Réglages des robots d'exploration IA sur Vercel
hero_boxes: Où|Firewall, Rules; Offres|Toutes les offres; Par défaut|Allow (inactif); Actions|Log ou Deny
widget: on
related: /fr/platforms|Toutes les plateformes comparées; /fr/platforms/cloudflare|Cloudflare; /fr/bots|Robots d'exploration IA comparés; /fr/guides/cms|Checklist de visibilité IA pour Shopify, WooCommerce et plus
answer: Vercel gère les bots IA avec un jeu de règles du Firewall, pas avec une ligne robots.txt. Dans votre projet, ouvrez Firewall, puis Rules, et réglez l'AI Bots Ruleset sur Log ou Deny. Il est disponible sur toutes les offres et démarre inactif, affiché comme Allow : rien n'est bloqué tant que vous ne le changez pas.

## Où se trouve le réglage sur Vercel

Depuis le tableau de bord de votre projet, ouvrez Firewall dans la barre latérale, puis Rules. Dans la section Bot Management, vous trouverez la règle AI Bots Ruleset. La documentation de Vercel dit que ce jeu de règles est disponible sur toutes les offres.

## Ce que dit la page de Vercel et que les autres plateformes ne disent pas

Vous n'avez pas à tenir à jour la liste des bots IA de Vercel. Le jeu de règles couvre les bots IA qui explorent le web pour des données d'entraînement, pour la recherche ou pour des récupérations déclenchées par un utilisateur, et Vercel tient la liste à jour. La même page dit que le jeu de règles est inactif par défaut et affiché comme Allow dans le tableau de bord : le trafic correspondant n'est donc pas évalué et atteint votre application. Le contrôle se résume à une action pour tout le jeu de règles, Log ou Deny, appliquée au niveau du Firewall.

Dans les mots du fournisseur (original en anglais) : “When new AI bots emerge, Vercel automatically adds them to its managed list and handles them according to your existing configured action without requiring any changes on your part.”

Source : [Vercel Docs: Bot Management](https://vercel.com/docs/bot-management), lu le 24 octobre 2026.

## Les étapes

1. Depuis le tableau de bord de votre projet, ouvrez Firewall dans la barre latérale.
2. Ouvrez Rules dans la barre latérale.
3. Dans la section Bot Management, sélectionnez Log ou Deny sur la règle AI Bots Ruleset. Log enregistre le trafic des bots IA sans le bloquer et sert à la surveillance. Deny bloque tout le trafic identifié comme venant de bots IA.
4. Quand vous faites un changement, un bouton Review Changes apparaît avec le nombre de changements. Sélectionnez Review Changes, vérifiez-les, puis sélectionnez Publish pour appliquer les changements à votre déploiement de production.

## Les lignes à utiliser

Les pages de Vercel décrivent cela comme un réglage du Firewall : il n'y a donc aucune ligne robots.txt à ajouter. Les deux états sont les suivants :

Pour autoriser :

```
AI Bots Ruleset: Allow (the default, ruleset inactive)
```

Pour bloquer :

```
AI Bots Ruleset: Deny
```

## Pièges à éviter

Deny bloque tout le trafic identifié comme venant de bots IA, et le périmètre du jeu de règles couvre ensemble l'entraînement, la recherche et les récupérations déclenchées par un utilisateur : ce n'est donc pas un moyen de bloquer les bots d'entraînement tout en gardant les bots de recherche. Log est la première étape la plus prudente. La page de Vercel ne dit pas comment le jeu de règles s'articule avec votre robots.txt : vérifiez donc séparément ce que dit votre propre fichier. Pour des bots précis, la même page dit que vous pouvez bloquer une partie ou la totalité des bots de son répertoire de bots vérifiés avec des règles personnalisées du WAF qui utilisent la condition de correspondance User Agent ou l'en-tête Signature-Agent.

## Comparer avec Cloudflare

[Cloudflare](/fr/platforms/cloudflare) : lui aussi un interrupteur au niveau du réseau, avec trois actions pour chacun de Search, Agent et Training.

## Vérifier votre propre site

Le contrôle gratuit dans l'encadré ci-dessus lit robots.txt pour les robots d'exploration IA et envoie une requête réelle par robot. Une règle que les réglages de votre plateforme autorisent mais qu'un pare-feu refuse apparaît donc. La liste complète des robots se trouve sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Vercel bloque-t-il les bots IA par défaut ?

Non. La documentation de Vercel dit que l'AI Bots Ruleset est inactif par défaut, affiché comme Allow dans le tableau de bord, et que le trafic correspondant n'est pas évalué et atteint votre application.

### Dois-je tenir à jour la liste des bots IA de Vercel ?

Non. Vercel dit que la liste des bots IA connus est maintenue et mise à jour automatiquement par Vercel, et que les nouveaux bots sont traités selon l'action que vous avez déjà réglée.

## Sources

- [Vercel Docs: Bot Management](https://vercel.com/docs/bot-management), lu le 24 octobre 2026
- [Vercel Docs: WAF Managed Rulesets](https://vercel.com/docs/vercel-firewall/vercel-waf/managed-rulesets), lu le 24 octobre 2026
