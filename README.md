# 🧠 FAANGin — Resume Analyzer for FAANG Internships

FAANGin is a modern web app that allows users to upload their resume (PDF) and receive AI-powered feedback tailored for FAANG-style internship applications. It uses Google Gemini to analyze resume content and return strengths, weaknesses, and actionable suggestions.

---

## 🚀 Features

- 🔍 Upload and analyze PDF resumes
- 🧠 AI-generated career coaching feedback using Gemini API
- 🎯 Focused on conciseness, quantifiable impact, and technical storytelling
- 🌙 Clean, dark-themed UI using Tailwind CSS
- 🧾 Markdown-to-HTML rendering for structured AI output

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **AI/NLP:** Google Gemini (Generative AI)
- **PDF Parsing:** `pdfminer.six`
- **Frontend:** HTML + Tailwind CSS (dark mode)
- **Markdown Rendering:** `markdown` Python module
- **Environment Management:** `dotenv`

---

## 📦 Installation

```bash
git clone https://github.com/ayaannshaikhh/faangin.git
cd faangin
python3 -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 🔐 Setup

Create a `.env` file in the root of your project:

```
GEMINI_API_KEY=your_gemini_api_key_here
SECRET_KEY=your_flask_secret_key
```

---

## ▶️ Running the App

```bash
flask run
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 📁 Folder Structure

```
faangin/
├── app.py
├── templates/
│   ├── index.html
│   └── results.html
├── uploads/
│   └── (user-uploaded PDFs)
├── .env
└── requirements.txt
```

---

## 📄 Example Output

The app returns AI-powered feedback like:

- **Strengths**: Well-structured projects, strong technical stack
- **Weaknesses**: No quantifiable results, vague leadership impact
- **Suggestions**: Use stronger action verbs, add metrics, restructure skills section

---

## 🌐 Live Demo

_(Coming soon)_

---

## 📌 License

MIT License — feel free to fork, improve, and use it for your portfolio.

---
