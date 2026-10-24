title: Perplexity-User: what it does and what blocking it changes
h1: Perplexity-User: what it does and what blocking it changes
description: Perplexity-User (Perplexity): user-triggered fetch. Robots.txt token, what a Disallow changes and how to verify a request, read from the operator's own page.
slug: perplexity-user
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about Perplexity-User: operator Perplexity, job User-triggered fetch, obeys robots.txt Not always, address list 4 ranges
hero_sub: Perplexity-User, run by Perplexity
hero_boxes: Operator|Perplexity; Job|User-triggered fetch; Obeys robots.txt|Not always; Address list|4 ranges
widget: on
related: /bots|All AI crawlers compared; /bots/perplexitybot|PerplexityBot; /platforms|AI crawler settings by platform; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website? What decides it
answer: Perplexity-User is Perplexity's user-action fetcher: when a user asks a question, it may visit a page to answer accurately and link to it. Perplexity says it is not used for web crawling or for training AI models, and that it generally ignores robots.txt rules because a user requested the fetch.

## What Perplexity-User is

Perplexity-User is Perplexity's user-action fetcher. When a user asks Perplexity a question, it might visit a web page to help provide an accurate answer and include a link to the page in its response. Perplexity says it is not used for web crawling or to collect content for training AI foundation models, and it is separate from PerplexityBot, which surfaces and links websites in Perplexity search results.

| Fact | Perplexity-User |
| --- | --- |
| Operator | Perplexity |
| Job | User-triggered fetch |
| robots.txt token | `Perplexity-User` |
| Follows robots.txt | Generally ignores robots.txt rules, because a user requested the fetch |
| IP addresses | 4 ranges (www.perplexity.com/perplexity-user.json, file dated 2025-10-17) |
| Vendor page read | 24 October 2026 |

## What the vendor says

In the vendor's words (English original): “Since a user requested the fetch, this fetcher generally ignores robots.txt rules.”

Source: [Perplexity: Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers), read on 24 October 2026.

## What happens if you block Perplexity-User

Perplexity lists Perplexity-User as a robots.txt token and says it controls which sites these user requests can access. Perplexity also says this fetcher generally ignores robots.txt rules because a user requested the fetch. Perplexity says each of its robots.txt settings works independently and changes may take up to 24 hours to take effect.

## The robots.txt lines

To allow Perplexity-User:

```
User-agent: Perplexity-User
Allow: /
```

To block Perplexity-User:

```
User-agent: Perplexity-User
Disallow: /
```

Paste a block into the robots.txt at the root of your host, for example https://example.com/robots.txt. A group for one token does not cover the operator's other crawlers.

The user-agent string the vendor shows:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Perplexity-User/1.0; +https://perplexity.ai/perplexity-user)
```

## How to tell a real request from a fake one

The file at www.perplexity.com/perplexity-user.json held 4 ranges on 24 October 2026, file dated 2025-10-17.

Perplexity publishes the Perplexity-User IP addresses as a JSON file and says to use it as the source of truth for allow rules, combined with the user-agent string.

## Compare with PerplexityBot

[PerplexityBot](/bots/perplexitybot): PerplexityBot surfaces and links sites in Perplexity search results, while Perplexity-User fetches a page when a user's question needs it and generally ignores robots.txt.

## Your own site

The free check in the box above tests eight crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot). Perplexity-User is not one of them: read your robots.txt for a `Perplexity-User` group and look for the user agent in your server log. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does Perplexity-User follow robots.txt?

Generally ignores robots.txt rules, because a user requested the fetch. A rule for Perplexity-User in robots.txt may therefore not stop it. To refuse it for certain, use a firewall or CDN rule that matches both the user agent and the published addresses.

### How do I know Perplexity-User is really blocked?

robots.txt is only one layer: a CDN or firewall rule can also turn a crawler away, and a crawler can ignore the file. Check your server log for the user agent, and test the address from outside your network.

## Sources

- [Perplexity: Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers)
- [Perplexity: Perplexity-User IP addresses JSON (read 2026-10-24)](https://www.perplexity.com/perplexity-user.json)
