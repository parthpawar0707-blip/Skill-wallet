# Tableau Dashboard Design & Layout Guide

## Dashboard Title
**"Student Mental Health & Academic Well-Being Dashboard"**

---

## Dashboard Architecture & Layout Wireframe

The dashboard is structured into an executive, modular 4-tier grid with consistent margins, modern hierarchy, and intuitive interactive filtering:

```
+---------------------------------------------------------------------------------------------------+
|  [HEADER BANNER]  Student Mental Health & Academic Well-Being Dashboard                           |
|  Interactive Analytics for University Student Support & Wellness Monitoring                       |
+---------------------------------------------------------------------------------------------------+
|  [FILTERS BAR]  Gender: [All] | Academic Year: [All] | Department: [All] | Mental Health Risk: [All]|
+---------------------------------------------------------------------------------------------------+
|  [KPI SUMMARY CARDS] (Viz 6)                                                                      |
|  [ Total Students: 80 ]  [ Avg Stress: 4.95 ]  [ Avg Sleep: 6.60 hrs ]  [ Avg Academic: 80.5% ]   |
+---------------------------------------------------------------------------------------------------+
|  [MIDDLE ROW: Primary Behavioral Correlations]                                                    |
|  +------------------------------------+---------------------------------+-------------------------+
|  | Viz 3: Study Hours vs Academic     | Viz 4: Average Stress Level     | Viz 7: Mental Risk      |
|  | Performance (Scatter Plot with     | by Gender (Bar Chart)           | Distribution (Donut)    |
|  | Trendline & Risk Color Marks)      |                                 |                         |
|  +------------------------------------+---------------------------------+-------------------------+
+---------------------------------------------------------------------------------------------------+
|  [BOTTOM ROW: In-Depth Diagnostic Breakdown]                                                      |
|  +------------------------------------+---------------------------------+-------------------------+
|  | Viz 2: Depression Level Across     | Viz 5: Heart Rate Variability   | Viz 8: Academic Grade   |
|  | Gender Cohorts (Bar Chart)         | Analysis by Risk Tier (HRV)     | Breakdown (Bar Chart)   |
|  +------------------------------------+---------------------------------+-------------------------+
```

---

## Sizing & Responsive Design Configuration

To ensure your dashboard displays cleanly across college lab monitors, laptop screens, and web browser embeds:

1. In the bottom-left corner of Tableau, click the **New Dashboard** icon (the icon with a grid of 4 squares).
2. Look at the left sidebar under the **Dashboard** pane -> find **Size**.
3. Click the dropdown arrow on Size.
4. Select **Range** (or **Automatic**):
   * **Minimum:** `Width: 1000px`, `Height: 800px`
   * **Maximum:** `Width: 1600px`, `Height: 1050px`
   *(Alternatively, selecting **Automatic** will dynamically adapt to any browser window size on Tableau Public).*

---

## Step-by-Step Dashboard Assembly Instructions

### Step 1: Add Containers & Title Banner
1. Under **Objects** in the bottom left, check the option for **Tiled** (simplest and cleanest for beginners).
2. Drag a **Vertical** layout container onto the blank canvas.
3. Drag a **Text** object to the very top.
   * Enter Title: `Student Mental Health & Academic Well-Being Dashboard`
   * Format: Bold, 20pt, Dark Slate Blue (`#1a2a44`), Centered.
   * Enter Subtitle: `Holistic Analysis of Lifestyle, Physiological Stress, and Academic Performance Across Student Ecosystems` (Regular, 11pt, Gray `#555555`).

### Step 2: Add Global Filters Bar
1. Drag a **Horizontal** container immediately below the title banner.
2. From the Sheets list, temporarily drag `Viz 3 - Study Hours vs Academic Performance` into the dashboard.
3. Click the small downward arrow on the top right of the Viz 3 sheet frame -> select **Filters** -> check:
   * `Gender`
   * `Academic_Year`
   * `Department`
   * `Mental_Health_Risk`
4. For each filter card that appears:
   * Click its top-right arrow -> change display type to **Multiple Values (Dropdown)**.
   * Click the arrow again -> select **Apply to Worksheets** -> **All Using This Data Source**. (This ensures that toggling any filter updates ALL charts across the entire dashboard!).
5. Drag each filter dropdown side-by-side into the horizontal container below the title banner.

### Step 3: Insert KPI Summary Cards (Viz 6)
1. Drag `Viz 6 - KPI Overview Cards` directly below the filter bar.
2. Right-click the title of Viz 6 and select **Hide Title** (the text values already provide context).
3. Adjust the height of this KPI row to approximately 80–90 pixels.

### Step 4: Insert the Middle Row of Charts
1. Drag a **Horizontal** container below the KPI row.
2. Drag `Viz 3 - Study Hours vs Academic Performance` into the left 40% of this container.
3. Drag `Viz 4 - Average Stress Level by Gender` into the middle 30%.
4. Drag `Viz 7 - Mental Risk Level Distribution` into the right 30%.

### Step 5: Insert the Bottom Row of Charts
1. Drag another **Horizontal** container below the middle row.
2. Drag `Viz 2 - Gender and Depression Level` into the left 33%.
3. Drag `Viz 5 - Analyzing Heart Rate Variability` into the middle 34%.
4. Drag `Viz 8 - Academic Performance Breakdown` into the right 33%.

### Step 6: Polish Visual Formatting & Legends
1. **Legends:** Tableau may place color legends on the far right. You can drag legends into floating positions, place them beneath their respective charts, or right-click any redundant legend and choose **Remove from Dashboard**.
2. **Padding & Borders:** Under the **Layout** tab on the far left:
   * Set outer padding on each chart container to `4px` or `6px` for clean spacing.
   * Set a light subtle border or light background (`#ffffff` with `#f4f6f9` dashboard background).
3. **Use as Filter (Interactive Highlighting):** Click the small **Funnel** icon ("Use as Filter") on `Viz 7 - Mental Risk Level Distribution`. Now, clicking any slice of the Donut/Pie chart (e.g., High Risk) automatically highlights high-risk students in all other charts!

---

## Demonstration Talking Points for the Dashboard
> *"Examiners and faculty members, this central dashboard brings together all key facets of our university wellness analytics. At the top, campus administrators get four instant KPI metrics. In the middle row, we see how daily study habits interact with mental health tiers and stress levels across genders. In the bottom row, we drill down into physiological data like Heart Rate Variability and academic grade distributions. Every filter is globally linked—if we filter down to '1st Year' students in 'Computer Science', every visual dynamically recalculates in real-time."*
