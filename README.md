# Audio Transcription

# Overview
This project is an offline audio transcription application built using Streamlit and Open-Source Whisper. The app allows users to upload audio files and generate text transcripts entirely on their computer, without needing an OpenAI API key or internet connection.

# Features
- Upload audio files in wav, mp3, m4a, or mp4 formats
- Offline transcription using Open-Source Whisper
- Display the transcription directly in the Streamlit web app
- Download the transcript as a .txt file
- Works on CPU or GPU automatically for faster performance

# Technologies
- Python 3.11+
- Streamlit for the interactive web interface
- Whisper (Open-Source) for offline audio transcription
- PyTorch as the backend for Whisper model

# Setup & Running the App
1. Clone the repository and navigate to the project folder:
 ```bash
     git clone <your-repo-link>
     cd <repo-folder>
   ```

3. Install the required Python packages:
 ```bash
    pip install -r requirements.txt
   ```
4. Run the Streamlit app:
 ```bash
    streamlit run app.py
   ```
5. Upload your audio file, click "Transcribe Audio", view the transcript, and download it as needed

