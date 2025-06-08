import streamlit as st
import requests
import json
import re # Import regex module for email validation

# Inject white background and styling
def inject_custom_css():
    st.markdown("""
        <style>
        /* Set background and text */
        .stApp {
            background-color: white !important;
            color: black !important;
        }

        /* Layout & content box */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 800px;
        }

        .custom-title {
            font-size: 2.2rem;
            font-weight: bold;
            text-align: center;
            margin-bottom: 2rem;
            color: black;
        }

        /* Specific purple buttons with white text and shadow */
        button {
            background-color: #6108c4 !important; /* Exactly the requested purple color */
            border: none;
            border-radius: 12px !important;
            padding: 0.6rem 1.2rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            transition: 0.2s ease-in-out;
        }

        /* Ensure text inside buttons is white by targeting the button and all its descendants */
        button, button * {
            color: white !important; /* White text for better contrast within the button */
        }

        button:hover {
            background-color: #5006a8 !important; /* Slightly darker purple on hover */
            transform: scale(1.02);
        }

        /* Box container for other sections (e.g., Instructions, Questions, Summary) */
        .box {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 1rem;
            background-color: #ffffff;
            margin-bottom: 1.5rem;
            color: black !important;
        }

        /* White input boxes and textarea */
        input, textarea {
            background-color: white !important;
            color: black !important;
            border-radius: 8px !important;
            border: 1px solid #ccc !important;
        }

        /* Ensure all text inputs and markdown content are black */
        input, .stMarkdown, .stText, span, div {
            color: black !important;
        }
        </style>
    """, unsafe_allow_html=True)

def get_ollama_response(prompt: str) -> str:
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": True
    }
    try:
        response = requests.post(url, json=data, headers=headers, stream=True)
        response.raise_for_status()
        full_response = ""
        for line in response.iter_lines():
            if line:
                chunk = json.loads(line.decode("utf-8"))
                full_response += chunk.get("response", "")
        return full_response.strip()
    except Exception as e:
        return f"Error: {e}"

def init_session_state():
    keys_defaults = {
        "page": "form",
        "name": "", "email": "", "phone": "",
        "role": "", "location": "", "tech_stack": "", "years_experience": "",
        "questions": [], "answers": [],
        "current_q": 0
    }
    for key, default in keys_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default

def form_page():
    st.markdown('<div class="custom-title">Talent Scout AI - Candidate Information</div>', unsafe_allow_html=True)

    with st.expander("Instructions", expanded=True):
        st.markdown("""
        <div class="box">
            Welcome to the Talent Scout AI assessment.<br><br>
            1. Fill in your personal and technical details.<br>
            2. Based on your tech stack, you'll receive 10 custom questions.<br>
            3. You can move back and forth between questions.<br>
            4. At the end, your responses will be saved and shown.
        </div>
        """, unsafe_allow_html=True)

    with st.form("info_form"):
        st.markdown("### Candidate Details")
        st.session_state.name = st.text_input("Full Name", value=st.session_state.name)
        st.session_state.email = st.text_input("Email", value=st.session_state.email)
        st.session_state.phone = st.text_input("Phone Number", value=st.session_state.phone)
        st.session_state.years_experience = st.text_input("Years of Experience", value=st.session_state.years_experience)
        st.session_state.role = st.text_input("Role you're applying for", value=st.session_state.role)
        st.session_state.location = st.text_input("Your Location", value=st.session_state.location)
        st.session_state.tech_stack = st.text_area("Technologies you're familiar with", height=100, value=st.session_state.tech_stack)

        # Create a placeholder for error messages
        error_message_placeholder = st.empty()

        submitted = st.form_submit_button("🚀 Start Interview")

        if submitted:
            # Clear previous error messages before re-validating
            error_message_placeholder.empty()

            # --- Validation Logic ---
            validation_passed = True
            errors = [] # List to accumulate errors

            # Email validation
            email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_regex, st.session_state.email):
                errors.append("Please enter a valid email address.")
                validation_passed = False

            # Phone number validation (digits only and not empty)
            if not st.session_state.phone.isdigit() or not st.session_state.phone.strip():
                errors.append("Phone Number must contain only digits and cannot be empty.")
                validation_passed = False

            # Years of Experience validation (digits only and not empty)
            if not st.session_state.years_experience.isdigit() or not st.session_state.years_experience.strip():
                errors.append("Years of Experience must contain only digits and cannot be empty.")
                validation_passed = False

            # Name, Role, Location, Tech Stack validation (no numbers and not empty)
            text_fields = {
                "Full Name": st.session_state.name,
                "Role": st.session_state.role,
                "Your Location": st.session_state.location,
                "Technologies you're familiar with": st.session_state.tech_stack
            }
            for label, value in text_fields.items():
                if not value.strip(): # Check if field is empty
                    errors.append(f"{label} cannot be empty.")
                    validation_passed = False
                if any(char.isdigit() for char in value):
                    errors.append(f"{label} should not contain numbers.")
                    validation_passed = False

            # Display all accumulated errors
            if errors:
                for error in errors:
                    error_message_placeholder.error(error) # Display errors in the placeholder

            # --- Proceed only if validation passes ---
            if validation_passed:
                prompt = (
                    f"As an interviewer, generate exactly 10 distinct technical questions "
                    f"for a candidate familiar with the following tech stack:\n{st.session_state.tech_stack}\n"
                    f"Present ONLY the questions, numbered 1 to 10, with no introductory text."
                )
                with st.spinner("...generating questions"):
                    questions_text = get_ollama_response(prompt)
                questions = [q.strip("1234567890. ").strip() for q in questions_text.strip().split('\n') if q.strip()]
                st.session_state.questions = questions[:10]
                st.session_state.answers = [""] * 10
                st.session_state.page = "questions"
                st.rerun()

