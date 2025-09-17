import streamlit as st
import os
from utils.transcribe import transcribe_audio
from utils.generate_soap import generate_soap_notes

# Page config
st.set_page_config(
    page_title="HealthLens",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar for app info
with st.sidebar:
    st.title("HealthLens ⚕️")
    st.markdown(
        """
    HealthLens converts patient voice recordings into structured SOAP notes.
    Upload your audio file and get a professionally formatted report.
    """
    )
    st.markdown(
        """
    **Developer:** Himasri Alu  
    **Tech Stack:** Python, Streamlit, AssemblyAI, Google Gemini LLM"""
    )
    st.markdown("---")
    st.info("⚠️ This AI-generated report should be reviewed by a clinician before use.")

# Header
st.markdown(
    """
    <div style='background-color:#f0f4f8; padding:15px; border-radius:10px'>
        <h1 style='color:#0f4c81;'>HealthLens – AI Symptom → SOAP Generator</h1>
        <p style='color:#333;'>Upload a voice recording describing your symptoms. The AI will generate structured SOAP notes automatically.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("---")

# Audio upload
uploaded_file = st.file_uploader(
    "🎤 Upload your audio file (.mp3 or .wav)", type=["mp3", "wav"]
)

if uploaded_file:
    # Ensure audio folder exists
    os.makedirs("audio", exist_ok=True)
    file_path = os.path.join("audio", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Transcription
    with st.spinner("📝 Transcribing audio..."):
        transcript = transcribe_audio(file_path)
        # st.subheader("Transcript")
        # st.text(transcript)

    # SOAP generation
    with st.spinner("📄 Generating SOAP notes..."):
        soap_notes = generate_soap_notes(transcript)
        # st.subheader("Generated SOAP Notes")
        # st.text(soap_notes)

    # Display transcript and SOAP notes side by side
    st.subheader("Results")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🗣 Transcript")
        st.text_area("Transcript", transcript, height=300)

    with col2:
        st.markdown("### 📋 Generated SOAP Notes")
        st.text_area("SOAP Notes", soap_notes, height=300)

        # Download button
        st.download_button(
            label="💾 Download SOAP Notes",
            data=soap_notes,
            file_name="soap_notes.txt",
            mime="text/plain"
        )

    
