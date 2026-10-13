# Smart Campus Analytics — HacXlerate Round 1 Write-up

## One line
An AI-powered student success platform that predicts which students are at risk, explains why, and gives colleges one dashboard to act early.

## The problem
Colleges collect attendance, marks, LMS activity and feedback — but it sits scattered across registers and spreadsheets. By the time a student is visibly failing, it is too late to help. Mentors and HODs have no single view of who needs attention, or why.

## The solution
Smart Campus Analytics pulls a college's student data into one place and computes a **Student Success Score** for every student. It flags at-risk students with plain-English explanations (e.g. "attendance dropped below 60% this month"), segments students so mentors can target help, and includes a what-if simulator: move the attendance / assignment-completion / aptitude sliders and the score and risk flag update live, so a mentor can see exactly what would turn a student around.

## What we built (maps to the brief)
- **Data integration** — attendance, academics, LMS engagement, skills, placements and feedback merged for 200 students (synthetic dataset, 8 tables)
- **Student Success Score** for every student
- **At-risk identification** with plain-English explanations for each flagged student
- **Interactive dashboard** prototype
- **Bonus:** student segmentation + explainable scores
- **What-if simulator** — attendance, assignment completion and aptitude sliders change the score and risk flags live
- **Full-stack app** — register, then login; student database kept in the app under your account; college-style roll numbers (like 25TP1A0590, with 99 → A0 → B0 numbering); add / edit / reset students
- **Campus operations** — separate staff login for the office team: certificates issued per student, counseling records, fee dues and payments
- **Points system** — Classroom-of-the-Elite style: earned for attendance, marks, hackathons, events and certifications; absences deduct (backlogs cost zero)
- **In-app courses** — Python and every subject, with completion certificates recorded in the student's log
- **AI study tutor** — unlimited, any subject, step-by-step problem solving, for every role

## How the score works
The score is built from attendance, assignment-completion and aptitude/academic signals in the integrated data. Every at-risk flag ships with a plain-English reason, so a mentor knows what to act on instead of guessing.

## Tech stack
Python data pipeline (synthetic dataset generation + scoring engine), interactive HTML dashboard prototype, and a full-stack web app with register/login and a per-account student database.

## Submission package
- Live app: [PASTE APP LINK]
- Demo video: [PASTE VIDEO LINK] (screen-recorded walkthrough of the app is stronger than the promo teaser if time allows)
- Slides: smart-campus-analytics-demo.pptx
- 2-minute demo script + answers to likely judge questions: ready

## Team
[TEAM MEMBER NAMES]

---
Deadline: tonight, 2026-10-13, 23:59:59 UTC (5:29 AM IST, Oct 14).
