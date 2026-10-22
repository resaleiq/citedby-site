title: Cloudflare: AI bot policies for Search, Agent and Training
slug: cloudflare
description: Cloudflare's Block AI Bots page splits AI bots into Search, Agent and Training with Block, Block on pages with ads and Allow. New defaults from 15 Sept 2026.
section: platforms
locale: en
cluster: AI crawlers by platform
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Four facts about Cloudflare: Where Security Settings, Behaviors Search, Agent, Training, Choices 3 per behavior, Page updated 1 Jul 2026
hero_sub: AI crawler settings on Cloudflare
hero_boxes: Where|Security Settings; Behaviors|Search, Agent, Training; Choices|3 per behavior; Page updated|1 Jul 2026
widget: on
related: /platforms|All platforms compared; /platforms/shopify|Shopify; /bots|AI crawlers compared; /guides/cms|AI visibility checklist for Shopify, WooCommerce and more
answer: Cloudflare sorts AI bots into three behaviors: Search, Agent and Training. For each you choose Block on all pages, Block on pages with ads, or Allow, under Security Settings, then Configure AI bot policies. Its page, last updated 1 July 2026, says updated defaults for new domains start on 15 September 2026.

## Where the setting is on Cloudflare

In the Cloudflare dashboard go to Security Settings, then Configure AI bot policies. Each of the three behaviors gets its own setting. This works at the network level, so it applies whatever platform the site runs on.

## Three behaviors, three choices and a date that has already passed

Cloudflare's presets are: Search, crawlers that collect or index your content to answer questions about it later; Agent, automated activity acting in real time on a person's behalf, such as chat fetch bots and browser-use agents; Training, crawlers taking your content to train or fine-tune a model, including mixed-purpose crawlers used for both Training and Search. Each preset blocks verified bots classified that way plus some unverified bots that behave similarly. The page, last updated 1 July 2026, announces new defaults for new domains from 15 September 2026: Training and Agent bots blocked on pages that display ads, Search remaining allowed, and mixed-purpose crawlers blocked by every configuration that blocks AI training, including the legacy Block AI bots option, which it marks as deprecating on that date. The page still used future tense when we read it on 21 October, five weeks after that date, so open your own dashboard and look at what is switched on rather than trusting either text.

In the vendor's words: “Search: crawlers that collect or index your content to answer questions about it later.”

Source: [Cloudflare Docs: Block AI Bots](https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/), read on 21 October 2026.

## The steps

1. Open your zone in the Cloudflare dashboard and go to Security Settings.
2. Open Configure AI bot policies.
3. For Search, Agent and Training pick Block on all pages, Block on pages with ads, or Allow.
4. If you use the legacy Block AI bots option, check which mixed-purpose crawlers it now covers, because Cloudflare says it is deprecating.
5. Test with the free [AI-crawler access checker](/tools/ai-crawler-check): a bot that robots.txt allows can still be refused here.

## The lines to use

To allow:

```
# Cloudflare settings are not robots.txt lines.
# Choose Allow (do not block) for Search so answer engines can fetch pages.
```

To block:

```
# Cloudflare settings are not robots.txt lines.
# Choose Block (on all pages) for Training; leave Search on Allow.
```

## Gotchas

The risk for a shop that wants citations is the middle preset: Cloudflare defines Agent as chat fetch bots acting on a person's behalf, which is the job of fetchers like [ChatGPT-User](/bots/chatgpt-user). Blocking Agent can stop an assistant opening your page when a person asks about it, even when your robots.txt allows it. Also note that Shopify says it does not recommend a proxy configuration in front of a Shopify store.

## Compare with Shopify

[Shopify](/platforms/shopify): Says it handles bot management itself and advises against a proxy.

## Check your own site

The free check in the box above reads robots.txt for the AI crawlers and sends one live request per crawler, so a rule that your platform's settings allow but a firewall refuses shows up. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does Cloudflare's AI block override robots.txt?

Cloudflare's page describes blocking by behavior at its network, so a bot can be refused there even where your robots.txt allows it. That is why a live request test matters.

### What is the difference between Search and Training on Cloudflare?

Search crawlers index content to answer questions later; Training crawlers take content to train or fine-tune a model. Mixed-purpose crawlers are classed as Training.

### Is Block AI bots still available?

Cloudflare marks it as deprecating on 15 September 2026. Its page was still written in future tense when we read it on 21 October 2026.

## Sources

- [Cloudflare Docs: Block AI Bots](https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/), read 21 October 2026
