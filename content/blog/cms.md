title: AI visibility checklist for Shopify, WooCommerce and more
h1: AI visibility checklist for Shopify, WooCommerce and more
description: Where to find robots.txt, the sitemap and product data on Shopify, WordPress with WooCommerce and other shop platforms, and what to check for AI crawlers.
slug: cms
section: guides
locale: en
cluster: Guide
date: 2026-10-20
reviewed: 2026-10-20
hero: auto
hero_alt: Four checks to run on any shop platform: robots.txt, sitemap, product data in JSON-LD, and text that needs JavaScript
hero_sub: Where each setting lives on your platform
hero_boxes: Find robots.txt|Open it in a browser; Find the sitemap|List of products and pages; Check product data|JSON-LD in the source; Check theme text|Is it in the raw HTML
steps_img: on
widget: on
related: /guides/technical-seo-checklist|Technical SEO checklist for AI visibility; /blog/is-gptbot-blocked|Is GPTBot blocked on your site?; /blog/can-chatgpt-read-my-website|Can ChatGPT read my website?
answer: On any shop platform, check four things: robots.txt does not block AI crawlers, the sitemap lists your products, product pages carry price and availability as JSON-LD, and product text is in the raw HTML. Shopify and WordPress generate the first two for you. Our audit tests all four on every page, from €9.

## Which checks apply on every shop platform?

The same four questions apply whatever you sell on. Open `yourshop.com/robots.txt` and check that nothing blocks the crawlers you want. Open `yourshop.com/sitemap.xml` and check that products are listed. View the source of a product page and search for `application/ld+json` to see the product data. Then search the same source for a sentence from the product description. If it is missing, a script adds it after loading and many crawlers never see it.

The platform decides where you change each of these. The sections below say what the official help pages confirm and leave the rest to your own settings.

## How do I check AI crawler access on Shopify?

Shopify creates a default robots.txt for every store. Shopify's help page says the file sits at the root of your primary domain, and that you can customise it by adding a `robots.txt.liquid` template to your theme. It calls this an unsupported customisation that Shopify Support cannot help with, so ask a Shopify Partner or a developer if you are unsure ([Shopify: editing robots.txt.liquid](https://help.shopify.com/en/manual/promoting-marketing/seo/editing-robots-txt)).

The same page explains that robots.txt rules are advisory, and that blocking AI crawlers there affects only open-web discoverability. Product data sent through Shopify Catalog to agentic storefronts you have activated is not stopped by it.

## Where is the sitemap on Shopify and WordPress?

Shopify generates sitemap files automatically at `yourshop.com/sitemap.xml`. They link to separate sitemaps for products, collections, blogs and pages and update when you add content. Search engines cannot read the sitemap if the store is in private mode ([Shopify: find your sitemap](https://help.shopify.com/en/manual/promoting-marketing/seo/find-site-map)).

WordPress, which WooCommerce runs on, has exposed a sitemap index at `/wp-sitemap.xml` since version 5.5, and the robots.txt it serves references that index ([WordPress core announcement](https://make.wordpress.org/core/2020/07/22/new-xml-sitemaps-functionality-in-wordpress-5-5/)). An SEO plugin may replace it with its own sitemap address, so open both and see which one your site answers with.

## How do I check product data and text on my platform?

Shopify's guidance on product pages for AI systems asks for clear titles, price and availability shown prominently, detailed specifications, structured data and product attributes. It adds that detail meant only for AI systems can sit lower on the page ([Shopify: optimizing your store for AI](https://help.shopify.com/en/manual/promoting-marketing/seo/optimizing-store-for-ai)).

There is no official help page I could confirm that states exactly which structured data a given theme or plugin outputs on WooCommerce, Wix, Squarespace, PrestaShop or Magento. So check your own product page source. If `application/ld+json` is missing or shows the wrong price, look in your platform's settings or your SEO plugin for a structured data option, and compare the values against the page.

Text hidden behind tabs, accordions or "read more" buttons is fine if it is in the HTML. It is a problem if a theme or app loads it with JavaScript only after the page opens.

## Which platform setting is easiest to miss?

| Platform | Where to look | What to confirm |
| --- | --- | --- |
| Shopify | robots.txt.liquid in the theme code | Default file is intact or edits are deliberate |
| Shopify | Online store preferences | Store is not in private mode |
| WordPress with WooCommerce | `/wp-sitemap.xml` or your SEO plugin | One sitemap, listing products |
| Any platform | CDN or firewall rules | Crawlers are not refused by name |
| Any platform | Product page source | JSON-LD price matches the page |

## What does the audit check?

Platform dashboards show settings. A crawler sees the result. The [CitedBy audit](/) crawls your shop up to your plan's page limit, shows which AI crawlers it lets in and gives the exact fix for each issue. It starts at €9, paid once, with a 14-day money-back guarantee.

## FAQ

### Can I edit robots.txt on every platform?

No. On Shopify you can, through the `robots.txt.liquid` template. On other platforms it depends on the platform and plan, so look in your platform's settings or help pages.

### Does a sitemap plugin matter for AI assistants?

A sitemap helps crawlers find your pages, but assistants also need to be allowed in and to read the page. See the [technical SEO checklist](/guides/technical-seo-checklist).

### My theme loads descriptions with JavaScript. What now?

Ask the theme or app developer for a version that outputs the text in the HTML, or move the key facts into the standard product description field.

## Sources

- [Shopify: editing robots.txt.liquid](https://help.shopify.com/en/manual/promoting-marketing/seo/editing-robots-txt)
- [Shopify: finding and submitting your sitemap](https://help.shopify.com/en/manual/promoting-marketing/seo/find-site-map)
- [Shopify: optimizing your store for AI](https://help.shopify.com/en/manual/promoting-marketing/seo/optimizing-store-for-ai)
- [WordPress core: XML sitemaps in 5.5](https://make.wordpress.org/core/2020/07/22/new-xml-sitemaps-functionality-in-wordpress-5-5/)
