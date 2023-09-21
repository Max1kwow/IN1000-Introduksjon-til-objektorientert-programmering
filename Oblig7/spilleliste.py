from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn


    def lesFraFil(self, filnavn):
        openfile = open(filnavn, "r")
        for linje in openfile:
            line = linje.strip().split(";")
            sang = Sang(line[0],line[1])
            self._sanger.append(sang)
        openfile.close()

    def leggTilSang(self, nySang):
        self._sanger.append(nySang)

    def fjernSang(self, sang):
        self._sanger.remove(sang)

    def spillSang(self, sang):
        sang.spill()

    def spillAlle(self):
        for sang in self._sanger:
            sang.spill()

    def finnSang(self, tittel):
        for x in self._sanger:
            if x.sjekkTittel(tittel):
                return x
        return None

    def hentArtistUtvalg(self, artistnavn):
        list = []
        for x in self._sanger:
            if x.sjekkArtist(artistnavn):
                list.append(x)
        return list
