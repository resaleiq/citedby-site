title: ChatGPT affiche un ancien prix : trouver la source, corriger
h1: ChatGPT affiche mon ancien prix : comment trouver où il l'a lu et le corriger
description: ChatGPT cite un prix que vous avez changé. Trois origines possibles : votre page, votre flux produits, d'autres sites. Comment les tracer et retester.
slug: chatgpt-wrong-price
locale: fr
cluster: Informations erronées
date: 2026-10-20
reviewed: 2026-10-20
hero: auto
hero_alt: Carte de titre : ChatGPT affiche mon ancien prix, avec trois cases : votre page, votre flux produits, les autres sites
hero_sub: Trois sources possibles, à vérifier dans l'ordre
hero_boxes: Votre page|HTML et JSON-LD; Votre flux produits|Google Shopping; Autres sites|avis et comparateurs
widget: on
steps_img: on
howto: on
related: /fr/blog/check-what-ai-says-about-your-brand|Que dit ChatGPT de votre marque ? 20 questions; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ?; /sample-audit|Un exemple de mini-audit
answer: ChatGPT affiche un ancien prix quand il l'a lu dans une source périmée : votre propre page, un flux produits ou un autre site. Cherchez l'ancien prix à chacun de ces endroits, corrigez la source, puis reposez la question deux fois dans une nouvelle conversation. Mettez votre flux à jour à chaque début et fin de promotion.

## Pourquoi un assistant cite-t-il un prix que vous avez changé ?

Un assistant répond à partir de ce qu'il trouve : les pages qu'il a récupérées, les flux envoyés par les marchands et les pages de tiers qui parlent de vous. Si l'une de ces sources garde l'ancien chiffre, la réponse peut le garder aussi. Un prix faux est donc un problème de données sur une page que vous maîtrisez ou que vous pouvez contacter, et c'est ce qui permet de le corriger. La correction se fait à la source, pas dans la conversation.

Un internaute a décrit exactement ce cas sur r/ecommerce le 22 septembre : ChatGPT recommandait un lot abandonné un an plus tôt, à l'ancien prix de 149 $ ([fil de discussion](https://old.reddit.com/comments/1wnbg86/)). C'est un témoignage isolé, pas un taux mesuré.

## Étape 1 : comment noter la mauvaise réponse ?

Ouvrez une nouvelle conversation, avec la recherche web activée si l'assistant la propose, et demandez : « Combien coûte [produit] chez [boutique] ? » Copiez la réponse, la date, l'assistant et tout lien cité. Un lien cité est le meilleur indice, car il nomme la page qui a nourri la réponse. Posez la question une seconde fois dans une autre conversation. Si les deux réponses diffèrent, notez les deux : les réponses varient d'une exécution à l'autre.

## Étape 2 : comment chercher l'ancien prix sur votre propre page ?

1. Affichez le code source : ouvrez la fiche produit, puis clic droit et Afficher le code source de la page.
2. Cherchez l'ancien prix : par exemple `49,00` et `49.00`, avec et sans le signe €.
3. Relisez le JSON-LD : trouvez le bloc `application/ld+json` et lisez le prix dans `offers`. Un balisage produit jamais mis à jour est une cause fréquente de prix périmé, et Google indique que le prix du balisage et du flux doit correspondre à celui de la page d'atterrissage ([aide Google Merchant Center](https://support.google.com/merchants/answer/9773429)).
4. Cherchez un second prix : un prix barré, un prix de lot, une déclinaison qui charge un autre montant.
5. Récupérez la page comme un robot : sans JavaScript. Si le prix n'apparaît qu'après l'exécution de scripts, un robot peut ne pas voir le chiffre final.

## Étape 3 : votre flux produits affiche-t-il encore l'ancien prix ?

