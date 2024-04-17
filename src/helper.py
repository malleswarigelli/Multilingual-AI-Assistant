import speech_recognition as sr
import google.generativeai as palm
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS # google text to speech


# to access gemini model, requires google key; access it from .env

load_dotenv()
GOOGLE_API_KEY= os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"]= GOOGLE_API_KEY  # get key from .env


def voice_input() -> str:
    """
    Recognizes your voice, returns text
    """
    # from speech_recognition
    voice_rec= sr.Recognizer()
    # from speech_recognition open microphone
    with sr.Microphone() as source:
        print("listening....")
        # capture audio by listening voice_rec from source
        audio = voice_rec.listen(source)
    try:
        # change audio as text
        text= voice_rec.recognize_google(audio)
        print("You said:", text)
        return text
        
    except sr.UnknownValueError:
        print("Sorry, couldn't understand the audio")
    
    except sr.RequestError as e:
        print("Could not request result from google speech recognition service: {0}".format(e))
        

def text_to_speech(text):
    """
    Methods converts text to speech
    """
    # google text to speech method takes text as input and convert to speech
    text_to_speech= gTTS(text=text, lang="en") # language can be changed
    
    # save audio as MP3 file
    text_to_speech.save("speech.mp3")

def llm_model_object(user_text):
    """
    input: user provided text
    loads llm model from gemini api
    generates -> GenerateContentResponse
    """
    # Genai configuration
    genai.configure(api_key=GOOGLE_API_KEY)
    
    # initialize generative model
    model= genai.GenerativeModel('gemini-pro')
    
    # generate text
    response= model.generate_content(user_text)
    result= response.text
    
    return result
