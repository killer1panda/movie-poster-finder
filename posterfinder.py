import os
import requests

API_KEY = "YOUR_TMDB_API_KEY"  # Replace with your key
MOVIE_TITLES = [
    "Inception", "The Dark Knight", "Titanic", "Avatar", "Interstellar"
]
SAVE_DIR = "movie_posters"

os.makedirs(SAVE_DIR, exist_ok=True)

def download_poster(title):
    search_url = f"https://api.themoviedb.org/3/search/movie"
    params = {"api_key": API_KEY, "query": title}
    response = requests.get(search_url, params=params)
    results = response.json().get("results")
    
    if results:
        poster_path = results[0].get("poster_path")
        if poster_path:
            full_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
            image_data = requests.get(full_url).content
            with open(f"{SAVE_DIR}/{title}.jpg", "wb") as f:
                f.write(image_data)
            print(f"✅ Downloaded poster for: {title}")
        else:
            print(f"⚠️ No poster found for: {title}")
    else:
        print(f"❌ No results for: {title}")

for title in MOVIE_TITLES:
    download_poster(title)
