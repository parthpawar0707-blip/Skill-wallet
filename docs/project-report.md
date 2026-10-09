# Comprehensive Project Report: Analysing Mental Health in Student Ecosystem

**Project Title:** Analysing Mental Health in Student Ecosystem  
**Author:** Parth Pawar  
**Program:** SkillWallet / SmartBridge Virtual Internship &bull; Data Analytics with Tableau  
**Domain:** Higher Education & Campus Wellness Analytics  
**Deployment URL:** https://parthpawar0707-blip.github.io/Skill-wallet/  
**Repository:** https://github.com/parthpawar0707-blip/Skill-wallet  
**Tableau Public Dashboard:** [Student Mental Health Analysis](https://public.tableau.com/views/Student_Mental_Health_Analysis_sufiyan_17913953791380/AnalysingMentalHealthinStudentEcosystem?:language=en-US&publish=yes)  

---

## 1. Introduction
Collegiate environments impose strenuous cognitive, social, and emotional demands on undergraduate students. Meeting demanding course deadlines, preparing for competitive examinations, managing sleep schedules, and coping with digital overload often lead to severe psychological strain. Unaddressed chronic distress diminishes student quality of life, suppresses academic achievement, and leads to university attrition.

This project delivers an end-to-end data analytics and business intelligence solution to systematically analyze, visualize, and monitor mental health dynamics across a student ecosystem. By bridging demographic data, daily lifestyle habits, subjective psychological ratings, physiological telemetry (Heart Rate Variability), and academic performance metrics into an interactive Tableau dashboard and responsive portfolio website, this study provides actionable insights for proactive student support.

---

## 2. Problem Statement
Historically, university counseling departments and academic advisors have operated in silos. Mental health surveys are rarely conducted dynamically, while student records and grade databases reside in separate systems. Consequently, institutional awareness of student distress typically occurs reactively—after a student has failed multiple classes, accumulated excessive absenteeism, or withdrawn entirely. There is an acute need for a unified, real-time analytical framework to visualize how everyday lifestyle choices and autonomic stress signals correlate with academic success.

---

## 3. Project Objectives
1. **Audit & Validate Multi-Dimensional Data:** Evaluate 1,000 collegiate profiles across 16 clinical, behavioral, and academic dimensions for 100% data hygiene.
2. **Quantify Inter-Variable Dynamics:** Model how sleep duration, screen time, study habits, and social interaction correlate with stress, anxiety, and depression.
3. **Incorporate Objective Physiological Telemetry:** Utilize Heart Rate Variability (HRV in milliseconds) as an autonomic biomarker to substantiate self-reported survey scores.
4. **Engineer an Interactive Tableau BI Dashboard:** Develop executive KPI scorecards, multi-dimensional worksheets, and synchronized filters for dynamic slicing.
5. **Deploy a Portfolio Web Application:** Host a portfolio website on GitHub Pages with automated GitHub Actions CI/CD and direct Tableau embed.
6. **Produce a Full Video Walkthrough:** Record a 5–7 minute walkthrough in natural Indian English.

---

## 4. Dataset Description & Provenance
The project dataset was verified directly from the project data source ([Google Spreadsheet](https://docs.google.com/spreadsheets/d/1DSnFv7DdV8l1nBcQ-KNIrbgnmDMIDeh7/edit?usp=sharing)).

- **Cohort Size:** 1,000 undergraduate student records
- **Total Variables:** 16 fields
- **Data Completeness:** 100% (0 nulls across 16,000 cells)
- **Primary Key Uniqueness:** Exactly 1,000 distinct `Student_ID` values

### Attribute Categorization
| Category | Variables | Scale / Units | Description |
|---|---|---|---|
| Demographics | `Student_ID`, `Age`, `Gender` | Numeric / Categorical | Identification, Age (18–25), Gender (Male, Female, Other) |
| Psychological | `Stress_Level`, `Anxiety_Level`, `Depression_Level` | Integer (1–10) | Standardized self-reported psychological rating scales |
| Lifestyle | `Sleep_Duration_Hours`, `Study_Hours_Per_Day`, `Social_Interaction_Score` | Float / Integer | Daily habits and peer engagement (1–9) |
| Academic | `Academic_Performance_Index`, `Attendance_Rate (%)`, `LMS_Activity_Score` | Percentage / Score | Academic achievement (50–100%), attendance (60–100%), LMS portal score (10–99) |
| Biometrics | `Heart_Rate_Variability` | Float (ms) | Autonomic cardiac vagal tone / RMSSD (36.6–99.2 ms) |
| Interventions | `Mental_Health_Risk`, `Personalized_Intervention_Strategy` | Categorical | Risk stratification (Low, Medium, High) and 8 support pathways |

---

## 5. Data Inspection, Cleaning & Preparation
- **Missing Value Audit:** Automated check via `scripts/analyze_dataset.py` identified zero null or empty cells.
- **Duplicate Check:** Verified zero duplicate records.
- **Outlier Bounds:** Numerical measures verified within plausible clinical and collegiate boundaries.
- **Student Privacy:** Individual emotional journal entries and row-level records are preserved privately, with only aggregate metrics published to public web assets.

---

## 6. Calculated Fields & Feature Engineering
1. **Age Cohorts (`Age_Group`):**
   - `Below 20`: Age < 20 (250 students, 25.0%)
   - `20–22`: Age 20 to 22 (384 students, 38.4%)
   - `23–25`: Age 23 to 25 (366 students, 36.6%)
2. **Study Intensity (`Study_Category`):**
   - `Light`: < 3.0 hrs/day
   - `Moderate`: 3.0 to 5.5 hrs/day
   - `Intensive`: > 5.5 hrs/day
3. **Sleep Hygiene Category (`Sleep_Category`):**
   - `Deprived`: < 6.0 hrs/day
   - `Adequate`: 6.0 to 7.5 hrs/day
   - `Optimal`: > 7.5 hrs/day

---

## 7. Interactive Tableau Dashboard Architecture
The published Tableau dashboard integrates:
- **Executive Scorecard:** Total Students (1,000), Avg Stress (5.45), Avg Depression (5.50), Avg Sleep (6.49 hrs), Avg Attendance (79.96%), Avg Academic Index (75.12%), and Avg HRV (69.71 ms).
- **Viz 1 (Study Hours vs Performance):** Demonstrates non-linear returns where moderate study achieves high grades without acute stress.
- **Viz 2 & 4 (Demographic Cohort Analysis):** Highlights that mental strain is evenly distributed across gender groups, requiring systemic rather than gender-exclusive solutions.
- **Viz 3 (Student Scatter Plot):** Displays student-level granularity with linear regression trendlines.
- **Viz 5 (HRV Biometric Telemetry):** Demonstrates suppressed HRV (<50 ms) in severely distressed students.
- **Viz 6 (Risk Tier Donut):** Visualizes cohort stratification: Low Risk (41.4%), Medium Risk (34.7%), and High Risk (23.9%).

---

## 8. Empirical Findings & Institutional Insights
1. **Sleep as an Emotional Buffer:** Students achieving &ge; 7.5 hours of sleep reported average stress scores of 4.8, compared to 6.2 for students sleeping < 6.0 hours.
2. **Diminishing Study Returns:** Beyond 5.5 hours of daily study, academic performance gains level off when anxiety exceeds 7/10.
3. **Social Buffering:** Peer interaction scores &ge; 6 strongly correlate with reduced depression severity (avg 4.6 vs 6.1 for isolated students).
4. **Targeted Interventions:** 23.9% of the student body requires priority counseling, validating automated screening tools.

---

## 9. Web Integration & CI/CD Deployment
A responsive, accessible portfolio website was built using standard HTML5/CSS/JavaScript and hosted via GitHub Pages:
- Live Tableau Public embed with reload and external launch capabilities.
- Integrated HTML5 video player streaming the narrated demonstration video with subtitles.
- Automated GitHub Actions deployment (`.github/workflows/deploy.yml`) publishing the `site/` directory on pushes to `main`.

---

## 10. Limitations & Responsible Use
- **Observational Nature:** Correlational patterns do not establish direct clinical causation.
- **Educational Scope:** This project is an academic decision-support model, not an automated clinical diagnostic tool.
- **Data Privacy:** Raw emotional journals are kept confidential to respect student privacy.

---

## 11. Conclusion & Future Scope
This project demonstrates how data analytics and interactive business intelligence can transform campus surveys and physiological telemetry into actionable wellness insights. Future expansions could incorporate real-time wearable API streams, semester-long longitudinal tracking, and automated advising alerts.
