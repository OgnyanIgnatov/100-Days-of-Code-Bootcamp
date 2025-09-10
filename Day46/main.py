import requests,spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv(key="CLIENT_ID")
CLIENT_SECRET = os.getenv(key="CLIENT_SECRET")
REDIRECT_URI = "https://example.com/callback"


date = input("What year would you like to travel to? Type the date in the following format: YYYY-MM-DD: ")
header = header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"}

request = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}", headers=header)
request_html = request.text

soup = BeautifulSoup(request_html,"html.parser")
song_names_raw = soup.select("li ul li h3")
song_names = [song.get_text().strip() for song in song_names_raw]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope = "playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=os.getenv(key="USERNAME")
        )
    )
#user_id = sp.current_user()["id"]

print(sp)
playlist_name = f"Top 100 of {date}"

playlist = sp.user_playlist_create(
    user=os.getenv(key="USERNAME"),
    name=playlist_name,
    public=False,
)

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

sp.playlist_add_items(
    playlist_id=playlist['id'],
    items=song_uris,
)
