title: Vercel: the AI Bots ruleset in the Firewall (Log or Deny)
slug: vercel
description: Vercel blocks AI bots with a Firewall ruleset, not a robots.txt line. Where the AI Bots Ruleset is, the Log and Deny actions, and its self-updating bot list.
section: platforms
locale: en
cluster: AI crawlers by platform
date: 2026-10-24
reviewed: 2026-10-24
hero: auto
hero_alt: Four facts about Vercel: Where Firewall, Rules, Plans All plans, Default Allow (inactive), Actions Log or Deny
hero_sub: AI crawler settings on Vercel
hero_boxes: Where|Firewall, Rules; Plans|All plans; Default|Allow (inactive); Actions|Log or Deny
widget: on
related: /platforms|All platforms compared; /platforms/cloudflare|Cloudflare; /bots|AI crawlers compared; /guides/cms|AI visibility checklist for Shopify, WooCommerce and more
answer: Vercel handles AI bots with a Firewall ruleset, not a robots.txt line. In your project open Firewall, then Rules, and set the AI Bots Ruleset to Log or Deny. It is available on all plans and starts inactive, shown as Allow, so nothing is blocked until you change it.

## Where the setting is on Vercel

From your project's dashboard, open Firewall in the sidebar, then Rules. In the Bot Management section you will find the AI Bots Ruleset rule. Vercel's docs say the ruleset is available on all plans.

## The one thing Vercel's page says that the other platforms do not

Vercel's list of AI bots is not yours to maintain. The ruleset covers AI bots that crawl for training data, search purposes or user-generated fetches, and Vercel keeps the list current. The same page says the ruleset is inactive by default and labelled Allow in the dashboard, so matching traffic is not evaluated and reaches your application. The control is one action for the whole ruleset, Log or Deny, applied at the Firewall.

In the vendor's words: “When new AI bots emerge, Vercel automatically adds them to its managed list and handles them according to your existing configured action without requiring any changes on your part.”

Source: [Vercel Docs: Bot Management](https://vercel.com/docs/bot-management), read on 24 October 2026.

## The steps

1. From your project's dashboard, open Firewall in the sidebar.
2. Open Rules in the sidebar.
3. In the Bot Management section, select Log or Deny on the AI Bots Ruleset rule. Log records AI bot traffic without blocking it and is useful for monitoring. Deny blocks all traffic identified as coming from AI bots.
4. When you make a change, a Review Changes button appears with the number of changes. Select Review Changes, check them, then select Publish to apply the changes to your production deployment.

## The lines to use

Vercel's pages describe this as a Firewall setting, so there is no robots.txt line to add. The two states are:

To allow:

```
AI Bots Ruleset: Allow (the default, ruleset inactive)
```

To block:

```
AI Bots Ruleset: Deny
```

## Gotchas

Deny blocks all traffic identified as coming from AI bots, and the ruleset's scope is training, search and user-generated fetches together, so it is not a way to block training bots while keeping search bots. Log is the safer first step. Vercel's page does not say how the ruleset relates to your robots.txt, so check what your own file says separately. For individual bots, the same page says you can block some or all of the bots in its verified bots directory with WAF custom rules that use the User Agent match condition or the Signature-Agent header.

## Compare with Cloudflare

[Cloudflare](/platforms/cloudflare): Also a network-level switch, with three actions for each of Search, Agent and Training.

## Check your own site

The free check in the box above reads robots.txt for the AI crawlers and sends one live request per crawler, so a rule that your platform's settings allow but a firewall refuses shows up. The full list of crawlers is on [the AI crawler hub](/bots).

## FAQ

### Does Vercel block AI bots by default?

No. Vercel's docs say the AI Bots Ruleset is inactive by default, labelled Allow in the dashboard, and that matching traffic is not evaluated and reaches your application.

### Do I have to keep Vercel's list of AI bots up to date?

No. Vercel says the list of known AI bots is automatically maintained and updated by Vercel, and that new bots are handled according to the action you have already set.

## Sources

- [Vercel Docs: Bot Management](https://vercel.com/docs/bot-management), read 24 October 2026
- [Vercel Docs: WAF Managed Rulesets](https://vercel.com/docs/vercel-firewall/vercel-waf/managed-rulesets), read 24 October 2026
