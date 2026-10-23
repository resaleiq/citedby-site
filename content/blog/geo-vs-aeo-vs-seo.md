title: GEO vs AEO vs SEO audit: what differs, what you need
h1: GEO audit vs AEO audit vs SEO audit: what is different and which one you need
description: Three names for overlapping checks. What each audit looks at, what Google says about AI features, and a short order of work for a small online shop.
slug: geo-vs-aeo-vs-seo
locale: en
cluster: AI visibility basics
date: 2026-10-18
reviewed: 2026-10-18
hero: geo-vs-aeo-vs-seo-hero.svg
hero_alt: Title card: GEO vs AEO vs SEO audit, three boxes asking do I rank, am I the answer, does AI name me
og: geo-vs-aeo-vs-seo-og.png
widget: on
howto: off
related: /blog/can-chatgpt-read-my-website|Can ChatGPT read my website?; /blog/check-what-ai-says-about-your-brand|Check what AI says about your brand; /sample|A sample report; /changes|What changed: log of AI-crawler and search changes; /compare/profound-vs-peec-vs-otterly|Profound vs Peec vs Otterly compared
answer: An SEO audit checks whether you rank in search results. An AEO audit checks whether your pages give direct answers that assistants can quote. A GEO audit checks whether AI assistants name your brand in generated answers. The terms have no official definition, and the first two checks feed the third.

## The short version

None of the three terms is a standard. Each vendor draws the lines a little differently, so ask what a quoted audit actually tests before you compare prices. The grid below is how we use the words at CitedBy, and the sections after it explain each one.

![Grid of six checks against SEO, AEO and GEO audits: crawl access and raw HTML content are shared, ranking is SEO only, quotable answers are AEO and GEO, matching facts and being named are GEO](/blog/img/audit-compare.svg "Our reading of the three terms. Other vendors group the checks differently.")

## What an SEO audit checks

An SEO audit asks whether search engines can crawl and index your pages and whether those pages deserve to rank for the searches your buyers make. Typical items are crawl access, page speed, titles, internal links, structured data and backlinks. The output is a list of fixes and a set of ranking positions.

## What an AEO audit checks

AEO, answer engine optimization, asks whether a page answers a question so directly that a system can lift the answer. Typical items are a short answer under a question heading, FAQ blocks, tables and clear facts such as price, shipping time and returns. It overlaps with SEO, since a page that answers clearly also reads well to a search engine.

## What a GEO audit checks

GEO, generative engine optimization, asks whether an assistant such as ChatGPT, Gemini or Perplexity names your brand when someone asks for a recommendation, and whether what it says is true. The check is run by asking real buyer questions, several times, and counting who gets named, who gets linked and which facts are wrong. A page-level checklist cannot answer that, because the result depends on what the assistant finds across the web.

## What Google says

Google's documentation on AI features in Search states that there are no additional requirements to appear in AI Overviews or AI Mode and no other special optimizations necessary. It adds that the best practices for SEO remain relevant, that a page must be indexed and eligible to show with a snippet, and that you do not need new machine-readable files, AI text files or markup ([Google Search Central: AI features](https://developers.google.com/search/docs/appearance/ai-features)). That applies to Google's own features. ChatGPT uses its own crawlers, and OpenAI lists three with different jobs: OAI-SearchBot for ChatGPT's search features, GPTBot for model training, and ChatGPT-User for actions a person starts ([OpenAI crawler documentation](https://developers.openai.com/api/docs/bots)).

So the honest answer to "is it just SEO?" is: the base is shared, and the part that is new is measuring whether assistants name you.

## Which one a small shop needs first

| Your situation | Start with | Why |
| --- | --- | --- |
| Pages are not indexed, or the site is slow or empty without JavaScript | SEO basics | Nothing else works if crawlers cannot read the page |
| You rank, but pages bury price, shipping and returns | AEO fixes | Direct facts are what an assistant can quote |
| You rank and answer well, but buyers ask an assistant and rivals get named | GEO audit | This is the question only asking the assistant can answer |
| You are not sure | An audit, then 20 prompts by hand | The audit shows crawler access on every page, the prompts show what is said |

## A five-step order of work

1. Run the free check in the box above and fix any crawler that is blocked or any page that is empty to a crawler.
2. Make sure price, shipping, returns and a short description sit in the HTML text, not only in images or scripts.
3. Add a short answer and a FAQ to your top three pages, written in your buyers' own words.
4. Ask an assistant 20 buyer questions twice each and log who gets named ([the 20-prompt method](/blog/check-what-ai-says-about-your-brand)).
5. Fix the sources behind any wrong fact, then repeat the prompts a few weeks later.

## FAQ

### Is GEO just SEO with a new name?
Partly. The technical base is shared, and Google says SEO best practices remain relevant for its AI features. What GEO adds is measuring whether assistants name your brand, which a ranking report does not show.

### What is the difference between AEO and GEO?
AEO is about making a page easy to quote as an answer. GEO is about whether an assistant mentions your brand in what it generates. The first is a property of your pages, the second is an outcome you measure by asking.

### Do I need an llms.txt file for any of them?
Google says you do not need new machine-readable files or AI text files to appear in its AI features. We cover the evidence for other assistants in a separate guide on llms.txt.

### Which audit should I buy first?
Fix crawl access and basic facts first, since you can check those yourself. Buy a GEO audit when you want to know who gets named when buyers ask, and ask the seller what prompts it runs and how often.

## Sources

- [Google Search Central: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)
- [OpenAI: crawlers and user agents](https://developers.openai.com/api/docs/bots)
- [CitedBy site audit](https://citedby.eu/)
