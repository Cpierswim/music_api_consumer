from os import system, name

class Helper():

    DISPLAY_ALL_SONGS = 1

    @staticmethod
    def display_songs(song_list):
        for song in song_list:
            print(song)

    @staticmethod
    def clearscreen():
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')