title: GoogleOther: what it does and what blocking it changes
h1: GoogleOther: what it does and what blocking it changes
description: GoogleOther (Google): several jobs. Robots.txt token, what a Disallow changes and how to verify a request, read from the operator's own page.
slug: googleother
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about GoogleOther: operator Google, job Several jobs, obeys robots.txt Yes, address list 317 ranges
hero_sub: GoogleOther, run by Google
hero_boxes: Operator|Google; Job|Several jobs; Obeys robots.txt|Yes; Address list|317 ranges
widget: on
related: /bots|All AI crawlers compared; /bots/googlebot|Googlebot; /platforms|AI crawler settings by platform; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website? What decides it
answer: GoogleOther is Google's generic crawler. Various Google product teams use it to fetch publicly accessible content, for example in one-off crawls for internal research and development. Google says rules addressed to GoogleOther do not affect any specific product. GoogleOther-Image and GoogleOther-Video are documented as separate tokens.

## What GoogleOther is

GoogleOther is Google's generic crawler, used by various Google product teams to fetch publicly accessible content, for example in one-off crawls for internal research and development. Google lists it among its common crawlers, next to Googlebot, and also documents GoogleOther-Image and GoogleOther-Video as versions optimized for image and video URLs. The Google page does not say it is used for AI training.

| Fact | GoogleOther |
| --- | --- |
| Operator | Google |
| Job | Generic crawl for various Google product teams |
| robots.txt token | `GoogleOther` |
| Follows robots.txt | Yes. Google says common crawlers always obey robots.txt rules when crawling automatically. |
| IP addresses | 317 ranges (developers.google.com/static/crawling/ipranges/common-crawlers.json, file dated 2026-10-23) |
| Vendor page read | 24 October 2026 |

## What the vendor says

In the vendor's words (English original): “GoogleOther is the generic crawler that may be used by various product teams for fetching publicly accessible content from sites. For example, it may be used for one-off crawls for internal research and development.”

Source: [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers), read on 24 October 2026.

## What happens if you block GoogleOther

Google says crawling preferences addressed to the GoogleOther user agent do not affect any specific product. Google documents GoogleOther-Image and GoogleOther-Video as separate robots.txt tokens, so a rule for GoogleOther is not stated to cover them, and the Googlebot token is a separate token again.

## The robots.txt lines

To allow GoogleOther:

```
User-agent: GoogleOther
Allow: /
```

To block GoogleOther:

```
User-agent: GoogleOther
Disallow: /
```

Paste a block into the robots.txt at the root of your host, for example https://example.com/robots.txt. A group for one token does not cover the operator's other crawlers.

The user-agent string the vendor shows:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GoogleOther) Chrome/W.X.Y.Z Safari/537.36
```

## How to tell a real request from a fake one

The file at developers.google.com/static/crawling/ipranges/common-crawlers.json held 317 ranges on 24 October 2026, file dated 2026-10-23.

Google says the common crawlers generally crawl from the ranges in common-crawlers.json, and that the reverse DNS name matches crawl-***-***-***-***.googlebot.com or geo-crawl-***-***-***-***.geo.googlebot.com.

## Compare with Googlebot

[Googlebot](/bots/googlebot): Googlebot crawls for Google Search and related products, while GoogleOther is a generic crawler whose robots.txt rules do not affect any specific Google product.

## Your own site

The free check in the box above tests eight crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot). GoogleOther is not one of them: read your robots.txt for a `GoogleOther` group and look for the user agent in your server log. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does GoogleOther follow robots.txt?

Yes. Google says common crawlers always obey robots.txt rules when crawling automatically. Give GoogleOther its own User-agent group in robots.txt: the operator's other crawlers have their own settings.

### How do I know GoogleOther is really blocked?

robots.txt is only one layer: a CDN or firewall rule can also turn a crawler away, and a crawler can ignore the file. Check your server log for the user agent, and test the address from outside your network.

## Sources

- [Google Search Central: Google's common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers)
- [Google: common-crawlers.json (read 2026-10-24, creationTime 2026-10-23)](https://developers.google.com/static/crawling/ipranges/common-crawlers.json)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
