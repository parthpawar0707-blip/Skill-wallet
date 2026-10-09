import asyncio
import os
import json
import subprocess
import aiohttp
import aiohttp.connector

# Ensure standard DNS resolution on Windows
aiohttp.AsyncResolver = aiohttp.ThreadedResolver
aiohttp.connector.AsyncResolver = aiohttp.ThreadedResolver

import edge_tts

# 8-Chapter Master Storyboard Segments (Target ~365-380 seconds total duration, ~6m 10s)
# Each segment is precisely matched to an authentic on-screen visual.
SECTIONS = [
    {
        "id": "chap_01_intro",
        "chapter": 1,
        "title": "Introduction & Welcome",
        "text": (
            "Hello everyone! My name is Parth Pawar, and welcome to this complete walkthrough of "
            "Analysing Mental Health in Student Ecosystem. Today, undergraduates navigate heavy academic pressures, "
            "irregular sleep schedules, and prolonged screen exposure. In this walkthrough, I will guide you "
            "through our verified dataset, our interactive Tableau Public dashboard, and the empirical takeaways "
            "that emerge from the data."
        )
    },
    {
        "id": "chap_02_problem",
        "chapter": 2,
        "title": "Problem Statement & Objectives",
        "text": (
            "Collegiate mental health is frequently addressed only reactively after severe distress. "
            "However, well-being is intricately connected to daily lifestyle patterns like screen time, sleep quality, "
            "and support systems. Our objective is building an interactive Tableau decision-support dashboard that reveals "
            "empirical patterns across student lifestyles and clinical scores, empowering mentors and counselors "
            "to offer timely, proactive support."
        )
    },
    {
        "id": "chap_03_dataset",
        "chapter": 3,
        "title": "Dataset Architecture & Source",
        "text": (
            "Our verified dataset contains exactly 200 student records across 18 multi-dimensional behavioral, clinical, "
            "and academic variables, tracked from STU 0001 to STU 0200. Demographics capture age 18 to 25 and gender cohorts. "
            "Clinical scales measure Anxiety and Depression from 0 to 100, alongside categorical Stress Levels. "
            "Lifestyle telemetry tracks daily screen time in hours, sleep quality, physical activity, and therapeutic pathways like CBT and Counseling."
        )
    },
    {
        "id": "chap_04_methodology",
        "chapter": 4,
        "title": "Methodology & Calculations",
        "text": (
            "Using Python and Pandas, we verified zero null values and zero duplicates across all records. "
            "In Tableau Desktop, we engineered two vital calculated fields: "
            "First, Active Therapy, defined as: IF Therapy Type does not equal No Therapy THEN 1 ELSE 0 END, "
            "isolating students in institutional care. "
            "Second, High Stress and Poor Sleep, flagging students suffering concurrently from acute stress and severe sleep disruption."
        )
    },
    {
        "id": "chap_05a_kpi",
        "chapter": 5,
        "title": "Tableau Walkthrough: Executive KPI Ribbon",
        "text": (
            "On our live Tableau Public dashboard, the executive KPI ribbon establishes four cohort benchmarks across all 200 students: "
            "Total Students: exactly 200 undergraduates. Average Anxiety Score: 52.59 out of 100. Average Depression Score: 48.09 out of 100. "
            "And Average Daily Screen Time: 7.10 hours per day. These metrics ground our entire visual analysis."
        )
    },
    {
        "id": "chap_05b_stress_dist",
        "chapter": 5,
        "title": "Tableau Walkthrough: Stress Level Distribution",
        "text": (
            "Worksheet one examines Stress Level Distribution across the cohort. "
            "107 students, or 53.5 percent, experience Medium stress. "
            "49 students, or 24.5 percent, experience High stress, while 44 students, or 22 percent, report Low stress. "
            "Combined, over 78 percent of surveyed students operate under moderate to severe stress, proving this is a widespread campus challenge."
        )
    },
    {
        "id": "chap_05c_screen_time",
        "chapter": 5,
        "title": "Tableau Walkthrough: Screen Time vs Stress",
        "text": (
            "Worksheet two evaluates daily screen time against reported stress levels. "
            "A distinct upward trend emerges: students with Low stress average 6.00 hours of screen time. "
            "Medium stress students average 7.07 hours, while High stress students surge to 8.12 hours daily. "
            "High-stress students spend over two additional hours on screens each day, highlighting digital fatigue."
        )
    },
    {
        "id": "chap_05d_sleep_quality",
        "chapter": 5,
        "title": "Tableau Walkthrough: Sleep Quality vs Stress",
        "text": (
            "Worksheet three explores Sleep Quality against Stress Level. "
            "Among students reporting Poor sleep, 35 out of 66 suffer from High stress, 30 report Medium stress, and only one maintains Low stress. "
            "Conversely, among students with Good sleep, 22 report Low stress and only two report High stress. "
            "This confirms sleep quality as a vital resilience buffer."
        )
    },
    {
        "id": "chap_05e_gender",
        "chapter": 5,
        "title": "Tableau Walkthrough: Gender Mental Health Comparison",
        "text": (
            "Worksheet four benchmarks mental health across gender cohorts. "
            "Average anxiety remains evenly distributed: 53.32 for females, 51.76 for males, and 53.50 for other cohorts. "
            "Depression scores follow a similar pattern: 48.10 for females, 47.88 for males, and 50.38 for others. "
            "This statistical parity shows psychological strain is evenly shared across demographics, making lifestyle factors the primary differentiators."
        )
    },
    {
        "id": "chap_05f_anxiety_depression",
        "chapter": 5,
        "title": "Tableau Walkthrough: Stress vs Symptoms Escalation",
        "text": (
            "Worksheets five and six analyze how stress escalates into clinical symptoms. "
            "Anxiety scores rise steeply from 30.27 in Low stress, to 52.85 in Medium stress, reaching 72.06 in High stress. "
            "Similarly, depression scores escalate from 26.80 in Low stress to 68.78 in High stress—over two and a half times higher. "
            "Chronic stress reliably compounds into acute distress."
        )
    },
    {
        "id": "chap_05g_therapy_history",
        "chapter": 5,
        "title": "Tableau Walkthrough: Therapy Efficacy & History Prevalence",
        "text": (
            "Worksheets seven and eight evaluate support modalities and history. "
            "In Ranked Therapy Efficacy, Cognitive Behavioral Therapy leads with an average progress score of 40.80, followed by Counseling at 34.43 and Support Groups at 33.10. "
            "Meanwhile, exactly 40 percent of students, or 80 out of 200, report prior mental health history, underscoring the need for early screening."
        )
    },
    {
        "id": "chap_05h_filters",
        "chapter": 5,
        "title": "Tableau Walkthrough: Interactive Cross-Filtering",
        "text": (
            "On the published Tableau dashboard, interactive cross-filtering allows advisors to segment the cohort by stress level or sleep quality. "
            "Clicking a high-stress tier dynamically updates all connected worksheets, isolating vulnerable students and enabling targeted intervention planning in real time."
        )
    },
    {
        "id": "chap_06_findings",
        "chapter": 6,
        "title": "Core Empirical Findings & Interpretation",
        "text": (
            "Synthesizing our observations yields three primary findings: "
            "First, Sleep Quality is the Paramount Protective Buffer against high stress—restorative sleep strongly shields students from distress. "
            "Second, daily screen time exceeding 7.5 hours strongly co-occurs with elevated anxiety and burnout. "
            "Third, structured interventions like CBT deliver proven symptom progress compared to unguided coping. "
            "These empirical signals offer actionable guidance for campus welfare initiatives."
        )
    },
    {
        "id": "chap_07_website",
        "chapter": 7,
        "title": "Portfolio Website & Public Deployment",
        "text": (
            "To present this work professionally, I deployed a dedicated portfolio website on GitHub Pages featuring a modern editorial design. "
            "The site includes an Executive Hero section, an interactive Tableau embed with reload controls and fallback options, "
            "a Worksheet Gallery, an embedded HTML5 video player with captions, and direct links to our documentation and repository."
        )
    },
    {
        "id": "chap_08_conclusion",
        "chapter": 8,
        "title": "Conclusion & Final Thoughts",
        "text": (
            "In conclusion, Analysing Mental Health in Student Ecosystem demonstrates how Tableau transforms complex student wellness data into "
            "intuitive, actionable dashboards. All source datasets, data dictionaries, workbooks, and documentation are available on my GitHub repository. "
            "Thank you for watching! My name is Parth Pawar, and I look forward to your thoughts."
        )
    }
]

