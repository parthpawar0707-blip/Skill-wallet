"""
Flask Application for Student Mental Health Analytics Project
Integrates Tableau Dashboard and Story with an interactive web portal.
"""

import os
import csv
from flask import Flask, render_template, abort
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "student_mental_health_cleaned.csv")

def load_student_data():
    """Load cleaned student records from CSV for data preview."""
    records = []
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                records.append(row)
    return records

@app.route("/")
def index():
    records = load_student_data()
    total_students = len(records)
    
    # Calculate baseline metrics
    if total_students > 0:
        avg_stress = round(sum(float(r["Stress_Level"]) for r in records) / total_students, 2)
        avg_sleep = round(sum(float(r["Sleep_Hours"]) for r in records) / total_students, 2)
        avg_perf = round(sum(float(r["Academic_Performance"]) for r in records) / total_students, 2)
        avg_hrv = round(sum(float(r["Heart_Rate_Variability"]) for r in records) / total_students, 2)
        high_risk_count = sum(1 for r in records if r["Mental_Health_Risk"] == "High")
        med_risk_count = sum(1 for r in records if r["Mental_Health_Risk"] == "Medium")
        low_risk_count = sum(1 for r in records if r["Mental_Health_Risk"] == "Low")
    else:
        avg_stress = avg_sleep = avg_perf = avg_hrv = 0
        high_risk_count = med_risk_count = low_risk_count = 0

    kpis = {
        "total_students": total_students,
        "avg_stress": avg_stress,
        "avg_sleep": avg_sleep,
        "avg_perf": avg_perf,
        "avg_hrv": avg_hrv,
        "high_risk": high_risk_count,
        "med_risk": med_risk_count,
        "low_risk": low_risk_count
    }
    
    return render_template("index.html", kpis=kpis, config=app.config)

@app.route("/dashboard")
def dashboard():
    return render_template(
        "dashboard.html",
        dashboard_url=app.config["TABLEAU_DASHBOARD_URL"],
        config=app.config
    )

@app.route("/story")
def story():
    return render_template(
        "story.html",
        story_url=app.config["TABLEAU_STORY_URL"],
        config=app.config
    )

@app.route("/data")
def data_view():
    records = load_student_data()
    headers = list(records[0].keys()) if records else []
    return render_template("data.html", records=records, headers=headers, config=app.config)

@app.route("/insights")
def insights():
    return render_template("insights.html", config=app.config)

if __name__ == "__main__":
    port = app.config.get("PORT", 5000)
    debug = app.config.get("DEBUG", True)
    print(f"Starting Student Mental Health Analytics Web Server on port {port}...")
    app.run(host="0.0.0.0", port=port, debug=debug)
