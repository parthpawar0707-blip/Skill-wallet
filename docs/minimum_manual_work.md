# Minimum Manual Work Action Plan

This document outlines the **exact, minimal tasks** you personally need to perform. All coding, data generation, data cleaning, automated testing, documentation, web portal creation, and git setup have been completed automatically.

---

## Part A: What Antigravity Has Already Completed for You (100% Done)

1. **Dataset Synthesized:** Generated 80 realistic student records across 19 attributes (`data/student_mental_health.csv`).
2. **Data Cleaning Pipeline:** Created and executed `scripts/clean_data.py`, verifying zero duplicates, zero nulls, and clinical range boundaries to produce `data/student_mental_health_cleaned.csv`.
3. **Data Dictionary & Cleaning Reports:** Detailed schema and audit reports written in `docs/data_dictionary.md` and `docs/data_cleaning.md`.
4. **Calculated Field Logic:** Tested and provided exact formulas for all 5 required fields in `tableau/calculated_fields.md`.
5. **Detailed Worksheet Blueprints:** Exact field-by-field instructions prepared for all 8 visualizations in `tableau/visualizations.md`.
6. **Dashboard & Story Architectures:** Comprehensive wireframe, layout, filter actions, and 3-scene story points in `tableau/dashboard_design.md` and `tableau/story_plan.md`.
7. **Performance Testing Documentation:** Epic 6 compliance report written in `docs/performance_testing.md`.
8. **Flask Web Application:** Complete, tested web application (`app.py`, `config.py`, templates, and CSS) embedding Tableau visuals.
9. **Automated Unit Testing:** Test suite `scripts/test_app.py` passed all route verification tests.
10. **Full 27-Section Academic Project Report:** Master report prepared in `docs/project_documentation.md`.
11. **Demo Script & 18 Viva Answers:** Student-friendly presentation guide in `docs/demo_script.md` and `docs/presentation_notes.md`.
12. **Git Repository Configuration:** Initialized local git repository with `.gitignore` and remote tracking.

---

## Part B: Your Tableau Desktop Manual Tasks (Numbered Click-by-Click)

Estimated time to complete: **15 to 20 minutes**.

