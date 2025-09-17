# utils/transcribe.py
import assemblyai as aai
import streamlit as st
ASSEMBLYAI_API_KEY = st.secrets["ASSEMBLYAI_API_KEY"]
aai.settings.api_key = ASSEMBLYAI_API_KEY

def transcribe_audio(audio_file):
    """
    Transcribes an audio file (local path or URL) using AssemblyAI
    Returns the transcript text
    """
    # Configure transcription
    config = aai.TranscriptionConfig(speech_model=aai.SpeechModel.universal)
    
    # Create transcriber and transcribe
    transcript = aai.Transcriber(config=config).transcribe(audio_file)
    
    # Check for errors
    if transcript.status == "error":
        raise RuntimeError(f"Transcription failed: {transcript.error}")
    
    return transcript.text
