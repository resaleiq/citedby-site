title: PerplexityBot vs Perplexity-User: differences and how to allow it
h1: PerplexityBot: how it differs from Perplexity-User and how to allow it
description: PerplexityBot surfaces and links sites in Perplexity search; it is not used for foundation model crawling. User-agent, the 8 IP ranges published, WAF advice.
slug: perplexitybot
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Four facts about PerplexityBot: operator Perplexity, job Search, robots.txt behaviour, published address lists
hero_sub: PerplexityBot, run by Perplexity
hero_boxes: Operator|Perplexity; Job|Search; Obeys robots.txt|Yes; Address list|8 ranges
widget: on
related: /bots|All AI crawlers compared; /blog/is-gptbot-blocked|Is GPTBot blocked on your site?; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website?
answer: PerplexityBot is Perplexity's crawler for surfacing and linking websites in its search results. Perplexity says it is not used to crawl content for AI foundation models. It follows robots.txt, changes can take up to 24 hours to apply, and Perplexity publishes 8 IP ranges for it.

## What PerplexityBot is

Perplexity names two agents. PerplexityBot builds the search index; Perplexity-User visits a page when a person asks. Perplexity's page contains configuration guidelines for popular WAF providers because a firewall can stop the crawler before robots.txt matters.

| Fact | PerplexityBot |
| --- | --- |
| Operator | Perplexity |
| Job | Search |
| robots.txt token | `PerplexityBot` |
| Follows robots.txt | Yes, it follows robots.txt |
| Published address list | 8 ranges (perplexity.com/perplexitybot.json, file dated 2025-02-07) |
| Vendor page read | 21 October 2026 |

## What the vendor says

In the vendor's words: “PerplexityBot is designed to surface and link websites in search results on Perplexity. It is not used to crawl content for AI foundation models.”

Source: [Perplexity: Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers), read on 21 October 2026.

## What happens if you block it

Perplexity recommends allowing PerplexityBot in robots.txt and permitting requests from its published IP ranges if you want to appear in its search results. It also says changes to your robots.txt can take up to 24 hours to be reflected in its systems, so a check made an hour after an edit proves little.

## The robots.txt lines

To allow it:

```
User-agent: PerplexityBot
Allow: /
```

To block it:

```
User-agent: PerplexityBot
Disallow: /
```

The user-agent string the vendor shows:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)
```

## How to tell a real request from a fake one

Perplexity's file at perplexity.com/perplexitybot.json held 8 prefixes on 21 October 2026, creation time 2025-02-07. Its WAF section suggests a rule that combines the user-agent with the IP condition, so a request claiming the name from another address does not get through.

## Compare with Perplexity-User

[Perplexity-User](/bots/perplexity-user): The user-triggered fetcher; Perplexity says it generally ignores robots.txt.

## Check your own site

The free check in the box above reads robots.txt for the crawlers in this set and sends one live request per crawler, so a rule that robots.txt allows but a firewall refuses shows up. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### How long does a robots.txt change take for PerplexityBot?

Perplexity says it may take up to 24 hours for its systems to reflect a change.

### Does PerplexityBot train AI models?

Perplexity says it is not used to crawl content for AI foundation models.

## Sources

- [Perplexity: Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers)
- [perplexity.com/perplexitybot.json](https://www.perplexity.ai/perplexitybot.json), read 21 October 2026
