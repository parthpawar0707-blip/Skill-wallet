# Analysing Mental Health in Student Ecosystem

[![GitHub Pages Deployment](https://github.com/parthpawar0707-blip/Skill-wallet/actions/workflows/deploy.yml/badge.svg)](https://github.com/parthpawar0707-blip/Skill-wallet/actions/workflows/deploy.yml)
[![Live Portfolio](https://img.shields.io/badge/Live-GitHub%20Pages%20Portfolio-teal)](https://parthpawar0707-blip.github.io/Skill-wallet/)
[![Tableau Public Dashboard](https://img.shields.io/badge/Tableau-Public%20Dashboard-blue)](https://public.tableau.com/views/Student_Mental_Health_Analysis_sufiyan_17913953791380/AnalysingMentalHealthinStudentEcosystem?:language=en-US&publish=yes)

An applied data analytics and business intelligence portfolio investigating the multi-dimensional relationships between student lifestyle patterns, study habits, physiological telemetry, and mental health risks in higher education ecosystems.

Developed by **Parth Pawar** for the **SkillWallet / SmartBridge Virtual Internship (Data Analytics with Tableau)**.

---

## 🌟 Key Project Links

- 🌐 **Live Portfolio Website:** [https://parthpawar0707-blip.github.io/Skill-wallet/](https://parthpawar0707-blip.github.io/Skill-wallet/)
- 📊 **Published Tableau Public Dashboard:** [Student Mental Health Analysis](https://public.tableau.com/views/Student_Mental_Health_Analysis_sufiyan_17913953791380/AnalysingMentalHealthinStudentEcosystem?:language=en-US&publish=yes)
- 📁 **Dataset Source:** [Google Sheets Dataset (1,000 Records)](https://docs.google.com/spreadsheets/d/1DSnFv7DdV8l1nBcQ-KNIrbgnmDMIDeh7/edit?usp=sharing)
- 🎥 **Walkthrough Video:** `site/assets/video/student-mental-health-demo.mp4` (Natural Indian English, 720p HD, with captions)

---

## 🎯 Executive Overview & Problem Statement

Undergraduate students face compounding pressures including heavy examination loads, competitive GPA standards, disrupted sleep schedules, and extended digital screen time. These stressors frequently lead to unmanaged mental exhaustion, depressive symptoms, and high university attrition.

Traditional university support structures typically discover student distress reactively—after examination failures or excessive absenteeism. This project provides an interactive, data-driven Business Intelligence (BI) platform that combines self-reported psychological surveys with objective physiological telemetry (Heart Rate Variability) to deliver proactive decision-support for campus advisors and counseling centers.

---

## 📊 Verified Dataset & Schema Architecture

The analysis is based on the certified Google Sheets deliverable containing **1,000 collegiate profiles across 16 multi-dimensional variables** with **100% data completeness (0 nulls, 0 duplicate records)**:

| Category | Field Name | Type | Description & Boundaries |
|---|---|---|---|
| **Demographics** | `Student_ID` | Integer | Unique identifier (`1` to `1000`) |
| | `Age` | Integer | Chronological age (`18` to `25` years) |
| | `Gender` | String | Cohort categorization (`Male`, `Female`, `Other`) |
| **Psychological** | `Stress_Level` | Integer | Self-reported stress scale (`1` to `10`) |
| | `Anxiety_Level` | Integer | Generalized anxiety scale (`1` to `10`) |
| | `Depression_Level` | Integer | Depressive symptom severity scale (`1` to `10`) |
| **Lifestyle** | `Sleep_Duration_Hours` | Float | Nightly sleep duration (`2.8` to `10.4` hrs) |
| | `Study_Hours_Per_Day` | Float | Daily self-study duration (`1.0` to `8.0` hrs) |
| | `Social_Interaction_Score` | Integer | Daily peer interaction score (`1` to `9`) |
| **Academic** | `Attendance_Rate (%)` | Float | Class attendance percentage (`60.1%` to `100.0%`) |
| | `Academic_Performance_Index`| Float | Cumulative grade percentage (`50.0%` to `100.0%`) |
| | `LMS_Activity_Score` | Integer | Learning Management System activity (`10` to `99`) |
| **Biometric** | `Heart_Rate_Variability` | Float | Autonomic cardiac vagal tone / RMSSD (`36.6` to `99.2` ms) |
| **Interventions** | `Mental_Health_Risk` | String | Stratified risk tier (`Low`, `Medium`, `High`) |
| | `Personalized_Intervention` | String | 8 structured counseling strategies |
| | `Emotional_Journal` | Text | Qualitative journal entry (preserved privately) |

---

## 💡 Verified Key Performance Indicators (KPIs)

- **Total Students:** `1,000`
- **Average Stress Level:** `5.45 / 10`
- **Average Depression Level:** `5.50 / 10`
- **Average Sleep Duration:** `6.49 hours/day`
- **Average Attendance Rate:** `79.96%`
- **Average Academic Performance Index:** `75.12%`
- **Average Heart Rate Variability (HRV):** `69.71 ms`
- **Mental Health Risk Breakdown:** Low Risk (`41.4%`), Medium Risk (`34.7%`), High Risk (`23.9%`)

---

## 🔬 Key Empirical Findings

1. **Sleep Duration as a Primary Stress Buffer:**  
   Students with under 6.0 hours of nightly sleep exhibited an average stress score of `6.2`, compared to `4.8` for students getting `7.5+ hours`.
2. **Diminishing Academic Returns Beyond 5.5 Hours:**  
   Increasing study hours past 5.5 hours per day yields diminishing academic performance gains when accompanied by acute anxiety scores (&ge; 7/10).
3. **Biometric Validation via Suppressed HRV:**  
   Students in the High Risk tier display suppressed Heart Rate Variability (<50 ms), objectively validating self-reported subjective survey ratings.
4. **Peer Connection Drives Resilience:**  
   Students maintaining social interaction scores &ge; 6 reported significantly lower depression levels (`4.6` vs `6.1` for socially isolated students).

---

## 📁 Repository Structure

```
Skill-wallet/
├── site/                               # Static portfolio deployed to GitHub Pages
│   ├── index.html                      # Main portfolio landing page
│   ├── assets/
│   │   ├── css/styles.css              # Modern responsive CSS styling
│   │   ├── js/main.js                  # Frontend interactions & fallback handling
│   │   ├── data/summary.json           # Verified aggregate analytics payload
│   │   └── video/
│   │       ├── student-mental-health-demo.mp4  # 720p HD walkthrough video
│   │       ├── narration.mp3           # Natural Indian English narration track
│   │       ├── video-captions.srt      # Subtitles (SRT format)
│   │       └── video-captions.vtt      # Subtitles (WebVTT for HTML5 video)
│   └── README.md
├── docs/                               # Formal academic and project documentation
│   ├── project-report.md               # 20+ section comprehensive academic report
│   ├── methodology.md                  # 10-step analytical methodology
│   ├── video-narration.md              # Full video narration transcript & timings
│   ├── video-production-notes.md       # Video encoding & audio technical specs
│   └── data_preparation.md             # Dataset schema & validation report
├── scripts/                            # Reproducible Python scripts
│   ├── analyze_dataset.py              # Google Sheets audit & summary generator
│   ├── generate_narration.py           # Edge Neural TTS narration generator
│   ├── build_walkthrough_video.py      # Automated FFmpeg video rendering pipeline
│   ├── validate_dataset.py             # Data integrity validation
│   └── prepare_dataset.py              # Data cleaning pipeline
├── .github/
│   └── workflows/deploy.yml            # Automated GitHub Pages CI/CD workflow
├── .gitignore
└── README.md
```

---

## 🚀 Local Development & Execution

### 1. Run Dataset Audit & Generate Summary JSON:
```powershell
python scripts/analyze_dataset.py
```

### 2. Run Portfolio Locally:
```powershell
# Open site/index.html in any modern web browser or start a local server:
cd site
python -m http.server 8000
# Browse to: http://localhost:8000
```

---

## ⚖️ Ethics, Privacy & Responsible Use
- **Educational Scope:** This study is an academic data analytics project for decision-support modeling. It is **not** an automated clinical diagnostic tool or medical recommendation system.
- **Student Privacy:** Qualitative emotional journal entries and row-level personal data are kept confidential and represented only through aggregate biostatistical summaries.

---

## 👤 Author & Acknowledgments
- **Project Lead:** Parth Pawar
- **Repository:** [https://github.com/parthpawar0707-blip/Skill-wallet](https://github.com/parthpawar0707-blip/Skill-wallet)
- **Institution / Program:** SkillWallet &bull; SmartBridge Virtual Internship 2025–2026
