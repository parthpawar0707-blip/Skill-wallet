# Flask Web Integration Guide

This guide walks you through setting up, running, and configuring the Flask web application that hosts and embeds your Tableau Dashboard and Story.

---

## 1. Prerequisites & System Requirements
* Python 3.9 or higher installed on your computer.
* Pip package manager.
* A modern web browser (Google Chrome, Microsoft Edge, Firefox, or Safari).

---

## 2. Virtual Environment Setup (Recommended)

Open PowerShell or Command Prompt, navigate to the project directory, and create a virtual environment:

```powershell
# Navigate to the project root
cd "D:\Skill wallet"

# Create a virtual environment named .venv
python -m venv .venv

# Activate the virtual environment on Windows
.\.venv\Scripts\Activate.ps1
```
*(If PowerShell displays an execution policy restriction, run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`, then run the activate command again).*

---

## 3. Install Dependencies

Install the required minimal dependencies from `requirements.txt`:

```powershell
pip install -r requirements.txt
```
*(Dependencies installed: `Flask>=3.0.0`)*

---

## 4. Run the Application

Start the Flask development server:

```powershell
python app.py
```

You should see output similar to:
```text
Starting Student Mental Health Analytics Web Server on port 5000...
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.x.x:5000
Press CTRL+C to quit
```

---

## 5. View in Web Browser
Open your browser and navigate to:
**[http://127.0.0.1:5000](http://127.0.0.1:5000)**

Explore the tabs:
* **Overview (`/`):** Summary KPIs, project metadata, and module cards.
* **Dashboard (`/dashboard`):** Embedded Tableau Dashboard with interactive filters.
* **Tableau Story (`/story`):** Embedded 3-scene Tableau analytical narrative.
* **Student Dataset (`/data`):** Interactive tabular view of all 80 cleaned student records.
* **Analytical Insights (`/insights`):** 6 key academic and psychological conclusions.

---

## 6. How to Replace the Tableau Public Embed URLs
Once you publish your workbook to Tableau Public, updating the web portal is simple:

1. Open `config.py` in any text editor.
2. Locate the lines:
   ```python
   TABLEAU_DASHBOARD_URL = os.environ.get(
       "TABLEAU_DASHBOARD_URL",
       "https://public.tableau.com/views/StudentMentalHealthAnalytics/Dashboard"
   )

   TABLEAU_STORY_URL = os.environ.get(
       "TABLEAU_STORY_URL", 
       "https://public.tableau.com/views/StudentMentalHealthAnalytics/Story"
   )
   ```
3. Replace the placeholder URLs with the live links you copied from Tableau Public.
4. Save the file and refresh your browser. The embedded Tableau frame will now display your live charts!

---

## 7. Troubleshooting

* **Issue: `python` command is not recognized**
  * Solution: If Python is installed with a specific path (such as through pgAdmin or Anaconda), specify the full path:
    `& "C:\Program Files\PostgreSQL\18\pgAdmin 4\python\python.exe" app.py`
* **Issue: Tableau Dashboard shows a blank frame or refused to connect**
  * Solution: Ensure your Tableau Public workbook has **Allow others to download the workbook and its data** enabled in Tableau Public settings, and verify that third-party cookies are not blocked in your browser.
* **Issue: Port 5000 is already in use**
  * Solution: Run the app on an alternative port by passing an environment variable:
    `$env:PORT=5050; python app.py`
