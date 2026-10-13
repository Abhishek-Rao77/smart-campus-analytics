# Smart Campus Analytics — Synthetic Dataset

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
