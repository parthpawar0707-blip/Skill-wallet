# Methodology: Student Mental Health Analytics

**Project Title:** Analysing Mental Health in Student Ecosystem  
**Author / Lead Analyst:** Parth Pawar  
**Program:** SkillWallet / SmartBridge Virtual Internship &bull; Data Analytics with Tableau  
**Repository:** https://github.com/parthpawar0707-blip/Skill-wallet  
**Live Site:** https://parthpawar0707-blip.github.io/Skill-wallet/  

---

## The 10-Step Analytical Lifecycle

```
[1. Data Acquisition & Provenance] -> [2. Data Quality & Hygiene Audit] -> [3. Privacy & Ethics Protocol] 
                                                  |
                                                  v
[4. Feature Engineering in Tableau] <- [5. Data Extraction & Workbook Ingestion]
         |
         v
[6. Worksheet Construction (8 Views)] -> [7. Dashboard Sizing & Filter Scoping] -> [8. Story Design]
                                                                                            |
                                                                                            v
[9. Video Walkthrough & Audio Engineering] <- [10. Web Portfolio & CI/CD Deployment] <-------+
```

---

### Step 1: Data Acquisition & Provenance
- Source repository and Google Sheets dataset inspected:
  `https://docs.google.com/spreadsheets/d/1DSnFv7DdV8l1nBcQ-KNIrbgnmDMIDeh7/edit?usp=sharing` (1,000 records × 16 variables).
- Anonymized analytical extract created for Tableau workbook modeling:
  `data/mental_health_student_ecosystem_cleaned.csv` (200 undergraduate profiles × 18 variables).

---

### Step 2: Data Quality & Hygiene Audit
- Automated verification using Python (`pandas`):
  - **Uniqueness:** 200 distinct student records (`STU_0001` through `STU_0200`).
  - **Completeness:** Zero missing or null values across all 3,600 cells (100% data density).
  - **Duplicate Audit:** Zero duplicate records.
  - **Range Boundaries:** Anxiety and Depression scores validated in the `0–100` range; Daily Screen Time validated between `3.5` and `12.0` hours; Age restricted to undergraduate brackets (`18–25` years).

---

### Step 3: Privacy & Ethics Protocol
- Student identification anonymized via synthetic alphanumeric tokens (`STU_xxxx`).
- All qualitative subjective texts (such as individual emotional journals) are preserved privately and omitted from public GitHub and web assets.
- Explicit non-clinical disclaimers integrated across all presentations and web pages.

---

### Step 4: Feature Engineering & Calculated Fields
Two business logic calculated fields were engineered directly in Tableau Desktop:

1. **`Active_Therapy`**:
   ```tableau
   IF [Therapy Type] != "No Therapy" THEN 1 ELSE 0 END
   ```
   *Rationale:* Aggregates students receiving active clinical intervention across CBT, Counseling, Support Groups, and Meditation to evaluate institutional program uptake.

2. **`HighStress_PoorSleep`**:
   ```tableau
   IF [Stress Level] = "High" AND [Sleep Quality] = "Poor" THEN 1 ELSE 0 END
   ```
   *Rationale:* Identifies compound risk vulnerability. Students concurrently experiencing poor sleep and severe stress constitute 35 of the 49 high-stress students (71.4%), marking this sub-group as the highest priority for campus wellness intervention.

---

### Step 5: Data Extraction & Workbook Ingestion
- Connected the cleaned CSV extract to Tableau Desktop.
- Categorized dimensions (`User ID`, `Gender`, `Stress Level`, `Sleep Quality`, `Physical Activity Level`, `Therapy Type`, `Mental Health History`).
- Categorized continuous measures (`Anxiety Score`, `Depression Score`, `Daily Screen Time (hrs)`, `Progress Score`, `Intervention Duration (weeks)`).

---

### Step 6: Worksheet Construction (8 Core Views)
1. **Stress Distribution:** Bar column distribution displaying Low (44), Medium (107), High (49).
2. **Screen Time vs. Stress:** Average screen hours across stress tiers (6.00h, 7.07h, 8.12h).
3. **Sleep Quality vs. Stress:** Cross-tabulation isolating 35 high-stress cases in the poor sleep group.
4. **Gender Mental Health Comparison:** Multi-series bar chart evaluating anxiety and depression parity.
5. **Stress vs. Anxiety:** Escalation bar chart mapping 30.27 (Low) to 72.06 (High).
6. **Stress vs. Depression:** Escalation bar chart mapping 26.80 (Low) to 68.78 (High).
7. **Therapy Efficacy:** Progress scores ranked across CBT (40.80), Counseling (34.43), Groups (33.10), Meditation (32.57).
8. **History Prevalence:** Proportional distribution showing 40% with prior history.

---

### Step 7: Dashboard Sizing & Filter Scoping
- Sized dashboard using modern 1366×768 responsive canvas dimensions.
- Integrated top-ribbon executive scorecard highlighting the 4 core benchmarks (200 Students, 52.59 Anxiety, 48.09 Depression, 7.10h Screen Time).
- Structured worksheets into scannable analytical zones with linked filter parameters.

---

### Step 8: Story Design & Tableau Public Publishing
- Sequenced analytical narrative through cohort baseline, digital lifestyle drivers, and therapeutic intervention pathways.
- Published to Tableau Public cloud servers and verified public embed parameters (`:embed=yes&:showVizHome=no`).

---

### Step 9: Video Walkthrough & Audio Engineering
- **Scripting:** Formatted 8 conversational chapters covering background, data, methodology, Tableau charts, and findings.
- **Narration Synthesis:** Generated natural Indian English male narration using Microsoft Edge Neural TTS (`en-IN-PrabhatNeural`, calibrated at `pitch="-5Hz"` and `rate="+22%"`).
- **Synchronization:** Edited 15 visual scenes using FFmpeg, matching spoken narration 1:1 with genuine Tableau dashboard recordings.
- **Duration & Assets:** Final video rendered to **06:41.97** (401.97s, 9.44 MB, 1280×720 H.264/AAC), accompanied by WebVTT and SubRip subtitle tracks.

---

### Step 10: Web Portfolio & CI/CD Deployment
- Built static web application in `site/` with 11 structured sections.
- Embedded Tableau dashboard with backdrop capture preview and 7-second fallback.
- Verified responsive layout across 1440×900, 768×1024, 390×844, and 360×800.
- Implemented dual root and `site/` redundancy for GitHub Pages deployment compatibility.
- Automated CI/CD deployment via GitHub Actions (`.github/workflows/deploy.yml`).
