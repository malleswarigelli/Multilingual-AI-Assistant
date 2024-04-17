

import streamlit as st
from src.helper import voice_input, llm_model_object, text_to_speech


def main():
    st.title("Multilingual AI Assistant")
    
    # Button to start recording
    if st.button("Ask me anything"):
        with st.spinner("Listening ...."):
            # what is listening
            text= voice_input()
            # get response by passing llm model object
            response= llm_model_object(text)
            # pass response to text to speech
            text_to_speech(response)
            
            # Display audio player and download link
            audio_file = open("speech.mp3", 'rb')
            audio_bytes = audio_file.read()
            
            st.text_area(label="Response:", value=response, height=350)
            st.audio(audio_bytes, format='audio/mp3')
            st.download_button(label="Download Speech",
                                data=audio_bytes,
                                file_name="speech.mp3",
                                mime="audio/mp3")

# call the main method
if __name__ == "__main__":
    main()
    
