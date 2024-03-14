import fitz
my_path = f'D:/Python/projects/Resume-Analyser/resume_analyser/resumes/RESUME-FINAL.pdf'

doc = fitz.open(my_path)
for page in doc:
    text = page.get_text()
    print(text)