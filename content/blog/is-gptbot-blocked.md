title: Is GPTBot blocked on your site? 4 ways to check (2026)
h1: Is GPTBot blocked on my site? Four places to check, with a test for each
description: GPTBot can be stopped by robots.txt, your CDN, a firewall rule or your server. How to find out which, in minutes, and what blocking it does and does not change.
slug: is-gptbot-blocked
locale: en
cluster: Crawlability
date: 2026-10-18
reviewed: 2026-10-18
hero: is-gptbot-blocked-hero.svg
hero_alt: Four boxes numbered 1 to 4: robots.txt, CDN, firewall, server, the places GPTBot can be stopped
og: is-gptbot-blocked-og.png
widget: on
howto: on
related: /bots|AI crawlers: what each one does and how to allow or block it; /tools/ai-crawler-check|AI-crawler access checker (free); /blog/can-chatgpt-read-my-website|Can ChatGPT read my website?; /|The CitedBy site audit; /sample|A sample report; /tools/findable-check|Findable check: can search engines find your pages? (free); /changes|What changed: log of AI-crawler and search changes
answer: GPTBot is blocked on your site if robots.txt has a Disallow rule that applies to it, or if a CDN, firewall or server rule refuses its requests. Open yourshop.com/robots.txt, run an audit, then compare two requests to your server. Blocking GPTBot does not by itself block ChatGPT search.

## Four places GPTBot can be stopped

GPTBot is the crawler OpenAI says it uses to collect content that may be used to train its models. A request from it can be turned away at four layers, and each one needs its own test. The free check in the box above covers the first. The other three answer with an error code even when robots.txt says yes.

![Table of four layers where GPTBot can be stopped: robots.txt, CDN, security plugin or WAF rule, web server rule, each with how to see it](/blog/img/four-places.svg "Layers 2 to 4 are invisible in robots.txt, so check them separately.")

## How to check, step by step

1. Open `yourshop.com/robots.txt` in a browser. Look for a group that names `GPTBot`. If there is none, GPTBot follows the `User-agent: *` group, so a blanket `Disallow: /` under it blocks GPTBot too ([RFC 9309](https://www.rfc-editor.org/info/rfc9309/)).
2. Run the free check in the box above. It reads robots.txt for GPTBot, OAI-SearchBot, PerplexityBot, Google-Extended and Bingbot and names the ones that are blocked.
3. Send two requests to your homepage and compare the status codes: one normal, one that carries the GPTBot user-agent string. Commands below.
4. Open your CDN account and look at its AI crawler settings. For Cloudflare, the steps are below.
5. Open your security plugin or firewall rule list and search for `GPTBot`, `bot`, `AI` and `crawler`.
6. Search your server logs for `GPTBot`. A run of 403 responses to it is the sign of a block that robots.txt does not show.

## The two-request test

Replace `yourshop.com` with your address. The first command sends a normal request, the second sends the GPTBot user-agent string that OpenAI publishes. Each prints only the status code.

```
curl -s -o /dev/null -w "%{http_code}\n" https://yourshop.com/
curl -s -o /dev/null -w "%{http_code}\n" -A "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.4; +https://openai.com/gptbot" https://yourshop.com/
```

![Two requests to one page, one normal and one with the GPTBot user-agent, and what each pair of status codes means](/blog/img/curl-compare.svg "A 403 on the second request alone means a rule targets the crawler's name.")

Read the result with one limit in mind. This test comes from your own computer. If your host also judges crawlers by IP address, the real GPTBot can get a different answer from the one you saw. OpenAI publishes the IP ranges for GPTBot at `openai.com/gptbot.json`, so your logs can show whether requests from those ranges got through ([OpenAI crawler documentation](https://developers.openai.com/api/docs/bots)).

## Cloudflare: where the setting lives

Cloudflare's documentation describes the steps: open your domain, go to AI Crawl Control, open the Security tab, then the Crawlers tab. The Actions column lets you Allow or Block each crawler. Choosing Block creates or updates a WAF custom rule, and you can still enforce robots.txt when you choose Allow ([Cloudflare: manage AI crawlers](https://developers.cloudflare.com/ai-crawl-control/features/manage-ai-crawlers/)).

Cloudflare's defaults are also changing. Help Net Security reports that from 15 September 2026 new domains block Training and Agent crawlers by default on pages that show ads, while Search crawlers stay allowed ([Help Net Security](https://www.helpnetsecurity.com/2026/07/02/cloudflare-ai-crawler-controls/)). Check your own dashboard rather than assuming which default your domain got.

## When the check says your site refused the request

A plain request from our check can itself be refused. When the answer is HTTP 403, 429 or 503, the check says so and says it cannot tell from outside whether AI crawlers are refused as well. A 403 usually means a rule blocked the request. A 429 or 503 can also mean rate limiting or an outage, which affects every visitor. Fix the cause in your CDN, firewall or hosting panel, then run the check again.

## Should you unblock GPTBot?

That is your decision, and blocking it is a legitimate choice. OpenAI lists GPTBot, OAI-SearchBot and ChatGPT-User as separate crawlers with separate jobs. GPTBot is for training data. OAI-SearchBot surfaces sites in ChatGPT's search features. ChatGPT-User fetches pages when a person asks about them.

| Your goal | What to do |
| --- | --- |
| Appear in ChatGPT search results, keep content out of training | Allow `OAI-SearchBot`, disallow `GPTBot` |
| Appear in ChatGPT search results and allow training | Allow both |
| Stay out of both | Disallow both and check your logs for ChatGPT-User |

A change to robots.txt can take about 24 hours to reach OAI-SearchBot, according to OpenAI.

## FAQ

### Does blocking GPTBot remove my shop from ChatGPT?
Not by itself. OpenAI describes OAI-SearchBot as the crawler for ChatGPT's search features and GPTBot as the training crawler, each set separately in robots.txt.

### Why does robots.txt look fine but GPTBot still gets a 403?
robots.txt is a request to the crawler. A CDN, firewall or server rule can refuse the request anyway, so check those layers with the two-request test and your logs.

### Does ChatGPT-User obey robots.txt?
OpenAI says robots.txt rules may not apply to ChatGPT-User, because a person starts those requests.

### Will unblocking GPTBot get my shop recommended?
No. Being readable is the entry ticket. Whether an assistant names your shop depends on what it finds about your category, which the CitedBy audit measures with real buyer questions.

## Sources

- [OpenAI: crawlers and user agents, IP ranges](https://developers.openai.com/api/docs/bots)
- [Cloudflare: manage AI crawlers](https://developers.cloudflare.com/ai-crawl-control/features/manage-ai-crawlers/)
- [Help Net Security: Cloudflare changes AI crawler access rules, 2 July 2026](https://www.helpnetsecurity.com/2026/07/02/cloudflare-ai-crawler-controls/)
- [IETF RFC 9309: Robots Exclusion Protocol](https://www.rfc-editor.org/info/rfc9309/)
- [CitedBy site audit](https://citedby.eu/)
