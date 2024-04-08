
import streamlit as st
from pydub import AudioSegment
from pydub.playback import play

# Function to play audio
def play_audio(file_path):
    audio = AudioSegment.from_file(file_path, format="mp3")
    play(audio)

def main():
    st.title("Hare Krishna Mantra Player")
    st.write("Welcome to the Hare Krishna Mantra Player!")
    
    # Display the Hare Krishna mantra
    st.header("Hare Krishna Mantra")
    st.write("Hare Krishna, Hare Krishna, Krishna Krishna, Hare Hare")
    st.write("Hare Rama, Hare Rama, Rama Rama, Hare Hare")
    
    # Button to play audio
    if st.button("Play Audio"):
        play_audio("hare-krishna.mp3")

if __name__ == "__main__":
    main()

