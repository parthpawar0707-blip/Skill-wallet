# Analysing Mental Health in Student Ecosystem

[![GitHub Pages Deployment](https://github.com/parthpawar0707-blip/Skill-wallet/actions/workflows/deploy.yml/badge.svg)](https://github.com/parthpawar0707-blip/Skill-wallet/actions/workflows/deploy.yml)
[![Live Portfolio](https://img.shields.io/badge/Live-GitHub%20Pages%20Portfolio-teal)](https://parthpawar0707-blip.github.io/Skill-wallet/)
[![Tableau Public Dashboard](https://img.shields.io/badge/Tableau-Public%20Dashboard-blue)](https://public.tableau.com/views/Student_Mental_Health_Analysis_sufiyan_17913953791380/AnalysingMentalHealthinStudentEcosystem?:language=en-US&publish=yes)
[![License: MIT](https://img.shields.io/badge/License-MIT-slate.svg)](LICENSE)

An applied data analytics and business intelligence portfolio investigating the multi-dimensional relationships between student lifestyle patterns, study habits, digital telemetry, and mental health risks in higher education ecosystems.

Developed by **Parth Pawar** for the **SkillWallet / SmartBridge Virtual Internship (Data Analytics with Tableau)**.

---

## Table of Contents

- [A. Project Title & Introduction](#a-project-title--introduction)
- [B. Project Links & Deployment Status](#b-project-links--deployment-status)
- [C. Problem Statement](#c-problem-statement)
- [D. Project Objectives](#d-project-objectives)
- [E. Dataset Description & Provenance](#e-dataset-description--provenance)
- [F. Technology Stack](#f-technology-stack)
- [G. Project Features](#g-project-features)
- [H. Tableau Visualization Inventory](#h-tableau-visualization-inventory)
- [I. Key Analytical Findings](#i-key-analytical-findings)
- [J. UI/UX Design System & Accessibility](#j-uiux-design-system--accessibility)
- [K. Video Walkthrough & Audio Engineering](#k-video-walkthrough--audio-engineering)
- [L. Local Setup & Development](#l-local-setup--development)
- [M. GitHub Pages Deployment & CI/CD](#m-github-pages-deployment--cicd)
- [N. Project Structure](#n-project-structure)
- [O. Documentation Index](#o-documentation-index)
- [P. Limitations & Responsible Use](#p-limitations--responsible-use)
- [Q. Future Enhancements](#q-future-enhancements)
- [R. Credits & References](#r-credits--references)

---

## A. Project Title & Introduction

# Analysing Mental Health in Student Ecosystem

Undergraduate students face a challenging convergence of rigorous academic deadlines, competitive performance benchmarks, erratic sleep cycles, and extended digital screen exposure. While universities provide counseling infrastructure, intervention is traditionally reactive—occurring only after students experience academic probation, severe absenteeism, or complete withdrawal.

This project delivers an interactive, data-driven Business Intelligence (BI) platform that models self-reported psychological indicators (stress, anxiety, depression) alongside lifestyle telemetry (sleep quality, daily screen hours, physical activity) and structured support modalities (CBT, counseling, meditation). 

The platform is designed for:
- **Academic Advisors & Mentors:** To recognize systemic indicators of student strain early in the semester.
- **Campus Counseling Services:** To assess the relative progress scores associated with different intervention strategies.
- **Higher Education Administrators:** To base campus wellness policies on verifiable empirical data rather than anecdotal assumptions.

---

## B. Project Links & Deployment Status

| Resource | URL / Location | Status |
| :--- | :--- | :---: |
| **Live Portfolio Website** | [https://parthpawar0707-blip.github.io/Skill-wallet/](https://parthpawar0707-blip.github.io/Skill-wallet/) | **Active (HTTP 200 OK)** |
| **GitHub Repository** | [https://github.com/parthpawar0707-blip/Skill-wallet](https://github.com/parthpawar0707-blip/Skill-wallet) | **Public / Main** |
| **Tableau Public Dashboard** | [Analysing Mental Health in Student Ecosystem](https://public.tableau.com/views/Student_Mental_Health_Analysis_sufiyan_17913953791380/AnalysingMentalHealthinStudentEcosystem?:language=en-US&publish=yes) | **Live / Published** |
| **Dataset Source (Google Sheets)** | [Student Mental Health Google Sheet](https://docs.google.com/spreadsheets/d/1DSnFv7DdV8l1nBcQ-KNIrbgnmDMIDeh7/edit?usp=sharing) | **Verified Source** |
| **Walkthrough Video Asset** | [`site/assets/video/student-mental-health-demo.mp4`](file:///d:/Skill%20wallet/site/assets/video/student-mental-health-demo.mp4) | **Verified (06:42 / 9.44 MB)** |

*Deployment Note:* Both root (`/index.html`) and `./site` directory structures are mirrored and kept in sync, ensuring that the portfolio loads reliably whether GitHub Pages is configured via GitHub Actions or branch deployment (`main / root`).

---

## C. Problem Statement

Modern university students balance complex commitments across academics, social obligations, and digital connectivity. However, institutional wellness initiatives often operate without integrated data systems:
1. **Academic & Curricular Pressures:** Examination milestones and cumulative performance expectations create cyclical stress spikes that are rarely tracked alongside wellness indicators.
2. **Lifestyle & Telemetry Imbalances:** Late-night screen exposure and compromised sleep quality directly correlate with elevated anxiety and depressive symptoms, yet remain largely invisible to advisors.
3. **Reactive vs. Proactive Decision Support:** Campus counseling services are frequently overburdened because interventions begin only after severe academic or emotional crises occur.

> **Non-Clinical Notice:** This study is an exploratory data analytics project intended strictly for institutional decision-support and educational insight. It is **not** a clinical diagnostic instrument, psychiatric evaluation, or medical guidance tool.

---

## D. Project Objectives

1. **Reconcile & Audit Data Hygiene:** Inspect raw student records to ensure 100% data cleanliness, zero null values, and valid clinical ranges.
2. **Model Multi-Dimensional Lifestyle Indicators:** Quantify how daily screen time, sleep quality, and physical activity correlate with standardized stress, anxiety, and depression scores.
3. **Engineer Tableau Calculated Fields:** Create analytical measures (`Active_Therapy` and `HighStress_PoorSleep`) to isolate actionable student sub-cohorts.
4. **Develop an Interactive Tableau BI Workbook:** Publish executive KPI ribbons, segmented distribution charts, and cross-filtering mechanisms to Tableau Public.
5. **Architect a Production Web Portfolio:** Deploy an editorial, responsive, accessible portfolio on GitHub Pages with embedded Tableau visualization and zero white-space voids.
6. **Produce a Synchronized Walkthrough Video:** Deliver a 5–7 minute walkthrough with natural Indian English male narration and 1:1 synchronized dashboard recordings.
7. **Document Analytical Rigor & Ethics:** Maintain reproducible documentation, clear limitations, and strict student privacy safeguards.

---

## E. Dataset Description & Provenance

To resolve conflicting dataset references found across preliminary drafts:

### 1. Benchmark Source vs. Analytical Extract
- **Google Sheets Benchmark Source:**  
  URL: `https://docs.google.com/spreadsheets/d/1DSnFv7DdV8l1nBcQ-KNIrbgnmDMIDeh7/edit?usp=sharing`  
  Dimensions: **1,000 rows &times; 16 variables**.  
  Included fields: `Student_ID`, `Age`, `Gender`, `Stress_Level`, `Anxiety_Level`, `Depression_Level`, `Heart_Rate_Variability`, `Sleep_Duration_Hours`, `Attendance_Rate (%)`, `Study_Hours_Per_Day`, `LMS_Activity_Score`, `Social_Interaction_Score`, `Academic_Performance_Index`, `Emotional_Journal`, `Mental_Health_Risk`, `Personalized_Intervention_Strategy`.  
  *Privacy Safeguard:* Individual qualitative `Emotional_Journal` text entries are kept private and never published to client-facing web assets.

- **Verified Tableau Workbook Extract (Ground Truth):**  
  File: `data/mental_health_student_ecosystem_cleaned.csv` (and `assets/data/summary.json`).  
  Dimensions: **Exactly 200 student records (`STU_0001` to `STU_0200`) across 18 cleaned variables**.  
  Data Completeness: **100% (0 nulls, 0 duplicates across all 3,600 cells)**.  
  This exact extract powers the published Tableau Public workbook and live portfolio KPIs.

- **Preliminary Prototype Exploration:**  
  File: `data/student_mental_health.csv` (80 rows &times; 19 columns with 6 missing values). Retained solely for historical pipeline context.

### 2. Complete Schema Specification (200-Student Extract)
| Attribute Name | Data Type | Permissible Range / Values | Analytical Purpose |
| :--- | :--- | :--- | :--- |
| `User ID` | String | `STU_0001` – `STU_0200` | Anonymized unique student identifier |
| `Age` | Integer | 18 – 25 years | Chronological student age |
| `Gender` | String | Female, Male, Other | Demographic categorization |
| `Occupation` | String | Student, Working Student | Academic/workload status |
| `Stress Level` | String | Low, Medium, High | Perceived general stress tier |
| `Anxiety Score` | Integer | 0 – 100 | Standardized generalized anxiety scale |
| `Depression Score` | Integer | 0 – 100 | Standardized depression symptom rating |
| `Sleep Quality` | String | Poor, Average, Good | Qualitative sleep restoration |
| `Daily Screen Time (hrs)` | Float | 3.5 – 12.0 hrs | Daily hours on mobile/laptop screens |
| `Physical Activity Level` | String | Low, Moderate, High | Weekly exercise engagement |
| `Social Interaction Score`| Integer | 1 – 10 | Peer engagement rating |
| `Mental Health History` | String | Yes, No | Prior personal or familial condition |
| `Therapy Type` | String | CBT, Counseling, Support Group, Meditation, No Therapy | Active support modality |
| `Intervention Duration (weeks)` | Integer | 0 – 24 weeks | Duration enrolled in intervention |
| `Progress Score` | Integer | 0 – 100 | Therapeutic improvement metric |
| `Medication Usage` | String | Yes, No | Prescribed psychotropic medication |
| `Support System Strength` | String | Low, Medium, High | Family/mentor support network rating |
| `Work-Life Balance Score` | Integer | 1 – 10 | Subjective academic equilibrium rating |

---

## F. Technology Stack

Only tools and libraries actively utilized in the final codebase are listed:

- **Business Intelligence & Visualization:** Tableau Desktop 2024 / Tableau Public Cloud.
- **Frontend Core:** HTML5 (Semantic elements, WebVTT tracks), CSS3 (CSS Variables, Flexbox/Grid, Fluid Typography via `clamp()`), Modern ES6+ JavaScript.
- **Icons & Typography:** Lucide Outline SVG Icons (zero generic emojis), Google Fonts (`Inter`).
- **Data Engineering & Analysis:** Python 3.11, `pandas`, `numpy`, `tableauhyperapi`.
- **Audio Engineering & Speech Synthesis:** Microsoft Edge Neural TTS (`edge-tts` engine, `en-IN-PrabhatNeural` model with pitch/rate shaping).
- **Video Production & Compositing:** FFmpeg 7.x (H.264 video encoding, AAC audio muxing, subtitle burning).
- **Version Control & CI/CD:** Git, GitHub, GitHub Actions (`actions/configure-pages@v5`, `actions/deploy-pages@v4`).
- **Local Application Server:** Python Flask 3.x (optional local exploratory server with Jinja2 templates).

---

## G. Project Features

- **Editorial UI/UX Design System:** Clean white card surfaces (`#FFFFFF`), subtle slate borders (`#E2E8F0`), deep navy typography (`#0F172A`), and deep teal accents (`#0F766E`).
- **Strict 11-Section Layout:** Follows a logical presentation structure from introduction to dataset, KPIs, dashboard, gallery, video, methodology, and verified links.
- **Resilient Tableau Public Embed:** Pre-loads a crisp backdrop capture (`tableau_capture.png`) with loading spinner, preventing white voids. Features an automatic 7-second fallback with direct launch CTA.
- **Verified KPI Scorecard:** 4 prominent cards displaying cohort totals and averages with tabular numerals.
- **Interactive Video Player:** Embedded HTML5 player with poster image, WebVTT captions, and an interactive **8-Chapter Quick-Jump Bar**.
- **Responsive Layout Across All Viewports:** Audited and verified at 1440&times;900, 768&times;1024, 390&times;844, and 360&times;800 with zero horizontal scroll.
- **Dual-Deployment Redundancy:** Root (`/`) and `./site` directories mirrored for seamless GitHub Pages deployment.

---

## H. Tableau Visualization Inventory

The published Tableau dashboard integrates 8 core analytical worksheets:

| Worksheet | Chart Type | Key Metrics / Dimensions | Core Finding & Question Answered |
| :--- | :--- | :--- | :--- |
| **1. Stress Distribution** | Column Chart | `Stress Level`, `COUNT(User ID)` | 107 Medium (53.5%), 49 High (24.5%), 44 Low (22.0%). Over 78% of students experience moderate-to-severe stress. |
| **2. Screen Time vs. Stress** | Bar Chart | `Stress Level`, `AVG(Screen Time)` | High-stress students average 8.12 hrs/day vs. 6.00 hrs for low-stress peers (+2.12 hr daily excess). |
| **3. Sleep Quality vs. Stress**| Stacked Cross-Tab | `Sleep Quality`, `Stress Level` | 35 of 66 poor sleepers experience high stress (53%). Only 2 good sleepers experience high stress (4.4%). |
| **4. Gender Comparison** | Grouped Bars | `Gender`, `AVG(Anxiety)`, `AVG(Depression)` | Anxiety (51.8–53.5) and Depression (47.9–50.4) show parity across gender cohorts; stress is campus-wide. |
| **5. Stress vs. Anxiety** | Bar Chart | `Stress Level`, `AVG(Anxiety Score)` | Anxiety escalates monotonically: Low (30.27) &rarr; Med (52.85) &rarr; High (72.06) (+138%). |
| **6. Stress vs. Depression** | Bar Chart | `Stress Level`, `AVG(Depression Score)` | Depression scores surge from Low (26.80) to High (68.78) (+156% increase in acute distress). |
| **7. Therapy Efficacy** | Ranked Bars | `Therapy Type`, `AVG(Progress Score)` | CBT yields highest progress (40.80), followed by Counseling (34.43), Groups (33.10), and Meditation (32.57). |
| **8. History Prevalence** | Proportional Ring | `Mental Health History`, `COUNT(User ID)` | 80 students (40%) report prior history, emphasizing the need for proactive orientation screening. |

*Detailed inventory documentation:* [`docs/tableau-dashboard-inventory.md`](file:///d:/Skill%20wallet/docs/tableau-dashboard-inventory.md)

---

## I. Key Analytical Findings

1. **Sleep Quality as the Primary Psychological Buffer:**  
   Sleep quality functions as the single strongest protective factor. Among students reporting good sleep quality, only 4.4% (2 students) registered high stress. Conversely, 71.4% of all high-stress students in the cohort suffer from poor sleep.
2. **The 7.5-Hour Digital Screen Threshold:**  
   Daily screen time exceeding 7.5 hours strongly associates with acute stress classification. High-stress students log an average of 8.12 hours daily, suggesting digital fatigue or escapism as a major compounding stressor.
3. **Demographic Equity in Psychological Distress:**  
   Anxiety and depression levels show negligible statistical differences across male, female, and other gender cohorts. Interventions must be universal campus policies rather than segmented exclusively by demographic traits.
4. **Therapeutic Progress Differential:**  
   Students undergoing Cognitive Behavioral Therapy (CBT) demonstrated the highest average progress rating (40.80), outperforming unstructured support groups (33.10) and general meditation (32.57).

> **Causal Disclaimer:** These observations represent statistical associations within an observational sample. Screen time and poor sleep correlate with elevated symptoms, but bidirectional influences (e.g., anxious students using screens for avoidance) cannot be ruled out.

---

## J. UI/UX Design System & Accessibility

- **Design Philosophy:** Clean, editorial research layout inspired by modern scientific and SaaS design systems (Stripe, Linear).
- **Color Variables:**
  - Page Background: `#F8FAFC` (Slate 50)
  - Card Surfaces: `#FFFFFF` with 1px border `#E2E8F0`
  - Body Text: `#334155` (Slate 700)
  - Headings: `#0F172A` (Slate 900)
  - Primary Accent: `#0F766E` (Teal 700)
- **Accessibility Enhancements:**
  - Semantic HTML5 structure (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`).
  - Text contrast ratios exceed WCAG 2.1 AA standards (minimum 4.5:1 for body copy; 7:1 for headings).
  - Keyboard-navigable skip link (`#main-content`) and focus rings on all interactive elements.
  - Video player includes WebVTT subtitle tracks (`kind="captions"`) for hearing accessibility.
- **Responsive Layout Verification:** Verified with headless Chrome across desktop (1440&times;900), tablet (768&times;1024), and mobile viewports (390&times;844, 360&times;800) with zero horizontal overflow.

---

## K. Video Walkthrough & Audio Engineering

| Specification | Value / Detail |
| :--- | :--- |
| **File Location** | [`site/assets/video/student-mental-health-demo.mp4`](file:///d:/Skill%20wallet/site/assets/video/student-mental-health-demo.mp4) (mirrored in `assets/video/`) |
| **Verified Duration** | **06:41.97** (401.97 seconds, strictly within the 5:00 to 7:00 minute window) |
| **File Size** | **9,898,270 bytes** (~9.44 MB) |
| **Video Encoding** | H.264 / AVC High Profile, 1280&times;720 HD, 30.0 fps progressive |
| **Audio Encoding** | AAC, 24,000 Hz, Mono, ~110–144 kbps |
| **Voice Engine** | Microsoft Edge Neural TTS (`edge-tts`) |
| **Voice Model** | `en-IN-PrabhatNeural` (Natural Indian English Male) |
| **Acoustic Shaping** | `pitch="-5Hz"` (Acoustic warmth, zero high-pitch distortion), `rate="+22%"` (Conversational presentation tempo) |
| **Subtitle Formats** | Synchronized WebVTT (`video-captions.vtt`) and SubRip (`video-captions.srt`) |
| **Visual Synchronization** | 15 scenes edited in FFmpeg matching narration 1:1 with authentic Tableau Public dashboard footage |

### Interactive Video Chapter Navigation
The video player on the portfolio website features an interactive chapter quick-jump bar:
- `00:00` Overview & Welcome
- `00:45` Cohort KPIs
- `01:30` Sleep Buffer
- `02:15` Screen Time
- `03:00` Extracurriculars
- `03:45` Therapy Efficacy
- `04:30` Calculated Fields
- `05:30` Recommendations

---

## L. Local Setup & Development

### 1. Static Website (Recommended for Quick Preview)
The portfolio website is entirely static and requires no server runtime to test:

```bash
# Clone the repository
git clone https://github.com/parthpawar0707-blip/Skill-wallet.git
cd Skill-wallet

# Serve the static website on port 8080 (Python standard library)
python -m http.server 8080 --directory site

# Or test the mirrored root directory
python -m http.server 8080
```
Open your browser to `http://localhost:8080`.

### 2. Optional Local Flask Application
The repository also includes an optional local Flask exploratory application (`app.py`):

```bash
# Install dependencies
pip install -r requirements.txt

# Start the Flask development server
python app.py
```
Open your browser to `http://localhost:5000`.

> **Important Deployment Distinction:** GitHub Pages **only** serves static assets (`HTML`, `CSS`, `JS`, media). GitHub Pages does **not** run Python or execute Flask servers. The Flask application is retained strictly for local development and offline inspection.

---

## M. GitHub Pages Deployment & CI/CD

Deployment is fully automated via GitHub Actions:
- **Workflow File:** [`.github/workflows/deploy.yml`](file:///d:/Skill%20wallet/.github/workflows/deploy.yml)
- **Deployment Trigger:** Every push to branch `main`.
- **Target Folder:** `./site` (with mirrored files at `./` for dual redundancy).
- **Actions Used:**
  - `actions/checkout@v4`
  - `actions/configure-pages@v5`
  - `actions/upload-pages-artifact@v3` (packages `./site`)
  - `actions/deploy-pages@v4`

### Required Repository Settings
If GitHub Pages is not deploying automatically, ensure that:
1. Navigate to **Settings > Pages** in your GitHub repository.
2. Under **Build and deployment > Source**, select **GitHub Actions** (or select **Deploy from a branch > main / (root)**).
3. Both configurations will succeed because root files (`index.html`, `404.html`, `assets/`) and `./site` are identical.

---

## N. Project Structure

```text
Skill-wallet/
├── .github/
│   └── workflows/
│       └── deploy.yml              # GitHub Actions Pages deployment workflow
├── assets/                         # Mirrored root static assets
│   ├── css/styles.css              # Editorial responsive CSS stylesheet
│   ├── js/main.js                  # Navigation, fallback & chapter jump logic
│   ├── data/summary.json           # Verified 200-student aggregate metrics
│   ├── images/                     # UI captures & backdrop preview images
│   └── video/                      # Walkthrough MP4, narration MP3, VTT/SRT captions
├── data/
│   ├── mental_health_student_ecosystem_cleaned.csv  # 200-student Tableau extract (Ground Truth)
│   ├── student_mental_health.csv                    # 80-student prototype data
│   └── student_mental_health_cleaned.csv            # Cleaned prototype data
├── docs/
│   ├── project-report.md           # Formal academic and institutional project report
│   ├── methodology.md              # 10-step analytical methodology
│   ├── tableau-dashboard-inventory.md  # 8-worksheet structural inventory
│   ├── video-narration.md          # 8-chapter verbatim narration script
│   ├── video-storyboard.md         # 15-scene visual storyboard
│   ├── video-visual-audit.md       # Audio-visual synchronization audit
│   ├── video-production-notes.md   # Technical media specs & encoding details
│   ├── repair-report.md            # Diagnostic and remediation report
│   └── [test screenshots]          # Responsive visual test captures (1440, 768, 390, 360)
├── scripts/
│   ├── analyze_dataset.py          # Data validation & summary.json generator
│   ├── build_natural_video.py      # 15-scene FFmpeg video compositor
│   └── clean_data.py               # Data cleaning & standardization script
├── site/                           # Canonical static website folder
│   ├── index.html                  # Main 11-section portfolio website
│   ├── 404.html                    # Custom 404 error page
│   └── assets/                     # Styles, scripts, images, and video assets
├── templates/                      # Flask Jinja2 templates (local app)
├── static/                         # Flask static styles (local app)
├── app.py                          # Local Flask exploratory web application
├── config.py                       # Flask configuration module
├── requirements.txt                # Python dependencies
├── index.html                      # Mirrored root entry point
├── 404.html                        # Mirrored root 404 page
└── README.md                       # Master project technical documentation
```

---

## O. Documentation Index

All technical documents are maintained in the [`docs/`](file:///d:/Skill%20wallet/docs/) directory:

- [**Comprehensive Project Report**](docs/project-report.md): Formal research report covering academic context, data hygiene, and institutional findings.
- [**Analytical Methodology**](docs/methodology.md): Step-by-step breakdown of the 10-stage data lifecycle.
- [**Tableau Dashboard Inventory**](docs/tableau-dashboard-inventory.md): Structural review of all 8 worksheets and calculated fields.
- [**Video Narration Script**](docs/video-narration.md): Complete verbatim transcript for the 06:42 Indian English male narration.
- [**Video Storyboard**](docs/video-storyboard.md): Shot-by-shot specification of the 15 synchronized scenes.
- [**Video Visual Audit**](docs/video-visual-audit.md): Verification notes demonstrating 1:1 narration-to-chart sync.
- [**Video Production Notes**](docs/video-production-notes.md): Bitrate, sample rate, codec, and container specifications.
- [**Repair & Diagnostic Report**](docs/repair-report.md): Engineering record of root causes and remediations applied.

---

## P. Limitations & Responsible Use

1. **Exploratory Observational Data:** The findings reflect correlation, not clinical causation. Elevated screen time may cause stress, or stressed students may engage in excessive digital screen consumption as an avoidance mechanism.
2. **Sample Size Scope:** The verified Tableau extract contains 200 student records. While sufficient for exploratory modeling, institution-wide policies should be corroborated with multi-campus longitudinal data.
3. **Self-Reported Survey Subjectivity:** Psychometric metrics (anxiety and depression scales) rely on self-reported questionnaires, which carry inherent subjective reporting bias.
4. **Data Privacy Protocol:** Raw student identifiers and sensitive emotional journal texts must never be made public. All public assets operate exclusively on anonymized aggregates.

---

## Q. Future Enhancements

- **Longitudinal Trend Tracking:** Expand the data pipeline to track student mental health indicators across multiple academic semesters to observe pre- and post-exam fluctuations.
- **Machine Learning Predictive Early-Warning:** Train supervised classification models (e.g., Random Forest or Gradient Boosting) to generate early-warning risk scores based on LMS activity and attendance drops.
- **Tableau JavaScript API Dynamic Interactivity:** Integrate two-way JavaScript API filtering between custom HTML controls and the embedded Tableau dashboard.
- **Multilingual Captions:** Generate Hindi and regional Indian language subtitle tracks for the video walkthrough.

---

## R. Credits & References

- **Project Author & Lead Analyst:** **Parth Pawar**
- **Internship Program:** SkillWallet / SmartBridge Virtual Internship (Data Analytics with Tableau)
- **Tableau Public Dashboard:** [Student Mental Health Analysis](https://public.tableau.com/views/Student_Mental_Health_Analysis_sufiyan_17913953791380/AnalysingMentalHealthinStudentEcosystem?:language=en-US&publish=yes)
- **Dataset Reference:** [Google Sheets Dataset Deliverable](https://docs.google.com/spreadsheets/d/1DSnFv7DdV8l1nBcQ-KNIrbgnmDMIDeh7/edit?usp=sharing)
- **Iconography:** [Lucide Icons](https://lucide.dev/)
- **Speech Synthesis:** Microsoft Edge Neural TTS (`edge-tts`)
- **Video Tools:** [FFmpeg](https://ffmpeg.org/)
