# Tableau Calculated Fields Guide

Calculated fields in Tableau allow you to create new dimensions and segmentation categories directly from raw data fields using simple logical statements (`IF ... ELSEIF ... ELSE ... END`).

---

## How to Create a Calculated Field in Tableau (Quick Steps)
1. In any worksheet, look at the **Data Pane** on the far left.
2. Click the small drop-down arrow at the top right of the Data pane (next to the search magnifying glass), OR right-click anywhere in the blank space of the Data pane.
3. Select **Create Calculated Field...**
4. A calculation editor window will appear.
5. In the top text box, enter the **Field Name**.
6. In the large code area below, copy and paste the **Exact Tableau Formula** given below.
7. Verify that the bottom of the calculation dialog displays: `The calculation is valid.`
8. Click **Apply**, then click **OK**.
9. The new calculated field will now appear in your Data pane ready for use!

---

## 1. Performance Category
* **Field Name:** `Performance_Category`
* **Purpose:** Categorizes numerical `Academic_Performance` percentages into academic grade tiers (Low, Average, Good, Excellent) for demographic segmentation.
* **Where to Use:** Visualization 8 (Academic Performance Breakdown), Dashboard filters, and tooltip details.
* **Exact Tableau Formula:**
```tableau
IF [Academic_Performance] >= 90 THEN "Excellent"
ELSEIF [Academic_Performance] >= 75 THEN "Good"
ELSEIF [Academic_Performance] >= 60 THEN "Average"
ELSE "Low"
END
```

---

## 2. Sleep Category
* **Field Name:** `Sleep_Category`
* **Purpose:** Classifies daily sleep duration based on medical sleep hygiene standards for young adults (minimum 6.0 hours recommended).
* **Where to Use:** Scene 2 of Story (Lifestyle and Mental Health), color encoding on lifestyle charts, and cross-tab analysis.
* **Exact Tableau Formula:**
```tableau
IF [Sleep_Hours] >= 7.0 THEN "Healthy (7+ hrs)"
ELSEIF [Sleep_Hours] >= 6.0 THEN "Moderate (6-7 hrs)"
ELSE "Low Sleep (<6 hrs)"
END
```

---

## 3. Stress Category
* **Field Name:** `Stress_Category`
* **Purpose:** Translates subjective 1–10 numeric stress scores into actionable clinical severity tiers.
* **Where to Use:** Color marks for Visualization 4, filter shelf, and high-risk student callout lists.
* **Exact Tableau Formula:**
```tableau
IF [Stress_Level] <= 3 THEN "Low Stress"
ELSEIF [Stress_Level] <= 6 THEN "Moderate Stress"
ELSE "High Stress"
END
```

---

## 4. Study Hours Category
* **Field Name:** `Study_Hours_Category`
* **Purpose:** Groups daily study investment into light, balanced, and heavy study loads to evaluate burnout risks.
* **Where to Use:** Visualization 1 and 3 (Study Hours vs Performance), Story Scene 2.
* **Exact Tableau Formula:**
```tableau
IF [Study_Hours] < 3.5 THEN "Light Study (<3.5 hrs)"
ELSEIF [Study_Hours] <= 6.0 THEN "Balanced Study (3.5-6 hrs)"
ELSE "Intensive Study (>6 hrs)"
END
```

---

## 5. Mental Health Risk Score (Calculated Composite)
* **Field Name:** `Calculated_Risk_Tier`
* **Purpose:** Provides a transparent formula validating the raw `Mental_Health_Risk` column based on clinical weighted factors (Stress + Anxiety + Depression).
* **Where to Use:** Performance testing verification, cross-validation against raw data, and Scene 1 of the Story.
* **Exact Tableau Formula:**
```tableau
IF ([Stress_Level] + [Anxiety_Level] + [Depression_Level]) >= 21 THEN "High Risk"
ELSEIF ([Stress_Level] + [Anxiety_Level] + [Depression_Level]) >= 13 THEN "Medium Risk"
ELSE "Low Risk"
END
```

---

## Summary of Calculated Fields Created

| Field Name | Return Type | Role | Business Value |
| :--- | :--- | :--- | :--- |
| `Performance_Category` | String | Dimension | Grade grouping for academic distribution analysis |
| `Sleep_Category` | String | Dimension | Evaluates sleep deprivation prevalence |
| `Stress_Category` | String | Dimension | Quick visual stratification of mental strain |
| `Study_Hours_Category` | String | Dimension | Correlates workload intensity with performance |
| `Calculated_Risk_Tier` | String | Dimension | Automated multi-factor psychological classification |
