title: ClaudeBot: Anthropic's training crawler, Crawl-delay and blocking
h1: ClaudeBot: Anthropic's training crawler, Crawl-delay and blocking
description: ClaudeBot collects web content that could contribute to Anthropic's model training. The robots.txt group, the Crawl-delay Anthropic supports and why IP blocking does not work.
slug: claudebot
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Four facts about ClaudeBot: operator Anthropic, job Training, robots.txt behaviour, published address lists
hero_sub: ClaudeBot, run by Anthropic
hero_boxes: Operator|Anthropic; Job|Training; Obeys robots.txt|Yes; Address list|Anthropic points to a list
widget: on
related: /bots|All AI crawlers compared; /bots/claude-searchbot|Claude-SearchBot; /blog/is-gptbot-blocked|Is GPTBot blocked on your site?; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website?
answer: ClaudeBot is Anthropic's crawler for content that could contribute to model training. A robots.txt Disallow signals that a site's future materials should be excluded from training datasets. Anthropic honours Crawl-delay, and warns that blocking its IP addresses can stop it reading robots.txt, so use robots.txt instead.

## What ClaudeBot is

Anthropic names three robots in its help article: ClaudeBot for training data, [Claude-User](/bots/claude-user) for pages fetched at a user's request, and [Claude-SearchBot](/bots/claude-searchbot) for search quality. ClaudeBot is the training one. The article is dated 7 April 2026.

| Fact | ClaudeBot |
| --- | --- |
| Operator | Anthropic |
| Job | Training |
| robots.txt token | `ClaudeBot` |
| Follows robots.txt | Yes, it follows robots.txt and Crawl-delay |
| Published address list | Anthropic points to a list but advises against IP blocking |
| Vendor page read | 21 October 2026 |

## What the vendor says

In the vendor's words: “ClaudeBot helps enhance the utility and safety of our generative AI models by collecting web content that could potentially contribute to their training. When a site restricts ClaudeBot access, it signals that the site's future materials should be excluded from our AI model training datasets.”

Source: [Anthropic Help Center: Does Anthropic crawl data from the web, and how can site owners block the crawler? (7 April 2026)](https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler), read on 21 October 2026.

## What happens if you block it

Anthropic says a restriction signals that the site's future materials should be excluded from its training datasets. The wording says "future materials"; it does not say what happens to content already collected. The other two Claude robots are separate, so blocking ClaudeBot leaves their rules untouched.

## The robots.txt lines

To allow it:

```
User-agent: ClaudeBot
Allow: /
```

To block it:

```
User-agent: ClaudeBot
Disallow: /
```

## How to tell a real request from a fake one

Anthropic's article says its robots respect "do not crawl" signals in robots.txt and will not try to bypass CAPTCHAs. It supports the non-standard Crawl-delay directive, for example `User-agent: ClaudeBot` followed by `Crawl-delay: 1`. It also says that blocking by IP address may not give a lasting opt-out, because it stops the robot from reading robots.txt. Anthropic's article states that robots.txt must be set for every subdomain you want to opt out.

## Compare with Claude-SearchBot

[Claude-SearchBot](/bots/claude-searchbot): A separate search robot: blocking ClaudeBot does not touch it.

## Check your own site

The audit box above reads robots.txt for the crawlers in this set and sends one live request per crawler, so a rule that robots.txt allows but a firewall refuses shows up. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does ClaudeBot support Crawl-delay?

Yes. Anthropic says it supports the non-standard Crawl-delay extension and gives `Crawl-delay: 1` under `User-agent: ClaudeBot` as an example.

### Do I need a robots.txt file on every subdomain?

Anthropic's article says to add the rule at the top level for every subdomain you want to opt out. A rule on example.com does not cover shop.example.com.

## Sources

- [Anthropic Help Center: Does Anthropic crawl data from the web, and how can site owners block the crawler? (7 April 2026)](https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)
