title: ExaUser: what it does and what blocking it changes
h1: ExaUser: what it does and what blocking it changes
description: ExaUser (Exa): user-triggered fetch. Robots.txt token, what a Disallow changes and how to verify a request, read from the operator's own page.
slug: exauser
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about ExaUser: operator Exa, job User-triggered fetch, obeys robots.txt Not always, address list Verify tool
hero_sub: ExaUser, run by Exa
hero_boxes: Operator|Exa; Job|User-triggered fetch; Obeys robots.txt|Not always; Address list|Verify tool
widget: on
related: /bots|All AI crawlers compared; /bots/exasearchbot|ExaSearchBot; /platforms|AI crawler settings by platform; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website? What decides it
answer: ExaUser is the agent Exa uses to fetch a page live when a user, or an application built on the Exa API, asks for its current content. Exa says robots.txt rules may not apply to such user-initiated fetches. Search opt-outs and automatic crawling are controlled with the ExaSearchBot token instead.

## What ExaUser is

ExaUser is the agent Exa uses to fetch a page live when a user, or an application built on the Exa API, asks for its current content. Exa says it is not used to crawl the web automatically; that is ExaSearchBot. It does not try to bypass logins, paywalls or CAPTCHAs, and submits no forms.

| Fact | ExaUser |
| --- | --- |
| Operator | Exa |
| Job | User-triggered fetch |
| robots.txt token | `ExaUser` |
| Follows robots.txt | Partial, vendor says robots.txt rules may not apply to user-initiated fetches |
| IP addresses | Verify tool |
| Vendor page read | 24 October 2026 |

## What the vendor says

In the vendor's words (English original): “Exa uses ExaUser to fetch a page live when a user, or an application built on the Exa API, asks for its current content.”

Source: [Exa: ExaUser](https://crawler.exa.ai/exauser), read on 24 October 2026.

## What happens if you block ExaUser

Exa says that because fetches are initiated by a user, robots.txt rules may not apply to ExaUser. It also says ExaUser is not used to decide whether content appears in Exa search, and that search opt-outs and automatic crawling are managed with the ExaSearchBot token in robots.txt.

## The robots.txt lines

To allow ExaUser:

```
User-agent: ExaUser
Allow: /
```

To block ExaUser:

```
User-agent: ExaUser
Disallow: /
```

Paste a block into the robots.txt at the root of your host, for example https://example.com/robots.txt. A group for one token does not cover the operator's other crawlers.

The user-agent string the vendor shows:

```
Mozilla/5.0 (compatible; ExaUser/1.0; +https://crawler.exa.ai/exauser)
```

## How to tell a real request from a fake one

The vendor says every request is signed with Web Bot Auth (RFC 9421) and publishes its keys at a public directory; it does not publish an IP list.

## Compare with ExaSearchBot

[ExaSearchBot](/bots/exasearchbot): ExaSearchBot crawls automatically to build Exa's search index and follows robots.txt, while ExaUser fetches a page only when a user or application asks and the vendor says robots.txt may not apply.

## Your own site

The free check in the box above tests eight crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot). ExaUser is not one of them: read your robots.txt for a `ExaUser` group and look for the user agent in your server log. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does ExaUser follow robots.txt?

Not always: vendor says robots.txt rules may not apply to user-initiated fetches. A rule for ExaUser in robots.txt may therefore not stop it. To refuse it for certain, use a firewall or CDN rule that matches both the user agent and the published addresses.

### How do I know ExaUser is really blocked?

robots.txt is only one layer: a CDN or firewall rule can also turn a crawler away, and a crawler can ignore the file. Check your server log for the user agent, and test the address from outside your network.

## Sources

- [Exa: ExaUser](https://crawler.exa.ai/exauser)
- [Exa: Exa Search Crawler](https://crawler.exa.ai/)
