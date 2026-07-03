from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Read the API key
API_KEY = os.getenv("NEWS_API_KEY")

# Validate that it exists
if not API_KEY:
    raise ValueError(
        "NEWS_API_KEY not found. Please create a .env file."
    )