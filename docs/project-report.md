# Comprehensive Project Report: Analysing Mental Health in Student Ecosystem

**Project Title:** Analysing Mental Health in Student Ecosystem  
**Author / Lead Analyst:** Parth Pawar  
**Program:** SkillWallet / SmartBridge Virtual Internship &bull; Data Analytics with Tableau  
**Domain:** Higher Education, Student Telemetry & Campus Wellness Analytics  
**Live Portfolio Website:** https://parthpawar0707-blip.github.io/Skill-wallet/  
**GitHub Repository:** https://github.com/parthpawar0707-blip/Skill-wallet  
**Published Tableau Public Dashboard:** [Student Mental Health Analysis](https://public.tableau.com/views/Student_Mental_Health_Analysis_sufiyan_17913953791380/AnalysingMentalHealthinStudentEcosystem?:language=en-US&publish=yes)  
**Dataset Reference:** [Google Sheets Source](https://docs.google.com/spreadsheets/d/1DSnFv7DdV8l1nBcQ-KNIrbgnmDMIDeh7/edit?usp=sharing)  

---

## 1. Executive Summary

Collegiate environments impose strenuous cognitive, social, and emotional demands on undergraduate students. Navigating heavy curricular deadlines, examination pressure, erratic sleep schedules, and continuous digital screen exposure frequently triggers acute psychological distress. When unmanaged, chronic distress reduces quality of life, impairs academic performance, and escalates university attrition.

This project delivers an end-to-end data analytics and business intelligence solution to systematically analyze, model, and visualize mental health dynamics across a student ecosystem. By bridging demographic data, daily lifestyle habits, subjective psychometric ratings, and therapeutic modalities into an interactive Tableau Public dashboard and a responsive editorial web portfolio, this study provides actionable, non-clinical decision support for campus advisors, academic counselors, and university wellness committees.

---

## 2. Problem Statement & Research Questions

Historically, university counseling departments and academic affairs offices have operated in administrative silos. Mental health surveys are conducted infrequently, while student attendance records and grade books reside in segregated databases. Consequently, institutional awareness of student distress typically occurs reactively—after a student has failed multiple classes, accumulated excessive absenteeism, or withdrawn entirely.

This investigation addresses three primary research questions:
1. **Lifestyle Telemetry Dynamics:** How strongly do daily digital habits (screen time hours) and sleep quality correlate with self-reported stress, anxiety, and depression?
2. **Demographic Equity:** Do psychological distress indicators vary substantially across gender cohorts, or is strain uniformly distributed across modern undergraduate populations?
3. **Intervention Efficacy:** Which institutional support pathways (e.g., Cognitive Behavioral Therapy, counseling, meditation) associate with the highest measurable progress scores?

---

## 3. Dataset Architecture & Provenance

To resolve historical discrepancies in earlier documentation, this project formally reconciles the relationship between the raw survey benchmark and the analytical extract:

### 3.1 Raw Benchmark Source (Google Sheets)
- **Source URL:** `https://docs.google.com/spreadsheets/d/1DSnFv7DdV8l1nBcQ-KNIrbgnmDMIDeh7/edit?usp=sharing`
- **Dimensions:** 1,000 student rows &times; 16 multi-dimensional variables.
- **Attributes:** `Student_ID`, `Age`, `Gender`, `Stress_Level`, `Anxiety_Level`, `Depression_Level`, `Heart_Rate_Variability`, `Sleep_Duration_Hours`, `Attendance_Rate (%)`, `Study_Hours_Per_Day`, `LMS_Activity_Score`, `Social_Interaction_Score`, `Academic_Performance_Index`, `Emotional_Journal`, `Mental_Health_Risk`, `Personalized_Intervention_Strategy`.
- **Privacy Notice:** Individual emotional journal text entries are strictly preserved privately and excluded from public-facing web assets to protect student privacy.

### 3.2 Verified Tableau Public & Portfolio Extract
- **File:** `data/mental_health_student_ecosystem_cleaned.csv` (and `summary.json`)
- **Dimensions:** Exactly **200 student records** (`STU_0001` through `STU_0200`) across **18 cleaned variables**.
- **Data Completeness:** 100% (0 missing or null values across all 3,600 data cells; 0 duplicate rows).
- **Target Workbook:** Directly extracted and verified from the published Tableau workbook (`AnalysingMentalHealthinStudentEcosystem`).

### 3.3 Complete Schema Specification (200-Student Extract)
| Column Name | Data Type | Value Range / Categories | Description |
| :--- | :--- | :--- | :--- |
| `User ID` | String | `STU_0001` to `STU_0200` | Anonymized unique student identifier |
| `Age` | Integer | 18 – 25 years | Chronological student age |
| `Gender` | String | Female, Male, Other | Demographic categorization |
| `Occupation` | String | Student / Working Student | Collegiate occupational status |
| `Stress Level` | String | Low, Medium, High | Perceived general stress tier |
| `Anxiety Score` | Integer | 0 – 100 | Standardized generalized anxiety scale |
| `Depression Score` | Integer | 0 – 100 | Standardized depressive symptoms score |
| `Sleep Quality` | String | Poor, Average, Good | Qualitative sleep restoration level |
| `Daily Screen Time (hrs)` | Float | 3.5 – 12.0 hours | Daily digital screen exposure |
| `Physical Activity Level` | String | Low, Moderate, High | Weekly exercise and movement level |
| `Social Interaction Score` | Integer | 1 – 10 | Peer engagement and connectedness rating |
| `Mental Health History` | String | Yes, No | Prior personal or familial mental health history |
| `Therapy Type` | String | CBT, Counseling, Support Group, Meditation, No Therapy | Active support modality |
| `Intervention Duration (weeks)` | Integer | 0 – 24 weeks | Length of time enrolled in intervention |
| `Progress Score` | Integer | 0 – 100 | Measured therapeutic improvement rating |
| `Medication Usage` | String | Yes, No | Prescribed psychotropic medication status |
| `Support System Strength` | String | Low, Medium, High | Self-reported family/mentor support level |
| `Work-Life Balance Score` | Integer | 1 – 10 | Subjective equilibrium rating |

---

## 4. Calculated Fields & Feature Engineering

Two key calculated fields were engineered in Tableau Desktop to isolate high-risk sub-cohorts:

1. **`Active_Therapy`**:
   ```tableau
   IF [Therapy Type] != "No Therapy" THEN 1 ELSE 0 END
   ```
   *Purpose:* Separates students actively receiving structured care from untreated students to measure institutional service coverage.

2. **`HighStress_PoorSleep`**:
   ```tableau
   IF [Stress Level] = "High" AND [Sleep Quality] = "Poor" THEN 1 ELSE 0 END
   ```
   *Purpose:* Flags students suffering concurrently from acute stress and compromised sleep quality (accounting for 35 of 49 high-stress students, or 71.4%), isolating the highest priority cohort for campus wellness outreach.

---

## 5. Verified Key Performance Indicators (KPIs)

The executive KPI ribbon in the published Tableau workbook establishes four foundational benchmarks:
- **Total Students Analyzed:** `200`
- **Average Anxiety Score:** `52.59 / 100`
- **Average Depression Score:** `48.09 / 100`
- **Average Daily Screen Time:** `7.10 Hours / Day`

---

## 6. Detailed Tableau Worksheet Analysis

The published Tableau dashboard integrates 8 analytical worksheets:

1. **Stress Level Distribution (Column Chart):**
   - Medium Stress: 107 students (53.5%)
   - High Stress: 49 students (24.5%)
   - Low Stress: 44 students (22.0%)
   - *Insight:* Over 78% of the cohort experiences moderate to high stress, confirming stress is a systemic collegiate reality rather than an edge-case anomaly.

2. **Daily Screen Time vs. Stress Level (Bar Chart):**
   - Low Stress: 6.00 hrs/day
   - Medium Stress: 7.07 hrs/day
   - High Stress: 8.12 hrs/day
   - *Insight:* A continuous upward gradient. High-stress students spend over 2 additional hours on digital screens daily compared to low-stress peers.

3. **Sleep Quality vs. Stress Level (Matrix / Stacked Bars):**
   - Poor Sleep (66 students): 35 High Stress (53.0%), 30 Medium Stress (45.5%), 1 Low Stress (1.5%).
   - Good Sleep (45 students): 2 High Stress (4.4%), 21 Medium Stress (46.7%), 22 Low Stress (48.9%).
   - *Insight:* Sleep quality functions as a primary protective buffer. Less than 5% of good sleepers report high stress.

4. **Gender Mental Health Comparison (Multi-Series Bar Chart):**
   - Female: Avg Anxiety = 53.32, Avg Depression = 48.10
   - Male: Avg Anxiety = 51.76, Avg Depression = 47.88
   - Other: Avg Anxiety = 53.50, Avg Depression = 50.38
   - *Insight:* Negligible variance exists between gender groups. Well-being initiatives must be universal rather than demographic-exclusive.

5. **Stress Level vs. Anxiety Score (Bar Chart):**
   - Low Stress: 30.27 &rarr; Medium Stress: 52.85 &rarr; High Stress: 72.06 (+138% increase).

6. **Stress Level vs. Depression Score (Bar Chart):**
   - Low Stress: 26.80 &rarr; Medium Stress: 47.37 &rarr; High Stress: 68.78 (+156% increase).

7. **Therapy Efficacy Progress (Ranked Horizontal Bar):**
   - Cognitive Behavioral Therapy (CBT): 40.80 avg progress score
   - Counseling: 34.43 avg progress score
   - Support Group: 33.10 avg progress score
   - Meditation: 32.57 avg progress score
   - No Therapy: 0.00 progress score

8. **Mental Health History Prevalence (Ring Chart):**
   - Prior History (Yes): 80 students (40.0%)
   - No Prior History (No): 120 students (60.0%)

---

## 7. Video Walkthrough Deliverable

- **Asset Path:** [`site/assets/video/student-mental-health-demo.mp4`](file:///d:/Skill%20wallet/site/assets/video/student-mental-health-demo.mp4)
- **Duration:** Exactly **06:41.97** (401.97 seconds, within the 5–7 minute target).
- **Video Specs:** H.264 / AVC, 1280&times;720 HD, 30.0 fps progressive, 9.44 MB.
- **Audio Specs:** AAC audio, 24 kHz mono, calibrated Indian English male neural voice (`en-IN-PrabhatNeural`, pitch -5Hz, rate +22%).
- **Visuals:** 15 synchronized scenes pairing exact narration sentences with genuine Tableau dashboard recordings and live portfolio captures.
- **Accessibility:** Synchronized SubRip (`.srt`) and WebVTT (`.vtt`) subtitle tracks with on-page chapter navigation.

---

## 8. Web Portfolio Architecture & Deployment

The static website is deployed via GitHub Actions and GitHub Pages:
- **Design System:** Editorial research aesthetic with white card surfaces, slate borders, deep navy typography, and deep teal accents.
- **Zero Emojis:** Standardized Lucide outline SVG icons throughout.
- **Tableau Embed Resilience:** Instant backdrop capture preview (`tableau_capture.png`) with loading spinner and automatic 7-second fallback.
- **Responsive Proof:** Verified at 1440&times;900, 768&times;1024, 390&times;844, and 360&times;800 with zero horizontal overflow.
- **Dual Redundancy:** Root (`index.html`, `404.html`, `assets/`) and `site/` directories are kept in lockstep to support both GitHub Actions (`./site`) and direct branch (`main / root`) deployment.

---

## 9. Limitations & Ethical Notice

- **Non-Clinical Disclaimer:** This project is an exploratory educational data analysis designed for institutional decision support. It does not constitute a clinical psychological assessment, diagnostic tool, or medical treatment recommendation.
- **Correlation vs. Causation:** Observed relationships (e.g., higher screen time with higher stress) represent empirical correlations. Screen time may exacerbate stress, or stressed students may engage in digital avoidance.
- **Sample Scope:** The extract reflects 200 surveyed students and should be calibrated against larger campus censuses before establishing university policy.
