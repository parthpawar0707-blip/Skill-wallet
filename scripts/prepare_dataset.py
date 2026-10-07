"""
prepare_dataset.py
------------------
Reproducible data preparation script for 'Analysing Mental Health in Student Ecosystem'.
Audits, cleans, validates, and prepares the dataset deterministically from raw data
(data/student_mental_health.csv) to analysis-ready data (data/student_mental_health_cleaned.csv)
for Tableau Desktop / Tableau Public.
"""

import csv
import os
import sys

RAW_DATA_PATH = os.path.join("data", "student_mental_health.csv")
CLEANED_DATA_PATH = os.path.join("data", "student_mental_health_cleaned.csv")

EXPECTED_COLUMNS = [
    "Student_ID", "Age", "Gender", "Academic_Year", "Department",
    "Study_Hours", "Sleep_Hours", "Screen_Time", "Social_Interaction_Hours",
    "Physical_Activity_Hours", "Stress_Level", "Anxiety_Level", "Depression_Level",
    "Mood_Score", "Academic_Performance", "Attendance_Percentage",
    "Heart_Rate_Variability", "Support_System", "Mental_Health_Risk"
]

NUMERIC_RULES = {
    "Age": {"type": int, "min": 16, "max": 30},
    "Study_Hours": {"type": float, "min": 0.0, "max": 16.0, "round": 1},
    "Sleep_Hours": {"type": float, "min": 0.0, "max": 16.0, "round": 1},
    "Screen_Time": {"type": float, "min": 0.0, "max": 24.0, "round": 1},
    "Social_Interaction_Hours": {"type": float, "min": 0.0, "max": 16.0, "round": 1},
    "Physical_Activity_Hours": {"type": float, "min": 0.0, "max": 12.0, "round": 1},
    "Stress_Level": {"type": int, "min": 1, "max": 10},
    "Anxiety_Level": {"type": int, "min": 1, "max": 10},
    "Depression_Level": {"type": int, "min": 1, "max": 10},
    "Mood_Score": {"type": int, "min": 1, "max": 10},
    "Academic_Performance": {"type": float, "min": 0.0, "max": 100.0, "round": 1},
    "Attendance_Percentage": {"type": float, "min": 0.0, "max": 100.0, "round": 1},
    "Heart_Rate_Variability": {"type": float, "min": 10.0, "max": 150.0, "round": 1}
}

CATEGORICAL_RULES = {
    "Gender": {"Male", "Female", "Non-Binary"},
    "Academic_Year": {"1st Year", "2nd Year", "3rd Year", "4th Year"},
    "Department": {
        "Computer Science",
        "Mechanical Engineering",
        "Electronics & Comm",
        "Business Administration",
        "Humanities & Arts"
    },
    "Support_System": {"None", "Family", "Friends", "Counselor", "Multiple"},
    "Mental_Health_Risk": {"Low", "Medium", "High"}
}

def prepare_data():
    print("=" * 70)
    print("DATA PREPARATION PIPELINE: ANALYSING MENTAL HEALTH IN STUDENT ECOSYSTEM")
    print("=" * 70)

    if not os.path.exists(RAW_DATA_PATH):
        print(f"[ERROR] Raw dataset not found at '{RAW_DATA_PATH}'")
        sys.exit(1)

    with open(RAW_DATA_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        raw_rows = list(reader)

    print(f"[INFO] Raw records loaded: {len(raw_rows)}")
    print(f"[INFO] Columns detected: {len(headers)}")

    if headers != EXPECTED_COLUMNS:
        print("[WARNING] Headers deviate from canonical schema ordering.")

    cleaned_records = []
    seen_ids = set()
    errors = 0
    modifications = 0

    for idx, row in enumerate(raw_rows, start=1):
        cleaned_row = {}

        # 1. Primary Key: Student_ID
        sid = row.get("Student_ID", "").strip()
        if not sid:
            print(f"[Row {idx}] Critical Error: Missing Student_ID")
            errors += 1
            continue
        if sid in seen_ids:
            print(f"[Row {idx}] Critical Error: Duplicate Student_ID '{sid}'")
            errors += 1
            continue
        seen_ids.add(sid)
        cleaned_row["Student_ID"] = sid

        # 2. Categorical Fields with whitespace trimming and casing standardization
        for cat_col, valid_set in CATEGORICAL_RULES.items():
            val = row.get(cat_col, "").strip()
            # Normalize title case for single words
            normalized = val.title() if " " not in val else val
            if normalized not in valid_set:
                print(f"[Row {idx}] Warning: Invalid category '{val}' for '{cat_col}'")
                errors += 1
            cleaned_row[cat_col] = normalized

        # 3. Numeric Fields
        for num_col, rules in NUMERIC_RULES.items():
            raw_val = row.get(num_col, "").strip()
            try:
                num = float(raw_val)
                if not (rules["min"] <= num <= rules["max"]):
                    print(f"[Row {idx}] Warning: {num_col}={num} out of bounds [{rules['min']}, {rules['max']}]")
                    errors += 1
                if rules["type"] == int:
                    cleaned_row[num_col] = int(round(num))
                else:
                    cleaned_row[num_col] = round(num, rules.get("round", 1))
            except ValueError:
                print(f"[Row {idx}] Critical Error: Non-numeric '{raw_val}' in {num_col}")
                errors += 1

        cleaned_records.append(cleaned_row)

    if errors > 0:
        print(f"[FAILURE] Data preparation encountered {errors} critical errors. Aborting.")
        sys.exit(1)

    # Deterministically order columns according to expected schema
    ordered_records = []
    for r in cleaned_records:
        ordered_row = {col: r[col] for col in EXPECTED_COLUMNS}
        ordered_records.append(ordered_row)

    # Write cleaned dataset
    os.makedirs(os.path.dirname(CLEANED_DATA_PATH), exist_ok=True)
    with open(CLEANED_DATA_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=EXPECTED_COLUMNS)
        writer.writeheader()
        writer.writerows(ordered_records)

    print(f"\n[SUCCESS] Deterministically prepared {len(ordered_records)} clean records.")
    print(f" -> Output: {CLEANED_DATA_PATH}")
    print("=" * 70)

if __name__ == "__main__":
    prepare_data()
