# Smart Campus Analytics

An AI-powered student success platform that predicts which students are at risk, explains why, and gives colleges one dashboard to act early.

**Live demo:** https://muse.ai/s/smart-campus-analytics-online-xjr6xi6xapxbdxef

Built for the HacXlerate national hackathon — *"Smart Campus Analytics: Predict, Optimize & Improve Student Success."*

## The problem

Colleges collect attendance, marks, LMS activity and feedback — but it sits scattered across registers and spreadsheets. By the time a student is visibly failing, it is too late to help. Mentors and HODs have no single view of who needs attention, or why.

## The solution

Smart Campus Analytics pulls a college's student data into one place and computes a **Student Success Score** for every student. It flags at-risk students with plain-English explanations, segments students so mentors can target help, and includes a what-if simulator: move the attendance / assignment-completion / aptitude sliders and the score and risk flags update live.

## What's in this repo

| Folder | Contents |
|---|---|
| `data/` | Synthetic dataset — 200 students across 8 tables (`students`, `academics`, `attendance`, `lms`, `engagement`, `placement`, `skills`, `feedback`), plus the reproducible generator (`generate_dataset.py`, fixed seed 42) |
| `dashboard/` | Interactive HTML dashboard prototype — KPIs, student filters, explainable score details, intervention suggestions, what-if simulator. Open `dashboard.html` in any browser, no server needed |
| `demo/` | Demo slide deck (`.pptx`) and the full 2-minute demo script with answers to likely judge questions |
| `docs/` | HacXlerate Round 1 submission write-up |

## How the score works

The score is built from attendance, assignment-completion and aptitude/academic signals in the integrated data. Every at-risk flag ships with a plain-English reason (e.g. "attendance dropped below 60% this month"), so a mentor knows what to act on instead of guessing.

## Regenerate the dataset

```bash
cd data
python generate_dataset.py
```

## Tech stack

Python data pipeline (synthetic dataset generation + scoring engine), interactive HTML dashboard prototype, and a full-stack web app with register/login, role-based dashboards (Student, Teacher, HOD, Principal, Staff, Parent) and a per-account student database.

> Note: the full-stack app with authentication runs privately and is not part of this repo. The live demo link above is a public showcase version.

## Team

[Team member names]
