# Tableau Data Connection & Setup Guide

This guide provides step-by-step, beginner-friendly instructions to connect your cleaned dataset (`student_mental_health_cleaned.csv`) to **Tableau Desktop** or the free **Tableau Public** application.

---

## Step 1: Launch Tableau
1. Open **Tableau Desktop** or **Tableau Public** from your Start Menu or Desktop shortcut.
2. When the application opens, you will see the blue **Connect** pane on the left side of the window.

---

## Step 2: Connect to the Cleaned CSV File
1. Under the **Connect** pane on the left, locate the **To a File** section.
2. Click on **Text file** (Tableau treats `.csv` files as text files).
3. A Windows File Explorer dialog will open.
4. Navigate to your project folder:
   `D:\Skill wallet\data\`
5. Select `student_mental_health_cleaned.csv` and click **Open**.

---

## Step 3: Inspect the Data Source Screen
Once the file is loaded, Tableau opens the **Data Source** tab:
1. You will see a table preview showing the first 80 rows of your dataset.
2. The data connection type in the top right will default to **Live** (this is ideal for our CSV).
3. Look at the column headers: each header has a small data-type icon just above the column name.

---

## Step 4: Verify Data Types and Roles
Verify that Tableau has correctly detected the data type for each column. If any column has the wrong icon, click the icon and change it:

| Column Name | Expected Icon | Expected Data Type in Tableau |
| :--- | :--- | :--- |
| `Student_ID` | `Abc` | String (Text) |
| `Age` | `#` (Blue or Green) | Number (Whole) |
| `Gender` | `Abc` | String (Text) |
| `Academic_Year` | `Abc` | String (Text) |
| `Department` | `Abc` | String (Text) |
| `Study_Hours` | `#` | Number (Decimal) |
| `Sleep_Hours` | `#` | Number (Decimal) |
| `Screen_Time` | `#` | Number (Decimal) |
| `Social_Interaction_Hours` | `#` | Number (Decimal) |
| `Physical_Activity_Hours` | `#` | Number (Decimal) |
| `Stress_Level` | `#` | Number (Whole) |
| `Anxiety_Level` | `#` | Number (Whole) |
| `Depression_Level` | `#` | Number (Whole) |
| `Mood_Score` | `#` | Number (Whole) |
| `Academic_Performance` | `#` | Number (Decimal) |
| `Attendance_Percentage` | `#` | Number (Decimal) |
| `Heart_Rate_Variability` | `#` | Number (Decimal) |
| `Support_System` | `Abc` | String (Text) |
| `Mental_Health_Risk` | `Abc` | String (Text) |

*(Note: If `Age` appears as a Measure, you can right-click it later in the worksheet and select **Convert to Dimension** if you wish to group students by age.)*

---

## Step 5: Check for Nulls or Missing Data
1. Scroll horizontally and vertically across the preview grid.
2. Verify that there are no blank cells or `Null` entries in any row.
3. Total row count displayed at the bottom right of the preview should read: `80 rows`.

---

## Step 6: Navigate to Your First Worksheet
1. At the very bottom-left of the Tableau window, find the orange tab labeled:
   **Sheet 1** (next to the Data Source tab).
2. Click on **Sheet 1**.
3. You are now in the Tableau Worksheet canvas:
   - The left sidebar displays your **Data** pane, divided into **Tables**:
     - Categorical attributes appear with blue icons (Dimensions).
     - Numeric attributes appear with green icons (Measures).
4. You are now fully prepared to create calculated fields and build the 8 project visualizations!
