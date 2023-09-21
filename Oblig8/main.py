from spillebrett import Spillebrett

def main():
    radinp = int(input("Skriv inn antall rader: "))
    kollinp = int(input("Skriv inn antall kolonner: "))


    spillebrett = Spillebrett(radinp, kollinp)
    spillebrett.tegnBrett()
    print(f"Generasjon: {spillebrett.hent_generasjon()} - Antall levende celler: {spillebrett.finnAntallLevende()}")
    svar = input(f"Press enter for aa fortsette. Skriv inn q og trykk enter for aa avslutte: ")
    while svar != "q":
        spillebrett.oppdatering()
        spillebrett.tegnBrett()
        print(f"Generasjon: {spillebrett.hent_generasjon()} - Antall levende celler: {spillebrett.finnAntallLevende()}")
        svar = input(f"Press enter for aa fortsette. Skriv inn q og trykk enter for aa avslutte: ")
main()
