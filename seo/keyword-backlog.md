# Keyword Backlog

> Append-only backlog maintained by the `seo-keyword-discovery` skill; consumed by `seo-write-article` / `seo-write-comparison`.
> **Volume tiers** (estimated, no paid tools): T1 = head term (10k+/mo), T2 = 1k–10k, T3 = 100–1k, T4 = long-tail (<100 but high intent).
> **Difficulty**: judged by reading the live SERP — `easy` = indie app blogs / forums rank, `medium` = mixed, `hard` = big media + aggregators own page 1.
> **Status**: idea → queued → drafted → published → (skip).
> Rule of thumb from Search Console reality: roundups & comparisons get clicks, informational gets impressions. Tools rank fastest and keep ranking.

## Tools (highest priority — rank fastest, earn links)

| Keyword | Tier | Difficulty | Notes | Status |
|---|---|---|---|---|
| calorie calculator / maintenance calorie calculator | T1 | hard | Head term; our calculator targets long-tail variants first | published 2026-07-12 → /tools/calorie-calculator/ |
| tdee calculator | T1 | hard | Same page targets it as secondary; "tdee calculator with steps" is T3/easy | published (same page) |
| calorie deficit calculator | T1 | medium | Autocomplete: +kg, +to lose weight, +tdee, +woman | idea — build as own tool |
| macro calculator | T1 | medium | +for weight loss, +women, +free | idea — own tool |
| protein intake calculator | T2 | medium | | idea |
| water intake calculator | T3 | easy | Matches app's water tracking | idea |
| weight goal date calculator ("when will I reach my goal weight") | T3 | easy | Mirrors app's goal-feasibility feature — unique angle | idea |
| calories burned walking calculator | T2 | medium | | idea |

## Roundups ("best X") — the click earners

| Keyword | Tier | Difficulty | Notes | Status |
|---|---|---|---|---|
| best ai calorie counter apps | T2 | easy-medium | Indie blogs rank (amyfoodjournal, macaron.im); our flagship | published 2026-07-12 → /blog/best-ai-calorie-counter-apps/ |
| best calorie counting app free / best free calorie tracker app | T1 | medium | "reddit" variants show forum-weight SERP = winnable | queued |
| best calorie tracker without subscription | T3 | easy | Perfect differentiator match (usable free tier) | queued |
| calorie tracker without account / without login | T4 | easy | ~~Exact differentiator match~~ — INVALID as of 2026-07-13, CalTracker now requires an account, do not target | skip |
| best offline calorie tracker | T4 | easy | Partial match only — CalTracker has no offline food database (quick add/history/cached barcodes only, see product-context.md). Don't write this as a #1 claim; position honestly or skip. | queued |
| best food scanner app / food calorie scanner app | T2 | medium | | idea |
| best calorie counting app for weight loss | T2 | medium | | idea |
| best macro tracking app | T2 | medium | Concede MacroFactor strengths honestly | idea |
| best calorie counter app uk | T3 | easy | Geo variant seen in autocomplete | idea |

## Comparisons ("X vs Y") — shopping-intent clicks

| Keyword | Tier | Difficulty | Notes | Status |
|---|---|---|---|---|
| cal ai vs myfitnesspal | T3 | easy | Active space; nutrola/intakenutrition rank | queued |
| caltracker vs myfitnesspal | T4 | easy | Brand-building; write once brand queries appear in GSC | queued |
| cal ai vs caltracker | T4 | easy | Own the SERP for our own comparison | queued |
| myfitnesspal vs yazio | T3 | easy | Top autocomplete for "myfitnesspal vs" | idea |
| myfitnesspal vs cronometer | T3 | medium | | idea |
| myfitnesspal vs lose it | T3 | medium | | idea |
| cal ai vs snapcalorie | T4 | easy | | idea |
| yazio vs lifesum | T3 | easy | EU-angle | idea |
| yazio vs caltracker | T4 | easy | Own the SERP; YAZIO now researched (product-context.md-equivalent detail in the roundup post) — concede fasting/EU-database, lead with price + AI-model choice | idea |

## Informational (cluster support — expect impressions, not clicks)

| Keyword | Tier | Difficulty | Notes | Status |
|---|---|---|---|---|
| how accurate are ai calorie counters | T3 | easy | Link-earning potential; supports AI cluster | queued |
| how to track calories (beginner guide) | T1 | hard | AI-overview-eaten; write for cluster only | idea |
| how to track calories when eating out | T3 | medium | Autocomplete find | idea |
| what is a calorie deficit / how big should it be | T1 | hard | Supports deficit-calculator tool | idea |
| mifflin st jeor equation explained | T3 | easy | Supports calorie calculator; scientific angle | idea |

## Discovery log

- 2026-07-12: Seeded from Google autocomplete (12 seeds, note: run with `&gl=us&hl=en` next time — this run had EU bias) + live SERP scan. GSC has no data for blog yet (no blog until today); re-run discovery against GSC after ~4 weeks of data.
- 2026-07-13: Correction — CalTracker removed anonymous/no-account mode (account now mandatory at onboarding, confirmed by Simon). Retired the "without account/login" backlog row and stripped the claim from product-context.md, rules.md, llms.txt, the post template, both write skills, and the published roundup post. See change-log.md.
- 2026-07-13: Correction #2 — "fully offline" was also overstated (no offline food database; confirmed by Simon). Downgraded the "best offline calorie tracker" row to a partial-match caution note. Also added YAZIO to the published roundup (fasting/EU-focused competitor, worth its own future "yazio vs caltracker" comparison — added as idea below) and repositioned CalTracker to #3 in that post, grounded in fresh competitor research. See change-log.md.
