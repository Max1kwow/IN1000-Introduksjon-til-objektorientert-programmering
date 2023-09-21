from random import randint
from celle import Celle

class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = []
        self._generasjon = 1

        for rad in range(self._rader):
            liste = []
            for kolonne in range(self._kolonner):
                celle = Celle()
                liste.append(celle)

            self._rutenett.append(liste)
        self._generer()


    def tegnBrett(self):
        for x in self._rutenett:
            for element in x:
                print(element.hentStatusTegn(), end="")
            print()

    def hent_generasjon(self):
        return self._generasjon

    def oppdatering(self):
        self._generasjon += 1

        doedTilLevende = []
        levendeTilDoed = []

        for radnmr in range(self._rader):
            for kolonnenmr in range(self._kolonner):
                naacelle = self._rutenett[radnmr][kolonnenmr]
                naboliste = self.finnNabo(radnmr, kolonnenmr)
                antallLevende = 0
                for element in naboliste:
                    if element.erLevende():
                        antallLevende += 1
                if naacelle.erLevende():
                    if antallLevende < 2 or antallLevende > 3:
                        levendeTilDoed.append(naacelle)
                elif naacelle.erLevende() == False:
                    if antallLevende == 3:
                        doedTilLevende.append(naacelle)

        for element in doedTilLevende:
            element.settLevende()
        for element in levendeTilDoed:
            element.settDoed()

    def finnAntallLevende(self):
        teller = 0
        for x in self._rutenett:
            for element in x:
                if element.erLevende():
                    teller += 1
        return teller

    def _generer(self) :
        for x in self._rutenett:
            for element in x:
                randomtall = randint(0,2)
                if randomtall == 1:
                    element.settLevende()

    def finnNabo(self, rad, kolonne):
        naboliste = []
        for i in range(-1,2):
            for j in range(-1,2):
                naborad = i + rad
                nabokollone = j + kolonne
                gyldig = True
                if i == 0 and j == 0:
                    gyldig = False

                if naborad == self._rader or naborad < 0:
                    gyldig = False

                if nabokollone == self._kolonner or nabokollone < 0:
                    gyldig = False

                if gyldig == True:
                    naboliste.append(self._rutenett[naborad][nabokollone])
        return naboliste
