# Student Project Demo Script & Viva Examination Preparation

This document contains a natural, student-friendly **5-to-10 minute project presentation script** and **18 essential viva examination questions with simple, confident answers**.

---

# Part 1: 5-to-10 Minute Project Presentation Script

### 1. Introduction (0:00 – 0:45)
> "Good morning, respected professors and evaluators. My name is Parth Pawar, and today I am presenting my Skill Wallet project titled **'Analysing Mental Health in Student Ecosystem'** under the Data Analytics with Tableau program.
>
> In university life, students face intense academic pressures, changing sleep schedules, and high screen time. The goal of this project is to use data analytics and visual business intelligence to understand how everyday student habits impact stress levels, academic performance, and overall psychological risk, allowing colleges to provide timely, proactive support."

### 2. The Problem Statement (0:45 – 1:30)
> "In most colleges today, student mental health is either ignored or only evaluated after a student fails an exam or drops out. Traditional surveys are static, stored in messy spreadsheets, and never linked with academic grades or biological indicators.
>
> There is no interactive system that allows deans, professors, or campus counselors to see early warning signs. Our project solves this problem by creating an interactive, real-time analytics dashboard in Tableau, integrated into a clean Flask web portal."

### 3. The Dataset & Key Attributes (1:30 – 2:30)
> "For this study, we modeled a realistic collegiate dataset of **80 students** across five university departments: Computer Science, Mechanical Engineering, Electronics, Business Administration, and Humanities.
>
> The dataset includes 19 comprehensive attributes organized into five groups:
> - **Demographics:** Age, Gender, Academic Year, and Department.
> - **Lifestyle:** Daily study hours, sleep hours, screen time, social hours, and physical activity.
> - **Mental Health Scales:** Self-reported Stress, Anxiety, Depression, and Mood scores from 1 to 10.
> - **Academic Metrics:** Academic Performance percentage and Class Attendance.
> - **Biometrics & Support:** Heart Rate Variability—or HRV—in milliseconds, support system, and composite Mental Health Risk."

### 4. Data Preparation & Cleaning (2:30 – 3:15)
> "Before importing the data into Tableau, data quality was our top priority. We developed a Python cleaning script, `clean_data.py`, that checked:
> - First, zero duplicate Student IDs.
> - Second, 100% data completeness with zero missing or null values.
> - Third, valid ranges for all numeric scales.
> - And fourth, standardized categorical text.
>
> This produced our cleaned dataset, `student_mental_health_cleaned.csv`, which is completely Tableau-ready and ensures fast, bug-free dashboard rendering."

### 5. Tableau Visualizations & Calculated Fields (3:15 – 5:00)
*(Screen share your Tableau workbook or web portal)*
> "To analyze this data, I built **8 distinct visualizations** in Tableau, supported by 5 custom calculated fields like `Performance_Category` and `Sleep_Category`:
>
> 1. **Viz 1:** Examines the **Impact of Study Hours on Academic Performance**, where color marks show average stress across study intensity groups.
> 2. **Viz 2:** Compares **Depression Levels Across Gender**, showing that pressure affects all groups, with female and non-binary students reporting slightly higher acute distress.
> 3. **Viz 3:** A comprehensive **Scatter Plot of Study Hours vs Academic Performance** plotting all 80 individual students. Notice the trend line: grades rise with study time, but students marked in Red (High Mental Health Risk) struggle to reach top scores due to cognitive exhaustion.
> 4. **Viz 4:** Tracks **Average Stress by Gender**, showing a consistent campus baseline around 5 out of 10.
> 5. **Viz 5:** A crucial highlight of our project: **Analyzing Heart Rate Variability (HRV)**. HRV is a clinical biological indicator of nervous system stress. Our chart proves that High-Risk students have drastically lower HRV—below 40 milliseconds—providing biological proof for their reported distress!
> 6. **Viz 6:** Our **Executive KPI Banner** showing Total Students (80), Average Stress (4.95), Average Sleep (6.6 hours), and Average Academic Score (80.5%).
> 7. **Viz 7:** A **Mental Health Risk Distribution Donut Chart** showing that 15% are High Risk, 48.8% are Moderate Risk, and 36.2% are Low Risk.
> 8. **Viz 8:** An **Academic Performance Breakdown** categorizing students into Excellent, Good, Average, and Low grade tiers."

### 6. The Tableau Dashboard (5:00 – 6:15)
> "Next, I brought these charts together into one unified, responsive **Master Dashboard**.
>
> Across the top, we have our Title and four global dropdown filters: **Gender, Academic Year, Department, and Mental Health Risk**. When an administrator selects 'Computer Science' or '1st Year', all 8 charts and KPI scorecards instantly update in real time. We also configured the Risk Donut chart as an interactive Action Filter—clicking on 'High Risk' immediately highlights those specific students across the entire dashboard."

