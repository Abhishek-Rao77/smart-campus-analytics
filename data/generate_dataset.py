"""
Synthetic student dataset generator for the Smart Campus Analytics hackathon prototype.
Indian engineering college context. Fixed seed (42) -> reproducible.

Segments (deliberate, for demo):
  - at_risk (15%): low attendance (<60) + low CGPA + backlogs
  - seg_b  (10%): high academics (CGPA > 8.5) but low placement readiness
  - seg_c  (10%): high engagement (events/hackathons) but weak academics (CGPA < 6.5)
  - healthy (65%): realistic correlated mix
"""
import numpy as np
import pandas as pd
from pathlib import Path

SEED = 42
N = 200
OUT = Path(__file__).resolve().parent / "data"
OUT.mkdir(parents=True, exist_ok=True)

rng = np.random.default_rng(SEED)

male_first = ["Aarav", "Arjun", "Aditya", "Rahul", "Rohan", "Sai", "Vikram",
              "Karthik", "Nikhil", "Varun", "Anil", "Deepak", "Harish", "Manish",
              "Pavan", "Rakesh", "Sandeep", "Suresh", "Teja", "Vishal",
              "Abhishek", "Akash", "Chaitanya", "Dinesh", "Goutham", "Kiran",
              "Pranav", "Ravi", "Srinivas", "Yash"]
female_first = ["Aishwarya", "Ananya", "Divya", "Kavya", "Lakshmi", "Meera",
                "Neha", "Pooja", "Priya", "Ritu", "Sahana", "Shreya", "Sneha",
                "Swathi", "Tanvi", "Vaishnavi", "Anitha", "Deepika", "Geetha",
                "Harika", "Kavitha", "Mounika", "Nandini", "Pallavi", "Ramya",
                "Sravani", "Supriya", "Vani", "Yamini", "Zoya"]
last = ["Sharma", "Reddy", "Rao", "Gupta", "Patel", "Khan", "Iyer", "Nair",
        "Das", "Kumar", "Singh", "Chowdary", "Varma", "Joshi", "Mehta",
        "Agarwal", "Bose", "Chandra", "Devi", "Menon", "Pillai", "Rajan",
        "Saxena", "Tiwari", "Verma", "Yadav", "Mishra", "Pandey", "Kulkarni",
        "Deshmukh"]


def C(x, lo, hi):
    return float(np.clip(x, lo, hi))


def ri(x, lo, hi):  # rounded int within bounds
    return int(np.clip(round(x), lo, hi))


# ---- segment assignment -----------------------------------------------------
idx = rng.permutation(N)
seg = np.array(["healthy"] * N, dtype=object)
seg[idx[:30]] = "at_risk"          # 15%
seg[idx[30:50]] = "seg_b"          # 10% high academics / low placement
seg[idx[50:70]] = "seg_c"          # 10% high engagement / weak academics

