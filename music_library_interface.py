import requests
import json
from song import Song
from helper import Helper





class MusicLibraryInterface():

    def run(self):
        MusicLibraryInterface.__display_welcome()
        selection = -100
        while selection != Helper.QUIT:
            MusicLibraryInterface.__display_options()
            selection = MusicLibraryInterface.__get_selection()
            if selection == Helper.DISPLAY_ALL_SONGS:
                MusicLibraryInterface.__display_all_songs()
            if selection == Helper.INFO_BY_ID:
                selection = MusicLibraryInterface.__get_song_selection()
                MusicLibraryInterface.__display_all_info(selection)

    @staticmethod
    def __display_welcome():
        Helper.clearscreen()
        print("Welcome to the Music Library API Interface\n\nWhat would you like to do?")

    @staticmethod
    def __display_options():
        print("\n")
        print("OPTIONS: ")
        print("--------")
        print(f"{Helper.DISPLAY_ALL_SONGS}. Display ALL songs in the library")
        print(f"{Helper.INFO_BY_ID}. Get Full info of a certain by song")
        print(f"{Helper.QUIT}. Quit")
        print("")

    @staticmethod
    def __get_selection():
        
        selection = input("\nSelection: ")
        selection_helper = MusicLibraryInterface.__is_valid_selection(selection)
        if selection_helper[0]:
            return selection_helper[1]
        print("---ERROR: Selection not recognized---")
        return MusicLibraryInterface.__get_selection()
    
    @staticmethod 
    def __is_valid_selection(selection:str) -> bool:
        selection_as_int = None
        try:
            selection_as_int = int(selection)
        except:
            return False, None
        
        if selection_as_int == Helper.DISPLAY_ALL_SONGS:
            return True, selection_as_int
        elif selection_as_int == Helper.QUIT:
            return True, selection_as_int
        elif selection_as_int == Helper.INFO_BY_ID:
            return True, selection_as_int
        return False, None

    @staticmethod
    def __display_all_songs():
        response = requests.get("http://127.0.0.1:5000/api/songs")

        songs_json = response.json()

        song_list = []
        for song in songs_json:
            song_list.append(Song.song_decoder(song))

        Helper.clearscreen()
        print(f"There are {len(song_list)} songs in the library: \n\n")
        for song in song_list:
            print(song.partial_string())

    @staticmethod
    def __get_song_selection():
        selection = input("Enter song ID: ")
        try:
            id = int(selection)
            return id
        except:
            print("--ERROR: Invalid ID--\n")
            return MusicLibraryInterface.__get_song_selection()

    staticmethod
    def __display_all_info(id:int):
        Helper.clearscreen()
        response = requests.get(f"http://127.0.0.1:5000/api/songs/{id}")

        try:
            song = Song.song_decoder(response.json())
            print(f"       Title: {song.title}")
            print(f"      Artist: {song.artist}")
            print(f"       Album: {song.album}")
            custom_date_string = ''
            if song.release_date.day < 10:
                custom_date_string = song.release_date.strftime("%B") + " " + song.release_date.strftime("%d, %Y").removeprefix("0")
            else:
                custom_date_string = song.release_date.strftime("%B %d, %Y")
            print(f"Release Date: {custom_date_string}")
            print(f"       Genre: {song.genre}")
            print(f"       Likes: {song.likes}")
            print("\n")
        except:
            print("No song found by that ID Number\n")

