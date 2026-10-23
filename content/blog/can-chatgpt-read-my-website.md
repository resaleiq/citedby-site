title: Can ChatGPT read my website? What decides it
h1: Can ChatGPT read my website?
description: Three things decide whether ChatGPT and other AI assistants can read your shop: robots.txt, the text in your HTML, and structured data. How to check each.
slug: can-chatgpt-read-my-website
locale: en
cluster: Crawlability
date: 2026-10-18
reviewed: 2026-10-18
hero: can-chatgpt-read-my-website-hero.svg
hero_alt: Three gates between a shop page and an AI assistant: robots.txt, page text and structured data
og: can-chatgpt-read-my-website-og.png
widget: on
howto: on
related: /bots|AI crawlers: what each one does and how to allow or block it; /ai-visibility-audit|AI visibility audit: what it is and what to check; /data|Who ChatGPT linked, by niche; /sample|A sample report; /tools/findable-check|Findable check: can search engines find your pages? (free)
answer: ChatGPT can read your website if three things hold: robots.txt does not block OAI-SearchBot, the page text is in the HTML your server sends rather than added by JavaScript, and your server or firewall does not refuse the crawler. The CitedBy audit tests the first two on every page.

## The three gates

ChatGPT search uses a crawler called OAI-SearchBot to find pages. OpenAI also runs GPTBot, which collects training data, and ChatGPT-User, which fetches a page when a person asks about it. OpenAI says each is controlled separately in robots.txt, so you can allow one and block another ([OpenAI crawler documentation](https://developers.openai.com/api/docs/bots)).

![Three gates: robots.txt, page response, page content, with what the audit tests at each](/blog/img/three-gates.svg "The audit tests gates 1 and 3. Gate 2 needs your server logs.")

## How to check, step by step

1. Open `yourshop.com/robots.txt` in a browser. Look for `User-agent: OAI-SearchBot`, `GPTBot` or `*` followed by `Disallow: /`. A blanket `Disallow: /` under `User-agent: *` blocks every crawler that has no rule of its own.
2. Run the free check in the box above. It reads robots.txt for OAI-SearchBot, GPTBot, PerplexityBot, Google-Extended and Bingbot and tells you which are blocked.
3. Look at the word count it reports for the page HTML. Your homepage should have hundreds of words there, including your brand name and what you sell.
4. Open the page, choose "View page source" and search for your product name. If it is missing, the page builds its text with JavaScript and a crawler that does not run scripts sees nothing.
5. Check that Organization data (JSON-LD) is present, so assistants get your name, logo and contact details from one place.

![A CitedBy check run on bbc.com on 18 October 2026: robots.txt blocks OAI-SearchBot, GPTBot, PerplexityBot and Google-Extended; 2,547 words are readable in the HTML](/blog/img/check-result-bbc.webp "A real run on bbc.com, 18 Oct 2026. The BBC blocks these crawlers on purpose; for a shop that wants to be named, a result like this is the problem to fix."){972x559}

## What a blocked page looks like to a crawler

Some shop themes and website builders send an almost empty page and fill it in with JavaScript. A visitor sees a full product page. A crawler that does not run JavaScript receives a shell.

![Left: a visitor sees name, price and description. Right: the crawler receives only an empty div and a script tag](/blog/img/crawler-vs-visitor.svg "Illustration with invented example values.")

Some assistants do run JavaScript and some do not, so the safe position is to have your brand and product text in the HTML itself.

## The gate the audit cannot see

robots.txt is a request, and your hosting is the enforcement. A firewall or CDN setting can answer a crawler with an error even when robots.txt allows it. The audit does not test this. Look in your server or CDN logs for requests from `OAI-SearchBot` and see which status codes came back; a run of 403 responses is the sign.

## What to do with the result

- **robots.txt blocks a crawler you want:** remove the matching `Disallow` rule. OpenAI says changes can take about a day to take effect.
- **Few words in the HTML:** render the homepage and product text on the server.
- **No Organization data:** add it as JSON-LD on the homepage.
- **All clear:** being readable is the entry ticket, not the result. Whether an assistant names your shop is a separate question, which the audit measures by asking real buyer questions.

## FAQ

### Is GPTBot the same as ChatGPT search?
No. GPTBot collects data that may be used to train models. OAI-SearchBot is the crawler for ChatGPT search results. You can block GPTBot and still allow OAI-SearchBot.

### If I block GPTBot, will ChatGPT stop mentioning my shop?
Not by itself. Search results depend on OAI-SearchBot. Blocking only GPTBot is a common choice for shops that do not want their content used for training.

### Does adding llms.txt fix this?
It is optional. We do not expect it to change what assistants answer, and the audit marks it as optional.

### How long until a change shows up?
OpenAI says it can take about 24 hours for its systems to adjust after you change robots.txt.

## Sources

- [OpenAI: crawlers and user agents](https://developers.openai.com/api/docs/bots)
- [CitedBy site audit](https://citedby.eu/)
