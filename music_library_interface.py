import requests
import json
from song import Song
from helper import Helper
from datetime import datetime




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
            if selection == Helper.DELETE_BY_ID:
                selection = MusicLibraryInterface.__get_song_selection()
                MusicLibraryInterface.__delete_song_by_id(selection)
            if selection == Helper.LIKE_BY_ID:
                selection = MusicLibraryInterface.__get_song_selection()
                MusicLibraryInterface.__like_song(selection)
            if selection == Helper.ADD_NEW_SONG:
                MusicLibraryInterface.__add_new_song()


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
        print(f"{Helper.LIKE_BY_ID}. Like a song")
        print(f"{Helper.ADD_NEW_SONG}. Add a new song")
        print(f"{Helper.DELETE_BY_ID}. Delete a song")
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
        elif selection_as_int == Helper.DELETE_BY_ID:
            return True, selection_as_int
        elif selection_as_int == Helper.LIKE_BY_ID:
            return True, selection_as_int
        elif selection_as_int == Helper.ADD_NEW_SONG:
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
        selection = input("Enter song ID Number: ")
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

    @staticmethod
    def __delete_song_by_id(id: int) -> None:
        Helper.clearscreen()
        response = requests.get(f"http://127.0.0.1:5000/api/songs/{id}")

        try:
            song = Song.song_decoder(response.json())
            print(f"Deleting \"{song.title}\" by {song.artist}")

            delete_response = requests.delete(f"http://127.0.0.1:5000/api/songs/{id}")

            if delete_response.status_code == 204:
                print(".....sucessfully deleted")
            else:
                print(".....there was an error deleting the song")
            print("")
        except:
            print("No song found by that ID Number\n")

        
    @staticmethod
    def __like_song(id: int) -> None:
        Helper.clearscreen()
        response = requests.get(f"http://127.0.0.1:5000/api/songs/{id}")

        try:
            song = Song.song_decoder(response.json())
            print(f"Liking \"{song.title}\" by {song.artist}")

            like_response = requests.put(f"http://127.0.0.1:5000/api/add_like/{id}")

            if like_response.status_code == 200:
                print(".....liked")
            else:
                print(".....there was an error liking the song")
        except:
            print("No song found by that ID Number\n")

    @staticmethod
    def __add_new_song() -> None:
        Helper.clearscreen()
        print("Please enter all requried information:\n")
        valid = False
        title = None
        while (not valid):
            title = input("  Song title: ")
            title = title.strip()
            if title != "":
                valid = True
            else:
                print("Please try again.")
        valid = False
        artist = None
        while (not valid):
            artist = input("      Artist: ")
            artist = artist.strip()
            if artist != "":
                valid = True
            else:
                print("Please try again.")
        valid = False
        album = None
        while (not valid):
            album = input("       Album: ")
            album = album.strip()
            if album != "":
                valid = True
            else:
                print("Please try again.")
        valid = False
        release_date = None
        while (not valid):
            release_date = input("Release Date (YYYY-MM-DD): ")
            release_date = release_date.strip()
            if release_date != "":
                try:
                    date = datetime.strptime(release_date, "%Y-%m-%d")
                    valid = True
                except:
                    print(f"Date unrecognized, please use this format: YYYY-MM-DD, so today would be {datetime.now():%Y-%m-%d}")
            else:
                print("Please try again.")
        valid = False
        genre = None
        while (not valid):
            genre = input("       Genre: ")
            genre = genre.strip()
            if genre != "":
                valid = True
            else:
                print("Please try again.")

        new_song = Song(None, title=title, artist=artist, album=album, release_date=release_date, genre=genre)
        
        
        new_song_json_string = new_song.jsonify_for_insert()
        new_song_json = json.loads(new_song_json_string)
        response = requests.post(f"http://127.0.0.1:5000/api/songs", json=new_song_json)

        if response.status_code == 201:
            song_with_id = Song.song_decoder(response.json())
            print(f"\nSong \"{new_song.title}\" sucessfully added as Song #{song_with_id.id}")
        else:
            print("\nThere was an error adding the song.")


       