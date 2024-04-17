# Multilingual-AI-Assistant


##  Crete GOOGLE_API_KEY from Genimi api link [https://ai.google.dev/]
- https://deepmind.google/technologies/gemini/#introduction


## python SDK for Gemini API is avai in google-generativeai package
- pip insatll -q -U google-generativeai
## To use gemini API, set up your API key
- Add GOOGLE_API_KEY to .env 

## Git commands
- git add .

- git commit -m "Updated"r
- git push origin main

# How to run?
- conda create -n multilin python=3.9 -y # genai require python version >=3.9
- conda activate multilin

# Install requirements
- pip install -r requirements.txt
- pip list # show all installed libraries including local package (multilingual-assistant)

# Create a .env file in the root directory and add your GOOGLE_API_KEY credentials as follows:
- GOOGLE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Finally run the following command
- streamlit run app.py

# Now,

- open up localhost:port#

# Techstack Used:
- Python
- Google API
- Streamlit
- PaLM2
- s2t
- t2s