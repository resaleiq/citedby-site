title: Amzn-User: what it does and what blocking it changes
h1: Amzn-User: what it does and what blocking it changes
description: Amzn-User (Amazon): user-triggered fetch. Robots.txt token, what a Disallow changes and how to verify a request, read from the operator's own page.
slug: amzn-user
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about Amzn-User: operator Amazon, job User-triggered fetch, obeys robots.txt Not always, address list Listed on its page
hero_sub: Amzn-User, run by Amazon
hero_boxes: Operator|Amazon; Job|User-triggered fetch; Obeys robots.txt|Not always; Address list|Listed on its page
widget: on
related: /bots|All AI crawlers compared; /bots/amzn-searchbot|Amzn-SearchBot; /platforms|AI crawler settings by platform; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website? What decides it
answer: Amzn-User is the Amazon user agent that fetches live pages when a customer asks Alexa something that needs current information. Amazon says it does not crawl for generative AI training and may not follow all robots.txt directives, because the action is user-initiated. Amazonbot and Amzn-SearchBot are separate settings.

## What Amzn-User is

Amzn-User is an Amazon user agent that supports user actions, such as responding to Alexa queries that require up-to-date information. Amazon says that when a customer asks a question, Amzn-User may fetch live information from the web to provide accurate answers on the user's behalf. Amazon says it does not crawl content for generative AI model training.

| Fact | Amzn-User |
| --- | --- |
| Operator | Amazon |
| Job | User-triggered fetch |
| robots.txt token | `Amzn-User` |
| Follows robots.txt | Partial, may not follow all robots.txt directives because actions can be user-initiated |
| IP addresses | Listed on the vendor's page (developer.amazon.com/amazonbot/live-ip-addresses) |
| Vendor page read | 24 October 2026 |

## What the vendor says

In the vendor's words (English original): “Because actions taken by Amzn-User can be initiated by a user, it may not follow all robots.txt directives.”

Source: [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot), read on 24 October 2026.

## What happens if you block Amzn-User

Amazon says Amzn-User may not follow all robots.txt directives because its actions can be initiated by a user. Amazon also says each of its user agent settings (Amazonbot, Amzn-SearchBot, Amzn-User) is independent of the others and may take about 24 hours to reflect changes.

## The robots.txt lines

To allow Amzn-User:

```
User-agent: Amzn-User
Allow: /
```

To block Amzn-User:

```
User-agent: Amzn-User
Disallow: /
```

Paste a block into the robots.txt at the root of your host, for example https://example.com/robots.txt. A group for one token does not cover the operator's other crawlers.

The user-agent string the vendor shows:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Amzn-User/0.1) Chrome/W.X.Y.Z Safari/537.36
```

## How to tell a real request from a fake one

Amazon publishes the Amzn-User IP addresses on a web page that shows the list as JSON, and links it from the Amazonbot documentation page.

## Compare with Amzn-SearchBot

[Amzn-SearchBot](/bots/amzn-searchbot): Amzn-SearchBot is an automated crawler for Amazon search experiences that Amazon says respects robots.txt, while Amzn-User fetches live information when a customer asks and may not follow all directives.

## Your own site

The free check in the box above tests eight crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot). Amzn-User is not one of them: read your robots.txt for a `Amzn-User` group and look for the user agent in your server log. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does Amzn-User follow robots.txt?

Not always: may not follow all robots.txt directives because actions can be user-initiated. A rule for Amzn-User in robots.txt may therefore not stop it. To refuse it for certain, use a firewall or CDN rule that matches both the user agent and the published addresses.

### How do I know Amzn-User is really blocked?

robots.txt is only one layer: a CDN or firewall rule can also turn a crawler away, and a crawler can ignore the file. Check your server log for the user agent, and test the address from outside your network.

## Sources

- [Amazon: About Amazonbot](https://developer.amazon.com/amazonbot)
- [Amazon: Amzn-User IP addresses (read 2026-10-24)](https://developer.amazon.com/amazonbot/live-ip-addresses/)
