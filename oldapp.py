# # import streamlit as st

# # st.title("HealthLens – AI Symptom → Report Generator")
# # st.write("If you see this, Streamlit is working!")
# import sys
# print(sys.path)

import streamlit as st
import os
from utils.transcribe import transcribe_audio
from utils.generate_soap import generate_soap_notes

# # Create audio folder if not exists
# if not os.path.exists("audio"):
#     os.makedirs("audio")

st.title("HealthLens  AI Symptom → Report Generator")
st.markdown("Upload a voice recording describing your symptoms. The AI will generate structured SOAP notes.")

uploaded_file = st.file_uploader("Upload your audio", type=["mp3", "wav"])

if uploaded_file:
    file_path = os.path.join("audio", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Transcribe audio
    with st.spinner("Transcribing audio..."):
        transcript = transcribe_audio(file_path)
        st.subheader("Transcript")
        st.text(transcript)

    # Generate SOAP notes
    with st.spinner("Generating SOAP notes..."):
        soap_notes = generate_soap_notes(transcript)
        st.subheader("Generated SOAP Notes")
        st.text(soap_notes)

    # Download button
    st.download_button(
        label="Download SOAP Notes",
        data=soap_notes,
        file_name="soap_notes.txt"
    )