Si vous vendez via Google Shopping, une place de marché ou le flux shopping de ChatGPT, le flux est une seconde copie de votre prix. La spécification de flux d'OpenAI demande un prix sous la forme `79.99 USD`, une ligne par article ou déclinaison achetable, et indique de mettre le flux à jour au début et à la fin d'une promotion ([spécification du flux produits OpenAI](https://developers.openai.com/commerce/specs/feed)). Une promotion terminée sur votre site mais restée dans le flux est le décalage classique.

Google décrit le même piège pour son flux : quand le flux et la page d'atterrissage divergent, la solution est de les aligner, de renvoyer le flux (import, Content API ou plateforme de votre boutique), puis de demander un examen, qui prend 7 jours ouvrés selon Google ([aide Google Merchant Center](https://support.google.com/merchants/answer/9773429)). La page d'OpenAI ne décrit aucun moyen de contester des données déjà intégrées, nous n'en promettons donc pas.

## Étape 4 : comment trouver l'ancien prix sur d'autres sites ?

Cherchez l'ancien prix avec le nom de votre marque et celui du produit. Regardez les sites d'avis, les listes de prix, les comparateurs, les anciens articles de blog et vos propres communiqués. Demandez au propriétaire de chaque page de la mettre à jour, ou publiez sur votre site une page à jour qui indique le prix avec sa date : la source la plus récente devient aussi la plus claire.

## Étape 5 : combien de temps attendre avant de reposer la question ?

OpenAI indique qu'une modification de robots.txt peut mettre environ 24 heures à atteindre son robot de recherche ([documentation des robots OpenAI](https://developers.openai.com/api/docs/bots)). Elle ne publie aucun calendrier de rafraîchissement pour une page déjà lue : personne ne peut vous promettre une date. Reposez la même question deux fois, dans de nouvelles conversations, une fois par semaine, et notez chaque réponse dans un tableau.

| Date | Assistant | Question | Prix affiché | Lien cité | Identique à votre page ? |
| --- | --- | --- | --- | --- | --- |
| 20/10/2026 | ChatGPT, recherche activée | Combien coûte [produit] chez [boutique] ? | | | |

## L'audit peut-il repérer ce problème ?

L'audit CitedBy explore vos pages et teste si les robots IA peuvent les atteindre et lire vos données produit. Si la page de votre prix est bloquée ou vide pour un robot, aucune correction du prix ne servira : testez cela d'abord.

## FAQ

### Pourquoi ChatGPT affiche-t-il un ancien prix pour mon produit ?
Il a probablement lu l'ancien chiffre sur votre page, dans votre flux produits ou sur un autre site qui le garde. Cherchez l'ancien prix à chacun de ces endroits et regardez le lien cité, s'il y en a un.

### Combien de temps avant que ChatGPT affiche le nouveau prix ?
Personne ne peut promettre de date. OpenAI indique que les modifications de robots.txt mettent environ 24 heures à atteindre son robot de recherche, et ne donne aucun calendrier pour les pages déjà lues. Reposez la question chaque semaine et notez les réponses.

### Puis-je demander à OpenAI de corriger un prix erroné ?
La spécification de flux d'OpenAI ne décrit aucun moyen de corriger des données déjà intégrées : corrigez donc les sources et retestez. Regardez dans le centre d'aide d'OpenAI si une option de signalement existe au moment où vous lisez ceci.

### Le prix dans le balisage schema compte-t-il ?
Oui, quand il est périmé. Google indique que le prix du balisage et du flux doit correspondre à celui de la page, et un bloc jamais mis à jour est un décalage courant à chercher.

## Sources

- [OpenAI : spécification du flux produits](https://developers.openai.com/commerce/specs/feed)
- [OpenAI : robots d'exploration et user agents](https://developers.openai.com/api/docs/bots)
- [Google Merchant Center : prix inexact dû à un décalage entre flux et page d'atterrissage](https://support.google.com/merchants/answer/9773429)
- [r/ecommerce, 22 septembre 2026 : ChatGPT recommande un lot abandonné à l'ancien prix](https://old.reddit.com/comments/1wnbg86/)
