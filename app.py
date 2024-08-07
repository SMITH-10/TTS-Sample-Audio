import streamlit as st
import os

# Directory containing audio files (relative path)
audio_directory = "."

# Function to list all generated audio files
def list_audio_files(directory):
    if not os.path.exists(directory):
        st.error(f"The directory {directory} does not exist.")
        return []
    
    # files = os.listdir(directory)
    # st.write(f"Files in directory {directory}: {files}")
    # return [f for f in files if f.endswith('.mp3')]

# List all audio files in the directory
audio_files = list_audio_files(audio_directory)

# Streamlit application
st.title("Generated Audio Samples")

# Display current working directory
st.write(f"Current working directory: {os.getcwd()}")

# Display audio players for each file
for audio_file in audio_files:
    st.text(audio_file.replace('.mp3', ''))
    st.audio(os.path.join(audio_directory, audio_file), format="audio/mp3")

# Run the Streamlit application
if __name__ == "__main__":
    st.set_page_config(page_title="Audio Samples", layout="wide")
