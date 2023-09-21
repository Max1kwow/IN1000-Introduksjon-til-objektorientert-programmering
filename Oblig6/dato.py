class Dato:
    def __init__(self, nyDag, nyMaaned, nyttAar):
        self._nyDag = nyDag
        self._nyMaaned = nyMaaned
        self._nyttAar = nyttAar

    def aaret(self):
        return self._nyttAar

    def strengAvDatoen(self):
        print(f"{self._nyDag}.{self._nyMaaned}.{self._nyttAar}")

    def bestemtDag(self, nydag):
        if self._nyDag == nydag:
            return True
        return False

    def lesInnNyDato(self, dag, maaned, aar):
        if aar < self._nyttAar:
            print("Ny dato kommer før dato-objektet")
        elif aar > self._nyttAar:
            print("Ny dato kommer etter")
        else: #aar == self._nyttAar
            if maaned < self._nyMaaned:
                print("Ny dato kommer før dato-objektet")
            elif maaned > self._nyMaaned:
                print("Ny dato kommer etter")
            else:
                if dag < self._nyDag:
                    print("Ny dato kommer før dato-objektet")
                elif dag > self._nyDag:
                    print("Ny dato kommer etter")
                else:
                    print("Samme dato!")
