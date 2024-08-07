import streamlit as st
import os

# Directory containing audio files
audio_directory = "E:/TTS"

# Function to list all generated audio files
def list_audio_files(directory):
    return [f for f in os.listdir(directory) if f.endswith('.mp3')]

# List all audio files in the directory
audio_files = list_audio_files(audio_directory)

# Streamlit application
st.title("Generated Audio Samples")

# Display audio players for each file
for audio_file in audio_files:
    st.text(audio_file.replace('.mp3', ''))
    st.audio(os.path.join(audio_directory, audio_file), format="audio/mp3")

# Run the Streamlit application
if __name__ == "__main__":
    st.set_page_config(page_title="Audio Samples", layout="wide")
