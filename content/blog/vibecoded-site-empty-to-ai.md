title: Lovable, Bolt or React site empty to AI? Check and fix
h1: My Lovable, Bolt or React site looks empty to AI. How to check it and fix it
description: Many AI crawlers do not run JavaScript, so a client-rendered site can look empty to them. A 30-second test, what Lovable says, and the fixes by setup.
slug: vibecoded-site-empty-to-ai
locale: en
cluster: Crawlability
date: 2026-10-18
reviewed: 2026-10-18
hero: vibecoded-site-empty-to-ai-hero.svg
hero_alt: Title card: a vibe-coded site is full in a browser but shows only an empty div to a crawler that skips JavaScript
og: vibecoded-site-empty-to-ai-og.png
widget: on
howto: on
related: /blog/can-chatgpt-read-my-website|Can ChatGPT read my website?; /blog/is-gptbot-blocked|Is GPTBot blocked on my site?; /sample-audit|A sample mini-audit
answer: AI crawlers read the HTML your server sends and, according to Vercel's analysis, do not run JavaScript. A site built in the browser can look empty to them even when it looks perfect to you. Test it by viewing the page source, then switch to server rendering or prerendering if your text is missing.

## Why a site that looks fine can be empty to AI

A site made with an AI app builder is often a single-page app. The server sends a near-empty HTML shell, and JavaScript builds the headline, price and buttons in your browser. A visitor never notices. A crawler that does not run the script receives the shell and nothing else.

Vercel analysed AI crawler traffic across its network and reported that none of the major AI crawlers it looked at render JavaScript. It names OpenAI (OAI-SearchBot, ChatGPT-User, GPTBot), Anthropic (ClaudeBot), Perplexity (PerplexityBot), Meta and ByteDance. It also reports that ChatGPT's and Claude's crawlers fetch JavaScript files (11.5% and 23.84% of their requests) without executing them, while Gemini uses Googlebot's infrastructure and can render JavaScript ([Vercel: the rise of the AI crawler](https://vercel.com/blog/the-rise-of-the-ai-crawler)). That is one company's measurement from its own network, and crawler behaviour can change, so test your own site instead of assuming.

![Two paths compared: with client-side rendering the server sends an empty shell and the crawler reads nothing, with server-side rendering or prerendering the server sends the finished page and every crawler reads the content](/blog/img/spa-vs-ssr.svg "What a crawler without JavaScript receives, in both setups.")

## The 30-second test

1. Open your homepage in a browser, right click and choose View page source (not Inspect, which shows the page after scripts ran).
2. Search the source for your main headline and one price or product name.
3. If you find them in the text, crawlers can read them. If you find only a `<div id="root"></div>` and script tags, the page is empty to a crawler that skips JavaScript.
4. Run the free check in the box above. It fetches your page with a plain request, without running scripts, and counts the readable words in the HTML.

For a command-line version, `curl -s https://yourshop.com/ | head -c 3000` prints the start of what a crawler gets.

## What Lovable says

Lovable's FAQ says new apps created from 13 May 2026 (22 June 2026 for Enterprise workspaces) use TanStack Start, which renders pages on the server, and that older apps use React with Vite and render in the browser. For those older apps it says Lovable serves pre-rendered copies of published pages to verified search engines, social preview bots and AI crawlers ([Lovable FAQ](https://docs.lovable.dev/introduction/faq)). So a Lovable site may be readable even if it is client-rendered, but that depends on how and where it is published. A custom setup or a copy exported to another host does not inherit it. Check the source on your live address, not on the builder's preview.

We found no equivalent statement from Bolt or other builders, so we make no claim about them. Run the test on each site.

## Fixes by setup

| Your setup | Fix | Check afterwards |
| --- | --- | --- |
| New Lovable app (TanStack Start) | Nothing to switch, rendering is on the server | View source on the live address |
| Older Lovable app (React + Vite) | Confirm the live address returns the text, and read Lovable's rendering notes for options | View source, and the free check |
| React + Vite you host yourself | Move critical pages to server rendering or prerender them at build time | View source on each key page |
| Next.js | Pages and layouts are Server Components by default, which render on the server ([Next.js docs](https://nextjs.org/docs/app/getting-started/server-and-client-components)). Keep price and description out of client-only components | View source |
| Other builder | Ask the vendor how published pages are rendered, then test | View source |

Whatever you choose, the pages that matter are the ones a buyer would ask about: home, category, product, shipping and returns. Put price, availability and a short description in the server-sent HTML and keep scripts for interaction only.

## Two other things to check at the same time

- Product data: the price and name should also appear as `Product` JSON-LD in the server HTML, not injected later.
- Blocks: a site can be readable and still be refused. See [Is GPTBot blocked on my site?](/blog/is-gptbot-blocked).

## FAQ

### Does ChatGPT run JavaScript on my site?
Vercel's analysis found that none of the major AI crawlers, including OpenAI's, render JavaScript. Test your own page with View page source, since behaviour can change.

### How do I know if my site is client-side rendered?
View the page source. If your headline and price are not in it, and you see an empty root div with script tags, the page is built in the browser.

### Is a Lovable site always empty to AI?
No. Lovable says new apps render on the server and that older apps get pre-rendered copies served to verified crawlers. Check the live address to be sure.

### Does Google see my client-rendered site?
Vercel reports Gemini uses Googlebot's infrastructure and can render JavaScript. Other assistants may still read nothing, so server rendering helps with all of them.

## Sources

- [Vercel: the rise of the AI crawler](https://vercel.com/blog/the-rise-of-the-ai-crawler)
- [Lovable FAQ: rendering and SEO](https://docs.lovable.dev/introduction/faq)
- [Next.js: Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)
- [CitedBy free check, method note](https://citedby.eu/check)
