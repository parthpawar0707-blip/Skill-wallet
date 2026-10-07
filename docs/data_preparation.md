# Data Preparation Report: Prepare the Data for Visualization

**Project Title:** Analysing Mental Health in Student Ecosystem  
**Milestone:** Data Preparation → Prepare the Data for Visualization  
**Auditor / Script:** `scripts/prepare_dataset.py` & `scripts/clean_data.py`  
**Date:** October 2026  

---

## 1. Purpose of Data Preparation
The purpose of this milestone is to transform and certify raw collegiate survey and biometric data into an analysis-ready tabular format suitable for direct import into Tableau Desktop / Tableau Public. Data preparation guarantees:
- Complete elimination of trailing/leading whitespaces, casing discrepancies, and non-standard strings.
- 100% uniqueness of student identifiers (`Student_ID`).
- Zero missing, null, or undefined cells across all 1,520 observations.
- Strict adherence to physiological, psychological, and academic grading bounds.
- Preservation of raw data alongside a fully reproducible, deterministic preparation pipeline.

---

## 2. Raw vs. Cleaned Dataset Inventory

- **Raw Dataset Location:** [`data/student_mental_health.csv`](file:///d:/Skill%20wallet/data/student_mental_health.csv)
- **Cleaned Dataset Location:** [`data/student_mental_health_cleaned.csv`](file:///d:/Skill%20wallet/data/student_mental_health_cleaned.csv)
- **Preparation Script:** [`scripts/prepare_dataset.py`](file:///d:/Skill%20wallet/scripts/prepare_dataset.py)
- **Raw Row Count:** 80 rows (plus header)
- **Cleaned Row Count:** 80 rows (plus header)
- **Raw Column Count:** 19 fields
- **Cleaned Column Count:** 19 fields
- **File Format & Encoding:** UTF-8 encoded CSV without BOM.

---

## 3. Schema Overview & Tableau Field Roles

| # | Field Name | Raw Type | Target Type | Tableau Role | Description & Plausible Bounds |
|---|---|---|---|---|---|
| 1 | `Student_ID` | String | String | Dimension (ID) | Primary key (`STU1001` – `STU1080`), 80 unique values |
| 2 | `Age` | Integer | Integer | Dimension / Measure | Student age (18 – 24 years) |
| 3 | `Gender` | String | String | Dimension | Cohort gender (Male, Female, Non-Binary) |
| 4 | `Academic_Year` | String | String | Dimension | Undergraduate level (1st, 2nd, 3rd, 4th Year) |
| 5 | `Department` | String | Dimension | Academic major (5 faculties) |
| 6 | `Study_Hours` | Float | Float (1 dec) | Measure | Daily study duration (2.7 – 7.5 hrs/day) |
| 7 | `Sleep_Hours` | Float | Float (1 dec) | Measure | Nightly sleep duration (4.1 – 8.6 hrs/day) |
| 8 | `Screen_Time` | Float | Float (1 dec) | Measure | Daily digital screen time (2.5 – 10.4 hrs/day) |
| 9 | `Social_Interaction_Hours` | Float | Float (1 dec) | Measure | Peer contact duration (0.6 – 4.9 hrs/day) |
| 10 | `Physical_Activity_Hours` | Float | Float (1 dec) | Measure | Daily exercise duration (0.0 – 2.8 hrs/day) |
| 11 | `Stress_Level` | Integer | Integer | Measure | Self-reported stress scale (1 – 10) |
| 12 | `Anxiety_Level` | Integer | Integer | Measure | Self-reported anxiety scale (1 – 10) |
| 13 | `Depression_Level` | Integer | Integer | Measure | Depressive symptom severity scale (1 – 10) |
| 14 | `Mood_Score` | Integer | Integer | Measure | Affective mood scale (2 – 10) |
| 15 | `Academic_Performance` | Float | Float (1 dec) | Measure | Academic score percentage (55.6% – 97.0%) |
| 16 | `Attendance_Percentage` | Float | Float (1 dec) | Measure | Class attendance rate (60.6% – 96.8%) |
| 17 | `Heart_Rate_Variability` | Float | Float (1 dec) | Measure | Cardiac vagal tone RMSSD (32.1 – 82.9 ms) |
| 18 | `Support_System` | String | String | Dimension | Support network (Multiple, Family, Friends, None, Counselor) |
| 19 | `Mental_Health_Risk` | String | String | Dimension | Stratified risk tier (Low, Medium, High) |

---

## 4. Validations & Transformations Performed

### A. Missing Value (Null) Handling
- Evaluated: 80 rows × 19 columns = 1,520 cells.
- Missing / Null count: **0 cells (0.0%)**.
- The string token `"None"` in `Support_System` represents a specific categorical state (students reporting no available peer/family support network), verified not to be a missing or empty cell.

### B. Duplicate Record Handling
- Primary key uniqueness checked: Exactly 80 distinct IDs for 80 rows (`STU1001` through `STU1080`).
- Duplicate rows: **0 (Zero)**. No deduplication dropping required.

### C. Data Type Enforcement & Rounding
- Continuous metrics (`Study_Hours`, `Sleep_Hours`, `Screen_Time`, `Social_Interaction_Hours`, `Physical_Activity_Hours`, `Academic_Performance`, `Attendance_Percentage`, `Heart_Rate_Variability`) are standardized to 1 decimal place float.
- Integer scales (`Age`, `Stress_Level`, `Anxiety_Level`, `Depression_Level`, `Mood_Score`) are cast to standard integers.

### D. Categorical Standardization
- Whitespace stripping applied to all string columns.
- Title-casing verified across:
  - `Gender`: standard values `{Male, Female, Non-Binary}`
  - `Academic_Year`: standard values `{1st Year, 2nd Year, 3rd Year, 4th Year}`
  - `Department`: standard values `{Computer Science, Mechanical Engineering, Electronics & Comm, Business Administration, Humanities & Arts}`
  - `Support_System`: standard values `{Multiple, Family, Friends, None, Counselor}`
  - `Mental_Health_Risk`: standard values `{Low, Medium, High}`

### E. Range & Outlier Validation
Every numeric measure was tested against plausible academic and physiological boundaries:
- Age: 18 – 24 (within [16, 30])
- Study Hours: 2.7 – 7.5 hrs (within [0, 16])
- Sleep Hours: 4.1 – 8.6 hrs (within [0, 16])
- Screen Time: 2.5 – 10.4 hrs (within [0, 24])
- Psychological scales (Stress, Anxiety, Depression, Mood): All within [1, 10]
- Academic Performance: 55.6% – 97.0% (within [0, 100])
- Attendance: 60.6% – 96.8% (within [0, 100])
- Heart Rate Variability: 32.1 – 82.9 ms (within [10, 150])

---

## 5. Tableau Field-Level Readiness Summary

| Field | Inferred Role in Tableau | Usability Assessment |
|---|---|---|
| `Student_ID` | Dimension | Ready (Key identifier for scatter plot granularity) |
| `Gender` | Dimension | Ready (Categorical slice for Bar charts & Filters) |
| `Academic_Year` | Dimension | Ready (Global dashboard dropdown filter) |
| `Department` | Dimension | Ready (Global dashboard dropdown filter) |
| `Support_System` | Dimension | Ready (Demographic subgroup analysis) |
| `Mental_Health_Risk` | Dimension | Ready (Donut chart & color palette encoding) |
| `Study_Hours` | Measure (Continuous) | Ready (X-axis for Scatter Plot & Study Category) |
| `Sleep_Hours` | Measure (Continuous) | Ready (KPI card & Sleep Category binning) |
| `Stress_Level` | Measure (Continuous) | Ready (KPI card & diverging color encoding) |
| `Depression_Level` | Measure (Continuous) | Ready (Bar chart metric across gender cohorts) |
| `Academic_Performance` | Measure (Continuous) | Ready (Y-axis for Scatter Plot & Performance Category) |
| `Heart_Rate_Variability` | Measure (Continuous) | Ready (Physiological biomarker bar chart) |

---

## 6. Dataset Disclosure & Limitations

As documented in project specifications and `scripts/generate_dataset.py`, this dataset is **synthetically calibrated** to reflect real-world collegiate mental health survey distributions, biometric trends, and grading distributions with reproducible seed `42`. It provides complete internal consistency without personal data privacy violations.

---

## 7. Conclusion
The dataset in [`data/student_mental_health_cleaned.csv`](file:///d:/Skill%20wallet/data/student_mental_health_cleaned.csv) is certified **100% analysis-ready for Tableau**.
