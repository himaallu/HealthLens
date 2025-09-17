# 🩺 HealthLens – AI Symptom → SOAP Notes Generator

HealthLens is an AI-powered clinical documentation assistant that helps transform **patient voice recordings** into structured **SOAP notes** (Subjective, Objective, Assessment, Plan).  
It combines **speech-to-text transcription** with **LLM-powered summarization** to assist healthcare professionals in quickly generating accurate medical notes.

---

## ✨ Features
- 🎙️ **Voice Upload**: Upload audio recordings (MP3/WAV) of patient-doctor conversations.
- 🔊 **AI Transcription**: Converts speech to text using **AssemblyAI**.
- 🧠 **SOAP Notes Generation**: Creates structured SOAP notes using **Google Gemini AI**.
- 💾 **Download Notes**: Export generated notes as `.txt` files.
- 📊 **Streamlit UI**: Simple, interactive web interface with sidebar information.

---

## 🖼️ UI Preview
- Upload audio file from the main page.
- View **Transcript** of the audio.
- View and download **AI-generated SOAP Notes**.
- Sidebar shows **Developer Info** + **Tech Stack**.

---

## 🛠️ Tech Stack
- **[Python](https://www.python.org/)**  
- **[Streamlit](https://streamlit.io/)** – UI Framework  
- **[AssemblyAI](https://www.assemblyai.com/)** – Speech-to-Text API  
- **[Google Gemini AI](https://ai.google/)** – LLM for SOAP note generation  

---
## ⚡ Installation & Setup

1. **Clone this repository**
   ```bash
   git clone https://github.com/<your-username>/HealthLens.git
   cd HealthLens
Create and activate virtual environment

bash
Copy code
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
Install dependencies

bash
Copy code
pip install -r requirements.txt
Add your API keys
Create a file called config.py in the root folder:

python
Copy code
ASSEMBLYAI_API_KEY = "your_assemblyai_key"
GEMINI_API_KEY = "your_gemini_api_key"
Run the app

bash
Copy code
streamlit run app.py

