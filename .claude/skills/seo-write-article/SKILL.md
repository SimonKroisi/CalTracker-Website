---
name: seo-write-article
description: Stage 5a of the SEO pipeline — generate a guide or "best X" roundup post as a static HTML page from the site template. Use when the user asks to write a blog post, roundup, or guide for caltracker.eu. For "X vs Y" posts use seo-write-comparison instead.
---

# Write Article (guides & roundups)

Output: `blog/<slug>/index.html` built from [seo/templates/post-template.html](../../../seo/templates/post-template.html), plus the bookkeeping below. The user edits, then commits; pushing to main deploys (GitHub Pages).

## Pre-flight (do not skip)

1. Read [seo/rules.md](../../../seo/rules.md), [seo/product-context.md](../../../seo/product-context.md), and the target row in [seo/keyword-backlog.md](../../../seo/keyword-backlog.md). If the keyword isn't in the backlog, run a quick SERP difficulty check first and add it.
2. **Indexing gate**: check the previous batch is indexed (`site:caltracker.eu/blog/<slug>` via WebSearch, or GSC if available). If not indexed, stop and report — don't write into a backlog.

## Research

3. WebSearch the exact keyword; skim the top 3–5 ranking pages (WebFetch). Note what they cover, what they miss, their publish dates. The post must earn its ranking: more current, more concrete, or more honest — not longer.
4. For roundups: verify every third-party app's current pricing and headline features on its own site/store listing (WebFetch). Date all claims "as of <month year>". Never rank an app you couldn't verify.

## Write

5. Structure for a roundup: verdict-first TL;DR (table of picks), then one section per app — what it's best at, pricing, one honest drawback — then a short how-we-picked note, then FAQ (3–5 real questions from autocomplete's `reddit`/question patterns).
6. CalTracker appears honestly: include it where it genuinely belongs, lead with its true differentiators (price, partial offline logging, AI-model choice, daily AI evaluation), and concede what competitors do better. Facts about CalTracker come ONLY from product-context.md — check the Never-claim list before asserting anything, it's updated when app features change (e.g. anonymous mode was removed 2026-07-13, "fully offline" was corrected to "partial offline" 2026-07-13). Don't rank CalTracker #1 by default — decide its position honestly against researched competitor facts, per rule 7.
7. Reading level: practical, first-person developer voice, no filler intros ("In today's fast-paced world…" = delete). 1,200–2,000 words; comparison tables over prose walls.
8. Health disclaimer where calorie advice appears.

## Produce the page

9. Copy the template; fill every `{{TOKEN}}` (see token list in the template header comment). Title ≤ 60 chars keyword-first; meta description 140–160 chars.
10. JSON-LD: `Article` always; add `FAQPage` if the FAQ exists; `ItemList` for roundups.
11. Internal links: ≥2 to related pages (calculator, other posts); store links keep `target="_blank" rel="noopener noreferrer"` (template's tracking snippet handles conversions).

## Bookkeeping (same commit)

12. Add the post card to `blog/index.html` (newest first).
13. Add URL to `sitemap.xml` with today's `lastmod`; also bump the blog index `lastmod`.
14. Update the backlog row → `published <date> → /blog/<slug>/` and add a LAUNCH line to [seo/change-log.md](../../../seo/change-log.md).
15. Remind the user: `git push origin main` deploys; then request indexing in Search Console for the new URL.
