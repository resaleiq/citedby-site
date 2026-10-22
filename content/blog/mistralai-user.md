title: MistralAI-User, MistralAI-Index and MistralAI-Training explained
h1: MistralAI-User, MistralAI-Index and MistralAI-Training explained
description: Mistral documents three robots: a user-action fetcher, a search index agent and a training crawler. What each does, its robots.txt token and published IP files.
slug: mistralai-user
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Four facts about MistralAI-User: operator Mistral, job User-triggered fetch, robots.txt behaviour, published address lists
hero_sub: MistralAI-User, run by Mistral
hero_boxes: Operator|Mistral; Job|User-triggered fetch; Obeys robots.txt|Opt-out through robots.txt; Address list|4 ranges
widget: on
related: /bots|All AI crawlers compared; /bots/chatgpt-user|ChatGPT-User; /blog/is-gptbot-blocked|Is GPTBot blocked on your site?; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website?
answer: MistralAI-User is the Mistral agent that may visit a page when a user asks Vibe a question and link the source in its answer. Mistral says it is not used to crawl automatically or for generative AI training. Mistral's page also lists MistralAI-Index and MistralAI-Training, each with its own token.

## What MistralAI-User is

Mistral's crawler page lists three agents: MistralAI-User for user actions in Vibe, MistralAI-Index for indexing content for Mistral search, and MistralAI-Training, which crawls web content to help build datasets for training Mistral generative AI models. Webmasters can disallow each in robots.txt.

| Fact | MistralAI-User |
| --- | --- |
| Operator | Mistral |
| Job | User-triggered fetch |
| robots.txt token | `MistralAI-User` |
| Follows robots.txt | Opt-out through robots.txt |
| Published address list | 4 ranges (mistral.ai/mistralai-user-ips.json, file dated 2025-02-19) |
| Vendor page read | 21 October 2026 |

## What the vendor says

In the vendor's words: “MistralAI-User is for user actions in Vibe. When users ask Vibe a question, it may visit a web page to help answer and include a link to the source in its response.”

Source: [Mistral Docs: Mistral crawlers](https://docs.mistral.ai/robots), read on 21 October 2026.

## What happens if you block it

Disallowing MistralAI-User stops that agent opening your page for a Vibe user's question; it leaves the index and training agents alone, which have their own tokens. Mistral says the user agent is not used for crawling the web in any automatic fashion, nor to crawl content for generative AI training, and that content crawled by the index agent is not used for generative AI training of any kind.

## The robots.txt lines

To allow it:

```
User-agent: MistralAI-User
Allow: /
```

To block it:

```
User-agent: MistralAI-User
Disallow: /

User-agent: MistralAI-Training
Disallow: /
```

The user-agent string the vendor shows:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; MistralAI-User/1.0; +https://docs.mistral.ai/robots)
```

## How to tell a real request from a fake one

Mistral publishes separate address files for the agents. mistral.ai/mistralai-user-ips.json held 4 prefixes (creation time 2025-02-19) and the index file 2 prefixes (creation time 2026-04-19) on 21 October 2026. Two entries for an index crawler is a list a firewall rule can hold exactly.

## Compare with ChatGPT-User

[ChatGPT-User](/bots/chatgpt-user): The same job at OpenAI, with a different robots.txt promise.

## Check your own site

The audit box above reads robots.txt for the crawlers in this set and sends one live request per crawler, so a rule that robots.txt allows but a firewall refuses shows up. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Which Mistral agent trains models?

Mistral's page says MistralAI-Training crawls web content to help build datasets for training its generative AI models. MistralAI-User and MistralAI-Index are described as not used for training.

### Is Vibe a crawler?

Vibe is Mistral's product. MistralAI-User is the agent that may visit a page on behalf of a Vibe user.

## Sources

- [Mistral Docs: Mistral crawlers](https://docs.mistral.ai/robots)
- [mistral.ai/mistralai-user-ips.json](https://mistral.ai/mistralai-user-ips.json), read 21 October 2026
