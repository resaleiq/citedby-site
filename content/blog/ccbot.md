title: CCBot: what it does and what blocking it changes
h1: CCBot: what it does and what blocking it changes
description: CCBot (Common Crawl): several jobs. Robots.txt token, what a Disallow changes and how to verify a request, read from the operator's own page.
slug: ccbot
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about CCBot: operator Common Crawl, job Several jobs, obeys robots.txt Yes, address list Reverse DNS
hero_sub: CCBot, run by Common Crawl
hero_boxes: Operator|Common Crawl; Job|Several jobs; Obeys robots.txt|Yes; Address list|Reverse DNS
widget: on
related: /bots|All AI crawlers compared; /bots/gptbot|GPTBot; /platforms|AI crawler settings by platform; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website? What decides it
answer: CCBot is the crawler of Common Crawl, a non-profit that maintains an open repository of web crawl data anyone can access and analyze. Common Crawl says User-agent: CCBot with Disallow: / stops it crawling a site. It also warns that other crawlers falsely identify themselves as CCBot, so verify requests.

## What CCBot is

CCBot is the crawler of Common Crawl, a non-profit foundation that produces and maintains an open repository of web crawl data that anyone can access and analyze. The vendor page says the crawl data is meant to be freely available to organizations, academia and non-profits.

| Fact | CCBot |
| --- | --- |
| Operator | Common Crawl |
| Job | Open web crawl archive |
| robots.txt token | `CCBot` |
| Follows robots.txt | Yes, via a robots.txt rule for CCBot |
| IP addresses | Reverse DNS check |
| Vendor page read | 24 October 2026 |

## What the vendor says

In the vendor's words (English original): “To prevent Common Crawl from crawling your website, include the following in your robots.txt”

Source: [Common Crawl: CCBot](https://commoncrawl.org/ccbot), read on 24 October 2026.

## What happens if you block CCBot

Common Crawl says that adding User-agent: CCBot with Disallow: / to robots.txt prevents Common Crawl from crawling the site. The page also says it is aware of crawlers falsely identifying themselves as CCBot and recommends verifying user agent strings.

## The robots.txt lines

To allow CCBot:

```
User-agent: CCBot
Allow: /
```

To block CCBot:

```
User-agent: CCBot
Disallow: /
```

Paste a block into the robots.txt at the root of your host, for example https://example.com/robots.txt. A group for one token does not cover the operator's other crawlers.

The user-agent string the vendor shows:

```
CCBot/2.0 (https://commoncrawl.org/faq/)
```

## How to tell a real request from a fake one

Common Crawl says CCBot runs on dedicated IP address ranges with reverse DNS (not for IPv6), so a logged request can be checked with a reverse lookup that resolves to a crawl.commoncrawl.org hostname; the ranges are also published as JSON at https://index.commoncrawl.org/ccbot.json.

## Compare with GPTBot

[GPTBot](/bots/gptbot): CCBot builds a public crawl archive that others can use, while GPTBot collects content for OpenAI's own purposes.

## Your own site

The free check in the box above tests eight crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot). CCBot is not one of them: read your robots.txt for a `CCBot` group and look for the user agent in your server log. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does CCBot follow robots.txt?

Yes, via a robots.txt rule for CCBot. Give CCBot its own User-agent group in robots.txt: the operator's other crawlers have their own settings.

### How do I know CCBot is really blocked?

robots.txt is only one layer: a CDN or firewall rule can also turn a crawler away, and a crawler can ignore the file. Check your server log for the user agent, and test the address from outside your network.

## Sources

- [Common Crawl: CCBot (read 2026-10-24)](https://commoncrawl.org/ccbot)
