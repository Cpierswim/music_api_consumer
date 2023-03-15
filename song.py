from datetime import datetime

class Song():

    def  __init__(self, id, title, artist, album, release_date, genre, likes ) -> None:
        self.id = id
        self.title = title
        self.artist = artist
        self.album = album
        self.release_date = datetime.strptime(release_date, "%Y-%m-%d")
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