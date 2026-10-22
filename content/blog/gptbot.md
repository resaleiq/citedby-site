title: GPTBot: what it does and what blocking it changes
h1: GPTBot: what it does and what blocking it changes
description: GPTBot crawls content that may be used to train OpenAI models. What a Disallow does, what it leaves alone, its user-agent and the 18 IP ranges OpenAI publishes.
slug: gptbot
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Four facts about GPTBot: operator OpenAI, job Training, robots.txt behaviour, published address lists
hero_sub: GPTBot, run by OpenAI
hero_boxes: Operator|OpenAI; Job|Training; Obeys robots.txt|Yes; Address list|18 ranges
widget: on
related: /bots|All AI crawlers compared; /bots/oai-searchbot|OAI-SearchBot; /blog/is-gptbot-blocked|Is GPTBot blocked on your site?; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website?
answer: GPTBot is OpenAI's training crawler. Disallowing it in robots.txt tells OpenAI the site's content should not be used to train its generative AI foundation models. It does not control ChatGPT search, which uses OAI-SearchBot. OpenAI publishes 18 IP ranges for GPTBot.

## What GPTBot is

GPTBot is the crawler people usually mean when they say "block OpenAI". OpenAI's page says it is used to crawl content that may be used in training its models. It is one of three crawlers named in the OpenAI documentation for the ChatGPT product family, next to [OAI-SearchBot](/bots/oai-searchbot) and [ChatGPT-User](/bots/chatgpt-user).

| Fact | GPTBot |
| --- | --- |
| Operator | OpenAI |
| Job | Training |
| robots.txt token | `GPTBot` |
| Follows robots.txt | Yes, it follows robots.txt |
| Published address list | 18 ranges (openai.com/gptbot.json, file dated 2026-09-22) |
| Vendor page read | 21 October 2026 |

## What the vendor says

In the vendor's words: “GPTBot is used to make our generative AI foundation models more useful and safe. It is used to crawl content that may be used in training our generative AI foundation models. Disallowing GPTBot indicates a site's content should not be used in training generative AI foundation models.”

Source: [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots), read on 21 October 2026.

## What happens if you block it

OpenAI frames a GPTBot Disallow as a signal about training: the content should not be used in training generative AI foundation models. The same page gives an example of a site allowing OAI-SearchBot to appear in search results while disallowing GPTBot, so a block here does not by itself take you out of ChatGPT's search answers. Whether to block is a business choice; both are legitimate.

## The robots.txt lines

To allow it:

```
User-agent: GPTBot
Allow: /
```

To block it:

```
User-agent: GPTBot
Disallow: /
```

The user-agent string the vendor shows:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.4; +https://openai.com/gptbot
```

## How to tell a real request from a fake one

The GPTBot list at openai.com/gptbot.json is the shortest of the three OpenAI files we counted: 18 prefixes on 21 October 2026, creation time 2026-09-22. When a request names GPTBot but comes from an address outside that list, the name alone proves nothing.

## Compare with OAI-SearchBot

[OAI-SearchBot](/bots/oai-searchbot): Allow it and disallow GPTBot to stay in ChatGPT search while opting out of training.

## Check your own site

The free check in the box above reads robots.txt for the crawlers in this set and sends one live request per crawler, so a rule that robots.txt allows but a firewall refuses shows up. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### If I block GPTBot, will ChatGPT stop mentioning my shop?

Not through GPTBot alone. OpenAI treats its crawler settings as independent and says search appearance is managed through OAI-SearchBot. Check both tokens in your robots.txt.

### How do I know GPTBot is really blocked?

Robots.txt is only one layer. A CDN or firewall rule can also turn the crawler away. Our guide to the four places GPTBot can be stopped shows a two-request test for each.

## Sources

- [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots)
- [openai.com/gptbot.json](https://openai.com/gptbot.json), read 21 October 2026
