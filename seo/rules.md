# SEO Operating Rules

> Binding for every SEO skill in this repo. These encode lessons learned (mostly by breaking them).

## Cadence & measurement

1. **Never change a page's `<title>` or meta description twice within 7 days.** You can't attribute ranking movement to a change if you stack changes. Every title/meta change gets a dated line in [change-log.md](change-log.md).
2. **Check indexing before writing a new batch.** Before generating new articles, verify the last batch is indexed (Search Console URL inspection, or `site:caltracker.eu/blog/<slug>` search). Writing into an indexing backlog is fighting the wrong blocker. If pages aren't indexed after ~2 weeks: improve internal linking / request indexing — don't pile on more posts.
3. **New content > edited content** for the first months. Only revisit a published post after it has 28+ days of Search Console data.

## Strategy

4. **No programmatic SEO.** No generated page factories, no /compare/ URL matrices. Every page is written and edited individually. (Google eventually torches factories, and our name is on this.)
5. **Priority order: tools > roundups > comparisons > informational.** Tools rank fastest and earn backlinks. Roundups and comparisons get clicks (reader is shopping). Informational posts feed topic clusters but get eaten by AI overviews — write them for structure, not traffic.
6. **Product truth only from [product-context.md](product-context.md).** Generators never invent CalTracker features. Competitor claims need a live check (WebFetch their pricing page) and an "as of <month year>" qualifier.
7. **Honesty is the conversion strategy.** Concede real competitor strengths (MFP's database, Cronometer's micros, MacroFactor's adaptive TDEE). Recommend CalTracker only where it genuinely wins: price, anonymous mode, offline, AI-model choice, daily AI evaluation.

## Page mechanics (every new page)

8. Clean URL: `blog/<slug>/index.html` or `tools/<slug>/index.html` → `https://caltracker.eu/blog/<slug>/`.
9. `<title>` ≤ 60 chars, keyword-first. Meta description 140–160 chars with a reason to click. One `<h1>`.
10. Canonical tag, Open Graph + Twitter card, JSON-LD (`Article` for posts, `FAQPage` where there's a real FAQ, `SoftwareApplication` only on app-focused pages).
11. Responsive single URL — blog/tool pages get **no** mobile.html variant and **no** UA redirect.
12. Same consent-gated analytics block as the rest of the site (TikTok holdConsent + GA4 after consent). Never add tracking that fires pre-consent.
13. Internal links: every new page links to ≥2 related pages (post ↔ tool ↔ post) and gets linked **from** the blog index; flagship pages also from the homepage footer. Orphan pages don't rank.
14. Add the URL to `sitemap.xml` with correct `lastmod` the same commit the page lands.
15. App-store links: `target="_blank" rel="noopener noreferrer"`, and keep the existing download-click tracking snippet so conversions attribute.
16. Images: explicit `width`/`height` or aspect-ratio, `loading="lazy"` below the fold, descriptive alt text.
17. Health content gets the standard disclaimer (not medical advice); nothing targeting eating-disorder-adjacent queries.

## Language

18. English only for now (`en_US` OG locale). German (`kalorienzähler…`) is a deliberate later expansion, not something a generator decides on its own.
