# utils/transcribe.py
import assemblyai as aai
from config import ASSEMBLYAI_API_KEY  # Store your API key here

# Set AssemblyAI API key globally
aai.settings.api_key = "7bca7b06a25b4bb1931559bf074833c3"

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
