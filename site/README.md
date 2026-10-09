# Static Site Documentation

This directory contains the production-ready static website deployed to **GitHub Pages** via the automated GitHub Actions workflow in `.github/workflows/deploy.yml` (and mirrored to root `./` for dual-redundancy deployment).

## Directory Contents
- `index.html`: Responsive 11-section portfolio web page with live Tableau Public embed, KPI scorecards, video walkthrough player with chapter quick-jump navigation, and documentation links.
- `404.html`: Custom 404 page for missing or broken routes.
- `assets/css/styles.css`: Custom responsive styling (editorial design system: off-white background, deep navy typography, Lucide SVG icons, and teal accents).
- `assets/js/main.js`: Mobile navigation handling, smooth scrolling, video chapter seeking, and Tableau Public fallback logic.
- `assets/data/summary.json`: Verified aggregate statistics from the 200-student Tableau extract (protects student privacy by avoiding raw text exposure).
- `assets/video/`:
  - `student-mental-health-demo.mp4`: 720p HD video walkthrough narrated in natural Indian English male voice (`en-IN-PrabhatNeural`, 06:42 duration).
  - `narration.mp3`: Indian English audio narration track.
  - `video-poster.jpg` / `video-poster.png`: Splash poster frame.
  - `video-captions.srt`: Synchronized subtitle track (SubRip format).
  - `video-captions.vtt`: WebVTT subtitle track for HTML5 `<video>` element.
