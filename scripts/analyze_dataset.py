"""
analyze_dataset.py
------------------
Audits and analyzes the verified student mental health dataset from the official Google Sheet.
Computes robust aggregate benchmarks and generates site/assets/data/summary.json without
exposing individual student records or emotional journal text.
"""

import urllib.request
import io
import json
import os
import sys
import pandas as pd

SOURCE_URL = "https://docs.google.com/spreadsheets/d/1DSnFv7DdV8l1nBcQ-KNIrbgnmDMIDeh7/export?format=csv"
OUTPUT_PATH = os.path.join("site", "assets", "data", "summary.json")

def categorize_age(age):
    if age < 20:
        return "Below 20"
    elif 20 <= age <= 22:
        return "20-22"
    elif 23 <= age <= 25:
        return "23-25"
    else:
        return "Above 25"

def categorize_study(hours):
    if hours < 3.0:
        return "Light (<3 hrs)"
    elif 3.0 <= hours <= 5.5:
        return "Moderate (3-5.5 hrs)"
    else:
        return "Intensive (>5.5 hrs)"

def categorize_sleep(hours):
    if hours < 6.0:
        return "Deprived (<6 hrs)"
    elif 6.0 <= hours <= 7.5:
        return "Adequate (6-7.5 hrs)"
    else:
        return "Optimal (>7.5 hrs)"

def analyze():
    print(f"[INFO] Fetching verified dataset from: {SOURCE_URL}")
    req = urllib.request.Request(SOURCE_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        csv_data = resp.read()

    df = pd.read_csv(io.BytesIO(csv_data))
    total_records = len(df)
    total_cols = len(df.columns)
    print(f"[INFO] Successfully loaded {total_records} rows and {total_cols} columns.")

    # Data Quality Validation
    null_counts = df.isnull().sum().to_dict()
    duplicates = int(df.duplicated().sum())
    unique_ids = int(df["Student_ID"].nunique())

    # Add calculated analytical groupings
    df["Age_Group"] = df["Age"].apply(categorize_age)
    df["Study_Category"] = df["Study_Hours_Per_Day"].apply(categorize_study)
    df["Sleep_Category"] = df["Sleep_Duration_Hours"].apply(categorize_sleep)

    # Core High-level KPIs
    kpis = {
        "total_students": total_records,
        "avg_stress_level": round(float(df["Stress_Level"].mean()), 2),
        "avg_depression_level": round(float(df["Depression_Level"].mean()), 2),
        "avg_anxiety_level": round(float(df["Anxiety_Level"].mean()), 2),
        "avg_sleep_hours": round(float(df["Sleep_Duration_Hours"].mean()), 2),
        "avg_attendance_rate": round(float(df["Attendance_Rate (%)"].mean()), 2),
        "avg_study_hours": round(float(df["Study_Hours_Per_Day"].mean()), 2),
        "avg_academic_performance_index": round(float(df["Academic_Performance_Index"].mean()), 2),
        "avg_heart_rate_variability": round(float(df["Heart_Rate_Variability"].mean()), 2),
        "avg_lms_activity": round(float(df["LMS_Activity_Score"].mean()), 2),
        "avg_social_interaction": round(float(df["Social_Interaction_Score"].mean()), 2)
    }

    # Grouped distributions
    gender_dist = df["Gender"].value_counts().to_dict()
    risk_dist = df["Mental_Health_Risk"].value_counts().to_dict()
    intervention_dist = df["Personalized_Intervention_Strategy"].value_counts().to_dict()
    age_group_dist = df["Age_Group"].value_counts().to_dict()

    # Cross-tabulations: Gender vs Stress & Depression
    gender_metrics = {}
    for g, group in df.groupby("Gender"):
        gender_metrics[g] = {
            "count": len(group),
            "avg_stress": round(float(group["Stress_Level"].mean()), 2),
            "avg_depression": round(float(group["Depression_Level"].mean()), 2),
            "avg_anxiety": round(float(group["Anxiety_Level"].mean()), 2),
            "avg_hrv": round(float(group["Heart_Rate_Variability"].mean()), 2),
            "avg_api": round(float(group["Academic_Performance_Index"].mean()), 2)
        }

    # Study Hours vs Academic Performance
    study_vs_perf = []
    for cat in ["Light (<3 hrs)", "Moderate (3-5.5 hrs)", "Intensive (>5.5 hrs)"]:
        subset = df[df["Study_Category"] == cat]
        study_vs_perf.append({
            "category": cat,
            "count": len(subset),
            "avg_study_hours": round(float(subset["Study_Hours_Per_Day"].mean()), 2),
            "avg_academic_perf": round(float(subset["Academic_Performance_Index"].mean()), 2),
            "avg_stress": round(float(subset["Stress_Level"].mean()), 2)
        })

    # Mental Health Risk vs Sleep & Attendance
    risk_metrics = {}
    for r in ["Low", "Medium", "High"]:
        subset = df[df["Mental_Health_Risk"] == r]
        risk_metrics[r] = {
            "count": len(subset),
            "percentage": round(len(subset) / total_records * 100, 1),
            "avg_sleep": round(float(subset["Sleep_Duration_Hours"].mean()), 2),
            "avg_attendance": round(float(subset["Attendance_Rate (%)"].mean()), 2),
            "avg_stress": round(float(subset["Stress_Level"].mean()), 2),
            "avg_api": round(float(subset["Academic_Performance_Index"].mean()), 2),
            "avg_hrv": round(float(subset["Heart_Rate_Variability"].mean()), 2)
        }

    # Assemble summary payload
    summary_payload = {
        "project": "Analysing Mental Health in Student Ecosystem",
        "dataset_metadata": {
            "source": "Google Sheets (Verified Internship Deliverable Dataset)",
            "source_url": SOURCE_URL,
            "rows": total_records,
            "columns": total_cols,
            "unique_student_ids": unique_ids,
            "duplicates": duplicates,
            "null_values_count": sum(null_counts.values()),
            "privacy_notice": "Student emotional journal entries and individual row records are aggregated for student privacy."
        },
        "kpis": kpis,
        "distributions": {
            "gender": gender_dist,
            "mental_health_risk": risk_dist,
            "age_groups": age_group_dist,
            "interventions": intervention_dist
        },
        "gender_breakdown": gender_metrics,
        "study_vs_performance": study_vs_perf,
        "risk_breakdown": risk_metrics
    }

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(summary_payload, f, indent=2)

    print(f"[SUCCESS] Wrote verified aggregate summary to {OUTPUT_PATH}")

if __name__ == "__main__":
    analyze()