rows = []
for i in range(N):
    s = seg[i]
    sid = f"STU{i + 1:03d}"
    gender = "M" if rng.random() < 0.55 else "F"
    first = rng.choice(male_first if gender == "M" else female_first)
    name = f"{first} {rng.choice(last)}"
    branch = rng.choice(["CSE", "ECE", "IT"], p=[0.45, 0.30, 0.25])
    year = int(rng.choice([2, 3, 4], p=[0.35, 0.35, 0.30]))
    section = rng.choice(["A", "B", "C"])

    if s == "at_risk":
        overall = rng.uniform(40, 59)
        cgpa = rng.uniform(4.5, 6.4)
        backlogs = int(rng.choice([1, 1, 2, 2, 3, 4]))
        logins = ri(rng.uniform(0, 2), 0, 10)
        assign = rng.uniform(20, 50)
        quiz = rng.uniform(30, 55)
        video = rng.uniform(0, 3)
        events = ri(rng.uniform(0, 2), 0, 15)
        clubs = ri(rng.uniform(0, 1), 0, 3)
        hacks = 0
        certs = ri(rng.uniform(0, 1), 0, 5)
        apt = rng.uniform(20, 45)
        cod = rng.uniform(20, 45)
        mocks = ri(rng.uniform(0, 1), 0, 6)
        mock_avg = rng.uniform(30, 55)
        tech = rng.uniform(25, 50)
        soft = rng.uniform(30, 55)
        comm = rng.uniform(30, 55)
        sat = ri(rng.uniform(2, 4), 1, 5)
        fac = ri(rng.uniform(2, 3.4), 1, 5)

    elif s == "seg_b":
        overall = rng.uniform(78, 96)
        cgpa = rng.uniform(8.6, 9.6)
        backlogs = 0
        logins = ri(rng.uniform(4, 7), 0, 10)
        assign = rng.uniform(85, 100)
        quiz = rng.uniform(75, 95)
        video = rng.uniform(4, 10)
        events = ri(rng.uniform(2, 5), 0, 15)
        clubs = ri(rng.uniform(1, 2), 0, 3)
        hacks = ri(rng.uniform(0, 1), 0, 6)
        certs = ri(rng.uniform(1, 2), 0, 5)
        apt = rng.uniform(25, 44)          # deliberately low
        cod = rng.uniform(25, 44)          # deliberately low
        mocks = ri(rng.uniform(1, 3), 0, 6)
        mock_avg = rng.uniform(35, 55)
        tech = rng.uniform(55, 70)         # theory ok, test performance weak
        soft = rng.uniform(60, 85)
        comm = rng.uniform(60, 85)
        sat = ri(rng.uniform(3, 5), 1, 5)
        fac = ri(rng.uniform(4, 5), 1, 5)

    elif s == "seg_c":
        overall = rng.uniform(55, 75)
        cgpa = rng.uniform(5.0, 6.4)
        backlogs = int(rng.choice([0, 1, 1, 1, 2]))
        logins = ri(rng.uniform(2, 5), 0, 10)
        assign = rng.uniform(50, 75)
        quiz = rng.uniform(45, 65)
        video = rng.uniform(2, 6)
        events = ri(rng.uniform(6, 12), 0, 15)   # deliberately high
        clubs = ri(rng.uniform(2, 3), 0, 3)
        hacks = ri(rng.uniform(2, 5), 0, 6)     # deliberately high
        certs = ri(rng.uniform(2, 4), 0, 5)
        apt = rng.uniform(35, 60)
        cod = rng.uniform(35, 60)
        mocks = ri(rng.uniform(1, 2), 0, 6)
        mock_avg = rng.uniform(40, 60)
        tech = rng.uniform(40, 60)
        soft = rng.uniform(65, 90)         # sociable
        comm = rng.uniform(60, 85)
        sat = ri(rng.uniform(3, 5), 1, 5)
        fac = ri(rng.uniform(2, 4), 1, 5)

    else:  # healthy mix, correlated
        ability = float(np.clip(rng.normal(7.6, 0.9), 6.0, 9.8))
        cgpa = C(ability + rng.normal(0, 0.25), 4.0, 10.0)
        backlogs = int(rng.choice([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2],
                                  p=[0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10,
                                     0.10, 0.06, 0.06, 0.03, 0.05]))
        overall = C(rng.normal(85, 8), 65, 99)
        logins = ri(rng.normal(4, 1.5), 1, 8)
        assign = C(cgpa * 10 + rng.normal(0, 6), 55, 100)
        quiz = C(cgpa * 8.5 + rng.normal(0, 6), 40, 100)
        video = C(rng.normal(4, 2), 0, 12)
        events = ri(abs(rng.normal(2.5, 2)), 0, 10)
        clubs = ri(abs(rng.normal(1, 0.8)), 0, 3)
        hacks = ri(abs(rng.normal(0.7, 0.9)), 0, 4)
        certs = ri(abs(rng.normal(1, 1)), 0, 4)
        apt = C(cgpa * 9 + rng.normal(0, 8), 25, 98)
        cod = C(cgpa * 8.5 + rng.normal(0, 9), 25, 98)
        mocks = ri(rng.normal(2.5, 1.2), 0, 6)
        mock_avg = C((apt + cod) / 2 + rng.normal(0, 6), 20, 95)
        tech = C(cod + rng.normal(0, 7), 20, 100)
        soft = C(rng.normal(65, 12), 25, 100)
        comm = C(rng.normal(62, 12), 25, 100)
        sat = ri(rng.normal(3.8, 0.8), 1, 5)
        fac = ri(cgpa / 2.4 + rng.normal(0, 0.5), 1, 5)

    # attendance drives marks: low attendance -> lower marks (consistency)
    att_effect = (overall - 75) * 0.15
    base = cgpa * 9.3 + att_effect
    sem1 = C(base + rng.normal(0, 3.5), 30, 100)
    sem2 = C(base + rng.normal(0, 3.5), 30, 100)
    sem3 = C(base + rng.normal(0, 3.5), 30, 100)
    maths = C(base + rng.normal(0, 4), 30, 100)
    coding_sub = C(base + rng.normal(0, 4), 30, 100)

    maths_att = C(overall + rng.normal(0, 4), 0, 100)
    coding_att = C(overall + rng.normal(0, 4), 0, 100)
    physics_att = C(overall + rng.normal(0, 4), 0, 100)

    rows.append({
        "student_id": sid, "name": name, "branch": branch, "year": year,
        "section": section, "gender": gender, "segment": s,
        "cgpa": round(cgpa, 2), "backlogs": backlogs,
        "sem1_marks": round(sem1, 1), "sem2_marks": round(sem2, 1),
        "sem3_marks": round(sem3, 1),
        "maths_marks": round(maths, 1), "coding_subject_marks": round(coding_sub, 1),
        "overall_pct": round(overall, 1),
        "maths_att": round(maths_att, 1), "coding_att": round(coding_att, 1),
        "physics_att": round(physics_att, 1),
        "logins_per_week": logins,
        "assignment_completion_pct": round(assign, 1),
        "avg_quiz_score": round(quiz, 1), "video_hours": round(video, 1),
        "events_attended": events, "clubs": clubs, "hackathons": hacks,
        "certifications": certs,
        "aptitude_score": round(apt, 1), "coding_score": round(cod, 1),
        "mock_interviews": mocks, "mock_avg_score": round(mock_avg, 1),
        "tech_skill_score": ri(tech, 0, 100),
        "soft_skill_score": ri(soft, 0, 100),
        "communication_score": ri(comm, 0, 100),
        "satisfaction": sat, "faculty_remarks_score": fac,
    })

