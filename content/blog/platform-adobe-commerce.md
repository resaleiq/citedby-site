title: Adobe Commerce: robots.txt is in Content, Design, Configuration
slug: adobe-commerce
description: Adobe Commerce edits robots.txt in the Admin under Search Engine Robots. Cloud projects add pub/media steps, and Adobe's pages name no AI crawler.
section: platforms
locale: en
cluster: AI crawlers by platform
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about Adobe Commerce: Where Content, Design, Configuration, Section Search Engine Robots, Cloud Extra steps, AI names Not listed
hero_sub: AI crawler settings on Adobe Commerce
hero_boxes: Where|Content > Design > Configuration; Section|Search Engine Robots; Cloud|Extra steps; AI names|Not listed
widget: on
related: /platforms|All platforms compared; /platforms/shopify|Shopify; /bots|AI crawlers compared; /guides/cms|AI visibility checklist for Shopify, WooCommerce and more
answer: In Adobe Commerce you edit robots.txt in the Admin: Content, Design, Configuration, the Global row, then Search Engine Robots and the custom instruction box. Adobe's pages speak of web crawlers and bots in general and name no AI crawler, so any AI user agents are yours to add. Cloud projects have extra file-path steps.

## Where the setting is on Adobe Commerce

On the Admin sidebar go to Content, then Design, then Configuration. Adobe's SEO overview says to find the Global configuration in the first row of the grid, click Edit, and expand the Search Engine Robots section. The Edit Custom instruction of robots.txt file box is there, with a Reset to Default button.

## The one thing Adobe Commerce's pages say that the other platforms do not

On Adobe Commerce on cloud infrastructure the robots.txt file has a location problem that the other platforms do not have. Adobe's implementation playbook says to add the content in the Admin, but the file system is read-only, so the file has to live under pub/media and a custom Fastly VCL snippet redirects /robots.txt there. For several sites in one project, the playbook names the files per site, for example domainone_robots.txt. For on-premises installs it says to write the files to /path/to/commerce/pub/media/ or /path/to/commerce/media, whichever is right for your installation.

In the vendor's words: “Due to the read-only file system on Adobe Commerce on cloud infrastructure projects, you must specify the pub/media path before generating the file.”

Source: [Adobe Commerce Implementation Playbook: Best practices for configuring web crawlers](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/launch/robots-txt), read on 24 October 2026.

## The steps

1. On the Admin sidebar go to Content, then Design, then Configuration.
2. Find the Global configuration in the first row of the grid and click Edit.
3. Scroll down and expand Search Engine Robots.
4. Set Default Robots to INDEX, FOLLOW, NOINDEX, FOLLOW, INDEX, NOFOLLOW or NOINDEX, NOFOLLOW. Adobe describes these as instructions to crawlers about indexing and following links.
5. If needed, enter your own rules in the Edit Custom instruction of robots.txt file box. Reset to Default restores Adobe's instructions.
6. Click Save Configuration, then open your store's /robots.txt to see the result. Adobe's playbook tips that you can view the auto-generated file there.

## The lines to use

Adobe's own examples use User-agent: * for all crawlers. To allow or block one named crawler, add a group for its name:

To allow:

```
User-agent: OAI-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /
```

To block:

```
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /
```

Adobe's pages do not say whether text you type is added to or replaces its default instructions. Save, then read /robots.txt to confirm what is served.

## Gotchas

Adobe's playbook says not to expose your Admin path in robots.txt, because that is a vulnerability for site hacking and potential loss of data, and to remove it. Adobe's default instructions start with User-agent: * and a list of Disallow lines such as /checkout/ and /catalog/, so check what you keep. On cloud, a knowledge base article dated 18 August 2026 says robots.txt content is generated from Admin configuration and stored in the database, with no physical file needed in that scenario, while the playbook describes the pub/media redirect. The two pages read differently, so confirm with Adobe Commerce Support which applies to your project. The playbook also says its advice covers the native Adobe Commerce storefront only, not headless or Adobe Experience Manager storefronts.

## Compare with Shopify

[Shopify](/platforms/shopify): A theme template instead of an Admin box, and Support will not fix edits to it.

## Check your own site

The free check in the box above reads robots.txt for the AI crawlers and sends one live request per crawler, so a rule that your platform's settings allow but a firewall refuses shows up. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Why does my custom robots.txt not change on Adobe Commerce cloud?

Adobe's knowledge base says the usual cause is that indexing by search engines is disabled, which stops custom robots.txt content being applied. Fix it in the Cloud Console or with the magento-cloud CLI restrict_robots setting. The article adds that Staging environments have indexing disabled by default and it cannot be enabled there.

### Does Adobe Commerce list AI crawlers for robots.txt?

Not in the pages we read. They talk about web crawlers and bots, and their examples use User-agent: * only. Add each AI user agent you want to allow or block as its own group.

## Sources

- [Adobe Commerce Implementation Playbook: Best practices for configuring web crawlers](https://experienceleague.adobe.com/en/docs/commerce-operations/implementation-playbook/best-practices/launch/robots-txt), read 24 October 2026
- [Adobe Commerce Admin guide: SEO overview](https://experienceleague.adobe.com/en/docs/commerce-admin/marketing/seo/seo-overview), read 24 October 2026
- [Adobe Commerce knowledge base: Resolve robots.txt not updating or displaying default settings](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/miscellaneous/robots-txt-not-updated-or-displaying-default-settings), read 24 October 2026
