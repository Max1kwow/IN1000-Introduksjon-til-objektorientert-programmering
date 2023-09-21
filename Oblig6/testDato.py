from dato import Dato

def hovedprogram():
    dato = Dato(15,7,1999)
    dato.strengAvDatoen()
    dato.aaret()

    if dato.bestemtDag(15):
        print("Loenningsdag!")
    elif dato.bestemtDag(1):
        print("Ny maaned, nye muligheter")

    dato.lesInnNyDato(15,7,1999)
hovedprogram()
