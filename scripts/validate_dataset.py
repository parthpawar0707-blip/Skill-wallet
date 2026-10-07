"""
validate_dataset.py
-------------------
Reproducible data validation script for the 'Analysing Mental Health in Student Ecosystem' project.
Performs end-to-end data integrity, schema consistency, null/blank audit,
primary key uniqueness, and physiological/academic domain range audits.
Compatible with Python 3.8+ using only standard library modules.
"""

import csv
import os
import sys

DATASET_PATH = os.path.join("data", "student_mental_health.csv")

EXPECTED_FIELDS = [
    "Student_ID", "Age", "Gender", "Academic_Year", "Department",
    "Study_Hours", "Sleep_Hours", "Screen_Time", "Social_Interaction_Hours",
    "Physical_Activity_Hours", "Stress_Level", "Anxiety_Level", "Depression_Level",
    "Mood_Score", "Academic_Performance", "Attendance_Percentage",
    "Heart_Rate_Variability", "Support_System", "Mental_Health_Risk"
]

NUMERIC_BOUNDS = {
    "Age": (16, 30),
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

VALID_CATEGORIES = {
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

def run_validation():
    print("=" * 70)
    print("REPRODUCIBLE DATASET AUDIT & INTEGRITY VERIFICATION")
    print("Project: Analysing Mental Health in Student Ecosystem")
    print("=" * 70)

    if not os.path.exists(DATASET_PATH):
        print(f"[FAIL] Dataset file not found at: {DATASET_PATH}")
        sys.exit(1)

    print(f"[OK] Located dataset at: {DATASET_PATH}")
    file_size_bytes = os.path.getsize(DATASET_PATH)
    print(f"[INFO] File size: {file_size_bytes} bytes")

    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames

        print(f"[INFO] Total columns: {len(headers)}")
        if headers != EXPECTED_FIELDS:
            print("[WARN] Column ordering differs from baseline canonical order:")
            print("  Found:   ", headers)
            print("  Expected:", EXPECTED_FIELDS)
        else:
            print("[OK] Exact canonical schema header match (19/19 fields).")

        rows = list(reader)

    total_rows = len(rows)
    print(f"[INFO] Total data records (excluding header): {total_rows}")

    errors = 0
    warnings = 0
    seen_ids = set()
    category_counts = {col: {} for col in VALID_CATEGORIES}
    numeric_min_max = {col: [float("inf"), float("-inf"), 0.0] for col in NUMERIC_BOUNDS}

    for idx, row in enumerate(rows, start=1):
        # 1. Primary key check
        sid = row.get("Student_ID", "").strip()
        if not sid:
            print(f"[Row {idx}] ERROR: Blank Student_ID")
            errors += 1
        elif sid in seen_ids:
            print(f"[Row {idx}] ERROR: Duplicate Student_ID: {sid}")
            errors += 1
        else:
            seen_ids.add(sid)

        # 2. Null/blank check across all columns
        for col in headers:
            raw_val = row.get(col, "")
            if raw_val is None or raw_val.strip() == "":
                print(f"[Row {idx}] ERROR: Null or empty value in column '{col}'")
                errors += 1

        # 3. Categorical distribution and validity
        for cat_col, valid_set in VALID_CATEGORIES.items():
            val = row.get(cat_col, "").strip()
            if val not in valid_set:
                print(f"[Row {idx}] WARNING: Non-standard category '{val}' in '{cat_col}'")
                warnings += 1
            category_counts[cat_col][val] = category_counts[cat_col].get(val, 0) + 1

        # 4. Numeric range validation
        for num_col, (low_b, high_b) in NUMERIC_BOUNDS.items():
            raw_str = row.get(num_col, "").strip()
            try:
                num_val = float(raw_str)
                if num_val < low_b or num_val > high_b:
                    print(f"[Row {idx}] WARNING: {num_col} value {num_val} outside [{low_b}, {high_b}]")
                    warnings += 1
                if num_val < numeric_min_max[num_col][0]:
                    numeric_min_max[num_col][0] = num_val
                if num_val > numeric_min_max[num_col][1]:
                    numeric_min_max[num_col][1] = num_val
                numeric_min_max[num_col][2] += num_val
            except ValueError:
                print(f"[Row {idx}] ERROR: Non-numeric value '{raw_str}' in '{num_col}'")
                errors += 1

    print("\n" + "-" * 70)
    print("NUMERICAL MEASURE BOUNDS & SUMMARY:")
    print("-" * 70)
    for col, (min_v, max_v, sum_v) in numeric_min_max.items():
        avg_v = sum_v / total_rows if total_rows else 0
        print(f"  {col:<26}: Min={min_v:<5} Max={max_v:<5} Mean={avg_v:.2f}")

    print("\n" + "-" * 70)
    print("CATEGORICAL ATTRIBUTE DISTRIBUTIONS:")
    print("-" * 70)
    for cat_col, counts in category_counts.items():
        print(f"  [{cat_col}]")
        for k, v in counts.items():
            print(f"    - {k:<25}: {v} students ({v / total_rows * 100:.1f}%)")

    print("\n" + "=" * 70)
    print("VALIDATION RESULT SUMMARY:")
    print(f"  Rows evaluated     : {total_rows}")
    print(f"  Unique Student IDs : {len(seen_ids)}")
    print(f"  Critical errors    : {errors}")
    print(f"  Range warnings     : {warnings}")
    print("=" * 70)

    if errors == 0:
        print("[SUCCESS] Dataset passes all structural integrity and completeness checks.")
        print("[READY] Dataset is 100% prepared and ready for Tableau connection.")
        return 0
    else:
        print("[FAILURE] Dataset contains critical integrity errors.")
        return 1

if __name__ == "__main__":
    sys.exit(run_validation())
