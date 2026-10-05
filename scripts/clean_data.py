"""
clean_data.py
Simple and robust data validation and cleaning script for the Student Mental Health project.
Uses Python standard libraries only (no external packages required).
"""

import csv
import os
import sys

RAW_DATA_PATH = os.path.join("data", "student_mental_health.csv")
CLEANED_DATA_PATH = os.path.join("data", "student_mental_health_cleaned.csv")

VALID_GENDERS = {"Male", "Female", "Non-Binary"}
VALID_YEARS = {"1st Year", "2nd Year", "3rd Year", "4th Year"}
VALID_RISKS = {"Low", "Medium", "High"}
VALID_SUPPORTS = {"None", "Family", "Friends", "Counselor", "Multiple"}

def clean_and_validate():
    print("=" * 60)
    print("STUDENT MENTAL HEALTH DATASET: VALIDATION & CLEANING")
    print("=" * 60)

    if not os.path.exists(RAW_DATA_PATH):
        print(f"Error: Raw dataset not found at '{RAW_DATA_PATH}'")
        sys.exit(1)

    cleaned_records = []
    seen_ids = set()
    errors_found = 0
    warnings_found = 0

    with open(RAW_DATA_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        print(f"Input Fields ({len(fields)}): {', '.join(fields)}")
        
        row_idx = 0
        for row in reader:
            row_idx += 1
            cleaned_row = {}
            
            # 1. Clean & validate Student_ID
            raw_id = row.get("Student_ID", "").strip()
            if not raw_id:
                print(f"[Row {row_idx}] ERROR: Missing Student_ID")
                errors_found += 1
                continue
            if raw_id in seen_ids:
                print(f"[Row {row_idx}] ERROR: Duplicate Student_ID: {raw_id}")
                errors_found += 1
                continue
            seen_ids.add(raw_id)
            cleaned_row["Student_ID"] = raw_id

            # 2. Clean & validate Demographic fields
            try:
                age = int(float(row.get("Age", 0)))
                if not (16 <= age <= 30):
                    print(f"[Row {row_idx}] WARNING: Age out of typical student range: {age}")
                    warnings_found += 1
                cleaned_row["Age"] = age
            except ValueError:
                print(f"[Row {row_idx}] ERROR: Invalid Age: {row.get('Age')}")
                errors_found += 1

            gender = row.get("Gender", "").strip().title()
            if gender not in VALID_GENDERS:
                gender = "Other"
            cleaned_row["Gender"] = gender

            cleaned_row["Academic_Year"] = row.get("Academic_Year", "").strip()
            cleaned_row["Department"] = row.get("Department", "").strip()

            # 3. Clean & validate Numeric Lifestyle & Metric fields
            numeric_fields = {
                "Study_Hours": (0.0, 16.0),
                "Sleep_Hours": (0.0, 16.0),
                "Screen_Time": (0.0, 24.0),
                "Social_Interaction_Hours": (0.0, 16.0),
                "Physical_Activity_Hours": (0.0, 12.0),
                "Stress_Level": (1, 10),
                "Anxiety_Level": (1, 10),
                "Depression_Level": (1, 10),
                "Mood_Score": (1, 10),
                "Academic_Performance": (0.0, 100.0),
                "Attendance_Percentage": (0.0, 100.0),
                "Heart_Rate_Variability": (10.0, 150.0)
            }

            for field_name, (min_v, max_v) in numeric_fields.items():
                val_str = row.get(field_name, "").strip()
                try:
                    val = float(val_str)
                    if not (min_v <= val <= max_v):
                        print(f"[Row {row_idx}] WARNING: {field_name} value {val} outside standard bounds [{min_v}, {max_v}]")
                        warnings_found += 1
                    # Format integer levels as integers, continuous metrics as 1 decimal place
                    if field_name in ["Stress_Level", "Anxiety_Level", "Depression_Level", "Mood_Score"]:
                        cleaned_row[field_name] = int(round(val))
                    else:
                        cleaned_row[field_name] = round(val, 1)
                except ValueError:
                    print(f"[Row {row_idx}] ERROR: Non-numeric value for {field_name}: '{val_str}'")
                    errors_found += 1

            # 4. Clean & validate Categorical fields
            support = row.get("Support_System", "").strip().title()
            cleaned_row["Support_System"] = support if support in VALID_SUPPORTS else "Other"

            risk = row.get("Mental_Health_Risk", "").strip().title()
            cleaned_row["Mental_Health_Risk"] = risk if risk in VALID_RISKS else "Medium"

            cleaned_records.append(cleaned_row)

    print(f"\nProcessing summary:")
    print(f"- Total rows processed: {row_idx}")
    print(f"- Valid unique records: {len(cleaned_records)}")
    print(f"- Errors encountered:   {errors_found}")
    print(f"- Warnings encountered: {warnings_found}")

    if errors_found > 0:
        print("\nData cleaning halted due to critical errors. Please resolve errors.")
        sys.exit(1)

    # Save cleaned data
    os.makedirs(os.path.dirname(CLEANED_DATA_PATH), exist_ok=True)
    with open(CLEANED_DATA_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(cleaned_records)

    print(f"\nSuccessfully wrote {len(cleaned_records)} cleaned records to:")
    print(f" -> {CLEANED_DATA_PATH}")

    # Compute quick verification statistics
    avg_study = sum(r["Study_Hours"] for r in cleaned_records) / len(cleaned_records)
    avg_sleep = sum(r["Sleep_Hours"] for r in cleaned_records) / len(cleaned_records)
    avg_stress = sum(r["Stress_Level"] for r in cleaned_records) / len(cleaned_records)
    avg_perf = sum(r["Academic_Performance"] for r in cleaned_records) / len(cleaned_records)
    avg_hrv = sum(r["Heart_Rate_Variability"] for r in cleaned_records) / len(cleaned_records)

    risk_counts = {}
    for r in cleaned_records:
        rc = r["Mental_Health_Risk"]
        risk_counts[rc] = risk_counts.get(rc, 0) + 1

    print("\n" + "=" * 60)
    print("KEY METRIC BENCHMARKS FOR TABLEAU KPI VALIDATION:")
    print(f"- Total Students:             {len(cleaned_records)}")
    print(f"- Average Study Hours:        {avg_study:.2f} hrs/day")
    print(f"- Average Sleep Hours:        {avg_sleep:.2f} hrs/day")
    print(f"- Average Stress Level:       {avg_stress:.2f} / 10")
    print(f"- Average Academic Score:     {avg_perf:.2f}%")
    print(f"- Average HRV (ms):           {avg_hrv:.2f} ms")
    print(f"- Mental Health Risk Breakdown: {risk_counts}")
    print("=" * 60)

if __name__ == "__main__":
    clean_and_validate()
