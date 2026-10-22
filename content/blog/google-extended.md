title: Google-Extended: the robots.txt token for Gemini, not a crawler
h1: Google-Extended: the robots.txt token for Gemini, not a crawler
description: Google-Extended is a control token, not a crawler: no user agent, never in server logs. What it controls, what it leaves alone and why IP lists cannot verify it
slug: google-extended
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Four facts about Google-Extended: operator Google, job Control token (no requests of its own), robots.txt behaviour, published address lists
hero_sub: Google-Extended, run by Google
hero_boxes: Operator|Google; Job|Control token; Obeys robots.txt|Read from robots.txt only; there is no separate user agent; Address list|None
widget: on
related: /bots|All AI crawlers compared; /bots/googlebot|Googlebot; /blog/is-gptbot-blocked|Is GPTBot blocked on your site?; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website?
answer: Google-Extended is a robots.txt product token that lets publishers manage whether content Google crawls may be used to train future Gemini models. It has no HTTP user agent of its own, so it never shows in your logs. Google says it does not affect inclusion in Search or ranking.

## What Google-Extended is

Most pages in this set describe a crawler you can find in a log. This one you cannot. Google states that Google-Extended "doesn't have a separate HTTP request user agent string": crawling happens with existing Google user agents, and the robots.txt token is used in a control capacity.

| Fact | Google-Extended |
| --- | --- |
| Operator | Google |
| Job | Control token (no requests of its own) |
| robots.txt token | `Google-Extended` |
| Follows robots.txt | Read from robots.txt only; there is no separate user agent |
| Published address list | None: it never fetches |
| Vendor page read | 21 October 2026 |

## What the vendor says

In the vendor's words: “Google-Extended is a standalone product token that web publishers can use to manage whether content Google crawls from their sites may be used for training future generations of Gemini models that power Gemini Apps and Vertex AI API for Gemini. Google-Extended does not impact a site's inclusion in Google Search nor is it used as a ranking signal in Google Search.”

Source: [Google Search Central: Google's common crawlers (last updated 2026-10-15)](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers), read on 21 October 2026.

## What happens if you block it

Adding `Disallow: /` under Google-Extended tells Google it may not use the content for training future Gemini models behind Gemini Apps and the Vertex AI API for Gemini. Google also says it does not impact inclusion in Google Search and is not a ranking signal. Our audit reads this token in robots.txt as one of its checks; it is the only signal there is.

## The robots.txt lines

To allow it:

```
User-agent: Google-Extended
Allow: /
```

To block it:

```
User-agent: Google-Extended
Disallow: /
```

## How to tell a real request from a fake one

There is nothing to verify at the network layer: no user agent, no address list. Check the robots.txt itself, on every host, and remember that a log search for Google-Extended finds nothing whether you block it or not. Google's own example group shows the token taking an allow path and a disallow path like any other.

## Compare with Googlebot

[Googlebot](/bots/googlebot): The crawler that actually fetches your pages for Search.

## Check your own site

The free check in the box above reads robots.txt for the crawlers in this set and sends one live request per crawler, so a rule that robots.txt allows but a firewall refuses shows up. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Why does Google-Extended never appear in my logs?

Google says it has no separate HTTP request user agent string. It is a robots.txt token only, and the crawling is done by existing Google user agents.

### Does blocking Google-Extended hurt my Google rankings?

Google says it does not impact a site's inclusion in Google Search and is not used as a ranking signal.

## Sources

- [Google Search Central: Google's common crawlers (last updated 2026-10-15)](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers)
