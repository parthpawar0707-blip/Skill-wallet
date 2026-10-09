"""
build_walkthrough_video.py
--------------------------
Renders high-definition synchronized visuals for each of the 8 segments of the walkthrough,
combines them with the natural Indian English narration track (narration.mp3),
and encodes the production video: site/assets/video/student-mental-health-demo.mp4 (720p HD).
"""

import os
import subprocess
import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = os.path.join("site", "assets", "video")
AUDIO_FILE = os.path.join(OUTPUT_DIR, "narration.mp3")
VIDEO_FILE = os.path.join(OUTPUT_DIR, "student-mental-health-demo.mp4")
TEMP_SLIDES_DIR = os.path.join("site", "assets", "video", "slides")
os.makedirs(TEMP_SLIDES_DIR, exist_ok=True)

# 8 Segments totaling 398.18 seconds (~6m 38s)
SEGMENTS = [
    {
        "id": 1,
        "title": "Analysing Mental Health in Student Ecosystem",
        "subtitle": "Project Walkthrough & Technical Demonstration",
        "presenter": "Presenter: Parth Pawar | Data Analytics with Tableau",
        "tag": "SEGMENT 1: INTRODUCTION",
        "bullets": [
            "Comprehensive investigation of collegiate mental health dynamics",
            "Bridging behavioral survey metrics with biometric telemetry",
            "End-to-end data analytics workflow: Acquisition, Validation, BI & Web Integration"
        ],
        "duration": 35.0,
        "color": (15, 23, 42)
    },
    {
        "id": 2,
        "title": "Problem Statement & Collegiate Realities",
        "subtitle": "Why Traditional Mental Health Monitoring Falls Short",
        "presenter": "Healthcare & Higher Education Domain Context",
        "tag": "SEGMENT 2: PROBLEM DEFINITION",
        "bullets": [
            "Academic distress discovered reactively after examination failure or absenteeism",
            "Campus surveys administered irregularly without dynamic cross-filtering",
            "Absence of objective physiological telemetry to substantiate self-reported survey ratings",
            "Lack of unified decision-support dashboards for college advisors and counselors"
        ],
        "duration": 45.0,
        "color": (20, 30, 55)
    },
    {
        "id": 3,
        "title": "Verified Dataset Architecture & Data Quality",
        "subtitle": "1,000 Collegiate Records Across 16 Multi-Dimensional Fields",
        "presenter": "Certified Google Sheets Deliverable Data Source",
        "tag": "SEGMENT 3: DATA AUDIT & SCHEMA",
        "bullets": [
            "Demographics: Student_ID (1-1000), Age (18-25), Gender (Male: 341, Female: 331, Other: 328)",
            "Psychological Scales: Stress (1-10), Anxiety (1-10), Depression (1-10)",
            "Lifestyle & Academics: Sleep Duration (hrs), Study Hours, Attendance Rate (%), LMS Score",
            "Biometrics & Support: Heart Rate Variability (RMSSD ms), 8 Structured Intervention Strategies",
            "Data Quality Certified: 100% Completeness, 0 Nulls, 0 Duplicates across all 16,000 data cells"
        ],
        "duration": 60.0,
        "color": (13, 148, 136)
    },
    {
        "id": 4,
        "title": "Analytical Methodology & Calculated Fields",
        "subtitle": "Reproducible Preparation & Feature Engineering in Tableau",
        "presenter": "Standardized 10-Step Lifecycle Pipeline",
        "tag": "SEGMENT 4: METHODOLOGY & FEATURE ENGINEERING",
        "bullets": [
            "Step 1-4: Automated data validation, type normalization, and boundary verification in Python",
            "Step 5: Custom Calculated Field — Age Groups (<20: 250, 20-22: 384, 23-25: 366 students)",
            "Step 6: Custom Calculated Field — Study Categories (Light <3h, Moderate 3-5.5h, Intensive >5.5h)",
            "Step 7: Custom Calculated Field — Sleep Hygiene (<6h Deprived, 6-7.5h Adequate, >7.5h Optimal)",
            "Step 8-10: Tableau worksheet construction, responsive layout containers, and cloud publishing"
        ],
        "duration": 55.0,
        "color": (37, 99, 235)
    },
    {
        "id": 5,
        "title": "Interactive Tableau Dashboard Walkthrough",
        "subtitle": "Executive Scorecard & Multi-Dimensional Worksheets",
        "presenter": "Live Public Tableau Server Demonstration",
        "tag": "SEGMENT 5: LIVE TABLEAU BI DEMONSTRATION",
        "bullets": [
            "Executive Scorecard: 1,000 Students | Avg Stress 5.45 | Avg Depression 5.50 | Avg Sleep 6.49h",
            "Viz 1: Impact of Study Hours — Moderate study (3-5.5h) achieves optimal performance without high anxiety",
            "Viz 2 & 4: Demographic breakdowns — Stress & Depression levels distributed evenly across gender cohorts",
            "Viz 3: Study Hours vs Academic Performance Index — Positive linear correlation with grade benchmarks",
            "Viz 5: Autonomic HRV Telemetry — Suppressed HRV (<50 ms) objectively validates severe mental distress",
            "Viz 6: Risk Distribution Donut — 23.9% High Risk (239 students) prioritized for immediate counseling"
        ],
        "duration": 105.0,
        "color": (15, 118, 110)
    },
    {
        "id": 6,
        "title": "Key Empirical Findings & Institutional Insights",
        "subtitle": "Actionable Conclusions Derived from Data Evidence",
        "presenter": "Evidence-Based Student Support Insights",
        "tag": "SEGMENT 6: EMPIRICAL FINDINGS",
        "bullets": [
            "Finding 1: Sleep Duration as a Stress Buffer — Sleeping <6h strongly correlates with acute stress spikes (avg 6.2)",
            "Finding 2: The Diminishing Returns Threshold — Excessive study >6.5h yields plateaued scores when anxiety is high",
            "Finding 3: Social Connection Buffers Isolation — Peer engagement scores >=6 strongly reduce depressive severity",
            "Finding 4: Targeted Interventions — Personalized pathways (CBT, Time Coaching) provide scalable support"
        ],
        "duration": 50.0,
        "color": (30, 41, 59)
    },
    {
        "id": 7,
        "title": "Portfolio Web Portal & Automated Deployment",
        "subtitle": "Production-Ready Static Architecture on GitHub Pages",
        "presenter": "Full-Stack Deployment & CI/CD Pipeline",
        "tag": "SEGMENT 7: WEB INTEGRATION & CI/CD",
        "bullets": [
            "Modern, accessible UI design with deep navy typography and teal analytical accents",
            "Direct live Tableau Public interactive embed with reload and external launch capabilities",
            "Responsive layout across desktop, tablet, and mobile with keyboard accessibility",
            "Automated GitHub Actions CI/CD workflow deploying static site to GitHub Pages on main branch push"
        ],
        "duration": 40.0,
        "color": (2, 132, 199)
    },
    {
        "id": 8,
        "title": "Conclusion, Limitations & Future Scope",
        "subtitle": "Summary of Contributions & Ethical Considerations",
        "presenter": "Closing Remarks by Parth Pawar",
        "tag": "SEGMENT 8: CONCLUSION",
        "bullets": [
            "Ethical Disclosure: Educational diagnostic model, not an automated clinical medical device",
            "Student Privacy: Aggregate metrics displayed; individual emotional journals protected",
            "Future Scope: Integration of real-time wearable streams and semester-long time-series modeling",
            "Repository & Tableau Public links fully verified and open-source on GitHub"
        ],
        "duration": 30.0,
        "color": (15, 23, 42)
    }
]

