# Video & Visual Synchronization Audit

**Project Title:** Analysing Mental Health in Student Ecosystem  
**Author & Presenter:** Parth Pawar  
**Date of Audit:** 2026-10-09  
**Audited Media Asset:** `site/assets/video/student-mental-health-demo.mp4` (Previous Build)  
**Target Window:** 5:00 to 7:00 minutes (Target: ~6:00 to 6:20)  

---

## 1. Executive Summary of Audit

A rigorous review of the previously rendered video walkthrough revealed significant visual-audio synchronization discrepancies. While the spoken narration discussed specific data dimensions, clinical indicators, and dashboard components, the on-screen visuals did not always maintain tight, shot-by-shot correspondence. 

This audit documents each discovered mismatch to establish the corrective requirements for the rebuilt video timeline.

---

## 2. Identified Visual-Audio Discrepancies

| Scene / Timestamp | Spoken Narration Topic | Visual Displayed in Previous Video | Discrepancy & Root Cause | Required Correction in Rebuilt Timeline |
| :--- | :--- | :--- | :--- | :--- |
| **Scene 01** (00:00 – 00:23) | Introduction of project by Parth Pawar, higher education context, and overview of Tableau BI analysis. | Static dark title slide with metadata box. | Visual lacked direct reference to the actual live website or Tableau interface being introduced. | Transition smoothly from clean title card to live view of the actual portfolio website and Tableau header. |
| **Scene 02** (00:23 – 00:49) | Academic pressures, digital screen fatigue, erratic sleep, and proactive decision support. | Generic 3-card slide. | Text was static and dense; did not visually highlight the key lifestyle factors (screen time, sleep, support) as spoken. | Streamline problem cards into clear, scannable pillars with distinct iconography and highlighted focus areas. |
| **Scene 03** (00:49 – 01:16) | 200 student records (`STU_0001`–`STU_0200`), 18 variables, standardized Anxiety/Depression scales. | Static two-column text table. | Visual was static text; did not dynamically emphasize the specific variable categories (clinical, telemetry, therapy) as named. | Highlight each variable group (identifiers, clinical scores, lifestyle telemetry, therapy types) in sync with spoken words. |
| **Scene 04** (01:16 – 01:40) | Data hygiene validation and Tableau calculated fields: `Active_Therapy` and `HighStress_PoorSleep`. | Static slide with two formula boxes. | Formulas remained static without visual breakdown of why each calculation was engineered. | Display clean formula code blocks with step-by-step logic badges and direct annotations explaining their analytic utility. |
| **Scene 05** (01:40 – 02:11) | Executive KPI Ribbon: 200 Students, 52.59 Anxiety, 48.09 Depression, 7.10 hrs Screen Time. | KPI cards placed above a scaled-down static dashboard capture. | The embedded Tableau screenshot was too small to read individual chart labels, creating visual crowding. | Dedicate full visual prominence to the KPI ribbon with large tabular figures, followed by a clear, high-resolution view of the Tableau workbook. |
| **Scenes 06–11** (02:11 – 05:01) | Individual Tableau Worksheets (Stress Distribution, Screen Time, Sleep Quality, Gender, Clinical Symptoms, Therapy Efficacy, History). | Isolated matplotlib plots displayed one by one. | While the numbers matched ground truth, the presentation looked like separate charts rather than a cohesive walkthrough of the real Tableau BI workbook. | Anchor every chart explanation in its actual Tableau workbook context with readable title bars, clear axis labels, and visible cohort metrics. |
| **Scene 12** (05:01 – 05:29) | Core empirical findings (Sleep buffer, 7.5+ hr digital threshold, CBT progress) and correlation vs. causation. | Static bullet points. | Bullet points did not visually link back to the supporting chart evidence discussed. | Pair each empirical finding with callout highlights and the corresponding chart proof points from the workbook. |
| **Scene 13** (05:29 – 05:51) | Live portfolio website walkthrough: Hero section, interactive Tableau embed, gallery, video player, and documentation. | Split screen with a single static thumbnail of the hero and a text checklist. | The video only showed the hero thumbnail while the narrator described the embedded dashboard, gallery, and video player. | Walk sequentially through the actual sections of the live website: Hero &rarr; Tableau Embed &rarr; Gallery &rarr; Video Player &rarr; Documentation. |
| **Scene 14** (05:51 – 06:15) | Conclusion, student wellness implications, limitations, GitHub repository, and sign-off. | Dark closing slide with repository URL. | Displayed static text without showing the real repository or clear author credits. | Present a clean, professional closing frame with verified repository links, author branding, and presentation sign-off. |

---

## 3. Corrective Architecture for Rebuilt Video

1. **8-Chapter Sequential Narrative:** Align video chapters strictly to the master plan:
   - Chapter 1: Introduction (~25s)
   - Chapter 2: Problem Statement (~35s)
   - Chapter 3: Dataset Architecture & Source (~40s)
   - Chapter 4: Methodology & Calculation Engineering (~40s)
   - Chapter 5: Genuine Tableau Dashboard Walkthrough (~120s / 2 mins)
   - Chapter 6: Evidence-Supported Analytical Findings (~50s)
   - Chapter 7: Portfolio Website Demonstration (~45s)
   - Chapter 8: Conclusion & Professional Sign-off (~25s)
2. **Shot-by-Shot Visual Alignment:** Ensure on-screen visuals change in lockstep with the narrator's specific points.
3. **Chart Title & Label Legibility:** Standardize all chart views to 1280&times;720 HD with bold headings and readable values.
4. **Authentic Screen Captures:** Integrate real browser captures of the live website and Tableau Public workbook.
5. **Synchronized Subtitles:** Recalculate SubRip (`.srt`) and WebVTT (`.vtt`) timecodes to match the new timeline to the millisecond.
