title: DuckAssistBot: DuckDuckGo's real-time answer crawler and its 486 addresses
h1: DuckAssistBot: DuckDuckGo's real-time answer crawler and its 486 addresses
description: DuckAssistBot fetches pages for DuckDuckGo's AI-assisted answers, which cite their sources. Opt-out takes 72 hours, search rankings are unaffected and DuckDuckGo lists 486 IP addresses.
slug: duckassistbot
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Four facts about DuckAssistBot: operator DuckDuckGo, job Real-time fetch for AI-assisted answers, robots.txt behaviour, published address lists
hero_sub: DuckAssistBot, run by DuckDuckGo
hero_boxes: Operator|DuckDuckGo; Job|Real-time fetch for AI-assisted answers; Obeys robots.txt|Yes; Address list|486 addresses
widget: on
related: /bots|All AI crawlers compared; /bots/amazonbot|Amazonbot; /blog/is-gptbot-blocked|Is GPTBot blocked on your site?; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website?
answer: DuckAssistBot crawls pages in real time for DuckDuckGo's AI-assisted answers, which cite their sources. DuckDuckGo says the data is not used to train AI models. A robots.txt Disallow takes effect after 72 hours and does not affect organic search rankings. It lists 486 IP addresses.

## What DuckAssistBot is

DuckDuckGo runs two bots that people confuse. DuckDuckBot is the search crawler; DuckAssistBot is the one behind AI-assisted answers. DuckDuckGo's help page says the answers prominently cite their sources and that the crawled data is not used to train AI models.

| Fact | DuckAssistBot |
| --- | --- |
| Operator | DuckDuckGo |
| Job | Real-time fetch for AI-assisted answers |
| robots.txt token | `DuckAssistBot` |
| Follows robots.txt | Yes, a change takes effect after 72 hours |
| Published address list | 486 addresses (duckduckgo.com/duckassistbot.json, file dated 2026-09-01) |
| Vendor page read | 21 October 2026 |

## What the vendor says

In the vendor's words: “DuckAssistBot is a web crawler for DuckDuckGo Search that crawls pages in real-time for our AI-assisted answers, which prominently cite their sources. This data is not used in any way to train AI models.”

Source: [DuckDuckGo Help Pages: About DuckAssistBot](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot), read on 21 October 2026.

## What happens if you block it

DuckDuckGo says that once you disallow DuckAssistBot the change takes effect after 72 hours, and that opting out does not impact organic search rankings and will not affect whether sites appear in its search results. The cost of a block is therefore limited to the assisted answers and their citations. Opt-out problems go to the address the page gives, crawling@duckduckgo.com.

## The robots.txt lines

To allow it:

```
User-agent: DuckAssistBot
Allow: /
```

To block it:

```
User-agent: DuckAssistBot
Disallow: /
```

The user-agent string the vendor shows:

```
DuckAssistBot/1.2; (+http://duckduckgo.com/duckassistbot.html)
```

## How to tell a real request from a fake one

DuckDuckGo lists the addresses in the help article and as JSON at duckduckgo.com/duckassistbot.json. The file held 486 entries on 21 October 2026, creation time 2026-09-01, longer than any other address list we counted for this set, and it holds single addresses where the others publish CIDR ranges. The user agent appears as `DuckAssistBot/1.2`.

## Compare with Amazonbot

[Amazonbot](/bots/amazonbot): Amazon's family of three agents, one of which may ignore robots.txt.

## Check your own site

The audit box above reads robots.txt for the crawlers in this set and sends one live request per crawler, so a rule that robots.txt allows but a firewall refuses shows up. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### How long does a DuckAssistBot opt-out take?

DuckDuckGo says the change takes effect after 72 hours.

### Will blocking DuckAssistBot drop me from DuckDuckGo search?

DuckDuckGo says it does not impact organic search rankings and does not affect whether sites appear in its search results.

## Sources

- [DuckDuckGo Help Pages: About DuckAssistBot](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot)
- [duckduckgo.com/duckassistbot.json](https://duckduckgo.com/duckassistbot.json), read 21 October 2026
