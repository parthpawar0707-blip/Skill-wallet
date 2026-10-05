"""
Configuration file for Student Mental Health Analytics Web Application.
Update the Tableau URLs below after publishing your workbook to Tableau Public.
"""

import os

class Config:
    PROJECT_NAME = "Analysing Mental Health in Student Ecosystem"
    DOMAIN = "Healthcare & Higher Education"
    STUDENT_NAME = "Parth Pawar"
    ACADEMIC_YEAR = "2025 - 2026"
    
    # TABLEAU EMBED URLs:
    # Replace these placeholders with your live Tableau Public URLs after publishing.
    # Example format: "https://public.tableau.com/views/StudentMentalHealthAnalytics/Dashboard"
    TABLEAU_DASHBOARD_URL = os.environ.get(
        "TABLEAU_DASHBOARD_URL",
        "https://public.tableau.com/views/StudentMentalHealthAnalytics/Dashboard"
    )
    
    TABLEAU_STORY_URL = os.environ.get(
        "TABLEAU_STORY_URL", 
        "https://public.tableau.com/views/StudentMentalHealthAnalytics/Story"
    )

    # Server configuration
    PORT = int(os.environ.get("PORT", 5000))
    DEBUG = os.environ.get("FLASK_DEBUG", "True").lower() == "true"
