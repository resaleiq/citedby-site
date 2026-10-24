title: LinkupBot: what it does and what blocking it changes
h1: LinkupBot: what it does and what blocking it changes
description: LinkupBot (Linkup): search. Robots.txt token, what a Disallow changes and how to verify a request, read from the operator's own page.
slug: linkupbot
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about LinkupBot: operator Linkup, job Search, obeys robots.txt Yes, address list Listed on its page
hero_sub: LinkupBot, run by Linkup
hero_boxes: Operator|Linkup; Job|Search; Obeys robots.txt|Yes; Address list|Listed on its page
widget: on
related: /bots|All AI crawlers compared; /bots/perplexitybot|PerplexityBot; /platforms|AI crawler settings by platform; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website? What decides it
answer: LinkupBot is the web crawler of Linkup. It fetches publicly accessible pages to build the Linkup search index, which Linkup says powers search and web grounding for AI applications. Linkup says User-agent: LinkupBot with Disallow: / blocks the whole site, and that robots.txt is not an access-control mechanism.

## What LinkupBot is

LinkupBot is the web crawler of Linkup. It fetches publicly accessible pages to build and maintain the Linkup search index, which Linkup says powers search and web grounding for AI applications.

| Fact | LinkupBot |
| --- | --- |
| Operator | Linkup |
| Job | Search index for AI web search |
| robots.txt token | `LinkupBot` |
| Follows robots.txt | Yes, vendor says it respects applicable robots.txt rules |
| IP addresses | Listed on the vendor's page (www.linkup.so/linkupbot-ips.txt) |
| Vendor page read | 24 October 2026 |

## What the vendor says

In the vendor's words (English original): “LinkupBot is Linkup’s web crawler. It discovers and retrieves publicly accessible webpages to build and maintain the Linkup web search index, which powers search and web grounding for AI applications.”

Source: [Linkup: LinkupBot](https://www.linkup.so/bot), read on 24 October 2026.

## What happens if you block LinkupBot

Adding User-agent: LinkupBot with Disallow: / to robots.txt blocks the whole site, according to the vendor. The vendor also says robots rules apply per host, that allowing LinkupBot through a firewall does not override robots.txt, and that robots.txt is not an access-control mechanism.

## The robots.txt lines

To allow LinkupBot:

```
User-agent: LinkupBot
Allow: /
```

To block LinkupBot:

```
User-agent: LinkupBot
Disallow: /
```

Paste a block into the robots.txt at the root of your host, for example https://example.com/robots.txt. A group for one token does not cover the operator's other crawlers.

The user-agent string the vendor shows:

```
LinkupBot/1.0 (LinkupBot for web indexing; https://www.linkup.so/bot; bot@linkup.so)
```

## How to tell a real request from a fake one

The vendor says requests come from the CIDR ranges in its published list and to verify with both a source IP in that list and a user-agent containing the LinkupBot token.

## Compare with PerplexityBot

[PerplexityBot](/bots/perplexitybot): Both build a search index that feeds AI answers; LinkupBot's index serves AI applications through Linkup's search and grounding service, and its IP list is a plain text file rather than JSON.

## Your own site

The free check in the box above tests eight crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot). LinkupBot is not one of them: read your robots.txt for a `LinkupBot` group and look for the user agent in your server log. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does LinkupBot follow robots.txt?

Yes, vendor says it respects applicable robots.txt rules. Give LinkupBot its own User-agent group in robots.txt: the operator's other crawlers have their own settings.

### How do I know LinkupBot is really blocked?

robots.txt is only one layer: a CDN or firewall rule can also turn a crawler away, and a crawler can ignore the file. Check your server log for the user agent, and test the address from outside your network.

## Sources

- [Linkup: LinkupBot](https://www.linkup.so/bot)
- [Linkup: linkupbot-ips.txt (plain text, read 2026-10-24)](https://www.linkup.so/linkupbot-ips.txt)
