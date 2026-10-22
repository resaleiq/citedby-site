title: Webflow: robots.txt rules and the Content-Signal header for AI
slug: webflow
description: Where Webflow's robots.txt editor is, which plan it needs and how its Content-Signal header separates AI training, search and AI input.
section: platforms
locale: en
cluster: AI crawlers by platform
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Four facts about Webflow: Where Site settings, SEO, Needs Site or paid Workspace, Extra Content-Signal, Status Proposed extension
hero_sub: AI crawler settings on Webflow
hero_boxes: Where|Site settings, SEO; Needs|Site or paid Workspace; Extra|Content-Signal; Status|Proposed extension
widget: on
related: /platforms|All platforms compared; /platforms/wix|Wix; /bots|AI crawlers compared; /guides/cms|AI visibility checklist for Shopify, WooCommerce and more
answer: Webflow puts robots.txt in Site settings, then SEO, then Indexing, and one of its help pages says you need a Site plan or a paid Workspace plan. It can also send a Content-Signal header that sets ai-train, search and ai-input separately. Webflow calls that a proposed extension, not an accepted standard.

## Where the setting is on Webflow

Go to Site settings, then SEO, then Indexing, add the robots.txt rule or rules you want, then click Save and publish your site. Webflow adds a sitemap line by default; a toggle removes it.

## A header that splits training, search and AI answers

Besides robots.txt, Webflow's page says a site can serve a Content-Signal HTTP header, set in the same Indexing area, to give AI crawlers more granular instructions. Its example is `Content-Signal: ai-train=no, search=yes, ai-input=no`. Webflow explains the split: robots.txt controls whether bots can access your pages, while Content-Signal says whether content can be used for AI training, search indexing, or AI-generated responses, separately. Webflow adds the caveat itself: this is based on a proposed extension to RFC 9309 and is not yet an accepted standard. So it states a preference; it does not stop a crawler, and Webflow's page does not say which crawlers read it.

In the vendor's words: “This is based on a proposed extension to RFC 9309 and is not yet an accepted standard.”

Source: [Webflow Help: Set robots.txt rules](https://help.webflow.com/hc/en-us/articles/41954080897683-Set-robots-txt-rules), read on 21 October 2026.

## The steps

1. Open Site settings and go to SEO, then Indexing.
2. Type the robots.txt rules you want in the rules field.
3. Optionally set the Content-Signal header in the same area.
4. Click Save and publish your site, then open yourdomain.com/robots.txt to check the live file.

## The lines to use

To allow:

```
User-agent: OAI-SearchBot
Allow: /

User-agent: *
Allow: /
```

To block:

```
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

Content-Signal: ai-train=no, search=yes, ai-input=no
```

## Gotchas

Webflow's page says your robots.txt is publicly visible, so do not rely on it to hide private pages, and that not all bots follow it.

## Compare with Wix

[Wix](/platforms/wix): A longer editing path and a four-name example.

## Check your own site

The free check in the box above reads robots.txt for the AI crawlers and sends one live request per crawler, so a rule that your platform's settings allow but a firewall refuses shows up. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Do I need a paid plan for robots.txt on Webflow?

One Webflow help page says you need a Site plan or a paid Workspace plan to add a robots.txt file to your site.

### What is Content-Signal?

A proposed extension to RFC 9309 that Webflow can send as a header: ai-train, search and ai-input, each set to yes or no.

### Does Webflow block bad bots for me?

Its help page shows how to write a rule for a named bot. It says some bots, especially malicious ones, do not follow robots.txt.

## Sources

- [Webflow Help: Set robots.txt rules](https://help.webflow.com/hc/en-us/articles/41954080897683-Set-robots-txt-rules), read 21 October 2026
- [Webflow Help: Request to block specific bots from visiting your site](https://help.webflow.com/hc/en-us/articles/41954183592851-Request-to-block-specific-bots-from-visiting-your-site), read 21 October 2026
