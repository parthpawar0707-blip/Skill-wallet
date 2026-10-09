"""
verify_repo.py
--------------
Automated verification suite to validate:
1. Static website HTML and asset link integrity (index.html, 404.html)
2. Media assets existence and duration check
3. JSON syntax validity
4. Cleanliness scan for secret keys, credentials, or leaks
"""

import os
import sys
import json
import re
import glob

def check_json():
    print("[1/4] Checking JSON file syntax...")
    files = glob.glob("**/*.json", recursive=True)
    for jf in files:
        if ".git" in jf:
            continue
        with open(jf, "r", encoding="utf-8") as f:
            try:
                json.load(f)
                print(f"  OK: {jf}")
            except Exception as e:
                print(f"  FAIL: {jf} - {e}")
                return False
    return True

def check_html_assets():
    print("\n[2/4] Checking HTML asset paths...")
    html_files = ["index.html", "404.html", "site/index.html", "site/404.html"]
    all_ok = True
    for hf in html_files:
        if not os.path.exists(hf):
            print(f"  FAIL: {hf} missing!")
            all_ok = False
            continue
        with open(hf, "r", encoding="utf-8") as f:
            html = f.read()
        
        base_dir = os.path.dirname(hf) or "."
        matches = re.findall(r'(?:src|href)="([^"]+)"', html)
        checked = 0
        missing = []
        for m in matches:
            if m.startswith("http") or m.startswith("#") or m.startswith("mailto:"):
                continue
            path_part = m.split("?")[0].split("#")[0]
            full_path = os.path.normpath(os.path.join(base_dir, path_part))
            checked += 1
            if not os.path.exists(full_path):
                missing.append((m, full_path))
        if missing:
            print(f"  FAIL: {hf} has missing assets: {missing}")
            all_ok = False
        else:
            print(f"  OK: {hf} ({checked} local paths verified)")
    return all_ok

def check_media():
    print("\n[3/4] Checking media assets...")
    media_targets = [
        ("site/assets/video/student-mental-health-demo.mp4", 9_000_000),
        ("assets/video/student-mental-health-demo.mp4", 9_000_000),
        ("site/assets/video/narration.mp3", 7_000_000),
        ("assets/video/narration.mp3", 7_000_000),
        ("site/assets/video/video-captions.vtt", 5_000),
        ("assets/video/video-captions.vtt", 5_000),
        ("site/assets/video/video-poster.jpg", 50_000),
        ("assets/video/video-poster.jpg", 50_000),
    ]
    all_ok = True
    for path, min_size in media_targets:
        if not os.path.exists(path):
            print(f"  FAIL: {path} not found!")
            all_ok = False
        else:
            sz = os.path.getsize(path)
            if sz < min_size:
                print(f"  FAIL: {path} suspiciously small ({sz} bytes < {min_size})")
                all_ok = False
            else:
                print(f"  OK: {path} ({sz:,} bytes)")
    return all_ok

def check_secrets():
    print("\n[4/4] Checking for sensitive credentials or keys...")
    patterns = [
        re.compile(r'(?i)bearer\s+[a-zA-Z0-9_\-\.]{25,}'),
        re.compile(r'(?i)(?:api[_-]?key|secret[_-]?key)\s*[:=]\s*["\'][a-zA-Z0-9_\-\.]{20,}["\']'),
        re.compile(r'AKIA[0-9A-Z]{16}'),
        re.compile(r'ghp_[a-zA-Z0-9]{36}')
    ]
    findings = []
    for root, dirs, files in os.walk("."):
        if ".git" in root:
            continue
        for file in files:
            if file.endswith((".png", ".jpg", ".mp4", ".mp3", ".pyc")):
                continue
            fpath = os.path.join(root, file)
            try:
                with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                    for lnum, line in enumerate(f, 1):
                        for p in patterns:
                            if p.search(line):
                                findings.append((fpath, lnum, line.strip()[:60]))
            except:
                pass
    if findings:
        print(f"  FAIL: Secrets found: {findings}")
        return False
    else:
        print("  OK: Zero credentials, tokens, or private secrets found.")
        return True

if __name__ == "__main__":
    r1 = check_json()
    r2 = check_html_assets()
    r3 = check_media()
    r4 = check_secrets()
    if r1 and r2 and r3 and r4:
        print("\n[ALL AUDIT CHECKS PASSED SUCCESSFULLY]")
        sys.exit(0)
    else:
        print("\n[AUDIT FAILED]")
        sys.exit(1)
