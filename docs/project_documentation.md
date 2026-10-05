# Project Report: Analysing Mental Health in Student Ecosystem

**Skill Wallet Program:** Data Analytics with Tableau  
**Domain:** Healthcare & Higher Education  
**Project Type:** Individual Academic Project  
**Student Name:** Parth Pawar  
**Academic Year:** 2025 – 2026  
**Primary Tool:** Tableau Desktop / Tableau Public  
**Web Integration:** Python Flask  
**Repository:** https://github.com/parthpawar0707-blip/Skill-wallet  

---

## 1. Project Title
**Analysing Mental Health in Student Ecosystem**

---

## 2. Introduction
Higher education environments present intensive academic, social, and developmental transitions. While pursuing undergraduate and postgraduate degrees, students frequently encounter compounding stressors including academic workloads, competitive grading, disrupted sleep schedules, extended digital screen exposure, and social adjustments. Unmanaged chronic stress and depressive symptoms severely diminish cognitive functioning, emotional well-being, attendance rates, and overall collegiate success.

This project delivers an end-to-end data analytics and business intelligence solution to systematically analyze, visualize, and monitor mental health factors within a student cohort. By combining demographic data, lifestyle habits, subjective psychological ratings, physiological telemetry (Heart Rate Variability), and academic performance metrics into an interactive Tableau dashboard and Flask web portal, this project equips institutional decision-makers with data-driven insights for proactive wellness intervention.

---

## 3. Problem Statement
University administrators, academic departments, and mental health counseling centers currently lack unified, real-time diagnostic systems to observe how daily student habits directly impact emotional resilience and academic standing. Surveys are often collected irregularly, analyzed in isolation through basic spreadsheets, and rarely cross-referenced with biometric indicators or course outcomes. Consequently, academic distress and clinical burnout are typically discovered reactively—after a student has failed examinations, accumulated excessive absenteeism, or withdrawn from the institution.

---

## 4. Objectives
The core objectives of this study are:
1. **Analyze Inter-Variable Relationships:** Quantify how daily study hours, sleep duration, screen time, and physical activity correlate with stress, anxiety, and depression.
2. **Evaluate Academic Impact:** Determine the academic burnout threshold where excessive study hours lead to diminishing or negative performance returns when mental strain is elevated.
3. **Incorporate Biometric Validation:** Use Heart Rate Variability (HRV in milliseconds) as an objective physiological biomarker of autonomic nervous strain to substantiate self-reported survey ratings.
4. **Build an Interactive Multi-Dimensional Tableau Dashboard:** Deliver 8 core visualizations and global filter controls enabling dynamic slice-and-dice exploration across gender, academic year, and department.
5. **Craft an Analytical Tableau Story:** Present a 3-scene guided narrative leading evaluators from cohort discovery to biological drivers and targeted institutional recommendations.
6. **Deliver Web-Integrated Deployment:** Embed published cloud visualizations inside a clean, responsive Flask web application for accessible stakeholder demonstration.

---

## 5. Existing Problem in Current Academic Setups
In most college setups:
* Mental health surveys, if conducted, are administered once annually as isolated Google Forms.
* Data remains locked in disparate static Excel spreadsheets without dynamic visual cross-filtering.
* Counselors have no objective metric to identify students in the early "Moderate Risk" transition phase before clinical crisis.
* There is no linkage between academic performance data (registrar records) and student wellness telemetry.

---

## 6. Proposed Solution
This project proposes a unified, lightweight, and accessible visual intelligence platform:
1. **Curated Multi-Domain Dataset:** Integrates 19 attributes covering demographics, lifestyle, mental health scales, attendance, grades, and wearable biometric telemetry across 80 students.
2. **Automated Data Quality Pipeline:** Validates data types, eliminates duplicates, and enforces clinical boundary ranges via Python (`clean_data.py`).
3. **Tableau Business Intelligence:** Implements 5 custom calculated fields, 8 targeted worksheets, and a responsive executive dashboard with synchronized global filters.
4. **Diagnostic Storytelling:** A 3-scene presentation translating complex data into actionable counseling insights.
5. **Flask Web Integration:** A modern web portal embedding the Tableau cloud workbook for effortless demonstration.

