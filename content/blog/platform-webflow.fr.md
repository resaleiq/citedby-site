title: Webflow : règles robots.txt et en-tête Content-Signal pour l'IA
slug: webflow
description: Où se trouve l'éditeur robots.txt de Webflow, l'offre requise, et comment l'en-tête Content-Signal sépare entraînement IA, recherche et entrée IA.
section: platforms
locale: fr
cluster: Robots d'exploration IA par plateforme
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Quatre faits sur Webflow : Où Site settings, SEO, Requis Offre Site ou Workspace payante, En plus Content-Signal, Statut Extension proposée
hero_sub: Réglages des robots d'exploration IA sur Webflow
hero_boxes: Où|Site settings, SEO; Requis|Offre Site ou Workspace payante; En plus|Content-Signal; Statut|Extension proposée
widget: on
related: /fr/platforms|Toutes les plateformes comparées; /fr/platforms/wix|Wix; /fr/bots|Robots d'exploration IA comparés; /fr/guides/cms|Checklist de visibilité IA pour Shopify, WooCommerce et plus
answer: Webflow place robots.txt dans Site settings, puis SEO, puis Indexing, et l'une de ses pages d'aide dit qu'il faut une offre Site ou une offre Workspace payante. Il peut aussi envoyer un en-tête Content-Signal qui règle séparément ai-train, search et ai-input. Webflow parle d'une extension proposée, et non d'une norme acceptée.

## Où se trouve le réglage sur Webflow

Allez dans Site settings, puis SEO, puis Indexing, ajoutez la ou les règles robots.txt voulues, puis cliquez sur Save et publiez votre site. Webflow ajoute une ligne Sitemap par défaut ; un interrupteur la retire.

## Un en-tête qui sépare l'entraînement, la recherche et les réponses IA

En plus de robots.txt, la page de Webflow dit qu'un site peut servir un en-tête HTTP Content-Signal, réglé dans la même zone Indexing, pour donner des instructions plus fines aux robots d'exploration IA. Son exemple est `Content-Signal: ai-train=no, search=yes, ai-input=no`. Webflow explique la séparation : robots.txt contrôle si les bots peuvent accéder à vos pages, tandis que Content-Signal dit si le contenu peut être utilisé pour l'entraînement d'IA, l'indexation de recherche ou les réponses générées par l'IA, séparément. Webflow ajoute lui-même la réserve : cela repose sur une extension proposée de la RFC 9309 et n'est pas encore une norme acceptée. Il énonce donc une préférence ; il n'arrête pas un robot, et la page de Webflow ne dit pas quels robots le lisent.

Dans les mots du fournisseur (original en anglais) : “This is based on a proposed extension to RFC 9309 and is not yet an accepted standard.”

Source : [Webflow Help: Set robots.txt rules](https://help.webflow.com/hc/en-us/articles/41954080897683-Set-robots-txt-rules), lu le 21 octobre 2026.

## Les étapes

1. Ouvrez Site settings et allez dans SEO, puis Indexing.
2. Saisissez les règles robots.txt voulues dans le champ des règles.
3. Si vous le souhaitez, réglez l'en-tête Content-Signal dans la même zone.
4. Cliquez sur Save et publiez votre site, puis ouvrez yourdomain.com/robots.txt pour vérifier le fichier en ligne.

## Les lignes à utiliser

Pour autoriser :

```
User-agent: OAI-SearchBot
Allow: /

User-agent: *
Allow: /
```

Pour bloquer :

```
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

Content-Signal: ai-train=no, search=yes, ai-input=no
```

## Pièges à éviter

La page de Webflow dit que votre robots.txt est visible publiquement : ne comptez donc pas sur lui pour cacher des pages privées. Elle dit aussi que tous les bots ne le suivent pas.

## Comparer avec Wix

[Wix](/fr/platforms/wix) : un chemin d'édition plus long et un exemple de quatre noms.

## Vérifier votre propre site

Le contrôle gratuit dans l'encadré ci-dessus lit robots.txt pour les robots d'exploration IA et envoie une requête réelle par robot. Une règle que les réglages de votre plateforme autorisent mais qu'un pare-feu refuse apparaît donc. La liste complète des robots se trouve sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Me faut-il une offre payante pour robots.txt sur Webflow ?

Une page d'aide de Webflow dit qu'il faut une offre Site ou une offre Workspace payante pour ajouter un fichier robots.txt à votre site.

### Qu'est-ce que Content-Signal ?

Une extension proposée de la RFC 9309 que Webflow peut envoyer sous forme d'en-tête : ai-train, search et ai-input, chacun réglé sur yes ou no.

### Webflow bloque-t-il les mauvais bots à ma place ?

Sa page d'aide montre comment écrire une règle pour un bot nommé. Elle dit que certains bots, surtout les malveillants, ne suivent pas robots.txt.

## Sources

- [Webflow Help: Set robots.txt rules](https://help.webflow.com/hc/en-us/articles/41954080897683-Set-robots-txt-rules), lu le 21 octobre 2026
- [Webflow Help: Request to block specific bots from visiting your site](https://help.webflow.com/hc/en-us/articles/41954183592851-Request-to-block-specific-bots-from-visiting-your-site), lu le 21 octobre 2026
