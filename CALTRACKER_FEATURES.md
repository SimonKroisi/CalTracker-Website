# CalTracker – Complete Feature Reference for Website AI

> **Purpose:** This document describes every feature of the CalTracker app, organized by section, with interactive demo suggestions for each. Use this as a reference to build website sections, feature showcases, and interactive animations.

> **App Info:** CalTracker is a calorie & nutrition tracking app available on Android and iOS. Website: caltracker-app.eu | Contact: caltracker.app@gmail.com

---

## Table of Contents

1. [Track Food in Many Ways](#1-track-food-in-many-ways)
2. [Track Calories & Macros](#2-track-calories--macros)
3. [Track Water Intake](#3-track-water-intake)
4. [Track Your Weight](#4-track-your-weight)
5. [Set Your Goals](#5-set-your-goals)
6. [AI-Powered Features](#6-ai-powered-features)
7. [Daily AI Evaluation & Insights](#7-daily-ai-evaluation--insights)
8. [Dashboard & Customization](#8-dashboard--customization)
9. [Statistics & History](#9-statistics--history)
10. [With or Without Account](#10-with-or-without-account)
11. [Cloud Sync & Offline Mode](#11-cloud-sync--offline-mode)
12. [Health App Integration](#12-health-app-integration)
13. [Subscription Plans](#13-subscription-plans)
14. [Favorites & Meal Recall](#14-favorites--meal-recall)
15. [Notifications & Reminders](#15-notifications--reminders)
16. [Export Your Data](#16-export-your-data)
17. [Onboarding Experience](#17-onboarding-experience)
18. [Streak & Gamification](#18-streak--gamification)
19. [Theming & Appearance](#19-theming--appearance)
20. [Support System](#20-support-system)

---

## 1. Track Food in Many Ways

CalTracker offers **5 different ways** to log your meals — so you can always pick the fastest method for the moment.

### 🔍 Database Search
- Search a massive food database powered by **FatSecret** (primary) and **OpenFoodFacts** (fallback)
- Thousands of branded and generic foods with accurate nutrition data
- Results include calories, protein, carbs, and fat per serving
- Adjustable serving sizes and portions
- Tap to add any result directly to your daily log

**Interactive Demo Idea:** Animated search bar where a user types a food name (e.g., "Banana"), results slide in from below with nutrition info cards. Tapping a result shows it being added with a checkmark animation.

---

### 📸 AI Photo Scanner
- Take a photo of your meal or pick from gallery
- AI identifies the food and estimates calories + macros automatically
- Choose from **7 different AI models** with varying speed and accuracy
- Editable food description before analysis for better results
- **Web Search** mode (Pro only) for better brand/product recognition
- Supports batch analysis of complex meals with multiple items

**AI Models Available:**
| Model | Speed | Accuracy | Access |
|-------|-------|----------|--------|
| GPT-4o-mini | Very Fast | Good | All users |
| GPT-4.1-mini | Fast | Good | All users |
| GPT-4o | Moderate | Very Good | Pro only |
| GPT-4.1 | Moderate | Very Good | Pro only |
| GPT-4.5-preview | Slow | Excellent | Pro (2/day) |
| o1 (Reasoning) | Slow | Excellent | Pro (2/day) |
| o3-mini (Reasoning) | Moderate | Good | Pro only |

**Interactive Demo Idea:** Show a phone mockup where a photo of food appears, then a shimmer/pulse loading animation plays, and nutrition results pop in with detected food items. Include a model selector dropdown that highlights different tiers.

---

### 📷 Barcode Scanner
- Scan any product barcode using your camera
- Instantly pulls nutrition data from **OpenFoodFacts** database
- Camera overlay shows green corner brackets for barcode alignment
- Supports torch (flashlight) toggle and camera flip
- Results auto-populate calories, macros, and serving size

**Interactive Demo Idea:** Animated phone screen showing a camera view with green corner brackets. A barcode slides into frame, brackets pulse green, and a product card flies in from the bottom with nutrition details.

---

### ⚡ Quick Add
- Fastest method — just type the calories directly
- Perfect for when you already know the calorie count
- Optional macro entry (protein, carbs, fat)
- Meals are auto-categorized by time of day:
  - **Breakfast:** 5:00–10:00
  - **Lunch:** 10:00–15:00
  - **Dinner:** 15:00–23:00
  - **Snacks:** 23:00–5:00
- Manual category override available

**Interactive Demo Idea:** Minimalist input field animation — user types "350" for calories, selects a category chip (Breakfast/Lunch/Dinner/Snack), and the meal slides into a daily list with a smooth fade-in.

---

### ⭐ Add from Favorites
- Save your frequently eaten meals for **one-tap** reuse
- Custom meals with name, calories, macros, ingredients, and photo
- Usage counter ranks your most-used favorites at the top
- Search and filter through your saved favorites
- Edit or delete favorites anytime

**Interactive Demo Idea:** A favorites grid/list with food icons. Tapping one shows a quick "Added!" checkmark animation and the meal appears in today's log.

---

## 2. Track Calories & Macros

### 🔥 Calorie Tracking
- Beautiful **animated circular progress ring** showing daily calorie intake
- Color changes based on progress:
  - 🔵 **Blue** (0–50%) — Still plenty of room
  - 🟢 **Green** (50–80%) — On track
  - 🟠 **Orange** (80–100%) — Approaching goal
  - 🔴 **Red** (>100%) — Over goal
- Shows remaining calories or "over by X" counter
- Weekly activity visualization (7-day bar chart)
- 90+ days of history browsing

**Interactive Demo Idea:** An animated calorie ring that fills from 0% to ~75% with smooth color transitions (blue → green → orange). A number counter in the center counts up from 0 to "1,850 / 2,400 kcal". Below, a mini weekly bar chart animates each day's bar growing to different heights.

---

### 🥩🍞🥑 Macro Tracking (Protein, Carbs, Fat)
- Track protein, carbohydrates, and fat in grams
- Customizable macro goals (default 30% protein / 50% carbs / 20% fat)
- Individual animated progress bars for each macro
- Percentage display showing how close you are to each target
- Macro balance scoring in daily evaluations

**Interactive Demo Idea:** Three horizontal progress bars (Protein = red/pink, Carbs = blue, Fat = yellow/orange) that fill simultaneously with smooth animation. Each bar has a label showing "85g / 120g" and a percentage badge.

---

### 🍽️ Meal Categories
- Meals are organized into 4 categories with distinct colors:
  - 🔵 **Breakfast** (Blue)
  - 🟠 **Lunch** (Orange)
  - 🟣 **Dinner** (Purple)
  - 🟡 **Snacks** (Amber)
- Auto-detection based on time of day
- Manual override always available
- Grouped display on home screen

---

## 3. Track Water Intake

### 💧 Water Tracking
- Track daily water intake in milliliters
- **Quick-add buttons** for common amounts: 200ml, 250ml, 330ml, 500ml, 750ml, 1000ml
- Manual entry for custom amounts
- Default daily goal: 2,500ml (customizable)
- Visual progress bar showing intake vs. goal
- Dashboard widget for at-a-glance hydration status

**Interactive Demo Idea:** A water glass or bottle that fills up as the user "taps" quick-add buttons (200ml, 500ml). The progress bar animates upward, and a label shows "1,750ml / 2,500ml". Each tap creates a small water splash effect.

---

## 4. Track Your Weight

### ⚖️ Weight Tracking
- Log your weight manually (supports kg and lbs, switchable)
- **Trend chart** showing weight over time with a smooth trend line
- **BMI calculation** with a color-coded gauge bar:
  - Blue = Underweight
  - Green = Normal
  - Orange = Overweight
  - Red = Obese
- **Expected vs. Actual** comparison based on your calorie deficit/surplus
- **Goal feasibility scoring** — shows the probability (%) of reaching your weight goal by your target date
- Add notes to each weight entry
- Weight history browsable in detail

**Interactive Demo Idea:** A line chart that draws itself from left to right showing a weight trend going down over 30 days. Below it, a BMI gauge needle animates to the user's position on the scale (blue → green → orange → red). A probability badge pulses showing "87% likely to reach your goal."

---

## 5. Set Your Goals

CalTracker helps you set personalized goals whether you want to **lose weight (Abnehmen)**, **gain weight (Zunehmen)**, or **maintain weight (Gewicht halten)**.

### 🎯 Calorie Goal
- Calculated using the scientific **Mifflin-St Jeor equation** based on:
  - Your weight, height, age, and gender
  - Your **activity level** (5 levels: Sedentary → Very Active)
  - Your **goal type**: Lose / Maintain / Gain
- Shows estimated weekly weight change
- Custom calorie goal override available for advanced users
- Configurable deficit/surplus amount (kcal/day)

### 🥗 Macro Goals
- Default split: 30% Protein / 50% Carbs / 20% Fat
- Fully customizable per gram
- Macro targets auto-adjust when calorie goal changes

### ⚖️ Weight Goal
- Set a target weight and deadline
- **Probability calculator** shows how realistic your goal is
- Compares expected weight loss trajectory vs. actual progress
- Adjusts recommendations based on your tracking data

### 💧 Water Goal
- Default 2,500ml/day
- Adjustable to personal needs

**Interactive Demo Idea:** A goal setup wizard animation: Step 1 shows selecting "Lose Weight" / "Maintain" / "Gain Weight" with a tap. Step 2 shows a calorie goal calculating with animated numbers. Step 3 shows macro bars adjusting. Final step shows a weight progress projection chart drawing itself. Each step slides in smoothly.

---

## 6. AI-Powered Features

### 🤖 Smart Food Recognition
- Powered by **OpenAI vision models** (GPT-4o, GPT-4.1, etc.)
- Take a photo → AI identifies food → auto-fills nutrition info
- **7 AI models** to choose from (speed vs. accuracy trade-off)
- Editable description for better accuracy
- Web search mode for branded products (Pro exclusive)

### 🧠 AI Quick Analysis
- Fast nutrition estimation from food descriptions
- Works with text input (no photo needed)
- Great for custom or home-cooked meals

### 🔒 Server-Side Processing
- All AI processing happens securely on our cloud servers
- Your API keys are never exposed on your device
- Fast response times (typically under 10 seconds)

**Interactive Demo Idea:** Split-screen animation: Left side shows a phone camera capturing food. Right side shows AI processing (spinning brain icon or neural network animation), then results appear with food name, calories, and macros sliding in one by one.

---

## 7. Daily AI Evaluation & Insights

Get a **personalized AI analysis** of your entire day's nutrition — including a score, strengths, and improvement suggestions.

### 📊 Scoring System
- Overall score from **0–100**
- Rating: Excellent / Good / Average / Poor
- Sub-scores (Plus & Pro):
  - **Macro Balance Score** — Are your macros well-distributed?
  - **Meal Timing Score** — Are you eating at good times?
  - **Food Quality Score** — How nutritious are your choices?
  - **Hydration Score** — Are you drinking enough water?

### 📋 Insights by Tier
| Insight | Free | Plus | Pro |
|---------|------|------|-----|
| Overall Score & Rating | ✅ | ✅ | ✅ |
| Summary Text | ❌ | ✅ | ✅ |
| Strengths (up to 3) | ❌ | ✅ | ✅ |
| Improvements (up to 3) | ❌ | ✅ | ✅ |
| Goal-Specific Advice | ❌ | ✅ | ✅ |
| Sub-Category Scores | ❌ | ✅ | ✅ |
| Food Category Breakdown | ❌ | ❌ | ✅ |
| Food Swap Tips (up to 5) | ❌ | ❌ | ✅ |

### Daily Evaluation Limits
- **Free:** 1 evaluation/day
- **Plus:** 3 evaluations/day
- **Pro:** 10 evaluations/day

**Interactive Demo Idea:** Animated score reveal — a large number counts from 0 to 85 with a circular ring filling. Below it, insight cards fade in one by one: "✅ Great protein intake", "⚠️ Try to eat more vegetables", "💡 Swap white bread for whole grain". The rating text ("Good") appears with a color-pop animation.

---

## 8. Dashboard & Customization

### 📱 Customizable Home Dashboard
- **Grid-based responsive layout** (4-column grid)
- **Default widgets:**
  - Calorie Stats Card (animated ring with progress)
  - Quick Add Button
  - AI Food Scanner Button
  - Barcode Scanner Button
  - Favorites Button
  - Meals Section (grouped by Breakfast / Lunch / Dinner / Snacks)

### 🔧 Optional Widgets (toggleable)
- Weekly calorie stats chart
- Nutrition tip card
- Individual Protein / Carbs / Fat stat cards
- Weight tracking card with mini chart
- Water intake card with progress bar
- Streak badge with fire animation

### ✏️ Edit Mode
- Toggle "Edit Mode" to customize your dashboard
- **Drag & drop** to reorder cards
- **Hide/show** widgets you don't need
- Layout is saved and persists across sessions

**Interactive Demo Idea:** Show a phone dashboard mockup. Tap an "Edit" button → widgets start wiggling (like iOS home screen). Drag a widget from one position to another with a smooth animation. Toggle off a widget and it fades away. Tap "Done" and the layout locks in.

---

## 9. Statistics & History

### 📅 History Browser
- Browse all tracked days in a scrollable list
- Each day card shows:
  - Date with color-coded progress indicator
  - Total calories vs. goal
  - Meal count
  - AI evaluation score (if available)
  - Macro breakdown
- Tap any day to see full details

### 📊 Day Detail View
- Full meal list grouped by category (Breakfast, Lunch, Dinner, Snacks)
- Daily totals and goal progress
- Add, edit, or delete meals
- View daily AI evaluation
- Swipe to delete meals

### 📈 Aggregated Statistics
- Weekly stats (7 days)
- Monthly stats (30 days)
- All-time stats
- Average daily calories
- Days on target (within 80–110% of goal)

### 📊 Weekly Calorie Chart
- 7-day bar chart comparing daily intake vs. goal
- Color-coded bars (on-target / under / over)
- Tap a bar to view that day's details

**Interactive Demo Idea:** A weekly bar chart where each bar grows up from zero to its value. A goal line draws across. Bars that are on-target turn green, under-target turn blue, over-target turn orange/red. Tapping a bar highlights it and shows a tooltip with "Monday — 2,150 kcal."

---

## 10. With or Without Account

CalTracker works perfectly **without creating an account** — or you can sign up for cloud sync and cross-device access.

### 👤 Anonymous Mode (No Account)
- Full app functionality without signing up
- All data stored locally on your device
- No email, no password — just start tracking
- Perfect for privacy-focused users
- Can create an account later without losing data

### 📧 Email & Password
- Classic sign-up with email verification
- Password reset via email
- Full cloud sync support

### 🔵 Google Sign-In
- One-tap sign in with your Google account
- Fastest account creation method
- Automatic profile linking

### 🍎 Apple Sign-In
- Sign in with Apple ID
- Hide My Email supported
- Required for iOS compliance

### 🔄 Account Benefits
- **Cloud sync** — access your data on any device
- **Subscription management** — linked to your account
- **Data backup** — never lose your tracking history
- **AI usage tracking** — quota tied to authenticated account

**Interactive Demo Idea:** A split view showing two paths: Left side "Without Account" shows a phone with a simple "Start Tracking" button → immediately enters the app. Right side "With Account" shows Google / Apple / Email buttons → quick sign-in animation → cloud sync icon. Both paths lead to the same full-featured dashboard.

---

## 11. Cloud Sync & Offline Mode

### ☁️ Cloud Sync
- **Firebase Firestore** powered cloud backup
- **Bidirectional sync** — upload local changes AND download cloud changes
- **Smart diff-based** — only syncs changed data, not everything
- **Synced data includes:** Meals, weight entries, favorites, user profile, daily evaluations

### Sync by Tier
| Feature | Free | Plus | Pro |
|---------|------|------|-----|
| Auto-Sync | ❌ | ✅ | ✅ |
| Manual Sync | 1x per week | Unlimited | Unlimited |

### 📴 Full Offline Mode
CalTracker works **100% offline** for core features:
- ✅ Add & edit meals
- ✅ Track water intake
- ✅ Log weight
- ✅ View history & statistics
- ✅ Full dashboard display

**Features requiring internet:**
- ❌ AI food scanner (cloud processing)
- ❌ Barcode lookup (online database)
- ❌ Database search (online food API)
- ❌ Cloud sync

**Auto-recovery:** When connection is restored, the app automatically syncs all pending changes.

**Interactive Demo Idea:** An animation showing a phone with a WiFi icon. WiFi turns off (icon goes red/crossed-out) — the phone continues tracking normally (adding meals, logging weight). WiFi reconnects (icon goes green) — a cloud sync animation shows data uploading with a checkmark.

---

## 12. Health App Integration

### 🏃 Google Health Connect (Android)
- Sync steps and active calories burned
- Read your daily step count directly in CalTracker
- Write your CalTracker nutrition data back to Health Connect
- Permission flow with clear explanation dialogs

### 🍎 Apple Health (iOS)
- Same integration via Apple HealthKit
- Steps, active calories, nutrition data
- Native iOS permission dialog

### 📊 What Gets Synced
- **Read:** Steps count, active calories burned, workouts
- **Write:** Daily calorie intake (nutrition)

**Interactive Demo Idea:** Two phone mockups side by side — Android with Health Connect icon and iOS with Apple Health icon. Both show a "Connect" button that, when tapped, triggers a permission dialog animation. After connecting, step count and burned calories appear on the CalTracker dashboard with a slide-in animation.

---

## 13. Subscription Plans

### 🆓 Free
- **Price:** Free forever
- **AI Calls:** 20 lifetime total
- **AI Models:** GPT-4o-mini only
- **Cloud Sync:** 1x manual sync per week
- **Daily Evaluation:** 1 per day (basic score only)
- All core tracking features included (calories, macros, water, weight, history)

### ⭐ Plus — €2.49/month or €19.99/year
- **AI Calls:** 5 per day
- **AI Models:** GPT-4o-mini + GPT-4.1-mini
- **Cloud Sync:** Auto-sync + unlimited manual sync
- **Daily Evaluation:** 3 per day (with detailed insights)
- Strengths, improvements, and goal advice included

### 👑 Pro — €7.99/month or €59.99/year
- **AI Calls:** 25 per day
- **AI Models:** All 7 models (including GPT-4.5-preview, o1, o3-mini)
- **Web Search** mode for AI scanner (better brand recognition)
- **Cloud Sync:** Auto-sync + unlimited manual sync
- **Daily Evaluation:** 10 per day (full detailed analysis)
- Food swap tips, category breakdowns, food quality scoring
- Priority access to new features

### 💰 Yearly Savings
- Plus yearly: ~33% savings vs. monthly
- Pro yearly: ~37% savings vs. monthly

### 🔄 Manage Subscription
- Subscribe, upgrade, or cancel anytime
- Restore purchases on new devices
- Subscription managed through Apple App Store or Google Play

**Interactive Demo Idea:** An interactive pricing table/comparison toggle. Three columns (Free / Plus / Pro) with feature rows. A monthly/yearly toggle at the top switches prices with a smooth animation. Hovering or tapping a tier highlights its features. A "Most Popular" badge on Plus and a "Best Value" badge on Pro yearly. Checkmarks and X-marks animate in for each feature row.

---

## 14. Favorites & Meal Recall

### ⭐ Save Custom Meals
- Create custom meals with:
  - Name
  - Calories & macros (protein, carbs, fat)
  - Ingredient list (optional)
  - Photo (camera or gallery, optional)
  - Serving size & unit (g, ml, piece, etc.)
- Save any meal as a favorite for one-tap reuse

### 🔄 Quick Reuse
- Open Favorites → tap any saved meal → instantly added to today
- Usage counter tracks your most-used meals (sorted by frequency)
- Search and filter through favorites by name
- Edit or delete favorites anytime

**Interactive Demo Idea:** A favorites list with 3-4 meal cards (e.g., "Morning Oatmeal 350kcal", "Chicken Salad 450kcal"). Tapping one shows a quick ripple effect and "Added to Lunch ✓" toast. A "Create New" button opens a mini form that fills in with smooth field animations.

---

## 15. Notifications & Reminders

### 🔔 Meal Reminders
- Set custom reminder times for **Breakfast, Lunch, and Dinner**
- Individual toggle on/off per meal
- Daily recurring notifications
- Time picker for each meal

### 💧 Water Reminders
- Interval-based reminders (every 1–4 hours)
- Configurable time window (e.g., 8:00 AM – 10:00 PM)
- Toggle on/off
- Automatically scheduled during daytime hours

### ⚖️ Weight Reminders
- Single daily reminder at your chosen time
- Toggle on/off
- Helps build a consistent weighing habit

**Interactive Demo Idea:** A notification bell that rings with a small bounce animation. Below it, three rows appear: "🍳 Breakfast — 8:00 AM", "🥗 Lunch — 12:30 PM", "🍽️ Dinner — 7:00 PM" with toggle switches. Toggling one on shows a mini notification preview sliding down from the top.

---

## 16. Export Your Data

### 📤 CSV Export
- Export your tracking data as a standard **CSV file**
- Choose time range: **7 days, 30 days, or 365 days**
- Exported data includes:
  - Daily summaries (calories, macros, water, weight)
  - Individual meal entries (name, calories, macros, time, category)
- Share via email, cloud storage, or any app on your device

**Interactive Demo Idea:** A button that says "Export Data" with a download icon. On tap, a time range selector appears (7 / 30 / 365 days). After selection, a file icon animates being created and a share sheet slides up from the bottom.

---

## 17. Onboarding Experience

### 🚀 8-Step Guided Setup
1. **Welcome** — Friendly greeting and "Get Started" button
2. **About You** — Enter your name
3. **Body Measurements** — Weight (kg/lbs) and height (cm/in) with unit toggle
4. **Birthdate & Info** — Date picker, gender, activity level
5. **Goal Selection** — Choose: Lose / Maintain / Gain weight + see calorie estimate
6. **Review** — Summary of all your inputs
7. **Account (Optional)** — Create account or skip (anonymous)
8. **Premium Offer** — See Plus/Pro plans or continue free

- Personalized calorie and macro goals calculated automatically
- Skip account creation and use the app immediately
- Premium trial offer available during onboarding

**Interactive Demo Idea:** A step-by-step carousel showing each onboarding page sliding in from the right. Mini animations for each step: name types itself, weight slides with a dial animation, goal buttons highlight on tap, and a final confetti celebration when setup is complete.

---

## 18. Streak & Gamification

### 🔥 Daily Streak
- Track consecutive days with at least 1 meal logged
- Streak counter with **fire emoji badge**
- Prominent display on home screen and profile
- **Server-side validation** — no cheating possible
- Streak count displayed with a gradient background and pulse animation

### 🎮 Motivational Rewards
- Visual gamification element to keep users engaged
- Streak milestones recognized (3-day, 7-day, 30-day, etc.)
- Special trial offers may unlock at certain streak milestones

**Interactive Demo Idea:** A fire/flame icon with a counter that increments: 1🔥 → 2🔥 → 3🔥... with each number change triggering a small flame flicker and pulse glow effect. At milestone numbers (7, 30), a special confetti or burst animation plays.

---

## 19. Theming & Appearance

### 🎨 Theme Options
- **Light Mode** — Clean white backgrounds with dark text
- **Dark Mode** — True dark backgrounds (#0D0D0D) with light text
- **System Default** — Automatically follows your device's theme setting

### 🎨 App Design
- **Material Design 3** for a modern, clean look
- Primary color: **Green (#4CAF50)**
- Smooth animations throughout:
  - Circular progress indicators (calorie ring fills)
  - Pulse animations (AI processing)
  - Fade-in transitions (results appearing)
  - Slide transitions (page navigation)
  - Score counter animations (daily evaluation)
- Rounded corners, consistent spacing, floating buttons
- Units: Metric (kg, cm) or Imperial (lbs, inches) — switchable

**Interactive Demo Idea:** A toggle switch that flips between Light and Dark mode. The entire demo section smoothly transitions themes — backgrounds, text colors, card styles all animate. Below, a phone mockup shows the dashboard switching themes in real time.

---

## 20. Support System

### 🆘 In-App Support
- Create support requests with title and description
- Attach images (camera/gallery) or files
- Track request status: Open → In Progress → Answered → Completed
- View all active and archived requests
- Search and filter through your requests
- Time-stamped message history per request
- Requests follow you across devices (cloud-synced)

**Interactive Demo Idea:** A chat-bubble style support dialog. User types a message, attaches a screenshot (image slides in), and sends. A status badge shows "Open" → transitions to "In Progress" → "Answered" with a green checkmark.

---

## Summary: Key Feature Highlights for Website

### 🏆 Headline Features (Hero Section)
1. **5 ways to track food** (Search, AI Photo, Barcode, Quick Add, Favorites)
2. **AI-powered nutrition analysis** with 7 model options
3. **Works with or without an account**
4. **Full offline functionality**
5. **Daily AI evaluation** with personalized insights
6. **Customizable dashboard** with drag-and-drop widgets

### 📊 Tracking Features
- Calories with animated progress ring
- Macros (Protein, Carbs, Fat) with progress bars
- Water intake with quick-add buttons
- Weight with trends, BMI, and goal probability

### 🎯 Goal Features
- Lose weight / Gain weight / Maintain weight
- Science-based calorie calculation (Mifflin-St Jeor)
- Custom macro splits
- Weight goal with deadline and probability scoring

### 🔗 Integration Features
- Google Health Connect & Apple Health
- Cloud sync with Firebase
- CSV data export
- RevenueCat subscription management

### ✨ Premium Highlights
- 7 AI vision models for food scanning
- Web search for brand recognition (Pro)
- Detailed daily evaluation with food swap tips (Pro)
- Unlimited cloud sync (Plus & Pro)
- Up to 25 AI calls per day (Pro)

---

## Recommended Interactive Demo Animations (Priority Order)

| Priority | Animation | Description | Estimated Impact |
|----------|-----------|-------------|-----------------|
| 1 | **Calorie Ring** | Circle fills 0→100% with color change + number counter | Very High — Visual centerpiece |
| 2 | **5 Input Methods Carousel** | Swipeable cards showing Search → AI → Barcode → Quick → Favorites | Very High — Core value prop |
| 3 | **AI Scanner Demo** | Photo → loading pulse → results pop in | High — Wow factor |
| 4 | **Pricing Toggle** | Interactive Free/Plus/Pro comparison with monthly/yearly switch | High — Conversion driver |
| 5 | **Macro Bars** | 3 bars fill simultaneously to targets | Medium — Visual appeal |
| 6 | **Weight Chart** | Line draws with trend + BMI gauge | Medium — Goal visualization |
| 7 | **Daily Score Reveal** | Counter 0→85 with insights fading in | Medium — AI showcase |
| 8 | **Streak Fire** | Counter increments with flame pulse | Medium — Engagement hook |
| 9 | **Light/Dark Theme Toggle** | Dashboard switches theme smoothly | Low — Nice touch |
| 10 | **Water Glass Fill** | Glass fills on tap with splash effect | Low — Cute detail |

---

*This document was generated from the CalTracker Flutter codebase and documentation. All features are accurate as of the current app version.*
