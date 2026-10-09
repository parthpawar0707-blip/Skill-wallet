# Video Narration Script: Analysing Mental Health in Student Ecosystem

**Project Title:** Analysing Mental Health in Student Ecosystem | Complete Tableau Project Walkthrough  
**Presenter:** Parth Pawar  
**Voice Engine:** Microsoft Edge Neural Speech Synthesizer (`edge-tts`)  
**Voice Model:** `en-IN-PrabhatNeural` (Natural Indian English Male)  
**Tuning:** `rate="+20%"`, `pitch="-5Hz"` (Acoustic warmth, relaxed sentence cadence, no high-pitch or female distortion)  
**Final Duration:** 375.05 Seconds (06:15.05 — exactly within the 5:45 to 6:30 target window)  
**Captions:** Synchronized SubRip (`.srt`) and WebVTT (`.vtt`) files available  

---

### Scene 1: Introduction & Welcome (00:00 – 00:23)
*Hello everyone! My name is Parth Pawar, and welcome to the project walkthrough of Analysing Mental Health in Student Ecosystem. In modern higher education, undergraduates navigate heavy academic pressures, irregular sleep, and prolonged screen exposure. Today, I'll walk you through our verified dataset, Tableau Public dashboard, and key analytical takeaways.*

---

### Scene 2: Problem Statement & Objectives (00:23 – 00:49)
*Collegiate mental health is often discussed subjectively or addressed only reactively after severe distress. Well-being is closely tied to daily lifestyle factors like screen time, sleep quality, and support systems. Our goal is to build an interactive Tableau decision-support dashboard that uncovers empirical patterns across student lifestyles, helping academic institutions offer proactive, timely support.*

---

### Scene 3: Dataset Architecture & Source (00:49 – 01:16)
*Our verified dataset contains exactly 200 student records across 18 multi-dimensional behavioral and academic variables. Each student is tracked from STU 0001 to STU 0200. Attributes include age, gender, clinical Anxiety and Depression scores from 0 to 100, categorical Stress Levels, daily screen time, sleep quality, and therapy pathways including CBT and Counseling.*

---

### Scene 4: Data Preparation & Calculations (01:16 – 01:40)
*Using Python and Pandas, we confirmed 100 percent data completeness with zero null values and zero duplicates. In Tableau Desktop, we engineered two vital calculated fields: First, Active Therapy, isolating students receiving structured care. Second, High Stress and Poor Sleep, flagging students suffering concurrently from acute stress and severe sleep disruption.*

---

### Scene 5: Executive KPI Ribbon (01:40 – 02:11)
*Transitioning to our live Tableau dashboard, the executive KPI ribbon establishes four cohort benchmarks across all 200 students: Total Students: exactly 200 undergraduates. Average Anxiety Score: 52.59 out of 100. Average Depression Score: 48.09 out of 100. And Average Daily Screen Time: 7.10 hours per day. These benchmarks ground our subsequent visual analysis.*

---

### Scene 6: Worksheet 1: Stress Level Distribution (02:11 – 02:39)
*Worksheet one examines the Stress Level Distribution across the cohort. 107 students, or 53.5 percent, experience Medium stress. 49 students, or 24.5 percent, experience High stress, while 44 students, or 22 percent, report Low stress. Combined, over 78 percent of surveyed students operate under moderate to severe stress, proving this is a widespread campus challenge.*

---

### Scene 7: Worksheet 2: Screen Time vs Stress Level (02:39 – 03:06)
*Worksheet two evaluates daily screen time against reported stress levels. A distinct upward trend emerges: students with Low stress average 6.00 hours of screen time. Medium stress students average 7.07 hours, while High stress students surge to 8.12 hours daily. High stress students spend over two additional hours on screens each day, highlighting digital fatigue.*

---

### Scene 8: Worksheet 3: Sleep Quality vs Stress Level (03:06 – 03:31)
*Worksheet three explores Sleep Quality against Stress Level. Among students reporting Poor sleep, 35 out of 66 suffer from High stress, 30 report Medium stress, and only one maintains Low stress. Conversely, among students with Good sleep quality, 22 report Low stress and only two report High stress. This confirms sleep quality as a vital resilience buffer.*

---

### Scene 9: Worksheet 4: Gender Mental Health Comparison (03:31 – 04:04)
*Worksheet four benchmarks anxiety and depression across gender cohorts. Average anxiety remains evenly distributed: 53.32 for females, 51.76 for males, and 53.50 for other cohorts. Depression scores follow a similar pattern: 48.10 for females, 47.88 for males, and 50.38 for others. This proves psychological strain is evenly shared across demographics, making lifestyle factors the key drivers.*

---

### Scene 10: Worksheets 5 & 6: Stress vs Anxiety and Depression (04:04 – 04:33)
*Worksheets five and six analyze how stress escalates into clinical symptoms. Anxiety scores rise steeply from 30.27 in Low stress, to 52.85 in Medium stress, reaching 72.06 in High stress. Similarly, depression scores escalate from 26.80 in Low stress to 68.78 in High stress, over two and a half times higher. Chronic stress reliably compounds into acute distress.*

---

### Scene 11: Worksheets 7 & 8: Therapy Efficacy and History Prevalence (04:33 – 05:01)
*Worksheets seven and eight evaluate support modalities and mental health history. In Ranked Therapy Efficacy, Cognitive Behavioral Therapy leads with an average progress score of 40.80, followed by Counseling at 34.43 and Support Groups at 33.10. Meanwhile, exactly 40 percent of students, or 80 out of 200, report prior mental health history, urging early proactive screening.*

---

### Scene 12: Core Empirical Findings & Interpretation (05:01 – 05:29)
*Synthesizing our observations yields three primary findings: First, Sleep Quality is the Paramount Protective Buffer against high stress. Second, Daily screen time exceeding 7.5 hours strongly co-occurs with elevated stress and anxiety. Third, Structured interventions like CBT deliver proven symptom progress compared to unguided coping. These signals provide actionable guidance for student welfare initiatives.*

---

### Scene 13: Portfolio Website & Public Deployment (05:29 – 05:51)
*To present this work professionally, I deployed a dedicated portfolio website on GitHub Pages featuring a modern editorial design. The site includes an Executive Hero section, an interactive Tableau embed with reload controls and fallback options, a complete Worksheet Gallery, an embedded HTML5 video player with captions, and direct links to our documentation.*

---

### Scene 14: Conclusion & Final Thoughts (05:51 – 06:15)
*In conclusion, Analysing Mental Health in Student Ecosystem demonstrates how Tableau transforms complex student wellness data into intuitive, actionable dashboards. All source datasets, data dictionaries, workbooks, and documentation are available on my GitHub repository. Thank you for watching! My name is Parth Pawar, and I look forward to your thoughts.*
