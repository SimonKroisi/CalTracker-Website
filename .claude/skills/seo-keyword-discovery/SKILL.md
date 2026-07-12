---
name: seo-keyword-discovery
description: Stage 4 of the SEO pipeline — expand seed keywords through Google autocomplete, judge difficulty by reading the live SERP, cross-reference Search Console data, and append scored ideas to seo/keyword-backlog.md. Use when the user wants new keyword ideas or asks what to write next.
---

# Keyword Discovery

Goal: append scored, honest keyword rows to [seo/keyword-backlog.md](../../../seo/keyword-backlog.md). Zero paid tools.

## Process

1. **Pick seeds** from three sources:
   - Differentiators in [seo/product-context.md](../../../seo/product-context.md) (e.g. "without account", "offline", "ai photo")
   - Competitor gaps noted in [seo/competitors.md](../../../seo/competitors.md)
   - Existing winners: if Search Console access exists (MCP tool or user-provided export), queries already getting impressions at position 8–30 are the highest-value seeds. If no GSC access is configured, say so once and continue without it.

2. **Expand via Google autocomplete** (free, unauthenticated). Force US/English — results are otherwise geo-biased to the machine's location:
   ```
   curl -s "https://suggestqueries.google.com/complete/search?client=firefox&gl=us&hl=en&q=<url-encoded seed>"
   ```
   Mine patterns: `best <seed>`, `<seed> without`, `<seed> free`, `<seed> reddit`, `<competitor> vs`, `<seed> for <audience>`. Suffix letters (`<seed> a`, `<seed> b`…) when a seed looks rich.

3. **Judge difficulty by reading the live SERP** (WebSearch the exact phrase):
   - `easy` — indie app blogs (kcalm, nutrola, fitia class), forums, or thin/dated pages on page 1
   - `medium` — mixed indie + one or two big-media results
   - `hard` — big media, aggregators, or Google surfaces (AI overview dominance) own page 1 → find the long-tail variant instead of fighting
   - Note who ranks — a SERP full of sites from our SEO-competitor list is a green light.

4. **Estimate volume tier** (T1 head / T2 / T3 / T4 long-tail) from autocomplete presence, SERP investment (are people paying to rank?), and plausibility. Be honest about T4 — high-intent T4 with an exact differentiator match beats generic T2.

5. **Score & append** to the correct section (Tools / Roundups / Comparisons / Informational) with tier, difficulty, a one-line note (why us / what angle), and `idea` or `queued` status. Add a dated line to the Discovery log. Never delete existing rows; update status instead.

## Priorities (from seo/rules.md)

Tools > roundups > comparisons > informational. Informational keywords are backlog-worthy only as cluster support — mark them so nobody expects traffic.

## Before recommending "write more"

Check indexing of the last published batch first (rule 2 in [seo/rules.md](../../../seo/rules.md)): `site:caltracker.eu/blog/<slug>` for each recent post, or GSC URL inspection if available. If the last batch isn't indexed, the recommendation is "fix indexing", not "new keywords".
