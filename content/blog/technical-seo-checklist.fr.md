title: Checklist SEO technique : visibilité IA d'une boutique
h1: Checklist SEO technique pour la visibilité IA : 9 contrôles à faire à la main sur votre boutique en ligne
description: Neuf vérifications pour qu'un assistant IA lise votre boutique : robots.txt, codes HTTP, sitemap, canonical, JSON-LD, texte dans le HTML. Test manuel inclus.
slug: technical-seo-checklist
section: guides
locale: fr
cluster: Exploration par les robots
date: 2026-10-20
reviewed: 2026-10-20
hero: auto
hero_alt: Carte de titre : neuf contrôles techniques, de robots.txt au texte présent dans le HTML, pour qu'une boutique soit lisible par les IA
hero_sub: 9 contrôles, chacun testable à la main
hero_boxes: Accès|robots.txt et codes HTTP; Index|sitemap et canonical; Contenu|texte dans le HTML; Balisage|titres et JSON-LD
widget: on
howto: on
related: /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ?; /fr/blog/does-llms-txt-work|llms.txt : est-ce que ça marche ?; /fr/guides/cms|Checklist pour Shopify, WooCommerce et autres
answer: Pour qu'un assistant IA lise votre boutique, vérifiez neuf points : robots.txt et robots IA, codes HTTP des pages clés, sitemap, canonical, hreflang, titres et H1, JSON-LD, texte présent dans le HTML brut, liens internes cassés. Chacun se teste à la main en quelques minutes. Le fichier llms.txt reste facultatif.
steps_img: on

## Pourquoi une checklist technique avant de parler de contenu ?

Un assistant ne peut citer que ce qu'il a pu récupérer. Si une page renvoie une erreur, si son texte n'apparaît qu'après l'exécution de scripts ou si robots.txt la ferme, le meilleur contenu du monde ne sert à rien. Ces contrôles sont les mêmes que ceux d'un audit SEO classique, avec un ajout : les robots des assistants (OAI-SearchBot, GPTBot, PerplexityBot) comptent autant que Googlebot.

Comptez une heure pour tout passer en revue sur une petite boutique en ligne. Gardez un tableur ouvert pour noter ce que vous trouvez.

## Quels sont les 9 contrôles à faire à la main ?

