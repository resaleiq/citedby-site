title: Google-Agent: what it does and what blocking it changes
h1: Google-Agent: what it does and what blocking it changes
description: Google-Agent (Google): user-triggered fetch. Robots.txt token, what a Disallow changes and how to verify a request, read from the operator's own page.
slug: google-agent
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about Google-Agent: operator Google, job User-triggered fetch, obeys robots.txt Not always, address list 20 ranges
hero_sub: Google-Agent, run by Google
hero_boxes: Operator|Google; Job|User-triggered fetch; Obeys robots.txt|Not always; Address list|20 ranges
widget: on
related: /bots|All AI crawlers compared; /bots/chatgpt-user|ChatGPT-User; /platforms|AI crawler settings by platform; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website? What decides it
answer: Google-Agent is a user-triggered fetcher that Google says is used by agents hosted on Google infrastructure to navigate the web and act on a user's request. Google says user-triggered fetchers generally ignore robots.txt because a user requested the fetch. Google publishes its IP ranges in user-triggered-agents.json.

## What Google-Agent is

Google-Agent is a user-triggered fetcher that Google says is used by agents hosted on Google infrastructure to navigate the web and perform actions upon user request. Google lists separate mobile and desktop user agent strings. Google also says it is experimenting with the Web Bot Auth protocol using the https://agent.bot.goog identity.

| Fact | Google-Agent |
| --- | --- |
| Operator | Google |
| Job | User-triggered fetch (agents acting for a user) |
| robots.txt token | `Google-Agent` |
| Follows robots.txt | Partial. Google says user-triggered fetchers generally ignore robots.txt rules because a user requested the fetch. |
| IP addresses | 20 ranges (developers.google.com/static/crawling/ipranges/user-triggered-agents.json, file dated 2026-10-23) |
| Vendor page read | 24 October 2026 |

## What the vendor says

In the vendor's words (English original): “Google-Agent is used by agents hosted on Google infrastructure to navigate the web and perform actions upon user request.”

Source: [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers), read on 24 October 2026.

## What happens if you block Google-Agent

Google says that because the fetch was requested by a user, user-triggered fetchers generally ignore robots.txt rules. The Google page documents no robots.txt token for Google-Agent.

## The robots.txt lines

To allow Google-Agent:

```
User-agent: Google-Agent
Allow: /
```

To block Google-Agent:

```
User-agent: Google-Agent
Disallow: /
```

Paste a block into the robots.txt at the root of your host, for example https://example.com/robots.txt. A group for one token does not cover the operator's other crawlers.

The user-agent string the vendor shows:

```
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko; compatible; Google-Agent; +https://developers.google.com/crawling/docs/crawlers-fetchers/google-agent) Chrome/W.X.Y.Z Safari/537.36
```

## How to tell a real request from a fake one

The file at developers.google.com/static/crawling/ipranges/user-triggered-agents.json held 20 ranges on 24 October 2026, file dated 2026-10-23.

Google says Google-Agent uses IP ranges from user-triggered-agents.json, and that user-triggered fetchers' reverse DNS mask matches ***-***-***-***.gae.googleusercontent.com or google-proxy-***-***-***-***.google.com depending on whether the fetcher is Google or user owned.

## Compare with ChatGPT-User

[ChatGPT-User](/bots/chatgpt-user): Both act on a user's request rather than crawling on their own, and Google-Agent is described as navigating the web and performing actions for the user.

## Your own site

The free check in the box above tests eight crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot). Google-Agent is not one of them: read your robots.txt for a `Google-Agent` group and look for the user agent in your server log. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does Google-Agent follow robots.txt?

Not always. Google says user-triggered fetchers generally ignore robots.txt rules because a user requested the fetch. A rule for Google-Agent in robots.txt may therefore not stop it. To refuse it for certain, use a firewall or CDN rule that matches both the user agent and the published addresses.

### How do I know Google-Agent is really blocked?

robots.txt is only one layer: a CDN or firewall rule can also turn a crawler away, and a crawler can ignore the file. Check your server log for the user agent, and test the address from outside your network.

## Sources

- [Google Search Central: Google user-triggered fetchers](https://developers.google.com/search/docs/crawling-indexing/google-user-triggered-fetchers)
- [Google: user-triggered-agents.json (read 2026-10-24, creationTime 2026-10-23)](https://developers.google.com/static/crawling/ipranges/user-triggered-agents.json)
- [Google Search Central: Overview of Google crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers)
