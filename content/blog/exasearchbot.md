title: ExaSearchBot: what it does and what blocking it changes
h1: ExaSearchBot: what it does and what blocking it changes
description: ExaSearchBot (Exa): search. Robots.txt token, what a Disallow changes and how to verify a request, read from the operator's own page.
slug: exasearchbot
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about ExaSearchBot: operator Exa, job Search, obeys robots.txt Yes, address list Verify tool
hero_sub: ExaSearchBot, run by Exa
hero_boxes: Operator|Exa; Job|Search; Obeys robots.txt|Yes; Address list|Verify tool
widget: on
related: /bots|All AI crawlers compared; /bots/perplexitybot|PerplexityBot; /platforms|AI crawler settings by platform; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website? What decides it
answer: ExaSearchBot is the crawler of Exa, a search engine built for search and retrieval, so pages can be discovered and cited. Exa says it checks robots.txt before fetching and that User-agent: ExaSearchBot with Disallow: / blocks the whole site. Every request is cryptographically signed, so verification does not depend on an IP address.

## What ExaSearchBot is

ExaSearchBot is the crawler of Exa, a search engine. Exa says its purpose is search and retrieval, so pages become discoverable and can be cited. Pages Exa fetches on a user's request rather than by crawling go out as ExaUser.

| Fact | ExaSearchBot |
| --- | --- |
| Operator | Exa |
| Job | Search and retrieval index |
| robots.txt token | `ExaSearchBot` |
| Follows robots.txt | Yes, vendor says it checks robots.txt before fetching |
| IP addresses | Verify tool |
| Vendor page read | 24 October 2026 |

## What the vendor says

In the vendor's words (English original): “Exa is a search engine. Similar to other search engines, Exa uses a robot (ExaSearchBot) to discover and index pages on the public web.”

Source: [Exa: Exa Search Crawler](https://crawler.exa.ai/), read on 24 October 2026.

## What happens if you block ExaSearchBot

Exa says User-agent: ExaSearchBot with Disallow: / blocks ExaSearchBot from the whole site. If there is no ExaSearchBot group, it follows the rules set for major search engines, otherwise the * group. The vendor says robots.txt controls crawling, not indexing, so already indexed pages are removed with a noindex meta tag or X-Robots-Tag header.

## The robots.txt lines

To allow ExaSearchBot:

```
User-agent: ExaSearchBot
Allow: /
```

To block ExaSearchBot:

```
User-agent: ExaSearchBot
Disallow: /
```

Paste a block into the robots.txt at the root of your host, for example https://example.com/robots.txt. A group for one token does not cover the operator's other crawlers.

The user-agent string the vendor shows:

```
Mozilla/5.0 (compatible; ExaSearchBot/1.0; +https://crawler.exa.ai/)
```

## How to tell a real request from a fake one

The vendor says every request is cryptographically signed with HTTP Message Signatures (Web Bot Auth) and gives a public key directory to verify against, and that verification holds regardless of IP address.

## Compare with PerplexityBot

[PerplexityBot](/bots/perplexitybot): Both are search-index crawlers that feed AI answers with cited sources; ExaSearchBot signs its requests with Web Bot Auth and falls back to major search engines' rules when it has no group of its own.

## Your own site

The free check in the box above tests eight crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot). ExaSearchBot is not one of them: read your robots.txt for a `ExaSearchBot` group and look for the user agent in your server log. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does ExaSearchBot follow robots.txt?

Yes, vendor says it checks robots.txt before fetching. Give ExaSearchBot its own User-agent group in robots.txt: the operator's other crawlers have their own settings.

### How do I know ExaSearchBot is really blocked?

robots.txt is only one layer: a CDN or firewall rule can also turn a crawler away, and a crawler can ignore the file. Check your server log for the user agent, and test the address from outside your network.

## Sources

- [Exa: Exa Search Crawler](https://crawler.exa.ai/)
- [Exa: FAQs](https://exa.ai/docs/admin/faqs)
