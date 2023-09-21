def adder(tall1, tall2):
    return tall1+tall2

print(adder(10,20))
print(adder(10,20))

tekstreng = input("Skriv inn en tekststreng: ")
inputbokstav = input("Skriv inn en bokstav: ")

counter = 0
for bokstavitekst in tekstreng: #for index in range(len(tekstreng)):
    if inputbokstav == bokstavitekst:
        counter += 1

print(counter)

def tellForekomst (minTekst, minBokstav):
    counter = 0
    for bokstavitekst in minTekst: #for index in range(len(tekstreng)):
        if minBokstav == bokstavitekst:
            counter += 1
    return counter

def main():
    tekstreng = input("Skriv inn en tekststreng: ")
    inputbokstav = input("Skriv inn en bokstav: ")

    variabel = tellForekomst(tekstreng, inputbokstav)
    print(variabel)

main()
