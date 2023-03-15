import requests
import json
from song import Song
from helper import Helper


response = requests.get("http://127.0.0.1:5000/api/songs")

test1 = response.content
songs_json = response.json()

song_list = []
for song in songs_json:
    song_list.append(Song.song_decoder(song))


Helper.display_songs(song_list)


pass