Talent Scout AI
Talent Scout AI is a web application built with Streamlit that facilitates technical interviews by collecting candidate details and generating tailored technical questions based on their tech stack. It provides a user-friendly interface for candidates to input their information, answer questions, and review their responses.
Table of Contents

Overview
Features
Usage
File Structure
Dependencies
Contributing
License

Overview
Talent Scout AI is designed to streamline the technical interview process. Candidates provide their personal details and tech stack, after which the application uses the LLaMA 3.2 model (via Ollama) to generate 10 technical questions. Candidates can answer these questions, navigate between them, and review their responses at the end. The application includes form validation, a clean UI with a white background, and purple buttons styled for a professional look.
Features

Candidate Information Collection: Collects details such as name, email, phone number, years of experience, role, location, and tech stack.
Form Validation: Validates inputs (e.g., email format, digits-only for phone and years of experience, no numbers in text fields).
Dynamic Question Generation: Uses LLaMA 3.2 (via Ollama) to generate 10 technical questions based on the candidate's tech stack.
Interactive Question Navigation: Allows candidates to move between questions using "Previous" and "Next" buttons.
Response Summary: Displays a summary of the candidate's details and answers at the end.
Responsive Design: Centered layout with a clean, professional UI, white background, and purple buttons.
Error Handling: Displays error messages for invalid inputs without proceeding until corrected.

Usage

Form Page:

Open the app in your browser.
Fill in your details under the "Candidate Details" section.
Ensure all fields are valid (e.g., valid email, digits for phone and experience, no numbers in name/role/location/tech stack).
Click "Start Interview" to proceed.


Questions Page:

Answer each of the 10 generated technical questions.
Use "Previous" and "Next" buttons to navigate between questions.
Click "Submit" on the last question to finish.


Thank You Page:

Review your submitted details and answers.
The hiring team can access these responses for evaluation.



File Structure
talent-scout-ai/
├── talent scout.py               
└── README.md            

Dependencies
The project relies on the following Python packages (listed in requirements.txt):

streamlit - For building the web application.
requests - For making API calls to Ollama.
json - For handling JSON data (built-in).
re - For email validation (built-in).

Additionally, you need:

Ollama: To run the LLaMA 3.2 model locally for question generation.
LLaMA 3.2 Model: Available via Ollama.

Create a requirements.txt file with:
streamlit
requests

Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make your changes and commit (git commit -m "Add your feature").
Push to your branch (git push origin feature/your-feature).
Open a Pull Request with a detailed description of your changes.

Please ensure your code follows PEP 8 style guidelines and includes appropriate comments.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Note: This project assumes you have access to the LLaMA 3.2 model via Ollama. Ensure the Ollama server is running on http://localhost:11434 as specified in the code.




SAMPLE DEMO VIDEO:


https://github.com/user-attachments/assets/a251fb11-b357-4fa3-b20c-cc790223ca71