df = pd.DataFrame(rows)

# ---- split into per-source CSVs (challenge: disconnected sources) -------------
# NOTE: 'segment' is a generator-only label (ground truth for the demo team);
# it is intentionally NOT shipped in any CSV.
students = df[["student_id", "name", "branch", "year", "section", "gender"]]
academics = df[["student_id", "cgpa", "backlogs", "sem1_marks", "sem2_marks",
                "sem3_marks", "maths_marks", "coding_subject_marks"]]
attendance = df[["student_id", "overall_pct", "maths_att", "coding_att",
                 "physics_att"]]
lms = df[["student_id", "logins_per_week", "assignment_completion_pct",
          "avg_quiz_score", "video_hours"]]
engagement = df[["student_id", "events_attended", "clubs", "hackathons",
                 "certifications"]]
placement = df[["student_id", "aptitude_score", "coding_score",
                "mock_interviews", "mock_avg_score"]]
skills = df[["student_id", "tech_skill_score", "soft_skill_score",
             "communication_score"]]
feedback = df[["student_id", "satisfaction", "faculty_remarks_score"]]

files = {"students": students, "academics": academics, "attendance": attendance,
         "lms": lms, "engagement": engagement, "placement": placement,
         "skills": skills, "feedback": feedback}
for fname, fdf in files.items():
    fdf.to_csv(OUT / f"{fname}.csv", index=False)

# ---- verification ------------------------------------------------------------
loaded = {f: pd.read_csv(OUT / f"{f}.csv") for f in files}
ref_ids = set(loaded["students"]["student_id"])
assert all(len(v) == N for v in loaded.values()), "row count mismatch"
assert all(set(v["student_id"]) == ref_ids for v in loaded.values()), \
    "student_id mismatch across files"
