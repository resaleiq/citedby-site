title: Googlebot: what it covers, its IP ranges and what a block removes
h1: Googlebot: what it covers, its IP ranges and what a block removes
description: Googlebot's robots.txt token controls Google Search and the products built on it. Its user-agent, the 317 IP ranges Google publishes and how to verify one.
slug: googlebot
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Four facts about Googlebot: operator Google, job Search (also Images, Video, News, Discover), robots.txt behaviour, published address lists
hero_sub: Googlebot, run by Google
hero_boxes: Operator|Google; Job|Search; Obeys robots.txt|Yes; Address list|317 ranges
widget: on
related: /bots|All AI crawlers compared; /bots/google-extended|Google-Extended; /blog/is-gptbot-blocked|Is GPTBot blocked on your site?; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website?
answer: Googlebot is Google's main crawler for Search. Google says its common crawlers always obey robots.txt rules when crawling automatically. Crawling preferences for the Googlebot token affect Google Search, including Discover, and products such as Images, Video and News. Google publishes 317 IP ranges for it.

## What Googlebot is

Googlebot is the crawler every Search check starts from. Google's page lists several crawlers, and the single token Googlebot governs Search, Discover and the products that draw on the same crawl, such as Images, Video mode and News.

| Fact | Googlebot |
| --- | --- |
| Operator | Google |
| Job | Search (also Images, Video, News, Discover) |
| robots.txt token | `Googlebot` |
| Follows robots.txt | Yes, always when crawling automatically |
| Published address list | 317 ranges (developers.google.com/static/search/apis/ipranges/googlebot.json, file dated 2026-10-20) |
| Vendor page read | 21 October 2026 |

## What the vendor says

In the vendor's words: “Google's common crawlers are used to find information for building Google's search indexes, perform other product specific crawls, and for analysis. They always obey robots.txt rules when crawling automatically.”

Source: [Google Search Central: Google's common crawlers (last updated 2026-10-15)](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers), read on 21 October 2026.

## What happens if you block it

A Disallow for Googlebot is not a narrow AI opt-out; it affects Google Search itself, including Discover and the features built on it, per Google's list of affected products. The narrower control for Gemini training is the separate token [Google-Extended](/bots/google-extended).

## The robots.txt lines

To allow it:

```
User-agent: Googlebot
Allow: /
```

To block it:

```
User-agent: Googlebot
Disallow: /   # affects Google Search, not only AI features
```

The user-agent string the vendor shows:

```
Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)
```

## How to tell a real request from a fake one

Google publishes the ranges its common crawlers use. The Googlebot file held 317 prefixes on 21 October 2026, creation time 2026-10-20 14:46 UTC. Google also documents a reverse DNS mask for confirming a hostname, so a request is checked two ways: the address against the file, and the reverse lookup against the mask. The page itself was last updated 2026-10-15.

## Compare with Google-Extended

[Google-Extended](/bots/google-extended): A control token for Gemini training; it never fetches a page.

## Check your own site

The free check in the box above reads robots.txt for the crawlers in this set and sends one live request per crawler, so a rule that robots.txt allows but a firewall refuses shows up. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does Googlebot obey robots.txt?

Google says its common crawlers always obey robots.txt rules when crawling automatically.

### Will blocking Googlebot stop Gemini training?

Googlebot controls Search. The Gemini training control is the separate Google-Extended token, and blocking Googlebot would also take you out of Google Search.

## Sources

- [Google Search Central: Google's common crawlers (last updated 2026-10-15)](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers)
- [developers.google.com/static/search/apis/ipranges/googlebot.json](https://developers.google.com/static/crawling/ipranges/common-crawlers.json), read 21 October 2026
