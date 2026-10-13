# Smart Campus Analytics — 2-minute demo script

One laptop, `dashboard.html` open (works offline). Rehearse once before judges arrive.

## Setup
- Open `dashboard.html` on the **Overview** tab.
- Know your hero student: **Yamini Reddy (25TP1A0542)** — Year 3, score 55.3, attendance 59%, aptitude 42, flagged for **both** academic and placement risk. Search "Yamini" in the Students tab to find her fast. The simulator move: drag **attendance to 75** and **aptitude to 70** → score **55.3 → 60.3 (+5.0)**, both flags clear.

## The run

**0:00–0:20 — Problem → Overview**
> "Colleges generate tons of student data — attendance, marks, LMS activity, placements — but it sits in disconnected systems and nobody acts on it. We unified 8 data sources into one student view for 200 students."
- Point at the KPI cards: average success score **65.7**, and **44 students** flagged at academic risk right now.

**0:20–0:45 — The at-risk list**
> "Here's the at-risk list."
- Students tab → Risk filter → **Academic risk**. "44 students. But a list isn't intelligence — every student gets a Success Score from 6 weighted indicators, and the platform explains itself."
- Search **"Yamini"**, click her row.

**0:45–1:10 — Explainability**
> "Yamini's score is 55.3. The summary tells us why in plain English — flagged for both academic and placement risk, mainly low attendance at 59% and a backlog, with placement readiness her biggest lever. And these bars show exactly which indicator drags her score down."
- Point at the natural-language summary box, then the contribution bars.

**1:10–1:50 — What-if simulator (THE CLOSER)**
> "Now the part no dashboard does. Watch what happens if our interventions work — I drag her attendance from 59% to 75%, and her aptitude from 42 to 70…"
- Drag the **attendance slider to 75**, then the **aptitude slider to 70**.
> "Score jumps 55 to 60 — and *both* risk flags clear. Faculty don't just see *who's* at risk; they see *which intervention actually works* before spending a semester on it. That's decision intelligence."

**1:50–2:00 — Impact close**
> "The same engine found a hidden group: 15 students with 9+ CGPA who'll still miss placements without aptitude help. We catch them now — not after placement season. Happy to take questions."

## Likely judge questions (one-line answers)

1. **"How is the score computed?"**
   → "Six indicators with fixed weights — academic 35%, attendance 20%, LMS 15%, placement readiness 15%, skills 10%, engagement 5%. Risk flags fire on score below 50, 2+ backlogs, or attendance below 60%."

2. **"Is the data real?"**
   → "It's synthetic — 200 students generated with realistic correlations so we can demonstrate the full methodology end to end. The pipeline is source-agnostic and plugs into real college systems."

3. **"What makes this different from a dashboard?"**
   → "Dashboards report the past. Our what-if simulator predicts the outcome of an intervention *before* you act — that's the difference between reporting and decision intelligence."

## Tips
- Rehearse the slider drag once — it must feel instant.
- If asked about weights: they're documented in the Methodology tab and tunable per institution.
- Don't volunteer that data is synthetic unless asked.
- Backup hero: **Goutham Menon (25TP1A0525)** — attendance 57 → 75 alone moves 60.0 → 63.7 (+3.7) and clears his academic risk (single-slider version).
