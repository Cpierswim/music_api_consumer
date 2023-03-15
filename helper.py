from os import system, name

class Helper():

    DISPLAY_ALL_SONGS = 1
    INFO_BY_ID = 2
    LIKE_BY_ID = 3
    DELETE_BY_ID = 4
    QUIT = 5

    @staticmethod
    def clearscreen():
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')