dag1 = int(input("leser inn to datoer, altså to dager og to måneder: "))
maaned1 = int(input("leser inn to datoer, altså to dager og to måneder: "))
dag2 = int(input("leser inn to datoer, altså to dager og to måneder: "))
maaned2 = int(input("leser inn to datoer, altså to dager og to måneder: "))

if maaned1 < maaned2:
    print("riktig rekkefølge!")
elif maaned2 < maaned1:
    print("Feil rekkefølge!")
else:
    if dag1 == dag2:
        print("Samme dato!")

    elif dag1 > dag2:
        print("Feil rekkefølge!")
    else:
        print("Riktig rekkefølge!")
