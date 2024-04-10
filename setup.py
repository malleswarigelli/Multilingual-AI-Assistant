
from setuptools import find_packages, setup

setup(
    name="multilingual assistant",
    version="0.0.1",
    author="Malleswari Gelli",
    author_email="malleswari.gelli@gmail.com",
    packages=find_packages(),
    install_requires=["SpeechRecognition","pipwin","pyaudio","gTTS","google-generativeai","python-dotenv","streamlit"]
)