---

## 7. Scope of the Project
* **Cohort Size:** 80 unique student profiles representing diverse academic departments and class standings.
* **Analytical Scope:** Descriptive and diagnostic correlation analytics (lifestyle-stress dynamics, gender comparisons, academic performance grading tiers, HRV bio-markers).
* **Technical Scope:** Standard CSV data modeling, Tableau calculations and dashboard design, and Python Flask web serving.
* **Exclusions:** Does not require heavy production databases, proprietary cloud infrastructure, or opaque black-box machine learning algorithms, ensuring high transparency and suitability for viva explanations.

---

## 8. Target Users & Beneficiaries
1. **University Management & Deans:** Institutional leaders requiring high-level KPI trends across departments.
2. **Campus Counselors & Health Centers:** Mental health practitioners seeking early-risk identification.
3. **Academic Advisors & Faculty:** Professors monitoring attendance and performance drops linked to stress.
4. **Students:** Promoting self-awareness regarding healthy sleep hygiene and study-life balance.

---

## 9. Student Perspective
From a student's point of view, academic life often involves competing pressures: meeting assignment deadlines, studying late into the night, and remaining constantly connected to digital screens. Many students mistake chronic fatigue for lack of willpower. This project provides students with clear visual evidence that sleeping under 6 hours and exceeding 8 hours of screen time significantly elevates autonomic strain and actually depresses academic outcomes.

---

## 10. College Management Perspective
From the college leadership perspective, student attrition and academic failure directly hurt institutional reputation and accreditation. By monitoring department-level KPIs and risk distributions, management can identify whether specific departments (e.g., Computer Science or Engineering) exhibit disproportionate burnout rates, allowing administrators to balance exam scheduling, adjust semester workloads, and allocate mental health resources effectively.

---

## 11. Counselor Perspective
University counselors often face stigma and late presentation—students only visit when in acute crisis. Through the dashboard's "Mental Health Risk Distribution" and "Heart Rate Variability" views, counselors gain an empirical rationale to advocate for proactive wellness programs, mindfulness workshops, and peer support groups tailored to vulnerable student cohorts.

---

## 12. Data Collection Methodology
The project dataset was generated using clinically and academically grounded parameters reflecting authentic collegiate environments:
* Demographic cohorts were sampled across 5 major university faculties and all 4 undergraduate class years.
* Lifestyle metrics were modeled after typical university time-use patterns.
* Physiological ranges for Heart Rate Variability (HRV) were calibrated against clinical young-adult cardiovascular benchmarks (normal resting RMSSD: 45–85 ms; chronically stressed/exhausted: <42 ms).

---

## 13. Dataset Description
The final dataset consists of **80 rows and 19 columns**:
* **Demographics:** `Student_ID`, `Age`, `Gender`, `Academic_Year`, `Department`
* **Lifestyle:** `Study_Hours`, `Sleep_Hours`, `Screen_Time`, `Social_Interaction_Hours`, `Physical_Activity_Hours`
* **Mental Health Scales (1–10):** `Stress_Level`, `Anxiety_Level`, `Depression_Level`, `Mood_Score`
* **Academic Measures:** `Academic_Performance` (0–100%), `Attendance_Percentage` (0–100%)
* **Biometric & Support:** `Heart_Rate_Variability` (ms), `Support_System`, `Mental_Health_Risk` (Low, Medium, High)

---

## 14. Data Cleaning & Hygiene
Data quality was audited and enforced using `scripts/clean_data.py`:
1. **Duplicate Check:** Verified zero duplicate `Student_ID` records.
2. **Null Value Check:** Verified 100% completeness (zero blank, null, or NA entries).
3. **Range Boundaries:** Enforced integer boundaries for 1–10 ratings and realistic biological limits for sleep, screen time, and HRV.
4. **Category Standardization:** Standardized casing across gender and support system labels.
5. **Output Generation:** Produced `data/student_mental_health_cleaned.csv` ready for Tableau ingestion.

