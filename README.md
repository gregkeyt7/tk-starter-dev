# TK Starter Dev Repo

Three quick, recruiter-friendly proofs of skill:

1. **Website (HTML/CSS)** — a simple, responsive portfolio page (./website).
2. **Python Automation** — cleans a messy CSV into a normalized CSV (./python_automation).
3. **Flask To‑Do App** — minimal CRUD web app using Flask + SQLite (./flask_todo).

---

## Quick Start (copy/paste)

### 0) Clone & set up
```bash
# If you haven't already, create a GitHub repo named tk-starter-dev, then do:
git clone https://github.com/YOUR_USERNAME/tk-starter-dev.git
cd tk-starter-dev
```

### 1) Website
```bash
cd website
# Open index.html in your browser by double‑clicking it,
# or serve locally with Python:
python -m http.server 8080
# Visit http://localhost:8080
```

### 2) Python Automation
```bash
cd ../python_automation
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python clean_claims.py input_sample.csv output_clean.csv
# Check the new file output_clean.csv
```

### 3) Flask To‑Do App
```bash
cd ../flask_todo
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
# Visit http://127.0.0.1:5000
```

### 4) Push to GitHub
```bash
# From the repo root (tk-starter-dev)
git init
git add .
git commit -m "Initial commit: website + python automation + flask todo"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/tk-starter-dev.git
git push -u origin main
```

---

## What Recruiters See
- Clean, simple HTML/CSS.
- Practical Python for data cleanup.
- A minimal Flask CRUD app showing web fundamentals.
- Clear README with copy/paste commands (fast verification).

---

## Next Steps
- Replace placeholder text with your details (name, LinkedIn, GitHub).
- Add a screenshot of the Flask app to this README.
- Extend the automation script to handle your real insurance spreadsheets.
