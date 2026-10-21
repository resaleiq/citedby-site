title: Amazonbot, Amzn-SearchBot and Amzn-User: three Amazon agents, three rules
h1: Amazonbot, Amzn-SearchBot and Amzn-User: three Amazon agents, three rules
description: Amazon's page now describes three agents with independent robots.txt settings. What each does, which may train Amazon AI models and which may ignore robots.txt.
slug: amazonbot
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Four facts about Amazonbot: operator Amazon, job Product improvement, may train Amazon AI models, robots.txt behaviour, published address lists
hero_sub: Amazonbot, run by Amazon
hero_boxes: Operator|Amazon; Job|Product improvement; Obeys robots.txt|Yes; Address list|Published
widget: on
related: /bots|All AI crawlers compared; /bots/duckassistbot|DuckAssistBot; /blog/is-gptbot-blocked|Is GPTBot blocked on your site?; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website?
answer: Amazonbot is used to improve Amazon's products and services and may be used to train Amazon AI models. Amazon's page also covers Amzn-SearchBot, which makes content eligible for search experiences such as Alexa, and Amzn-User, which may not follow all robots.txt directives. Each setting is independent.

## What Amazonbot is

Amazon's page covers three user agents and says each setting is independent of the others and can take about 24 hours to take effect: Amazonbot, Amzn-SearchBot and Amzn-User. Only the first is described as possibly training Amazon AI models.

| Fact | Amazonbot |
| --- | --- |
| Operator | Amazon |
| Job | Product improvement, may train Amazon AI models |
| robots.txt token | `Amazonbot` |
| Follows robots.txt | Yes, changes take about 24 hours |
| Published address list | Published on Amazon's page (developer.amazon.com/amazonbot/ip-addresses) |
| Vendor page read | 21 October 2026 |

## What the vendor says

In the vendor's words: “Amazonbot is used to improve our products and services. This helps us provide more accurate information to customers and may be used to train Amazon AI models.”

Source: [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot), read on 21 October 2026.

## What happens if you block it

Amzn-SearchBot is for search experiences such as Alexa: allow it and the content is eligible to appear there. Amzn-User answers live Alexa queries that need up-to-date information; Amazon says it may not follow all robots.txt directives and does not crawl for generative AI training. A robots.txt that lists only Amazonbot therefore does not describe your policy for the other two.

## The robots.txt lines

To allow it:

```
User-agent: Amazonbot
Allow: /

User-agent: Amzn-SearchBot
Allow: /
```

To block it:

```
User-agent: Amazonbot
Disallow: /
```

The user-agent string the vendor shows:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Amazonbot/0.1) Chrome/W.X.Y.Z Safari/537.36
```

## How to tell a real request from a fake one

Amazon publishes the addresses for Amazonbot and, on separate pages, for Amzn-SearchBot and for live fetches; the lists are HTML pages, not a JSON file, so we do not state a count. Amazon also says that if robots.txt does not mention Amzn-SearchBot but allows other search bots, Amzn-SearchBot crawls in accordance with that file.

## Compare with DuckAssistBot

[DuckAssistBot](/bots/duckassistbot): Another answer-engine fetcher with a stated opt-out and a 72-hour delay.

## Check your own site

The audit box above reads robots.txt for the crawlers in this set and sends one live request per crawler, so a rule that robots.txt allows but a firewall refuses shows up. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does Amzn-User follow robots.txt?

Amazon says that because its actions can be initiated by a user, Amzn-User may not follow all robots.txt directives. It also says it does not crawl content for generative AI model training.

### Does blocking Amazonbot block Alexa answers?

Not by that line alone. Amazon describes Amzn-SearchBot and Amzn-User as separate agents with independent settings.

## Sources

- [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot)
- [developer.amazon.com/amazonbot/ip-addresses](https://developer.amazon.com/amazonbot/ip-addresses), read 21 October 2026
