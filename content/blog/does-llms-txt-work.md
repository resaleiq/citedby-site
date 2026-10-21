title: Does llms.txt work? What the data says (2026)
h1: Does llms.txt work? What two studies and Google's own documentation say
description: llms.txt is a proposed file for AI assistants. What the Ahrefs and SE Ranking studies found, what Google says, and when it is still worth adding.
slug: does-llms-txt-work
locale: en
cluster: AI visibility basics
date: 2026-10-18
reviewed: 2026-10-18
hero: does-llms-txt-work-hero.svg
hero_alt: Title card: does llms.txt work, with two figures: 97 percent of files got zero requests, and about 300,000 domains showed no clear link to AI citations
og: does-llms-txt-work-og.png
widget: on
howto: off
related: /tools/llms-txt-checker|llms.txt checker (free); /blog/can-chatgpt-read-my-website|Can ChatGPT read my website?; /blog/geo-vs-aeo-vs-seo|GEO vs AEO vs SEO audit; /sample|A sample report
answer: So far the evidence says llms.txt does not move AI citations. Ahrefs found 97% of valid llms.txt files got zero requests in May 2026, SE Ranking found no clear link to citations across about 300,000 domains, and Google says you do not need AI text files. Adding one is cheap, but do not expect traffic from it.

## What llms.txt is

llms.txt is a proposal by Jeremy Howard, published in September 2024: a Markdown file at `/llms.txt` with a title, a short summary and lists of links, meant to give AI agents a concise map of a site ([llmstxt.org](https://llmstxt.org/)). It is not an official standard of any search engine or AI lab. The proposal's own page lists adoption by documentation platforms and says OpenAI, Anthropic and Gemini publish the file for their own developer docs. That shows people write it. It does not show that assistants read yours when they answer a shopper.

## What the data says

![Two bars from the Ahrefs study of 137,210 domains in May 2026: 97 percent of valid llms.txt files got zero requests, and of the requests that arrived, 19.5 percent came from named AI tools](/blog/img/llms-txt-requests.svg "Figures as reported by Ahrefs. Most requests came from audit tools and unknown bots, not assistants.")

**Does anything fetch it?** Ahrefs checked 137,210 domains with its web analytics in May 2026. It found that 97% of valid llms.txt files received zero requests that month. Of the requests that did arrive, 19.5% came from named AI tools. SEO audit tools, unknown bots and general crawlers made up much of the rest. Ahrefs also reports that no AI bot went looking for the file on sites that did not have one ([Ahrefs study](https://ahrefs.com/blog/llmstxt-study)).

**Does it change citations?** SE Ranking analysed about 300,000 domains and published in November 2025 that having llms.txt showed no clear connection to how often a domain is cited by AI, with 10.13% of domains having the file ([Search Engine Journal on the SE Ranking study](https://www.searchenginejournal.com/llms-txt-shows-no-clear-effect-on-ai-citations-based-on-300k-domains/561542/)). Their own wording is that it "doesn't seem to directly impact AI citation frequency. At least not yet."

Both studies are correlation or log data from outside parties, run on different samples with different methods. They support "no measurable benefit so far", not "it can never matter".

## What Google says

Google's documentation on AI features states that there are no additional requirements to appear in AI Overviews or AI Mode, and that you do not need to create new machine-readable files, AI text files or markup to appear in them ([Google Search Central: AI features](https://developers.google.com/search/docs/appearance/ai-features)). For ChatGPT, OpenAI documents the crawlers it uses (OAI-SearchBot, GPTBot, ChatGPT-User) and says robots.txt controls them; it does not describe llms.txt there ([OpenAI crawler documentation](https://developers.openai.com/api/docs/bots)).

## So should you add one?

| Your site | Add llms.txt? | Why |
| --- | --- | --- |
| Online shop, no developer docs | Optional, after the basics | The data shows no citation benefit, so fix crawler access and on-page facts first |
| Software with public docs or an API | Reasonable | Coding agents and audit tools do fetch it, and Ahrefs saw agents among the requesters |
| You already have one | Leave it, keep it accurate | A stale file that lists dead pages helps nobody |

If you add one, keep it short: your name, one sentence on what you sell and where you ship, and links to your main category, shipping and returns pages. It takes minutes.

## What to do instead first

1. Audit your site with the box above (from €9). It tests whether AI crawlers can fetch your page and read it, and it reports whether an llms.txt exists as a hygiene item, without treating it as a ranking factor.
2. Put price, shipping and returns in the page text, not only in images or scripts.
3. Ask an assistant 20 buyer questions twice each and log who gets named ([the method](/blog/check-what-ai-says-about-your-brand)).

## FAQ

### Does ChatGPT read llms.txt?
There is no published evidence that it does. OpenAI documents its crawlers and robots.txt but does not describe llms.txt, and Ahrefs found most requests to llms.txt files came from other kinds of bots.

### Does llms.txt help me get cited by AI?
Not on current evidence. SE Ranking found no clear link across about 300,000 domains, and Google says no AI text file is needed for its AI features.

### Can llms.txt hurt?
It can mislead if it is stale or lists pages you removed. Keep it short and accurate, or do not publish one.

### Is llms.txt the same as robots.txt?
No. robots.txt tells crawlers what they may fetch. llms.txt is a proposed summary file for AI agents that no major search engine requires.

## Sources

- [llmstxt.org: the llms.txt proposal](https://llmstxt.org/)
- [Ahrefs: llms.txt study, 137,210 domains, May 2026](https://ahrefs.com/blog/llmstxt-study)
- [Search Engine Journal: SE Ranking study of about 300,000 domains, 20 November 2025](https://www.searchenginejournal.com/llms-txt-shows-no-clear-effect-on-ai-citations-based-on-300k-domains/561542/)
- [Google Search Central: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)
- [OpenAI: crawlers and user agents](https://developers.openai.com/api/docs/bots)
- [CitedBy site audit](https://citedby.eu/)
