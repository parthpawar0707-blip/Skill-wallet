"""
generate_narration.py
---------------------
Generates natural Indian English audio narration using edge-tts (en-IN-PrabhatNeural).
Creates narration.mp3 and reports duration.
"""

import asyncio
import edge_tts
import os

SCRIPT_TEXT = """
Hello everyone, and welcome. My name is Parth Pawar, and today I am excited to present my data analytics project: Analysing Mental Health in the Student Ecosystem. 

As higher education continues to demand intense academic dedication, understanding student well-being, everyday lifestyle habits, and autonomic biological stress has never been more critical. In this demonstration, I will walk you through the end-to-end analytical workflow, from dataset verification and data quality auditing to interactive Tableau dashboard engineering and key empirical insights.

In contemporary universities, mental health challenges such as chronic stress, anxiety, and depressive symptoms frequently go unnoticed until a student experiences acute academic burnout or severe absenteeism. Academic advisors and counseling centers often lack real-time, unified diagnostic visibility into how sleep disruption, screen time, and study habits directly impact student wellness. The core objective of this project is to build an interactive, data-driven business intelligence platform that bridges behavioral metrics, physiological telemetry, and academic performance, enabling proactive student support.

Our analysis is powered by a verified dataset comprising exactly 1,000 collegiate profiles across 16 multi-dimensional variables. These variables span six core domains: demographics such as age and gender; psychological ratings covering stress, anxiety, and depression on standardized 1 to 10 scales; daily lifestyle metrics including sleep duration and study hours; academic telemetry such as class attendance and learning management system activity; physiological telemetry via Heart Rate Variability; and finally, risk classifications and personalized intervention strategies. We conducted rigorous data validation, confirming 100% data completeness with zero missing values and zero duplicate records across all 1,000 student identifiers.

To prepare this dataset for Tableau, we followed a structured ten-step methodology. In Python, we validated range boundaries and data types. Inside Tableau, we engineered custom calculated fields to enable intuitive visual slicing. For example, we categorized chronological age into three distinct cohorts: below 20 years, 20 to 22 years, and 23 to 25 years. We also classified study intensity into light, moderate, and intensive study tiers. These calculated dimensions allow administrators to isolate specific cohorts and observe non-linear relationships across grades and stress levels.

Now, let us examine the published interactive Tableau dashboard. The dashboard is structured into an executive KPI scorecard and six core analytical views. At the top, our KPI scorecards summarize the cohort: an average stress score of 5.45, an average depression score of 5.50, and an average nightly sleep duration of 6.49 hours. 

Looking at our first visualization, Study Hours versus Academic Performance, we observe that moderate study between 3 and 5.5 hours delivers optimal academic scores without triggering severe anxiety. In our scatter plot with linear trendlines, we examine student-level granularity, proving that consistent study combined with high attendance strongly drives academic achievement. 

Crucially, in our physiological view, we track Heart Rate Variability in milliseconds. Students experiencing severe distress show significantly suppressed heart rate variability below 50 milliseconds, providing an objective biomarker that confirms self-reported survey ratings. Finally, our Mental Health Risk distribution reveals that 23.9% of students fall into the high-risk category, proving the necessity of targeted early interventions.

From our empirical findings, three critical insights emerge. First, sleep duration serves as a powerful natural stress buffer; students sleeping under 6 hours average significantly higher stress levels than those achieving 7.5 hours or more. Second, excessive study hours exhibit diminishing returns when coupled with acute anxiety. And third, social interaction and peer support strongly mitigate depressive symptoms, highlighting that campus engagement is vital for emotional resilience.

To make these findings universally accessible, I developed a responsive, portfolio-quality web application deployed via GitHub Pages and automated GitHub Actions. The web portal features an executive summary, direct live Tableau embed with interactive controls, visualization breakdowns, full academic documentation, and direct source code links, all adhering to modern responsive UX standards and student privacy guidelines.

In conclusion, this project illustrates how modern business intelligence tools can transform campus health data into actionable institutional insights. Looking forward, this platform could be expanded with longitudinal wearable sensor streams and semester-long time-series tracking. Thank you for watching, and I invite you to explore the live dashboard and documentation on our GitHub repository.
"""

OUTPUT_AUDIO = os.path.join("site", "assets", "video", "narration.mp3")

async def generate():
    voice = "en-IN-PrabhatNeural"
    print(f"[INFO] Synthesizing speech with voice: {voice}")
    communicate = edge_tts.Communicate(SCRIPT_TEXT, voice, rate="-4%")
    await communicate.save(OUTPUT_AUDIO)
    print(f"[SUCCESS] Audio saved to: {OUTPUT_AUDIO}")

if __name__ == "__main__":
    asyncio.run(generate())
