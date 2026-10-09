"""
build_natural_video.py
----------------------
Generates a human-paced, conversational walkthrough of the Student Mental Health Analysis project.
Voice: en-IN-NeerjaExpressiveNeural (natural Indian English intonation)
Target Duration: ~6 minutes (between 5m 45s and 6m 30s)
Renders high-definition visual chapters and combines them with synchronized audio and WebVTT subtitles.
"""

import asyncio
import os
import subprocess
import edge_tts
import imageio_ffmpeg
from PIL import Image, ImageDraw

OUTPUT_DIR = os.path.join("site", "assets", "video")
AUDIO_FILE = os.path.join(OUTPUT_DIR, "narration.mp3")
VIDEO_FILE = os.path.join(OUTPUT_DIR, "student-mental-health-demo.mp4")
SRT_FILE = os.path.join(OUTPUT_DIR, "video-captions.srt")
VTT_FILE = os.path.join(OUTPUT_DIR, "video-captions.vtt")
TEMP_SLIDES_DIR = os.path.join("site", "assets", "video", "slides")
os.makedirs(TEMP_SLIDES_DIR, exist_ok=True)

CHAPTERS = [
    {
        "id": 1,
        "title": "Analysing Mental Health in Student Ecosystem",
        "subtitle": "Project Walkthrough & Technical Demonstration",
        "tag": "CHAPTER 1: INTRODUCTION",
        "bullets": [
            "Project Lead: Parth Pawar | Data Analytics with Tableau",
            "Core Objective: Investigating the multi-dimensional ecosystem of student wellness",
            "End-to-end implementation: Data audit, Tableau BI development, and web deployment"
        ],
        "speech": (
            "Hello everyone, and welcome. My name is Parth Pawar, and I'm very excited to walk you through my data analytics project, "
            "titled Analysing Mental Health in the Student Ecosystem. "
            "College life brings intense academic workloads, competitive grading, disrupted sleep schedules, and constant screen time. "
            "In this walkthrough, I will show you how we investigated these patterns using real student data, built an interactive Tableau business intelligence dashboard, "
            "and deployed an accessible web portfolio."
        ),
        "color": (15, 23, 42)
    },
    {
        "id": 2,
        "title": "Problem Statement & Collegiate Reality",
        "subtitle": "Why Traditional Student Support Is Too Reactive",
        "tag": "CHAPTER 2: PROBLEM STATEMENT",
        "bullets": [
            "Academic burnout is typically discovered reactively after exams or attendance drops",
            "Student surveys are rarely connected with behavioral habits or objective biomarkers",
            "Advisors and counseling departments lack unified, real-time diagnostic visibility",
            "Need for an exploratory decision-support platform rather than a clinical diagnostic tool"
        ],
        "speech": (
            "Let's start with the problem statement. In most universities, student distress is identified far too late. "
            "Counselors usually find out about burnout only after a student has failed examinations or accumulated severe absenteeism. "
            "Surveys are often conducted only once a year, and the data stays locked in static spreadsheets without interactive cross-filtering. "
            "Our goal was to create an interactive analytics platform that connects daily lifestyle habits, autonomic stress signals, and academic performance, "
            "giving educators and advisors actionable visibility to support students proactively."
        ),
        "color": (20, 30, 55)
    },
    {
        "id": 3,
        "title": "Dataset Architecture & Data Validation",
        "subtitle": "1,000 Verified Student Profiles Across 16 Multi-Dimensional Fields",
        "tag": "CHAPTER 3: DATASET ARCHITECTURE",
        "bullets": [
            "Sourced from the verified Google Sheets deliverable (1,000 rows, 16 columns)",
            "Demographics: Age (18 to 25), Gender (Male: 341, Female: 331, Other: 328)",
            "Psychological Scales: Stress (1 to 10), Anxiety (1 to 10), Depression (1 to 10)",
            "Lifestyle & Academics: Sleep Duration (hrs), Study Hours, Attendance Rate (%), LMS Score",
            "Biometrics & Support: Heart Rate Variability (RMSSD ms), 8 Structured Intervention Strategies",
            "Quality Certified: 100% Completeness, 0 Nulls, 0 Duplicates across all 16,000 data cells"
        ],
        "speech": (
            "Next, let us look at the dataset. We analyzed a verified dataset of exactly 1,000 collegiate profiles across 16 multi-dimensional variables. "
            "This covers student demographics, standardized 1 to 10 ratings for stress, anxiety, and depression, "
            "daily lifestyle habits like sleep duration and study hours, and academic telemetry including attendance and learning portal scores. "
            "We also have Heart Rate Variability in milliseconds as an objective physiological biomarker, and eight structured intervention strategies. "
            "We audited the entire dataset in Python, confirming 100% completeness, zero missing values, and zero duplicate records across all 1,000 student IDs."
        ),
        "color": (13, 148, 136)
    },
    {
        "id": 4,
        "title": "Analytical Methodology & Calculated Fields",
        "subtitle": "Structured 10-Step Lifecycle Pipeline",
        "tag": "CHAPTER 4: METHODOLOGY & LOGIC",
        "bullets": [
            "Steps 1 to 4: Data acquisition, automated quality checks, and student privacy preservation",
            "Custom Field: Age Groups (Below 20: 250, 20 to 22: 384, 23 to 25: 366 students)",
            "Custom Field: Study Categories (Light <3h, Moderate 3 to 5.5h, Intensive >5.5h)",
            "Custom Field: Sleep Hygiene (Deprived <6h, Adequate 6 to 7.5h, Optimal >7.5h)",
            "Steps 8 to 10: Tableau worksheet construction, responsive layout containers, and cloud publishing"
        ],
        "speech": (
            "To transform raw data into visual insights, we followed a structured 10-step analytical methodology. "
            "In Python, we audited data types and range boundaries. "
            "Then, inside Tableau, we engineered custom calculated fields. "
            "For example, we grouped student ages into three non-overlapping cohorts: Below 20, 20 to 22, and 23 to 25 years. "
            "We also created categories for study intensity and sleep hygiene. "
            "These calculated dimensions make it easy for campus administrators to slice and dice the data across different student segments."
        ),
        "color": (37, 99, 235)
    },
    {
        "id": 5,
        "title": "Interactive Tableau Dashboard Walkthrough",
        "subtitle": "Live Public Tableau Server Demonstration",
        "tag": "CHAPTER 5: TABLEAU BI DASHBOARD",
        "bullets": [
            "Executive Scorecard: 1,000 Students | Avg Stress 5.45 | Avg Depression 5.50 | Avg Sleep 6.49h",
            "Viz 1: Impact of Study Hours — Moderate study (3 to 5.5h) achieves optimal performance without high anxiety",
            "Viz 2 & 4: Gender Breakdowns — Stress and depression are distributed evenly across gender cohorts",
            "Viz 3: Study Hours vs Academic Performance Index — Positive linear correlation with grade benchmarks",
            "Viz 5: Autonomic HRV Telemetry — Suppressed HRV (<50 ms) objectively validates severe mental distress",
            "Viz 6: Risk Distribution Donut — 23.9% High Risk (239 students) prioritized for immediate counseling"
        ],
        "speech": (
            "Now, let us examine the published Tableau Public dashboard. "
            "The dashboard is organized into an executive scorecard and six core analytical views. "
            "At the top, our KPI scorecard shows cohort averages: average stress is 5.45 out of 10, average depression is 5.50, and average sleep is 6.49 hours per day. "
            "In our first visualization, Study Hours versus Academic Performance, we observe that students with moderate study between 3 and 5.5 hours achieve strong academic scores without severe stress. "
            "Looking at the scatter plot, we see individual student data points with a positive linear regression trendline. "
            "Very importantly, our physiological chart tracks Heart Rate Variability. "
            "Students in high distress exhibit significantly suppressed HRV below 50 milliseconds, providing an objective biomarker that backs up self-reported survey answers. "
            "Finally, our risk distribution chart reveals that 23.9% of students fall into the high-risk category, showing the clear need for early counseling support."
        ),
        "color": (15, 118, 110)
    },
    {
        "id": 6,
        "title": "Key Empirical Findings & Institutional Insights",
        "subtitle": "Evidence-Based Student Support Insights",
        "tag": "CHAPTER 6: EMPIRICAL FINDINGS",
        "bullets": [
            "Finding 1: Sleep Duration as a Stress Buffer — Sleeping <6h strongly correlates with acute stress spikes (avg 6.2)",
            "Finding 2: The Diminishing Returns Threshold — Excessive study >5.5h yields plateaued scores when anxiety is high",
            "Finding 3: Social Connection Buffers Isolation — Peer engagement scores >=6 strongly reduce depressive severity",
            "Finding 4: Targeted Interventions — Personalized pathways (CBT, Time Coaching) provide scalable support"
        ],
        "speech": (
            "From this analysis, three essential insights stand out. "
            "First, sleep duration is the most powerful natural buffer against student stress. "
            "Students sleeping under 6 hours average a stress score of 6.2, compared to 4.8 for those sleeping 7.5 hours or more. "
            "Second, studying more than 5.5 hours per day shows diminishing returns if anxiety remains high. "
            "And third, peer interaction strongly protects against depression; students with active social interaction scores reported significantly lower depressive symptoms."
        ),
        "color": (30, 41, 59)
    },
    {
        "id": 7,
        "title": "Portfolio Web Portal & Automated Deployment",
        "subtitle": "Production-Ready Static Architecture on GitHub Pages",
        "tag": "CHAPTER 7: WEB PORTAL & CI/CD",
        "bullets": [
            "Modern, accessible UI design with deep navy typography and teal analytical accents",
            "Direct live Tableau Public interactive embed with reload and external launch capabilities",
            "Responsive layout across desktop, tablet, and mobile with keyboard accessibility",
            "Automated GitHub Actions CI/CD workflow deploying static site to GitHub Pages on main branch push"
        ],
        "speech": (
            "To share these findings professionally, I developed a modern portfolio website hosted on GitHub Pages. "
            "The site features a live, interactive Tableau Public embed, verified KPI summary cards, a worksheet gallery, and direct links to our documentation and dataset. "
            "Everything is built with clean HTML5, CSS, and JavaScript, ensuring fast loading and full responsiveness on mobile, tablet, and desktop devices."
        ),
        "color": (2, 132, 199)
    },
    {
        "id": 8,
        "title": "Conclusion, Limitations & Future Scope",
        "subtitle": "Closing Remarks by Parth Pawar",
        "tag": "CHAPTER 8: CONCLUSION",
        "bullets": [
            "Ethical Disclosure: Educational diagnostic model, not an automated clinical medical device",
            "Student Privacy: Aggregate metrics displayed; individual emotional journals protected",
            "Future Scope: Integration of real-time wearable streams and semester-long time-series modeling",
            "Repository & Tableau Public links fully verified and open-source on GitHub"
        ],
        "speech": (
            "In conclusion, this project shows how business intelligence and biostatistical indicators can help universities build proactive student wellness systems. "
            "As an ethical disclosure, this model is an educational decision-support tool, not a clinical diagnostic system. "
            "In the future, this work could expand to include real-time wearable sensor streams and semester-long time-series tracking. "
            "Thank you so much for watching, and please feel free to explore the live dashboard and documentation on our GitHub repository."
        ),
        "color": (15, 23, 42)
    }
]

