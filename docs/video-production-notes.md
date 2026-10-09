# Video Production & Technical Verification Notes

**Project Title:** Analysing Mental Health in Student Ecosystem | Complete Tableau Project Walkthrough  
**Presenter:** Parth Pawar  
**Date of Render:** 2026-10-09  
**Output Target:** GitHub Pages Static Analytics Portfolio  

---

## 1. Video Specifications & Encoding Details

- **Container:** MP4 (ISO Base Media file format)
- **Video Codec:** H.264 / AVC (High Profile, level 3.1)
- **Resolution:** 1280 × 720 (16:9 Standard High Definition)
- **Frame Rate:** 30.0 fps (Progressive)
- **Pixel Format:** `yuv420p` (Universal browser & mobile hardware compatibility)
- **Audio Codec:** AAC (LC profile)
- **Audio Sample Rate:** 24,000 Hz, Mono
- **Audio Bitrate:** ~110–144 kb/s
- **Total Duration:** 375.05 seconds (06:15.05 — exactly within the 5:45 to 6:30 target window)
- **Total File Size:** 9,119,503 bytes (~8.70 MB — lightweight, streamable, under GitHub 100MB limit)

---

## 2. Media Asset Manifest

| Asset Name | Repository Path | Size / Duration | Format / Purpose |
| :--- | :--- | :--- | :--- |
| **Walkthrough Video** | `site/assets/video/student-mental-health-demo.mp4` | 8.70 MB / 06:15 | Web-optimized H.264/AAC MP4 |
| **Master Narration** | `site/assets/video/narration.mp3` | 7.50 MB / 06:15 | Master voiceover track |
| **Video Poster (JPG)** | `site/assets/video/video-poster.jpg` | 79.9 KB | 1280×720 video splash frame |
| **Video Poster (PNG)** | `site/assets/images/video-poster.png` | 209.8 KB | High-fidelity site image asset |
| **Subtitles (SRT)** | `site/assets/video/video-captions.srt` | ~8.8 KB | Standard SubRip subtitle track |
| **Subtitles (WebVTT)** | `site/assets/video/video-captions.vtt` | ~8.8 KB | HTML5 WebVTT caption file |
| **Narration Script** | `docs/video-narration.md` | Verbatim text | Complete 14-chapter script |
| **Dashboard Inventory** | `docs/tableau-dashboard-inventory.md` | Verified metrics | Structural workbook breakdown |

---

## 3. Voice Generation & Audio Engineering

- **Voice Engine:** Microsoft Edge Neural Speech Synthesizer (`edge-tts`)
- **Voice Selected:** `en-IN-PrabhatNeural` (Natural Indian English Male)
- **Pitch Tuning:** `pitch="-5Hz"` to provide warm acoustic resonance and remove any high-frequency or robotic distortion.
- **Pacing Calibration:** `rate="+20%"` ensuring crisp, confident collegiate speech with natural sentence breaks.
- **Speech Style:** Confident, technical, and conversational Indian English suitable for an Indian university data science portfolio presentation or viva.
- **Pronunciation & Terminology:** Validated natural delivery for technical vocabulary including *Tableau*, *Cognitive Behavioral Therapy*, *Anxiety Scores*, and *Decision Support*.

---

## 4. Visual Chapters & Tableau Chart Synchronization

The video is divided into 14 synchronized scenes matching the exact timing of the narration:

1. **Scene 1 (00:00 – 00:23):** Title Screen & Executive Overview (Parth Pawar, Project Title, Analytics Scope).
2. **Scene 2 (00:23 – 00:49):** Problem Statement & Student Pressures (Academic, lifestyle, and institutional support).
3. **Scene 3 (00:49 – 01:16):** Dataset Architecture & Source (200 records, 18 columns, User IDs `STU_0001`–`STU_0200`).
4. **Scene 4 (01:16 – 01:40):** Data Hygiene & Calculations (`Active_Therapy` and `HighStress_PoorSleep`).
5. **Scene 5 (01:40 – 02:11):** Tableau Executive KPI Ribbon (200 Students, 52.59 Anxiety, 48.09 Depression, 7.10 hrs Screen Time).
6. **Scene 6 (02:11 – 02:39):** Worksheet 1: Stress Level Distribution (Medium 107 [53.5%], High 49 [24.5%], Low 44 [22%]).
7. **Scene 7 (02:39 – 03:06):** Worksheet 2: Daily Screen Time vs Stress Level (Low 6.00 hrs, Med 7.07 hrs, High 8.12 hrs).
8. **Scene 8 (03:06 – 03:31):** Worksheet 3: Sleep Quality vs Stress Level (Poor sleep: 35 High, 30 Med, 1 Low; Good sleep: 22 Low, 2 High).
9. **Scene 9 (03:31 – 04:04):** Worksheet 4: Gender Mental Health Comparison (Anxiety: 53.32 F, 51.76 M, 53.50 O; Depression: 48.10 F, 47.88 M, 50.38 O).
10. **Scene 10 (04:04 – 04:33):** Worksheets 5 & 6: Stress vs Anxiety (30.27 -> 72.06) & Depression (26.80 -> 68.78).
11. **Scene 11 (04:33 – 05:01):** Worksheets 7 & 8: Therapy Efficacy (CBT 40.80, Counseling 34.43, Support Groups 33.10) & History Prevalence (40% / 80 students).
12. **Scene 12 (05:01 – 05:29):** Core Empirical Findings & Institutional Implications (Sleep buffer, Screen time threshold, CBT progress).
13. **Scene 13 (05:29 – 05:51):** Portfolio Website Walkthrough (Interactive embed, reload buttons, downloads).
14. **Scene 14 (05:51 – 06:15):** Summary, GitHub Repository Links, and Professional Sign-off.

---

## 5. Website HTML5 Video Integration Verification

The video player is embedded at `#demo-video` in `site/index.html` with:
- Native `<video>` tag with `controls`, `preload="metadata"`, `playsinline`, and `poster="assets/video/video-poster.jpg"`.
- Synchronized WebVTT caption track `<track kind="captions" src="assets/video/video-captions.vtt" srclang="en" label="English" default>`.
- Secondary download link pointing to `assets/video/student-mental-health-demo.mp4`.
- Fully responsive 16:9 aspect ratio container (`.video-player-wrapper`).