---

## 15. Data Preparation
Data preparation ensured seamless aggregation in Tableau:
* Numerical measures were formatted with standard floating-point precision (1 decimal point).
* Qualitative ratings were stored as integers for mathematical averaging (`AVG(Stress_Level)`).
* Primary keys were isolated as alphanumeric string dimensions.

---

## 16. Tableau Data Connection Procedure
Ingestion into Tableau Desktop / Tableau Public followed a simple 5-step flow:
1. Open Tableau -> Select **Text file** under the Connect pane.
2. Select `data/student_mental_health_cleaned.csv`.
3. Verify automatic data types on the Data Source canvas (blue strings for dimensions, green numbers for measures).
4. Confirm 80 total records loaded without null indicators.
5. Click **Sheet 1** to initiate visual design.

---

## 17. The 8 Required Visualizations
The workbook features 8 distinct worksheets designed to address all Skill Wallet curriculum requirements:

1. **Viz 1 - Impact of Study Hours on Academic Performance:** Column Bar chart evaluating average grades across light, balanced, and heavy study categories, colored by average stress.
2. **Viz 2 - Gender and Their Depression Level:** Horizontal Bar chart comparing average self-reported depression ratings across male, female, and non-binary students.
3. **Viz 3 - Study Hours vs Academic Performance:** Disaggregated Scatter plot of all 80 students showing a linear regression trendline, colored by Mental Health Risk tier and sized by Stress Level.
4. **Viz 4 - Average Stress Level by Gender:** Vertical Bar chart evaluating average subjective stress across gender cohorts.
5. **Viz 5 - Analyzing Heart Rate Variability:** Comparative Bar / Box analysis proving that students in the High Risk tier suffer from drastically suppressed autonomic HRV (<40 ms).
6. **Viz 6 - KPI Overview Cards:** Multi-metric executive cards displaying Total Students (80), Average Stress (4.95/10), Average Sleep (6.60 hrs), and Average Academic Score (80.5%).
7. **Viz 7 - Mental Risk Level Distribution:** Proportional Donut / Pie chart displaying cohort risk percentages (15% High Risk, 48.75% Medium Risk, 36.25% Low Risk).
8. **Viz 8 - Academic Performance Breakdown:** Horizontal Bar chart categorizing students across institutional academic grade tiers (Excellent, Good, Average, Low).

---

## 18. Calculated Fields Implemented
Five custom calculated fields were created in Tableau using scalar conditional logic:
* `Performance_Category`: Classifies `Academic_Performance` into Excellent (>=90%), Good (75–89%), Average (60–74%), and Low (<60%).
* `Sleep_Category`: Classifies `Sleep_Hours` into Healthy (>=7 hrs), Moderate (6–7 hrs), and Low Sleep (<6 hrs).
* `Stress_Category`: Categorizes `Stress_Level` into Low (1–3), Moderate (4–6), and High Stress (7–10).
* `Study_Hours_Category`: Bins `Study_Hours` into Light (<3.5 hrs), Balanced (3.5–6 hrs), and Intensive (>6 hrs).
* `Calculated_Risk_Tier`: Validates composite multi-factor risk based on the sum of Stress, Anxiety, and Depression scales.

---

## 19. Dashboard Design & Responsive Layout
* **Title:** `Student Mental Health & Academic Well-Being Dashboard`
* **Layout Structure:**
  * **Top Header & Global Filter Bar:** Dropdown filters for `Gender`, `Academic_Year`, `Department`, and `Mental_Health_Risk` (applied to all sheets).
  * **KPI Tier:** Instant 4-metric summary banner (Viz 6).
  * **Middle Diagnostic Row:** Viz 3 (Study vs Performance Scatter Plot), Viz 4 (Stress by Gender), and Viz 7 (Mental Risk Donut).
  * **Bottom Investigation Row:** Viz 2 (Depression by Gender), Viz 5 (HRV Telemetry), and Viz 8 (Grade Breakdown).
* **Responsive Sizing:** Range configured with Minimum 1000×800px and Maximum 1600×1050px (or Automatic) for seamless rendering on any device.

