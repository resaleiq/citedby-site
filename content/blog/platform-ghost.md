title: Ghost: add robots.txt to your theme to allow or block AI crawlers
slug: ghost
description: Ghost has no robots.txt setting in the admin. Its help says to save a robots.txt in your theme's root, which replaces the default. Plan needed on Ghost(Pro).
section: platforms
locale: en
cluster: AI crawlers by platform
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about Ghost: Where Theme root, File robots.txt, Effect Replaces default, Ghost(Pro) Creator plan or higher
hero_sub: AI crawler settings on Ghost
hero_boxes: Where|Theme root; File|robots.txt; Effect|Replaces default; Ghost(Pro)|Creator or higher
widget: on
related: /platforms|All platforms compared; /platforms/wordpress-com|WordPress.com; /bots|AI crawlers compared; /guides/cms|AI visibility checklist for Shopify, WooCommerce and more
answer: Ghost serves a default robots.txt. To change it, save your own robots.txt at the root of your theme, then install and activate the new theme version. Ghost's help page says custom themes on Ghost(Pro) need the Creator plan or higher, so your plan decides whether you can edit it.

## Where the setting is on Ghost

There is no robots.txt field in the admin. Ghost's help page says the file lives inside your site's theme: write your robots.txt and save it to the root of the theme. Ghost's theme documentation says the same in one line: themes can include a robots.txt which overrides the default robots.txt provided by Ghost.

## The one thing Ghost's page says that the other platforms do not

On Ghost the file travels with the theme, so the plan you are on decides whether you can change it. Ghost's help page says it requires you to be comfortable writing your own robots.txt and installing a new version of your theme. It then adds a plan limit for Ghost(Pro), Ghost's hosted service: installing a custom theme requires the Creator plan or higher. The page describes what happens next in these terms.

In the vendor's words: “Once the new version of the theme is installed and activated, the theme's robots.txt will be used in place of Ghost's default robots.txt.”

Source: [Ghost Help: Modifying robots.txt](https://ghost.org/help/modifying-robots-txt/), read on 24 October 2026.

## The steps

1. Write your robots.txt file.
2. Save it to the root of your theme.
3. Install the new version of the theme, then activate it. Ghost says the theme's robots.txt is used in place of its default once the new version is installed and activated.
4. On Ghost(Pro), check your plan first: Ghost says installing a custom theme requires the Creator plan or higher.

## The lines to use

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

## Gotchas

The theme's file is used in place of Ghost's default, not added to it. Ghost's pages do not say what the default contains, so open yoursite.com/robots.txt before you replace it and copy across any lines you want to keep, such as a sitemap line. The page also warns that this route needs you to be comfortable writing the file yourself, and it does not cover AI crawlers by name.

## Compare with WordPress.com

[WordPress.com](/platforms/wordpress-com): Its AI opt-out is a sharing setting, not a file you write.

## Check your own site

The free check in the box above reads robots.txt for the AI crawlers and sends one live request per crawler, so a rule that your platform's settings allow but a firewall refuses shows up. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Where do I put a custom robots.txt on Ghost?

At the root of your theme. Ghost's help page says that once the new theme version is installed and activated, the theme's robots.txt is used in place of Ghost's default.

### Do I need a paid plan to edit robots.txt on Ghost(Pro)?

Ghost's page says installing a custom theme on Ghost(Pro) requires a subscription to the Creator plan or higher. Because the file is part of the theme, that applies to a custom robots.txt too.

## Sources

- [Ghost Help: Modifying robots.txt](https://ghost.org/help/modifying-robots-txt/), read 24 October 2026
- [Ghost Docs: Theme structure](https://docs.ghost.org/themes/structure), read 24 October 2026
