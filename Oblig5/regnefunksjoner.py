def addisjon(parameter1, parameter2):
    return parameter1 + parameter2

assert addisjon(2,7) == 9

def subtraksjon(parameter1, parameter2):
    return parameter1 - parameter2

assert subtraksjon(100,50) == 50

def divisjon(parameter1, parameter2):
    return parameter1 / parameter2

assert divisjon(9,3) == 3

def tommer_til_cm(antall_tommer):
    assert antall_tommer > 0
    return antall_tommer * 2.54
tommer_til_cm(10)

def skriv_beregninger():
    inputfrabruk = float(input("Skriv float tall: "))
    inputfrabruk1 = float(input("Skriv float tall: "))
    print(addisjon(inputfrabruk, inputfrabruk1))
    print(subtraksjon(inputfrabruk, inputfrabruk1))
    print(divisjon(inputfrabruk, inputfrabruk1))
    inputfrabruk2 = float(input("Skriv float tall: "))
    print(tommer_til_cm(inputfrabruk2))
skriv_beregninger()
