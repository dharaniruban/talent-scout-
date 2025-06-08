1. Project Overview
Talent Scout AI is a Streamlit-based web application designed to streamline technical interviews. It collects candidate details and leverages the LLaMA 3.2 model (via Ollama) to generate tailored technical questions based on the candidate’s tech stack. The app offers a clean, user-friendly interface with a white background and purple buttons.

2. Features
Candidate Details Collection: Gathers name, email, phone number, years of experience, role, location, and tech stack.

Input Validation: Ensures valid email format, digits-only for phone and experience, and no numbers in text fields.

Question Generation: Dynamically creates 10 technical questions based on the candidate’s tech stack.

Question Navigation: Allows navigation between questions using "Previous" and "Next" buttons.

Summary Display: Shows a summary of candidate details and answers upon completion.

UI Design: Features a centered layout with a white background and professional purple buttons.

Error Handling: Displays error messages for invalid inputs, preventing progression until corrected.

3. Usage Instructions
3.1 Form Page
Enter your details (name, email, tech stack, etc.) in the "Candidate Details" section.
Ensure all fields are valid (e.g., proper email, digits for phone/experience).
Click "Start Interview" to proceed.

3.2 Questions Page
Answer each of the 10 generated technical questions.
Use "Previous" and "Next" buttons to navigate.
Click "Submit" on the final question to finish.

3.3 Thank You Page
Review your submitted details and answers.
Responses are saved for hiring team evaluation.

4. File Structure
app.py: Main Streamlit application script.
requirements.txt: List of Python dependencies.
README.md: Project documentation.

5. Dependencies
5.1 Python Packages
streamlit: For the web application framework.
requests: For API calls to Ollama.
json: For JSON data handling (built-in).
re: For email validation (built-in).

5.2 External Requirements
Ollama: To run the LLaMA 3.2 model locally.
LLaMA 3.2 Model: Used for question generation.





SAMPLE DEMO VIDEO:


https://github.com/user-attachments/assets/a251fb11-b357-4fa3-b20c-cc790223ca71




