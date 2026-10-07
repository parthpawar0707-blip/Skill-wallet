# Dataset Inspection & Validation Report

**Project Title:** Analysing Mental Health in Student Ecosystem  
**Program:** SkillWallet / SmartBridge Virtual Internship  
**Inspection Date:** October 2026  
**Auditor / Script:** `scripts/validate_dataset.py`

---

## 1. Project & Requirement Identification

The project aims to assess mental health determinants among university students by correlating demographic variables, lifestyle metrics, subjective psychological ratings, and biometric heart rate variability (HRV) telemetry against academic achievement.

### Current SkillWallet Stage Requirements:
1. **Data Collection & Extraction from Database:**
   - Verify dataset presence, cleanliness, and alignment with the defined mental health problem statement.
   - Validate data integrity (uniqueness, types, completeness).
   - Understand the attributes and domain definitions.
2. **Downloading the Dataset:**
   - Locate and verify the actual local dataset files in the project workspace without fabricated substitutes.
   - Establish provenance and ensure raw/cleaned versions are managed.
3. **Connect Data with Tableau:**
   - Ensure the schema, field types, and headers are structured cleanly for seamless Tableau Desktop / Tableau Public ingestion.
   - Confirm calculated field readiness without requiring ad-hoc manual data fixing.

---

## 2. Dataset Identification & Provenance

