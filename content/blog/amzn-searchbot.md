title: Amzn-SearchBot: what it does and what blocking it changes
h1: Amzn-SearchBot: what it does and what blocking it changes
description: Amzn-SearchBot (Amazon): search. Robots.txt token, what a Disallow changes and how to verify a request, read from the operator's own page.
slug: amzn-searchbot
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about Amzn-SearchBot: operator Amazon, job Search, obeys robots.txt Yes, address list Listed on its page
hero_sub: Amzn-SearchBot, run by Amazon
hero_boxes: Operator|Amazon; Job|Search; Obeys robots.txt|Yes; Address list|Listed on its page
widget: on
related: /bots|All AI crawlers compared; /bots/amazonbot|Amazonbot; /platforms|AI crawler settings by platform; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website? What decides it
answer: Amzn-SearchBot is an Amazon crawler used to improve search experiences such as Alexa. Amazon says allowing it makes your content eligible to appear there, and that it does not crawl for generative AI model training. Its setting is independent of Amazonbot and Amzn-User, and a change can take about 24 hours.

## What Amzn-SearchBot is

Amzn-SearchBot is an Amazon crawler used to improve search experiences in Amazon products and services. Amazon says that allowing it makes your content eligible to appear in search experiences such as Alexa, and that it does not crawl content for generative AI model training. It is one of three Amazon user agents (Amazonbot, Amzn-SearchBot, Amzn-User) that Amazon documents on one page.

| Fact | Amzn-SearchBot |
| --- | --- |
| Operator | Amazon |
| Job | Search |
| robots.txt token | `Amzn-SearchBot` |
| Follows robots.txt | Yes, changes may take about 24 hours |
| IP addresses | Listed on the vendor's page (developer.amazon.com/amazonbot/searchbot-ip-addresses) |
| Vendor page read | 24 October 2026 |

## What the vendor says

In the vendor's words (English original): “If robots.txt files don’t mention Amzn-SearchBot but allow other search bots, Amzn-SearchBot will crawl in accordance with the robots.txt directives given to other search bots.”

Source: [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot), read on 24 October 2026.

## What happens if you block Amzn-SearchBot

Amazon says automated crawling from its listed user agents respects the Robots Exclusion Protocol, honoring the user-agent and allow/disallow directives. Amazon says each user agent setting is independent of the others and may take about 24 hours to take effect. If robots.txt does not mention Amzn-SearchBot but allows other search bots, it follows the directives given to those other search bots.

## The robots.txt lines

To allow Amzn-SearchBot:

```
User-agent: Amzn-SearchBot
Allow: /
```

To block Amzn-SearchBot:

```
User-agent: Amzn-SearchBot
Disallow: /
```

Paste a block into the robots.txt at the root of your host, for example https://example.com/robots.txt. A group for one token does not cover the operator's other crawlers.

The user-agent string the vendor shows:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Amzn-SearchBot/0.1) Chrome/W.X.Y.Z Safari/537.36
```

## How to tell a real request from a fake one

Amazon publishes the Amzn-SearchBot IP addresses on a web page that shows the list as JSON, and links it from the Amazonbot documentation page.

## Compare with Amazonbot

[Amazonbot](/bots/amazonbot): Amazonbot is used to improve Amazon products and services and may be used to train Amazon AI models, while Amzn-SearchBot is for search experiences and Amazon says it does not crawl for generative AI model training.

## Your own site

The free check in the box above tests eight crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot). Amzn-SearchBot is not one of them: read your robots.txt for a `Amzn-SearchBot` group and look for the user agent in your server log. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does Amzn-SearchBot follow robots.txt?

Yes, changes may take about 24 hours. Give Amzn-SearchBot its own User-agent group in robots.txt: the operator's other crawlers have their own settings.

### How do I know Amzn-SearchBot is really blocked?

robots.txt is only one layer: a CDN or firewall rule can also turn a crawler away, and a crawler can ignore the file. Check your server log for the user agent, and test the address from outside your network.

## Sources

- [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot)
- [Amazon: Amzn-SearchBot IP addresses (read 2026-10-24)](https://developer.amazon.com/amazonbot/searchbot-ip-addresses/)
