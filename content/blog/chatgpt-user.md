title: ChatGPT-User: the fetcher that opens your page when someone asks
h1: ChatGPT-User: the fetcher that opens your page when someone asks
description: ChatGPT-User visits a page when a person asks ChatGPT or a custom GPT about it. Why robots.txt may not apply, its user-agent string and 234 published IP ranges.
slug: chatgpt-user
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Four facts about ChatGPT-User: operator OpenAI, job User-triggered fetch, robots.txt behaviour, published address lists
hero_sub: ChatGPT-User, run by OpenAI
hero_boxes: Operator|OpenAI; Job|User-triggered fetch; Obeys robots.txt|Robots.txt rules may not apply; Address list|234 ranges
widget: on
related: /bots|All AI crawlers compared; /bots/oai-searchbot|OAI-SearchBot; /blog/is-gptbot-blocked|Is GPTBot blocked on your site?; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website?
answer: ChatGPT-User visits a web page when a person asks ChatGPT or a custom GPT a question that needs it. OpenAI says it is not used to crawl automatically and that, because a user starts the request, robots.txt rules may not apply. OpenAI lists 234 IP ranges for it.

## What ChatGPT-User is

Unlike the other OpenAI robots, ChatGPT-User does not roam the web by itself. OpenAI describes it as the agent used for certain user actions in ChatGPT and custom GPTs, including pages a custom GPT reaches through GPT Actions. A person typed something, and a request to your server followed.

| Fact | ChatGPT-User |
| --- | --- |
| Operator | OpenAI |
| Job | User-triggered fetch |
| robots.txt token | `ChatGPT-User` |
| Follows robots.txt | Robots.txt rules may not apply |
| Published address list | 234 ranges (openai.com/chatgpt-user.json, file dated 2026-10-20) |
| Vendor page read | 21 October 2026 |

## What the vendor says

In the vendor's words: “ChatGPT-User is not used for crawling the web in an automatic fashion. Because these actions are initiated by a user, robots.txt rules may not apply.”

Source: [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots), read on 21 October 2026.

## What happens if you block it

Because the visit is user-initiated, OpenAI warns that robots.txt rules may not apply, so a `Disallow` line for ChatGPT-User is not a guaranteed stop. OpenAI also says ChatGPT-User is not used to decide whether content appears in search and sends search opt-outs to OAI-SearchBot. If you need to stop these requests, the control is on your server or CDN, not in robots.txt alone.

## The robots.txt lines

To allow it:

```
User-agent: ChatGPT-User
Allow: /
```

To block it:

```
User-agent: ChatGPT-User
Disallow: /   # OpenAI says robots.txt rules may not apply to this agent
```

The user-agent string the vendor shows:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ChatGPT-User/1.0; +https://openai.com/bot
```

## How to tell a real request from a fake one

Its address list is the longest of the three OpenAI files we counted: openai.com/chatgpt-user.json held 234 prefixes on 21 October 2026, creation time 2026-10-20, the day before this page. A list that long is a reason to fetch it again when you check a log line, not to copy it once into a firewall.

## Compare with OAI-SearchBot

[OAI-SearchBot](/bots/oai-searchbot): OAI-SearchBot is the search crawler and does obey robots.txt.

## Check your own site

The free check in the box above reads robots.txt for the crawlers in this set and sends one live request per crawler, so a rule that robots.txt allows but a firewall refuses shows up. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does ChatGPT-User obey robots.txt?

OpenAI says robots.txt rules may not apply to it because a person starts each request. Treat a robots.txt block as a request that OpenAI is not committed to honour here.

### Is ChatGPT-User the same as GPTBot?

No. GPTBot crawls content that may be used for training. ChatGPT-User only fetches a page when a user action calls for it, and OpenAI says it is not used to crawl the web automatically.

## Sources

- [OpenAI: Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots)
- [openai.com/chatgpt-user.json](https://openai.com/chatgpt-user.json), read 21 October 2026
