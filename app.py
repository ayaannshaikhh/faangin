import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from pdfminer.high_level import extract_text
import google.generativeai as genai
import markdown as md
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
chat = genai.GenerativeModel("gemini-2.0-flash")

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
app.secret_key = 'your-secret-key'  # Required for flash messages

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'pdf'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_pdf_text(file_path):
    try:
        return extract_text(file_path)
    except Exception as e:
        return f"Error reading PDF: {e}"

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Extract PDF text and send to Gemini
            resume_text = extract_pdf_text(file_path)
            prompt = f"""
            You're a career coach for tech internships.

            Here is a resume:

            {resume_text}

            Analyze it and return:

            ## I. Overall Impression

            ## II. Strengths

            ## III. Weaknesses

            ## IV. Recommendations (Actionable Steps)

            ## V. Example Revisions

            Keep everything concise please do not overdo it.
            """
            response = chat.generate_content(prompt)
            raw_feedback = response.text
            html_feedback = md.markdown(raw_feedback)

            return render_template("results.html", feedback=html_feedback)

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
