title: DuckDuckBot: what it does and what blocking it changes
h1: DuckDuckBot: what it does and what blocking it changes
description: DuckDuckBot (DuckDuckGo): search. Robots.txt token, what a Disallow changes and how to verify a request, read from the operator's own page.
slug: duckduckbot
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about DuckDuckBot: operator DuckDuckGo, job Search, obeys robots.txt Yes, address list 486 addresses
hero_sub: DuckDuckBot, run by DuckDuckGo
hero_boxes: Operator|DuckDuckGo; Job|Search; Obeys robots.txt|Yes; Address list|486 addresses
widget: on
related: /bots|All AI crawlers compared; /bots/duckassistbot|DuckAssistBot; /platforms|AI crawler settings by platform; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website? What decides it
answer: DuckDuckBot is the web crawler for DuckDuckGo, whose stated job is to improve DuckDuckGo's search results. DuckDuckGo says it respects WWW::RobotRules and publishes its IP addresses as a list in JSON form. DuckAssistBot, the fetcher for AI-assisted answers, is documented on a separate DuckDuckGo help page.

## What DuckDuckBot is

DuckDuckBot is the web crawler for DuckDuckGo. DuckDuckGo says its job is to improve DuckDuckGo's search results. DuckDuckGo's help pages list DuckAssistBot on a separate page.

| Fact | DuckDuckBot |
| --- | --- |
| Operator | DuckDuckGo |
| Job | Search |
| robots.txt token | `DuckDuckBot` |
| Follows robots.txt | Yes, respects WWW::RobotRules (no timing note published) |
| IP addresses | 486 addresses (duckduckgo.com/duckduckbot.json, file dated 2026-09-01) |
| Vendor page read | 24 October 2026 |

## What the vendor says

In the vendor's words (English original): “DuckDuckBot’s job is to constantly improve our search results and offer users the best and most secure search experience possible.”

Source: [DuckDuckGo Help Pages: Is DuckDuckBot related to DuckDuckGo?](https://duckduckgo.com/duckduckgo-help-pages/results/duckduckbot), read on 24 October 2026.

## What happens if you block DuckDuckBot

DuckDuckGo says DuckDuckBot respects WWW::RobotRules, so a Disallow rule addressed to DuckDuckBot in robots.txt applies to this crawler. The page says nothing about what blocking it changes in DuckDuckGo results, and nothing about DuckAssistBot.

## The robots.txt lines

To allow DuckDuckBot:

```
User-agent: DuckDuckBot
Allow: /
```

To block DuckDuckBot:

```
User-agent: DuckDuckBot
Disallow: /
```

Paste a block into the robots.txt at the root of your host, for example https://example.com/robots.txt. A group for one token does not cover the operator's other crawlers.

The user-agent string the vendor shows:

```
DuckDuckBot/1.1; (+http://duckduckgo.com/duckduckbot.html)
```

## How to tell a real request from a fake one

The file at duckduckgo.com/duckduckbot.json held 486 addresses on 24 October 2026, file dated 2026-09-01.

DuckDuckGo says the crawler originates from the IP addresses listed on its help page, also available as JSON at duckduckgo.com/duckduckbot.json.

## Compare with DuckAssistBot

[DuckAssistBot](/bots/duckassistbot): DuckDuckBot is the crawler for DuckDuckGo search results, while DuckAssistBot is documented by DuckDuckGo on its own help page.

## Your own site

The free check in the box above tests eight crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot). DuckDuckBot is not one of them: read your robots.txt for a `DuckDuckBot` group and look for the user agent in your server log. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does DuckDuckBot follow robots.txt?

Yes, respects WWW::RobotRules (no timing note published). Give DuckDuckBot its own User-agent group in robots.txt: the operator's other crawlers have their own settings.

### How do I know DuckDuckBot is really blocked?

robots.txt is only one layer: a CDN or firewall rule can also turn a crawler away, and a crawler can ignore the file. Check your server log for the user agent, and test the address from outside your network.

## Sources

- [DuckDuckGo Help Pages: Is DuckDuckBot related to DuckDuckGo?](https://duckduckgo.com/duckduckgo-help-pages/results/duckduckbot)
- [DuckDuckBot IP list (JSON, creationTime 2026-09-01, read 2026-10-24)](https://duckduckgo.com/duckduckbot.json)
