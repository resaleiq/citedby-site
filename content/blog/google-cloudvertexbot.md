title: Google-CloudVertexBot: what it does and what blocking it changes
h1: Google-CloudVertexBot: what it does and what blocking it changes
description: Google-CloudVertexBot (Google): several jobs. Robots.txt token, what a Disallow changes and how to verify a request, read from the operator's own page.
slug: google-cloudvertexbot
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about Google-CloudVertexBot: operator Google, job Several jobs, obeys robots.txt Yes, address list 317 ranges
hero_sub: Google-CloudVertexBot, run by Google
hero_boxes: Operator|Google; Job|Several jobs; Obeys robots.txt|Yes; Address list|317 ranges
widget: on
related: /bots|All AI crawlers compared; /bots/googlebot|Googlebot; /platforms|AI crawler settings by platform; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website? What decides it
answer: Google-CloudVertexBot is a Google crawler that performs crawls requested by site owners to build Vertex AI Agents. Google lists it among its common crawlers, which always obey robots.txt when crawling automatically. Google says rules addressed to it have no effect on Google Search or other Google products.

## What Google-CloudVertexBot is

Google-CloudVertexBot is a Google crawler listed among its common crawlers. Google says it performs crawls requested by site owners for building Vertex AI Agents. Google shows it as a user agent substring, not a full user agent string.

| Fact | Google-CloudVertexBot |
| --- | --- |
| Operator | Google |
| Job | Crawl requested by site owners for Vertex AI Agents |
| robots.txt token | `Google-CloudVertexBot` |
| Follows robots.txt | Yes. Google says common crawlers always obey robots.txt rules when crawling automatically. |
| IP addresses | 317 ranges (developers.google.com/static/crawling/ipranges/common-crawlers.json, file dated 2026-10-23) |
| Vendor page read | 24 October 2026 |

## What the vendor says

In the vendor's words (English original): “Crawling preferences addressed to the Google-CloudVertexBot user agent affect crawls requested by the site owners' for building Vertex AI Agents”

Source: [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers), read on 24 October 2026.

## What happens if you block Google-CloudVertexBot

Google says preferences addressed to the Google-CloudVertexBot user agent affect crawls requested by site owners for building Vertex AI Agents. It says this has no effect on Google Search or other products.

## The robots.txt lines

To allow Google-CloudVertexBot:

```
User-agent: Google-CloudVertexBot
Allow: /
```

To block Google-CloudVertexBot:

```
User-agent: Google-CloudVertexBot
Disallow: /
```

Paste a block into the robots.txt at the root of your host, for example https://example.com/robots.txt. A group for one token does not cover the operator's other crawlers.

The user-agent string the vendor shows:

```
Google-CloudVertexBot
```

## How to tell a real request from a fake one

The file at developers.google.com/static/crawling/ipranges/common-crawlers.json held 317 ranges on 24 October 2026, file dated 2026-10-23.

Google says the common crawlers generally crawl from the ranges in common-crawlers.json, and that the reverse DNS name matches crawl-***-***-***-***.googlebot.com or geo-crawl-***-***-***-***.geo.googlebot.com.

## Compare with Googlebot

[Googlebot](/bots/googlebot): Googlebot crawls for Google Search, while Google-CloudVertexBot only crawls when a site owner has requested a crawl for building Vertex AI Agents.

## Your own site

The free check in the box above tests eight crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot). Google-CloudVertexBot is not one of them: read your robots.txt for a `Google-CloudVertexBot` group and look for the user agent in your server log. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does Google-CloudVertexBot follow robots.txt?

Yes. Google says common crawlers always obey robots.txt rules when crawling automatically. Give Google-CloudVertexBot its own User-agent group in robots.txt: the operator's other crawlers have their own settings.

### How do I know Google-CloudVertexBot is really blocked?

robots.txt is only one layer: a CDN or firewall rule can also turn a crawler away, and a crawler can ignore the file. Check your server log for the user agent, and test the address from outside your network.

## Sources

- [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers)
- [Google: common-crawlers.json (read 2026-10-24, creationTime 2026-10-23)](https://developers.google.com/static/crawling/ipranges/common-crawlers.json)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
