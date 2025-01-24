import streamlit as st
import spacy

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Streamlit UI
st.title("NEET PG Study Planner AI")

# User input
user_input = st.text_input("Enter your command (e.g. 'Move cardiology to Monday 8 AM')")

if st.button("Update Schedule"):
    doc = nlp(user_input)

    subjects = ["cardiology", "anatomy", "biochemistry", "pathology"]
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    found_subject = None
    found_day = None

    for token in doc:
        if token.text.lower() in subjects:
            found_subject = token.text.capitalize()
        if token.text.lower() in days:
            found_day = token.text.capitalize()

    if found_subject and found_day:
        st.success(f"Scheduled {found_subject} on {found_day}.")
    else:
        st.warning("Could not understand the command. Please try again.")
