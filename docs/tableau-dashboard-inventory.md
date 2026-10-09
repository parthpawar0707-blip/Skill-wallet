# Tableau Dashboard & Workbook Inventory

**Project Title:** Analysing Mental Health in Student Ecosystem  
**Author:** Parth Pawar  
**Published Tableau Public URL:** [Student Mental Health Analysis](https://public.tableau.com/views/Student_Mental_Health_Analysis_sufiyan_17913953791380/AnalysingMentalHealthinStudentEcosystem?:language=en-US&publish=yes)  
**Underlying Data Source:** `mental_health_student_ecosystem_cleaned.hyper` / Google Sheets source  
**Verification Method:** Direct extraction & structural inspection of the published Tableau packaged workbook (`Student_Mental_Health_Analysis.twbx`) using `tableauhyperapi` and XML element parsing.

---

## 1. Executive Summary & Dashboard Purpose

The primary dashboard titled **"Analysing Mental Health in Student Ecosystem"** is an applied Business Intelligence solution designed to investigate the interactions between academic routines, digital habits, sleep quality, and psychological well-being across a collegiate student ecosystem. 

Rather than relying purely on qualitative self-reporting, the dashboard structures multi-dimensional behavioral metrics (screen time, sleep quality, therapy modalities) alongside standardized clinical well-being indices (Anxiety Score, Depression Score, Stress Level).

---

## 2. Core Key Performance Indicators (KPIs)

The top ribbon of the dashboard presents four executive scorecards aggregating the cohort benchmarks:

| KPI Title | Measure & Aggregation | Verified Benchmark Value | Description / Unit |
| :--- | :--- | :--- | :--- |
| **KPI - Students** | `COUNT([User ID])` | **200** | Total undergraduate students analyzed in cohort |
| **KPI - Avg Anxiety** | `AVG([Anxiety Score])` | **52.59** | Standardized generalized anxiety scale (0–100) |
| **KPI - Avg Depression** | `AVG([Depression Score])` | **48.09** | Standardized depression symptom rating (0–100) |
| **KPI - Avg Screen Time** | `AVG([Daily Screen Time (hrs)])` | **7.10 hrs** | Average daily hours spent on digital screens |

---

## 3. Detailed Worksheet Inventory

### Worksheet 1: Stress Level Distribution
- **Chart Type:** Horizontal / Vertical Column Chart
- **Dimensions / Measures:** 
  - Columns: `[Stress Level]` (Categorical Dimension: Low, Medium, High)
  - Rows: `COUNT([User ID])` (Continuous Measure)
- **Verified Values:**
  - Medium Stress: **107 students** (53.5%)
  - High Stress: **49 students** (24.5%)
  - Low Stress: **44 students** (22.0%)
- **Analytical Pattern:** Over 78% of the student cohort falls into moderate-to-severe stress classifications, indicating that academic stress is widespread rather than an isolated phenomenon.

---

### Worksheet 2: Screen Time vs Stress Level
- **Chart Type:** Bar Chart
- **Dimensions / Measures:** 
  - Columns: `[Stress Level]` (Low, Medium, High)
  - Rows: `AVG([Daily Screen Time (hrs)])`
- **Verified Values:**
  - High Stress: **8.12 hours / day**
  - Medium Stress: **7.07 hours / day**
  - Low Stress: **6.00 hours / day**
- **Analytical Pattern:** Demonstrates a distinct upward trend between daily digital consumption and acute stress perception, showing that students in the high-stress category average over 2 hours more screen time daily than low-stress peers.

---

### Worksheet 3: Sleep Quality vs Stress Level
- **Chart Type:** Cross-Tabulation Stacked Matrix
- **Dimensions / Measures:**
  - Columns: `[Sleep Quality]` (Poor, Average, Good)
  - Rows: `COUNT([User ID])` segmented by `[Stress Level]`
- **Verified Values:**
  - **Poor Sleep (66 students):** 35 High Stress (53.0%), 30 Medium Stress (45.5%), 1 Low Stress (1.5%)
  - **Average Sleep (89 students):** 12 High Stress (13.5%), 56 Medium Stress (62.9%), 21 Low Stress (23.6%)
  - **Good Sleep (45 students):** 2 High Stress (4.4%), 21 Medium Stress (46.7%), 22 Low Stress (48.9%)
- **Analytical Pattern:** Sleep quality acts as a powerful discriminator. Out of 35 students with high stress, 35 (71.4%) report poor sleep. Only 2 students with good sleep experienced high stress.

---

### Worksheet 4: Gender Mental Health Comparison
- **Chart Type:** Grouped Multi-Series Bar Chart
- **Dimensions / Measures:**
  - Columns: `[Gender]` (Female, Male, Other)
  - Rows: `AVG([Anxiety Score])` and `AVG([Depression Score])`
- **Verified Values:**
  - **Female:** Avg Anxiety = 53.32, Avg Depression = 48.10
  - **Male:** Avg Anxiety = 51.76, Avg Depression = 47.88
  - **Other:** Avg Anxiety = 53.50, Avg Depression = 50.38
- **Analytical Pattern:** Minimal variance is observed across gender demographics (anxiety ranges 51.8–53.5; depression ranges 47.9–50.4), demonstrating that lifestyle variables (sleep, screen time) are vastly stronger determinants of psychological distress than gender alone.

---

### Worksheet 5: Stress Level vs Anxiety Score
- **Chart Type:** Column / Bar Chart
- **Dimensions / Measures:**
  - Columns: `[Stress Level]` (Low, Medium, High)
  - Rows: `AVG([Anxiety Score])`
- **Verified Values:**
  - Low Stress: **30.27**
  - Medium Stress: **52.85**
  - High Stress: **72.06**
- **Analytical Pattern:** Strict positive monotonic progression: students transitioning from low to high stress experience a 138% escalation in generalized anxiety scores.

---

### Worksheet 6: Stress Level vs Depression Score
- **Chart Type:** Column / Bar Chart
- **Dimensions / Measures:**
  - Columns: `[Stress Level]` (Low, Medium, High)
  - Rows: `AVG([Depression Score])`
- **Verified Values:**
  - Low Stress: **26.80**
  - Medium Stress: **47.37**
  - High Stress: **68.78**
- **Analytical Pattern:** Mirrors the anxiety distribution. High-stress students exhibit an average depression score of 68.78, more than 2.5 times higher than the low-stress baseline (26.80).

---

### Worksheet 7: Ranked Therapy Efficacy
- **Chart Type:** Ranked Horizontal Bar Chart
- **Dimensions / Measures:**
  - Rows: `[Therapy Type]` (CBT, Counseling, Support Group, Meditation, No Therapy)
  - Columns: `AVG([Progress Score])`
- **Verified Values:**
  - **Cognitive Behavioral Therapy (CBT):** **40.80** avg progress score
  - **Counseling:** **34.43** avg progress score
  - **Support Group:** **33.10** avg progress score
  - **Meditation:** **32.57** avg progress score
  - **No Therapy:** **0.00** avg progress score
- **Analytical Pattern:** CBT provides the highest measurable therapeutic improvement among students receiving intervention, outperforming general counseling by ~18.5%.

---

### Worksheet 8: Mental Health History Prevalence
- **Chart Type:** Pie Chart / Proportional Ring
- **Dimensions / Measures:**
  - Color Slice: `[Mental Health History]` (Yes, No)
  - Angle: `COUNT([User ID])`
- **Verified Values:**
  - **No:** **120 students (60.0%)**
  - **Yes:** **80 students (40.0%)**
- **Analytical Pattern:** 40% of the surveyed student cohort possesses prior personal or family history of psychological vulnerability, requiring institutional priority screening during examination periods.

---

## 4. Calculated Fields in Workbook

The Tableau workbook contains two user-engineered calculated fields:

1. **`Active_Therapy`**
   - **Data Type:** Integer (Measure)
   - **Formula:**
     ```tableau
     IF [Therapy Type] != "No Therapy" THEN 1 ELSE 0 END
     ```
   - **Function:** Identifies and isolates students actively participating in institutional mental health care.

2. **`HighStress_PoorSleep`**
   - **Data Type:** Integer (Measure)
   - **Formula:**
     ```tableau
     IF [Stress Level] = "High" AND [Sleep Quality] = "Poor" THEN 1 ELSE 0 END
     ```
   - **Function:** Serves as a compound physiological risk flag isolating students suffering concurrently from acute stress and critical sleep deprivation (35 out of 200 students).

---

## 5. Dataset Architecture & Verification Summary

- **Total Records:** 200 rows
- **Total Variables:** 18 fields
- **Completeness:** 100% (0 missing or null values across all fields)
- **Primary Key:** `User ID` (Format: `STU_0001` to `STU_0200`)
- **Fields in Schema:**
  1. `User ID` (String)
  2. `Age` (Integer, Range: 18 – 25)
  3. `Gender` (String: Female, Male, Other)
  4. `Occupation` (String)
  5. `Stress Level` (String: Low, Medium, High)
  6. `Anxiety Score` (Integer: 0 – 100)
  7. `Depression Score` (Integer: 0 – 100)
  8. `Sleep Quality` (String: Poor, Average, Good)
  9. `Daily Screen Time (hrs)` (Float: 3.5 – 12.0)
  10. `Physical Activity Level` (String: Low, Moderate, High)
  11. `Social Interaction Score` (Integer: 1 – 10)
  12. `Mental Health History` (String: Yes, No)
  13. `Therapy Type` (String: CBT, Counseling, Support Group, Meditation, No Therapy)
  14. `Intervention Duration (weeks)` (Integer)
  15. `Progress Score` (Integer: 0 – 100)
  16. `Medication Usage` (String: Yes, No)
  17. `Support System Strength` (String: Low, Medium, High)
  18. `Work-Life Balance Score` (Integer: 1 – 10)