async def generate_speech():
    os.makedirs('temp_audio', exist_ok=True)
    timing_data = []
    
    current_time = 0.0
    for idx, sec in enumerate(SECTIONS):
        sec_id = sec['id']
        txt = sec['text']
        mp3_path = f"temp_audio/{sec_id}.mp3"
        print(f"Generating audio for {sec_id}: {sec['title']}...")
        
        # Indian English Male voice: en-IN-PrabhatNeural
        # Natural collegiate presentation pace (+22% rate, -5Hz pitch)
        comm = edge_tts.Communicate(txt, voice="en-IN-PrabhatNeural", rate="+22%", pitch="-5Hz")
        await comm.save(mp3_path)
        
        cmd = [
            'ffprobe', '-v', 'error', '-show_entries', 'format=duration',
            '-of', 'default=noprint_wrappers=1:nokey=1', mp3_path
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        dur = float(res.stdout.strip())
        
        timing_data.append({
            "index": idx + 1,
            "id": sec_id,
            "chapter": sec.get("chapter", idx + 1),
            "title": sec['title'],
            "start": current_time,
            "end": current_time + dur,
            "duration": dur,
            "text": txt,
            "file": mp3_path
        })
        current_time += dur
    
    total_dur = current_time
    print(f"\n==========================================")
    print(f"TOTAL AUDIO DURATION: {total_dur:.2f} seconds ({total_dur/60:.2f} minutes)")
    print(f"TARGET WINDOW: 345 - 390 seconds (5:45 - 6:30 minutes)")
    print(f"==========================================")
    
    # Concatenate all mp3s
    concat_list = "temp_audio/concat.txt"
    with open(concat_list, "w", encoding="utf-8") as f:
        for t in timing_data:
            f.write(f"file '{os.path.abspath(t['file']).replace(chr(92), '/')}'\n")
    
    out_mp3 = "site/assets/video/narration.mp3"
    concat_cmd = [
        'ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', concat_list,
        '-c:a', 'libmp3lame', '-b:a', '192k', out_mp3
    ]
    subprocess.run(concat_cmd, check=True)
    print(f"Saved master narration: {out_mp3} ({os.path.getsize(out_mp3)} bytes)")
    
    generate_subtitles(timing_data)
    
    with open("temp_audio/timings.json", "w", encoding="utf-8") as f:
        json.dump(timing_data, f, indent=2)
    print("Saved temp_audio/timings.json")

def format_timestamp_srt(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int(round((seconds - int(seconds)) * 1000))
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def format_timestamp_vtt(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int(round((seconds - int(seconds)) * 1000))
    return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"

def generate_subtitles(timings):
    srt_lines = []
    vtt_lines = ["WEBVTT", ""]
    
    cue_idx = 1
    for t in timings:
        words = t['text'].split()
        chunk_size = 11
        chunks = [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
        
        chunk_dur = t['duration'] / len(chunks)
        for i, chunk in enumerate(chunks):
            cue_start = t['start'] + (i * chunk_dur)
            cue_end = t['start'] + ((i + 1) * chunk_dur)
            
            srt_lines.append(str(cue_idx))
            srt_lines.append(f"{format_timestamp_srt(cue_start)} --> {format_timestamp_srt(cue_end)}")
            srt_lines.append(chunk)
            srt_lines.append("")
            
            vtt_lines.append(str(cue_idx))
            vtt_lines.append(f"{format_timestamp_vtt(cue_start)} --> {format_timestamp_vtt(cue_end)}")
            vtt_lines.append(chunk)
            vtt_lines.append("")
            
            cue_idx += 1
            
    with open("site/assets/video/video-captions.srt", "w", encoding="utf-8") as f:
        f.write("\n".join(srt_lines))
    print("Saved site/assets/video/video-captions.srt")
    
    with open("site/assets/video/video-captions.vtt", "w", encoding="utf-8") as f:
        f.write("\n".join(vtt_lines))
    print("Saved site/assets/video/video-captions.vtt")

if __name__ == '__main__':
    asyncio.run(generate_speech())