1. Robots.txt et robots IA : ouvrez `votre-boutique.fr/robots.txt` et cherchez `OAI-SearchBot`, `GPTBot`, `PerplexityBot` ou `*` suivi de `Disallow: /`. Un blocage général ferme la porte à tous les robots sans règle propre ([RFC 9309](https://www.rfc-editor.org/rfc/rfc9309)). Le détail est dans notre guide [ChatGPT peut-il lire mon site ?](/fr/blog/can-chatgpt-read-my-website).
2. Codes HTTP des pages clés : ouvrez l'accueil, une catégorie, une fiche produit et la page livraison, et vérifiez qu'elles répondent 200. Une redirection en chaîne, un 404 ou un 403 sur ces pages est à corriger en premier. Avec `curl -sI https://votre-boutique.fr/` la première ligne donne le code.
3. Sitemap.xml : ouvrez `votre-boutique.fr/sitemap.xml`. Il doit lister les pages que vous voulez faire lire et seulement elles. Google rappelle qu'un sitemap indique aux moteurs quelles pages vous jugez importantes ([Google : qu'est-ce qu'un sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview)).
4. Balise canonical : affichez le code source d'une fiche produit (clic droit, Afficher le code source de la page) et cherchez `rel="canonical"`. Elle doit pointer vers l'adresse propre de la page, sans paramètres de tri ni de suivi ([Google : canonical](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)).
5. Hreflang : si vous vendez en France et en Belgique, ou en plusieurs langues, cherchez les balises `hreflang` dans le code source. Chaque version doit pointer vers les autres et vers elle-même ([Google : versions localisées](https://developers.google.com/search/docs/specialty/international/localized-versions)). Boutique en une seule langue : passez au point suivant.
6. Titre et H1 : cherchez `<title>` et `<h1>` dans le code source. Chaque page doit avoir un titre précis et différent des autres. Google déconseille les titres vagues comme « Accueil » ([Google : title links](https://developers.google.com/search/docs/appearance/title-link)). Un seul H1 par page, qui dit ce que la page propose.
7. JSON-LD Product et Organization : cherchez `application/ld+json` dans le code source. Le bloc `Product` doit porter le bon prix, la disponibilité et le nom. Le bloc `Organization` donne votre nom, votre logo et vos coordonnées. Google précise que ce balisage permet d'afficher prix et disponibilité dans les résultats ([Google : données structurées Product](https://developers.google.com/search/docs/appearance/structured-data/product)).
8. Texte présent dans le HTML brut : dans le code source (pas dans l'inspecteur, qui montre la page après les scripts), cherchez le nom d'un produit, son prix et sa description. S'ils manquent, la page se construit avec JavaScript. Googlebot exécute JavaScript, mais certains assistants ne le font pas : placez donc le texte essentiel dans le HTML lui-même.
9. Liens internes cassés : cliquez sur le menu, le pied de page et les liens d'une page catégorie, ou passez le site dans un outil d'exploration. Chaque lien doit mener à une page qui répond 200.

## Et le fichier llms.txt ?

Il est facultatif. Aucun grand assistant n'est confirmé comme lecteur de ce fichier, et les études disponibles ne trouvent aucun lien net avec les citations. Notre analyse complète est dans [llms.txt : est-ce que ça marche ?](/fr/blog/does-llms-txt-work). Faites les neuf contrôles ci-dessus d'abord.

## Dans quel ordre corriger ce que vous trouvez ?

| Priorité | Problème | Pourquoi |
| --- | --- | --- |
| 1 | robots.txt bloque un robot que vous voulez, ou une page clé répond 403 ou 404 | Sans accès, rien d'autre ne compte |
| 2 | Texte absent du HTML brut | Un robot qui n'exécute pas les scripts ne voit qu'une coque vide |
| 3 | Prix absent ou faux dans le JSON-LD | L'assistant peut citer un prix périmé |
| 4 | Sitemap, canonical, hreflang | Ils indiquent quelle page lire parmi les doublons |
| 5 | Titres, H1, liens cassés | Hygiène à passer en revue chaque trimestre |

## Peut-on automatiser ces contrôles ?

Oui. L'[audit CitedBy](/fr/ai-visibility-audit) explore votre site jusqu'à la limite de votre offre, vérifie ces points (sauf ce qui dépend de vos journaux serveur) et vous donne le correctif exact pour chaque problème, dès 9 €, avec une garantie de remboursement de 14 jours. Le test à la main reste utile pour comprendre ce que le rapport signale.

## FAQ

### Faut-il refaire cette checklist régulièrement ?
Oui, après chaque changement de thème, de plugin ou d'hébergeur, et au moins une fois par trimestre. Un thème mis à jour peut remplacer un bloc JSON-LD ou un plugin de sécurité peut bloquer des robots sans prévenir.

### Quel contrôle a le plus d'effet ?
L'accès des robots. Si robots.txt, le CDN ou le pare-feu refuse un robot, ou si la page arrive vide dans le HTML, les autres contrôles n'ont plus d'importance pour cet assistant.

### Ces contrôles garantissent-ils que ChatGPT citera ma boutique ?
Non. Ils rendent vos pages lisibles. Savoir si un assistant vous nomme se mesure en lui posant de vraies questions d'acheteurs, comme dans [la méthode des 20 questions](/fr/blog/check-what-ai-says-about-your-brand).

## Sources

- [IETF RFC 9309 : protocole d'exclusion des robots](https://www.rfc-editor.org/rfc/rfc9309)
- [Google Search Central : qu'est-ce qu'un sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview)
- [Google Search Central : indiquer une URL canonique](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- [Google Search Central : versions localisées d'une page](https://developers.google.com/search/docs/specialty/international/localized-versions)
- [Google Search Central : influencer les title links](https://developers.google.com/search/docs/appearance/title-link)
- [Google Search Central : données structurées Product](https://developers.google.com/search/docs/appearance/structured-data/product)
- [Google Search Central : bases du SEO JavaScript](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- [OpenAI : robots d'exploration et user agents](https://developers.openai.com/api/docs/bots)
