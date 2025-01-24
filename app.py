import streamlit as st
import spacy
import subprocess

# Ensure the spaCy model is installed
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    st.info("Downloading spaCy model. Please wait...")
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

# Streamlit UI
st.title("NEET PG Study Planner AI")
st.write("Enter a command below:")

user_input = st.text_input("Your command:")
if st.button("Process"):
    doc = nlp(user_input)
    st.write("Processed text:", [token.text for token in doc])
