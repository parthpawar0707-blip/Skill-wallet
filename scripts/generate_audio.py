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

# Conversational Indian English collegiate script with verified Tableau metrics
# Structured across 14 chapters, timed for ~6 minutes duration (5:45 - 6:30 window)
SECTIONS = [
    {
        "id": "scene_01_intro",
        "title": "Introduction & Welcome",
        "text": (
            "Hello everyone! My name is Parth Pawar, and welcome to the project walkthrough of "
            "Analysing Mental Health in Student Ecosystem. In modern higher education, undergraduates navigate heavy "
            "academic pressures, irregular sleep, and prolonged screen exposure. Today, I'll walk you through our "
            "verified dataset, Tableau Public dashboard, and key analytical takeaways."
        )
    },
    {
        "id": "scene_02_problem",
        "title": "Problem Statement & Objectives",
        "text": (
            "Collegiate mental health is often discussed subjectively or addressed only reactively after severe distress. "
            "Well-being is closely tied to daily lifestyle factors like screen time, sleep quality, and support systems. "
            "Our goal is to build an interactive Tableau decision-support dashboard that uncovers empirical patterns "
            "across student lifestyles, helping academic institutions offer proactive, timely support."
        )
    },
    {
        "id": "scene_03_dataset",
        "title": "Dataset Architecture & Source",
        "text": (
            "Our verified dataset contains exactly 200 student records across 18 multi-dimensional behavioral and academic variables. "
            "Each student is tracked from STU 0001 to STU 0200. Attributes include age, gender, clinical Anxiety and Depression "
            "scores from 0 to 100, categorical Stress Levels, daily screen time, sleep quality, and therapy pathways including CBT and Counseling."
        )
    },
    {
        "id": "scene_04_methodology",
        "title": "Data Preparation & Calculations",
        "text": (
            "Using Python and Pandas, we confirmed 100 percent data completeness with zero null values and zero duplicates. "
            "In Tableau Desktop, we engineered two vital calculated fields: First, Active Therapy, isolating students receiving structured care. "
            "Second, High Stress and Poor Sleep, flagging students suffering concurrently from acute stress and severe sleep disruption."
        )
    },
    {
        "id": "scene_05_kpi",
        "title": "Executive KPI Ribbon",
        "text": (
            "Transitioning to our live Tableau dashboard, the executive KPI ribbon establishes four cohort benchmarks across all 200 students: "
            "Total Students: exactly 200 undergraduates. Average Anxiety Score: 52.59 out of 100. Average Depression Score: 48.09 out of 100. "
            "And Average Daily Screen Time: 7.10 hours per day. These benchmarks ground our subsequent visual analysis."
        )
    },
    {
        "id": "scene_06_stress_dist",
        "title": "Worksheet 1: Stress Level Distribution",
        "text": (
            "Worksheet one examines the Stress Level Distribution across the cohort. 107 students, or 53.5 percent, experience Medium stress. "
            "49 students, or 24.5 percent, experience High stress, while 44 students, or 22 percent, report Low stress. "
            "Combined, over 78 percent of surveyed students operate under moderate to severe stress, proving this is a widespread campus challenge."
        )
    },
    {
        "id": "scene_07_screen_time",
        "title": "Worksheet 2: Screen Time vs Stress Level",
        "text": (
            "Worksheet two evaluates daily screen time against reported stress levels. A distinct upward trend emerges: students with Low stress "
            "average 6.00 hours of screen time. Medium stress students average 7.07 hours, while High stress students surge to 8.12 hours daily. "
            "High stress students spend over two additional hours on screens each day, highlighting digital fatigue."
        )
    },
    {
        "id": "scene_08_sleep_quality",
        "title": "Worksheet 3: Sleep Quality vs Stress Level",
        "text": (
            "Worksheet three explores Sleep Quality against Stress Level. Among students reporting Poor sleep, 35 out of 66 suffer from High stress, "
            "30 report Medium stress, and only one maintains Low stress. Conversely, among students with Good sleep quality, 22 report Low stress "
            "and only two report High stress. This confirms sleep quality as a vital resilience buffer."
        )
    },
    {
        "id": "scene_09_gender",
        "title": "Worksheet 4: Gender Mental Health Comparison",
        "text": (
            "Worksheet four benchmarks anxiety and depression across gender cohorts. Average anxiety remains evenly distributed: 53.32 for females, "
            "51.76 for males, and 53.50 for other cohorts. Depression scores follow a similar pattern: 48.10 for females, 47.88 for males, and 50.38 for others. "
            "This proves psychological strain is evenly shared across demographics, making lifestyle factors the key drivers."
        )
    },
    {
        "id": "scene_10_anxiety_depression",
        "title": "Worksheets 5 & 6: Stress vs Anxiety and Depression",
        "text": (
            "Worksheets five and six analyze how stress escalates into clinical symptoms. Anxiety scores rise steeply from 30.27 in Low stress, "
            "to 52.85 in Medium stress, reaching 72.06 in High stress. Similarly, depression scores escalate from 26.80 in Low stress to 68.78 in High stress, "
            "over two and a half times higher. Chronic stress reliably compounds into acute distress."
        )
    },
    {
        "id": "scene_11_therapy_prevalence",
        "title": "Worksheets 7 & 8: Therapy Efficacy and History Prevalence",
        "text": (
            "Worksheets seven and eight evaluate support modalities and mental health history. In Ranked Therapy Efficacy, Cognitive Behavioral Therapy leads "
            "with an average progress score of 40.80, followed by Counseling at 34.43 and Support Groups at 33.10. Meanwhile, exactly 40 percent of students, "
            "or 80 out of 200, report prior mental health history, urging early proactive screening."
        )
    },
    {
        "id": "scene_12_findings",
        "title": "Core Empirical Findings & Interpretation",
        "text": (
            "Synthesizing our observations yields three primary findings: First, Sleep Quality is the Paramount Protective Buffer against high stress. "
            "Second, Daily screen time exceeding 7.5 hours strongly co-occurs with elevated stress and anxiety. Third, Structured interventions like CBT "
            "deliver proven symptom progress compared to unguided coping. These signals provide actionable guidance for student welfare initiatives."
        )
    },
    {
        "id": "scene_13_website",
        "title": "Portfolio Website & Public Deployment",
        "text": (
            "To present this work professionally, I deployed a dedicated portfolio website on GitHub Pages featuring a modern editorial design. "
            "The site includes an Executive Hero section, an interactive Tableau embed with reload controls and fallback options, a complete Worksheet Gallery, "
            "an embedded HTML5 video player with captions, and direct links to our documentation."
        )
    },
    {
        "id": "scene_14_conclusion",
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
        # Natural collegiate presentation pace with warm acoustic resonance
        comm = edge_tts.Communicate(txt, voice="en-IN-PrabhatNeural", rate="+20%", pitch="-5Hz")
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
