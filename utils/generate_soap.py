# utils/generate_soap.py
import google.generativeai as genai
import streamlit as st
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)

def generate_soap_notes(transcript_text):
    """
    Generates SOAP notes from a plain transcript string.
    """
    prompt = f"""
You are a clinical documentation assistant.
- Provide output in plain text only.
- Do NOT use Markdown formatting (no **, *, _, #, etc.).
- Use clear headings like: Subjective:, Objective:, Assessment:, Plan:
Generate SOAP notes (Subjective, Objective, Assessment, Plan) from this transcript:

{transcript_text}
"""

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        soap_notes = response.text

        if not soap_notes:
            raise ValueError("Gemini returned empty content")

        return soap_notes

    except Exception as e:
        return f"Error generating SOAP notes: {e}"
