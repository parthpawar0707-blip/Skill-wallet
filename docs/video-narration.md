# Video Narration Script: Analysing Mental Health in Student Ecosystem

**Project Title:** Analysing Mental Health in Student Ecosystem | Complete Tableau Project Walkthrough  
**Presenter:** Parth Pawar  
**Voice Engine:** Microsoft Edge Neural Speech Synthesizer (`edge-tts`)  
**Voice Model:** `en-IN-PrabhatNeural` (Natural Indian English Male)  
**Tuning:** `rate="+22%"`, `pitch="-5Hz"` (Acoustic warmth, relaxed collegiate cadence, zero high-pitch distortion)  
**Final Duration:** 401.97 Seconds (06:41.97 — strictly within the 5:00 to 7:00 minute requirement)  
**Captions:** Synchronized SubRip (`.srt`) and WebVTT (`.vtt`) files generated  

---

### Chapter 1: Introduction & Welcome (00:00 – 00:25)
*Hello everyone! My name is Parth Pawar, and welcome to this complete walkthrough of Analysing Mental Health in Student Ecosystem. Today, undergraduates navigate heavy academic pressures, irregular sleep schedules, and prolonged screen exposure. In this walkthrough, I will guide you through our verified dataset, our interactive Tableau Public dashboard, and the empirical takeaways that emerge from the data.*

---

### Chapter 2: Problem Statement & Objectives (00:25 – 00:51)
*Collegiate mental health is frequently addressed only reactively after severe distress. However, well-being is intricately connected to daily lifestyle patterns like screen time, sleep quality, and support systems. Our objective is building an interactive Tableau decision-support dashboard that reveals empirical patterns across student lifestyles and clinical scores, empowering mentors and counselors to offer timely, proactive support.*

---

### Chapter 3: Dataset Architecture & Source (00:51 – 01:24)
*Our verified dataset contains exactly 200 student records across 18 multi-dimensional behavioral, clinical, and academic variables, tracked from STU 0001 to STU 0200. Demographics capture age 18 to 25 and gender cohorts. Clinical scales measure Anxiety and Depression from 0 to 100, alongside categorical Stress Levels. Lifestyle telemetry tracks daily screen time in hours, sleep quality, physical activity, and therapeutic pathways like CBT and Counseling.*

---

### Chapter 4: Methodology & Calculations (01:24 – 01:51)
*Using Python and Pandas, we verified zero null values and zero duplicates across all records. In Tableau Desktop, we engineered two vital calculated fields: First, Active Therapy, defined as: IF Therapy Type does not equal No Therapy THEN 1 ELSE 0 END, isolating students in institutional care. Second, High Stress and Poor Sleep, flagging students suffering concurrently from acute stress and severe sleep disruption.*

---

### Chapter 5A: Tableau Walkthrough: Executive KPI Ribbon (01:51 – 02:20)
*On our live Tableau Public dashboard, the executive KPI ribbon establishes four cohort benchmarks across all 200 students: Total Students: exactly 200 undergraduates. Average Anxiety Score: 52.59 out of 100. Average Depression Score: 48.09 out of 100. And Average Daily Screen Time: 7.10 hours per day. These metrics ground our entire visual analysis.*

---

### Chapter 5B: Tableau Walkthrough: Stress Level Distribution (02:20 – 02:49)
*Worksheet one examines Stress Level Distribution across the cohort. 107 students, or 53.5 percent, experience Medium stress. 49 students, or 24.5 percent, experience High stress, while 44 students, or 22 percent, report Low stress. Combined, over 78 percent of surveyed students operate under moderate to severe stress, proving this is a widespread campus challenge.*

---

### Chapter 5C: Tableau Walkthrough: Screen Time vs Stress (02:49 – 03:15)
*Worksheet two evaluates daily screen time against reported stress levels. A distinct upward trend emerges: students with Low stress average 6.00 hours of screen time. Medium stress students average 7.07 hours, while High stress students surge to 8.12 hours daily. High-stress students spend over two additional hours on screens each day, highlighting digital fatigue.*

---

### Chapter 5D: Tableau Walkthrough: Sleep Quality vs Stress (03:15 – 03:39)
*Worksheet three explores Sleep Quality against Stress Level. Among students reporting Poor sleep, 35 out of 66 suffer from High stress, 30 report Medium stress, and only one maintains Low stress. Conversely, among students with Good sleep, 22 report Low stress and only two report High stress. This confirms sleep quality as a vital resilience buffer.*

---

### Chapter 5E: Tableau Walkthrough: Gender Mental Health Comparison (03:39 – 04:12)
*Worksheet four benchmarks mental health across gender cohorts. Average anxiety remains evenly distributed: 53.32 for females, 51.76 for males, and 53.50 for other cohorts. Depression scores follow a similar pattern: 48.10 for females, 47.88 for males, and 50.38 for others. This statistical parity shows psychological strain is evenly shared across demographics, making lifestyle factors the primary differentiators.*

---

### Chapter 5F: Tableau Walkthrough: Stress vs Symptoms Escalation (04:12 – 04:41)
*Worksheets five and six analyze how stress escalates into clinical symptoms. Anxiety scores rise steeply from 30.27 in Low stress, to 52.85 in Medium stress, reaching 72.06 in High stress. Similarly, depression scores escalate from 26.80 in Low stress to 68.78 in High stress—over two and a half times higher. Chronic stress reliably compounds into acute distress.*

---

### Chapter 5G: Tableau Walkthrough: Therapy Efficacy & History Prevalence (04:41 – 05:08)
*Worksheets seven and eight evaluate support modalities and history. In Ranked Therapy Efficacy, Cognitive Behavioral Therapy leads with an average progress score of 40.80, followed by Counseling at 34.43 and Support Groups at 33.10. Meanwhile, exactly 40 percent of students, or 80 out of 200, report prior mental health history, underscoring the need for early screening.*

---

### Chapter 5H: Tableau Walkthrough: Interactive Cross-Filtering (05:08 – 05:26)
*On the published Tableau dashboard, interactive cross-filtering allows advisors to segment the cohort by stress level or sleep quality. Clicking a high-stress tier dynamically updates all connected worksheets, isolating vulnerable students and enabling targeted intervention planning in real time.*

---

### Chapter 6: Core Empirical Findings & Interpretation (05:26 – 05:56)
*Synthesizing our observations yields three primary findings: First, Sleep Quality is the Paramount Protective Buffer against high stress—restorative sleep strongly shields students from distress. Second, daily screen time exceeding 7.5 hours strongly co-occurs with elevated anxiety and burnout. Third, structured interventions like CBT deliver proven symptom progress compared to unguided coping. These empirical signals offer actionable guidance for campus welfare initiatives.*

---

### Chapter 7: Portfolio Website & Public Deployment (05:56 – 06:19)
*To present this work professionally, I deployed a dedicated portfolio website on GitHub Pages featuring a modern editorial design. The site includes an Executive Hero section, an interactive Tableau embed with reload controls and fallback options, a Worksheet Gallery, an embedded HTML5 video player with captions, and direct links to our documentation and repository.*

---

### Chapter 8: Conclusion & Final Thoughts (06:19 – 06:42)
*In conclusion, Analysing Mental Health in Student Ecosystem demonstrates how Tableau transforms complex student wellness data into intuitive, actionable dashboards. All source datasets, data dictionaries, workbooks, and documentation are available on my GitHub repository. Thank you for watching! My name is Parth Pawar, and I look forward to your thoughts.*
