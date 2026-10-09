# Video Production & Technical Verification Notes

**Project Title:** Analysing Mental Health in Student Ecosystem | Complete Tableau Project Walkthrough  
**Presenter & Lead Analyst:** Parth Pawar  
**Date of Render:** 2026-10-09  
**Output Target:** GitHub Pages Static Analytics Portfolio & Web Video Player  

---

## 1. Video Specifications & Encoding Details

- **Container:** MP4 (ISO Base Media file format)
- **Video Codec:** H.264 / AVC (High Profile, level 3.1)
- **Resolution:** 1280 &times; 720 (16:9 Standard High Definition)
- **Frame Rate:** 30.0 fps (Progressive)
- **Pixel Format:** `yuv420p` (Universal browser & mobile hardware compatibility)
- **Audio Codec:** AAC (LC profile)
- **Audio Sample Rate:** 24,000 Hz, Mono
- **Audio Bitrate:** ~110–144 kb/s
- **Total Duration:** **401.97 seconds** (**06:41.97** — strictly within the 5:00 to 7:00 target window)
- **Total File Size:** **9,898,270 bytes** (~9.44 MB — lightweight, streamable, under GitHub 100MB limit)

---

## 2. Media Asset Manifest

| Asset Name | Repository Path | Size / Duration | Format / Purpose |
| :--- | :--- | :--- | :--- |
| **Walkthrough Video** | `site/assets/video/student-mental-health-demo.mp4` | 9.44 MB / 06:42 | Web-optimized H.264/AAC MP4 |
| **Master Narration** | `site/assets/video/narration.mp3` | 7.67 MB / 06:42 | Master voiceover track |
| **Video Poster (JPG)** | `site/assets/video/video-poster.jpg` | 79.3 KB | 1280&times;720 video splash frame |
| **Video Poster (PNG)** | `site/assets/images/video-poster.png` | 209.8 KB | High-fidelity site image asset |
| **Subtitles (SRT)** | `site/assets/video/video-captions.srt` | ~8.9 KB | Standard SubRip subtitle track |
| **Subtitles (WebVTT)** | `site/assets/video/video-captions.vtt` | ~8.9 KB | HTML5 WebVTT caption file |
| **Narration Script** | `docs/video-narration.md` | Verbatim text | Complete 8-chapter script |
| **Storyboard** | `docs/video-storyboard.md` | Scene breakdown | 15 synchronized scenes |
| **Visual Audit** | `docs/video-visual-audit.md` | Sync review | Audit of scene transitions |

---

## 3. Voice Generation & Audio Engineering

- **Voice Engine:** Microsoft Edge Neural Speech Synthesizer (`edge-tts`)
- **Voice Model:** `en-IN-PrabhatNeural` (Natural Indian English Male)
- **Pitch Tuning:** `pitch="-5Hz"` to provide acoustic warmth and eliminate high-frequency distortion.
- **Pacing Calibration:** `rate="+22%"` ensuring confident, articulate collegiate cadence with natural pauses.
- **Tone & Delivery:** Analytical, technical, and conversational Indian English appropriate for a data science portfolio walkthrough or viva presentation.
- **Terminology Quality:** Verified accurate pronunciation of key terms: *Tableau*, *Cognitive Behavioral Therapy*, *Anxiety Scores*, and *Decision Support*.

---

## 4. Visual Chapters & Tableau Chart Synchronization

The video is composed of 15 synchronized scenes matching the exact timing of the narration:

1. **Scene 1 (00:00 – 00:25):** Title Screen & Executive Welcome (Parth Pawar, Project Overview, Analytics Scope).
2. **Scene 2 (00:25 – 00:51):** Problem Statement & Student Pressures (Academic, lifestyle, and institutional support).
3. **Scene 3 (00:51 – 01:24):** Dataset Architecture & Source (200 records, 18 columns, User IDs `STU_0001`–`STU_0200`).
4. **Scene 4 (01:24 – 01:51):** Data Hygiene & Calculations (`Active_Therapy` and `HighStress_PoorSleep`).
5. **Scene 5 (01:51 – 02:20):** Tableau Executive KPI Ribbon (200 Students, 52.59 Anxiety, 48.09 Depression, 7.10 hrs Screen Time).
6. **Scene 6 (02:20 – 02:49):** Worksheet 1: Stress Level Distribution (Medium 107 [53.5%], High 49 [24.5%], Low 44 [22.0%]).
7. **Scene 7 (02:49 – 03:15):** Worksheet 2: Daily Screen Time vs Stress Level (Low 6.00 hrs, Med 7.07 hrs, High 8.12 hrs).
8. **Scene 8 (03:15 – 03:39):** Worksheet 3: Sleep Quality vs Stress Level (Poor sleep: 35 High, 30 Med, 1 Low; Good sleep: 22 Low, 2 High).
9. **Scene 9 (03:39 – 04:12):** Worksheet 4: Gender Mental Health Comparison (Anxiety: 53.32 F, 51.76 M, 53.50 O; Depression: 48.10 F, 47.88 M, 50.38 O).
10. **Scene 10 (04:12 – 04:41):** Worksheets 5 & 6: Stress vs Anxiety (30.27 &rarr; 72.06) & Depression (26.80 &rarr; 68.78).
11. **Scene 11 (04:41 – 05:01):** Worksheets 7 & 8: Therapy Efficacy (CBT 40.80, Counseling 34.43, Support Groups 33.10) & History Prevalence (40% / 80 students).
12. **Scene 12 (05:01 – 05:29):** Core Empirical Findings & Institutional Implications (Sleep buffer, Screen time threshold, CBT progress).
13. **Scene 13 (05:29 – 05:51):** Portfolio Website Walkthrough (Interactive embed, reload buttons, downloads).
14. **Scene 14 (05:51 – 06:15):** Summary, GitHub Repository Links, and Professional Sign-off.
15. **Scene 15 (06:15 – 06:42):** Credits, Acknowledgments, and Video Outro.

---

## 5. Website HTML5 Video Integration Verification

The video player is embedded at `#demo-video` in `site/index.html` (and mirrored at `./index.html`):
- Native `<video>` tag with `controls`, `preload="metadata"`, `playsinline`, and `poster="assets/video/video-poster.jpg"`.
- Synchronized WebVTT caption track: `<track kind="captions" src="assets/video/video-captions.vtt" srclang="en" label="English" default>`.
- Secondary direct download button pointing to `assets/video/student-mental-health-demo.mp4`.
- Fully responsive 16:9 aspect ratio container (`.video-player-wrapper`).
- Interactive **Chapter Quick-Jump Bar** with 8 clickable timestamp pills (`00:00`, `00:45`, `01:30`, `02:15`, `03:00`, `03:45`, `04:30`, `05:30`) wired via JavaScript to seek the video player immediately.
