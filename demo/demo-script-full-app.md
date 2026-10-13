# Smart Campus Analytics — full-app demo script

For the **full app** (register → login version). Rehearse the logins once before judges arrive — the role switching IS the demo.

## Accounts to register first (do this before the demo)

Register four demo accounts in the app, one per role:
- `student_demo` — **Student** (sees own data only)
- `teacher_demo` — **Teacher** (assigned **CSE-A and CSE-B only**)
- `hod_demo` — **HOD** (whole CSE department)
- `principal_demo` — **Principal** (all departments)

## Pre-demo checklist (5 minutes)

1. Log in as `teacher_demo` → try opening an unassigned class (e.g. ECE-A) → it must be **blocked**. If it opens, tell me immediately — that's the one thing that couldn't be verified end-to-end.
2. Confirm demo data is loaded: a club join request pending, one event in "proposed" state, and a student with the teacher-visibility toggle OFF.
3. Know your hero student: **Yamini Reddy (25TP1A0542)** — score 55.3, attendance 59%, aptitude 42, academic + placement risk. Simulator move: attendance **59 → 75**, aptitude **42 → 70** → score **55.3 → 60.3**, both flags clear.

## The run (2 minutes)

**0:00–0:15 — Problem + the hook**
> "Colleges run on disconnected systems — attendance in one place, marks in another, nobody sees the full student. We built one platform with four doors: student, teacher, HOD, principal — each sees exactly what they're allowed to, nothing more."

**0:15–0:45 — Roles, live**
- Log in as `student_demo`. "Yamini sees only her own scores, her mentor, her timetable, her clubs."
- Log out, log in as `teacher_demo`. "Her teacher sees only CSE-A and CSE-B — her assigned classes. Nothing else."
- Log in as `hod_demo`. "The HOD sees the whole department."
> "Four logins, four different worlds, one database. Access is enforced, not cosmetic."

**0:45–1:15 — Attendance (the feature judges touch)**
- As teacher: open CSE-A → pick **Period 3** from the timetable → mark two students **Absent** → Submit.
> "Attendance is per period, not per day. Every absent student triggers an alert to the parent automatically — and it's logged in the app's alert outbox."
- Start **self check-in**: "For speed, the teacher flashes a code instead. Students enter it — the code rotates every 30 seconds, one check-in per account, and last-second entries get flagged. Flagged check-ins count as present unless the teacher explicitly rejects them — only rejections trigger the parent alert."
- Flip to the **privacy toggle**: "And this student has locked her detailed scores — her teacher sees the class list but not her breakdowns until she grants permission. Mentors see their mentees plus parent contact numbers."

**1:15–1:50 — The closer: what-if simulator**
- Back to Yamini's profile: "Her score is 55.3 — low attendance at 59%, a backlog, placement readiness her biggest lever."
- Drag **attendance to 75**, **aptitude to 70**. "Score jumps to 60.3 — both risk flags clear. Faculty don't just see *who's* at risk; they see *which intervention works* before spending a semester on it."

**1:50–2:00 — Campus life close**
> "Same app runs campus life too — students request clubs, propose events, a teacher approves and picks a student co-organizer, and one Publish button makes it visible to everyone. Student success isn't just scores — it's everything around them. Happy to take questions."

## Deep dives (only if judges ask)

- **Clubs**: student browses → sends join request → admin approves. Memberships appear in the student's extracurriculars section.
- **Events**: student proposes (game, program, anything) → appointed teacher approves → teacher picks a student co-organizer → student can approve and add details → **Publish** makes it visible to everyone. Demo data covers proposed → approved → published.
- **Timetable**: HOD adjusts it; students see their class's version, teachers see only assigned classes.
- **Mentors**: every student has an assigned mentor; mentors see mentees and father's/mother's numbers.

## Likely judge questions (one-line answers)

1. **"How is the score computed?"**
   → "Six indicators with fixed weights — academic 35%, attendance 20%, LMS 15%, placement readiness 15%, skills 10%, engagement 5%. Flags fire below 50, 2+ backlogs, or attendance below 60%."
2. **"Is the data real?"**
   → "Synthetic — 200 students with realistic correlations to demonstrate the methodology end to end. The pipeline is source-agnostic and plugs into real college systems."
3. **"How do you stop fake self check-in attendance?"**
   → "Rotating 30-second codes, one check-in per login, expiring sessions, teacher live view with removal, and flagged late entries that only go absent on explicit rejection."
4. **"Do parent alerts actually send SMS?"**
   → "The app logs every alert in the outbox with timestamp and recipient. Real SMS delivery plugs in through any SMS gateway — the logic and audit trail are built."
5. **"How is teacher access actually enforced?"**
   → "Server-side on every class request — the teacher's assigned-class list is checked before any data is served. Try it live: I can't open ECE-A as a CSE-A/CSE-B teacher."
6. **"What makes this more than a dashboard?"**
   → "Dashboards report the past. The what-if simulator predicts the outcome of an intervention *before* you act — that's reporting vs. decision intelligence."

## Backup plan

If live logins are slow on the judges' network, fall back to `dashboard.html` (works offline) and walk the original script: KPIs → at-risk list → Yamini → what-if → close. The simulator alone wins rounds.
