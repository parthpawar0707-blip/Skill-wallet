# Data Cleaning and Preparation Report

## 1. Raw Data Review
The raw dataset (`data/student_mental_health.csv`) was created to reflect the socio-demographic, lifestyle, physiological, and psychological realities of college students. To simulate real-world data collection via university survey forms, biometric smart-bands (e.g., HRV monitoring), and registrar academic records, raw data needed rigorous auditing before ingestion into Tableau.

- **Initial Record Count:** 80 rows
- **Initial Column Count:** 19 fields
- **File Format:** Comma-Separated Values (CSV), UTF-8 encoded
- **Key Granularity:** Single row per unique student (`Student_ID`)

---

## 2. Duplicate Check
Ensuring uniqueness of primary keys is critical so that visual aggregation in Tableau (such as `COUNT(Student_ID)`) accurately reflects the student head count without inflated tallies.
- **Verification Rule:** Every `Student_ID` must match the format `STU1001` through `STU1080` and occur exactly once.
- **Audit Result:**
  - Evaluated: 80 rows
  - Unique IDs found: 80
  - Duplicate IDs found: **0 (Zero)**
  - Action taken: Primary key uniqueness confirmed.

---

## 3. Missing Value (Null) Check
Tableau treats missing or null values by either dropping rows from scatter plots or displaying warning badges (e.g., "1 unknown value").
- **Verification Rule:** No mandatory column may contain empty strings `""`, `NA`, `null`, or whitespace-only tokens.
- **Audit Result:**
  - `Student_ID`: 0 nulls
  - Demographic fields (`Age`, `Gender`, `Academic_Year`, `Department`): 0 nulls
  - Lifestyle measures (`Study_Hours`, `Sleep_Hours`, `Screen_Time`, `Social_Interaction_Hours`, `Physical_Activity_Hours`): 0 nulls
  - Psychological scales (`Stress_Level`, `Anxiety_Level`, `Depression_Level`, `Mood_Score`): 0 nulls
  - Academic metrics (`Academic_Performance`, `Attendance_Percentage`): 0 nulls
  - Biometric & support fields (`Heart_Rate_Variability`, `Support_System`, `Mental_Health_Risk`): 0 nulls
  - Action taken: Dataset exhibits 100% field completeness.

---

## 4. Data Type Validation
Ensured that numeric measures are cast as appropriate numeric types (integers or floats) and categorical dimensions are cast as text strings to prevent Tableau from misclassifying continuous measures as discrete strings.

| Field Name | Raw Type | Target Type | Validation Rule |
| :--- | :--- | :--- | :--- |
| `Student_ID` | String | String | Alphanumeric string |
| `Age` | String/Number | Integer | Whole number |
| `Gender` | String | String | Title-cased discrete string |
| `Academic_Year` | String | String | Discrete string |
| `Department` | String | String | Discrete string |
| `Study_Hours`, `Sleep_Hours`, `Screen_Time` | String/Float | Float | 1 decimal point precision |
| `Stress_Level`, `Anxiety_Level`, `Depression_Level`, `Mood_Score` | String/Number | Integer | Integer scales (1 to 10) |
| `Academic_Performance`, `Attendance_Percentage` | String/Float | Float | Percentage score (1 decimal) |
| `Heart_Rate_Variability` | String/Float | Float | Physiological metric in ms (1 decimal) |
| `Support_System`, `Mental_Health_Risk` | String | String | Categorical strings |

---

## 5. Range Validation & Outlier Boundaries
To ensure student profiles remain realistic, numeric fields were checked against reasonable biological and collegiate operational boundaries:

| Attribute | Verified Range in Dataset | Plausible Boundary | Status |
| :--- | :--- | :--- | :--- |
| `Age` | 18 – 24 | 16 – 30 years | Passed |
| `Study_Hours` | 2.5 – 7.5 hrs/day | 0 – 16 hrs/day | Passed |
| `Sleep_Hours` | 4.0 – 8.8 hrs/day | 3 – 14 hrs/day | Passed |
| `Screen_Time` | 2.5 – 10.5 hrs/day | 0 – 18 hrs/day | Passed |
| `Stress_Level` | 1 – 10 | 1 – 10 scale | Passed |
| `Anxiety_Level` | 1 – 10 | 1 – 10 scale | Passed |
| `Depression_Level` | 1 – 10 | 1 – 10 scale | Passed |
| `Mood_Score` | 2 – 10 | 1 – 10 scale | Passed |
| `Academic_Performance` | 48.6% – 96.8% | 0 – 100% | Passed |
| `Attendance_Percentage` | 58.0% – 97.4% | 0 – 100% | Passed |
| `Heart_Rate_Variability` | 30.1 – 83.9 ms | 20 – 120 ms | Passed |

---

## 6. Categorical Standardization
Checked for whitespace inconsistencies, case mismatches (e.g., `male` vs `Male`), and irregular category values:
- `Gender`: Standardized to `Male`, `Female`, and `Non-Binary`.
- `Support_System`: Standardized to `Family`, `Friends`, `Counselor`, `Multiple`, `None`.
- `Mental_Health_Risk`: Standardized to `Low`, `Medium`, `High`.
- `Academic_Year`: Standardized to `1st Year`, `2nd Year`, `3rd Year`, `4th Year`.

---

## 7. Final Cleaned Dataset
The final cleaned data was saved to:
`data/student_mental_health_cleaned.csv`

Summary statistics of the cleaned file:
- **Total rows:** 80 (plus 1 header row)
- **Total columns:** 19
- **Encoding:** UTF-8 without BOM (prevents Tableau column name corruption)
- **Delimiters:** Standard comma `,`

---

## 8. Why the Data is Suitable for Tableau
1. **Clean Header Row:** Clear, concise column names with no special symbols, spaces, or illegal punctuation.
2. **Deterministic Data Types:** Tableau automatically infers dimensions (`Gender`, `Department`, `Risk`) and measures (`Stress_Level`, `Academic_Performance`, `Sleep_Hours`) without manual type overrides.
3. **No Hidden NaNs or Nulls:** Prevents broken visuals or unexpected filter dropouts.
4. **Rich Inter-variable Correlations:** Allows students to construct interactive cross-filters, dual-axis charts, scatter plots with regression trendlines, and donut breakdowns seamlessly.
5. **Instantaneous Render:** At 80 rows, queries and calculations in Tableau execute in under 15 milliseconds, ensuring optimal workbook performance.
