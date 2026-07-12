---
name: seo-competitor-scan
description: Stage 3 of the SEO pipeline — profile what each competitor in seo/competitors.md ranks for, what they charge, and what content/tools they run. Use when the user wants competitor profiles refreshed or asks what a competitor ranks for.
---

# Competitor Scan

Goal: per-competitor intelligence that feeds keyword discovery and comparison posts. Input roster: [seo/competitors.md](../../../seo/competitors.md).

## Process (per competitor — scan 2–4 per run, don't boil the ocean)

1. **Pricing**: WebFetch their pricing page; record exact current prices with "as of <month year>". Pricing changes are content opportunities ("X price increase" queries spike).
2. **Content surface**: WebFetch their blog index / tools index. Record:
   - Content types they run (roundups? vs-pages? calculators? programmatic factories?)
   - Posting velocity (rough posts/month from visible dates)
   - Free tools they offer (each of their calculators is a candidate for us to build better)
3. **What they rank for**: WebSearch `site:<their domain>` plus 2–3 of our target keywords to see which of their pages appear. Note which of OUR backlog keywords they already hold.
4. **Weaknesses**: paywalled features users complain about (search `<app> reddit complaints`), thin/dated pages we can beat, keywords they ignore.
5. **Write it down**: update their row + the Standing observations section in seo/competitors.md. Feed newly-found keyword gaps into [seo/keyword-backlog.md](../../../seo/keyword-backlog.md) as `idea` rows with a source note.

## Rules

- Facts about competitors used in published content must be re-verified at publish time by the article skills — your scan notes are leads, not citations.
- Follow [seo/rules.md](../../../seo/rules.md).
