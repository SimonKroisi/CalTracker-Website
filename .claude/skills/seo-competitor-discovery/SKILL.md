---
name: seo-competitor-discovery
description: Stage 2 of the SEO pipeline — find and classify competitors of the CalTracker app from live search results and "alternatives to X" queries, and update seo/competitors.md. Use when the user wants to refresh the competitor roster or asks who we compete with in search.
---

# Competitor Discovery

Goal: keep [seo/competitors.md](../../../seo/competitors.md) current. Read [seo/product-context.md](../../../seo/product-context.md) first so you know what CalTracker actually is.

## Process

1. **Search the space** with WebSearch (queries like):
   - `best calorie tracking apps 2026`
   - `best AI calorie counter app`
   - `<known competitor> alternatives` for each major name already in the roster
   - `calorie tracker app reddit` (forum threads surface apps media misses)
2. **Classify every recurring name** into exactly one of:
   - **App competitor** — an app users would install instead of CalTracker → comparison-post target.
   - **SEO competitor** — a site ranking for our keywords (indie app blogs, review sites) → difficulty benchmark and playbook intel, NOT a comparison target.
   - **Big media** — Fortune/Healthline/PCMag class → their presence in a SERP means pick a longer-tail variant.
3. **For new app competitors**, capture in one line: positioning, pricing ballpark (verify on their site with WebFetch, date it "as of <month year>"), and the content angle (what we'd concede, where we win — cross-check the differentiators in product-context.md).
4. **Update seo/competitors.md**: merge, don't duplicate; bump the "Last refreshed" date; note removals (dead/acquired apps) rather than silently deleting.
5. If discovery surfaced comparison-worthy pairs (autocomplete `X vs` patterns), append them to the Comparisons section of [seo/keyword-backlog.md](../../../seo/keyword-backlog.md) as `idea`.

## Rules

- Follow [seo/rules.md](../../../seo/rules.md). Never copy an SEO competitor's programmatic /compare/ factory pattern.
- FatSecret is both a competitor and our food-database supplier — flag that in any content plan touching it.
