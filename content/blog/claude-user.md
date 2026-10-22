title: Claude-User: fetches pages when someone asks Claude
h1: Claude-User: the agent that fetches pages when someone asks Claude
description: Claude-User retrieves a page when a person asks Claude something. What Anthropic says disabling it does, and how it differs from ClaudeBot and Claude-SearchBot.
slug: claude-user
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Four facts about Claude-User: operator Anthropic, job User-triggered fetch, robots.txt behaviour, published address lists
hero_sub: Claude-User, run by Anthropic
hero_boxes: Operator|Anthropic; Job|User-triggered fetch; Obeys robots.txt|Yes; Address list|Anthropic points to a list
widget: on
related: /bots|All AI crawlers compared; /bots/claude-searchbot|Claude-SearchBot; /blog/is-gptbot-blocked|Is GPTBot blocked on your site?; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website?
answer: Claude-User is the agent Claude may use to access a website when a person asks it a question. Anthropic says disabling it prevents retrieval of your content in response to a user query, which may reduce your visibility for user-directed web search. It is separate from ClaudeBot and Claude-SearchBot.

## What Claude-User is

Of Anthropic's three robots, Claude-User is the one tied to a person's question. It does not collect training data ([ClaudeBot](/bots/claudebot) does) and it does not build the search index ([Claude-SearchBot](/bots/claude-searchbot) does).

| Fact | Claude-User |
| --- | --- |
| Operator | Anthropic |
| Job | User-triggered fetch |
| robots.txt token | `Claude-User` |
| Follows robots.txt | Yes, Anthropic says its robots respect robots.txt |
| Published address list | Anthropic points to a list but advises against IP blocking |
| Vendor page read | 21 October 2026 |

## What the vendor says

In the vendor's words: “Claude-User supports Claude AI users. When individuals ask questions to Claude, it may access websites using a Claude-User agent. Disabling Claude-User on your site prevents our system from retrieving your content in response to a user query, which may reduce your site's visibility for user-directed web search.”

Source: [Anthropic Help Center: Does Anthropic crawl data from the web, and how can site owners block the crawler? (7 April 2026)](https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler), read on 21 October 2026.

## What happens if you block it

This is where Anthropic's wording on cost is most direct: disabling Claude-User prevents retrieval "in response to a user query" and "may reduce your site's visibility for user-directed web search". A shop that blocks it can still be known to the model from other sources, but Claude cannot open the page when asked.

## The robots.txt lines

To allow it:

```
User-agent: Claude-User
Allow: /
```

To block it:

```
User-agent: Claude-User
Disallow: /
```

## How to tell a real request from a fake one

Anthropic's help article does not print a user-agent string for the three robots, and it says its source IP addresses are on a list it links. Because Anthropic also says that blocking those addresses can stop its robots reading robots.txt, the article's advice is to control access in robots.txt rather than at the IP layer.

## Compare with Claude-SearchBot

[Claude-SearchBot](/bots/claude-searchbot): Search quality robot; its block affects indexing for search, not a user's live question.

## Check your own site

The free check in the box above reads robots.txt for the crawlers in this set and sends one live request per crawler, so a rule that robots.txt allows but a firewall refuses shows up. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### What is the difference between Claude-User and Claude-SearchBot?

Claude-User fetches a page when a person asks Claude a question. Claude-SearchBot navigates the web to improve the quality of search results. They have separate robots.txt rules.

### Will blocking Claude-User hide my shop from Claude?

Anthropic says it may reduce visibility for user-directed web search. It does not say it removes you from everything Claude knows.

## Sources

- [Anthropic Help Center: Does Anthropic crawl data from the web, and how can site owners block the crawler? (7 April 2026)](https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)
