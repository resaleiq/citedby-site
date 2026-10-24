title: Google-GeminiNotebook: what it does and what blocking it changes
h1: Google-GeminiNotebook: what it does and what blocking it changes
description: Google-GeminiNotebook (Google): user-triggered fetch. Robots.txt token, what a Disallow changes and how to verify a request.
slug: google-gemininotebook
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about Google-GeminiNotebook: operator Google, job User-triggered fetch, obeys robots.txt Not always, address list Reverse DNS
hero_sub: Google-GeminiNotebook, run by Google
hero_boxes: Operator|Google; Job|User-triggered fetch; Obeys robots.txt|Not always; Address list|Reverse DNS
widget: on
related: /bots|All AI crawlers compared; /bots/chatgpt-user|ChatGPT-User; /platforms|AI crawler settings by platform; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website? What decides it
answer: Google-GeminiNotebook is the user agent of the Gemini Notebook fetcher. It requests individual URLs that users have added as sources for their projects. Google lists it among user-triggered fetchers, which generally ignore robots.txt because a user requested the fetch. Google's page names Google-NotebookLM as the former agent.

## What Google-GeminiNotebook is

Google-GeminiNotebook is the user agent of the Gemini Notebook fetcher, which Google lists among its user-triggered fetchers. It requests individual URLs that users have provided as sources for their projects. Google's page lists Google-NotebookLM as the former agent, supported until August 2026.

| Fact | Google-GeminiNotebook |
| --- | --- |
| Operator | Google |
| Job | User-triggered fetch |
| robots.txt token | `Google-GeminiNotebook` |
| Follows robots.txt | Partial. Google says user-triggered fetchers generally ignore robots.txt rules because a user requested the fetch. |
| IP addresses | Reverse DNS check |
| Vendor page read | 24 October 2026 |

## What the vendor says

In the vendor's words (English original): “The Gemini Notebook fetcher requests individual URLs that Gemini Notebook users have provided as sources for their projects.”

Source: [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers), read on 24 October 2026.

## What happens if you block Google-GeminiNotebook

Google says that because the fetch was requested by a user, user-triggered fetchers generally ignore robots.txt rules. The Google page documents no robots.txt token for this fetcher.

## The robots.txt lines

To allow Google-GeminiNotebook:

```
User-agent: Google-GeminiNotebook
Allow: /
```

To block Google-GeminiNotebook:

```
User-agent: Google-GeminiNotebook
Disallow: /
```

Paste a block into the robots.txt at the root of your host, for example https://example.com/robots.txt. A group for one token does not cover the operator's other crawlers.

The user-agent string the vendor shows:

```
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 (compatible; Google-GeminiNotebook; +https://developers.google.com/crawling/docs/crawlers-fetchers/google-gemininotebook)
```

## How to tell a real request from a fake one

Google says user-triggered fetchers publish IP ranges in user-triggered-fetchers.json, user-triggered-fetchers-google.json and user-triggered-agents.json, and that the reverse DNS mask matches ***-***-***-***.gae.googleusercontent.com or google-proxy-***-***-***-***.google.com depending on whether the fetcher is Google or user owned.

## Compare with ChatGPT-User

[ChatGPT-User](/bots/chatgpt-user): Both fetch individual URLs because a user asked an assistant product to use them, and both vendors say these fetches may not follow robots.txt rules.

## Your own site

The free check in the box above tests eight crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot). Google-GeminiNotebook is not one of them: read your robots.txt for a `Google-GeminiNotebook` group and look for the user agent in your server log. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does Google-GeminiNotebook follow robots.txt?

Not always. Google says user-triggered fetchers generally ignore robots.txt rules because a user requested the fetch. A rule for Google-GeminiNotebook in robots.txt may therefore not stop it. To refuse it for certain, use a firewall or CDN rule that matches both the user agent and the published addresses.

### How do I know Google-GeminiNotebook is really blocked?

robots.txt is only one layer: a CDN or firewall rule can also turn a crawler away, and a crawler can ignore the file. Check your server log for the user agent, and test the address from outside your network.

## Sources

- [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
