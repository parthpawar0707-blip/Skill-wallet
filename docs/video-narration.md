# Video Narration Script: Analysing Mental Health in Student Ecosystem

**Video Title:** Analysing Mental Health in Student Ecosystem | Complete Tableau Project Walkthrough  
**Presenter:** Parth Pawar  
**Language & Accent:** Natural Indian English (`en-IN-PrabhatNeural`)  
**Target Duration:** ~5:30 to 6:00 Minutes  
**Target Speed:** ~145 Words per minute with natural pauses and cadence  

---

## Chapter 1: Introduction (00:00 – 00:40)

Hello everyone! My name is Parth Pawar, and welcome to this complete project walkthrough of my data analytics and business intelligence project titled **"Analysing Mental Health in Student Ecosystem"**.

In higher education today, students face a demanding mix of academic expectations, irregular sleep schedules, high screen exposure, and social adjustments. In this walkthrough, I will take you end-to-end through our verified dataset, our data preparation workflow, our interactive Tableau Public dashboard, and the analytical takeaways that emerge from the data.

Whether you are an academic advisor, an institutional counselor, or a data analytics evaluator, this demonstration shows how empirical business intelligence can transform student support from reactive crisis management into proactive, evidence-based care. Let us dive in!

---

## Chapter 2: Problem Statement (00:40 – 01:25)

Let us examine why this problem matters. Collegiate mental health is often discussed using subjective anecdotes or surveyed only after a student faces severe academic distress.

However, student well-being does not deteriorate in isolation. It is intricately connected to daily lifestyle patterns—such as how many hours a student spends on digital screens, whether they get restorative sleep, their level of physical exercise, and whether they have access to an active support system.

The core objective of this project is to build an analytical framework in Tableau that brings together lifestyle telemetry, behavioral indicators, and standardized psychological scores. By mapping these dimensions together, our goal is not to produce automated clinical diagnoses, but to empower academic mentors and counseling departments with clear, verifiable signals to identify at-risk cohorts early and tailor non-invasive support programs.

---

## Chapter 3: Dataset Architecture & Source (01:25 – 02:15)

Now, let us inspect the foundational dataset that powers our analysis.

Our verified dataset is structured from collegiate wellness records, comprising exactly 200 student profiles spanning 18 multi-dimensional behavioral, clinical, and academic attributes.

Every student record is tracked under a unique identifier from `STU_0001` through `STU_0200`. The demographic fields capture chronological age, ranging from 18 to 25 years, along with gender classifications across male, female, and other student cohorts.

On the psychological and clinical side, the schema includes standardized Anxiety Scores and Depression Scores measured on continuous 0 to 100 rating scales, alongside a tri-tier categorical Stress Level categorized as Low, Medium, or High.

On the daily habits side, we track daily screen time in hours, sleep quality categorized as Poor, Average, or Good, physical activity levels, and social interaction scores.

Finally, the dataset tracks intervention pathways—such as Cognitive Behavioral Therapy, Counseling, Support Groups, and Meditation—along with intervention durations and measurable progress scores.

---

## Chapter 4: Data Preparation & Calculation Engineering (02:15 – 03:00)

Before importing the dataset into Tableau Desktop, rigorous data hygiene and preparation procedures were executed in Python using Pandas.

First, we verified data completeness: all 200 rows were checked for missing or null values across all 18 columns, confirming a 100% complete dataset. We also verified that there were zero duplicate student records.

Second, correct data types were enforced. Numerical metrics such as daily screen time and progress scores were validated as continuous numeric types, while ordinal attributes like sleep quality and categorical fields like therapy types were structured as discrete dimensions.

Within Tableau, we engineered two vital calculated fields:

First, `Active_Therapy`, written as:
`IF [Therapy Type] != "No Therapy" THEN 1 ELSE 0 END`.
This creates a binary measure allowing instant cohort filtering between students receiving structured care versus those unassisted.

Second, `HighStress_PoorSleep`, written as:
`IF [Stress Level] = "High" AND [Sleep Quality] = "Poor" THEN 1 ELSE 0 END`.
This flags students facing the compound physiological risk of acute stress combined with severe sleep deprivation.

---

## Chapter 5: Live Tableau Dashboard Walkthrough (03:00 – 04:35)

Now, let us examine the main centerpiece of this project: our live Tableau Public dashboard, titled **"Analysing Mental Health in Student Ecosystem"**.

