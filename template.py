import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')




list_of_files=[

    "src/__init__.py",
    "src/helper.py",
    ".env",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"   
    
]

for file in list_of_files:
    filepath = Path(file) # creates your system compatible filepath (windows/mac/ubantu etc)
    filedir, filename = os.path.split(filepath)
    # if filedir not empty, create directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # overwrite
        logging.info(f"creating a directory {filedir} for the files: {filename}")
    # if path doesn't exist or pathsize=0, create empty file
    if (not os.path.exists(filepath)) or (os.path.getsize==0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"creating empty file:{filepath}")
    else:
        logging.info(f"{filename} is already exist")