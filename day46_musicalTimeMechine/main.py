import requests, spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
import pprint

# Spotify 使用者認證請求 + 取得id
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/",
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        show_dialog=True,
        cache_path="token.txt",
        username="YOUR_USERNAME",)
)
user_id = sp.current_user()["id"]

# 歌單排行榜請求: 網址+日期
print('歡迎來到建立 Spotify 播放清單')
query_date = input(' Which year do you want to travel to? Type the date in this formate YYYY-MM-DD: ')
print("正在建立清單中，請稍後...")
URL = 'https://www.billboard.com/charts/hot-100/'+ query_date
browser_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
playlist_response = requests.get(url = URL, headers=browser_header)

# 獲取百大歌名
rank_soup = BeautifulSoup(playlist_response.text, 'html.parser')
song_names = [song_tag.getText().strip() for song_tag in rank_soup.find_all(name='h3', class_="a-no-trucate",)]


# 搜尋 Spotify 上百大歌名的 uri
song_uris = []
for song in song_names:
    query = sp.search(q={f"track:{song} year:{query_date[:4]}"},type='track')
    try:
        uri = query['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} is doesn't exist in Spotify. Skipped")

#建立 Spotify 播放歌單
playlist = sp.user_playlist_create(user=user_id, name=f"{query_date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)




