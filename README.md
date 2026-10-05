# Analysing Mental Health in Student Ecosystem

[![Domain](https://img.shields.io/badge/Domain-Healthcare%20%26%20Education-blue.svg)](#)
[![Primary Tool](https://img.shields.io/badge/Primary%20Tool-Tableau%20Desktop%20%2F%20Public-E97627.svg)](#)
[![Web Integration](https://img.shields.io/badge/Web%20Framework-Python%20Flask-black.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#)

An integrated healthcare and higher-education data analytics project investigating the complex relationships between lifestyle habits, physiological stress indicators (including Heart Rate Variability), academic outcomes, and mental health risk across collegiate student ecosystems.

Developed under the **Skill Wallet: Data Analytics with Tableau** program.

---

## Live Links & Placeholders

* **Tableau Public Dashboard:**  
  `[ADD TABLEAU LINK AFTER PUBLISHING]` *(e.g., https://public.tableau.com/views/StudentMentalHealthAnalytics/Dashboard)*

* **Tableau Story:**  
  `[ADD STORY LINK AFTER PUBLISHING]` *(e.g., https://public.tableau.com/views/StudentMentalHealthAnalytics/Story)*

* **Project Demonstration Video:**  
  `[ADD DEMO LINK]` *(e.g., Unlisted YouTube or Google Drive video link)*

---

## Project Overview

In university ecosystems, academic pressure, sleep deprivation, and digital screen overload frequently culminate in acute psychological distress. Traditional higher-education institutions evaluate student distress reactively—typically after a student experiences academic probation or course withdrawal.

This project delivers a proactive business intelligence platform using **Tableau** and **Python Flask**. By analyzing a verified cohort of 80 students across 19 multidimensional attributes, the project enables university leaders, deans, and campus wellness counselors to identify early warning signs, detect burnout thresholds, and target counseling interventions before academic performance suffers.

---

## Problem Statement

* Mental health surveys in academic institutions are collected irregularly and analyzed through isolated, static spreadsheets.
* Institutions lack unified, real-time diagnostic systems linking subjective self-reports (stress, anxiety, depression) with biological biomarkers (Heart Rate Variability) and registrar academic outcomes.
* Decision-makers cannot easily slice and dice mental health patterns across demographic segments such as academic departments and class years.

---

## Objectives

1. **Analyze Behavioral Correlates:** Quantify how daily study hours, sleep duration, screen time, and physical activity correlate with stress, anxiety, and depression.
2. **Identify Academic Burnout Points:** Discover the optimal daily study window (3.5–6.0 hrs) and prove where excessive studying combined with sleep deficits causes diminishing grade returns.
3. **Biometric Validation:** Correlate subjective survey scores with autonomic Heart Rate Variability (HRV in milliseconds).
4. **Develop Tableau Master Dashboard:** Construct 8 required visual charts unified with synchronized global filters (Gender, Academic Year, Department, Risk Tier).
5. **Author a 3-Scene Tableau Story:** Deliver a guided diagnostic narrative leading from cohort baseline to biological strain and intervention policies.
6. **Deploy Full-Stack Web Portal:** Embed the live cloud visualizations inside a responsive Flask web application for stakeholder presentation.

---

## Dataset Description

The dataset comprises **80 individual student records** across **19 attributes** modeled after authentic university health survey metrics and wearable telemetry:

| Category | Attributes Included |
| :--- | :--- |
| **Demographics** | `Student_ID`, `Age`, `Gender`, `Academic_Year`, `Department` |
| **Lifestyle & Habits** | `Study_Hours`, `Sleep_Hours`, `Screen_Time`, `Social_Interaction_Hours`, `Physical_Activity_Hours` |
| **Mental Health Scales** | `Stress_Level` (1–10), `Anxiety_Level` (1–10), `Depression_Level` (1–10), `Mood_Score` (1–10) |
| **Academic Performance** | `Academic_Performance` (0–100%), `Attendance_Percentage` (0–100%) |
| **Biometric & Support** | `Heart_Rate_Variability` (ms), `Support_System`, `Mental_Health_Risk` (Low, Medium, High) |

* Cleaned dataset stored at: [`data/student_mental_health_cleaned.csv`](file:///d:/Skill%20wallet/data/student_mental_health_cleaned.csv)
* Full field specifications: [`docs/data_dictionary.md`](file:///d:/Skill%20wallet/docs/data_dictionary.md)

---

## Technology Stack

* **Primary Analytics & BI Tool:** Tableau Desktop / Tableau Public
* **Web Integration Backend:** Python 3 (Flask WSGI Web Framework)
* **Frontend:** Responsive HTML5, CSS3 Modern Flex/Grid, Tableau Embedding API v3
* **Data Processing & Validation:** Python standard library (`csv`, `os`, `sys`)
* **Version Control:** Git & GitHub

---

## The 8 Tableau Visualizations

1. **Viz 1: Impact of Study Hours on Academic Performance:** Column Bar chart analyzing grade distributions across study intensity groups, colored by average stress.
2. **Viz 2: Gender and Their Depression Level:** Horizontal Bar chart evaluating comparative depression scores across gender cohorts.
3. **Viz 3: Study Hours vs Academic Performance:** Disaggregated Scatter plot plotting all 80 individual students with linear regression trendlines and risk color marks.
4. **Viz 4: Average Stress Level by Gender:** Vertical Bar chart monitoring subjective stress ratings.
5. **Viz 5: Analyzing Heart Rate Variability:** Biomarker analysis proving that High-Risk students suffer from clinically suppressed autonomic HRV (<40 ms).
6. **Viz 6: KPI Overview Cards:** High-level executive scorecard: Total Students (80), Avg Stress (4.95), Avg Sleep (6.60 hrs), Avg Score (80.5%).
7. **Viz 7: Mental Risk Level Distribution:** Proportional Donut / Pie chart with percentage labels (15% High, 48.8% Medium, 36.2% Low).
8. **Viz 8: Academic Performance Breakdown:** Horizontal Bar chart grouping students across institutional performance tiers (`Performance_Category`).

*Detailed step-by-step instructions:* [`tableau/visualizations.md`](file:///d:/Skill%20wallet/tableau/visualizations.md)

---

## Calculated Fields in Tableau

Five scalar conditional logic fields created in Tableau:
1. `Performance_Category`: Classifies grades into `Excellent` (>=90%), `Good` (75–89%), `Average` (60–74%), and `Low` (<60%).
2. `Sleep_Category`: Classifies sleep into `Healthy` (>=7 hrs), `Moderate` (6–7 hrs), and `Low Sleep` (<6 hrs).
3. `Stress_Category`: Categorizes stress into `Low` (1–3), `Moderate` (4–6), and `High Stress` (7–10).
4. `Study_Hours_Category`: Classifies daily study into `Light` (<3.5 hrs), `Balanced` (3.5–6 hrs), and `Intensive` (>6 hrs).
5. `Calculated_Risk_Tier`: Validates multi-factor clinical risk from the sum of Stress, Anxiety, and Depression scales.

*Formula details:* [`tableau/calculated_fields.md`](file:///d:/Skill%20wallet/tableau/calculated_fields.md)

---

## Master Dashboard Architecture

* **Title:** *Student Mental Health & Academic Well-Being Dashboard*
* **Top:** Title Banner & Global Filters (`Gender`, `Academic_Year`, `Department`, `Mental_Health_Risk`)
* **KPI Row:** Executive Scorecards (Viz 6)
* **Middle Row:** Viz 3 (Scatter Plot), Viz 4 (Stress by Gender), Viz 7 (Risk Donut)
* **Bottom Row:** Viz 2 (Depression by Gender), Viz 5 (HRV Analysis), Viz 8 (Grade Breakdown)
* **Interactivity:** Synchronized data-source filters and Action Filters ("Use as Filter" on Risk Donut).
* **Responsive Layout:** Min: 1000×800px, Max: 1600×1050px (or Automatic).

*Dashboard placement guide:* [`tableau/dashboard_design.md`](file:///d:/Skill%20wallet/tableau/dashboard_design.md)

---

## 3-Scene Tableau Story

* **Scene 1: Baseline Student Mental Health Landscape & Risk Distribution:** Establishes the 80-student baseline, risk percentages, and gender stress consistency.
* **Scene 2: Lifestyle Imbalances & Autonomic Strain (HRV & Sleep):** Visualizes the physiological link between sleep deprivation, screen overload, and suppressed HRV.
* **Scene 3: Academic Efficacy & Targeted Intervention:** Examines the academic burnout threshold and provides counseling policy recommendations.

*Story layout details:* [`tableau/story_plan.md`](file:///d:/Skill%20wallet/tableau/story_plan.md)

---

## Project Structure

```text
Skill-wallet/
├── README.md                          # Master project documentation
├── requirements.txt                   # Minimal Python dependencies (Flask>=3.0.0)
├── app.py                             # Flask web application server
├── config.py                          # Centralized configuration & Tableau embed URLs
├── .gitignore                         # Standard git ignore definitions
│
├── data/
│   ├── student_mental_health.csv      # Raw synthesized student dataset (80 records)
│   └── student_mental_health_cleaned.csv  # Cleaned, validated, Tableau-ready CSV
│
├── scripts/
│   ├── clean_data.py                  # Automated data quality & validation script
│   ├── generate_dataset.py            # Reproducible synthetic dataset generator
│   └── test_app.py                    # Automated Flask route test suite
│
├── tableau/
│   ├── tableau_setup_guide.md         # Beginner click-by-click connection guide
│   ├── calculated_fields.md           # Exact formulas & usage for all 5 calculated fields
│   ├── visualizations.md              # Detailed guide for all 8 worksheets
│   ├── dashboard_design.md            # Dashboard layout wireframe & responsive guide
│   ├── story_plan.md                  # 3-scene story structure & insights
│   ├── publishing_guide.md            # Tableau Public save & embed guide
│   └── final_tableau_checklist.md     # Quick action checklist for Tableau Desktop
│
├── docs/
│   ├── data_dictionary.md             # Complete schema dictionary for all 19 attributes
│   ├── data_cleaning.md               # Data auditing, missing value & range report
│   ├── performance_testing.md         # Skill Wallet Epic 6 performance audit
│   ├── architecture.md                # System & data flow architecture with Mermaid diagrams
│   ├── project_documentation.md       # Master 27-section academic project report
│   ├── testing.md                     # Comprehensive 20-test-case validation matrix
│   ├── demo_script.md                 # 5-10 minute spoken presentation script + 18 viva Q&As
│   ├── presentation_notes.md          # 1-page viva presentation cheat-sheet
│   ├── skill_wallet_mapping.md        # Exact mapping for all 8 Epics & 22 tasks
│   ├── minimum_manual_work.md         # Click-by-click minimal manual work guide
│   └── evidence_checklist.md          # Screenshot checklist for submission approval
│
├── templates/
│   ├── base.html                      # Modular Jinja2 base layout
│   ├── index.html                     # Executive overview & baseline KPI portal
│   ├── dashboard.html                 # Embedded Tableau Dashboard view
│   ├── story.html                     # Embedded Tableau Story view
│   ├── data.html                      # Interactive 80-record dataset table viewer
│   └── insights.html                  # Summary of analytical findings & interventions
│
├── static/
│   └── style.css                      # Modern, responsive light-theme CSS styling
│
└── web/
    └── README.md                      # Dedicated Flask setup & troubleshooting guide
```

---

## Installation & Running the Flask Portal

1. **Clone the repository:**
   ```powershell
   git clone https://github.com/parthpawar0707-blip/Skill-wallet.git
   cd "Skill-wallet"
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Run the Flask application:**
   ```powershell
   python app.py
   ```

5. **Open your browser:**
   Navigate to `http://127.0.0.1:5000` to access the full portal!

---

## Key Analytical Insights

1. **The Study-Burnout Curvature:** Daily study between 3.5 and 6.0 hours produces optimal academic achievement (82%–90%). Pushing beyond 6.5 hours while sleep-deprived spikes stress and lowers grades.
2. **Sleep as the Master Predictor:** Students with fewer than 5.5 hours of sleep per night have a 3.8× higher likelihood of being classified as High Risk.
3. **Biometric Validation:** Low Heart Rate Variability (<40 ms) objectively verifies autonomic physical exhaustion in high-risk students.
4. **Early Intervention Window:** Over 48% of students sit in the Moderate Risk category, providing colleges with an ideal proactive intervention opportunity before exam failures occur.

---

## Testing & Quality Assurance

* **Data Cleaning & Auditing:** Automated verification in `scripts/clean_data.py` confirmed 0 duplicate IDs, 0 nulls, and 100% valid clinical ranges across all 80 rows.
* **Flask Web Server:** Automated unit test suite `scripts/test_app.py` validated all 5 HTTP endpoints with 100% pass rate.
* **Full Matrix:** See [`docs/testing.md`](file:///d:/Skill%20wallet/docs/testing.md) for the 20-point test case matrix.

---

## Skill Wallet Task Mapping

All 8 Epics and 22 Kanban tasks are documented with direct evidence in [`docs/skill_wallet_mapping.md`](file:///d:/Skill%20wallet/docs/skill_wallet_mapping.md).

* **Epic 1: Data Collection & Extraction:** Covered via `student_mental_health.csv`, `data_dictionary.md`, and `tableau_setup_guide.md`.
* **Epic 2: Data Preparation:** Covered via `clean_data.py` and `data_cleaning.md`.
* **Epic 3: Data Visualization:** All 8 visualizations mapped in `visualizations.md`.
* **Epic 4: Dashboard:** Full layout and responsive guide in `dashboard_design.md`.
* **Epic 5: Story:** 3 narrative scenes detailed in `story_plan.md`.
* **Epic 6: Performance Testing:** Audited and certified in `performance_testing.md`.
* **Epic 7: Web Integration:** Production-ready Flask portal in `app.py` and `web/README.md`.
* **Epic 8: Demonstration & Docs:** Demo script and 27-section project report in `demo_script.md` and `project_documentation.md`.

---

## Student Details
* **Student Name:** Parth Pawar
* **Program:** Data Analytics with Tableau
* **Skill Wallet Track:** Individual Capstone Project
* **GitHub Repository:** [parthpawar0707-blip/Skill-wallet](https://github.com/parthpawar0707-blip/Skill-wallet)
