title: OAI-SearchBot: what it is and how to allow or block it
h1: OAI-SearchBot: what it is and how to allow or block it
description: OAI-SearchBot decides whether your pages can appear in ChatGPT search answers. Its robots.txt token, user-agent, 39 published IP ranges and what a block costs.
slug: oai-searchbot
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Four facts about OAI-SearchBot: operator OpenAI, job Search, robots.txt behaviour, published address lists
hero_sub: OAI-SearchBot, run by OpenAI
hero_boxes: Operator|OpenAI; Job|Search; Obeys robots.txt|Yes; Address list|39 ranges
widget: on
related: /bots|All AI crawlers compared; /bots/gptbot|GPTBot; /blog/is-gptbot-blocked|Is GPTBot blocked on your site?; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website?
answer: OAI-SearchBot is OpenAI's crawler for ChatGPT search. Sites that opt out of it will not be shown in ChatGPT search answers, though they can still appear as navigational links. It obeys robots.txt under the token OAI-SearchBot, and OpenAI publishes 39 IP ranges for it.

## What OAI-SearchBot is

OpenAI runs several crawlers and says each setting is independent of the others. OAI-SearchBot is the one that decides whether your pages can be surfaced in ChatGPT's search features. It is not the training crawler (that is [GPTBot](/bots/gptbot)) and it is not the fetcher that opens a page when a person asks about it (that is [ChatGPT-User](/bots/chatgpt-user)).

| Fact | OAI-SearchBot |
| --- | --- |
| Operator | OpenAI |
| Job | Search |
| robots.txt token | `OAI-SearchBot` |
| Follows robots.txt | Yes, it follows robots.txt |
| Published address list | 39 ranges (openai.com/searchbot.json, file dated 2026-01-02) |
| Vendor page read | 21 October 2026 |

## What the vendor says

In the vendor's words: “OAI-SearchBot is used to surface websites in search results in ChatGPT's search features. Sites that are opted out of OAI-SearchBot will not be shown in ChatGPT search answers, though can still appear as navigational links.”

Source: [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots), read on 21 October 2026.

## What happens if you block it

OpenAI's own wording is that opted-out sites "will not be shown in ChatGPT search answers". That is the cost: a shop that blocks OAI-SearchBot gives up the part of ChatGPT that links to sources. OpenAI recommends the opposite for sites that want to appear: allow OAI-SearchBot in robots.txt and allow requests from its published IP ranges.

## The robots.txt lines

To allow it:

```
User-agent: OAI-SearchBot
Allow: /
```

To block it:

```
User-agent: OAI-SearchBot
Disallow: /
```

The user-agent string the vendor shows:

```
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36; compatible; OAI-SearchBot/1.4; +https://openai.com/searchbot
```

## How to tell a real request from a fake one

OpenAI publishes the addresses OAI-SearchBot uses at openai.com/searchbot.json. On 21 October 2026 that file held 39 prefixes and carried the creation time 2026-01-02. Match the address in your server log against those prefixes before you trust a request that only claims the name in its user-agent. OpenAI also says that when it fetches robots.txt it may add a `robots.txt` marker to the user-agent string, so those requests are easy to tell apart in logs without paths.

## Compare with GPTBot

[GPTBot](/bots/gptbot): GPTBot is for training; blocking it does not remove you from ChatGPT search because the settings are independent.

## Check your own site

The audit box above reads robots.txt for the crawlers in this set and sends one live request per crawler, so a rule that robots.txt allows but a firewall refuses shows up. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does blocking GPTBot also block OAI-SearchBot?

No. OpenAI states that each setting is independent of the others, so a robots.txt group for GPTBot does not change how OAI-SearchBot treats your site. Add a separate group for each token you want to control.

### Why would a firewall block OAI-SearchBot when robots.txt allows it?

Robots.txt is only a policy file. A CDN, WAF or host rule can still refuse the request before the server answers. OpenAI asks site owners to allow its published IP ranges for this reason.

## Sources

- [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots)
- [openai.com/searchbot.json](https://openai.com/searchbot.json), read 21 October 2026
