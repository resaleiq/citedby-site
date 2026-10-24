title: WP Engine : robots.txt, crawl-delay de 10 s par défaut, Web Rules
slug: wp-engine
description: Selon WP Engine, un robots.txt physique l'emporte sur les fichiers de plugin et fixe un crawl-delay de 10 secondes. Web Rules Engine refuse les bots par agent.
section: platforms
locale: fr
cluster: Robots d'exploration IA par plateforme
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur WP Engine : Où SFTP, Yoast ou Web Rules, Crawl-delay par défaut 10 secondes, Adresse wpengine.com Disallow all, Blocage par agent Web Rules Engine
hero_sub: Réglages des robots d'exploration IA sur WP Engine
hero_boxes: Où|SFTP, Yoast ou Web Rules; Crawl-delay|10 secondes par défaut; wpengine.com|Disallow all; Blocage par agent|Web Rules Engine
widget: on
related: /fr/platforms|Toutes les plateformes comparées; /fr/platforms/wordpress-com|WordPress.com; /fr/bots|Robots d'exploration IA comparés; /fr/guides/cms|Checklist de visibilité IA pour Shopify, WooCommerce et plus
answer: Selon WP Engine, un robots.txt physique à la racine l'emporte sur un fichier généré par un plugin ou un thème. Son fichier par défaut fixe un crawl-delay de 10 secondes, et les sites sur une adresse wpengine.com reçoivent un fichier qui interdit tout. Pour refuser un bot par user agent, WP Engine renvoie vers son Web Rules Engine.

## Où se trouve le réglage sur WP Engine

La page de WP Engine donne deux façons de créer le fichier. Avec le plugin Yoast SEO installé, allez dans SEO, puis Tools, choisissez l'éditeur de fichiers et sélectionnez Create robots.txt file. Ou créez vous-même un fichier robots.txt et envoyez-le par SFTP ou par SSH Gateway dans le répertoire racine de votre site. Pour bloquer par user agent, la page vous renvoie aux access rules du Web Rules Engine, dans le User Portal.

## Ce que dit la page de WP Engine et que les autres plateformes ne disent pas

WP Engine fournit un robots.txt par défaut, et la page dit ce qu'il contient. Sa note dit que le crawl-delay par défaut pour tous les sites est de 10 secondes, et que tout environnement sur une adresse wpengine.com reçoit un fichier qui interdit tout, pour éviter qu'un site soit indexé sur le mauvais domaine avant son lancement. Seuls les environnements qui utilisent un domaine personnalisé verront les modifications apportées à robots.txt. Un fichier physique que vous envoyez prend aussi le pas sur un fichier créé par un plugin ou un thème.

Dans les mots du fournisseur (original en anglais) : “This is what’s in the server’s default robots.txt file and can be overridden when you add a custom robots.txt file with one of the methods outlined in this article.”

Source : [WP Engine Support: Robots.txt and WordPress](https://wpengine.com/support/read-use-robots-txt/), lu le 24 octobre 2026.

## Les étapes

1. Créez un fichier nommé robots.txt. Le nom doit être en minuscules et l'extension doit être .txt, pas .html.
2. Ajoutez vos directives et enregistrez. Pour passer plutôt par un plugin, utilisez Yoast SEO, Tools, puis Create robots.txt file.
3. Envoyez le fichier par SFTP ou par SSH Gateway dans le répertoire racine de votre site.
4. Ouvrez /robots.txt sur votre domaine personnalisé en ligne pour le vérifier. Une copie sur une adresse wpengine.com n'affichera pas vos changements.
5. Pour refuser un bot au niveau du serveur à la place, ouvrez la page Sites dans le User Portal, sélectionnez l'environnement, cliquez sur Web Rules dans le menu secondaire de gauche (vous devrez peut-être déplier Advanced), choisissez Access rules et cliquez sur Add Rule.
6. Réglez Action sur Deny, IP sur All, et ajoutez une condition avec Type Header, Name User-Agent, Operator Regex matches (~) et le nom du user agent comme Value. Cliquez sur Add Rule pour enregistrer.

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

La page de WP Engine dit que les valeurs des directives sont sensibles à la casse et que les caractères génériques (globbing) et les expressions régulières ne sont pas entièrement pris en charge dans robots.txt.

## Pièges à éviter

La page ne nomme aucun robot d'exploration IA : ses exemples utilisent BadBotName, Googlebot, bingbot et SEMrush. Elle dit aussi que les robots ne sont pas obligés de suivre robots.txt, et recommande un pare-feu comme Sucuri WAF ou Cloudflare, ou de contacter le support, pour arrêter les acteurs malveillants avant qu'ils atteignent le site. Selon la page du Web Rules Engine, une requête refusée par une règle d'accès de Web Rules reçoit une réponse 403 Forbidden et n'est pas comptée dans les visites facturables. Votre robots.txt personnalisé l'emporte sur le fichier par défaut, y compris sa ligne de crawl-delay de 10 secondes : ajoutez vous-même une ligne Crawl-delay si vous voulez en garder une.

## Comparer avec WordPress.com

[WordPress.com](/fr/platforms/wordpress-com) : un refus de l'IA dans les réglages de confidentialité plutôt qu'un fichier robots.txt que vous écrivez.

## Vérifier votre propre site

Le contrôle gratuit dans l'encadré ci-dessus lit robots.txt pour les robots d'exploration IA et envoie une requête réelle par robot. Une règle que les réglages de votre plateforme autorisent mais qu'un pare-feu refuse apparaît donc. La liste complète des robots se trouve sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Pourquoi mon site de préproduction sur WP Engine ignore-t-il mon robots.txt ?

WP Engine dit que les sites sur une adresse environment.wpengine.com reçoivent automatiquement un robots.txt qui interdit tout, et que seuls les environnements avec un domaine personnalisé voient les changements apportés au fichier. Les comptes partagés ne peuvent ajouter un domaine personnalisé qu'à Production : Staging et Development n'afficheront donc généralement pas vos modifications.

### Un plugin robots.txt l'emporte-t-il sur un fichier que j'envoie à WP Engine ?

Non, c'est l'inverse. WP Engine dit qu'un robots.txt physique à la racine de votre site écrase tout fichier généré dynamiquement par un plugin ou un thème.

## Sources

- [WP Engine Support: Robots.txt and WordPress](https://wpengine.com/support/read-use-robots-txt/), lu le 24 octobre 2026
- [WP Engine Support: Web Rules Engine](https://wpengine.com/support/web-rules-engine/), lu le 24 octobre 2026
