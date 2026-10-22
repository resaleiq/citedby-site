title: Claude-SearchBot: Anthropic's search crawler and blocking it
h1: Claude-SearchBot: Anthropic's search crawler and what blocking costs
description: Claude-SearchBot indexes content to improve Claude's search results. Its robots.txt token, what a block does and how it differs from the other Claude robots.
slug: claude-searchbot
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Four facts about Claude-SearchBot: operator Anthropic, job Search, robots.txt behaviour, published address lists
hero_sub: Claude-SearchBot, run by Anthropic
hero_boxes: Operator|Anthropic; Job|Search; Obeys robots.txt|Yes; Address list|Anthropic points to a list
widget: on
related: /bots|All AI crawlers compared; /bots/claudebot|ClaudeBot; /blog/is-gptbot-blocked|Is GPTBot blocked on your site?; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website?
answer: Claude-SearchBot is the Anthropic robot that navigates the web to improve search result quality. Anthropic says disabling it prevents indexing of your content for search optimization, which may reduce your visibility and accuracy in user search results. Its robots.txt token is Claude-SearchBot.

## What Claude-SearchBot is

Claude-SearchBot is the indexing side of Anthropic's search. Anthropic describes it as analysing online content to improve relevance and accuracy of search responses. [ClaudeBot](/bots/claudebot) collects for training and [Claude-User](/bots/claude-user) answers a live question.

| Fact | Claude-SearchBot |
| --- | --- |
| Operator | Anthropic |
| Job | Search |
| robots.txt token | `Claude-SearchBot` |
| Follows robots.txt | Yes, Anthropic says its robots respect robots.txt |
| Published address list | Anthropic points to a list but advises against IP blocking |
| Vendor page read | 21 October 2026 |

## What the vendor says

In the vendor's words: “Claude-SearchBot navigates the web to improve search result quality for users. It analyzes online content specifically to enhance the relevance and accuracy of search responses. Disabling Claude-SearchBot on your site prevents our system from indexing your content for search optimization, which may reduce your site's visibility and accuracy in user search results.”

Source: [Anthropic Help Center: Does Anthropic crawl data from the web, and how can site owners block the crawler? (7 April 2026)](https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler), read on 21 October 2026.

## What happens if you block it

Anthropic names two effects of disabling it: your content is not indexed for search optimization, and your site's visibility and accuracy in user search results may fall.

## The robots.txt lines

To allow it:

```
User-agent: Claude-SearchBot
Allow: /
```

To block it:

```
User-agent: Claude-SearchBot
Disallow: /
```

## How to tell a real request from a fake one

The help article is dated 7 April 2026. It lists no user-agent string, so a log line that names Claude-SearchBot is a claim you cannot confirm from the article alone. Anthropic says traffic from an address on its linked list is Anthropic's, and it asks site owners who think a robot is misbehaving to write from an email on the domain concerned.

## Compare with ClaudeBot

[ClaudeBot](/bots/claudebot): Blocking ClaudeBot opts out of training only; it does not remove you from Claude's search index.

## Check your own site

The free check in the box above reads robots.txt for the crawlers in this set and sends one live request per crawler, so a rule that robots.txt allows but a firewall refuses shows up. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Do I have to allow Claude-SearchBot to be cited by Claude?

Anthropic says that disabling it may reduce your visibility and accuracy in user search results. It makes no promise either way that allowing it leads to a citation.

### Where do I put the rule?

In the robots.txt at the top level of each host. Anthropic says to do this for every subdomain.

## Sources

- [Anthropic Help Center: Does Anthropic crawl data from the web, and how can site owners block the crawler? (7 April 2026)](https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)
