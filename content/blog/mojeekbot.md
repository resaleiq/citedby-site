title: MojeekBot: what it does and what blocking it changes
h1: MojeekBot: what it does and what blocking it changes
description: MojeekBot (Mojeek): search. Robots.txt token, what a Disallow changes and how to verify a request, read from the operator's own page.
slug: mojeekbot
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about MojeekBot: operator Mojeek, job Search, obeys robots.txt Yes, address list 1 ranges
hero_sub: MojeekBot, run by Mojeek
hero_boxes: Operator|Mojeek; Job|Search; Obeys robots.txt|Yes; Address list|1 ranges
widget: on
related: /bots|All AI crawlers compared; /bots/bingbot|Bingbot; /platforms|AI crawler settings by platform; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website? What decides it
answer: MojeekBot is the web crawler for the Mojeek search engine. Mojeek says it obeys the Robots Exclusion Standard, using the first record whose User-Agent contains MojeekBot, and does not support the nonstandard crawl-delay directive. It should not request more than one page from a site in the same second.

## What MojeekBot is

MojeekBot is the web crawler for the Mojeek search engine. Mojeek says it should not request more than one page from a site within the same 1 second period. It obeys the noindex, nocache and nofollow meta tags.

| Fact | MojeekBot |
| --- | --- |
| Operator | Mojeek |
| Job | Search |
| robots.txt token | `MojeekBot` |
| Follows robots.txt | Yes, obeys the Robots Exclusion Standard; crawl-delay is not supported |
| IP addresses | 1 ranges (www.mojeek.com/mojeekbot.json, file dated 2025-05-14) |
| Vendor page read | 24 October 2026 |

## What the vendor says

In the vendor's words (English original): “MojeekBot is the web crawler for the Mojeek search engine.”

Source: [Mojeek: MojeekBot](https://www.mojeek.com/bot.html), read on 24 October 2026.

## What happens if you block MojeekBot

Mojeek says MojeekBot obeys the first robots.txt record whose User-Agent contains MojeekBot, and otherwise the first record for User-Agent *. It will not retrieve URLs containing a disallowed string. It does not support the nonstandard crawl-delay directive.

## The robots.txt lines

To allow MojeekBot:

```
User-agent: MojeekBot
Allow: /
```

To block MojeekBot:

```
User-agent: MojeekBot
Disallow: /
```

Paste a block into the robots.txt at the root of your host, for example https://example.com/robots.txt. A group for one token does not cover the operator's other crawlers.

The user-agent string the vendor shows:

```
MojeekBot
```

## How to tell a real request from a fake one

The file at www.mojeek.com/mojeekbot.json held 1 ranges on 24 October 2026, file dated 2025-05-14.

Mojeek says to reverse-resolve the visiting IP to a name in the mojeek.com domain and forward-resolve it back to the same IP, or to match the IP against its published list of MojeekBot IP addresses.

## Compare with Bingbot

[Bingbot](/bots/bingbot): Both crawl for a search engine; Mojeek publishes a one-range IP list and a reverse DNS check, and does not support crawl-delay.

## Your own site

The free check in the box above tests eight crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot). MojeekBot is not one of them: read your robots.txt for a `MojeekBot` group and look for the user agent in your server log. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does MojeekBot follow robots.txt?

Yes, obeys the Robots Exclusion Standard; crawl-delay is not supported. Give MojeekBot its own User-agent group in robots.txt: the operator's other crawlers have their own settings.

### How do I know MojeekBot is really blocked?

robots.txt is only one layer: a CDN or firewall rule can also turn a crawler away, and a crawler can ignore the file. Check your server log for the user agent, and test the address from outside your network.

## Sources

- [Mojeek: MojeekBot](https://www.mojeek.com/bot.html)
- [MojeekBot IP list (JSON, creationTime 2025-05-14, read 2026-10-24)](https://www.mojeek.com/mojeekbot.json)
