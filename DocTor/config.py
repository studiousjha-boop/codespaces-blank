import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

HF_API_KEY = os.getenv("HF_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found in .env")

if not HF_API_KEY:
    raise ValueError("HF_API_KEY not found")


