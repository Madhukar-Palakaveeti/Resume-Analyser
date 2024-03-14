# Resume Analysis using openAI chat completions api


This is a Flask web application that allows users to upload their resumes and receive feedback on them using the OpenAI GPT-3.5 model.

## Features
- Users can upload resumes in various formats such as PDF, DOC, and DOCX.
- The application extracts text from the uploaded resumes.
- The extracted text is sent to the OpenAI GPT-3.5 model to generate feedback on the resume.
- Users receive feedback on their resumes, focusing on technical skills and suitability for different roles.

## Packages used
1. openai
    - Used to send the user resume with the prompt for feedback
    - response received is a resume feedback 

2. Flask
    - Used for handling the api requests and web server.

3. pymupdf
    - used to read the resume as a pdf format and extract text

4. python-docx
    - used to read the resume as a docx format and extract text


## Installation
1. Clone the repository to your local machine.
2. Install the required Python packages listed in the poetry.lock using `poetry install`
3. Configure the poetry virtual environment in your IDE
4. Setup the openAI secret key by signing up for an openAI account
5. Follow the instructions and setup the secret key as an environment variable

## Usage
1. Run the app.py in ur IDE or use `python run app.py`
2. Open the webbrowser and navigate to `http://localhost:5000` to access the application.
3. Upload your resume using the provided form.
4. Receive feedback on your resume from the OpenAI GPT-3.5 model.