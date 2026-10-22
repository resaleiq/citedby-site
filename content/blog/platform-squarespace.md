title: Squarespace: the AI crawler box blocks 26 bots but not ChatGPT
slug: squarespace
description: Squarespace's Crawlers panel has one box blocking known AI crawlers. The 26 names it writes to robots.txt leave out ChatGPT's search and user bots.
section: platforms
locale: en
cluster: AI crawlers by platform
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Four facts about Squarespace: Where Settings, Crawlers, Names blocked 26, Edit robots.txt No, Past training Not removed
hero_sub: AI crawler settings on Squarespace
hero_boxes: Where|Settings, Crawlers; Names blocked|26; Edit robots.txt|No; Past training|Not removed
widget: on
related: /platforms|All platforms compared; /platforms/wix|Wix; /bots|AI crawlers compared; /guides/cms|AI visibility checklist for Shopify, WooCommerce and more
answer: Squarespace has one checkbox, Settings, then Crawlers, then Block known artificial intelligence crawlers. It adds 26 named bots to your robots.txt. The list includes GPTBot, ClaudeBot and DuckAssistBot but not OAI-SearchBot, ChatGPT-User or PerplexityBot, and you cannot edit robots.txt yourself.

## Where the setting is on Squarespace

Open the Settings panel, click Crawlers, and tick Block known artificial intelligence crawlers. Squarespace's page says ticking the box updates your robots.txt file for the bots listed below, and that it may add more over time.

## The 26 names, and which ones are missing

Squarespace's help page lists exactly 26 names: AI2Bot, Ai2Bot-Dolma, aiHitBot, Amazonbot, anthropic-ai, Applebot-Extended, Bytespider, CCBot, ClaudeBot, cohere-ai, cohere-training-data-crawler, DuckAssistBot, FacebookBot, Google-Extended, GoogleOther, GoogleOther-Image, GoogleOther-Video, GPTBot, img2dataset, Meta-ExternalAgent, MyCentralAIScraperBot, omgili, omgilibot, Quora-Bot, TikTokSpider and YouBot. Read against our own crawler pages, the box covers the training and dataset crawlers of OpenAI, Anthropic, Google, Apple, Meta and Common Crawl. It does not name [OAI-SearchBot](/bots/oai-searchbot), [ChatGPT-User](/bots/chatgpt-user), [PerplexityBot](/bots/perplexitybot), [Claude-SearchBot](/bots/claude-searchbot) or [Claude-User](/bots/claude-user), so ticking it does not remove you from ChatGPT search. It does name [DuckAssistBot](/bots/duckassistbot) and [Amazonbot](/bots/amazonbot), which are answer-engine and product crawlers, so ticking it can also cost you DuckDuckGo's AI answers.

In the vendor's words: “Checking the box updates your robots.txt file to tell the following bots not to crawl your site.”

Source: [Squarespace Help: Request that AI models exclude your site](https://support.squarespace.com/hc/en-us/articles/360022347072-Request-that-AI-models-exclude-your-site), read on 21 October 2026.

## The steps

1. Open the Settings panel of your Squarespace site.
2. Click Crawlers.
3. Tick Block known artificial intelligence crawlers to block the 26 names, or leave it unticked to leave them all allowed.
4. To ask for another bot to be added, contact Squarespace: your page's own text says you can request it.

## The lines to use

To allow:

```
# Squarespace sites are open to these crawlers while the box is unticked.
# You cannot add lines yourself, so there is nothing to paste.
```

To block:

```
# Written by Squarespace when the box is ticked (excerpt):
User-agent: GPTBot
User-agent: ClaudeBot
User-agent: CCBot
Disallow: /
```

## Gotchas

Squarespace states that ticking the box does not retroactively remove content already scraped from your site from AI model training data. It also says robots.txt is only a request that friendly crawlers have offered to obey. The excerpt above is our shortened illustration of the kind of lines the box produces; the exact file is whatever your site serves at /robots.txt, so open it and read it.

## Compare with Wix

[Wix](/platforms/wix): A real robots.txt editor, and an example list of four names.

## Check your own site

The free check in the box above reads robots.txt for the AI crawlers and sends one live request per crawler, so a rule that your platform's settings allow but a firewall refuses shows up. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Can I allow ChatGPT search but block training on Squarespace?

Partly. Ticking the box writes a rule for GPTBot, and OAI-SearchBot is not among the 26 names. You cannot add lines of your own, so open your live /robots.txt to confirm what it says.

### Can I edit robots.txt on Squarespace?

Squarespace's own page treats the Crawlers panel as the control and does not offer a robots.txt editor. Wix and Webflow do.

### Does the box stop Google from indexing my site?

No. It is separate from the search engine crawlers option in the same panel. The AI box names Google-Extended and GoogleOther, not Googlebot.

## Sources

- [Squarespace Help: Request that AI models exclude your site](https://support.squarespace.com/hc/en-us/articles/360022347072-Request-that-AI-models-exclude-your-site), read 21 October 2026
