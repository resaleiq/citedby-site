title: Google-Pinpoint: what it does and what blocking it changes
h1: Google-Pinpoint: what it does and what blocking it changes
description: Google-Pinpoint (Google): user-triggered fetch. Robots.txt token, what a Disallow changes and how to verify a request, read from the operator's own page.
slug: google-pinpoint
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about Google-Pinpoint: operator Google, job User-triggered fetch, obeys robots.txt Not always, address list Reverse DNS
hero_sub: Google-Pinpoint, run by Google
hero_boxes: Operator|Google; Job|User-triggered fetch; Obeys robots.txt|Not always; Address list|Reverse DNS
widget: on
related: /bots|All AI crawlers compared; /bots/google-gemininotebook|Google-GeminiNotebook; /platforms|AI crawler settings by platform; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website? What decides it
answer: Google-Pinpoint is a user-triggered fetcher listed by Google. It requests individual URLs that Pinpoint users specified as sources for their personal collections of documents. Google says user-triggered fetchers generally ignore robots.txt rules because a user requested the fetch, and documents no robots.txt token for it.

## What Google-Pinpoint is

Google-Pinpoint is a user-triggered fetcher listed by Google. It requests individual URLs that Pinpoint users specified as sources for their personal collections of documents. Google lists it with the user agent Google-Pinpoint.

| Fact | Google-Pinpoint |
| --- | --- |
| Operator | Google |
| Job | User-triggered fetch |
| robots.txt token | `Google-Pinpoint` |
| Follows robots.txt | Partial. Google says user-triggered fetchers generally ignore robots.txt rules because a user requested the fetch. |
| IP addresses | Reverse DNS check |
| Vendor page read | 24 October 2026 |

## What the vendor says

In the vendor's words (English original): “The Google-Pinpoint fetcher requests individual URLs that Pinpoint users specified as sources for their personal collections of documents.”

Source: [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers), read on 24 October 2026.

## What happens if you block Google-Pinpoint

Google says that because the fetch was requested by a user, user-triggered fetchers generally ignore robots.txt rules. The Google page documents no robots.txt token for Google-Pinpoint.

## The robots.txt lines

To allow Google-Pinpoint:

```
User-agent: Google-Pinpoint
Allow: /
```

To block Google-Pinpoint:

```
User-agent: Google-Pinpoint
Disallow: /
```

Paste a block into the robots.txt at the root of your host, for example https://example.com/robots.txt. A group for one token does not cover the operator's other crawlers.

The user-agent string the vendor shows:

```
Google-Pinpoint
```

## How to tell a real request from a fake one

Google says user-triggered fetchers publish IP ranges in user-triggered-fetchers.json, user-triggered-fetchers-google.json and user-triggered-agents.json, and that the reverse DNS mask matches ***-***-***-***.gae.googleusercontent.com or google-proxy-***-***-***-***.google.com depending on whether the fetcher is Google or user owned.

## Compare with Google-GeminiNotebook

[Google-GeminiNotebook](/bots/google-gemininotebook): Both fetch URLs that users supplied as sources in a Google product, and both fall under Google's user-triggered fetcher rules.

## Your own site

The free check in the box above tests eight crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot). Google-Pinpoint is not one of them: read your robots.txt for a `Google-Pinpoint` group and look for the user agent in your server log. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does Google-Pinpoint follow robots.txt?

Not always. Google says user-triggered fetchers generally ignore robots.txt rules because a user requested the fetch. A rule for Google-Pinpoint in robots.txt may therefore not stop it. To refuse it for certain, use a firewall or CDN rule that matches both the user agent and the published addresses.

### How do I know Google-Pinpoint is really blocked?

robots.txt is only one layer: a CDN or firewall rule can also turn a crawler away, and a crawler can ignore the file. Check your server log for the user agent, and test the address from outside your network.

## Sources

- [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
