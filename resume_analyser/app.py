from openai import OpenAI
from flask import Flask, session, render_template, request, flash, redirect, url_for
import fitz


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'doc', 'docx'}
app = Flask(__name__)
client = OpenAI()
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
                file.save(f'D:/Python/projects/Resume-Analyser/resume_analyser/resumes/{file.filename}')
                
                resume_text = session.get('text')
                
                my_path = f'D:/Python/projects/Resume-Analyser/resume_analyser/resumes/{file.filename}'
                doc = fitz.open(my_path)
                for page in doc:
                    resume_text += page.get_text()

                response = client.chat.completions.create(
                    model= "gpt-3.5-turbo",
                    messages=[
                        {"role" : "user",
                         "content" : resume_text + "Give me a feedback on the resume.Please focus more on the technical skills and which role it suits more.",
                        }                   
                    ]
                )

            return response.choices[0].message.content 

        else:
            flash('No file provided!')
            return redirect(url_for('index'))
    session.clear()

app.run(debug=True)