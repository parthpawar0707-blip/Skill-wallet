import os
import json
import subprocess
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

# Set high-quality styling
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#CBD5E1'
plt.rcParams['axes.linewidth'] = 0.8

os.makedirs('temp_frames', exist_ok=True)
os.makedirs('temp_clips', exist_ok=True)

df = pd.read_csv('data/mental_health_student_ecosystem_cleaned.csv')

with open('temp_audio/timings.json') as f:
    timings = json.load(f)

def create_base_canvas(chapter_num, chapter_title, subheader=""):
    fig = plt.figure(figsize=(12.8, 7.2), dpi=100)
    fig.patch.set_facecolor('#F8FAFC')
    ax_bg = fig.add_axes([0, 0, 1, 1])
    ax_bg.axis('off')
    
    # Top banner
    ax_bg.add_patch(patches.Rectangle((0, 0.88), 1, 0.12, facecolor='#0F172A', transform=ax_bg.transAxes))
    # Accent stripe
    ax_bg.add_patch(patches.Rectangle((0, 0.873), 1, 0.007, facecolor='#0F766E', transform=ax_bg.transAxes))
    # Bottom banner
    ax_bg.add_patch(patches.Rectangle((0, 0), 1, 0.06, facecolor='#0F172A', transform=ax_bg.transAxes))
    
    # Header texts
    ax_bg.text(0.04, 0.945, "ANALYSING MENTAL HEALTH IN STUDENT ECOSYSTEM", 
               color='#94A3B8', fontsize=12, weight='bold', transform=ax_bg.transAxes, va='center')
    ax_bg.text(0.04, 0.908, f"Chapter {chapter_num}: {chapter_title}", 
               color='#FFFFFF', fontsize=17, weight='bold', transform=ax_bg.transAxes, va='center')
    
    # Presenter tag
    ax_bg.text(0.96, 0.93, "Presenter: Parth Pawar", 
               color='#38BDF8', fontsize=12, weight='bold', ha='right', transform=ax_bg.transAxes, va='center')
    ax_bg.text(0.96, 0.898, "Tableau Public & Data Analytics Portfolio", 
               color='#94A3B8', fontsize=10, ha='right', transform=ax_bg.transAxes, va='center')
    
    # Footer text
    ax_bg.text(0.04, 0.03, "Tableau BI Demonstration • Empirical Cohort Analysis • 200 Students", 
               color='#64748B', fontsize=10, transform=ax_bg.transAxes, va='center')
    ax_bg.text(0.96, 0.03, "parthpawar0707-blip.github.io/Skill-wallet", 
               color='#38BDF8', fontsize=10, ha='right', transform=ax_bg.transAxes, va='center')
    
    return fig

# ----------------- SCENE GENERATORS ----------------- #

def render_scene_01():
    fig = plt.figure(figsize=(12.8, 7.2), dpi=100)
    fig.patch.set_facecolor('#0B1329')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    
    # Decorative elements
    ax.add_patch(patches.Rectangle((0, 0.85), 1, 0.15, facecolor='#0F172A', transform=ax.transAxes))
    ax.add_patch(patches.Rectangle((0, 0.84), 1, 0.01, facecolor='#0F766E', transform=ax.transAxes))
    
    # Title badge
    ax.text(0.5, 0.72, "DATA ANALYTICS & BUSINESS INTELLIGENCE PORTFOLIO", color='#2DD4BF', fontsize=14, weight='bold', ha='center')
    ax.text(0.5, 0.58, "Analysing Mental Health in Student Ecosystem", color='#FFFFFF', fontsize=28, weight='bold', ha='center')
    ax.text(0.5, 0.49, "A Multi-Dimensional Tableau Business Intelligence & Behavioral Analytics Investigation", color='#94A3B8', fontsize=15, ha='center')
    
    # Metadata cards
    box_props = dict(boxstyle='round,pad=0.8', facecolor='#1E293B', edgecolor='#334155', linewidth=1.5)
    meta_text = (
        "  Author: Parth Pawar          |   Tools: Tableau Desktop, Tableau Public, Python (Pandas)  \n"
        "  Cohort: 200 Undergraduates   |   Variables: 18 Telemetry & Well-Being Metrics             \n"
        "  Platform: GitHub Pages CI/CD |   Verification: 100% Complete (0 Missing, 0 Duplicates)    "
    )
    ax.text(0.5, 0.30, meta_text, color='#E2E8F0', fontsize=13, ha='center', bbox=box_props, linespacing=1.6)
    
    ax.text(0.5, 0.12, "Interactive Tableau Public Dashboard • Verified Empirical Findings • Project Walkthrough", color='#64748B', fontsize=12, ha='center')
    
    plt.savefig('temp_frames/scene_01_intro.png', facecolor=fig.get_facecolor(), bbox_inches='tight', pad_inches=0)
    plt.close()