def questions_page():
    st.markdown('<div class="custom-title">Interview Questions</div>', unsafe_allow_html=True)

    q_idx = st.session_state.current_q
    total_q = len(st.session_state.questions)
    question = st.session_state.questions[q_idx]

    st.markdown(f"#### Question {q_idx + 1} of {total_q}")
    st.markdown(f'<div class="box">{question}</div>', unsafe_allow_html=True)

    with st.form(key=f"form_q{q_idx}"):
        answer = st.text_area("Your Answer:", value=st.session_state.answers[q_idx], height=150)

        col1, col2, col3 = st.columns([1, 5, 1])
        with col1:
            prev_clicked = st.form_submit_button("Previous")
        with col3:
            next_label = "Next" if q_idx < total_q - 1 else "Submit"
            next_clicked = st.form_submit_button(next_label)

    st.session_state.answers[q_idx] = answer

    if prev_clicked and q_idx > 0:
        st.session_state.current_q -= 1
        st.rerun()
    elif next_clicked:
        if q_idx < total_q - 1:
            st.session_state.current_q += 1
            st.rerun()
        else:
            st.session_state.page = "thank_you"
            st.rerun()

def thank_you_page():
    st.markdown('<div class="custom-title">Thank You</div>', unsafe_allow_html=True)
    st.markdown('<div class="box">Your responses have been recorded successfully.</div>', unsafe_allow_html=True)

    st.markdown("### Candidate Summary")
    for label, key in [
        ("Name", "name"), ("Email", "email"),
        ("Phone", "phone"), ("Years of Experience", "years_experience"),
        ("Role", "role"),
        ("Location", "location"), ("Tech Stack", "tech_stack")
    ]:
        st.markdown(f'<div class="box"><strong>{label}:</strong><br>{st.session_state[key]}</div>', unsafe_allow_html=True)

    st.markdown("### Your Answers")
    for i, (q, a) in enumerate(zip(st.session_state.questions, st.session_state.answers)):
        st.markdown(f"""
            <div class="box">
                <strong>Q{i+1}: {q}</strong><br>
                <span>A: {a if a else "Not answered"}</span>
            </div>
        """, unsafe_allow_html=True)

# --- Run App ---
st.set_page_config(page_title="Talent Scout AI", layout="centered", initial_sidebar_state="collapsed")
inject_custom_css()
init_session_state()

if st.session_state.page == "form":
    form_page()
elif st.session_state.page == "questions":
    questions_page()
elif st.session_state.page == "thank_you":
    thank_you_page()
