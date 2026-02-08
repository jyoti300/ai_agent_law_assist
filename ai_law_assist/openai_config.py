# openai_config.py
import os
from dotenv import load_dotenv

load_dotenv()  # loads .env file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