def render_scene_02():
    fig = create_base_canvas(2, "Problem Statement & Analytical Objectives")
    ax = fig.add_axes([0.08, 0.14, 0.84, 0.68])
    ax.axis('off')
    
    cards = [
        ("Academic & Environmental Pressures", 
         "Undergraduate students routinely navigate heavy examination schedules,\nGPA benchmarking, erratic sleep cycles, and extended digital exposure\nthat heighten emotional vulnerability and academic burnout.",
         "#EFF6FF", "#2563EB"),
        ("Multi-Dimensional Lifestyle Telemetry", 
         "Mental health does not deteriorate in isolation. We analyze objective lifestyle\nindicators: daily screen time (hrs), sleep quality (Poor, Average, Good),\nphysical activity levels, and peer social interaction scores.",
         "#F0FDFA", "#0F766E"),
        ("Proactive Institutional Decision Support", 
         "Traditional counseling is often sought reactively after severe crisis.\nThis Tableau dashboard provides academic mentors and healthcare centers\nwith empirical risk signals for timely, non-invasive support interventions.",
         "#FAF5FF", "#7C3AED")
    ]
    
    y = 0.76
    for title, desc, bgcolor, bordercolor in cards:
        rect = patches.FancyBboxPatch((0.02, y - 0.22), 0.96, 0.23, boxstyle="round,pad=0.03", 
                                     facecolor=bgcolor, edgecolor=bordercolor, linewidth=1.5, transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(0.06, y - 0.05, title, fontsize=15, weight='bold', color=bordercolor, transform=ax.transAxes)
        ax.text(0.06, y - 0.15, desc, fontsize=12, color='#334155', transform=ax.transAxes, linespacing=1.4)
        y -= 0.30
        
    plt.savefig('temp_frames/scene_02_problem.png', facecolor=fig.get_facecolor(), bbox_inches='tight', pad_inches=0)
    plt.close()

def render_scene_03():
    fig = create_base_canvas(3, "Dataset Architecture & Source Verification")
    
    # Left table: Schema Overview
    ax_left = fig.add_axes([0.06, 0.14, 0.42, 0.68])
    ax_left.axis('off')
    
    ax_left.text(0, 0.95, "Verified Schema: 18 Attributes Across 200 Students", fontsize=14, weight='bold', color='#0F172A', transform=ax_left.transAxes)
    
    fields = [
        ("Identifiers", "User ID (STU_0001 to STU_0200)", "String (Primary Key)"),
        ("Demographics", "Age (18–25), Gender (M/F/Other), Occupation", "Discrete / Categorical"),
        ("Mental Health", "Stress Level (Low, Med, High)", "Categorical Tier"),
        ("Clinical Scales", "Anxiety Score (0–100), Depression Score (0–100)", "Continuous Numeric"),
        ("Lifestyle Habits", "Daily Screen Time (hrs), Sleep Quality", "Continuous / Ordinal"),
        ("Physical & Social", "Physical Activity Level, Social Interaction", "Categorical / Numeric"),
        ("Interventions", "Therapy Type (CBT, Counseling, etc.)", "Categorical Modality"),
        ("Progress & Support", "Intervention Duration, Progress Score (0–100)", "Continuous Numeric")
    ]
    
    y = 0.85
    for cat, col_desc, dtype in fields:
        ax_left.text(0.02, y, f"• {cat}:", fontsize=11, weight='bold', color='#0F766E', transform=ax_left.transAxes)
        ax_left.text(0.30, y, col_desc, fontsize=10.5, color='#334155', transform=ax_left.transAxes)
        y -= 0.105
        
    # Right panel: Integrity Metrics
    ax_right = fig.add_axes([0.54, 0.14, 0.40, 0.68])
    ax_right.axis('off')
    
    ax_right.text(0, 0.95, "Data Hygiene & Completeness Validation", fontsize=14, weight='bold', color='#0F172A', transform=ax_right.transAxes)
    
    metrics = [
        ("Total Records", "200 Students", "100% verified undergraduate records"),
        ("Missing / Null Values", "0 (Zero)", "Strict validation via Pandas null-check"),
        ("Duplicate Records", "0 (Zero)", "Confirmed unique User ID per record"),
        ("Data Source Type", "Cleaned Hyper Extract", "Embedded in Tableau packaged workbook (.twbx)")
    ]
    
    y = 0.82
    for m_label, m_val, m_sub in metrics:
        rect = patches.FancyBboxPatch((0.02, y - 0.16), 0.94, 0.17, boxstyle="round,pad=0.02",
                                      facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=1, transform=ax_right.transAxes)
        ax_right.add_patch(rect)
        ax_right.text(0.06, y - 0.05, m_label, fontsize=11, color='#64748B', transform=ax_right.transAxes)
        ax_right.text(0.06, y - 0.11, m_val, fontsize=15, weight='bold', color='#0F766E', transform=ax_right.transAxes)
        ax_right.text(0.06, y - 0.15, m_sub, fontsize=9.5, color='#94A3B8', transform=ax_right.transAxes)
        y -= 0.22
        
    plt.savefig('temp_frames/scene_03_dataset.png', facecolor=fig.get_facecolor(), bbox_inches='tight', pad_inches=0)
    plt.close()

def render_scene_04():
    fig = create_base_canvas(4, "Data Cleansing & Calculation Engineering")
    ax = fig.add_axes([0.08, 0.14, 0.84, 0.68])
    ax.axis('off')
    
    ax.text(0, 0.95, "Engineered Tableau Calculated Fields", fontsize=16, weight='bold', color='#0F172A', transform=ax.transAxes)
    
    calcs = [
        ("Calculated Field 1: Active_Therapy",
         "IF [Therapy Type] != \"No Therapy\" THEN 1 ELSE 0 END",
         "Purpose: Creates a discrete binary flag to segment students actively participating\nin structured institutional therapy versus students without therapeutic support.",
         "#0F766E"),
        ("Calculated Field 2: HighStress_PoorSleep",
         "IF [Stress Level] = \"High\" AND [Sleep Quality] = \"Poor\" THEN 1 ELSE 0 END",
         "Purpose: Isolates students suffering from severe dual physiological risk:\nacute subjective stress coupled with critical sleep disruption (35 students identified).",
         "#E11D48")
    ]
    
    y = 0.82
    for c_title, c_formula, c_desc, c_color in calcs:
        rect = patches.FancyBboxPatch((0.02, y - 0.32), 0.96, 0.34, boxstyle="round,pad=0.03",
                                      facecolor='#FFFFFF', edgecolor=c_color, linewidth=1.5, transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(0.05, y - 0.04, c_title, fontsize=15, weight='bold', color=c_color, transform=ax.transAxes)
        
        # Formula box
        f_box = patches.FancyBboxPatch((0.05, y - 0.17), 0.90, 0.09, boxstyle="round,pad=0.02",
                                      facecolor='#F1F5F9', edgecolor='#CBD5E1', transform=ax.transAxes)
        ax.add_patch(f_box)
        ax.text(0.08, y - 0.13, c_formula, fontsize=13, weight='bold', color='#0F172A', fontfamily='monospace', transform=ax.transAxes)
        ax.text(0.05, y - 0.26, c_desc, fontsize=11.5, color='#475569', transform=ax.transAxes, linespacing=1.4)
        y -= 0.44
        
    plt.savefig('temp_frames/scene_04_methodology.png', facecolor=fig.get_facecolor(), bbox_inches='tight', pad_inches=0)
    plt.close()

def render_scene_05():
    fig = create_base_canvas(5, "Tableau Dashboard: Executive KPI Ribbon & Workbook View")
    ax = fig.add_axes([0.06, 0.12, 0.88, 0.72])
    ax.axis('off')
    
    kpis = [
        ("Total Cohort Size", "200", "Students", "#2563EB", "#EFF6FF"),
        ("Avg Anxiety Score", "52.59", "Scale 0–100", "#0F766E", "#F0FDFA"),
        ("Avg Depression Score", "48.09", "Scale 0–100", "#7C3AED", "#FAF5FF"),
        ("Avg Screen Time", "7.10", "Hours / Day", "#EA580C", "#FFF7ED")
    ]
    
    x_positions = [0.01, 0.26, 0.51, 0.76]
    for x, (k_title, k_val, k_unit, k_color, k_bg) in zip(x_positions, kpis):
        rect = patches.FancyBboxPatch((x, 0.68), 0.23, 0.28, boxstyle="round,pad=0.02",
                                      facecolor=k_bg, edgecolor=k_color, linewidth=1.5, transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(x + 0.115, 0.89, k_title, fontsize=11, weight='bold', color='#0F172A', ha='center', transform=ax.transAxes)
        ax.text(x + 0.115, 0.77, k_val, fontsize=22, weight='bold', color=k_color, ha='center', transform=ax.transAxes)
        ax.text(x + 0.115, 0.71, k_unit, fontsize=9.5, color='#64748B', ha='center', transform=ax.transAxes)
        
    # Embed authentic Tableau Public dashboard capture
    if os.path.exists('temp_tableau_shot.png'):
        img = Image.open('temp_tableau_shot.png')
        ax_tab = fig.add_axes([0.08, 0.12, 0.84, 0.48])
        ax_tab.imshow(img)
        ax_tab.axis('off')
        # Border around Tableau capture
        rect_border = patches.Rectangle((0, 0), 1, 1, fill=False, edgecolor='#CBD5E1', linewidth=1.5, transform=ax_tab.transAxes)
        ax_tab.add_patch(rect_border)
        ax.text(0.5, 0.63, "Authentic Tableau Public Workbook • Live Interactive BI Telemetry", 
                fontsize=11, weight='bold', color='#0F766E', ha='center', transform=ax.transAxes)
    else:
        ax.text(0.5, 0.35, "Tableau Public Dashboard Walkthrough", fontsize=16, color='#64748B', ha='center', transform=ax.transAxes)
    
    plt.savefig('temp_frames/scene_05_kpi.png', facecolor=fig.get_facecolor(), bbox_inches='tight', pad_inches=0)
    plt.close()

def render_scene_06():
    fig = create_base_canvas(6, "Worksheet 1: Stress Level Distribution")
    
    # Left: Actual bar chart
    ax_chart = fig.add_axes([0.08, 0.18, 0.48, 0.62])
    counts = df['Stress Level'].value_counts()[['Low', 'Medium', 'High']]
    colors = ['#10B981', '#F59E0B', '#EF4444']
    bars = ax_chart.bar(counts.index, counts.values, color=colors, width=0.55, edgecolor='#334155', linewidth=1)
    
    for bar in bars:
        h = bar.get_height()
        pct = (h / len(df)) * 100
        ax_chart.text(bar.get_x() + bar.get_width()/2., h + 2.5, f"{int(h)} ({pct:.1f}%)", 
                      ha='center', va='bottom', fontsize=12, weight='bold', color='#0F172A')
        
    ax_chart.set_ylim(0, 125)
    ax_chart.set_ylabel("Student Count (COUNT([User ID]))", fontsize=11, weight='bold', color='#334155')
    ax_chart.set_title("Stress Level Distribution across Cohort", fontsize=13, weight='bold', pad=12, color='#0F172A')
    ax_chart.grid(axis='y', linestyle='--', alpha=0.5)
    
    # Right: Analytical takeaway card
    ax_info = fig.add_axes([0.62, 0.18, 0.32, 0.62])
    ax_info.axis('off')
    
    rect = patches.FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.03",
                                  facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=1.5, transform=ax_info.transAxes)
    ax_info.add_patch(rect)
    
    ax_info.text(0.08, 0.88, "Key Analytical Observations", fontsize=13, weight='bold', color='#0F172A', transform=ax_info.transAxes)
    
    pts = [
        ("Medium Stress Predominance:", "107 students (53.5%) operate in the\nmedium stress tier, forming the majority."),
        ("High Stress Prevalence:", "49 students (24.5%) suffer from acute\nhigh stress requiring priority support."),
        ("Low Stress Cohort:", "Only 44 students (22.0%) report low\nstress levels."),
        ("Institutional Takeaway:", "Over 78% of students experience\nmoderate-to-severe stress levels.")
    ]
    
    y = 0.74
    for title, desc in pts:
        ax_info.text(0.08, y, title, fontsize=11, weight='bold', color='#0F766E', transform=ax_info.transAxes)
        ax_info.text(0.08, y - 0.11, desc, fontsize=10.5, color='#475569', transform=ax_info.transAxes, linespacing=1.3)
        y -= 0.22
        
    plt.savefig('temp_frames/scene_06_stress_dist.png', facecolor=fig.get_facecolor(), bbox_inches='tight', pad_inches=0)
    plt.close()

def render_scene_07():
    fig = create_base_canvas(7, "Worksheet 2: Daily Screen Time vs Stress Level")
    
    ax_chart = fig.add_axes([0.08, 0.18, 0.48, 0.62])
    screen_means = df.groupby('Stress Level')['Daily Screen Time (hrs)'].mean()[['Low', 'Medium', 'High']]
    colors = ['#38BDF8', '#0284C7', '#0369A1']
    bars = ax_chart.bar(screen_means.index, screen_means.values, color=colors, width=0.55, edgecolor='#0C4A6E', linewidth=1)
    
    for bar in bars:
        h = bar.get_height()
        ax_chart.text(bar.get_x() + bar.get_width()/2., h + 0.15, f"{h:.2f} hrs", 
                      ha='center', va='bottom', fontsize=12, weight='bold', color='#0F172A')
        
    ax_chart.set_ylim(0, 10)
    ax_chart.set_ylabel("Average Daily Screen Time (Hours)", fontsize=11, weight='bold', color='#334155')
    ax_chart.set_title("Screen Time Escalation by Stress Level", fontsize=13, weight='bold', pad=12, color='#0F172A')
    ax_chart.grid(axis='y', linestyle='--', alpha=0.5)
    
    ax_info = fig.add_axes([0.62, 0.18, 0.32, 0.62])
    ax_info.axis('off')
    
    rect = patches.FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.03",
                                  facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=1.5, transform=ax_info.transAxes)
    ax_info.add_patch(rect)
    
    ax_info.text(0.08, 0.88, "Key Analytical Observations", fontsize=13, weight='bold', color='#0F172A', transform=ax_info.transAxes)
    
    pts = [
        ("Monotonic Upward Trend:", "Screen time increases steadily with stress:\nLow: 6.00 hrs | Med: 7.07 hrs | High: 8.12 hrs"),
        ("The +2.12 Hour Gap:", "High-stress students consume over 2 hours\nmore daily screen time than low-stress peers."),
        ("Digital Fatigue Threshold:", "Average screen time beyond 7.5 hours strongly\nco-occurs with elevated stress states."),
        ("Institutional Takeaway:", "Digital hygiene workshops represent a high-\nimpact, non-clinical intervention pathway.")
    ]
    
    y = 0.74
    for title, desc in pts:
        ax_info.text(0.08, y, title, fontsize=11, weight='bold', color='#0F766E', transform=ax_info.transAxes)
        ax_info.text(0.08, y - 0.11, desc, fontsize=10.5, color='#475569', transform=ax_info.transAxes, linespacing=1.3)
        y -= 0.22
        
    plt.savefig('temp_frames/scene_07_screen_time.png', facecolor=fig.get_facecolor(), bbox_inches='tight', pad_inches=0)
    plt.close()

def render_scene_08():
    fig = create_base_canvas(8, "Worksheet 3: Sleep Quality vs Stress Level")
    
    ax_chart = fig.add_axes([0.08, 0.18, 0.48, 0.62])
    ct = pd.crosstab(df['Sleep Quality'], df['Stress Level'])[['Low', 'Medium', 'High']].reindex(['Poor', 'Average', 'Good'])
    
    ct.plot(kind='bar', stacked=True, color=['#10B981', '#F59E0B', '#EF4444'], ax=ax_chart, width=0.55, edgecolor='#334155')
    ax_chart.set_ylabel("Student Count (COUNT([User ID]))", fontsize=11, weight='bold', color='#334155')
    ax_chart.set_title("Sleep Quality Cross-Tabulation by Stress Level", fontsize=13, weight='bold', pad=12, color='#0F172A')
    ax_chart.set_xticklabels(['Poor Sleep\n(66 total)', 'Average Sleep\n(89 total)', 'Good Sleep\n(45 total)'], rotation=0)
    ax_chart.legend(title='Stress Level', loc='upper right')
    ax_chart.grid(axis='y', linestyle='--', alpha=0.5)
    
    ax_info = fig.add_axes([0.62, 0.18, 0.32, 0.62])
    ax_info.axis('off')
    
    rect = patches.FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.03",
                                  facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=1.5, transform=ax_info.transAxes)
    ax_info.add_patch(rect)
    
    ax_info.text(0.08, 0.88, "Key Analytical Observations", fontsize=13, weight='bold', color='#0F172A', transform=ax_info.transAxes)
    
    pts = [
        ("Poor Sleep Disruption (66 students):", "35 suffer from High stress, 30 from Med stress,\nand ONLY 1 student maintains low stress!"),
        ("Good Sleep Protection (45 students):", "22 achieve Low stress, 21 Med stress, and\nONLY 2 students suffer from high stress."),
        ("Primary Resilience Buffer:", "Sleep quality is the strongest inverse\ncorrelate of severe psychological distress."),
        ("HighStress_PoorSleep Flag:", "35 students identified under dual acute\nrisk via our Tableau calculated field.")
    ]
    
    y = 0.74
    for title, desc in pts:
        ax_info.text(0.08, y, title, fontsize=11, weight='bold', color='#0F766E', transform=ax_info.transAxes)
        ax_info.text(0.08, y - 0.11, desc, fontsize=10.5, color='#475569', transform=ax_info.transAxes, linespacing=1.3)
        y -= 0.22
        
    plt.savefig('temp_frames/scene_08_sleep_quality.png', facecolor=fig.get_facecolor(), bbox_inches='tight', pad_inches=0)
    plt.close()

