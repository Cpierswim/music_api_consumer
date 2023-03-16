from os import system, name
from json import JSONEncoder
import datetime

class Helper():

    DISPLAY_ALL_SONGS = 1
    INFO_BY_ID = 2
    LIKE_BY_ID = 3
    UPDATE_SONG = 4
    ADD_NEW_SONG = 5
    DELETE_BY_ID = 6
    QUIT = 7

    @staticmethod
    def clearscreen():
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
