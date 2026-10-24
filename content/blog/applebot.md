title: Applebot: what it does and what blocking it changes
h1: Applebot: what it does and what blocking it changes
description: Applebot (Apple): several jobs. Robots.txt token, what a Disallow changes and how to verify a request, read from the operator's own page.
slug: applebot
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about Applebot: operator Apple, job Several jobs, obeys robots.txt Yes, address list 24 ranges
hero_sub: Applebot, run by Apple
hero_boxes: Operator|Apple; Job|Several jobs; Obeys robots.txt|Yes; Address list|24 ranges
widget: on
related: /bots|All AI crawlers compared; /bots/applebot-extended|Applebot-Extended; /platforms|AI crawler settings by platform; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website? What decides it
answer: Applebot is Apple's web crawler. Apple says its data powers search in Spotlight, Siri and Safari and may also help train Apple's foundation models. Disallowing Applebot-Extended opts content out of training only. If robots.txt does not mention Applebot but does mention Googlebot, Applebot follows the Googlebot rules.

## What Applebot is

Applebot is Apple's web crawler. Apple says its data powers search technology in Spotlight, Siri and Safari, and may also be used to help train Apple foundation models and to provide context when AI models generate output in Apple products. Apple also documents a separate Applebot-Extended token and an iTMS user agent for Apple Podcasts.

| Fact | Applebot |
| --- | --- |
| Operator | Apple |
| Job | Search (crawled data may also help train Apple models) |
| robots.txt token | `Applebot` |
| Follows robots.txt | Yes, for general search crawls targeted at Applebot |
| IP addresses | 24 ranges (search.developer.apple.com/applebot.json, file dated 2026-09-15) |
| Vendor page read | 24 October 2026 |

## What the vendor says

In the vendor's words (English original): “Applebot respects standard robots.txt directives in general search crawls that are targeted at Applebot.”

Source: [Apple: About Applebot](https://support.apple.com/en-us/119829), read on 24 October 2026.

## What happens if you block Applebot

Apple says disallowing Applebot-Extended opts content out of training Apple's generative foundation models, but the site may still be crawled by Applebot and stay discoverable through Spotlight, Siri and Safari. A Disallow for Applebot itself applies to general search crawls targeted at Applebot, and Apple says that if robots.txt does not mention Applebot but mentions Googlebot, Applebot follows the Googlebot instructions. Apple says the nosnippet meta tag opts content out of broad world knowledge answers.

## The robots.txt lines

To allow Applebot:

```
User-agent: Applebot
Allow: /
```

To block Applebot:

```
User-agent: Applebot
Disallow: /
```

Paste a block into the robots.txt at the root of your host, for example https://example.com/robots.txt. A group for one token does not cover the operator's other crawlers.

The user-agent string the vendor shows:

```
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15 (Applebot/0.1; +http://www.apple.com/go/applebot)
```

## How to tell a real request from a fake one

The file at search.developer.apple.com/applebot.json held 24 ranges on 24 October 2026, file dated 2026-09-15.

Apple says Applebot traffic is generally identified by reverse DNS in the *.applebot.apple.com domain, or by matching the IP address with a CIDR prefix in its published JSON file.

## Compare with Applebot-Extended

[Applebot-Extended](/bots/applebot-extended): Applebot is the crawler that fetches pages for Apple search features, while Applebot-Extended is the robots.txt token that controls whether crawled content is used to train Apple generative models.

## Your own site

The free check in the box above tests eight crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot). Applebot is not one of them: read your robots.txt for a `Applebot` group and look for the user agent in your server log. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does Applebot follow robots.txt?

Yes, for general search crawls targeted at Applebot. Give Applebot its own User-agent group in robots.txt: the operator's other crawlers have their own settings.

### How do I know Applebot is really blocked?

robots.txt is only one layer: a CDN or firewall rule can also turn a crawler away, and a crawler can ignore the file. Check your server log for the user agent, and test the address from outside your network.

## Sources

- [Apple: About Applebot](https://support.apple.com/en-us/119829)
- [Apple: Applebot IP CIDRs JSON (read 2026-10-24)](https://search.developer.apple.com/applebot.json)
