title: Meta-ExternalFetcher: what it does and what blocking it changes
h1: Meta-ExternalFetcher: what it does and what blocking it changes
description: Meta-ExternalFetcher (Meta): user-triggered fetch. Robots.txt token, what a Disallow changes and how to verify a request, read from the operator's own page.
slug: meta-externalfetcher
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about Meta-ExternalFetcher: operator Meta, job User-triggered fetch, obeys robots.txt Not always, address list None
hero_sub: Meta-ExternalFetcher, run by Meta
hero_boxes: Operator|Meta; Job|User-triggered fetch; Obeys robots.txt|Not always; Address list|None
widget: on
related: /bots|All AI crawlers compared; /bots/meta-externalagent|Meta-ExternalAgent; /platforms|AI crawler settings by platform; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website? What decides it
answer: Meta-ExternalFetcher is a Meta crawler that fetches individual links at a user's request. Meta says it supports product functions such as helping AI navigate websites to complete tasks for users, and that it may bypass robots.txt because the fetches are requested by a user. Robots.txt changes can take up to 24 hours.

## What Meta-ExternalFetcher is

Meta-ExternalFetcher is a Meta crawler that fetches individual links at a user's request. Meta says it supports product functions such as evaluating and improving agentic AI capabilities, including helping AI navigate websites to complete tasks for users. Meta documents it alongside Meta-ExternalAgent, Meta-WebIndexer, Meta-ExternalAds and FacebookExternalHit on one page.

| Fact | Meta-ExternalFetcher |
| --- | --- |
| Operator | Meta |
| Job | User-triggered fetch |
| robots.txt token | `Meta-ExternalFetcher` |
| Follows robots.txt | Partial, may bypass robots.txt because fetches are requested by a user |
| IP addresses | None published |
| Vendor page read | 24 October 2026 |

## What the vendor says

In the vendor's words (English original): “The Meta-ExternalFetcher crawler fetches individual links at a user's request and supports product functions such as evaluating and improving agentic AI capabilities—including helping AI navigate websites to complete tasks for users. Accordingly, this crawler may bypass robots.txt rules.”

Source: [Meta: Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers), read on 24 October 2026.

## What happens if you block Meta-ExternalFetcher

Meta says you can block its crawlers by adding a disallow for the relevant crawler to robots.txt. Meta also says Meta-ExternalFetcher may bypass robots.txt because it performs fetches that were requested by the user. Meta says changes to robots.txt can take up to 24 hours to take effect because crawlers may cache the file for up to 24 hours.

## The robots.txt lines

To allow Meta-ExternalFetcher:

```
User-agent: Meta-ExternalFetcher
Allow: /
```

To block Meta-ExternalFetcher:

```
User-agent: Meta-ExternalFetcher
Disallow: /
```

Paste a block into the robots.txt at the root of your host, for example https://example.com/robots.txt. A group for one token does not cover the operator's other crawlers.

The user-agent string the vendor shows:

```
meta-externalfetcher/1.1
```

## How to tell a real request from a fake one

Meta's crawler page does not list IP addresses or a verification method for this crawler; it identifies the crawler by its user-agent string.

## Compare with Meta-ExternalAgent

[Meta-ExternalAgent](/bots/meta-externalagent): Meta-ExternalAgent crawls the web in the background, including for training foundation AI models, while Meta-ExternalFetcher fetches single links a user asked for and may bypass robots.txt.

## Your own site

The free check in the box above tests eight crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot). Meta-ExternalFetcher is not one of them: read your robots.txt for a `Meta-ExternalFetcher` group and look for the user agent in your server log. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does Meta-ExternalFetcher follow robots.txt?

Not always. Partial, may bypass robots.txt because fetches are requested by a user. A rule for Meta-ExternalFetcher in robots.txt may therefore not stop it. To refuse it for certain, use a firewall or CDN rule that matches both the user agent and the published addresses.

### How do I know Meta-ExternalFetcher is really blocked?

robots.txt is only one layer: a CDN or firewall rule can also turn a crawler away, and a crawler can ignore the file. Check your server log for the user agent, and test the address from outside your network.

## Sources

- [Meta: Meta Web Crawlers](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers)
