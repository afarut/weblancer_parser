import os
from dotenv import load_dotenv
from pathlib import Path


load_dotenv()
BASE_DIR = Path(__file__).resolve().parent
API_KEY = os.environ["API_KEY"]
CHANNEL_ID = os.environ["CHANNEL_ID"]