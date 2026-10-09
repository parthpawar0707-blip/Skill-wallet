# Methodology: Student Mental Health Analytics

**Project Title:** Analysing Mental Health in Student Ecosystem  
**Author:** Parth Pawar  
**Program:** SkillWallet / SmartBridge Virtual Internship &bull; Data Analytics with Tableau  

---

## The 10-Step Analytical Workflow

This project adheres to a standardized, reproducible 10-step lifecycle:

```
[1. Data Acquisition] -> [2. Data Quality Audit] -> [3. Privacy & Sanitization] -> [4. Feature Engineering] -> [5. Tableau Data Source Ingestion]
        |
        v
[6. Worksheet Visualization] -> [7. Dashboard & Filter Scoping] -> [8. Story Design] -> [9. Tableau Public Publishing] -> [10. Web Portfolio & CI/CD Deployment]
```

### 1. Data Acquisition
- Downloaded and verified the official project dataset from Google Sheets:
  `https://docs.google.com/spreadsheets/d/1DSnFv7DdV8l1nBcQ-KNIrbgnmDMIDeh7/edit?usp=sharing`
- Ingested 1,000 student records across 16 multi-dimensional variables.

### 2. Data Quality Audit
- Executed `scripts/analyze_dataset.py` verifying:
  - 1,000 unique `Student_ID` keys (0 duplicate records).
  - 0 null, empty, or undefined entries across all 16,000 cells (100% completeness).
  - Range boundaries tested for clinical plausibility: Age (18–25), Scales (1–10), Sleep (2.8–10.4 hrs), Attendance (60–100%), and HRV (36.6–99.2 ms).

### 3. Student Privacy & Sanitization
- Protected individual student privacy by aggregating findings and excluding raw qualitative journal entries from public web assets.

### 4. Feature Engineering & Calculated Fields
1. **Age Cohort (`Age_Group`):**
   ```tableau
   IF [Age] < 20 THEN "Below 20"
   ELSEIF [Age] <= 22 THEN "20-22"
   ELSEIF [Age] <= 25 THEN "23-25"
   ELSE "Above 25"
   END
   ```
2. **Study Intensity (`Study_Category`):**
   ```tableau
   IF [Study_Hours_Per_Day] < 3.0 THEN "Light (<3 hrs)"
   ELSEIF [Study_Hours_Per_Day] <= 5.5 THEN "Moderate (3-5.5 hrs)"
   ELSE "Intensive (>5.5 hrs)"
   END
   ```
3. **Sleep Hygiene (`Sleep_Category`):**
   ```tableau
   IF [Sleep_Duration_Hours] < 6.0 THEN "Deprived (<6 hrs)"
   ELSEIF [Sleep_Duration_Hours] <= 7.5 THEN "Adequate (6-7.5 hrs)"
   ELSE "Optimal (>7.5 hrs)"
   END
   ```

### 5. Tableau Data Source Ingestion
- Connected dataset to Tableau Desktop / Public via Text connection.
- Verified discrete dimension assignments (`Gender`, `Age_Group`, `Mental_Health_Risk`, `Intervention_Strategy`) and continuous measure assignments (`Stress_Level`, `HRV`, `Academic_Performance_Index`, `Sleep_Duration_Hours`).

### 6. Worksheet Visualization Design
- Constructed 6 primary analytical worksheets answering targeted research questions:
  - Worksheet 1: Binned Bar chart of Study Intensity vs. Academic Performance Index.
  - Worksheet 2: Horizontal Bar chart of Gender Cohorts vs. Average Depression Level.
  - Worksheet 3: Granular Scatter Plot of Study Hours vs. Performance with linear regression trendlines.
  - Worksheet 4: Column Bar chart of Gender Cohorts vs. Average Stress Level.
  - Worksheet 5: Biometric Bar chart comparing Heart Rate Variability across Risk Tiers.
  - Worksheet 6: Proportional Donut chart illustrating Mental Health Risk Distribution.

### 7. Dashboard Layout & Filter Scoping
- Sized dashboard using modern 1366×768 desktop container architecture.
- Added executive scorecard with 7 key cohort KPI benchmarks.
- Configured global dropdown filters (`Gender`, `Age_Group`, `Mental_Health_Risk`) set to "Apply to All Worksheets using Related Data Sources".

### 8. Analytical Story Design
- Organized 3-scene narrative story guiding stakeholders from cohort baseline, to biological stress drivers, to targeted institutional interventions.

### 9. Publishing to Tableau Public
- Published packaged workbook to Tableau Public cloud servers.
- Verified live share URL and embed accessibility.

### 10. Web Portfolio & CI/CD Deployment
- Built responsive static web application in `site/` with live Tableau embed, video player, and interactive summaries.
- Configured GitHub Actions workflow (`.github/workflows/deploy.yml`) for automated static deployment to GitHub Pages.
