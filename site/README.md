# Static Site Documentation

This directory contains the production-ready static website deployed to **GitHub Pages** via the automated GitHub Actions workflow in `.github/workflows/deploy.yml`.

## Directory Contents
- `index.html`: Responsive portfolio web page with live Tableau Public embed, KPI scorecards, video walkthrough player, and documentation links.
- `assets/css/styles.css`: Custom responsive styling (clean light background, deep navy typography, and teal accents).
- `assets/js/main.js`: Mobile navigation handling, smooth scrolling, and Tableau Public fallback logic.
- `assets/data/summary.json`: Verified aggregate statistics from the 1,000 student dataset (protects student privacy by avoiding raw text exposure).
- `assets/video/`:
  - `student-mental-health-demo.mp4`: 720p HD video walkthrough narrated in natural Indian English (7m 30s).
  - `narration.mp3`: Indian English audio narration track (`en-IN-PrabhatNeural`).
  - `video-captions.srt`: Synchronized subtitle track (SRT format).
  - `video-captions.vtt`: WebVTT subtitle track for HTML5 `<video>` element.
