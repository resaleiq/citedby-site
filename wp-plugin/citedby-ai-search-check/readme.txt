=== CitedBy AI-Search Check ===
Contributors: citedby
Tags: seo, robots-txt, sitemap, llms-txt, crawlers
Requires at least: 5.8
Tested up to: 6.8
Requires PHP: 7.4
Stable tag: 0.1.0
License: GPLv2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html

One button in wp-admin shows whether AI-search crawlers can read your site: robots.txt, llms.txt, sitemap and a free page check.

== Description ==

AI assistants such as ChatGPT, Perplexity, Claude and Copilot send their own crawlers to read websites. If your robots.txt, a security plugin or a firewall turns them away, your site cannot be quoted in answers.

Open **Tools > AI-Search Check** and press the button. The plugin shows:

* Whether WordPress itself asks search engines to stay away (Settings > Reading).
* Whether robots.txt closes your whole site to ten named crawlers: OAI-SearchBot, GPTBot, ChatGPT-User, PerplexityBot, ClaudeBot, Claude-SearchBot, Google-Extended, Applebot-Extended, CCBot and Bingbot.
* Whether you have a sitemap and an llms.txt.
* A page check run from outside by citedby.eu: is your home page text in the HTML a crawler receives, and does it carry Organization structured data.

Then it links to the full CitedBy audit, which crawls up to your plan's page limit and gives you the exact fix per page.

= What the plugin does not do =

* It does not change any setting, file or content on your site.
* It does not add anything to your visitors' pages. No front-end code, no cookies, no tracking.
* It sends nothing until you press the button, and it stores nothing in your database.

== External service ==

The plugin calls one external service, CitedBy (citedby.eu), only when an administrator presses "Run the check".

* What is sent: your home page address (`home_url()`), your admin language (en, fr or nl) and the tag `wp-plugin` so we can count how many checks come from this plugin. Standard request data (your server's IP address) is received by any web service. The IP address is used to rate-limit and is not stored with your site address.
* What comes back: the page check result shown on screen.
* When: each press of the button.
* Service: https://citedby.eu. Terms: https://citedby.eu/terms. Privacy policy: https://citedby.eu/privacy.

The link "Get the full audit" opens citedby.eu in a new tab with `source=wp-plugin` in the address. It is a normal link; nothing is sent unless you click it.

== Installation ==

1. Upload the `citedby-ai-search-check` folder to `/wp-content/plugins/`, or install it from Plugins > Add New.
2. Activate the plugin.
3. Open Tools > AI-Search Check and press "Run the check".

== Frequently Asked Questions ==

= Does it block or allow crawlers for me? =

No. It reports. You change robots.txt yourself, or the full audit tells you the exact line.

= Why is a crawler shown as not blocked when my firewall blocks it? =

The local part reads robots.txt only. A firewall or CDN rule is not visible from inside WordPress. The outside check shows what citedby.eu receives.

= Do I need an account? =

No. The check is free and anonymous.

== Changelog ==

= 0.1.0 =
* First release.