At the very top, our executive KPI ribbon presents four macro benchmarks computed across all 200 students:
- Total Cohort Size: Exactly 200 students.
- Average Anxiety Score: 52.59 out of 100.
- Average Depression Score: 48.09 out of 100.
- Average Daily Screen Time: 7.10 hours per day.

Moving directly into our visualizations:

First, on the left, we have the **Stress Level Distribution**. This chart reveals that 107 students—over 53.5% of the entire cohort—fall into Medium Stress, while 49 students, or 24.5%, experience High Stress. Only 44 students report Low Stress. Combined, more than 78% of students experience moderate-to-severe stress.

Second, looking at **Screen Time versus Stress Level**, we observe a clear upward trend. Students reporting Low Stress average 6.00 hours of screen time daily. Medium-stress students average 7.07 hours, while High-stress students surge to 8.12 hours per day.

Third, the **Sleep Quality versus Stress Level** matrix provides one of our most striking insights. Among students with Poor sleep quality, 35 out of 66 suffer from High stress, and 30 suffer from Medium stress—only 1 student with poor sleep had low stress! In stark contrast, out of students who enjoy Good sleep quality, only 2 experienced high stress, while 22 enjoyed low stress.

Fourth, looking at the **Gender Mental Health Comparison**, we see that average anxiety scores remain remarkably tight: 53.32 for females, 51.76 for males, and 53.50 for other cohorts. Depression scores follow a similar pattern: 48.10 for females, 47.88 for males, and 50.38 for other cohorts. This confirms that mental health challenges are widespread across all gender groups.

Fifth and sixth, in our **Stress Level versus Anxiety Score** and **Stress Level versus Depression Score** charts, we observe strong positive progression. Students in the Low Stress tier average an anxiety score of 30.27 and depression score of 26.80. In the High Stress tier, these scores jump to 72.06 for anxiety and 68.78 for depression—more than double the low-stress baseline.

Finally, in our **Ranked Therapy Efficacy** chart, we compare therapeutic progress. Cognitive Behavioral Therapy leads the ranking with an average progress score of 40.80, followed by Professional Counseling at 34.43, Support Groups at 33.10, and Meditation at 32.57. Students with No Therapy record zero progress.

Additionally, our **Mental Health History Prevalence** breakdown highlights that exactly 40% of students—80 out of 200—report prior personal or family mental health history.

---

## Chapter 6: Empirical Findings & Interpretation (04:35 – 05:15)

Synthesizing these visualizations yields three critical conclusions:

First, **Sleep Quality is the Primary Resilience Buffer**. The data indicates that sleep quality is the strongest inverse correlate of high stress. Restorative sleep directly buffers against psychological exhaustion.

Second, **The Digital Fatigue Threshold**. Daily screen time beyond 7.5 hours strongly co-occurs with elevated anxiety and high stress scores, highlighting digital boundary management as a key campus health intervention.

Third, **Structured Therapies Deliver Measurable Progress**. Among available modalities, Cognitive Behavioral Therapy produces the highest measurable progress, outperforming unguided coping.

We must carefully note that these findings represent statistical associations and descriptive observations rather than direct clinical causation. However, as an institutional decision-support system, these empirical signals provide actionable guidance.

---

## Chapter 7: Portfolio Website Demonstration (05:15 – 05:45)

To present this project to stakeholders, evaluators, and recruiters, I built and deployed a dedicated analytics portfolio website hosted on GitHub Pages.

The website features an editorial, high-contrast design system with fluid typography, responsive layout, and structured documentation:
- An Executive Hero section with quick links to the live Tableau Public dashboard, video demo, and GitHub repository.
- A live, responsive Tableau embed with interactive reload controls and an automatic fallback card.
- A detailed Visualization Gallery showcasing each worksheet with its chart type and key findings.
- An embedded HTML5 video player with subtitle support and direct MP4 download capability.
- Full documentation links to our project report, verification logs, and source code.

---

## Chapter 8: Conclusion & Acknowledgments (05:45 – 06:10)

In conclusion, **"Analysing Mental Health in Student Ecosystem"** demonstrates how business intelligence tools like Tableau can transform complex health and lifestyle telemetry into intuitive, actionable institutional dashboards.

By bridging empirical data with proactive student wellness strategies, academic institutions can build supportive environments where students thrive both academically and personally.

All source code, data dictionaries, validation pipelines, and reports are openly available on my GitHub repository.

Thank you very much for watching! My name is Parth Pawar, and I look forward to your valuable feedback.