assert loaded["students"]["student_id"].is_unique, "duplicate student_ids"

checks = {
    "cgpa 0-10": loaded["academics"]["cgpa"].between(0, 10).all(),
    "backlogs 0-4": loaded["academics"]["backlogs"].between(0, 4).all(),
    "attendance 0-100": loaded["attendance"].filter(like="_pct").le(100).all().all()
    and loaded["attendance"].filter(like="att").ge(0).all().all(),
    "satisfaction 1-5": loaded["feedback"]["satisfaction"].between(1, 5).all(),
    "faculty 1-5": loaded["feedback"]["faculty_remarks_score"].between(1, 5).all(),
    "placement 0-100": loaded["placement"][["aptitude_score", "coding_score"]]
    .le(100).all().all(),
    "no nulls": all(v.notna().all().all() for v in loaded.values()),
}
assert all(checks.values()), {k: v for k, v in checks.items() if not v}

# ---- segment sanity report -----------------------------------------------------
print("rows per file:", {f: len(v) for f, v in loaded.items()})
print("all 200 student_ids consistent across 8 files: True")
print("\nsegment mix:")
print(df["segment"].value_counts().to_string())
print("\nsegment means (cgpa / attendance / aptitude / events / backlogs):")
print(df.groupby("segment")[["cgpa", "overall_pct", "aptitude_score",
      "events_attended", "backlogs"]].mean().round(1).to_string())
print("\nchecks passed:", checks)

# ---- README --------------------------------------------------------------------
readme = """# Smart Campus Analytics — Synthetic Dataset

Reproducible synthetic data for the hackathon prototype (Indian engineering
college context). Generated with `generate_dataset.py` using **fixed random
seed 42** (numpy). 200 students, one CSV per source system — mirroring the
challenge's "disconnected sources" premise. Join key: `student_id` (STU001–STU200).

## Files

| File | Columns |
|---|---|
| `students.csv` | student_id, name, branch (CSE/ECE/IT), year (2/3/4), section (A/B/C), gender (M/F) |
| `academics.csv` | student_id, cgpa (0–10), backlogs (0–4), sem1_marks, sem2_marks, sem3_marks (%), maths_marks (%), coding_subject_marks (%) |
| `attendance.csv` | student_id, overall_pct (%), maths_att (%), coding_att (%), physics_att (%) |
| `lms.csv` | student_id, logins_per_week, assignment_completion_pct (%), avg_quiz_score (%), video_hours |
| `engagement.csv` | student_id, events_attended, clubs (0–3), hackathons, certifications |
| `placement.csv` | student_id, aptitude_score (0–100), coding_score (0–100), mock_interviews, mock_avg_score (0–100) |
| `skills.csv` | student_id, tech_skill_score (0–100), soft_skill_score (0–100), communication_score (0–100) |
| `feedback.csv` | student_id, satisfaction (1–5), faculty_remarks_score (1–5) |

## Built-in demo segments

The generator deliberately plants segments for the prototype to discover
(segment labels are NOT in the CSVs — the dashboard should find them):

- **At-risk (~15%, 30 students):** attendance < 60%, low CGPA, 1–4 backlogs,
  weak LMS/placement/skill numbers.
- **High academics, low placement readiness (~10%, 20 students):** CGPA > 8.5
  but aptitude/coding test scores < 45 (theory-strong, test-weak).
- **High engagement, weak academics (~10%, 20 students):** many events /
  hackathons / clubs but CGPA < 6.5.
- **Healthy mix (~65%, 130 students):** realistic correlations — marks track
  CGPA, attendance nudges marks up/down, placement scores correlate with CGPA
  plus noise, LMS activity loosely tracks engagement.

## Regenerating

```bash
python3 generate_dataset.py
```

Requires `pandas` and `numpy`. The script asserts: 200 rows per file,
identical `student_id` sets across all files, no nulls, and valid value ranges.
"""
(OUT / "README.md").write_text(readme)
print("\nREADME.md written")
print("done")
