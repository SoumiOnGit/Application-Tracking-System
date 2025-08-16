from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import PyPDF2
import google.generativeai as genai
import google.api_core.exceptions
import time

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEYS"))

# Function to handle Gemini API calls with retry on quota errors
def get_gemini_response(input_prompt, pdf_text, job_text):
    model = genai.GenerativeModel('gemini-2.5-flash')  # text-only model
    while True:
        try:
            response = model.generate_content([input_prompt, pdf_text, job_text])
            return response.text
        except google.api_core.exceptions.ResourceExhausted:
            st.warning("Quota exceeded. Retrying in 60 seconds...")
            time.sleep(60)
        except Exception as e:
            return f"Error: {str(e)}"

# Function to extract text from PDF
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        pdf_text = ""
        for page in pdf_reader.pages:
            text = page.extract_text()
            if text:
                pdf_text += text + "\n"
        return pdf_text.strip()
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit UI
st.set_page_config(page_title="ATS Resume Analyzer")
st.header("ATS Resume Analyzer")

input_text = st.text_area("Job Description", key="input")
uploaded_file = st.file_uploader("Upload your Resume (PDF)..", type=["pdf"])

if uploaded_file:
    st.success("PDF Uploaded Successfully!")

submit1 = st.button("Tell Me About the Resume")
submit2 = st.button("Percentage match")

input_prompt1 = """
You are an experienced Technical Human Resource Manager. 
Your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
Your task is to evaluate the resume against the provided job description. 
Give me the percentage match, then keywords missing, and finally your overall thoughts.
"""

if submit1:
    if uploaded_file:
        pdf_text = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_text, input_text)
        st.subheader("Response")
        st.write(response)
    else:
        st.error("Please upload a PDF file.")

elif submit2:
    if uploaded_file:
        pdf_text = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_text, input_text)
        st.subheader("Response")
        st.write(response)
    else:
        st.error("Please upload a PDF file.")

