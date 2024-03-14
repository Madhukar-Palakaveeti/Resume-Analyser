import fitz
from docx import Document
my_path = f'D:/Python/projects/Resume-Analyser/resume_analyser/resumes/RESUME-FINAL.pdf'

doc = fitz.open(my_path)
for page in doc:
    text = page.get_text()
    print(text)

doc = Document('resume_analyser\static\MadhukarPalakaveetiAllRes.docx')
print('\n'.join([p.text for p in doc.paragraphs]))