def render_scene_09():
    fig = create_base_canvas(9, "Worksheet 4: Gender Mental Health Comparison")
    
    ax_chart = fig.add_axes([0.08, 0.18, 0.48, 0.62])
    g_means = df.groupby('Gender')[['Anxiety Score', 'Depression Score']].mean()
    
    x = np.arange(len(g_means))
    width = 0.32
    rects1 = ax_chart.bar(x - width/2, g_means['Anxiety Score'], width, label='Avg Anxiety Score', color='#0F766E', edgecolor='#134E4A')
    rects2 = ax_chart.bar(x + width/2, g_means['Depression Score'], width, label='Avg Depression Score', color='#2563EB', edgecolor='#1E3A8A')
    
    for r in rects1:
        ax_chart.text(r.get_x() + r.get_width()/2., r.get_height() + 1, f"{r.get_height():.1f}", ha='center', fontsize=11, weight='bold')
    for r in rects2:
        ax_chart.text(r.get_x() + r.get_width()/2., r.get_height() + 1, f"{r.get_height():.1f}", ha='center', fontsize=11, weight='bold')
        
    ax_chart.set_xticks(x)
    ax_chart.set_xticklabels(g_means.index, fontsize=11)
    ax_chart.set_ylim(0, 75)
    ax_chart.set_ylabel("Score (0–100 Scale)", fontsize=11, weight='bold', color='#334155')
    ax_chart.set_title("Anxiety & Depression Comparison by Gender", fontsize=13, weight='bold', pad=12, color='#0F172A')
    ax_chart.legend(loc='upper right')
    ax_chart.grid(axis='y', linestyle='--', alpha=0.5)
    
    ax_info = fig.add_axes([0.62, 0.18, 0.32, 0.62])
    ax_info.axis('off')
    
    rect = patches.FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.03",
                                  facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=1.5, transform=ax_info.transAxes)
    ax_info.add_patch(rect)
    
    ax_info.text(0.08, 0.88, "Key Analytical Observations", fontsize=13, weight='bold', color='#0F172A', transform=ax_info.transAxes)
    
    pts = [
        ("Demographic Parity:", "Anxiety is uniform across cohorts:\nFemale: 53.3 | Male: 51.8 | Other: 53.5"),
        ("Depression Consistency:", "Depression severity shows similar parity:\nFemale: 48.1 | Male: 47.9 | Other: 50.4"),
        ("Key Statistical Takeaway:", "Minimal variance between genders confirms\npsychological distress is cohort-wide."),
        ("Programmatic Guidance:", "Interventions should target lifestyle drivers\n(sleep, screen habits) rather than demographics.")
    ]
    
    y = 0.74
    for title, desc in pts:
        ax_info.text(0.08, y, title, fontsize=11, weight='bold', color='#0F766E', transform=ax_info.transAxes)
        ax_info.text(0.08, y - 0.11, desc, fontsize=10.5, color='#475569', transform=ax_info.transAxes, linespacing=1.3)
        y -= 0.22
        
    plt.savefig('temp_frames/scene_09_gender.png', facecolor=fig.get_facecolor(), bbox_inches='tight', pad_inches=0)
    plt.close()

