# Final Tableau Action Checklist

A concise, step-by-step checklist to track your manual actions in Tableau Desktop. Check each item off as you complete it:

- [ ] **1. Connect to Cleaned Dataset:** Open Tableau Desktop/Public, select `data/student_mental_health_cleaned.csv` as a Text File.
- [ ] **2. Verify Fields & Types:** Check that dimensions (`Gender`, `Department`, `Risk`) are blue strings and measures (`Stress_Level`, `HRV`, `Academic_Performance`) are green numbers.
- [ ] **3. Create 5 Calculated Fields:**
  - [ ] `Performance_Category` (Low, Average, Good, Excellent)
  - [ ] `Sleep_Category` (Healthy, Moderate, Low Sleep)
  - [ ] `Stress_Category` (Low, Moderate, High Stress)
  - [ ] `Study_Hours_Category` (Light, Balanced, Intensive)
  - [ ] `Calculated_Risk_Tier` (Low, Medium, High Risk)
- [ ] **4. Build Visualization 1:** `Viz 1 - Impact of Study Hours on Performance` (Column Bar of Study Group vs Avg Academic Performance colored by Avg Stress).
- [ ] **5. Build Visualization 2:** `Viz 2 - Gender and Depression Level` (Horizontal Bar of Gender vs Avg Depression Level).
- [ ] **6. Build Visualization 3:** `Viz 3 - Study Hours vs Academic Performance` (Scatter Plot of all 80 students with Trend Line and Risk color coding).
- [ ] **7. Build Visualization 4:** `Viz 4 - Average Stress Level by Gender` (Vertical Bar of Gender vs Avg Stress Level).
- [ ] **8. Build Visualization 5:** `Viz 5 - Analyzing Heart Rate Variability` (Bar / Box of Risk Tier vs Avg Heart Rate Variability in ms).
- [ ] **9. Build Visualization 6:** `Viz 6 - KPI Overview Cards` (Text cards showing Total Students: 80, Avg Stress: 4.95, Avg Sleep: 6.60 hrs, Avg Score: 80.5%).
- [ ] **10. Build Visualization 7:** `Viz 7 - Mental Risk Level Distribution` (Donut / Pie chart with percentage labels).
- [ ] **11. Build Visualization 8:** `Viz 8 - Academic Performance Breakdown` (Horizontal Bar chart of students per Performance Tier).
- [ ] **12. Add Global Filters:** Set `Gender`, `Academic_Year`, `Department`, and `Mental_Health_Risk` to "Apply to All Worksheets Using This Data Source".
- [ ] **13. Assemble Dashboard:** Create `Student Mental Health & Academic Well-Being Dashboard` with Title, KPI row, Middle row (Viz 3, 4, 7), Bottom row (Viz 2, 5, 8).
- [ ] **14. Configure Responsive Sizing:** Set Dashboard size to **Automatic** or **Range (Min: 1000x800, Max: 1600x1050)**.
- [ ] **15. Assemble Story (3 Scenes):**
  - [ ] Scene 1: Overall Student Mental Health (KPIs + Risk Donut + Stress Overview)
  - [ ] Scene 2: Lifestyle and Mental Health (HRV Analysis + Sleep / Study Balance)
  - [ ] Scene 3: Academic Performance and Risk (Scatter Plot + Grade Breakdown)
- [ ] **16. Save Local Packaged Workbook:** Save as `tableau/Student_Mental_Health_Analytics.twbx`.
- [ ] **17. Publish to Tableau Public:** Server -> Tableau Public -> Save to Tableau Public As...
- [ ] **18. Copy URLs:** Copy the Share Links for both the Dashboard and Story into `config.py` and `README.md`.
