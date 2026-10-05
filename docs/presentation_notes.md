# Quick Presentation Notes & Viva Cheat-Sheet

Keep this one-page bulleted cheat-sheet next to you during your project demonstration. It summarizes your talking points so you can speak fluently and confidently without memorizing long paragraphs.

---

## 1. Opening
* **My Name:** Parth Pawar
* **Project:** Analysing Mental Health in Student Ecosystem
* **Skill Wallet Track:** Data Analytics with Tableau
* **Domain:** Healthcare & Higher Education
* **One-liner Pitch:** *"We used Tableau and Flask to turn student survey and biometric data into actionable campus mental-health insights."*

---

## 2. The Problem
* Students face burnout from exams, sleep deprivation, and digital fatigue.
* Colleges only notice when a student fails or drops out.
* Existing data is stuck in static spreadsheets without interactive analysis.

---

## 3. Our Solution
* **80 student profiles** across 19 attributes and 5 academic departments.
* Objective biometrics included: **Heart Rate Variability (HRV)** in milliseconds.
* Automated Python data cleaning pipeline (`clean_data.py`).
* **8 Tableau charts**, 5 calculated fields, 1 master responsive dashboard, and 1 3-scene story.
* Web integration via a lightweight **Python Flask** portal.

---

## 4. The 8 Tableau Charts at a Glance
1. **Viz 1 (Study Hours vs Performance Bar):** Shows grades peak at balanced study (3.5–6 hrs); excessive study (>6.5 hrs) spikes stress.
2. **Viz 2 (Depression by Gender):** Depression averages 4.5–5.2 across cohorts; affects all genders.
3. **Viz 3 (Scatter Plot - 80 Dots):** Disaggregated students with linear trendline. Red dots (High Risk) plateau early due to burnout.
4. **Viz 4 (Stress by Gender):** Baseline stress is consistent (~5/10) across departments and genders.
5. **Viz 5 (HRV Analysis - Key Highlight):** High-risk students have low HRV (<40 ms), biologically proving autonomic strain.
6. **Viz 6 (KPI Banner):** 80 students, 4.95 Avg Stress, 6.60 hrs Sleep, 80.5% Avg Performance.
7. **Viz 7 (Risk Donut):** 15% High Risk (12 students), 48.8% Medium Risk (39 students), 36.2% Low Risk (29 students).
8. **Viz 8 (Academic Breakdown):** Grade tiers (Excellent, Good, Average, Low) cross-referenced with attendance and sleep.

---

## 5. The Master Dashboard
* **Filters:** Gender, Academic Year, Department, Risk Tier (applied across all worksheets).
* **Action Filter:** Clicking the 'High Risk' pie slice on Viz 7 filters the entire dashboard.
* **Layout:** Clean 4-tier grid (Title -> Filters -> KPIs -> Middle Row -> Bottom Row).
* **Responsive:** Sized to reflow cleanly across laptop and projector screens (1000px to 1600px).

---

## 6. The 3-Scene Tableau Story
* **Scene 1 (Landscape):** Executive overview of risk tiers and cohort stress baseline.
* **Scene 2 (Lifestyle & Telemetry):** How sleep deprivation (<6 hrs) and screen time drop HRV below 40 ms.
* **Scene 3 (Academic Burnout):** Proves that extra study hours without sleep degrade performance; presents counselor action plan.

---

## 7. Web Integration (Flask)
* Built using Python Flask (`app.py`).
* Embeds Tableau Public via official Web Component API (`<tableau-viz>`).
* URL configured in `config.py` in one line.
* Includes Overview, Dashboard, Story, Live Dataset Table, and Insights pages.

---

## 8. Top 3 Insights to Emphasize
1. **Sleep is the Master Switch:** Less than 5.5 hours sleep = 3.8× higher risk of mental crisis.
2. **The Burnout Curve:** Studying 4–6 hours is optimal. Studying 7+ hours with sleep deficits decreases grades.
3. **The 48% Opportunity:** Nearly half of students are in the 'Medium Risk' stage—colleges can intervene before crisis strikes.

---

## 9. Conclusion
* *"Tableau allows us to identify at-risk students before exams, moving university wellness from reactive crisis management to proactive student care."*