def render_scene_10():
    fig = create_base_canvas(10, "Worksheets 5 & 6: Stress vs Anxiety and Depression")
    
    # Dual bar charts
    ax1 = fig.add_axes([0.08, 0.18, 0.40, 0.62])
    ax2 = fig.add_axes([0.54, 0.18, 0.40, 0.62])
    
    anx_means = df.groupby('Stress Level')['Anxiety Score'].mean()[['Low', 'Medium', 'High']]
    dep_means = df.groupby('Stress Level')['Depression Score'].mean()[['Low', 'Medium', 'High']]
    
    bars1 = ax1.bar(anx_means.index, anx_means.values, color=['#10B981', '#F59E0B', '#EF4444'], width=0.55, edgecolor='#334155')
    for b in bars1:
        ax1.text(b.get_x() + b.get_width()/2., b.get_height() + 1.5, f"{b.get_height():.2f}", ha='center', fontsize=11, weight='bold')
    ax1.set_ylim(0, 90)
    ax1.set_title("Worksheet 5: Stress vs Anxiety", fontsize=12, weight='bold', color='#0F172A')
    ax1.set_ylabel("Average Anxiety Score", fontsize=11, weight='bold')
    ax1.grid(axis='y', linestyle='--', alpha=0.5)
    
    bars2 = ax2.bar(dep_means.index, dep_means.values, color=['#10B981', '#F59E0B', '#EF4444'], width=0.55, edgecolor='#334155')
    for b in bars2:
        ax2.text(b.get_x() + b.get_width()/2., b.get_height() + 1.5, f"{b.get_height():.2f}", ha='center', fontsize=11, weight='bold')
    ax2.set_ylim(0, 90)
    ax2.set_title("Worksheet 6: Stress vs Depression", fontsize=12, weight='bold', color='#0F172A')
    ax2.set_ylabel("Average Depression Score", fontsize=11, weight='bold')
    ax2.grid(axis='y', linestyle='--', alpha=0.5)
    
    plt.savefig('temp_frames/scene_10_anxiety_depression.png', facecolor=fig.get_facecolor(), bbox_inches='tight', pad_inches=0)
    plt.close()

