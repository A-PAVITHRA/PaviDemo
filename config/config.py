import os
from pathlib import Path
from dotenv import load_dotenv

config_path = Path(__file__).parent
credentials_path = os.path.join(config_path, "credential.env")

if os.path.exists(credentials_path):  # run locally
    CREDENTIALS_FILE = credentials_path

if CREDENTIALS_FILE:
    load_dotenv(CREDENTIALS_FILE)

