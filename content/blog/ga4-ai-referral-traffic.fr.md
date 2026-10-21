title: GA4 : suivre le trafic de ChatGPT et des assistants IA
h1: Le trafic IA convertit-il ? Configurer GA4 pour voir les visites venant de ChatGPT et des autres assistants
description: Créez un canal « Assistants IA » dans GA4, vérifiez les sources réelles de vos rapports et comparez les conversions aux autres canaux. Regex incluse.
slug: ga4-ai-referral-traffic
locale: fr
cluster: Mesure
date: 2026-10-20
reviewed: 2026-10-20
hero: auto
hero_alt: Trois étapes pour un canal Assistants IA dans GA4 : repérer les sources, créer le canal, le placer au-dessus des sites référents
hero_sub: Trois étapes, et l'ordre des canaux compte
hero_boxes: Repérer|les sources dans le rapport; Créer|le canal avec une regex; Réordonner|au-dessus des sites référents
widget: on
steps_img: on
howto: on
related: /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ?; /fr/blog/check-what-ai-says-about-your-brand|Que dit ChatGPT de votre marque ?; /fr/ai-visibility-audit|Audit de visibilité IA : que vérifier ?
answer: Créez dans GA4 un groupe de canaux personnalisé avec un canal « Assistants IA », dont la source correspond à une expression régulière des assistants visibles dans votre rapport. Placez-le au-dessus de « Sites référents », car GA4 attribue la session au premier canal qui correspond. Comparez ensuite les conversions. Les visites sans référent restent en Direct.

## Pourquoi le trafic des assistants IA se cache-t-il dans GA4 ?

GA4 range chaque session dans un canal. Les visites venant d'un assistant peuvent atterrir dans « Sites référents », mêlées aux liens de blogs et d'annuaires, ou dans un autre canal : impossible alors de les voir en un seul bloc. Un canal personnalisé leur donne leur propre ligne. La documentation de Google indique qu'un groupe de canaux personnalisé peut s'appliquer à vos rapports de façon rétroactive : votre historique est donc reclassé dès l'enregistrement ([aide Google Analytics](https://support.google.com/analytics/answer/13051316?hl=fr)).

Il faut le rôle Éditeur ou supérieur sur la propriété. D'après la même page, une propriété standard peut contenir 2 groupes de canaux personnalisés, avec jusqu'à 50 canaux chacun.

## Comment créer un canal Assistants IA dans GA4 ?

1. Repérez les sources : dans GA4, ouvrez Rapports, Acquisition, puis Acquisition de trafic, et passez la dimension sur la source ou le support de la session.
2. Notez les assistants : parcourez la liste à la recherche de noms comme chatgpt, perplexity, gemini ou copilot, et écrivez les sources exactes que vous voyez.
3. Ouvrez les groupes de canaux : dans Administration, sous Affichage des données, cliquez sur Groupes de canaux, puis créez un groupe.
4. Ajoutez le canal : nommez-le « Assistants IA », ajoutez une condition sur la source, choisissez « correspond à l'expression régulière » et collez votre liste.
5. Réorganisez : enregistrez le canal, cliquez sur Réorganiser, faites glisser « Assistants IA » au-dessus de « Sites référents », puis cliquez sur Appliquer.
6. Comparez : rouvrez Acquisition de trafic avec votre nouveau groupe comme dimension et comparez sessions, sessions engagées et conversions.

L'étape de l'ordre est celle que l'on oublie. Selon Google, le trafic est inclus dans le premier canal dont il correspond à la définition, selon l'ordre actuel des canaux. Si « Sites référents » est placé avant votre nouveau canal, les assistants n'y arrivent jamais.

## Quelle expression régulière utiliser comme point de départ ?

Partez des noms des assistants les plus connus :

```
(chatgpt|openai|perplexity|gemini|copilot)
```

Prenez-la comme une hypothèse de départ, pas comme une liste vérifiée. Les noms d'hôte changent et de nouveaux assistants arrivent : ce qui compte, c'est ce qui apparaît dans votre propre rapport. Ajoutez les sources que vous voyez réellement, retirez celles qui correspondent à autre chose qu'un assistant, et refaites ce contrôle au moins une fois par trimestre. Google publie lui-même un exemple « Assistants IA » dans sa page d'aide, avec une expression plus longue que vous pouvez comparer à la vôtre.

## Que ne peut pas vous dire GA4 ?

Seules les visites qui portent un référent peuvent être étiquetées. Quelqu'un qui copie votre adresse dans une réponse et la colle dans son navigateur arrive en Direct. Un canal GA4 donne donc une valeur plancher des visites venues de l'IA, pas le total. Dites-le quand vous présentez ce chiffre à quelqu'un qui va agir dessus.

Les petits nombres peuvent n'être que du bruit. Comparez le taux de conversion et le chiffre d'affaires par session avec ceux de la recherche naturelle avant de conclure, et n'extrapolez pas à partir d'une semaine de données.

## Comment savoir si les assistants nomment aussi votre boutique ?

Le canal indique si les assistants envoient des visiteurs. Il ne dit pas s'ils nomment votre boutique. L'[audit CitedBy](/fr/ai-visibility-audit) explore vos pages pour voir si les robots IA peuvent les lire, dès 9 €, et la méthode manuelle des [20 questions](/fr/blog/check-what-ai-says-about-your-brand) montre qui est nommé quand un acheteur pose la question.

## FAQ

### Comment voir le trafic de ChatGPT dans GA4 ?
Ouvrez Acquisition de trafic avec la source ou le support de la session et cherchez chatgpt dans la colonne source. Pour une vue permanente, créez un canal Assistants IA comme ci-dessus.

### Pourquoi mon trafic IA apparaît-il en Direct ?
Quand le navigateur du visiteur n'envoie aucun référent, GA4 n'a rien à étiqueter. Coller un lien ou l'ouvrir depuis une application sans information de référent donne ce résultat.

### Un groupe de canaux personnalisé modifie-t-il mes anciennes données ?
Google indique que les groupes de canaux personnalisés peuvent s'appliquer à vos rapports de façon rétroactive : votre historique est donc reclassé dans les rapports qui utilisent le groupe.

### Faut-il être administrateur pour le créer ?
Non, mais il faut au moins le rôle Éditeur sur la propriété.

## Sources

- [Aide Google Analytics : groupes de canaux personnalisés](https://support.google.com/analytics/answer/13051316?hl=fr)
- [CitedBy : exemple de rapport](https://citedby.eu/fr/sample)
