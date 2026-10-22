title: Meta-ExternalAgent: Meta's AI crawler and its four siblings
slug: meta-externalagent
description: Meta-ExternalAgent crawls for training foundation AI models or indexing. Meta's page, updated 21 May 2026, lists five agents and says two may bypass robots.txt.
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Four facts about Meta-ExternalAgent: operator Meta, job AI model training and content indexing, obeys robots.txt Yes
hero_sub: Meta-ExternalAgent, run by Meta
hero_boxes: Operator|Meta; Job|AI model training; Obeys robots.txt|Yes; Address list|None read
widget: on
related: /bots|All AI crawlers compared; /bots/gptbot|GPTBot; /platforms|AI crawler settings by platform; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website?
answer: Meta-ExternalAgent is Meta's crawler for use cases such as training foundation AI models or improving products by indexing content directly. Meta's page, updated 21 May 2026, lists five agents. It says Meta-ExternalFetcher and FacebookExternalHit may bypass robots.txt, and that changes can take up to 24 hours.

## What Meta-ExternalAgent is

Meta's page lists five crawlers. FacebookExternalHit fetches a page when someone shares a link on Facebook, Instagram or Messenger, to cache its title, description and thumbnail. Meta-WebIndexer improves Meta AI search results, and Meta says allowing it helps Meta cite and link to your content in Meta AI's responses. Meta-ExternalAds crawls for advertising and business products. Meta-ExternalAgent is the one for training foundation AI models or indexing. Meta-ExternalFetcher fetches individual links at a user's request, including helping AI navigate websites to complete tasks for users.

| Fact | Meta-ExternalAgent |
| --- | --- |
| Operator | Meta |
| Job | AI model training and content indexing |
| robots.txt token | `meta-externalagent` |
| Follows robots.txt | Yes |
| Published address list | None read |
| Vendor page read | 21 October 2026 |

## What the vendor says

In the vendor's words: “The Meta-ExternalAgent crawler crawls the web for use cases such as training foundation AI models or improving products by indexing content directly.”

Source: [Meta for Developers: Meta Web Crawlers](https://developers.facebook.com/docs/sharing/webmasters/web-crawlers/), read on 21 October 2026.

## What happens if you block it

Disallowing meta-externalagent affects that agent only: Meta's own examples give a separate group for each token, and the other four have their own. The costly one to block by mistake is FacebookExternalHit, because it builds the link preview when someone shares your page. Two of the five may ignore your robots.txt: Meta says Meta-ExternalFetcher may bypass robots.txt because it performs fetches requested by the user, and FacebookExternalHit may bypass it for security or integrity checks such as malware checks.

## The robots.txt lines

To allow it:

```
User-agent: meta-webindexer
Allow: /

User-agent: meta-externalagent
Allow: /
```

To block it:

```
User-agent: meta-externalagent
Disallow: /
```

The user-agent string the vendor shows:

```
meta-externalagent/1.1
```

## How to tell a real request from a fake one

Meta's page gives the user-agent strings (meta-externalagent/1.1 and the version with a link) and does not publish an IP list in the text we read, so we state no count. For FacebookExternalHit Meta says to allow-list either the user-agent strings or the IP addresses, and calls the addresses the more secure option. Meta says crawlers may cache robots.txt for up to 24 hours, so allow that long before judging a change. Questions go to webmasters@meta.com.

## Compare with GPTBot

[GPTBot](/bots/gptbot): OpenAI's training crawler, which honours robots.txt without Meta's bypass cases.

## Check your own site

The audit box above reads robots.txt for the crawlers in this set and sends one live request per crawler, so a rule that robots.txt allows but a firewall refuses shows up. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Which Meta crawler trains AI models?

Meta describes Meta-ExternalAgent as crawling for use cases such as training foundation AI models or improving products by indexing content directly.

### Does Meta-ExternalFetcher obey robots.txt?

Meta says it may bypass robots.txt rules because it fetches links at a user's request.

### How long does a robots.txt change take?

Meta says to allow up to 24 hours, because crawlers may cache the file for up to 24 hours.

## Sources

- [Meta for Developers: Meta Web Crawlers](https://developers.facebook.com/docs/sharing/webmasters/web-crawlers/), read 21 October 2026
