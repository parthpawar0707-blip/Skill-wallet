# Tableau Story Plan: 3 Narrative Scenes

A Tableau Story organizes your visualizations into a sequenced, interactive presentation with narrative text captions (story points). It guides professors, evaluators, and stakeholders through the analytical journey from cohort discovery to targeted intervention.

---

## How to Create a Story in Tableau (Quick Steps)
1. At the bottom edge of Tableau, click the **New Story** icon (the icon with an open book symbol).
2. A blank Story canvas opens with a top navigation bar and a left panel showing all your worksheets and dashboards.
3. In the left panel under **Story Size**, set size to **Automatic** or **1200 x 800**.
4. To add a scene, drag the specified sheets onto the center canvas.
5. In the gray box at the top of the scene, type the **Scene Title / Caption**.
6. To add the next scene, click the **Blank** button on the top left of the story toolbar.

---

## Scene 1: Overall Student Mental Health Landscape

* **Scene Title (Caption):** `Scene 1: Baseline Student Mental Health Landscape & Risk Distribution`
* **Sheets / Objects Added to Canvas:**
  * Top: `Viz 6 - KPI Overview Cards`
  * Bottom Left: `Viz 7 - Mental Risk Level Distribution`
  * Bottom Right: `Viz 4 - Average Stress Level by Gender`
* **What the Scene Shows:**
  An executive diagnostic snapshot of the 80 monitored students across university departments. It highlights key baseline indicators—average cohort stress of 4.95/10 and average sleep of 6.6 hours—alongside overall mental health risk stratification and gender comparisons.
* **Key Analytical Insights:**
  1. **Risk Tiers:** 15.0% of students (12 individuals) are classified as High Risk, while 48.75% (39 students) exhibit Moderate Risk symptoms.
  2. **Cohort Parity:** Reported stress levels remain relatively consistent across male, female, and non-binary students (ranging between 4.8 and 5.2/10), indicating that academic pressures affect the whole student body rather than isolated demographic silos.
  3. **Intervention Window:** The substantial moderate-risk group highlights an opportunity for campus wellness programs before academic burnouts occur.
* **What to Say in the Demo / Viva:**
  > *"Scene 1 sets the baseline context of our study. Through our KPI cards and risk distribution chart, we see that roughly 15% of our student population is currently operating under severe mental strain, with almost half showing early warning signs. This proves that mental health distress is not an isolated edge case, but an institutional reality requiring active campus-wide monitoring."*

---

## Scene 2: Lifestyle Habits, Screen Time & Physiological Strain

* **Scene Title (Caption):** `Scene 2: Lifestyle Imbalances & Autonomic Strain (HRV & Sleep)`
* **Sheets / Objects Added to Canvas:**
  * Left: `Viz 5 - Analyzing Heart Rate Variability`
  * Right: `Viz 1 - Impact of Study Hours on Performance` (or a dual view comparing Screen Time, Sleep, and Stress)
* **What the Scene Shows:**
  The biological and behavioral drivers of student fatigue. It connects daily lifestyle metrics (sleep deficiency and screen time overload) with biometric telemetry: Heart Rate Variability (HRV in milliseconds).
* **Key Analytical Insights:**
  1. **Physiological Biomarker Validation:** Students in the High Mental Health Risk category exhibit drastically suppressed Heart Rate Variability (averaging 37.2 ms vs 71.4 ms for low-risk peers), biologically confirming autonomic nervous system strain and chronic exhaustion.
  2. **Sleep Hygiene Deficit:** Students sleeping fewer than 5.5 hours per night report significantly elevated stress (>7.5/10) and heightened screen-time usage (>8 hrs/day).
  3. **Lifestyle Buffer:** Physical activity (even 1 to 2 hours per day) and adequate sleep correlate with elevated HRV resilience and reduced anxiety.
* **What to Say in the Demo / Viva:**
  > *"In Scene 2, we dive deeper into the lifestyle and biological causes of mental distress. A key highlight of our project is the inclusion of Heart Rate Variability (HRV). Low HRV below 45 milliseconds is a clinically proven indicator of chronic physiological stress. Our data demonstrates that sleep-deprived students with heavy screen time experience severe HRV drops, giving college wellness counselors concrete biometric data rather than relying only on subjective questionnaires."*

---

## Scene 3: Academic Performance Moderation & Intervention Strategy

* **Scene Title (Caption):** `Scene 3: Impact on Academic Efficacy & Targeted Intervention`
* **Sheets / Objects Added to Canvas:**
  * Top: `Viz 3 - Study Hours vs Academic Performance`
  * Bottom Left: `Viz 2 - Gender and Depression Level`
  * Bottom Right: `Viz 8 - Academic Performance Breakdown`
* **What the Scene Shows:**
  How psychological distress and study intensity directly moderate academic grades, classroom attendance, and overall academic achievement.
* **Key Analytical Insights:**
  1. **The Burnout Threshold:** While study hours correlate positively with performance up to 5.5–6 hours, students attempting 7+ hours while under high depression or stress suffer grade deterioration (the academic burnout effect).
  2. **Grade Breakdown Disparity:** Over 75% of students in the 'Low' academic performance category (<60%) belong to the High or Medium mental health risk categories and have attendance below 70%.
  3. **Support System Efficacy:** Students with strong support systems (counselors, peer groups, or family) maintain higher grade resilience even during high-stress exam periods.
* **What to Say in the Demo / Viva:**
  > *"In our final Scene, we connect mental health directly to academic outcomes. The scatter plot clearly shows that high study hours do NOT guarantee high grades if mental health is compromised. In fact, high-risk students experience diminishing returns and burnout. By identifying these students early through our Tableau dashboard, university administrators can provide timely academic accommodations and counseling interventions, preventing dropouts and improving student well-being."*
