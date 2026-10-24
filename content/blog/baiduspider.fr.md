title: Baiduspider : ce qu'il fait et ce que change son blocage
h1: Baiduspider : ce qu'il fait et ce que change son blocage
description: Baiduspider (Baidu) : recherche. Jeton robots.txt, effet d'un Disallow et vérification d'une requête, lus sur la page de l'opérateur.
slug: baiduspider
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Quatre faits sur Baiduspider : opérateur Baidu, rôle Recherche, respecte robots.txt Oui, liste d'adresses DNS inversé
hero_sub: Baiduspider, géré par Baidu
hero_boxes: Opérateur|Baidu; Rôle|Recherche; Respecte robots.txt|Oui; Liste d'adresses|DNS inversé
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/bingbot|Bingbot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: Baiduspider est le robot d’exploration du moteur de recherche Baidu. Baidu indique qu’il suit le protocole robots.txt et que bloquer Baiduspider bloque tous les user agents de Baidu, si bien que vos pages ne seront pas trouvées dans les résultats de Baidu. Baiduspider-cpro et Baiduspider-ads fonctionnent selon des accords avec des clients et ne suivent pas robots.txt.

## Ce qu'est Baiduspider

Baiduspider est le robot d’exploration du moteur de recherche Baidu ; il visite les pages et les intègre à l’index de Baidu. Baidu utilise des user agents différents selon les produits, par exemple Baiduspider pour la recherche sur PC et mobile, et Baiduspider-image, Baiduspider-video et Baiduspider-news pour ces recherches.

| Fait | Baiduspider |
| --- | --- |
| Opérateur | Baidu |
| Rôle | Recherche |
| Jeton robots.txt | `Baiduspider` |
| Respecte robots.txt | Oui pour Baiduspider ; Baiduspider-cpro et Baiduspider-ads ne suivent pas les enregistrements robots.txt |
| Adresses IP | Vérification par DNS inversé |
| Page de l'opérateur lue le | 24 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “Baiduspider is Baidu search engine program which is used to visit pages on the internet and build information into Baidu index.”

Source : [Baidu Help Center: FAQs of Baiduspider](https://help.baidu.com/question?prod_id=99&class=0&id=3001), lu le 24 octobre 2026.

## Que se passe-t-il si vous bloquez Baiduspider

Baidu indique que Baiduspider fonctionne selon le protocole robots.txt, et que le bloquer signifie que vos pages ne seront pas trouvées dans les résultats de recherche de Baidu ni dans aucun autre résultat fourni par Baidu. Vous pouvez définir des règles différentes pour différents user agents de Baidu, et bloquer Baiduspider bloque tous les user agents de Baidu. Baiduspider-cpro et Baiduspider-ads fonctionnent selon des accords avec des clients et ne suivent pas les enregistrements robots.txt.

## Les lignes robots.txt

Pour autoriser Baiduspider :

```
User-agent: Baiduspider
Allow: /
```

Pour bloquer Baiduspider :

```
User-agent: Baiduspider
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
Baiduspider
```

## Comment distinguer une vraie requête d'une fausse

Baidu recommande une recherche DNS inverse sur l’IP visiteuse ; le nom d’hôte de Baiduspider est *.baidu.com ou *.baidu.jp, et tout autre nom d’hôte est faux.

## À comparer avec Bingbot

[Bingbot](/fr/bots/bingbot) : Les deux explorent pour un moteur de recherche ; Baidu documente plusieurs user agents propres à chaque produit (image, vidéo, actualités, publicités) sous le nom Baiduspider et vérifie par le nom d’hôte du DNS inverse.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste huit robots (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot et Googlebot). Baiduspider n'en fait pas partie : lisez votre robots.txt pour un groupe `Baiduspider` et cherchez le user agent dans votre journal de serveur. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### Baiduspider respecte-t-il robots.txt ?

Oui pour Baiduspider ; Baiduspider-cpro et Baiduspider-ads ne suivent pas les enregistrements robots.txt. Donnez à Baiduspider son propre groupe User-agent dans robots.txt : les autres robots du même opérateur ont chacun leur réglage.

### Comment savoir si Baiduspider est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [Baidu Help Center: FAQs of Baiduspider](https://help.baidu.com/question?prod_id=99&class=0&id=3001)
- [Baidu Help Center: How to block the crawling (robots.txt)](https://www.baidu.com/search/robots_english.html)
