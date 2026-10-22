title: Bingbot: Microsoft's crawler, five user agents, how to verify
slug: bingbot
description: Bingbot is Bing's standard crawler. The five Microsoft crawler names, how to verify a request and where crawl rate is set, read from Bing's own help page.
section: bots
locale: en
cluster: AI crawlers
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Four facts about Bingbot: operator Microsoft, job Search crawler, obeys robots.txt Yes
hero_sub: Bingbot, run by Microsoft
hero_boxes: Operator|Microsoft; Job|Search crawler; Obeys robots.txt|Yes; Address list|Verify tool, no list read
widget: on
related: /bots|All AI crawlers compared; /bots/googlebot|Googlebot; /platforms|AI crawler settings by platform; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website?
answer: Bingbot is Microsoft's standard crawler and handles most of Bing's crawling. Bing's help page lists five crawlers: Bingbot, AdIdxBot, BingPreview, MicrosoftPreview and BingVideoPreview. You control them through robots.txt, and crawl rate through the Crawl control tool in Bing Webmaster Tools, not through robots.txt.

## What Bingbot is

Bing's page is titled "Overview of Bing crawlers (user agents)" and says Bing operates these main crawlers today: Bingbot (the standard crawler), AdIdxBot (used by Bing Ads, which crawls ads and follows their websites for quality control), BingPreview (page snapshots for Bing), MicrosoftPreview (snapshots for Microsoft products) and BingVideoPreview (video previews, in Bing only). Bingbot, AdIdxBot, BingPreview and BingVideoPreview have desktop and mobile variants. The page does not name a separate AI crawler. The same help section includes "How To Permanently Remove a URL or Page from Bing or Copilot", which is the page to read if the goal is removal rather than access.

| Fact | Bingbot |
| --- | --- |
| Operator | Microsoft |
| Job | Search crawler |
| robots.txt token | `bingbot` |
| Follows robots.txt | Yes |
| Published address list | Verify tool, no list read |
| Vendor page read | 21 October 2026 |

## What the vendor says

In the vendor's words: “Bingbot is our standard crawler and handles most of our crawling needs each day.”

Source: [Microsoft Bing Webmaster help: Which Crawlers Does Bing Use?](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0), read on 21 October 2026.

## What happens if you block it

Bing's page does not say what a block costs; this is our reading, not Bing's. Bingbot is the crawler that feeds Bing, so disallowing it in robots.txt stops Bing crawling those pages, and anything that relies on Bing's index loses them too. Bing gives you two controls: robots.txt tells its crawlers how to interact with your site, and Bing Webmaster Tools has a Crawl control tool that sets the crawl rate by the hour.

## The robots.txt lines

To allow it:

```
User-agent: bingbot
Allow: /
```

To block it:

```
User-agent: bingbot
Disallow: /
```

The user-agent string the vendor shows:

```
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm) Chrome/W.X.Y.Z Safari/537.36
```

## How to tell a real request from a fake one

Bing says user agent strings are easy to spoof, so not every request with them comes from a real Bing crawler. To check the address, use the Verify Bingbot tool, or one of the other verification methods Bing describes. In the user-agent string, W.X.Y.Z stands for the Microsoft Edge version Bing renders with, which Bing says it updates regularly. We did not read an IP list on that page, so we state no count.

## Compare with Googlebot

[Googlebot](/bots/googlebot): The other main search crawler: a different token and different verification.

## Check your own site

The free check in the box above reads robots.txt for the crawlers in this set and sends one live request per crawler, so a rule that robots.txt allows but a firewall refuses shows up. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Is there a separate Bing AI crawler?

Bing's page lists five crawlers and none is described as an AI crawler. Wix's example list names BingAI, which is not on Bing's list.

### How do I slow Bingbot down?

Bing says to use the Crawl control tool in Bing Webmaster Tools, which sets the crawl rate by the hour.

### How do I know a request is really Bingbot?

Do not trust the user agent alone. Bing says it can be faked and points to its Verify Bingbot tool.

## Sources

- [Microsoft Bing Webmaster help: Which Crawlers Does Bing Use?](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0), read 21 October 2026
