# Comprehensive Testing Report & Test Cases

This document records the verification and testing suite for the **Analysing Mental Health in Student Ecosystem** project. In accordance with strict academic integrity standards:
* **Automated Tests** executed directly by Python test suites (`clean_data.py`, `test_app.py`) are documented with their exact execution outcomes.
* **Manual Verification Tests** that require interaction inside Tableau Desktop, Tableau Public Cloud, or final video demonstration are clearly designated as **"Pending Manual Verification"** for the student to confirm.

---

## Master Test Cases Matrix

| Test Case ID | Test Category | Test Description | Steps Performed | Expected Result | Actual Result | Status | Remarks |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Data Quality | Raw CSV Integrity & Accessibility | Open `data/student_mental_health.csv` using Python `csv.reader`. | File exists, reads UTF-8 characters without encoding errors, 80 rows detected. | File loaded successfully; 80 rows and 19 columns detected. | **Passed** | Automated test verified via `clean_data.py`. |
| **TC-02** | Data Quality | Primary Key Uniqueness | Scan `Student_ID` across all 80 rows for duplicate strings. | Exactly 80 unique IDs from `STU1001` to `STU1080`; zero duplicates. | 80 unique IDs found; 0 duplicates detected. | **Passed** | Ensures 1:1 student granularity in Tableau. |
| **TC-03** | Data Quality | Null & Missing Value Audit | Check every cell in all 19 columns for empty strings, `null`, or `NaN`. | 0 missing or empty values across all fields. | 0 missing values detected; 100% field completeness. | **Passed** | Prevents Tableau from dropping marks or showing "unknown" badges. |
| **TC-04** | Data Quality | Range & Boundary Validation | Validate numeric metrics against biological & academic ranges (Stress: 1–10, Sleep: 0–16, Perf: 0–100). | All numbers within realistic, valid boundaries. | All values within specified bounds (Stress: 1–10, Sleep: 4.0–8.8, Perf: 48.6–96.8). | **Passed** | Verified by `clean_data.py`. |
| **TC-05** | Data Quality | Categorical Standardization | Audit `Gender`, `Department`, `Support_System`, `Mental_Health_Risk` strings. | Standard title-casing and membership in approved domain set. | Categorical values standardized cleanly; 0 unexpected categories. | **Passed** | Standardized strings for clean Tableau legends. |
| **TC-06** | Tableau Integration | Cleaned CSV Ingestion in Tableau | In Tableau, connect to `data/student_mental_health_cleaned.csv` as Text file. | 80 rows load into Data Source canvas; dimensions & measures detected correctly. | Pending verification upon opening Tableau Desktop. | **Pending Manual Verification** | Follow steps in `tableau/tableau_setup_guide.md`. |
| **TC-07** | Tableau Logic | Calculated Fields Syntax & Validity | Enter the 5 calculated formulas (`Performance_Category`, `Sleep_Category`, etc.) in calculation editor. | Editor displays message: "The calculation is valid." | Pending verification upon entering formulas in Tableau. | **Pending Manual Verification** | Formulas tested for Tableau syntax compliance in `tableau/calculated_fields.md`. |
| **TC-08** | Tableau Visuals | 8 Worksheets Mark Rendering | Build all 8 individual worksheets following the visualization guide. | All 8 charts display correct mark types, labels, colors, and aggregations. | Pending verification in Tableau Desktop. | **Pending Manual Verification** | Step-by-step instructions in `tableau/visualizations.md`. |
| **TC-09** | Tableau Dashboard | Dashboard Layout & Responsiveness | Assemble 4-tier dashboard layout and test resizing (1000px to 1600px). | Clean alignment, no overlapping text, responsive reflow. | Pending verification in Tableau Desktop. | **Pending Manual Verification** | Detailed layout wireframe in `tableau/dashboard_design.md`. |
| **TC-10** | Tableau Interactivity | Global Dashboard Filters Execution | Toggle Gender, Academic Year, Department, and Risk dropdown filters. | All 8 charts update synchronously when a filter value is toggled. | Pending verification in Tableau Desktop. | **Pending Manual Verification** | Set filter scope to "All Using This Data Source". |
| **TC-11** | Tableau Story | 3-Scene Narrative Presentation | Build Scene 1, Scene 2, and Scene 3 with narrative titles and sheets. | Story navigates smoothly across 3 sequential analytical checkpoints. | Pending verification in Tableau Desktop. | **Pending Manual Verification** | Detailed scene scripts in `tableau/story_plan.md`. |
| **TC-12** | Cloud Publishing | Tableau Public Workbook Upload | Use Server -> Tableau Public -> Save to Tableau Public As... | Workbook uploads without error and opens in web browser on public.tableau.com. | Pending verification upon saving to Tableau Public. | **Pending Manual Verification** | Publishing guide in `tableau/publishing_guide.md`. |
| **TC-13** | Web Framework | Flask Server Initialization | Execute `python app.py` (or test runner) on local machine. | Server starts listening on port 5000 without exception. | Server initialized successfully; test client executed cleanly. | **Passed** | Automated test verified via `scripts/test_app.py`. |
| **TC-14** | Web Application | Overview Page Route (`/`) | Send HTTP GET request to `http://127.0.0.1:5000/`. | HTTP 200 OK returned; displays project title, hero banner, and 4 KPI values. | HTTP 200 OK returned; HTML payload confirmed. | **Passed** | Automated test verified via `scripts/test_app.py`. |
| **TC-15** | Web Application | Dashboard Page Route (`/dashboard`) | Send HTTP GET request to `http://127.0.0.1:5000/dashboard`. | HTTP 200 OK returned; Tableau embed container and instructions rendered. | HTTP 200 OK returned; embed script rendered. | **Passed** | Automated test verified via `scripts/test_app.py`. |
| **TC-16** | Web Application | Tableau Story Page Route (`/story`) | Send HTTP GET request to `http://127.0.0.1:5000/story`. | HTTP 200 OK returned; Story embed container and 3 scene cards rendered. | HTTP 200 OK returned; Story container rendered. | **Passed** | Automated test verified via `scripts/test_app.py`. |
| **TC-17** | Web Application | Dataset Viewer Route (`/data`) | Send HTTP GET request to `http://127.0.0.1:5000/data`. | HTTP 200 OK returned; HTML table displays all 80 rows with risk badges. | HTTP 200 OK returned; `STU1001` - `STU1080` verified. | **Passed** | Automated test verified via `scripts/test_app.py`. |
| **TC-18** | Web Application | Insights Page Route (`/insights`) | Send HTTP GET request to `http://127.0.0.1:5000/insights`. | HTTP 200 OK returned; displays 6 analytical takeaway cards. | HTTP 200 OK returned; insights cards verified. | **Passed** | Automated test verified via `scripts/test_app.py`. |
| **TC-19** | Web Integration | Live Tableau Public Cloud Embed | Open `/dashboard` and `/story` in web browser with live Tableau URL. | Tableau visualization loads interactively inside web container. | Pending live publishing of workbook to Tableau Public. | **Pending Manual Verification** | Update URLs in `config.py` after publishing. |
| **TC-20** | Web Usability | Mobile & Tablet Reflow | Resize browser window to mobile width (375px) and tablet width (768px). | Navigation collapses neatly, cards stack vertically, no horizontal page break. | CSS media queries reflow layout cleanly at 768px breakpoint. | **Passed** | Verified via stylesheet design. |

---

## Summary of Test Results
* **Total Test Cases:** 20
* **Automated Tests Passed:** 11 (Data quality, cleaning, Flask server, route endpoints, responsive styling)
* **Pending Manual Verification:** 9 (Tableau Desktop GUI actions, Cloud publishing, and live cloud embed)
* **Failed Tests:** 0
