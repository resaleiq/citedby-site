title: Baiduspider: what it does and what blocking it changes
h1: Baiduspider: what it does and what blocking it changes
description: Baiduspider (Baidu): search. Robots.txt token, what a Disallow changes and how to verify a request, read from the operator's own page.
slug: baiduspider
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about Baiduspider: operator Baidu, job Search, obeys robots.txt Yes, address list Reverse DNS
hero_sub: Baiduspider, run by Baidu
hero_boxes: Operator|Baidu; Job|Search; Obeys robots.txt|Yes; Address list|Reverse DNS
widget: on
related: /bots|All AI crawlers compared; /bots/bingbot|Bingbot; /platforms|AI crawler settings by platform; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website? What decides it
answer: Baiduspider is the crawler of the Baidu search engine. Baidu says it follows the robots.txt protocol and that blocking Baiduspider blocks all Baidu user agents, so pages will not be found in Baidu results. Baiduspider-cpro and Baiduspider-ads work on customer agreements and do not follow robots.txt records.

## What Baiduspider is

Baiduspider is the crawler of the Baidu search engine; it visits pages and builds them into the Baidu index. Baidu uses different user agents for different products, for example Baiduspider for PC and mobile search and Baiduspider-image, Baiduspider-video and Baiduspider-news for those searches.

| Fact | Baiduspider |
| --- | --- |
| Operator | Baidu |
| Job | Search |
| robots.txt token | `Baiduspider` |
| Follows robots.txt | Yes for Baiduspider; Baiduspider-cpro and Baiduspider-ads do not follow robots.txt records |
| IP addresses | Reverse DNS check |
| Vendor page read | 24 October 2026 |

## What the vendor says

In the vendor's words (English original): “Baiduspider is Baidu search engine program which is used to visit pages on the internet and build information into Baidu index.”

Source: [Baidu Help Center: FAQs of Baiduspider](https://help.baidu.com/question?prod_id=99&class=0&id=3001), read on 24 October 2026.

## What happens if you block Baiduspider

Baidu says Baiduspider works on the robots.txt protocol, and that blocking it means your pages will not be found in Baidu search results or in any other results provided by Baidu. You can set different rules for different Baidu user agents, and blocking Baiduspider blocks all Baidu user agents. Baiduspider-cpro and Baiduspider-ads work on agreements with customers and do not follow robots.txt records.

## The robots.txt lines

To allow Baiduspider:

```
User-agent: Baiduspider
Allow: /
```

To block Baiduspider:

```
User-agent: Baiduspider
Disallow: /
```

Paste a block into the robots.txt at the root of your host, for example https://example.com/robots.txt. A group for one token does not cover the operator's other crawlers.

The user-agent string the vendor shows:

```
Baiduspider
```

## How to tell a real request from a fake one

Baidu recommends a reverse DNS lookup on the visiting IP; the host name of Baiduspider is *.baidu.com or *.baidu.jp, and other host names are fake.

## Compare with Bingbot

[Bingbot](/bots/bingbot): Both crawl for a search engine; Baidu documents several product-specific user agents (image, video, news, ads) under the Baiduspider name and verifies by reverse DNS host name.

## Your own site

The free check in the box above tests eight crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot). Baiduspider is not one of them: read your robots.txt for a `Baiduspider` group and look for the user agent in your server log. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does Baiduspider follow robots.txt?

Yes for Baiduspider; Baiduspider-cpro and Baiduspider-ads do not follow robots.txt records. Give Baiduspider its own User-agent group in robots.txt: the operator's other crawlers have their own settings.

### How do I know Baiduspider is really blocked?

robots.txt is only one layer: a CDN or firewall rule can also turn a crawler away, and a crawler can ignore the file. Check your server log for the user agent, and test the address from outside your network.

## Sources

- [Baidu Help Center: FAQs of Baiduspider](https://help.baidu.com/question?prod_id=99&class=0&id=3001)
- [Baidu Help Center: How to block the crawling (robots.txt)](https://www.baidu.com/search/robots_english.html)
