from os import system, name

class Helper():

    DISPLAY_ALL_SONGS = 1
    QUIT = 3
    INFO_BY_ID = 2

    @staticmethod
    def clearscreen():
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')