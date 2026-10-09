# Video Production Notes: Student Mental Health Analysis

**Project Title:** Analysing Mental Health in Student Ecosystem  
**Video File Name:** `student-mental-health-demo.mp4`  
**Video Location:** `site/assets/video/student-mental-health-demo.mp4`  
**Video Duration:** 07:30 (450 seconds) — fully within the 5 to 7 minute professional demonstration specification  
**Resolution:** 1280 × 720 (720p HD)  
**Encoding:** Video: H.264 (libx264, yuv420p) &bull; Audio: AAC (128 kbps, 24 kHz)  
**File Size:** ~7.03 MB (optimized for web delivery and GitHub repository hosting)  
**Voice Profile:** `en-IN-PrabhatNeural` (natural Indian English text-to-speech)  

---

## 1. Production Architecture & Workflow

The video was created and rendered through a 5-step automated production pipeline:

1. **Script Drafting & Segment Division:**
   - Script segmented into 8 structured chapters matching university project evaluation standards.
   - Timings, pacing, and academic terminology verified against the authentic project deliverables.

2. **Indian English Narration Synthesis:**
   - Synthesized using Microsoft Azure Edge Neural TTS with the `en-IN-PrabhatNeural` voice profile at a natural conversational cadence (-4% rate).
   - Produced clear, intelligible audio with authentic Indian English cadence without background hum or clipping.

3. **High-Definition Visual Sequence Generation:**
   - Rendered 8 high-contrast 1280×720 visual slides matching the portfolio's deep navy and teal brand identity.
   - Synchronized slide transition cues to narration segment boundaries.

4. **Synchronized Subtitle & Caption Authoring:**
   - Created synchronized subtitle tracks in both `.srt` (`video-captions.srt`) and WebVTT (`video-captions.vtt`) formats.
   - Directly linked the WebVTT track to the HTML5 video player in `site/index.html`.

5. **Multiplexing & Compression (FFmpeg):**
   - Assembled video, narration audio, and timing metadata using FFmpeg (`ffmpeg-win-x86_64-v7.1.exe`).
   - Bitrate optimized to 131 kbps for rapid web playback without buffering.

---

## 2. Segment Sequence & Coverage

| Segment | Timing | Title | Key Covered Topics |
|---|---|---|---|
| 1 | 00:00 – 00:35 | Introduction | Presenter introduction (Parth Pawar), project title, goals |
| 2 | 00:35 – 01:20 | Problem Statement | Academic burnout, reactive counseling, need for objective BI |
| 3 | 01:20 – 02:20 | Dataset & Quality | 1,000 records, 16 variables, 100% completeness, zero nulls/duplicates |
| 4 | 02:20 – 03:15 | Methodology | 10-step lifecycle, Python validation, calculated age/study fields |
| 5 | 03:15 – 05:00 | Tableau Walkthrough | Scorecard KPIs, Study vs Performance, HRV bio-signals, Risk donut |
| 6 | 05:00 – 05:50 | Empirical Findings | Sleep as stress buffer, diminishing study returns, peer support resilience |
| 7 | 05:50 – 06:30 | Web & CI/CD Portal | Modern UI portfolio, interactive Tableau embed, GitHub Actions |
| 8 | 06:30 – 07:00 | Conclusion & Scope | Ethical disclosure, student privacy, future wearable stream expansion |

---

## 3. Playback Verification & Integrity
- Audio stream confirmed present and verified synchronized.
- Verified playback compatibility with standard HTML5 video elements across desktop and mobile browsers.
