def antallBokstaver(ord):
    return len(ord)

print(antallBokstaver("Norge"))


def lagOrdbok(setning):
    ordbok = {}
    setning = setning.lower()
    for ord in setning.split(" "):
        if ord in ordbok:
            ordbok[ord] += 1
        else:
            ordbok[ord] = 1
    return ordbok

print(lagOrdbok("Jeg skal reise i sommeren! Jeg skal reise i sommeren!"))


def main():
    inputFraBruker = input("Skriv inn en setning: ")
    antBokstav = len(inputFraBruker.split(" "))
    print(antBokstav)
    nyordbok = lagOrdbok(inputFraBruker)

    for ord in nyordbok:
        print(f"Ord {ord} forekommer {nyordbok[ord]}, ord har {antallBokstaver(ord)}")
main()
