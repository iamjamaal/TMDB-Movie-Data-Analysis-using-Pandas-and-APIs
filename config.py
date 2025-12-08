import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('7884a11d22079309e268ac5ae881da5e')
BASE_URL = 'https://api.themoviedb.org/'
MOVIE_IDS = [0, 299534, 19995, 140607, 299536, 597, 135397, 
             420818, 24428, 168259, 99861, 284054, 12445, 
             181808, 330457, 351286, 109445, 321612, 260513]