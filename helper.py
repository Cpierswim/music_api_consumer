from os import system, name
from json import JSONEncoder
import datetime

class Helper():

    DISPLAY_ALL_SONGS = 1
    INFO_BY_ID = 2
    LIKE_BY_ID = 3
    ADD_NEW_SONG = 4
    DELETE_BY_ID = 5
    QUIT = 6

    @staticmethod
    def clearscreen():
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
