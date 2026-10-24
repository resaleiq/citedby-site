title: ICC-Crawler: what it does and what blocking it changes
h1: ICC-Crawler: what it does and what blocking it changes
description: ICC-Crawler (NICT (Universal Communication Research Institute)): training. Robots.txt token, what a Disallow changes and how to verify a request.
slug: icc-crawler
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about ICC-Crawler: operator NICT (Universal Communication Research Institute), job Training, obeys robots.txt Yes, address list Listed on its page
hero_sub: ICC-Crawler, run by NICT (Universal Communication Research Institute)
hero_boxes: Operator|NICT (Universal Communication Research Institute); Job|Training; Obeys robots.txt|Yes; Address list|Listed on its page
widget: on
related: /bots|All AI crawlers compared; /bots/gptbot|GPTBot; /platforms|AI crawler settings by platform; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website? What decides it
answer: ICC-Crawler is run by the Universal Communication Research Institute at Japan's NICT. NICT says it uses collected pages for research on information processing, including multilingual translation, information analysis and artificial intelligence. It supports the Robots Exclusion Protocol: User-agent: ICC-Crawler with Disallow: / could disable collection from all pages.

## What ICC-Crawler is

ICC-Crawler is a crawler run by the Universal Communication Research Institute at Japan's National Institute of Information and Communications Technology (NICT). NICT says it uses collected pages for research and development of information processing technologies, including multilingual translation, information analysis and artificial intelligence. NICT may also provide collected information or research products to third parties, to the extent permitted by law.

| Fact | ICC-Crawler |
| --- | --- |
| Operator | NICT (Universal Communication Research Institute) |
| Job | Research data collection (includes AI research and development) |
| robots.txt token | `ICC-Crawler` |
| Follows robots.txt | Yes, and with a Crawl-Delay it uses the larger of that interval and its own minimum |
| IP addresses | Listed on the vendor's page (ucri.nict.go.jp/en/icccrawler.html) |
| Vendor page read | 24 October 2026 |

## What the vendor says

In the vendor's words (English original): “NICT uses the information it collects for research and development of advanced information processing technologies including multilingual translation, information analysis, and artificial intelligence technologies.”

Source: [NICT Universal Communication Research Institute: ICC-Crawler](https://ucri.nict.go.jp/en/icccrawler.html), read on 24 October 2026.

## What happens if you block ICC-Crawler

NICT says ICC-Crawler supports the Robots Exclusion Protocol and that adding User-agent: ICC-Crawler with Disallow: / to robots.txt could disable collection from all pages. It also lets site owners block a path or file type, or allow selected paths under a full Disallow. If access continues after that, NICT asks site owners to contact it so it can stop collecting from the host.

## The robots.txt lines

To allow ICC-Crawler:

```
User-agent: ICC-Crawler
Allow: /
```

To block ICC-Crawler:

```
User-agent: ICC-Crawler
Disallow: /
```

Paste a block into the robots.txt at the root of your host, for example https://example.com/robots.txt. A group for one token does not cover the operator's other crawlers.

The vendor's page shows no full user-agent string for ICC-Crawler.

## How to tell a real request from a fake one

The vendor page lists the crawler's IP addresses in plain text; it does not publish a machine-readable list.

## Compare with GPTBot

[GPTBot](/bots/gptbot): Both collect pages that feed AI development, but ICC-Crawler is run by a Japanese public research institute for its own research and publishes two crawler IP addresses on its page, while GPTBot is run by a commercial company.

## Your own site

The free check in the box above tests eight crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended, Bingbot and Googlebot). ICC-Crawler is not one of them: read your robots.txt for a `ICC-Crawler` group and look for the user agent in your server log. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does ICC-Crawler follow robots.txt?

Yes, and with a Crawl-Delay it uses the larger of that interval and its own minimum. Give ICC-Crawler its own User-agent group in robots.txt: the operator's other crawlers have their own settings.

### How do I know ICC-Crawler is really blocked?

robots.txt is only one layer: a CDN or firewall rule can also turn a crawler away, and a crawler can ignore the file. Check your server log for the user agent, and test the address from outside your network.

## Sources

- [NICT Universal Communication Research Institute: ICC-Crawler](https://ucri.nict.go.jp/en/icccrawler.html)
