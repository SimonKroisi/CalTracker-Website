# CalTracker — Canonical Product Context for SEO Content

> **This file is the single source of truth for every content generator.**
> No article, comparison, or tool page may claim anything about CalTracker that is not in this file.
> If a fact is missing here, verify it in the app (or ask Simon) and add it here first — never invent it.
> Full feature detail lives in [CALTRACKER_FEATURES.md](../CALTRACKER_FEATURES.md); this file is the distilled, safe-to-publish subset.

## What CalTracker is

- AI-powered **calorie & nutrition tracking app** for **Android and iOS** (Flutter).
- Website: **https://caltracker.eu** · Contact: caltracker.app@gmail.com
- Google Play: `https://play.google.com/store/apps/details?id=com.trackerapp.caltracker`
- App Store: `https://apps.apple.com/us/app/caltracker-ai-calorie-counter/id6760666203`
- Primary market: English-speaking users; EU-based developer (prices in EUR). German-language SEO is a possible later expansion (kalorienzähler app).

## The 5 logging methods (core value prop)

1. **Database search** — FatSecret (primary) + OpenFoodFacts (fallback); branded and generic foods.
2. **AI photo scanner** — snap a meal photo, AI estimates calories + macros. Multiple AI models with speed/accuracy trade-offs (higher-accuracy models on paid tiers). Editable description before analysis. Web-search mode for brand recognition (Pro).
3. **Barcode scanner** — OpenFoodFacts lookup, torch + camera-flip support.
4. **Quick add** — type calories (optionally macros) directly; auto-categorized by time of day.
5. **Favorites** — save custom meals (name, macros, photo, ingredients) for one-tap re-logging; usage-ranked.

## What it tracks

- **Calories** (animated progress ring, color-coded), 90+ days of history.
- **Macros**: protein, carbs, fat with customizable goals (default 30/50/20). **No micronutrient tracking** — never claim vitamins/minerals.
- **Water** (quick-add buttons, default goal 2,500 ml).
- **Weight** (kg/lbs, trend chart, BMI gauge, expected-vs-actual, **goal feasibility probability** — % chance of hitting target weight by target date).
- **Steps & active calories** via Google Health Connect (Android) / Apple Health (iOS).

## Goals & science

- Calorie goal computed with the **Mifflin-St Jeor equation** (weight, height, age, gender, 5 activity levels, goal type lose/maintain/gain, configurable deficit/surplus).
- Estimated weekly weight change shown; custom calorie override available.

## Daily AI evaluation

- AI scores each day **0–100** with rating (Excellent/Good/Average/Poor).
- Paid tiers add sub-scores (macro balance, meal timing, food quality, hydration), strengths/improvements, goal-specific advice, food-swap tips (Pro).

## Differentiators to lead with (all true, all verifiable)

1. **Partial offline logging** once signed in: quick add, editing existing entries, water, weight, history/statistics all work without internet. Barcode scanning works offline only for barcodes already cached from an earlier lookup — there is no offline food database, so fresh barcode lookups, database search, and AI photo scanning all require a connection. Real but modest edge — don't oversell as "fully offline."
2. **Cheap**: Plus **€2.49/mo or €19.99/yr**; Pro **€7.99/mo or €59.99/yr**. Undercuts MyFitnessPal Premium (~$19.99/mo), Cal AI (~$9.99/mo), Cronometer Gold (~$10.99/mo). Free tier is genuinely usable (all core tracking free forever).
3. **Choice of AI models** for photo scanning (speed vs accuracy) instead of one black box.
4. **Daily AI evaluation** — scores the whole day, not just individual meals.
5. **Privacy-friendly**: EU developer, GDPR-conscious, data deletion available on request.

## Pricing (verify before every publish — may change)

| Tier | Price | Key limits |
|------|-------|-----------|
| Free | €0 forever | All core tracking; limited AI scans; basic daily score; 1 manual sync/week |
| Plus | €2.49/mo · €19.99/yr | 5 AI calls/day, auto-sync, detailed daily insights |
| Pro | €7.99/mo · €59.99/yr | 25 AI calls/day, best AI models, web-search scan mode, food-swap tips |

> ⚠️ Do **not** publish an exact free-tier AI-scan quota without checking the current app version; it has changed before. Say "a limited number of free AI scans" if unverified.

## Also true (usable when relevant)

- Cloud sync (Firebase) across devices; smart diff-based.
- CSV export (7/30/365 days).
- Meal reminders, water reminders, weight reminders.
- Streaks with server-side validation.
- Light/dark/system themes, Material Design 3, metric + imperial units.
- Customizable drag-and-drop dashboard.
- In-app support system.

## Never claim (features CalTracker does NOT have)

- ❌ **No-account / anonymous / guest mode** — REMOVED as of 2026-07-13. Account creation (email, Google, or Apple) is now mandatory at onboarding; there is no skip option. Do not describe CalTracker as "no sign-up" or "works without an account" anywhere.
- ❌ **"Fully offline" / "100% offline" / "offline core" as a blanket claim** — CORRECTED as of 2026-07-13. There is no offline food database: database search never works offline, and barcode scanning only works offline for previously-cached barcodes (fresh lookups need internet, same as AI scanning). Only say specifically what works offline: quick add, editing entries, water, weight, history/stats, and cached-barcode rescans.
- ❌ Micronutrient / vitamin / mineral tracking
- ❌ Recipes, meal plans, or recipe import
- ❌ Intermittent fasting timers
- ❌ Community/social features, friends, forums
- ❌ Coaching (human or programmatic courses à la Noom)
- ❌ Web app / desktop version
- ❌ Restaurant menu database
- ❌ Direct Garmin/Fitbit/Whoop integrations (only Health Connect / Apple Health)
- ❌ "Doctor-approved", "clinically proven", or any medical claims

## Voice

- Practical, honest, first-person-plural developer voice ("we built CalTracker because…") where a persona is needed.
- Concede competitor strengths plainly (MyFitnessPal's database size, Cronometer's micronutrients, MacroFactor's adaptive TDEE). Credibility converts better than hype.
- Health disclaimer on anything advising calorie targets: not medical advice, consult a professional for medical conditions/eating disorders.
