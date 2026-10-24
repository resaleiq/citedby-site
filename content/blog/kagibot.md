title: Kagibot: what it does and what blocking it changes
h1: Kagibot: what it does and what blocking it changes
description: Kagibot (Kagi): search. Robots.txt token, what a Disallow changes and how to verify a request, read from the operator's own page.
slug: kagibot
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about Kagibot: operator Kagi, job Search, obeys robots.txt Yes, address list Listed on its page
hero_sub: Kagibot, run by Kagi
hero_boxes: Operator|Kagi; Job|Search; Obeys robots.txt|Yes; Address list|Listed on its page
widget: on
related: /bots|All AI crawlers compared; /bots/googlebot|Googlebot; /platforms|AI crawler settings by platform; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website? What decides it
answer: Kagibot is the web crawler for the Kagi search engine. Kagi says standard robots.txt directives that target Kagibot are respected, and that when no rule targets Kagibot but one targets Googlebot, Kagibot follows the Googlebot directives. Kagi publishes its user-agent string and the IP addresses its requests come from.

## What Kagibot is

Kagibot is the web crawler for the Kagi search engine. Kagi publishes its user-agent string and the IP addresses that Kagibot requests originate from.

| Fact | Kagibot |
| --- | --- |
| Operator | Kagi |
| Job | Search |
| robots.txt token | `Kagibot` |
| Follows robots.txt | Yes, standard robots.txt directives targeting Kagibot are respected |
| IP addresses | Listed on the vendor's page (kagi.com/bot) |
| Vendor page read | 24 October 2026 |

## What the vendor says

In the vendor's words (English original): “Standard directives in robots.txt that target Kagibot are respected.”

Source: [Kagi: About KagiBot](https://kagi.com/bot), read on 24 October 2026.

## What happens if you block Kagibot

Kagi says standard robots.txt directives that target Kagibot are respected, for example Disallow rules for a path. If there is no rule for Kagibot but there is one for Googlebot, Kagibot follows the Googlebot directives.

## The robots.txt lines

To allow Kagibot:

```
User-agent: Kagibot
Allow: /
```

To block Kagibot:

```
User-agent: Kagibot
Disallow: /
```

Paste a block into the robots.txt at the root of your host, for example https://example.com/robots.txt. A group for one token does not cover the operator's other crawlers.

The user-agent string the vendor shows:

```
Mozilla/5.0 (compatible; Kagibot/1.0; +https://kagi.com/bot)
```

## How to tell a real request from a fake one

Kagi lists the IP addresses (with kagibot.org hostnames) that requests from Kagibot originate from on its bot page.

## Compare with Googlebot

[Googlebot](/bots/googlebot): Kagibot follows its own robots.txt rules, and falls back to the Googlebot rules when none target Kagibot.

## Your own site

The free check in the box above tests eight crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot). Kagibot is not one of them: read your robots.txt for a `Kagibot` group and look for the user agent in your server log. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does Kagibot follow robots.txt?

Yes, standard robots.txt directives targeting Kagibot are respected. Give Kagibot its own User-agent group in robots.txt: the operator's other crawlers have their own settings.

### How do I know Kagibot is really blocked?

robots.txt is only one layer: a CDN or firewall rule can also turn a crawler away, and a crawler can ignore the file. Check your server log for the user agent, and test the address from outside your network.

## Sources

- [Kagi: About KagiBot (read 2026-10-24)](https://kagi.com/bot)
