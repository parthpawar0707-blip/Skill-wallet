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
- **Audio Bitrate:** ~112–144 kb/s
- **Total Duration:** 382.08 seconds (06:22.08 — strictly within the 5 to 7 minute requirement)
- **Total File Size:** 9,361,711 bytes (~8.93 MB — lightweight, streamable, under GitHub 100MB limit)

---

## 2. Media Asset Manifest

| Asset Name | Repository Path | Size / Duration | Format / Purpose |
| :--- | :--- | :--- | :--- |
| **Walkthrough Video** | `site/assets/video/student-mental-health-demo.mp4` | 8.93 MB / 06:22 | Web-optimized H.264/AAC MP4 |
| **Master Narration** | `site/assets/video/narration.mp3` | 7.64 MB / 06:22 | Master voiceover track |
| **Video Poster (JPG)** | `site/assets/video/video-poster.jpg` | 79.9 KB | 1280×720 video splash frame |
| **Video Poster (PNG)** | `site/assets/images/video-poster.png` | 209.8 KB | High-fidelity site image asset |
| **Subtitles (SRT)** | `site/assets/video/video-captions.srt` | 13.2 KB | Standard SubRip subtitle track |
| **Subtitles (WebVTT)** | `site/assets/video/video-captions.vtt` | 12.8 KB | HTML5 WebVTT caption file |
| **Narration Script** | `docs/video-narration.md` | Verbatim text | Complete 8-chapter script |
| **Dashboard Inventory** | `docs/tableau-dashboard-inventory.md` | Verified metrics | Structural workbook breakdown |

---

## 3. Voice Generation & Audio Engineering

- **Voice Engine:** Microsoft Edge Neural Speech Synthesizer (`edge-tts`)
- **Voice Selected:** `en-IN-PrabhatNeural` (Natural Indian English)
- **Speech Style:** Confident, technical, and conversational Indian English suitable for an Indian university data science portfolio presentation.
- **Pronunciation & Terminology:** Validated natural delivery for technical vocabulary including *Tableau*, *Heart Rate Variability*, *Cognitive Behavioral Therapy*, *Anxiety Scores*, and *Decision Support*.
- **Tempo Tuning:** Calibrated at `rate="+30%"` with standard `ThreadedResolver` DNS dispatch to ensure smooth rhythm, natural pauses, and precise alignment within the 5–7 minute target window.

---

## 4. Visual Chapters & Tableau Chart Synchronization

The video is divided into 14 synchronized scenes matching the exact timing of the narration:

1. **Scene 1 (00:00 – 00:25):** Title Screen & Executive Overview (Parth Pawar, Project Title, Analytics Scope).
2. **Scene 2 (00:25 – 00:51):** Problem Statement & Student Pressures (Academic, lifestyle, and institutional support).
3. **Scene 3 (00:51 – 01:21):** Dataset Architecture & Source (200 records, 18 columns, User IDs `STU_0001`–`STU_0200`).
4. **Scene 4 (01:21 – 01:48):** Data Hygiene & Calculations (`Active_Therapy` and `HighStress_PoorSleep`).
5. **Scene 5 (01:48 – 02:17):** Tableau Executive KPI Ribbon (200 Students, 52.59 Anxiety, 48.09 Depression, 7.10 hrs Screen Time).
6. **Scene 6 (02:17 – 02:45):** Worksheet 1: Stress Level Distribution (Medium 107 [53.5%], High 49 [24.5%], Low 44 [22%]).
7. **Scene 7 (02:45 – 03:12):** Worksheet 2: Daily Screen Time vs Stress Level (Low 6.00 hrs, Med 7.07 hrs, High 8.12 hrs).
8. **Scene 8 (03:12 – 03:37):** Worksheet 3: Sleep Quality vs Stress Level (Poor sleep: 35 High / 30 Med / 1 Low; Good sleep: 2 High / 22 Low).
9. **Scene 9 (03:37 – 04:09):** Worksheet 4: Gender Mental Health Comparison (Female 53.3/48.1, Male 51.8/47.9, Other 53.5/50.4).
10. **Scene 10 (04:09 – 04:39):** Worksheets 5 & 6: Stress vs Anxiety (30.27 to 72.06) & Depression (26.80 to 68.78).
11. **Scene 11 (04:39 – 05:09):** Worksheets 7 & 8: Ranked Therapy Efficacy (CBT 40.80, Counseling 34.43, Support Group 33.10) & History Prevalence (60% No, 40% Yes).
12. **Scene 12 (05:09 – 05:37):** Empirical Findings & Strategic Interpretation (Sleep buffer, digital fatigue threshold, CBT outcomes).
13. **Scene 13 (05:37 – 05:59):** Portfolio Website Demonstration (Live embed, Gallery, Video player, Docs).
14. **Scene 14 (05:59 – 06:22):** Conclusion & Closing Screen (Author credits, Tableau Public URL, GitHub repository link).

---

## 5. Website Embedding & Validation

The video player is embedded in [site/index.html](file:///d:/Skill%20wallet/site/index.html) as an HTML5 responsive media component:

```html
<video 
  class="video-player" 
  controls 
  preload="metadata"
  poster="assets/video/video-poster.jpg"
  playsinline>
  <source src="assets/video/student-mental-health-demo.mp4" type="video/mp4">
  <track label="English" kind="subtitles" srclang="en" src="assets/video/video-captions.vtt" default>
  Your browser does not support HTML5 video playback.
</video>
```

- **Player Black Box Elimination:** The `poster="assets/video/video-poster.jpg"` attribute guarantees that modern browsers render the branded title slide immediately upon page load without showing an empty black frame.
- **Subtitles:** The WebVTT caption file is linked and configured as `default` for accessibility.
- **Direct Download:** A direct download button enables offline viewing of the MP4 file.
