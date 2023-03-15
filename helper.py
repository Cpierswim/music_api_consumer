from os import system, name

class Helper():

    DISPLAY_ALL_SONGS = 1
    QUIT = 4
    INFO_BY_ID = 2
    DELETE_BY_ID = 3

    @staticmethod
    def clearscreen():
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')