from datetime import datetime
import json
class Song():

    def  __init__(self, id, title, artist, album, release_date, genre, likes=0 ) -> None:
        self.id = id
        self.title = title
        self.artist = artist
        self.album = album
        if type(isinstance(release_date, str)):
            self.release_date = datetime.strptime(release_date, "%Y-%m-%d")
        else:
            self.release_date = release_date
        self.genre = genre
        self.likes = likes

    @staticmethod
    def song_decoder(obj):
        return Song(obj["id"], obj["title"], obj["artist"], obj["album"], obj["release_date"], obj["genre"], obj["likes"])
    
    def __str__(self) -> str:
        rjustid = "#" + str(self.id)
        rjustid = rjustid.rjust(4)
        ljusttitleandartist = "\"" + self.title + "\", by " + self.artist
        ljusttitleandartist = ljusttitleandartist.ljust(85, ".")
        ljustalbum = "Album: " + self.album
        ljustalbum = ljustalbum.ljust(35)
        custom_date_string = ''
        if self.release_date.day < 10:
            custom_date_string = self.release_date.strftime("%B") + " " + self.release_date.strftime("%d, %Y").removeprefix("0")
        else:
            custom_date_string = self.release_date.strftime("%B %d, %Y")
        return f"{rjustid}: {ljusttitleandartist}{ljustalbum} Released: {custom_date_string} ({self.genre} genre)"
    
    def partial_string(self) -> str:
        rjustid = "#" + str(self.id)
        rjustid = rjustid.rjust(4)
        return f"{rjustid} \"{self.title}\", by {self.artist}"
    
    def jsonify_for_insert(self):
        '''custom_date_string = self.release_date.strftime("%Y-%m-%d")
        json = "{"
        json += f"\"title\":\"{self.title}\","
        json += f"\"artist\":\"{self.artist}\","
        json += f"\"album\":\"{self.album}\","
        json += f"\"release_date\":\"{custom_date_string}\","
        json += f"\"genre\":\"{self.genre}\""
        json += "}"
        return json'''

        dict = {
            "title": self.title,
            "artist": self.artist,
            "album": self.album,
            "release_date": self.release_date.strftime("%Y-%m-%d"), 
            "genre": self.genre
        }

        asJsong =  json.dumps(dict)

        return asJsong