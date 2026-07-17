from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'
    GROQ_API_KEY = os.environ.get('GROQ_API_KEY') or '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'
    DEBUG = os.environ.get('DEBUG', 'False') == 'True'
    TIMEOUT = 10  # Timeout for requests in seconds
    CACHE_TIMEOUT = 3600  # Cache timeout for scraped content in seconds