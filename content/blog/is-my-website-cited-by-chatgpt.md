title: Is my website cited by ChatGPT? How to check it
h1: Is my website cited by ChatGPT? How to check it, step by step
description: Four checks tell you if ChatGPT can reach, index, name and send visitors to your site, with numbers from our crawl of 370 launched sites.
slug: is-my-website-cited-by-chatgpt
locale: en
cluster: Brand checks
date: 2026-10-23
reviewed: 2026-10-23
hero: auto
hero_alt: Four checks for a site and ChatGPT: reach, index, answers and visits
hero_sub: Reach, index, answers, visits
hero_boxes: 1 Reach|Crawlers let in; 2 Index|Bing holds your pages; 3 Answers|Ask real questions; 4 Visits|chatgpt.com in your logs
widget: on
howto: on
related: /tools/ai-crawler-check|AI crawler checker; /tools/findable-check|Is my site findable by Google, Bing and ChatGPT?; /data/launch-crawl-2026-10|Launch crawl: 370 sites; /blog/check-what-ai-says-about-your-brand|20 prompts to ask ChatGPT about your brand
answer: To find out if ChatGPT cites your website, run four checks: its crawlers can fetch your pages, Bing holds them in its index, ChatGPT names or links you when you ask the questions your buyers ask, and chatgpt.com shows up as a referrer in your analytics. A failure at step one or two explains most silence.

## The four checks

1. **Reach.** Open your robots.txt and look for rules on GPTBot, OAI-SearchBot and ChatGPT-User, then fetch your homepage without JavaScript and count the words. The [AI crawler checker](/tools/ai-crawler-check) does both for free.
2. **Index.** ChatGPT search draws on search-engine results from partners, and Bing is the one most often named, so check that Bing and Google hold your pages: add your site to Bing Webmaster Tools and Google Search Console, submit the sitemap, and run URL Inspection on your homepage.
3. **Answers.** Ask ChatGPT, logged out and in a new chat, the questions your buyers ask ("where can I buy [what you sell] in [country]?"). Write down whether it names you, links you and gets your facts right. Use the [20-prompt list](/blog/check-what-ai-says-about-your-brand).
4. **Visits.** In GA4 or your server logs, filter referrers for chatgpt.com. A cited page sends clicks; a mention without a link may not.

## What stops sites at step 1

We fetched 300 sites that launched on Show HN (15 to 20 October 2026) and 70 built with Lovable, as CitedBot, with robots.txt obeyed and no JavaScript. The [launch crawl](/data/launch-crawl-2026-10) found:

| Check | Show HN | Lovable |
| --- | --- | --- |
| Homepage under 100 words of text in the raw HTML | 16% (47/293) | 74% (49/66) |
| robots.txt blocks at least one of five AI crawlers | 4% (12/294) | 0% (0/67) |
| Homepage turned away a live request from one of those crawlers | 11% (33/293) | 0% (0/66) |

So robots.txt was the smaller factor. An empty HTML shell and a firewall that refuses AI user agents turned up more often. These numbers say nothing about whether those sites are cited; we did not measure that.

## What stops sites at step 2

A page that no index holds cannot be found by a search-backed answer. On 22 October 2026 Bing's own URL Inspection reported the home pages of three of our sites as "Discovered but not crawled". Discovered means Bing knows the URL and has not fetched it yet. Submitting the sitemap and the IndexNow protocol on every publish shortens the wait; it does not set a date.

## What to do with the result

- **Step 1 fails:** fix robots.txt rules or the firewall first, then make the homepage send its text in the HTML.
- **Step 2 fails:** submit the sitemap, request indexing and ping IndexNow, then check again in a week.
- **Step 3 shows rivals, not you:** open the pages ChatGPT linked for them and note what they hold that yours lacks.
- **Step 4 shows nothing:** one week is too short to judge; log the date and repeat monthly.

## The faster way

The audit crawls your site up to your plan's page limit, shows what AI crawlers cannot read or quote, and gives the exact fix for each issue. It starts at €9. Prefer to check only access first? [Run the free check](/tools/findable-check).

## FAQ

### Can I see every time ChatGPT cites my site?
No. OpenAI does not publish a citation report for site owners. Your server logs show its crawlers' requests and visits from chatgpt.com, and asking the questions by hand shows the rest.

### Does blocking GPTBot stop ChatGPT citing me?
Not by itself. GPTBot is the training crawler; OAI-SearchBot is the one used for search, and ChatGPT-User fetches pages when a person asks. Check each rule on its own.

### How long until a new page is cited?
We cannot give a number. It must first be crawled and indexed, and answers change from run to run.

## Sources

- [CitedBy launch crawl 2026-10: method, limits and CSV](https://citedby.eu/data/launch-crawl-2026-10)
- [OpenAI: crawlers overview (GPTBot, OAI-SearchBot, ChatGPT-User)](https://platform.openai.com/docs/bots)
- [About CitedBy: how we count](https://citedby.eu/about)