async def generate_speech_and_durations():
    print("[INFO] Synthesizing natural Indian English narration using en-IN-NeerjaExpressiveNeural...")
    full_text = " ".join([c["speech"] for c in CHAPTERS])
    voice = "en-IN-NeerjaExpressiveNeural"
    
    # Generate combined audio
    communicate = edge_tts.Communicate(full_text, voice, rate="+0%", pitch="+0Hz")
    await communicate.save(AUDIO_FILE)
    print(f"[SUCCESS] Audio saved to: {AUDIO_FILE}")

    # Inspect total duration
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    cmd = [ffmpeg_exe, "-i", AUDIO_FILE]
    proc = subprocess.run(cmd, stderr=subprocess.PIPE, text=True)
    total_dur = 360.0 # fallback
    for line in proc.stderr.splitlines():
        if "Duration" in line:
            parts = line.split("Duration:")[1].split(",")[0].strip()
            h, m, s = parts.split(":")
            total_dur = float(h)*3600 + float(m)*60 + float(s)
            print(f"[INFO] Verified total audio duration: {total_dur:.2f} seconds ({total_dur/60:.2f} minutes)")

    return total_dur

def draw_slide(chap, idx):
    width, height = 1280, 720
    img = Image.new("RGB", (width, height), color=chap["color"])
    draw = ImageDraw.Draw(img)

    # Accent decorative top bar
    draw.rectangle([0, 0, width, 8], fill=(13, 148, 136))

    # Tag Badge
    draw.rectangle([60, 40, 480, 75], fill=(255, 255, 255, 30), outline=(255, 255, 255, 100), width=1)
    draw.text((75, 48), chap["tag"], fill=(204, 251, 241))

    # Presenter tag right aligned
    draw.text((750, 48), "Presenter: Parth Pawar | Tableau BI", fill=(226, 232, 240))

    # Main Title & Subtitle
    draw.text((60, 100), chap["title"], fill=(255, 255, 255))
    draw.text((60, 155), chap["subtitle"], fill=(148, 163, 184))

    # Divider
    draw.line([(60, 205), (1220, 205)], fill=(255, 255, 255, 60), width=2)

    # Content Container
    draw.rectangle([60, 230, 1220, 640], fill=(255, 255, 255, 15), outline=(255, 255, 255, 40), width=1)

    # Bullets
    y_pos = 260
    for bullet in chap["bullets"]:
        draw.ellipse([90, y_pos + 6, 102, y_pos + 18], fill=(13, 148, 136))
        draw.text((120, y_pos), bullet, fill=(241, 245, 249))
        y_pos += 60

    # Footer
    draw.text((60, 670), "Student Mental Health Analytics | SkillWallet Project Walkthrough", fill=(148, 163, 184))
    draw.text((1140, 670), f"Chapter {idx+1}/8", fill=(204, 251, 241))

    slide_path = os.path.join(TEMP_SLIDES_DIR, f"slide_{idx+1}.png")
    img.save(slide_path)
    return slide_path

