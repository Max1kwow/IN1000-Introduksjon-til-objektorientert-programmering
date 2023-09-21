class Motorsykkel:
    def __init__(self, merke, reg_nummer, km):
        self._merke = merke
        self._reg_nummer = reg_nummer
        self._km = km

    def kjor(self, km):
        self._km += km

    def hentKilometerstand(self):
        return self._km

    def skrivUt(self):
        print(self._merke, self._reg_nummer, self._km)