### Step 1: Open Tableau & Connect Data (2 minutes)
1. Open **Tableau Desktop** (or **Tableau Public** application).
2. Under the left blue **Connect** pane, click **Text file**.
3. Browse to `D:\Skill wallet\data\` and select **`student_mental_health_cleaned.csv`**. Click **Open**.
4. Confirm you see 80 rows in the preview grid.
5. Click the orange **Sheet 1** tab at the bottom left.

---

### Step 2: Create the 5 Calculated Fields (3 minutes)
*(Right-click anywhere in the left Data pane -> click **Create Calculated Field...**)*

1. **`Performance_Category`**:
   * Name: `Performance_Category`
   * Formula:
     ```tableau
     IF [Academic_Performance] >= 90 THEN "Excellent"
     ELSEIF [Academic_Performance] >= 75 THEN "Good"
     ELSEIF [Academic_Performance] >= 60 THEN "Average"
     ELSE "Low"
     END
     ```
   * Click **OK**.

2. **`Sleep_Category`**:
   * Name: `Sleep_Category`
   * Formula:
     ```tableau
     IF [Sleep_Hours] >= 7.0 THEN "Healthy (7+ hrs)"
     ELSEIF [Sleep_Hours] >= 6.0 THEN "Moderate (6-7 hrs)"
     ELSE "Low Sleep (<6 hrs)"
     END
     ```
   * Click **OK**.

3. **`Stress_Category`**:
   * Name: `Stress_Category`
   * Formula:
     ```tableau
     IF [Stress_Level] <= 3 THEN "Low Stress"
     ELSEIF [Stress_Level] <= 6 THEN "Moderate Stress"
     ELSE "High Stress"
     END
     ```
   * Click **OK**.

4. **`Study_Hours_Category`**:
   * Name: `Study_Hours_Category`
   * Formula:
     ```tableau
     IF [Study_Hours] < 3.5 THEN "Light Study (<3.5 hrs)"
     ELSEIF [Study_Hours] <= 6.0 THEN "Balanced Study (3.5-6 hrs)"
     ELSE "Intensive Study (>6 hrs)"
     END
     ```
   * Click **OK**.

5. **`Calculated_Risk_Tier`**:
   * Name: `Calculated_Risk_Tier`
   * Formula:
     ```tableau
     IF ([Stress_Level] + [Anxiety_Level] + [Depression_Level]) >= 21 THEN "High Risk"
     ELSEIF ([Stress_Level] + [Anxiety_Level] + [Depression_Level]) >= 13 THEN "Medium Risk"
     ELSE "Low Risk"
     END
     ```
   * Click **OK**.

---

### Step 3: Build the 8 Worksheets (8 to 10 minutes)

* **Worksheet 1 (`Viz 1 - Impact of Study Hours on Performance`):**
  1. Drag `Study_Hours_Category` to **Columns**.
  2. Drag `Academic_Performance` to **Rows** -> right-click pill -> change **Measure** to **Average**.
  3. Drag `Stress_Level` to **Color** -> change Measure to **Average**.
  4. Click **Label** on Marks -> check **Show mark labels**.
  5. Right-click tab name -> Rename to `Viz 1 - Impact of Study Hours on Performance`.

* **Worksheet 2 (`Viz 2 - Gender and Depression Level`):**
  1. Click **New Worksheet** icon.
  2. Drag `Gender` to **Rows**.
  3. Drag `Depression_Level` to **Columns** -> change Measure to **Average**.
  4. Drag `Gender` to **Color**.
  5. Click **Label** -> check **Show mark labels**.
  6. Rename tab to `Viz 2 - Gender and Depression Level`.

* **Worksheet 3 (`Viz 3 - Study Hours vs Academic Performance`):**
  1. Click **New Worksheet**.
  2. Drag `Study_Hours` to **Columns**.
  3. Drag `Academic_Performance` to **Rows**.
  4. Drag `Student_ID` onto **Detail** tile in the Marks card (80 dots will appear!).
  5. Drag `Mental_Health_Risk` to **Color** (assign Green for Low, Orange for Medium, Red for High).
  6. Drag `Stress_Level` to **Size**.
  7. In the left **Analytics** tab, drag **Trend Line** onto **Linear**.
  8. Rename tab to `Viz 3 - Study Hours vs Academic Performance`.

* **Worksheet 4 (`Viz 4 - Average Stress Level by Gender`):**
  1. Click **New Worksheet**.
  2. Drag `Gender` to **Columns**.
  3. Drag `Stress_Level` to **Rows** -> change Measure to **Average**.
  4. Drag `Gender` to **Color**.
  5. Click **Label** -> check **Show mark labels**.
  6. Rename tab to `Viz 4 - Average Stress Level by Gender`.

* **Worksheet 5 (`Viz 5 - Analyzing Heart Rate Variability`):**
  1. Click **New Worksheet**.
  2. Drag `Mental_Health_Risk` to **Columns**.
  3. Drag `Heart_Rate_Variability` to **Rows** -> change Measure to **Average**.
  4. Drag `Mental_Health_Risk` to **Color**.
  5. Click **Label** -> check **Show mark labels**.
  6. Rename tab to `Viz 5 - Analyzing Heart Rate Variability`.

* **Worksheet 6 (`Viz 6 - KPI Overview Cards`):**
  1. Click **New Worksheet**.
  2. From Measures, double-click **Measure Values**.
  3. In the Measure Values shelf on the left, delete unwanted pills, leaving only:
     - `CNT(Student_ID)`
     - `AVG(Stress_Level)`
     - `AVG(Sleep_Hours)`
     - `AVG(Academic_Performance)`
  4. Drag **Measure Names** to **Columns**.
  5. Change Marks type to **Text**.
  6. At the top toolbar, change dropdown from 'Standard' to **Entire View**.
  7. Rename tab to `Viz 6 - KPI Overview Cards`.

* **Worksheet 7 (`Viz 7 - Mental Risk Level Distribution`):**
  1. Click **New Worksheet**.
  2. On Marks card, change mark dropdown to **Pie**.
  3. Drag `Mental_Health_Risk` to **Color**.
  4. Drag `Student_ID` to **Angle** -> change Measure to **Count**.
  5. Drag `Student_ID` to **Label** -> right-click -> **Quick Table Calculation** -> **Percent of Total**.
  6. Drag `Mental_Health_Risk` to **Label** as well.
  7. Set view dropdown to **Entire View**.
  8. Rename tab to `Viz 7 - Mental Risk Level Distribution`.

* **Worksheet 8 (`Viz 8 - Academic Performance Breakdown`):**
  1. Click **New Worksheet**.
  2. Drag `Performance_Category` to **Rows**.
  3. Drag `Student_ID` to **Columns** -> change Measure to **Count**.
  4. Drag `Performance_Category` to **Color**.
  5. Click **Label** -> check **Show mark labels**.
  6. Rename tab to `Viz 8 - Academic Performance Breakdown`.

---

### Step 4: Assemble the Master Dashboard (3 minutes)
1. Click the **New Dashboard** icon at the bottom.
2. In the left panel, set **Size** to **Automatic** (or Range: 1000px to 1600px).
3. Drag a **Text** object to the top: Type `Student Mental Health & Academic Well-Being Dashboard` (Bold, 18pt).
4. Drag `Viz 6 - KPI Overview Cards` directly below the title. Right-click its title and click **Hide Title**.
5. Drag `Viz 3` into the middle left, `Viz 4` into the middle center, and `Viz 7` into the middle right.
6. Drag `Viz 2` into bottom left, `Viz 5` into bottom center, and `Viz 8` into bottom right.
7. Click the small arrow on the Viz 3 frame -> select **Filters** -> check `Gender`, `Academic_Year`, `Department`, and `Mental_Health_Risk`.
8. For each filter that appears on the right, click its arrow -> **Apply to Worksheets** -> **All Using This Data Source**.
9. Click the small **Funnel** icon on Viz 7 ("Use as Filter").
10. Rename Dashboard tab to `Student Mental Health Dashboard`.

---

### Step 5: Build the 3-Scene Story (2 minutes)
1. Click the **New Story** icon at the bottom.
2. Set Story size to **Automatic**.
3. **Scene 1:** Drag `Viz 6`, `Viz 7`, and `Viz 4` onto the canvas. Set caption to:
   `Scene 1: Baseline Student Mental Health Landscape & Risk Distribution`
4. Click **Blank** at the top left to create Scene 2.
5. **Scene 2:** Drag `Viz 5` and `Viz 1` onto canvas. Set caption to:
   `Scene 2: Lifestyle Imbalances & Autonomic Strain (HRV & Sleep)`
6. Click **Blank** to create Scene 3.
7. **Scene 3:** Drag `Viz 3`, `Viz 2`, and `Viz 8` onto canvas. Set caption to:
   `Scene 3: Impact on Academic Efficacy & Targeted Intervention`
8. Rename Story tab to `Student Mental Health Story`.

---

### Step 6: Save and Publish to Tableau Public (2 minutes)
1. In Tableau, click **File** -> **Save As...** -> Save to `D:\Skill wallet\tableau\Student_Mental_Health_Analytics.twbx`.
2. Click **Server** in top menu -> hover over **Tableau Public** -> click **Save to Tableau Public As...**
3. Log in with your free Tableau Public account.
4. Set title: `Student Mental Health and Academic Well-Being Analytics` -> click **Save**.
5. When your browser opens on Tableau Public:
   * Click the **Share** button on the bottom right.
   * Copy the **Link** for the Dashboard.
   * Switch to the Story tab, click **Share**, and copy the **Link** for the Story.
6. Paste both URLs into `config.py` and `README.md`.

---

## Part C: Final Skill Wallet Submission Tasks

1. **Launch & Screenshot Web Portal:**
   * Run `python app.py` in PowerShell.
   * Open `http://127.0.0.1:5000` in your browser.
   * Take clean screenshots of the Overview, Dashboard, Story, and Dataset pages.
2. **Record Demo Video:**
   * Open OBS, Zoom, or Loom.
   * Read the 5–8 minute script in `docs/demo_script.md` while sharing your screen.
   * Upload video to Google Drive / YouTube (unlisted) and paste the link in `README.md`.
3. **Submit on Skill Wallet:**
   * Attach your GitHub repository URL: `https://github.com/parthpawar0707-blip/Skill-wallet`
   * Attach your Tableau Public workbook link.
   * Submit your screenshots as proof of completion for the 8 Epics!
