title: Meta-WebIndexer: what it does and what blocking it changes
h1: Meta-WebIndexer: what it does and what blocking it changes
description: Meta-WebIndexer (Meta): search. Robots.txt token, what a Disallow changes and how to verify a request, read from the operator's own page.
slug: meta-webindexer
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about Meta-WebIndexer: operator Meta, job Search, obeys robots.txt Yes, address list None
hero_sub: Meta-WebIndexer, run by Meta
hero_boxes: Operator|Meta; Job|Search; Obeys robots.txt|Yes; Address list|None
widget: on
related: /bots|All AI crawlers compared; /bots/meta-externalagent|Meta-ExternalAgent; /platforms|AI crawler settings by platform; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website? What decides it
answer: Meta-WebIndexer is a Meta crawler that navigates the web to improve Meta AI search result quality. Meta says allowing it in robots.txt helps Meta cite and link to your content in Meta AI's responses. Meta says you block its crawlers with a disallow for the relevant crawler, and a change can take up to 24 hours.

## What Meta-WebIndexer is

Meta-WebIndexer is a Meta crawler that navigates the web to improve Meta AI search result quality for users. Meta says allowing it in robots.txt helps Meta cite and link to your content in Meta AI's responses. Meta documents it alongside Meta-ExternalAgent, Meta-ExternalFetcher, Meta-ExternalAds and FacebookExternalHit on one page.

| Fact | Meta-WebIndexer |
| --- | --- |
| Operator | Meta |
| Job | Search |
| robots.txt token | `Meta-WebIndexer` |
| Follows robots.txt | Yes, changes may take up to 24 hours |
| IP addresses | None published |
| Vendor page read | 24 October 2026 |

## What the vendor says

In the vendor's words (English original): “The Meta-WebIndexer crawler navigates the web to improve Meta AI search result quality for users. In doing so, Meta analyzes online content to enhance the relevance and accuracy of Meta AI.”

Source: [Meta: Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers), read on 24 October 2026.

## What happens if you block Meta-WebIndexer

Meta says you can block its crawlers by adding a disallow for the relevant crawler to robots.txt, and that robots.txt changes can take up to 24 hours to take effect. Meta says allowing Meta-WebIndexer helps it cite and link to your content in Meta AI's responses. Meta's page does not say whether a disallow for Meta-WebIndexer affects its other crawlers.

## The robots.txt lines

To allow Meta-WebIndexer:

```
User-agent: Meta-WebIndexer
Allow: /
```

To block Meta-WebIndexer:

```
User-agent: Meta-WebIndexer
Disallow: /
```

Paste a block into the robots.txt at the root of your host, for example https://example.com/robots.txt. A group for one token does not cover the operator's other crawlers.

The user-agent string the vendor shows:

```
meta-webindexer/1.1
```

## How to tell a real request from a fake one

Meta's crawler page does not list IP addresses or a verification method for this crawler; it identifies the crawler by its user-agent string.

## Compare with Meta-ExternalAgent

[Meta-ExternalAgent](/bots/meta-externalagent): Meta-WebIndexer is for Meta AI search results and citations, while Meta-ExternalAgent is described by Meta as crawling for uses such as training foundation AI models or indexing content directly.

## Your own site

The free check in the box above tests eight crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot). Meta-WebIndexer is not one of them: read your robots.txt for a `Meta-WebIndexer` group and look for the user agent in your server log. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does Meta-WebIndexer follow robots.txt?

Yes, changes may take up to 24 hours. Give Meta-WebIndexer its own User-agent group in robots.txt: the operator's other crawlers have their own settings.

### How do I know Meta-WebIndexer is really blocked?

robots.txt is only one layer: a CDN or firewall rule can also turn a crawler away, and a crawler can ignore the file. Check your server log for the user agent, and test the address from outside your network.

## Sources

- [Meta: Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers)