def render_scene_11():
    fig = create_base_canvas(11, "Worksheets 7 & 8: Therapy Efficacy & History Prevalence")
    
    # Left: Therapy Efficacy (Horiz bar)
    ax1 = fig.add_axes([0.08, 0.18, 0.44, 0.62])
    t_means = df.groupby('Therapy Type')['Progress Score'].mean().sort_values(ascending=True)
    bars = ax1.barh(t_means.index, t_means.values, color='#0F766E', edgecolor='#134E4A', height=0.55)
    for b in bars:
        w = b.get_width()
        ax1.text(w + 1, b.get_y() + b.get_height()/2., f"{w:.2f}", va='center', fontsize=11, weight='bold')
    ax1.set_xlim(0, 50)
    ax1.set_xlabel("Average Progress Score", fontsize=11, weight='bold')
    ax1.set_title("Worksheet 7: Ranked Therapy Efficacy", fontsize=12, weight='bold', color='#0F172A')
    ax1.grid(axis='x', linestyle='--', alpha=0.5)
    
    # Right: Pie chart Mental health history
    ax2 = fig.add_axes([0.58, 0.18, 0.36, 0.62])
    h_counts = df['Mental Health History'].value_counts()
    ax2.pie(h_counts, labels=[f"No History\n{h_counts['No']} (60%)", f"Family / Personal History\n{h_counts['Yes']} (40%)"],
            autopct='%1.1f%%', colors=['#38BDF8', '#F59E0B'], startangle=90, textprops={'fontsize': 11, 'weight': 'bold'})
    ax2.set_title("Worksheet 8: Prior Mental Health History", fontsize=12, weight='bold', color='#0F172A')
    
    plt.savefig('temp_frames/scene_11_therapy_prevalence.png', facecolor=fig.get_facecolor(), bbox_inches='tight', pad_inches=0)
    plt.close()