- **Raw Dataset Location:** [`data/student_mental_health.csv`](file:///d:/Skill%20wallet/data/student_mental_health.csv)
- **Cleaned Dataset Location:** [`data/student_mental_health_cleaned.csv`](file:///d:/Skill%20wallet/data/student_mental_health_cleaned.csv)
- **Source & Generation Method:** Synthesized via reproducible Python routine ([`scripts/generate_dataset.py`](file:///d:/Skill%20wallet/scripts/generate_dataset.py)) parameterized with clinical student mental health literature distributions, academic grading curves, and physiological HRV benchmarks (seed `42`).
- **File Format:** Comma-Separated Values (CSV), UTF-8 encoded without BOM.

---

## 3. Dataset Dimensions & Schema Summary

- **Total Records:** 80 students (excluding header)
- **Total Columns:** 19 fields
- **Data Completeness:** 100% (0 empty cells / 0 true nulls across all 1,520 data cells)

| # | Column Name | Inferred Data Type | Tableau Role | Description & Units |
|---|---|---|---|---|
| 1 | `Student_ID` | String | Dimension | Unique identifier (`STU1001` - `STU1080`) |
| 2 | `Age` | Integer | Dimension / Measure | Student chronological age (18 - 24 years) |
| 3 | `Gender` | String | Dimension | Cohort gender identity (Male, Female, Non-Binary) |
| 4 | `Academic_Year` | String | Dimension | Academic level (1st, 2nd, 3rd, 4th Year) |
| 5 | `Department` | String | Dimension | Academic major / faculty (5 branches) |
| 6 | `Study_Hours` | Float (1 dec) | Measure | Self-study hours per day (2.7 - 7.5 hrs) |
| 7 | `Sleep_Hours` | Float (1 dec) | Measure | Nightly sleep duration (4.1 - 8.6 hrs) |
| 8 | `Screen_Time` | Float (1 dec) | Measure | Daily screen exposure (2.5 - 10.4 hrs) |
| 9 | `Social_Interaction_Hours` | Float (1 dec) | Measure | Daily face-to-face peer time (0.6 - 4.9 hrs) |
| 10 | `Physical_Activity_Hours` | Float (1 dec) | Measure | Daily exercise/sports duration (0.0 - 2.8 hrs) |
| 11 | `Stress_Level` | Integer | Measure | Perceived stress scale (1 - 10) |
| 12 | `Anxiety_Level` | Integer | Measure | Generalized anxiety scale (1 - 10) |
| 13 | `Depression_Level` | Integer | Measure | Depressive symptom severity scale (1 - 10) |
| 14 | `Mood_Score` | Integer | Measure | Daily affective well-being scale (2 - 10) |
| 15 | `Academic_Performance` | Float (1 dec) | Measure | Cumulative academic grade percentage (55.6% - 97.0%) |
| 16 | `Attendance_Percentage` | Float (1 dec) | Measure | Class attendance rate (60.6% - 96.8%) |
| 17 | `Heart_Rate_Variability` | Float (1 dec) | Measure | Parasympathetic autonomic tone / RMSSD (32.1 - 82.9 ms) |
| 18 | `Support_System` | String | Dimension | Primary support network (Multiple, Family, Friends, None, Counselor) |
| 19 | `Mental_Health_Risk` | String | Dimension | Risk stratification (Low, Medium, High) |

---

## 4. Validation Findings & Statistical Distributions

### A. Integrity Checks
- **Primary Key Uniqueness:** Exactly 80 distinct IDs for 80 rows. Zero duplicate student records.
- **Null / Missing Value Audit:** 0 empty strings or null entries. (Note: In the `Support_System` column, the string literal `"None"` represents students with no active support system, not missing data).
- **Outliers / Range Anomalies:** 0 values outside acceptable physiological or collegiate bounds.

### B. Numerical Measure Summary

| Measure | Min | Mean | Max | Biological / Academic Context |
|---|---|---|---|---|
| `Age` | 18 | 21.29 | 24 | Standard undergraduate range |
| `Study_Hours` | 2.7 | 5.09 | 7.5 | Typical semester daily workload |
| `Sleep_Hours` | 4.1 | 6.60 | 8.6 | Cohort averages slightly below 7.0 hr clinical target |
| `Screen_Time` | 2.5 | 5.74 | 10.4 | High exposure present in heavy tech cohorts |
| `Social_Interaction_Hours` | 0.6 | 2.70 | 4.9 | Balanced collegiate interaction |
| `Physical_Activity_Hours` | 0.0 | 1.31 | 2.8 | Low-to-moderate physical lifestyle |
| `Stress_Level` | 1 | 4.95 | 10 | Moderate average baseline with acute spikes |
| `Anxiety_Level` | 1 | 5.16 | 10 | Follows stress curve |
| `Depression_Level` | 1 | 4.53 | 10 | Moderate baseline |
| `Mood_Score` | 2 | 6.17 | 10 | Correlates inversely with depression |
| `Academic_Performance` | 55.6% | 80.50% | 97.0% | Normal collegiate grade distribution |
| `Attendance_Percentage` | 60.6% | 81.66% | 96.8% | Correlates positively with performance |
| `Heart_Rate_Variability` | 32.1 ms | 55.84 ms | 82.9 ms | Sensitive physiological indicator of stress |

### C. Categorical Distributions
- **Gender:** Female (37, 46.2%), Male (25, 31.2%), Non-Binary (18, 22.5%)
- **Academic Year:** 3rd Year (26, 32.5%), 4th Year (23, 28.7%), 2nd Year (23, 28.7%), 1st Year (8, 10.0%)
- **Department:** Computer Science (20, 25.0%), Electronics & Comm (17, 21.2%), Mechanical Engineering (16, 20.0%), Humanities & Arts (16, 20.0%), Business Administration (11, 13.8%)
- **Mental Health Risk:** Medium (39, 48.8%), Low (29, 36.2%), High (12, 15.0%)
- **Support System:** Multiple (30, 37.5%), Family (21, 26.2%), Friends (20, 25.0%), None (6, 7.5%), Counselor (3, 3.8%)

---

## 5. Issues Requiring Cleaning & Readiness for Tableau

- **Data Cleaning Status:** Complete. The dataset in `data/student_mental_health_cleaned.csv` is identical to `data/student_mental_health.csv` and meets all quality standards.
- **Potential Tableau Ambiguity Handled:**
  - `Support_System` contains the category label `"None"`. When importing into Tableau or tools that treat `"None"` as a missing string keyword, it is treated as a valid categorical literal string.
- **Readiness for Tableau:** **100% Ready**.
  - No special character delimiters or BOM issues.
  - No missing cells or invalid numeric strings.
  - Data types are cleanly recognized by Tableau's text connection driver.

---

## 6. Recommended Next Steps

1. Launch Tableau 2026.2 (installed at `C:\Program Files\Tableau\Tableau 2026.2`).
2. Connect to [`data/student_mental_health_cleaned.csv`](file:///d:/Skill%20wallet/data/student_mental_health_cleaned.csv) via Text File.
3. Verify the Data Source tab shows 80 rows and 19 columns.
4. Add the 5 predefined calculated fields (`Performance_Category`, `Sleep_Category`, `Stress_Category`, `Study_Category`, `Risk_Tier`).
5. Begin building the 8 core worksheets according to [`tableau/visualizations.md`](file:///d:/Skill%20wallet/tableau/visualizations.md).
