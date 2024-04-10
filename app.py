

import streamlit as st
from src.helper import voice_input, llm_model_object, text_to_speech


def main():
    st.title("Multilingual AI Assistant")
    
    # creating a button
    if st.button("Ask me anything"):
        with st.spinner("Listening ...."):
            # what is listening
            text= voice_input()
            # get response by passing llm model object
            response= llm_model_object()
            # pass response to text to speech
            text_to_speech(response)
            
            # open file, read
            audio_file= open("speech.mp3","rb")
            audio_bytes= audio_file.read()
            
            st.text_area()
            st.audio()
            st.download_button()

# call the main method
if __name__=="__main":
    