def render_scene_12():
    fig = create_base_canvas(12, "Empirical Findings & Interpretation")
    ax = fig.add_axes([0.08, 0.14, 0.84, 0.68])
    ax.axis('off')
    
    findings = [
        ("1. Sleep Quality is the Primary Resilience Buffer",
         "Students with Good sleep quality almost never experience high stress (only 2 out of 45 students).\nConversely, 53% of students with poor sleep suffer acute stress. Restorative sleep is the strongest insulator.",
         "#0F766E", "#F0FDFA"),
        ("2. The Digital Fatigue Threshold (7.5+ Hours)",
         "Screen time escalates from 6.00 hrs in Low stress to 8.12 hrs in High stress.\nSustained digital screen time beyond 7.5 hours strongly co-occurs with clinical anxiety spikes.",
         "#2563EB", "#EFF6FF"),
        ("3. Structured Intervention Proven Efficacy",
         "Cognitive Behavioral Therapy achieves the highest progress score (40.80), followed by counseling (34.43).\nActive therapeutic intervention delivers measurable improvement compared to unguided coping.",
         "#7C3AED", "#FAF5FF")
    ]
    
    y = 0.76
    for title, desc, bordercol, bgcol in findings:
        rect = patches.FancyBboxPatch((0.02, y - 0.22), 0.96, 0.23, boxstyle="round,pad=0.03",
                                      facecolor=bgcol, edgecolor=bordercol, linewidth=1.5, transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(0.06, y - 0.05, title, fontsize=14, weight='bold', color=bordercol, transform=ax.transAxes)
        ax.text(0.06, y - 0.15, desc, fontsize=11.5, color='#334155', transform=ax.transAxes, linespacing=1.4)
        y -= 0.30
        
    plt.savefig('temp_frames/scene_12_findings.png', facecolor=fig.get_facecolor(), bbox_inches='tight', pad_inches=0)
    plt.close()

def render_scene_13():
    # Capture or load actual screenshot of the website
    fig = create_base_canvas(13, "Portfolio Website & Public Deployment")
    
    # Load captured website screenshot if available
    if os.path.exists('temp_website_shot.png'):
        img = Image.open('temp_website_shot.png')
        ax_img = fig.add_axes([0.06, 0.14, 0.58, 0.68])
        ax_img.imshow(img)
        ax_img.axis('off')
    else:
        ax_img = fig.add_axes([0.06, 0.14, 0.58, 0.68])
        ax_img.axis('off')
        ax_img.text(0.5, 0.5, "Live Website Preview", ha='center', va='center', fontsize=16)
        
    # Right panel: Features
    ax_info = fig.add_axes([0.66, 0.14, 0.28, 0.68])
    ax_info.axis('off')
    
    ax_info.text(0, 0.95, "Portfolio Deliverables", fontsize=14, weight='bold', color='#0F172A', transform=ax_info.transAxes)
    
    feats = [
        ("Live Tableau Embed", "Direct iframe connection with responsive height & fallback card"),
        ("Worksheet Gallery", "Dedicated breakdown of all 8 core visualizations"),
        ("HTML5 Video Player", "Integrated captions, poster image, and download support"),
        ("Technical Reports", "Comprehensive project report and validation scripts"),
        ("GitHub Pages CI/CD", "Automated deployment workflow via GitHub Actions")
    ]
    
    y = 0.82
    for f_title, f_desc in feats:
        ax_info.text(0.02, y, f"✓ {f_title}", fontsize=11, weight='bold', color='#0F766E', transform=ax_info.transAxes)
        ax_info.text(0.02, y - 0.06, f_desc, fontsize=9.5, color='#475569', transform=ax_info.transAxes)
        y -= 0.16
        
    plt.savefig('temp_frames/scene_13_website.png', facecolor=fig.get_facecolor(), bbox_inches='tight', pad_inches=0)
    plt.close()

def render_scene_14():
    fig = plt.figure(figsize=(12.8, 7.2), dpi=100)
    fig.patch.set_facecolor('#0B1329')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    
    ax.add_patch(patches.Rectangle((0, 0.85), 1, 0.15, facecolor='#0F172A', transform=ax.transAxes))
    ax.add_patch(patches.Rectangle((0, 0.84), 1, 0.01, facecolor='#0F766E', transform=ax.transAxes))
    
    ax.text(0.5, 0.74, "THANK YOU FOR WATCHING", color='#2DD4BF', fontsize=16, weight='bold', ha='center')
    ax.text(0.5, 0.62, "Analysing Mental Health in Student Ecosystem", color='#FFFFFF', fontsize=26, weight='bold', ha='center')
    ax.text(0.5, 0.53, "Data Analytics & Business Intelligence Portfolio Project", color='#94A3B8', fontsize=15, ha='center')
    
    box_props = dict(boxstyle='round,pad=0.8', facecolor='#1E293B', edgecolor='#334155', linewidth=1.5)
    links_text = (
        "  Author: Parth Pawar                                                                    \n"
        "  GitHub Repository: https://github.com/parthpawar0707-blip/Skill-wallet                \n"
        "  Live Website:      https://parthpawar0707-blip.github.io/Skill-wallet/                \n"
        "  Tableau Dashboard: https://public.tableau.com/views/Student_Mental_Health_Analysis...  "
    )
    ax.text(0.5, 0.32, links_text, color='#E2E8F0', fontsize=12, ha='center', bbox=box_props, linespacing=1.6, fontfamily='monospace')
    
    ax.text(0.5, 0.12, "© 2026 Parth Pawar • SkillWallet / SmartBridge Data Analytics Program", color='#64748B', fontsize=12, ha='center')
    
    plt.savefig('temp_frames/scene_14_conclusion.png', facecolor=fig.get_facecolor(), bbox_inches='tight', pad_inches=0)
    plt.close()

def render_all_frames():
    print("Rendering 14 high-resolution 1280x720 video frames...")
    render_scene_01()
    render_scene_02()
    render_scene_03()
    render_scene_04()
    render_scene_05()
    render_scene_06()
    render_scene_07()
    render_scene_08()
    render_scene_09()
    render_scene_10()
    render_scene_11()
    render_scene_12()
    render_scene_13()
    render_scene_14()
    print("All 14 frames rendered successfully!")

def build_video():
    render_all_frames()
    
    clip_list = "temp_clips/clips.txt"
    with open(clip_list, "w") as f_clip:
        for t in timings:
            sec_id = t['id']
            dur = t['duration']
            img_path = f"temp_frames/{sec_id}.png"
            clip_path = f"temp_clips/{sec_id}.mp4"
            
            print(f"Encoding clip for {sec_id} ({dur:.2f}s)...")
            # Create video clip with exact frame rate and duration
            cmd = [
                'ffmpeg', '-y', '-loop', '1', '-i', img_path,
                '-c:v', 'libx264', '-t', str(dur),
                '-pix_fmt', 'yuv420p', '-r', '30',
                '-vf', 'scale=1280:720',
                clip_path
            ]
            subprocess.run(cmd, check=True)
            f_clip.write(f"file '{os.path.abspath(clip_path).replace(chr(92), '/')}'\n")
            
    # Concatenate video clips
    raw_video = "temp_clips/raw_combined.mp4"
    print("Concatenating video clips...")
    concat_cmd = [
        'ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', clip_list,
        '-c', 'copy', raw_video
    ]
    subprocess.run(concat_cmd, check=True)
    
    # Merge video and narration.mp3
    final_mp4 = "site/assets/video/student-mental-health-demo.mp4"
    print(f"Muxing audio and video into {final_mp4}...")
    mux_cmd = [
        'ffmpeg', '-y', '-i', raw_video, '-i', 'site/assets/video/narration.mp3',
        '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
        '-shortest', final_mp4
    ]
    subprocess.run(mux_cmd, check=True)
    
    # Generate high quality posters
    print("Generating video posters...")
    poster_jpg = "site/assets/video/video-poster.jpg"
    poster_png = "site/assets/images/video-poster.png"
    
    # Extract frame at 00:00:03 for poster
    poster_cmd = [
        'ffmpeg', '-y', '-ss', '00:00:03', '-i', final_mp4,
        '-vframes', '1', '-q:v', '2', poster_jpg
    ]
    subprocess.run(poster_cmd, check=True)
    
    # Copy to images/video-poster.png
    Image.open(poster_jpg).save(poster_png)
    
    print("\n==========================================")
    print("FINAL MP4 PRODUCTION COMPLETE!")
    print(f"File: {final_mp4}")
    print(f"Size: {os.path.getsize(final_mp4)} bytes ({os.path.getsize(final_mp4)/(1024*1024):.2f} MB)")
    print(f"Poster JPG: {poster_jpg} ({os.path.getsize(poster_jpg)} bytes)")
    print(f"Poster PNG: {poster_png} ({os.path.getsize(poster_png)} bytes)")
    print("==========================================")

if __name__ == '__main__':
    build_video()
