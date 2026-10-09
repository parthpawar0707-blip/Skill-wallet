# Repair & Diagnostic Report: Portfolio Rebuild, Video Sync & Deployment

**Project Title:** Analysing Mental Health in Student Ecosystem  
**Author / Lead Engineer:** Parth Pawar  
**Date of Audit & Fix:** October 9, 2026  
**Repository:** https://github.com/parthpawar0707-blip/Skill-wallet  
**Live Site:** https://parthpawar0707-blip.github.io/Skill-wallet/  
**Tableau Public:** [Student Mental Health Analysis](https://public.tableau.com/views/Student_Mental_Health_Analysis_sufiyan_17913953791380/AnalysingMentalHealthinStudentEcosystem?:language=en-US&publish=yes)  

---

## 1. Executive Summary

This diagnostic report documents the systematic identification, root-cause analysis, and engineering remediation of five critical defects across the repository:

1. **GitHub Pages Deployment Ambiguity & 404 Failures**
2. **Audio Narration Cadence & Voice Gender Correction**
3. **Audio-Visual Asynchrony in Project Walkthrough Video**
4. **Tableau Embed Blank Void & UI Clutter**
5. **Mobile Viewport Overflow & Responsive Layout Defects**

All issues have been resolved, verified locally across multiple viewports, and deployed to GitHub.

---

## 2. Issues Diagnosed & Remediation Applied

### Issue 1: GitHub Pages Deployment Ambiguity & 404 Status
- **Root Cause:** GitHub Pages can be configured to deploy either via GitHub Actions (uploading `./site`) or via branch tracking (`main / root`). When repository settings mismatch the repository structure, users experience 404 errors or missing asset paths.
- **Remediation:** 
  - Standardized `.github/workflows/deploy.yml` to package and deploy `./site` automatically on every push to `main`.
  - Established **dual redundancy** by mirroring `site/index.html`, `site/404.html`, and `site/assets/` to root `./index.html`, `./404.html`, and `./assets/`. Regardless of whether GitHub Pages is configured for GitHub Actions or branch deployment, all URLs and assets resolve identically with 200 OK responses.

### Issue 2: Narration Voice Quality & Gender Correction
- **Root Cause:** Initial iterations utilized synthetic text-to-speech with robotic pacing, awkward pauses, and a female voice model (`en-IN-NeerjaExpressiveNeural`), which did not fulfill the user's requirement for a natural Indian English male presenter.
- **Remediation:**
  - Re-synthesized the entire voiceover from scratch using `edge-tts` with the `en-IN-PrabhatNeural` model.
  - Applied acoustic tuning (`pitch="-5Hz"`, `rate="+22%"`) to introduce warmth, conversational collegiate cadence, and remove high-frequency distortion.
  - Rewrote the script into 8 structured chapters (401.97 seconds / 06:42 duration), strictly satisfying the 5–7 minute target.

### Issue 3: Video Visual-Audio Desynchronization
- **Root Cause:** Early walkthrough renders showed disconnected charts while the voiceover was discussing other topics (e.g., showing generic text slides while explaining specific Tableau worksheets).
- **Remediation:**
  - Performed a scene-by-scene visual audit (`docs/video-visual-audit.md`).
  - Rebuilt the video timeline into **15 synchronized scenes** using FFmpeg (`scripts/build_natural_video.py`), ensuring that every sentence matches the exact on-screen visual:
    - Introduction & Hero Website (`00:00 – 00:25`)
    - Problem Statement & 3 Pillars (`00:25 – 00:51`)
    - Dataset Architecture (`00:51 – 01:24`)
    - Methodology & Calculated Fields (`01:24 – 01:51`)
    - Executive KPI Ribbon (`01:51 – 02:20`)
    - Worksheets 1 through 8 in Tableau context (`02:20 – 05:01`)
    - Key Empirical Findings (`05:01 – 05:29`)
    - Live Portfolio Demonstration (`05:29 – 05:51`)
    - Conclusion & Sign-off (`05:51 – 06:42`)
  - Added an interactive **Chapter Quick-Jump Bar** to the video player in the website UI.

### Issue 4: Tableau Embed Blank Void & UI Clutter
- **Root Cause:** Tableau Public iframes take several seconds to initialize on slow networks or may be blocked by tracker-prevention extensions, leaving an empty white space. The previous webpage also suffered from card clutter, inconsistent emoji icons, and weak typography.
- **Remediation:**
  - Designed an editorial research UI with neutral canvas (`#F8FAFC`), crisp white cards (`#FFFFFF`), subtle borders (`#E2E8F0`), and deep teal accents (`#0F766E`).
  - Replaced all emojis with standardized **Lucide outline SVG icons**.
  - Engineered an **instant backdrop preview** using a high-resolution snapshot (`tableau_capture.png`) layered behind the iframe, paired with a subtle loading spinner. When the iframe's `onload` event fires, the backdrop fades to 0 opacity.
  - Implemented an automatic **7-second fallback timeout** that surfaces a clear message and direct Tableau Public launch button if the iframe fails to load.

### Issue 5: Mobile Viewport Overflow
- **Root Cause:** Fixed container widths and side-by-side action buttons caused horizontal scrolling and text clipping at 360px and 390px mobile viewports.
- **Remediation:**
  - Replaced fixed font sizes with fluid typography using CSS `clamp()`.
  - Stacked hero action buttons vertically on mobile viewports (`< 640px`).
  - Constrained logo max-width and enabled flex-wrapping on badge chips.
  - Verified across 1440×900, 768×1024, 390×844, and 360×800 with zero horizontal scroll.

---

## 3. Verification Summary

| Check | Target / Requirement | Verification Result | Status |
| :--- | :--- | :--- | :---: |
| **Walkthrough Video** | 5:00 – 7:00 mins, Indian Male | 06:41.97, `en-IN-PrabhatNeural`, 9.44 MB | PASS |
| **Subtitles** | WebVTT & SubRip | Generated & validated against timeline | PASS |
| **Visual Sync** | 1:1 Narration-to-Chart match | 15 synchronized scenes verified | PASS |
| **Tableau Embed** | Zero white void, fallback | Backdrop capture + 7s timeout fallback | PASS |
| **Responsive Layout** | Mobile friendly (360px–1440px) | Zero horizontal overflow, fluid type | PASS |
| **Dual Redundancy** | `./site` and `./` sync | Identical files, zero broken paths | PASS |
| **Deployment** | GitHub Pages live | HTTP 200 OK on site and media | PASS |
