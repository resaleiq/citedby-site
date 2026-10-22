title: Applebot-Extended: opt out of Apple model training, keep search
h1: Applebot-Extended: opting out of Apple's model training without leaving search
description: Applebot-Extended is Apple's opt-out token for generative model training. What it does, why Applebot can still crawl you and what stays in Spotlight and Siri.
slug: applebot-extended
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Four facts about Applebot-Extended: operator Apple, job Control token (no requests of its own), robots.txt behaviour, published address lists
hero_sub: Applebot-Extended, run by Apple
hero_boxes: Operator|Apple; Job|Control token; Obeys robots.txt|Read from robots.txt only; Address list|None
widget: on
related: /bots|All AI crawlers compared; /blog/is-gptbot-blocked|Is GPTBot blocked on your site?; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website?
answer: Applebot-Extended is a robots.txt token. Apple says publishers can opt out of having their content used to train generative foundation models by disallowing it. Applebot may still crawl the page, so the content stays discoverable in Spotlight, Siri and Safari. It makes no requests of its own.

## What Applebot-Extended is

Apple's page describes Applebot-Extended as the way to keep content out of training for foundation models behind Apple Intelligence, services and developer tools. Like [Google-Extended](/bots/google-extended) it is a control token: you will not find it in a log.

| Fact | Applebot-Extended |
| --- | --- |
| Operator | Apple |
| Job | Control token (no requests of its own) |
| robots.txt token | `Applebot-Extended` |
| Follows robots.txt | Read from robots.txt only |
| Published address list | None: it never fetches |
| Vendor page read | 21 October 2026 |

## What the vendor says

In the vendor's words: “Web publishers can opt-out from having their content used to train generative foundation models by disallowing Applebot-Extended in the robots.txt file.”

Source: [Apple Support: About Applebot](https://support.apple.com/en-us/119829), read on 21 October 2026.

## What happens if you block it

Apple spells out the limit: if you disallow Applebot-Extended and also tag content with the nosnippet meta tag, your instructions may still allow Applebot to crawl the page, and the content remains discoverable through Spotlight, Siri and Safari. The same page says publishers can opt out of use in broad world-knowledge answers by applying this robots.txt control.

## The robots.txt lines

To allow it:

```
User-agent: Applebot-Extended
Allow: /
```

To block it:

```
User-agent: Applebot-Extended
Disallow: /
```

## How to tell a real request from a fake one

No network check exists for a token that sends no requests. Read robots.txt, on each host, and check Applebot separately, because the two tokens are independent and a single `User-agent: Applebot-Extended` group says nothing about Applebot.

## Compare with Applebot

Applebot: The crawler itself: allowing it keeps you in Spotlight, Siri and Safari search.

## Check your own site

The free check in the box above reads robots.txt for the crawlers in this set and sends one live request per crawler, so a rule that robots.txt allows but a firewall refuses shows up. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Why does Applebot-Extended not show up in my server logs?

It sends no requests. Apple describes it as a robots.txt control for whether crawled content is used for training.

### Does Disallow Applebot-Extended remove me from Siri?

Apple says content stays discoverable through Spotlight, Siri and Safari because Applebot may still crawl it.

## Sources

- [Apple Support: About Applebot](https://support.apple.com/en-us/119829)
