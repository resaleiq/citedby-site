title: Wix: block AI crawlers in the Robots.txt Editor (four names)
slug: wix
description: Wix's help page tells you to paste four user agents into the Robots.txt Editor. Where the editor is, what the example leaves out and the nosnippet option.
section: platforms
locale: en
cluster: AI crawlers by platform
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Four facts about Wix: Where Robots.txt Editor, Example names 4, Page-level nosnippet tag, Support Not for edits
hero_sub: AI crawler settings on Wix
hero_boxes: Where|Robots.txt Editor; Example names|4; Page-level|nosnippet tag; Support|Not for edits
widget: on
related: /platforms|All platforms compared; /platforms/webflow|Webflow; /bots|AI crawlers compared; /guides/cms|AI visibility checklist for Shopify, WooCommerce and more
answer: Wix lets you edit robots.txt: SEO & GEO in the dashboard, then Tools and settings, then Robots.txt Editor. Its help page pastes four names to block: CCBot, GPTBot, ChatGPT-User and BingAI. ClaudeBot, PerplexityBot and Google-Extended are not in that example, so add them yourself if you want them blocked.

## Where the setting is on Wix

In your site's dashboard go to SEO & GEO, scroll to Tools and settings, click Robots.txt Editor, then View File. Wix's separate editing guide calls this an advanced feature and says Wix Customer Care cannot help with changes you make to the file.

## The example blocks four names, and one of them is not on Bing's list

Wix's help page says its list "includes some known AI crawlers, but you can always add more". The four it prints are CCBot, GPTBot, ChatGPT-User and BingAI. It leaves out the Anthropic, Perplexity, Google and Meta tokens that appear on our other pages. "BingAI" is the odd one: Microsoft's page on which crawlers Bing uses, read the same day, lists Bingbot, AdIdxBot, BingPreview, MicrosoftPreview and BingVideoPreview and no BingAI. A rule for a name that no crawler uses does nothing, so treat Wix's list as a starting point and check it against each vendor's own page. Also note [ChatGPT-User](/bots/chatgpt-user) is the fetcher that opens a page for a person asking ChatGPT, so blocking it removes that route to your pages.

In the vendor's words: “This list includes some known AI crawlers, but you can always add more as needed.”

Source: [Wix Help Center: Blocking AI Crawlers from Your Site](https://support.wix.com/en/article/blocking-ai-crawlers-from-your-site), read on 21 October 2026.

## The steps

1. Go to SEO & GEO in your site's dashboard.
2. Scroll to Tools and settings and click Robots.txt Editor.
3. Click View File, then click the field under Your robots.txt file.
4. Add the directives under This is your current file, then Save Changes and Save.
5. For one page only, open the page's SEO basics, Advanced SEO, Robots meta tag, and tick nosnippet. Wix says this prevents the content being used as direct input for AI overviews.

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
User-agent: CCBot
Disallow: /

User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /
```

## Gotchas

Wix's FAQ says blocking AI crawlers in robots.txt may limit NLWeb functionality, because AI agents need access to your structured content. It also says some crawlers ignore robots.txt, so a block is not airtight.

## Compare with Webflow

[Webflow](/platforms/webflow): Also a robots.txt editor, plus a Content-Signal header.

## Check your own site

The free check in the box above reads robots.txt for the AI crawlers and sends one live request per crawler, so a rule that your platform's settings allow but a firewall refuses shows up. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Will blocking AI crawlers hurt my Wix SEO?

Wix says blocking specific AI crawlers should not significantly affect SEO, and recommends checking your analytics afterwards.

### Is BingAI a real crawler?

It is not on Microsoft's current list of Bing crawlers, which names Bingbot, AdIdxBot, BingPreview, MicrosoftPreview and BingVideoPreview. See the [Bingbot page](/bots/bingbot).

### Does nosnippet block AI crawlers?

Wix describes it as preventing your content being used as a direct input for AI overviews. It is a page-level tag, not a crawler block.

## Sources

- [Wix Help Center: Blocking AI Crawlers from Your Site](https://support.wix.com/en/article/blocking-ai-crawlers-from-your-site), read 21 October 2026
- [Wix Help Center: Editing Your Site's Robots.txt File](https://support.wix.com/en/article/editing-your-sites-robotstxt-file), read 21 October 2026
- [Microsoft Bing Webmaster help: Which Crawlers Does Bing Use?](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0), read 21 October 2026
