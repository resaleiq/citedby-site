title: Diffbot: what it does and what blocking it changes
h1: Diffbot: what it does and what blocking it changes
description: Diffbot (Diffbot): search. Robots.txt token, what a Disallow changes and how to verify a request, read from the operator's own page.
slug: diffbot
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about Diffbot: operator Diffbot, job Search, obeys robots.txt Yes, address list None
hero_sub: Diffbot, run by Diffbot
hero_boxes: Operator|Diffbot; Job|Search; Obeys robots.txt|Yes; Address list|None
widget: on
related: /bots|All AI crawlers compared; /bots/bingbot|Bingbot; /platforms|AI crawler settings by platform; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website? What decides it
answer: Diffbot documents two user agents. Diffbot crawls the web proactively for a general search engine, so sites can be discovered and cited from its Knowledge Graph. Diffbot-User fetches a URL for a person using its software. Diffbot says its crawls follow robots.txt by default, including disallow and crawl-delay.

## What Diffbot is

Diffbot documents two user agents. Diffbot is used for general, proactive web crawling for building a general search engine, so sites can be discovered and cited from the Diffbot Knowledge Graph and web search services. Diffbot-User is used for requests made on behalf of a human user browsing a URL with Diffbot software.

| Fact | Diffbot |
| --- | --- |
| Operator | Diffbot |
| Job | Search (general web crawl) |
| robots.txt token | `Diffbot` |
| Follows robots.txt | Yes, by default (disallow and crawl-delay directives) |
| IP addresses | None published |
| Vendor page read | 24 October 2026 |

## What the vendor says

In the vendor's words (English original): “By default Diffbot's web crawls adhere to a site’s robots.txt instructions, including the disallow and crawl-delay directives.”

Source: [Diffbot: Does Diffbot respect robots.txt?](https://www.diffbot.com/docs/crawl/faq/robots-txt), read on 24 October 2026.

## What happens if you block Diffbot

Diffbot says its web crawls follow robots.txt by default, including disallow and crawl-delay, and that a rule can be overridden in specific cases such as a partnership or agreement with the site. It lists Diffbot and Diffbot-User as separate user agents, and says users of its Extract and Crawlbot APIs define their own crawl parameters and can set their own User-Agent.

## The robots.txt lines

To allow Diffbot:

```
User-agent: Diffbot
Allow: /
```

To block Diffbot:

```
User-agent: Diffbot
Disallow: /
```

Paste a block into the robots.txt at the root of your host, for example https://example.com/robots.txt. A group for one token does not cover the operator's other crawlers.

The user-agent string the vendor shows:

```
Diffbot
```

## How to tell a real request from a fake one

The vendor page does not describe an IP list or verification method.

## Compare with Bingbot

[Bingbot](/bots/bingbot): Diffbot is described by its operator as similar to Googlebot and Bing, a general crawler for a search index, and the vendor says it is not used for AI training.

## Your own site

The free check in the box above tests eight crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot). Diffbot is not one of them: read your robots.txt for a `Diffbot` group and look for the user agent in your server log. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does Diffbot follow robots.txt?

Yes, by default (disallow and crawl-delay directives). Give Diffbot its own User-agent group in robots.txt: the operator's other crawlers have their own settings.

### How do I know Diffbot is really blocked?

robots.txt is only one layer: a CDN or firewall rule can also turn a crawler away, and a crawler can ignore the file. Check your server log for the user agent, and test the address from outside your network.

## Sources

- [Diffbot: Does Diffbot respect robots.txt? (read 2026-10-24)](https://www.diffbot.com/docs/crawl/faq/robots-txt)
