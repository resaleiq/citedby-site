title: YouBot: what it does and what blocking it changes
h1: YouBot: what it does and what blocking it changes
description: YouBot (You.com): search. Robots.txt token, what a Disallow changes and how to verify a request, read from the operator's own page.
slug: youbot
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about YouBot: operator You.com, job Search, obeys robots.txt Yes, address list Listed on its page
hero_sub: YouBot, run by You.com
hero_boxes: Operator|You.com; Job|Search; Obeys robots.txt|Yes; Address list|Listed on its page
widget: on
related: /bots|All AI crawlers compared; /bots/mojeekbot|MojeekBot; /platforms|AI crawler settings by platform; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website? What decides it
answer: YouBot is the web crawler that powers the You.com search engine, discovering and indexing pages for its results. You.com says it respects robots.txt, honors Crawl-delay and caches robots.txt for 30 minutes. User-agent: YouBot with Disallow: / blocks it from the whole site.

## What YouBot is

YouBot is the web crawler that powers the You.com search engine. It discovers and indexes web pages for You.com search results. You.com says X.X.X.X in the user agent stands for the Google Chrome version number.

| Fact | YouBot |
| --- | --- |
| Operator | You.com |
| Job | Search |
| robots.txt token | `YouBot` |
| Follows robots.txt | Yes, robots.txt is cached for 30 minutes, so changes can take up to 30 minutes |
| IP addresses | Listed on the vendor's page (you.com/docs/youbot) |
| Vendor page read | 24 October 2026 |

## What the vendor says

In the vendor's words (English original): “YouBot is the web crawler that powers the You.com search engine.”

Source: [You.com Docs: YouBot: You.com's Web Crawler](https://docs.you.com/youbot), read on 24 October 2026.

## What happens if you block YouBot

You.com says YouBot respects robots.txt and shows User-agent: YouBot with Disallow: / as the way to block it from the whole site. It also honors Crawl-delay and caches robots.txt for 30 minutes. The page does not describe any other You.com agents.

## The robots.txt lines

To allow YouBot:

```
User-agent: YouBot
Allow: /
```

To block YouBot:

```
User-agent: YouBot
Disallow: /
```

Paste a block into the robots.txt at the root of your host, for example https://example.com/robots.txt. A group for one token does not cover the operator's other crawlers.

The user-agent string the vendor shows:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; YouBot/1.0; +https://docs.you.com/youbot; env:prod) Chrome/X.X.X.X Safari/537.36
```

## How to tell a real request from a fake one

You.com says requests originate from 68.67.112.0/24, hosts resolve as youbot-{octets-with-hyphens}.search.you.com, and requests carry Cloudflare Web Bot Auth signatures with public keys at you.com/.well-known/http-message-signatures-directory.

## Compare with MojeekBot

[MojeekBot](/bots/mojeekbot): Both are search-engine crawlers that follow robots.txt; You.com supports Crawl-delay and signs requests with Web Bot Auth, while Mojeek does not support Crawl-delay.

## Your own site

The free check in the box above tests eight crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot). YouBot is not one of them: read your robots.txt for a `YouBot` group and look for the user agent in your server log. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does YouBot follow robots.txt?

Yes, robots.txt is cached for 30 minutes, so changes can take up to 30 minutes. Give YouBot its own User-agent group in robots.txt: the operator's other crawlers have their own settings.

### How do I know YouBot is really blocked?

robots.txt is only one layer: a CDN or firewall rule can also turn a crawler away, and a crawler can ignore the file. Check your server log for the user agent, and test the address from outside your network.

## Sources

- [You.com Docs: YouBot: You.com's Web Crawler](https://docs.you.com/youbot)