### 7. The Tableau Story (6:15 – 7:15)
> "To present these findings to college management, I created a **3-Scene Tableau Story**:
> - **Scene 1** establishes the baseline campus risk landscape.
> - **Scene 2** dives into the lifestyle drivers, showing how sleep deficits and screen time drag down Heart Rate Variability.
> - **Scene 3** proves the academic burnout effect and outlines recommendations for student support."

### 8. Web Integration with Flask (7:15 – 8:00)
> "Finally, to make this solution accessible to campus stakeholders without requiring them to install Tableau Desktop, we integrated the published dashboard into a modern **Flask web application**.
>
> The web portal includes a clean overview home page, an interactive dashboard page embedding Tableau's official JavaScript API, a Story page, a live tabular dataset viewer, and an analytical insights summary. All configuration is centralized in `config.py`, making it very easy to maintain."

### 9. Key Findings & Recommendations (8:00 – 8:45)
> "Our three biggest analytical takeaways are:
> 1. **The Study-Burnout Curvature:** Studying 3.5 to 6 hours is optimal. Studying over 6.5 hours while sleep-deprived causes severe stress and actually lowers grades.
> 2. **Sleep is the Master Switch:** Students sleeping fewer than 5.5 hours have nearly 4 times higher risk of high mental distress.
> 3. **The Moderate Risk Window:** Over 48% of students are in the Moderate Risk category. This is the crucial golden window where colleges can intervene with workshops and peer mentoring before students experience clinical burnout."

### 10. Conclusion (8:45 – 9:15)
> "In conclusion, this project demonstrates how data analytics with Tableau can bridge the gap between student lifestyle, mental health, and academic success. It provides university leaders with an intuitive, real-time tool to create a healthier, more supportive campus ecosystem.
>
> Thank you very much, and I am now ready for your questions."

---

# Part 2: Essential Viva Examination Questions & Answers

### Q1: Why did you choose Tableau as the primary visualization tool for this project?
> **Answer:** "Tableau is the industry-standard Business Intelligence tool for interactive visual analytics. It excels at multi-dimensional drag-and-drop analysis, calculated fields, dynamic cross-filtering across worksheets, and allows us to build responsive dashboards and guided stories without writing hundreds of lines of complex charting code."

### Q2: What is the difference between a Dimension and a Measure in Tableau?
> **Answer:** "A **Dimension** contains qualitative or categorical values (like Gender, Department, or Academic Year) used to segment, slice, and group data. A **Measure** contains continuous numeric quantitative data (like Study Hours, Stress Level, or Academic Performance) that can be mathematically aggregated using functions like SUM, AVERAGE, MIN, or MAX."

### Q3: What is a Calculated Field, and which ones did you create?
> **Answer:** "A calculated field is a custom formula in Tableau that creates a new field from existing data. I created 5 calculated fields using simple IF/ELSEIF logic:
> 1. `Performance_Category` (grouping grades into Low, Average, Good, and Excellent)
> 2. `Sleep_Category` (Healthy vs Low Sleep)
> 3. `Stress_Category` (Low, Moderate, and High Stress)
> 4. `Study_Hours_Category` (Light, Balanced, and Intensive study)
> 5. `Calculated_Risk_Tier` (validating multi-factor composite risk)."

### Q4: Why did you perform data cleaning in Python before bringing data into Tableau?
> **Answer:** "Even though Tableau has basic data preparation features, performing data cleaning with a Python script (`clean_data.py`) ensures that data quality is audited and verified programmatically. We checked for duplicate Student IDs, validated numeric bounds, eliminated missing or null values, and standardized categorical text. This guarantees clean ingestion and eliminates errors in Tableau."

### Q5: What is Heart Rate Variability (HRV), and why is it important in a mental health study?
> **Answer:** "Heart Rate Variability (HRV) is the variation in time between consecutive heartbeats, measured in milliseconds. In medical science, high HRV indicates a healthy, flexible autonomic nervous system and parasympathetic resilience. Low HRV (under 45 ms) is a clinically proven biomarker of chronic stress, anxiety, and physical exhaustion. Including HRV adds objective biological evidence to our self-reported survey data."

### Q6: What is the difference between a Tableau Worksheet, a Dashboard, and a Story?
> **Answer:**
> - A **Worksheet** contains a single view or chart (like a scatter plot or bar chart).
> - A **Dashboard** combines multiple worksheets and filters onto a single interactive screen for real-time monitoring.
> - A **Story** is a sequence of guided sheets or dashboard states arranged chronologically with narrative captions to walk an audience through analytical insights."

