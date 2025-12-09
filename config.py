import os
from dotenv import load_dotenv

load_dotenv()

# Load API key from .env file
API_KEY = os.getenv('TMDB_API_KEY')

BASE_URL = 'https://api.themoviedb.org/3'

MOVIE_IDS = [299534, 19995, 140607, 299536, 597, 135397, 
             420818, 24428, 168259, 99861, 284054, 12445, 
             181808, 330457, 351286, 109445, 321612, 260513]