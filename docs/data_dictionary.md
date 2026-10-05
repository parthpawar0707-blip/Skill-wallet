# Data Dictionary: Student Mental Health Dataset

## Overview
This document describes the schema, structure, and attributes of the `student_mental_health.csv` and `student_mental_health_cleaned.csv` datasets. The dataset contains **80 individual student records** specifically modeled to analyze the multi-dimensional relationships between lifestyle habits, physiological stress indicators, academic engagement, and psychological well-being in an undergraduate/graduate collegiate environment.

---

## Domain Group Categorization

To facilitate structured analytics and dashboard reporting in Tableau, the 19 attributes are organized into five logical categories:

1. **Demographics**: Contextual personal attributes (`Student_ID`, `Age`, `Gender`, `Academic_Year`, `Department`).
2. **Lifestyle & Habits**: Daily time allocations influencing circadian rhythm and health (`Study_Hours`, `Sleep_Hours`, `Screen_Time`, `Social_Interaction_Hours`, `Physical_Activity_Hours`).
3. **Psychological & Physiological Indicators**: Clinical/subjective mental health ratings and biometric measures (`Stress_Level`, `Anxiety_Level`, `Depression_Level`, `Mood_Score`, `Heart_Rate_Variability`).
4. **Academic Performance**: Institutional engagement metrics (`Academic_Performance`, `Attendance_Percentage`).
5. **Support & Clinical Risk Assessment**: Social buffer and holistic risk tier (`Support_System`, `Mental_Health_Risk`).

---

## Detailed Field Definitions

| Field Name | Group | Data Type | Tableau Role | Example Value | Allowed Range / Domain | Why It Is Useful |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Student_ID** | Demographic | String (Text) | Dimension (Identifier) | `STU1001` | Unique string (`STU1001` - `STU1080`) | Primary key; ensures granularity at the student level and enables scatter plot mark separation. |
| **Age** | Demographic | Integer (Whole Number) | Dimension / Measure | `20` | 18 – 24 | Evaluates whether mental distress varies as students advance from adolescence into early adulthood. |
| **Gender** | Demographic | String (Text) | Dimension | `Female` | `Male`, `Female`, `Non-Binary` | Facilitates comparative disparity analysis in reported depression and stress coping tendencies. |
| **Academic_Year** | Demographic | String (Text) | Dimension | `2nd Year` | `1st Year`, `2nd Year`, `3rd Year`, `4th Year` | Segregates freshman transition stress from senior graduation/placement anxiety. |
| **Department** | Demographic | String (Text) | Dimension | `Computer Science` | `Computer Science`, `Mechanical Engineering`, `Electronics & Comm`, `Business Administration`, `Humanities & Arts` | Identifies departmental curricula workloads and high-risk academic disciplines. |
| **Study_Hours** | Lifestyle | Decimal (Float) | Measure | `5.5` | 1.0 – 10.0 hrs/day | Quantifies daily curricular investment; tests whether excessive study causes academic diminishing returns. |
| **Sleep_Hours** | Lifestyle | Decimal (Float) | Measure | `6.8` | 3.5 – 10.0 hrs/day | Key physiological recovery metric; critical for understanding sleep deprivation and emotional dysregulation. |
| **Screen_Time** | Lifestyle | Decimal (Float) | Measure | `6.2` | 2.0 – 12.0 hrs/day | Quantifies digital overload, smartphone fatigue, and social media exposure. |
| **Social_Interaction_Hours** | Lifestyle | Decimal (Float) | Measure | `2.5` | 0.5 – 6.0 hrs/day | Assesses interpersonal connectivity and isolation mitigation. |
| **Physical_Activity_Hours** | Lifestyle | Decimal (Float) | Measure | `1.2` | 0.0 – 4.0 hrs/day | Tracks endorphin-producing cardiovascular/gym exercise acting as an anti-stress buffer. |
| **Stress_Level** | Mental Health | Integer (Whole Number) | Measure | `6` | 1 (Minimum) – 10 (Severe) | Quantifies subjective perceived pressure, cognitive overload, and academic burnout. |
| **Anxiety_Level** | Mental Health | Integer (Whole Number) | Measure | `5` | 1 (Minimum) – 10 (Severe) | Measures acute apprehension, nervousness, and panic symptoms in academic situations. |
| **Depression_Level** | Mental Health | Integer (Whole Number) | Measure | `4` | 1 (Minimum) – 10 (Severe) | Measures feelings of persistent sadness, loss of interest, fatigue, and low motivation. |
| **Mood_Score** | Mental Health | Integer (Whole Number) | Measure | `7` | 1 (Extremely Low) – 10 (Positive/Optimistic) | Inverted emotional well-being indicator; acts as a check against self-reported depressive tendencies. |
| **Academic_Performance** | Academic | Decimal (Float) | Measure | `82.4` | 0.0 – 100.0 (%) | Quantitative cumulative academic achievement score (equivalent to GPA percentage). |
| **Attendance_Percentage** | Academic | Decimal (Float) | Measure | `88.5` | 0.0 – 100.0 (%) | Tracks physical/virtual class attendance; proxy for student motivation and functional presence. |
| **Heart_Rate_Variability** | Physiological | Decimal (Float) | Measure | `58.4` | 25.0 – 95.0 ms | Root mean square of successive differences (RMSSD) in millisecond time. High HRV (>60 ms) = parasympathetic health; low HRV (<45 ms) = autonomic strain. |
| **Support_System** | Support | String (Text) | Dimension | `Friends` | `Family`, `Friends`, `Counselor`, `Multiple`, `None` | Identifies interpersonal scaffolding available to the student during academic crises. |
| **Mental_Health_Risk** | Risk | String (Text) | Dimension | `Medium` | `Low`, `Medium`, `High` | Clinically calibrated composite risk tier derived from combined stress, anxiety, depression, and biometric markers. |

---

## Data Summary & Baseline Benchmarks (Cleaned Dataset)

- **Total Records:** 80
- **Total Attributes:** 19
- **Mean Study Hours:** 5.09 hrs/day
- **Mean Sleep Hours:** 6.60 hrs/day
- **Mean Stress Level:** 4.95 / 10
- **Mean Academic Score:** 80.50%
- **Mean HRV:** 55.84 ms
- **Risk Segmentation:**
  - `Low`: 29 students (36.25%)
  - `Medium`: 39 students (48.75%)
  - `High`: 12 students (15.00%)
