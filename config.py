import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path="env/.env")

# Fetch Twitter API credentials
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

