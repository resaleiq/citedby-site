title: How to create an llms.txt file: 6 steps and a template (2026)
h1: How to create an llms.txt file, step by step
description: Write an llms.txt in six steps with a copy-paste template that follows the llmstxt.org format, publish it at your site root and check it with a free tool.
slug: how-to-create-an-llms-txt-file
locale: en
cluster: AI visibility basics
date: 2026-10-21
reviewed: 2026-10-21
hero: auto
hero_alt: Title card: how to create an llms.txt file, with four parts of the file: title, summary, link sections, optional section
hero_sub: A # title, a > summary, ## link lists, then a free check
hero_boxes: # Title|the only required line;> Summary|what the site is;## Sections|lists of links;## Optional|links to skip
widget: off
howto: on
related: /tools/llms-txt-checker|llms.txt checker (free); /blog/does-llms-txt-work|Does llms.txt work?; /tools/ai-crawler-check|AI-crawler access checker (free); /blog/can-chatgpt-read-my-website|Can ChatGPT read my website?
answer: To create an llms.txt file, write a plain-text Markdown file with a # title, a short > summary and ## sections that list your key pages as [name](url): note links, save it as llms.txt and upload it to your site root so it loads at yourshop.com/llms.txt. Then run the free checker to confirm it loads and its links work.

## What llms.txt is

llms.txt is a proposal published at [llmstxt.org](https://llmstxt.org/): a Markdown file at the root of your site that gives language-model assistants a short map of the pages that matter most. It is not a standard that any search engine or assistant has committed to read. [Does llms.txt work?](/blog/does-llms-txt-work) covers what the studies found. The file is cheap to write, and writing it makes you decide which of your pages answer buyers' questions.

## The format, in order

The llmstxt.org specification lists these parts in this order. Only the first is required.

- A `#` title with the name of the site or project.
- A `>` blockquote with a short summary.
- Optional paragraphs or lists with more detail, but no headings.
- Zero or more `##` sections, each holding a list of links.
- By convention, a section named `Optional` for links an assistant can skip when it needs shorter context.

Each list item is a Markdown link, then optionally a colon and a note: `- [Link title](https://link_url): what this page answers`.

## Template to copy

Replace the example text with your own. Keep the shape.

```
# Example Shop
> Example Shop sells handmade leather bags and ships across the EU.

## Products
- [Leather bags](https://example.com/bags): all models with prices and sizes
- [Care guide](https://example.com/care): how to clean and store a bag

## Policies
- [Shipping and returns](https://example.com/shipping): delivery times and the 30-day return rule

## Optional
- [About us](https://example.com/about)
```

## How to create the file

1. Open a plain-text editor and type the title line: `# Your shop name`. Keep it to the name buyers know you by.
2. Add one `>` line under it that says what you sell and where, in one sentence. Use facts a page of yours also states.
3. List your most useful pages under `##` headings such as Products, Help or Policies. Use full URLs, one link per line, and add a short note after a colon saying what the page answers.
4. Put pages that are nice to have, such as About or press, under a section named `Optional`.
5. Save the file as `llms.txt` (plain text, UTF-8) and upload it to the root of your site so that `https://yourshop.com/llms.txt` loads. A file in a subfolder does not count, and the address must answer with text, not a login or an HTML error page.
6. Run the [free llms.txt checker](/tools/llms-txt-checker) on your domain. It reports whether the file loads, follows the format, links to pages that load, and agrees with your robots.txt and sitemap.

## Mistakes the checker finds

- The title is missing or is not the first line.
- A list item is not in `[name](url)` form, for example a bare URL.
- A listed page returns an error, or robots.txt keeps AI crawlers away from it. A page you list but block sends mixed signals.
- A listed page is not in your sitemap.
- The address returns an HTML page instead of a text file.

## Check the crawlers too

A perfect llms.txt does nothing for a site whose firewall refuses AI crawlers. Run the [AI-crawler access checker](/tools/ai-crawler-check) next: it tests robots.txt and a live request for eight crawlers.

## FAQ

### Where does llms.txt go?
At the root of the domain: `https://yourshop.com/llms.txt`. Not in a subfolder.

### Do I have to list every page?
No. List the pages that best answer buyers' questions. A short, accurate file is better than a long list of everything.

### Do ChatGPT, Gemini or Perplexity read llms.txt?
No major assistant has confirmed that it does. Treat the file as a cheap addition, not as a way to get cited.

### What is llms-full.txt?
An optional second file some sites publish with the full text of key pages in one document. The checker only reports whether it exists.

### How do I know the file is valid?
Run the free [llms.txt checker](/tools/llms-txt-checker) on your domain.

## Sources

- [llmstxt.org: the /llms.txt file proposal](https://llmstxt.org/)
