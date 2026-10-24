title: ImagesiftBot: what it does and what blocking it changes
h1: ImagesiftBot: what it does and what blocking it changes
description: ImagesiftBot (Hive (ImageSift)): search. Robots.txt token, what a Disallow changes and how to verify a request, read from the operator's own page.
slug: imagesiftbot
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about ImagesiftBot: operator Hive (ImageSift), job Search, obeys robots.txt Yes, address list None
hero_sub: ImagesiftBot, run by Hive (ImageSift)
hero_boxes: Operator|Hive (ImageSift); Job|Search; Obeys robots.txt|Yes; Address list|None
widget: on
related: /bots|All AI crawlers compared; /bots/googlebot|Googlebot; /platforms|AI crawler settings by platform; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website? What decides it
answer: ImagesiftBot is the crawler of ImageSift, a Hive product. It collects publicly available images with the host URL, page text and image alt text for an index used to search for similar images. The vendor says it respects robots.txt and Crawl-delay, and follows the Googlebot rules when none target it.

## What ImagesiftBot is

ImageSiftBot is the crawler of ImageSift, a Hive product. It collects publicly available images, along with the host URL, page text and image alt text. ImageSift stores the data in an index that its products use for search and retrieval of similar images.

| Fact | ImagesiftBot |
| --- | --- |
| Operator | Hive (ImageSift) |
| Job | Image index for similar-image search |
| robots.txt token | `ImagesiftBot` |
| Follows robots.txt | Yes, and it supports Crawl-delay |
| IP addresses | None published |
| Vendor page read | 24 October 2026 |

## What the vendor says

In the vendor's words (English original): “ImageSiftBot is a web crawler that scrapes the internet for publicly available images to support our suite of web intelligence products”

Source: [Imagesift by Hive: ImageSift Bot](https://imagesift.com/about), read on 24 October 2026.

## What happens if you block ImagesiftBot

The vendor says standard robots.txt directives that target ImagesiftBot are respected, and that it supports Crawl-delay. If no rule targets ImagesiftBot but a rule targets Googlebot, it follows the Googlebot rules. The page also gives support@imagesift.com for opt-out requests.

## The robots.txt lines

To allow ImagesiftBot:

```
User-agent: ImagesiftBot
Allow: /
```

To block ImagesiftBot:

```
User-agent: ImagesiftBot
Disallow: /
```

Paste a block into the robots.txt at the root of your host, for example https://example.com/robots.txt. A group for one token does not cover the operator's other crawlers.

The user-agent string the vendor shows:

```
Mozilla/5.0 (compatible; ImagesiftBot; +imagesift.com)
```

## How to tell a real request from a fake one

The vendor page does not publish an IP list or a verification method.

## Compare with Googlebot

[Googlebot](/bots/googlebot): ImagesiftBot falls back to Googlebot's robots.txt rules when it has none of its own, and it collects images for a similar-image index rather than for a general web search.

## Your own site

The free check in the box above tests eight crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot). ImagesiftBot is not one of them: read your robots.txt for a `ImagesiftBot` group and look for the user agent in your server log. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does ImagesiftBot follow robots.txt?

Yes, and it supports Crawl-delay. Give ImagesiftBot its own User-agent group in robots.txt: the operator's other crawlers have their own settings.

### How do I know ImagesiftBot is really blocked?

robots.txt is only one layer: a CDN or firewall rule can also turn a crawler away, and a crawler can ignore the file. Check your server log for the user agent, and test the address from outside your network.

## Sources

- [Imagesift by Hive: ImageSift Bot](https://imagesift.com/about)