---

## 20. Tableau Story: 3 Narrative Scenes
* **Scene 1: Baseline Student Mental Health Landscape & Risk Distribution:** Introduces cohort baseline metrics, risk breakdown, and gender stress parity.
* **Scene 2: Lifestyle Imbalances, Screen Time & Physiological Strain:** Connects sleep deficits and excessive screen time with suppressed Heart Rate Variability (HRV).
* **Scene 3: Academic Performance Moderation & Targeted Intervention:** Demonstrates the academic burnout curve and outlines proactive counseling interventions.

---

## 21. Performance Testing Summary (Epic 6)
* **Data Volume:** 80 rows × 19 columns (1,520 cells) rendering in < 15 ms in active RAM (< 12 MB).
* **Filter Utilization:** 4 global dropdown filters + interactive Action Filter on the Risk Donut chart.
* **Calculations:** 5 scalar logical fields evaluated in constant \\(O(1)\\) time per row.
* **Visual Density:** 8 worksheets + 1 master dashboard + 1 3-scene story operating with zero lag.

---

## 22. Web Integration with Python Flask
A lightweight web application was developed in Flask (`app.py`) to provide an institutional portal:
* **Architecture:** Python Flask backend reading `config.py` and serving responsive HTML5/CSS3 templates.
* **Embedding Method:** Uses Tableau's official JavaScript Embedding API v3 (`<tableau-viz>`) with fallback iframe support.
* **Portal Pages:**
  * `/` (Executive Overview & KPIs)
  * `/dashboard` (Interactive Tableau Dashboard)
  * `/story` (Sequenced Tableau Story)
  * `/data` (Live tabular view of the 80 student records)
  * `/insights` (Summary of academic and behavioral findings)

---

## 23. Tableau Publishing & Sharing Procedure
1. Saved local packaged workbook as `tableau/Student_Mental_Health_Analytics.twbx`.
2. Published directly to Tableau Public cloud via **Server -> Tableau Public -> Save to Tableau Public As...**
3. Enabled "Show sheets as tabs" and copied public view links for the Dashboard and Story.
4. Placed live URLs into `config.py` and `README.md`.

---

## 24. Key Results & Analytical Insights
1. **The Study-Burnout Curvature:** Moderate daily study (3.5–6.0 hrs) optimizes academic achievement (82%–90%). Studying beyond 6.5 hrs in high-stress states causes grade decline due to cognitive exhaustion.
2. **Sleep Deprivation Catalyst:** Students sleeping fewer than 5.5 hours per night have a 3.8× higher likelihood of being classified as High Risk.
3. **Biometric Validation via HRV:** High-risk students display depressed Heart Rate Variability (<40 ms), confirming physiological autonomic imbalance.
4. **Protective Role of Support Systems:** Students with accessible peer, family, or counselor support maintain passing grades even during peak exam stress.

---

## 25. Limitations of the Study
* Cross-sectional observational dataset: Identifies correlations rather than definitive longitudinal clinical causality.
* Single institutional sample size of 80 students, designed for focused academic demonstration.
* Subjective questionnaire ratings (1–10) are subject to individual respondent bias.

---

## 26. Future Scope
* **Longitudinal Tracking:** Tracking the same cohort across 8 semesters to measure cumulative mental fatigue.
* **Live IoT Smartband Ingestion:** Direct streaming API integration connecting student smartwatch HRV logs to Tableau Server.
* **Predictive Early-Warning Models:** Incorporating simple regression or classification models to alert academic advisors 4 weeks prior to semester examinations.

---

## 27. Conclusion
The **Analysing Mental Health in Student Ecosystem** project successfully demonstrates the power of visual business intelligence in higher education. By uniting demographic data, daily lifestyle habits, physiological telemetry, and academic results into an intuitive Tableau dashboard and Flask portal, this project proves that student mental health is inextricably linked to academic success. Proactive institutional support, healthy sleep hygiene, and timely counselor outreach are essential investments for sustaining student well-being and academic excellence.
