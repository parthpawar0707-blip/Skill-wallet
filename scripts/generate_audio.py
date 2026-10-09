import asyncio
import os
import subprocess
import aiohttp
import aiohttp.connector

# Ensure standard DNS resolution on Windows
aiohttp.AsyncResolver = aiohttp.ThreadedResolver
aiohttp.connector.AsyncResolver = aiohttp.ThreadedResolver

import edge_tts

SECTIONS = [
    {
        "id": "scene_01_intro",
        "title": "Introduction & Welcome",
        "text": (
            "Hello everyone! My name is Parth Pawar, and welcome to this complete walkthrough of my data analytics "
            "and business intelligence project: Analysing Mental Health in Student Ecosystem. "
            "In modern higher education, undergraduates navigate academic pressures, irregular sleep, "
            "and prolonged digital exposure. Today, I will walk you through our verified dataset, data preparation, "
            "live Tableau Public dashboard, and key analytical takeaways."
        )
    },
    {
        "id": "scene_02_problem",
        "title": "Problem Statement & Objectives",
        "text": (
            "Collegiate mental health is often discussed subjectively or addressed only reactively after severe distress. "
            "However, well-being is closely tied to daily lifestyle patterns like screen time, sleep quality, and support systems. "
            "Our objective is to build an interactive Tableau decision-support dashboard that uncovers empirical patterns across "
            "lifestyle habits and validated mental health indicators, enabling institutions to offer timely, non-invasive support."
        )
    },
    {
        "id": "scene_03_dataset",
        "title": "Dataset Architecture & Source",
        "text": (
            "Our verified dataset comprises exactly 200 student records across 18 multi-dimensional clinical, behavioral, and academic variables. "
            "Each student is tracked by a unique ID from STU 0001 to STU 0200. "
            "Variables include age, gender, standardized Anxiety and Depression scores from 0 to 100, categorical Stress Levels, "
            "daily screen time, sleep quality, physical activity, and structured therapy pathways including CBT, Counseling, and Meditation."
        )
    },
    {
        "id": "scene_04_methodology",
        "title": "Data Preparation & Calculations",
        "text": (
            "Using Python and Pandas, we confirmed 100 percent data completeness with zero missing values and zero duplicate records. "
            "Within Tableau Desktop, we engineered two vital calculated fields: "
            "First, Active Therapy, defined as: IF Therapy Type does not equal No Therapy THEN 1 ELSE 0 END, "
            "isolating students receiving structured care. "
            "Second, High Stress and Poor Sleep, which flags students suffering concurrently from acute stress and severe sleep deprivation."
        )
    },
    {
        "id": "scene_05_kpi",
        "title": "Executive KPI Ribbon",
        "text": (
            "Transitioning to our live Tableau Public dashboard, the top executive KPI ribbon establishes four cohort benchmarks across all 200 students: "
            "Total Students: exactly 200 undergraduates. "
            "Average Anxiety Score: 52.59 out of 100. "
            "Average Depression Score: 48.09 out of 100. "
            "And Average Daily Screen Time: 7.10 hours per day. "
            "These benchmarks ground our subsequent visual analysis."
        )
    },
    {
        "id": "scene_06_stress_dist",
        "title": "Worksheet 1: Stress Level Distribution",
        "text": (
            "Worksheet one examines the Stress Level Distribution across the cohort. "
            "107 students, or 53.5 percent, experience Medium stress. "
            "49 students, or 24.5 percent, experience High stress, while 44 students, or 22 percent, report Low stress. "
            "Combined, over 78 percent of surveyed students operate under moderate-to-severe stress, proving that academic stress is widespread rather than an isolated issue."
        )
    },
    {
        "id": "scene_07_screen_time",
        "title": "Worksheet 2: Screen Time vs Stress Level",
        "text": (
            "Worksheet two evaluates daily screen time against reported stress levels. "
            "A distinct upward trend emerges: students with Low stress average 6.00 hours of screen time daily. "
            "Medium-stress students average 7.07 hours, while High-stress students surge to 8.12 hours per day. "
            "Students facing acute stress consume over two hours more digital screen time daily, highlighting digital fatigue as an institutional concern."
        )
    },
    {
        "id": "scene_08_sleep_quality",
        "title": "Worksheet 3: Sleep Quality vs Stress Level",
        "text": (
            "Worksheet three explores the cross-tabulation of Sleep Quality against Stress Level. "
            "Among students reporting Poor sleep, 35 out of 66 suffer from High stress, 30 have Medium stress, and only one maintains low stress! "
            "In stark contrast, among students with Good sleep quality, 22 report Low stress and only two suffer from high stress. "
            "This confirms sleep quality as a vital personal resilience buffer."
        )
    },
    {
        "id": "scene_09_gender",
        "title": "Worksheet 4: Gender Mental Health Comparison",
        "text": (
            "Worksheet four benchmarks anxiety and depression across gender cohorts. "
            "Average anxiety remains evenly distributed: 53.32 for females, 51.76 for males, and 53.50 for other cohorts. "
            "Depression scores follow a similar pattern: 48.10 for females, 47.88 for males, and 50.38 for others. "
            "This proves that psychological strain is shared across demographics, making lifestyle factors far more influential determinants."
        )
    },
    {
        "id": "scene_10_anxiety_depression",
        "title": "Worksheets 5 & 6: Stress vs Anxiety and Depression",
        "text": (
            "Worksheets five and six analyze how everyday stress translates into clinical symptoms. "
            "Anxiety scores rise steeply from 30.27 in Low stress, to 52.85 in Medium stress, reaching 72.06 in High stress. "
            "Similarly, depression scores escalate from 26.80 in Low stress to 68.78 in High stress—more than two and a half times higher. "
            "This steep escalation demonstrates how unmanaged academic stress reliably compounds into acute distress."
        )
    },
    {
        "id": "scene_11_therapy_prevalence",
        "title": "Worksheets 7 & 8: Therapy Efficacy and History Prevalence",
        "text": (
            "Worksheets seven and eight evaluate support modalities and mental health history. "
            "In Ranked Therapy Efficacy, Cognitive Behavioral Therapy leads with an average progress score of 40.80, followed by Counseling at 34.43 and Support Groups at 33.10. "
            "Students with No Therapy record zero progress. "
            "Additionally, exactly 40 percent of students, or 80 out of 200, report prior mental health history, emphasizing the importance of early orientation screening."
        )
    },
    {
        "id": "scene_12_findings",
        "title": "Core Empirical Findings & Interpretation",
        "text": (
            "Synthesizing our observations yields three primary findings: "
            "First, Sleep Quality is the Paramount Protective Buffer against high stress. "
            "Second, Daily screen time exceeding 7.5 hours strongly co-occurs with elevated stress and anxiety. "
            "Third, Structured interventions like CBT deliver proven symptom progress compared to unguided coping. "
            "These empirical signals offer actionable guidance for student welfare initiatives without making unverified medical claims."
        )
    },
    {
        "id": "scene_13_website",
        "title": "Portfolio Website & Public Deployment",
        "text": (
            "To showcase this work professionally, I deployed a dedicated portfolio website on GitHub Pages featuring a modern editorial design. "
            "The site includes an Executive Hero section, an interactive Tableau embed with reload controls and fallback options, "
            "a complete Worksheet Gallery, an embedded HTML5 video player with captions, and links to our technical reports and GitHub repository."
        )
    },
    {
        "id": "scene_14_conclusion",
        "title": "Conclusion & Final Thoughts",
        "text": (
            "In conclusion, Analysing Mental Health in Student Ecosystem demonstrates how business intelligence with Tableau transforms complex student wellness data into intuitive, actionable dashboards. "
            "All source code, data dictionaries, workbooks, and documentation are available on my GitHub repository. "
            "Thank you for watching! My name is Parth Pawar, and I look forward to your feedback."
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
        
        comm = edge_tts.Communicate(txt, voice="en-IN-PrabhatNeural", rate="+30%")
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
    print(f"TARGET WINDOW: 300 - 420 seconds (5 - 7 minutes)")
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
    
    import json
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
        chunk_size = 12
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
