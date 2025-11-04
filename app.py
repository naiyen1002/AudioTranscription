import os
import datetime
import streamlit as st
import whisper 
import torch

# App title
st.title("Audio Transcription")

# Load Whisper model once at startup
st.write("Loading Whisper model...")
device = "cuda" if torch.cuda.is_available() else "cpu"  # Use GPU if available
model = whisper.load_model("small", device=device)       # Small model for faster transcription
st.success(f"Model loaded on {device}")

current_audio_file = None

# Upload audio file section
uploaded_file = st.file_uploader(
    "Upload audio file (wav, mp3, m4a, mp4):",
    type=["wav", "mp3", "m4a", "mp4"]
)
if uploaded_file:
    # Generate timestamped filename to avoid conflicts
    ext = uploaded_file.name.split(".")[-1]
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    current_audio_file = f"audio_{timestamp}.{ext}"
    
    # Save uploaded audio to local file
    with open(current_audio_file, "wb") as f:
        f.write(uploaded_file.read())
    
    # Display audio player in the app
    st.audio(current_audio_file)
    st.success(f"Audio uploaded as {current_audio_file}")

# Transcribe button
if current_audio_file:
    if st.button("Transcribe Audio"):
        with st.spinner("Transcribing audio..."):
            try:
                # Offline transcription using Whisper
                result = model.transcribe(current_audio_file)
                transcript_text = result["text"]

                # Display the transcript in the app
                st.header("Transcript")
                st.write(transcript_text)

                # Save transcript to local text file
                transcript_file = "transcript.txt"
                with open(transcript_file, "w", encoding="utf-8") as f:
                    f.write(transcript_text)

                # Provide download button for transcript
                st.download_button(
                    "Download Transcript",
                    transcript_text,
                    file_name=transcript_file
                )

            except Exception as e:
                st.error(f"Transcription failed: {e}")
