title: ChatGPT-User : ce qu'il fait et ce que change son blocage
h1: ChatGPT-User : ce qu'il fait et ce que change son blocage
description: ChatGPT-User (OpenAI) : récupération déclenchée par l'utilisateur. Jeton robots.txt, effet d'un Disallow et vérification d'une requête.
slug: chatgpt-user
section: bots
locale: fr
cluster: Robots d'exploration IA
date: 2026-10-24
reviewed: 2026-10-21
hero: auto
hero_alt: Quatre faits sur ChatGPT-User : opérateur OpenAI, rôle Récupération déclenchée par l'utilisateur, respecte robots.txt Pas toujours, liste d'adresses 234 plages
hero_sub: ChatGPT-User, géré par OpenAI
hero_boxes: Opérateur|OpenAI; Rôle|Récupération déclenchée par l'utilisateur; Respecte robots.txt|Pas toujours; Liste d'adresses|234 plages
widget: on
related: /fr/bots|Tous les robots IA comparés; /fr/bots/oai-searchbot|OAI-SearchBot; /fr/platforms|Réglages des robots IA par plateforme; /fr/blog/can-chatgpt-read-my-website|ChatGPT peut-il lire mon site ? Ce qui décide
answer: ChatGPT-User visite une page web lorsqu’une personne pose à ChatGPT ou à un GPT personnalisé une question qui l’exige. OpenAI indique qu’il n’est pas utilisé pour explorer automatiquement et que, comme c’est un utilisateur qui lance la requête, les règles robots.txt peuvent ne pas s’appliquer. OpenAI liste 234 plages d’IP pour lui.

## Ce qu'est ChatGPT-User

Contrairement aux autres robots d’OpenAI, ChatGPT-User ne parcourt pas le web de lui-même. OpenAI le décrit comme l’agent utilisé pour certaines actions d’utilisateurs dans ChatGPT et les GPT personnalisés, y compris pour les pages qu’un GPT personnalisé atteint via les GPT Actions. Une personne a tapé quelque chose, puis une requête est arrivée sur votre serveur.

| Fait | ChatGPT-User |
| --- | --- |
| Opérateur | OpenAI |
| Rôle | Récupération déclenchée par l’utilisateur |
| Jeton robots.txt | `ChatGPT-User` |
| Respecte robots.txt | Les règles robots.txt peuvent ne pas s’appliquer |
| Adresses IP | 234 plages (openai.com/chatgpt-user.json, fichier daté du 2026-10-20) |
| Page de l'opérateur lue le | 21 octobre 2026 |

## Ce que dit l'opérateur

Les mots de l'opérateur (original en anglais) : “ChatGPT-User is not used for crawling the web in an automatic fashion. Because these actions are initiated by a user, robots.txt rules may not apply.”

Source : [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots), lu le 21 octobre 2026.

## Que se passe-t-il si vous bloquez ChatGPT-User

La visite étant lancée par un utilisateur, OpenAI prévient que les règles robots.txt peuvent ne pas s’appliquer : une ligne `Disallow` pour ChatGPT-User n’est donc pas un arrêt garanti. OpenAI indique aussi que ChatGPT-User n’est pas utilisé pour décider si un contenu apparaît dans la recherche et renvoie les refus de recherche vers OAI-SearchBot. Si vous devez arrêter ces requêtes, le contrôle se fait sur votre serveur ou votre CDN, pas dans robots.txt seul.

## Les lignes robots.txt

Pour autoriser ChatGPT-User :

```
User-agent: ChatGPT-User
Allow: /
```

Pour bloquer ChatGPT-User :

```
User-agent: ChatGPT-User
Disallow: /
```

Collez un bloc dans le fichier robots.txt à la racine de votre hôte, par exemple https://example.com/robots.txt. Un groupe pour un jeton ne couvre pas les autres robots du même opérateur.

La chaîne user-agent indiquée par l'opérateur :

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ChatGPT-User/1.0; +https://openai.com/bot
```

## Comment distinguer une vraie requête d'une fausse

Sa liste d’adresses est la plus longue des trois fichiers OpenAI que nous avons comptés : openai.com/chatgpt-user.json contenait 234 préfixes le 21 octobre 2026, avec une date de création au 2026-10-20, la veille de cette page. Une liste aussi longue est une raison de la télécharger à nouveau chaque fois que vous vérifiez une ligne du journal de serveur, pas de la copier une seule fois dans un pare-feu.

## À comparer avec OAI-SearchBot

[OAI-SearchBot](/fr/bots/oai-searchbot) : OAI-SearchBot est le robot de recherche et il respecte robots.txt.

## Votre propre site

Le contrôle gratuit dans l'encadré ci-dessus teste ChatGPT-User avec une requête réelle et lit robots.txt pour lui. La liste complète des robots est sur [le répertoire des robots d'exploration IA](/fr/bots).

## FAQ

### ChatGPT-User respecte-t-il robots.txt ?

Les règles robots.txt peuvent ne pas s’appliquer. Une règle pour ChatGPT-User dans robots.txt peut donc ne pas l'arrêter. Pour le refuser à coup sûr, utilisez une règle de pare-feu ou de CDN qui combine le user agent et les adresses publiées.

### Comment savoir si ChatGPT-User est vraiment bloqué ?

robots.txt n'est qu'une couche : une règle de CDN ou de pare-feu peut aussi refuser un robot, et un robot peut ignorer le fichier. Cherchez le user agent dans votre journal de serveur et testez l'adresse depuis l'extérieur de votre réseau.

## Sources

- [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots)
- [openai.com/chatgpt-user.json](https://openai.com/chatgpt-user.json)
