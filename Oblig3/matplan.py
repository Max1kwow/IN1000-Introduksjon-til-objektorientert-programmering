ordbok = {"Jonas":["brød", "melk", "banan"],
        "Tom":["brfed", "eflk", "befnan"],
        "Henrik":["bhrtd", "mtrhlk", "banefefefn"],}

def beboer():
    for x in ordbok:
        print(x)
    navn = input("Skriv navnet til en beboer: ")

    if navn in ordbok:
        print(ordbok[navn][0], ordbok[navn][1], ordbok[navn][2])

    else:
        print("Navnet finnes ikke")
beboer()
