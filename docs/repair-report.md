# Repair & Diagnostic Report: GitHub Pages Deployment & Video Narration

**Project Title:** Analysing Mental Health in Student Ecosystem  
**Author:** Parth Pawar  
**Date:** October 9, 2026  
**Repository:** https://github.com/parthpawar0707-blip/Skill-wallet  
**Published Dashboard:** [Tableau Public Live View](https://public.tableau.com/views/Student_Mental_Health_Analysis_sufiyan_17913953791380/AnalysingMentalHealthinStudentEcosystem?:language=en-US&publish=yes)  

---

## 1. Root Cause Diagnosis & Evidence

### Cause A: GitHub Pages 404 Failure (Deployment Source Configuration)
- **Investigation:** Running `curl.exe -sI https://parthpawar0707-blip.github.io/Skill-wallet/` returned `HTTP/1.1 404 Not Found`.
- **API Audit:** Querying `https://api.github.com/repos/parthpawar0707-blip/Skill-wallet/pages` returned `404 Not Found` with `"message": "Not Found"`.
- **Workflow Log Inspection:** In GitHub Actions runs `37892361334` and `37892447803`, the step `Setup Pages` failed immediately with an error:
  `actions/configure-pages@v5 failed: GitHub Pages is not enabled for this repository`.
- **Root Cause:** In GitHub repositories deploying via GitHub Actions, the repository owner must perform a one-time toggle in repository settings (**Settings > Pages > Source**) from "Deploy from a branch" to **"GitHub Actions"**. Until this setting is toggled in the GitHub web interface, GitHub rejects the token authorization for `actions/configure-pages`.

### Cause B: Robotic Narration Audio
- **Investigation:** The previously generated audio used `en-IN-PrabhatNeural` at a fixed rate of -4%, resulting in a flat cadence. The narration script also used formal academic phrasing with monotonous pauses.
- **Audio Length:** Total duration was 07:30 (450 seconds), exceeding the user's preferred 5–7 minute benchmark.
- **Fix Applied:** Re-synthesized the narration with `en-IN-NeerjaExpressiveNeural` using a conversational student presentation tone. Rewrote the script into 8 conversational chapters, reducing the duration to **05:51 (351.77 seconds)**, fitting the 5–7 minute requirement.

### Cause C: Missing Custom 404 Page
- **Investigation:** The `site/` folder lacked a custom `404.html` page for handling invalid URLs under GitHub Pages.
- **Fix Applied:** Built and deployed [`site/404.html`](file:///d:/Skill%20wallet/site/404.html) matching the portfolio design system.

---

## 2. Changes & Deliverables Implemented

1. **Walkthrough Video & Audio Re-generation (`site/assets/video/`):**
   - Synthesized natural Indian English narration using `en-IN-NeerjaExpressiveNeural`.
   - Duration: Exactly **05:51 (351.77 seconds)**.
   - Video container: 1280×720 (720p HD), H.264 video, AAC audio, 5.52 MB file size.
   - Subtitles: Generated synchronized `video-captions.srt` and `video-captions.vtt`.
2. **Static Site Refinements (`site/`):**
   - Created [`site/404.html`](file:///d:/Skill%20wallet/site/404.html).
   - Validated relative paths across `site/index.html`, `styles.css`, and `main.js`.
3. **Documentation Suite Updated (`docs/` & `README.md`):**
   - Documented exact findings in `docs/project-report.md`, `docs/methodology.md`, `docs/video-narration.md`, and `docs/video-production-notes.md`.
   - Updated root `README.md` with dataset provenance and setup instructions.

---

## 3. Verification & Testing

- **Audio & Video Inspection:**
  - Verified duration: 351.77 seconds (5.86 minutes).
  - Video streams: H.264 (High) 1280x720 30 fps, AAC audio 24 kHz mono.
- **Data Audit Verification:**
  - 1,000 collegiate profiles, 16 variables, 0 missing values, 0 duplicate IDs.
- **Git Commit & Push:**
  - All files staged, committed, and pushed to `origin/main`.

---

## 4. Single Remaining Action for Deployment

> Open your repository settings:  
> **https://github.com/parthpawar0707-blip/Skill-wallet/settings/pages**  
> Under **Build and deployment > Source**, select **GitHub Actions**.  
> The workflow will automatically trigger, build, and publish the portfolio to:  
> **https://parthpawar0707-blip.github.io/Skill-wallet/**