def build_video_and_captions(total_dur):
    # Proportional durations based on speech word counts
    word_counts = [len(c["speech"].split()) for c in CHAPTERS]
    total_words = sum(word_counts)
    durations = [round(w / total_words * total_dur, 2) for w in word_counts]
    # Adjust last duration to match total exactly
    durations[-1] = round(total_dur - sum(durations[:-1]), 2)

    print(f"[INFO] Chapter durations: {durations}")

    slide_files = []
    for idx, chap in enumerate(CHAPTERS):
        path = draw_slide(chap, idx)
        slide_files.append((path, durations[idx]))

    # Generate Concat Script for FFmpeg
    concat_file = os.path.join(TEMP_SLIDES_DIR, "concat.txt")
    with open(concat_file, "w", encoding="utf-8") as f:
        for path, dur in slide_files:
            abs_p = os.path.abspath(path).replace("\\", "/")
            f.write(f"file '{abs_p}'\n")
            f.write(f"duration {dur}\n")
        last_p = os.path.abspath(slide_files[-1][0]).replace("\\", "/")
        f.write(f"file '{last_p}'\n")

    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    cmd = [
        ffmpeg_exe, "-y",
        "-f", "concat", "-safe", "0", "-i", concat_file,
        "-i", AUDIO_FILE,
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
        "-c:a", "aac", "-b:a", "128k",
        "-shortest",
        VIDEO_FILE
    ]

    print("[INFO] Rendering video via FFmpeg...")
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        print("[ERROR] FFmpeg failed:", res.stderr)
        return False

    print(f"[SUCCESS] Rendered final video to: {VIDEO_FILE}")
    size_mb = os.path.getsize(VIDEO_FILE) / (1024 * 1024)
    print(f"[INFO] Video size: {size_mb:.2f} MB")

    # Generate Subtitles (SRT and VTT)
    current_time = 0.0
    srt_entries = []
    vtt_entries = ["WEBVTT\n"]

    for idx, (chap, dur) in enumerate(zip(CHAPTERS, durations)):
        start_t = current_time
        end_t = current_time + dur
        current_time = end_t

        def fmt_time(sec, srt=True):
            m, s = divmod(sec, 60)
            h, m = divmod(m, 60)
            ms = int((s - int(s)) * 1000)
            if srt:
                return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{ms:03d}"
            else:
                return f"{int(h):02d}:{int(m):02d}:{int(s):02d}.{ms:03d}"

        srt_text = f"{idx+1}\n{fmt_time(start_t, True)} --> {fmt_time(end_t, True)}\n{chap['speech'][:140]}...\n"
        vtt_text = f"\n{fmt_time(start_t, False)} --> {fmt_time(end_t, False)}\n{chap['speech'][:140]}...\n"

        srt_entries.append(srt_text)
        vtt_entries.append(vtt_text)

    with open(SRT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(srt_entries))
    with open(VTT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(vtt_entries))

    print("[SUCCESS] Subtitle files written: video-captions.srt and video-captions.vtt")
    return True

if __name__ == "__main__":
    dur = asyncio.run(generate_speech_and_durations())
    build_video_and_captions(dur)
