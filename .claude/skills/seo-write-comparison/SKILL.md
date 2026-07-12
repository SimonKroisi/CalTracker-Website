---
name: seo-write-comparison
description: Stage 5b of the SEO pipeline — generate an "X vs Y" comparison post as a static HTML page. Use when the user asks for a comparison/versus article (e.g. "Cal AI vs MyFitnessPal" or "CalTracker vs X") for caltracker.eu.
---

# Write Comparison ("X vs Y")

Same pre-flight, bookkeeping, and page mechanics as [seo-write-article](../seo-write-article/SKILL.md) — read that skill and [seo/rules.md](../../../seo/rules.md) first. This skill only changes the research and structure.

## Research (accuracy is the whole product here)

1. For BOTH apps: WebFetch current pricing page + app-store listing. Record exact prices, trial terms, and paywall boundaries (e.g. "barcode scanning requires Premium") with "as of <month year>". A stale price in a vs-post kills trust and rankings.
2. Search `<X> vs <Y> reddit` — real user threads reveal the deciding factors people actually weigh. The post should answer those, not a generic feature matrix.
3. If one of the apps is CalTracker: facts ONLY from [seo/product-context.md](../../../seo/product-context.md), including the Never-claim list.

## Structure

4. **Verdict first**: 2–3 sentence answer naming who each app is for. Readers of vs-posts are shopping; don't make them scroll.
5. Side-by-side table: price, free tier reality, logging methods, AI features, database, offline, account requirement, platforms.
6. One section per deciding dimension (from the Reddit research), each ending with a one-line "winner" call.
7. "Who should pick X / who should pick Y" — genuinely balanced.
8. If neither app is CalTracker: a short, clearly-marked "where CalTracker fits" box (price, offline core, AI-model choice) — one box, not a hijack. If CalTracker loses a dimension, say so; conceding is the credibility play.
9. FAQ from autocomplete questions on the pair.

## Page specifics

10. Slug: `blog/<x>-vs-<y>/` (alphabetical unless one is CalTracker — CalTracker goes last: `cal-ai-vs-caltracker`).
11. Title pattern: `X vs Y (2026): <deciding factor>` ≤ 60 chars. JSON-LD `Article` + `FAQPage`.
12. Never fabricate hands-on testing claims ("we tested for 30 days") — write from verifiable features, pricing, and cited user reports.
