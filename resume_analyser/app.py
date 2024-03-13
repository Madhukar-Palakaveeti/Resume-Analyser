from openai import OpenAI
from flask import Flask, session, render_template, request, flash, redirect, url_for
from PyPDF2 import PdfReader


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'doc', 'docx'}
app = Flask(__name__)
app.secret_key = "dvmsioadjlf"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyse', methods=['GET', 'POST'])
def analyse():
    session['text'] = ""
    if request.method == 'POST':
        if 'resume' in request.files:
            file = request.files['resume']
            if file.filename == '':
                flash('Resume not selected!')
                return redirect(url_for('index'))
            
            if file and allowed_file(file.filename):
                file.save(f'D:/Python/projects/resume_analyser/resume_analyser/resume_analyser/resumes/{file.filename}')
                
                resume_text = session.get('text')
                reader =  PdfReader(f'D:/Python/projects/resume_analyser/resume_analyser/resume_analyser/resumes/{file.filename}')
                for i in range(len(reader.pages)):
                    resume_text += reader.pages[i].extract_text()

                return resume_text
        else:
            flash('No file provided!')
            return redirect(url_for('index'))
    session.clear()

app.run(debug=True).