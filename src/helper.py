import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS



print("This is Malli")

# access gemini model, requires google key; access it from .env

load_dotenv()
GOOGLE_API_KEY= os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"]= GOOGLE_API_KEY  # get key from .env


def voice_input():
    pass

def text_to_speech():
    pass

def llm_model_object():
    pass

