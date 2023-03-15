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
            selection = MusicLibraryInterface.__display_options_get_selection()
            if selection == Helper.DISPLAY_ALL_SONGS:
                MusicLibraryInterface.__display_all_songs()

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
        print(f"{Helper.QUIT}. Quit")
        print("")

    @staticmethod
    def __display_options_get_selection():
        
        selection = input("\nSelection: ")
        selection_helper = MusicLibraryInterface.__is_valid_selection(selection)
        if selection_helper[0]:
            return selection_helper[1]
        print("---ERROR: Selection not recognized---")
        return MusicLibraryInterface.__display_options_get_selection()
    
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
        Helper.display_songs(song_list)