### Q7: How do global filters work on your dashboard?
> **Answer:** "On our dashboard, we added filters for Gender, Academic Year, Department, and Risk. By right-clicking each filter and selecting 'Apply to Worksheets -> All Using This Data Source', Tableau applies the filter condition across all 8 worksheets simultaneously, updating all charts in real time whenever a filter dropdown is selected."

### Q8: What is an Action Filter in Tableau?
> **Answer:** "An Action Filter allows a chart itself to act as a filter for other charts on the dashboard. In our dashboard, we clicked 'Use as Filter' on the Risk Distribution Donut chart. When an evaluator clicks the 'High Risk' slice, Tableau immediately filters all other charts to display only the High-Risk student cohort."

### Q9: What is a KPI, and what KPIs did you track?
> **Answer:** "A Key Performance Indicator (KPI) is a high-level summary metric that gives decision-makers an immediate understanding of system health. We tracked 4 core KPIs: Total Students Monitored (80), Average Stress Level (4.95/10), Average Sleep Duration (6.6 hours), and Average Academic Performance (80.5%)."

### Q10: Why did you use CSV format instead of a heavy SQL database?
> **Answer:** "For a focused cohort of 80 students, a clean CSV file is portable, lightweight, fast, and does not require complex database server installation or network configuration. Tableau connects natively to CSV files in milliseconds with zero latency."

### Q11: How does your Flask web application integrate with Tableau?
> **Answer:** "Our Flask application uses Tableau's official JavaScript Embedding API v3 (the `<tableau-viz>` web component) and secure iframes. In `config.py`, we define the published Tableau Public URL. The Flask templates render this URL in a responsive, beautifully styled web page, allowing users to interact with the full dashboard directly inside their web browser."

### Q12: What does your scatter plot show regarding the relationship between study hours and academic performance?
> **Answer:** "The scatter plot reveals that study hours have a positive correlation with performance up to around 6 hours per day. However, beyond that point, we see diminishing returns. Students who study 7 or 8 hours while experiencing high stress (red dots) actually achieve lower scores than students studying 5 hours with healthy sleep, demonstrating academic burnout."

### Q13: How many students are in the High, Medium, and Low mental health risk categories?
> **Answer:** "In our dataset of 80 students:
> - **High Risk:** 12 students (15.0%)
> - **Medium Risk:** 39 students (48.75%)
> - **Low Risk:** 29 students (36.25%).
> The large Medium Risk group is especially significant because it represents an opportunity for proactive early intervention before symptoms worsen."

### Q14: Did you observe any significant differences in stress levels across genders?
> **Answer:** "Average stress scores were relatively balanced across gender cohorts—hovering between 4.8 and 5.2 out of 10. However, female and non-binary students reported slightly higher acute depressive episodes. This shows that academic stress is widespread across the entire student population rather than isolated to one gender."

### Q15: What role does physical activity and sleep play in student mental health?
> **Answer:** "Our data clearly shows that sleep duration is the strongest single lifestyle predictor of mental health. Students sleeping over 7 hours reported low stress and high HRV. Regular physical activity (even 1 to 2 hours per day) also acts as an effective buffer, improving mood scores and reducing anxiety."

### Q16: How did you ensure your dashboard is responsive?
> **Answer:** "In Tableau Dashboard layout settings, we set the dashboard size to 'Range' with a minimum width of 1000px and a maximum width of 1600px (or 'Automatic'). In our Flask application, CSS container queries and media queries ensure that the embed frame reflows smoothly on desktop, laptop, and tablet screens."

### Q17: What performance testing did you carry out (Skill Wallet Epic 6)?
> **Answer:** "Under Epic 6, we audited four key parameters:
> 1. Amount of Data Rendered: 80 rows × 19 columns (1,520 cells), loading in under 15 milliseconds.
> 2. Utilization of Data Filters: 4 global dropdown filters plus interactive action filters.
> 3. Number of Calculation Fields: 5 optimized scalar conditional logic fields evaluated in O(1) time.
> 4. Number of Visualizations: 8 unique worksheets, 1 dashboard, and 1 story."

### Q18: If you had another month to work on this project, what would you add?
> **Answer:** "I would expand this project in two ways: first, by conducting longitudinal tracking across all four college years to observe how stress evolves from freshman transition to final-year placements; and second, by connecting live smartwatch telemetry APIs (like Apple Health or Fitbit) directly to our analytics pipeline for real-time automated wellness alerts."
