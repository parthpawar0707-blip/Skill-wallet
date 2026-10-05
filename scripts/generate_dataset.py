"""
Dataset Generator for Student Mental Health Project
Generates 80 realistic student records reflecting authentic academic and lifestyle patterns.
"""
import csv
import random

# Fix random seed for exact reproducibility
random.seed(42)

departments = [
    "Computer Science", 
    "Mechanical Engineering", 
    "Electronics & Comm", 
    "Business Administration", 
    "Humanities & Arts"
]
years = ["1st Year", "2nd Year", "3rd Year", "4th Year"]
genders = ["Female", "Male", "Female", "Male", "Female", "Male", "Non-Binary"]
support_systems = ["Family", "Friends", "Multiple", "Counselor", "None"]

# Archetypes to ensure realistic distributions across High, Medium, Low risk
records = []

for i in range(1, 81):
    student_id = f"STU{1000 + i}"
    
    # Assign an archetype with natural probability
    # 0: High Stress / Vulnerable (approx 25%)
    # 1: Moderate Stress / Typical Busy Student (approx 45%)
    # 2: Resilient / Well-balanced Student (approx 30%)
    archetype = random.choices([0, 1, 2], weights=[0.25, 0.45, 0.30])[0]
    
    age = random.choice([18, 19, 20, 21, 22, 23, 24])
    gender = random.choice(genders)
    year = random.choice(years)
    dept = random.choice(departments)
    
    if archetype == 0:
        # High Risk / High Stress archetype
        sleep_hours = round(random.uniform(4.0, 5.8), 1)
        screen_time = round(random.uniform(7.0, 10.5), 1)
        study_hours = round(random.uniform(2.5, 7.5), 1)
        social_hours = round(random.uniform(0.5, 2.0), 1)
        physical_activity = round(random.uniform(0.0, 1.0), 1)
        
        stress_level = random.randint(7, 10)
        anxiety_level = random.randint(7, 10)
        depression_level = random.randint(6, 10)
        mood_score = random.randint(2, 5)
        
        # Low HRV corresponds to elevated sympathetic nervous system / chronic stress
        hrv = round(random.uniform(30.0, 44.0), 1)
        support = random.choice(["None", "Counselor", "Friends", "Family"])
        attendance = round(random.uniform(58.0, 80.0), 1)
        
        # Academic performance: affected by stress and attendance, moderate to lower
        base_perf = 55 + (study_hours * 2.5) + (attendance * 0.15) - (stress_level * 1.8)
        perf = round(max(45.0, min(82.0, base_perf + random.uniform(-4, 4))), 1)
        
        mental_risk = "High" if (stress_level >= 8 or depression_level >= 8) else "Medium"
        
    elif archetype == 1:
        # Moderate Risk / Typical College Student archetype
        sleep_hours = round(random.uniform(5.8, 7.2), 1)
        screen_time = round(random.uniform(4.5, 7.5), 1)
        study_hours = round(random.uniform(3.0, 6.5), 1)
        social_hours = round(random.uniform(1.5, 3.5), 1)
        physical_activity = round(random.uniform(0.5, 1.8), 1)
        
        stress_level = random.randint(4, 7)
        anxiety_level = random.randint(4, 7)
        depression_level = random.randint(3, 6)
        mood_score = random.randint(5, 7)
        
        hrv = round(random.uniform(45.0, 62.0), 1)
        support = random.choice(["Family", "Friends", "Multiple", "Family"])
        attendance = round(random.uniform(72.0, 89.0), 1)
        
        base_perf = 64 + (study_hours * 2.2) + (attendance * 0.12) - (stress_level * 1.0)
        perf = round(max(60.0, min(89.0, base_perf + random.uniform(-3, 3))), 1)
        
        mental_risk = "Medium" if (stress_level >= 5 or anxiety_level >= 6) else "Low"
        
    else:
        # Low Risk / Balanced Student archetype
        sleep_hours = round(random.uniform(7.0, 8.8), 1)
        screen_time = round(random.uniform(2.5, 5.0), 1)
        study_hours = round(random.uniform(4.0, 7.5), 1)
        social_hours = round(random.uniform(2.5, 5.0), 1)
        physical_activity = round(random.uniform(1.2, 2.8), 1)
        
        stress_level = random.randint(1, 4)
        anxiety_level = random.randint(1, 4)
        depression_level = random.randint(1, 3)
        mood_score = random.randint(7, 10)
        
        # High HRV indicates healthy cardiac vagal tone
        hrv = round(random.uniform(63.0, 84.0), 1)
        support = random.choice(["Family", "Multiple", "Friends", "Multiple"])
        attendance = round(random.uniform(84.0, 97.5), 1)
        
        base_perf = 74 + (study_hours * 2.0) + (attendance * 0.12) - (stress_level * 0.8)
        perf = round(max(75.0, min(97.0, base_perf + random.uniform(-2, 3))), 1)
        
        mental_risk = "Low"

    records.append({
        "Student_ID": student_id,
        "Age": age,
        "Gender": gender,
        "Academic_Year": year,
        "Department": dept,
        "Study_Hours": study_hours,
        "Sleep_Hours": sleep_hours,
        "Screen_Time": screen_time,
        "Social_Interaction_Hours": social_hours,
        "Physical_Activity_Hours": physical_activity,
        "Stress_Level": stress_level,
        "Anxiety_Level": anxiety_level,
        "Depression_Level": depression_level,
        "Mood_Score": mood_score,
        "Academic_Performance": perf,
        "Attendance_Percentage": attendance,
        "Heart_Rate_Variability": hrv,
        "Support_System": support,
        "Mental_Health_Risk": mental_risk
    })

fieldnames = [
    "Student_ID", "Age", "Gender", "Academic_Year", "Department",
    "Study_Hours", "Sleep_Hours", "Screen_Time", "Social_Interaction_Hours",
    "Physical_Activity_Hours", "Stress_Level", "Anxiety_Level", "Depression_Level",
    "Mood_Score", "Academic_Performance", "Attendance_Percentage",
    "Heart_Rate_Variability", "Support_System", "Mental_Health_Risk"
]

with open("data/student_mental_health.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(records)

print(f"Generated {len(records)} student records into data/student_mental_health.csv")
