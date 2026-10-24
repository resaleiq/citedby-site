title: Storebot-Google: what it does and what blocking it changes
h1: Storebot-Google: what it does and what blocking it changes
description: Storebot-Google (Google): search. Robots.txt token, what a Disallow changes and how to verify a request, read from the operator's own page.
slug: storebot-google
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about Storebot-Google: operator Google, job Search, obeys robots.txt Yes, address list 317 ranges
hero_sub: Storebot-Google, run by Google
hero_boxes: Operator|Google; Job|Search; Obeys robots.txt|Yes; Address list|317 ranges
widget: on
related: /bots|All AI crawlers compared; /bots/googlebot|Googlebot; /platforms|AI crawler settings by platform; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website? What decides it
answer: Storebot-Google is the crawler Google documents as Google StoreBot among its common crawlers. Google says a Disallow addressed to its token affects all surfaces of Google Shopping, such as the Shopping tab in Google Search and Google Shopping. Googlebot is a separate token with its own affected products.

## What Storebot-Google is

Storebot-Google is the Google crawler documented as Google StoreBot among its common crawlers. Google says rules addressed to it affect all surfaces of Google Shopping. Google lists separate desktop and mobile user agent strings for it.

| Fact | Storebot-Google |
| --- | --- |
| Operator | Google |
| Job | Search (Google Shopping surfaces) |
| robots.txt token | `Storebot-Google` |
| Follows robots.txt | Yes. Google says common crawlers always obey robots.txt rules when crawling automatically. |
| IP addresses | 317 ranges (developers.google.com/static/crawling/ipranges/common-crawlers.json, file dated 2026-10-23) |
| Vendor page read | 24 October 2026 |

## What the vendor says

In the vendor's words (English original): “Crawling preferences addressed to the Storebot-Google user agent affect all surfaces of Google Shopping”

Source: [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers), read on 24 October 2026.

## What happens if you block Storebot-Google

Google says a Disallow addressed to the Storebot-Google token affects all surfaces of Google Shopping, such as the Shopping tab in Google Search and Google Shopping. The page lists Googlebot as a separate token with its own affected products.

## The robots.txt lines

To allow Storebot-Google:

```
User-agent: Storebot-Google
Allow: /
```

To block Storebot-Google:

```
User-agent: Storebot-Google
Disallow: /
```

Paste a block into the robots.txt at the root of your host, for example https://example.com/robots.txt. A group for one token does not cover the operator's other crawlers.

The user-agent string the vendor shows:

```
Mozilla/5.0 (X11; Linux x86_64; Storebot-Google/1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z Safari/537.36
```

## How to tell a real request from a fake one

The file at developers.google.com/static/crawling/ipranges/common-crawlers.json held 317 ranges on 24 October 2026, file dated 2026-10-23.

Google says the common crawlers generally crawl from the ranges in common-crawlers.json, and that the reverse DNS name matches crawl-***-***-***-***.googlebot.com or geo-crawl-***-***-***-***.geo.googlebot.com.

## Compare with Googlebot

[Googlebot](/bots/googlebot): Googlebot's rules affect Google Search and related products, while Storebot-Google's rules affect Google Shopping surfaces.

## Your own site

The free check in the box above tests eight crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot). Storebot-Google is not one of them: read your robots.txt for a `Storebot-Google` group and look for the user agent in your server log. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does Storebot-Google follow robots.txt?

Yes. Google says common crawlers always obey robots.txt rules when crawling automatically. Give Storebot-Google its own User-agent group in robots.txt: the operator's other crawlers have their own settings.

### How do I know Storebot-Google is really blocked?

robots.txt is only one layer: a CDN or firewall rule can also turn a crawler away, and a crawler can ignore the file. Check your server log for the user agent, and test the address from outside your network.

## Sources

- [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers)
- [Google: common-crawlers.json (read 2026-10-24, creationTime 2026-10-23)](https://developers.google.com/static/crawling/ipranges/common-crawlers.json)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
