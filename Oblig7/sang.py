class Sang:
    def __init__(self, artist, tittel):
        self._artist = artist
        self._tittel = tittel

    def spill(self):
        print(f"Spiller {self._tittel}-{self._artist}")

    def sjekkArtist(self, navn):
        liste = navn.split()
        for x in liste:
            if x in self._artist.split():
                return True
        return False

    def sjekkTittel(self, tittel):
        if self._tittel.lower() == tittel.lower():
            return True
        return False

    def sjekkArtistOgTittel(self, artist, tittel):
        if self.sjekkArtist(artist) and self.sjekkTittel(tittel):
            return True
        return False