def draw_slide(seg, idx):
    width, height = 1280, 720
    img = Image.new("RGB", (width, height), color=seg["color"])
    draw = ImageDraw.Draw(img)

    # Accent decorative header bar
    draw.rectangle([0, 0, width, 8], fill=(13, 148, 136))

    # Tag Badge
    draw.rectangle([60, 40, 460, 75], fill=(255, 255, 255, 30), outline=(255, 255, 255, 100), width=1)
    draw.text((75, 48), seg["tag"], fill=(204, 251, 241))

    # Presenter tag right aligned
    draw.text((720, 48), seg["presenter"], fill=(226, 232, 240))

    # Main Title
    draw.text((60, 100), seg["title"], fill=(255, 255, 255))
    draw.text((60, 155), seg["subtitle"], fill=(148, 163, 184))

    # Divider
    draw.line([(60, 205), (1220, 205)], fill=(255, 255, 255, 60), width=2)

    # Content Container
    draw.rectangle([60, 230, 1220, 640], fill=(255, 255, 255, 15), outline=(255, 255, 255, 40), width=1)

    # Bullets
    y_pos = 260
    for bullet in seg["bullets"]:
        draw.ellipse([90, y_pos + 6, 102, y_pos + 18], fill=(13, 148, 136))
        # Word wrap bullet if long
        draw.text((120, y_pos), bullet, fill=(241, 245, 249))
        y_pos += 60

    # Footer
    draw.text((60, 670), "Student Mental Health Analytics | Data Analytics Portfolio Project | Parth Pawar", fill=(148, 163, 184))
    draw.text((1140, 670), f"{idx+1} / {len(SEGMENTS)}", fill=(204, 251, 241))

    slide_path = os.path.join(TEMP_SLIDES_DIR, f"slide_{idx+1}.png")
    img.save(slide_path)
    return slide_path

def build_video():
    print("[INFO] Generating presentation slides...")
    slide_files = []
    for idx, seg in enumerate(SEGMENTS):
        path = draw_slide(seg, idx)
        slide_files.append((path, seg["duration"]))

    # Create concat file for FFmpeg
    concat_file = os.path.join(TEMP_SLIDES_DIR, "concat.txt")
    with open(concat_file, "w", encoding="utf-8") as f:
        for path, dur in slide_files:
            abs_p = os.path.abspath(path).replace("\\", "/")
            f.write(f"file '{abs_p}'\n")
            f.write(f"duration {dur}\n")
        # Repeat last file for trailing frame
        last_p = os.path.abspath(slide_files[-1][0]).replace("\\", "/")
        f.write(f"file '{last_p}'\n")

    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    print(f"[INFO] Using FFmpeg at: {ffmpeg_exe}")

    # Render video with audio
    cmd = [
        ffmpeg_exe, "-y",
        "-f", "concat", "-safe", "0", "-i", concat_file,
        "-i", AUDIO_FILE,
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
        "-c:a", "aac", "-b:a", "128k",
        "-shortest",
        VIDEO_FILE
    ]

    print("[INFO] Rendering video with FFmpeg...")
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        print("[ERROR] FFmpeg rendering failed:")
        print(res.stderr)
        return False

    print(f"[SUCCESS] Rendered final video to: {VIDEO_FILE}")
    size_mb = os.path.getsize(VIDEO_FILE) / (1024 * 1024)
    print(f"[INFO] Video file size: {size_mb:.2f} MB")
    return True

if __name__ == "__main__":
    build_video()
